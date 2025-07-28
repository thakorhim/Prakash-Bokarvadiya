from flask import Flask, render_template, request, send_file, jsonify
from yt_dlp import YoutubeDL
import os
import sys
from pathlib import Path
from queue import Queue
from threading import Thread
import time

app = Flask(__name__)
DOWNLOAD_FOLDER = 'downloads'

# Configure FFmpeg path
FFMPEG_PATH = Path('C:/ffmpeg/bin/ffmpeg.exe')
if not FFMPEG_PATH.exists():
    ffmpeg_env = os.getenv('FFMPEG_PATH')
    if ffmpeg_env:
        FFMPEG_PATH = Path(ffmpeg_env)

if FFMPEG_PATH.exists():
    os.environ['PATH'] = f"{FFMPEG_PATH.parent};{os.environ['PATH']}"
else:
    print('Warning: FFmpeg not found. Please install FFmpeg and set the correct path.')
    print('Expected location:', FFMPEG_PATH)

# Error messages
ERROR_MESSAGES = {
    'FFmpeg not found': 'FFmpeg is not installed or configured properly. Please check the installation.',
    'Video unavailable': 'The video is unavailable or restricted. Please check the URL.',
    'Network error': 'Network connection error. Please check your internet connection.',
    'Invalid URL': 'Please provide a valid YouTube URL.',
    'Download error': 'Failed to download the video. Please try again later.',
}

# Global variables to store download progress and queue
download_progress = 0
download_queue = Queue()
active_downloads = {}
queue_thread = None

def progress_hook(d):
    if d['status'] == 'downloading':
        # Extract percentage and update progress for specific download
        video_id = d.get('info_dict', {}).get('id', '')
        percentage = d.get('_percent_str', '0%').replace('%', '')
        try:
            progress = float(percentage)
            if video_id in active_downloads:
                active_downloads[video_id]['progress'] = progress
        except ValueError:
            if video_id in active_downloads:
                active_downloads[video_id]['progress'] = 0
        print(f'Downloading {video_id}: {percentage}%', flush=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/progress')
def get_progress():
    queue_size = download_queue.qsize()
    downloads = [{
        'video_id': video_id,
        'title': info['title'],
        'progress': info['progress'],
        'status': info['status']
    } for video_id, info in active_downloads.items()]
    
    return jsonify({
        'queue_size': queue_size,
        'downloads': downloads
    })

def process_download_queue():
    while True:
        try:
            download_info = download_queue.get()
            if download_info is None:  # Shutdown signal
                break
                
            url = download_info['url']
            format_type = download_info['format']
            video_id = download_info['video_id']
            
            try:
                # Update status to downloading
                active_downloads[video_id]['status'] = 'downloading'
                
                with YoutubeDL({'quiet': True}) as ydl:
                    info = ydl.extract_info(url, download=False)
                    active_downloads[video_id]['title'] = info['title']
                
                # Configure download options
                ydl_opts = get_download_options(format_type)
                ydl_opts['progress_hooks'] = [progress_hook]
                
                # Start download
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                # Update status to completed
                active_downloads[video_id]['status'] = 'completed'
                active_downloads[video_id]['progress'] = 100
                
            except Exception as e:
                print(f"Error downloading {url}: {str(e)}")
                active_downloads[video_id]['status'] = 'error'
                active_downloads[video_id]['error'] = str(e)
            
            # Remove from active downloads after some time
            time.sleep(5)  # Keep status visible for 5 seconds
            if video_id in active_downloads:
                del active_downloads[video_id]
                
        except Exception as e:
            print(f"Queue processing error: {str(e)}")
        finally:
            download_queue.task_done()

def get_download_options(format_type):
    base_opts = {
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'noplaylist': True,
        'quiet': False,
        'cookies-from-browser': 'chrome',
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        },
        'buffersize': 1024 * 16,
        'concurrent_fragment_downloads': 8,
        'retries': 10,
        'fragment_retries': 10,
        'file_access_retries': 10,
        'extractor_retries': 10,
        'socket_timeout': 30,
    }
    
    if format_type == 'mp3':
        return {
            **base_opts,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    elif format_type == 'mp4-hd':
        return {
            **base_opts,
            'format': 'bestvideo[ext=mp4][height>=720]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'merge_output_format': 'mp4',
        }
    else:
        return {
            **base_opts,
            'format': 'best[ext=mp4]',
        }

@app.route('/download', methods=['POST'])
def download():
    try:
        # Reset progress for new download
        global download_progress
        download_progress = 0
        
        url = request.form['url']
        format_type = request.form['format']
        
        # First check if we can get video info without downloading
        with YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            video_title = info['title']
            
            # Prepare expected filename
            expected_filename = os.path.join(DOWNLOAD_FOLDER, f"{video_title}.{'mp3' if format_type == 'mp3' else 'mp4'}")
            
            # If file already exists, send it directly
            if os.path.exists(expected_filename):
                return send_file(
                    expected_filename,
                    as_attachment=True,
                    download_name=os.path.basename(expected_filename)
                )
        
        # Base options for both formats with optimized download settings
        base_opts = {
            'progress_hooks': [progress_hook],
            'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
            'nocheckcertificate': True,
            'noplaylist': True,
            'quiet': False,
            'cookies-from-browser': 'chrome',  # Use browser cookies for authentication
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9',
            },
            'buffersize': 1024 * 16,  # Increased buffer size for faster downloads
            'concurrent_fragment_downloads': 8,  # Increased concurrent downloads
            'retries': 10,  # Increased retry attempts
            'fragment_retries': 10,  # Increased fragment retry attempts
            'file_access_retries': 10,  # Increased file access retry attempts
            'extractor_retries': 10,  # Increased extractor retry attempts
            'socket_timeout': 30,  # Increased socket timeout
        }
        
        if format_type == 'mp3':
            ydl_opts = {
                **base_opts,
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        elif format_type == 'mp4-hd':  # HD MP4
            ydl_opts = {
                **base_opts,
                'format': 'bestvideo[ext=mp4][height>=720]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'merge_output_format': 'mp4',
            }
        else:  # Standard MP4
            ydl_opts = {
                **base_opts,
                'format': 'best[ext=mp4]',
            }

        # Create downloads directory if it doesn't exist
        if not os.path.exists(DOWNLOAD_FOLDER):
            os.makedirs(DOWNLOAD_FOLDER)

        # Download the video
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            # Adjust filename for mp3
            if format_type == 'mp3':
                filename = filename.rsplit('.', 1)[0] + '.mp3'

        # Send the file to user
        return send_file(
            filename,
            as_attachment=True,
            download_name=os.path.basename(filename)
        )

    except Exception as e:
        error_message = str(e)
        print(f"Download error: {error_message}")
        
        # Map common error messages to user-friendly messages
        user_message = ERROR_MESSAGES.get('Download error')
        if 'ffmpeg' in error_message.lower():
            user_message = ERROR_MESSAGES['FFmpeg not found']
        elif 'video unavailable' in error_message.lower():
            user_message = ERROR_MESSAGES['Video unavailable']
        elif 'network' in error_message.lower() or 'connection' in error_message.lower():
            user_message = ERROR_MESSAGES['Network error']
        elif 'invalid url' in error_message.lower():
            user_message = ERROR_MESSAGES['Invalid URL']
            
        return jsonify({
            'error': True,
            'message': user_message,
            'details': str(error_message)
        }), 400

@app.route('/batch-download', methods=['POST'])
def batch_download():
    try:
        urls = request.form.getlist('urls[]')
        format_type = request.form.get('format', 'mp3')
        
        if not urls:
            return jsonify({
                'error': True,
                'message': 'No URLs provided'
            }), 400
        
        # Create downloads directory if it doesn't exist
        if not os.path.exists(DOWNLOAD_FOLDER):
            os.makedirs(DOWNLOAD_FOLDER)
        
        # Start queue processing thread if not already running
        global queue_thread
        if queue_thread is None or not queue_thread.is_alive():
            queue_thread = Thread(target=process_download_queue, daemon=True)
            queue_thread.start()
        
        # Add each URL to the download queue
        for url in urls:
            try:
                # Extract video ID from URL
                with YoutubeDL({'quiet': True}) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_id = info['id']
                    
                # Add to active downloads with initial status
                active_downloads[video_id] = {
                    'title': info['title'],
                    'progress': 0,
                    'status': 'queued'
                }
                
                # Add to download queue
                download_queue.put({
                    'url': url,
                    'format': format_type,
                    'video_id': video_id
                })
                
            except Exception as e:
                print(f"Error processing URL {url}: {str(e)}")
                return jsonify({
                    'error': True,
                    'message': f'Error processing URL: {str(e)}'
                }), 400
        
        return jsonify({
            'message': f'Added {len(urls)} videos to download queue',
            'queue_size': download_queue.qsize()
        })
        
    except Exception as e:
        return jsonify({
            'error': True,
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)