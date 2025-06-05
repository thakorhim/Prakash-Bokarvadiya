from flask import Flask, request, render_template, send_file, jsonify
import os
import torch
from TTS.api import TTS
import soundfile as sf
import librosa
import numpy as np
from scipy.io import wavfile
from threading import Thread

# Global variable to track progress
processing_progress = 0

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/progress')
def get_progress():
    return jsonify({'progress': processing_progress})

@app.route('/upload', methods=['POST'])
def upload_file():
    global processing_progress
    if 'voice_file' not in request.files:
        processing_progress = -1
        return jsonify({'error': 'No file uploaded. Please select a voice file.', 'status': 'error'}), 400
    
    file = request.files['voice_file']
    text = request.form.get('text', '')
    
    if file.filename == '':
        processing_progress = -1
        return jsonify({'error': 'No selected file. Please choose a voice file.', 'status': 'error'}), 400
    
    if not text.strip():
        processing_progress = -1
        return jsonify({'error': 'Text is required. Please enter the text you want to convert to speech.', 'status': 'error'}), 400
    
    # Validate file type
    allowed_extensions = {'wav', 'mp3'}
    if not file.filename.lower().endswith(tuple(allowed_extensions)):
        processing_progress = -1
        return jsonify({'error': 'Invalid file type. Only WAV and MP3 files are allowed.', 'status': 'error'}), 400
    
    processing_progress = 0
    
    try:
        # Save uploaded file
        input_path = os.path.join(UPLOAD_FOLDER, 'input_voice.wav')
        output_path = os.path.join(OUTPUT_FOLDER, 'cloned_voice.wav')
        file.save(input_path)
        
        # Start processing in a separate thread
        thread = Thread(target=process_voice_cloning, args=(input_path, output_path, text))
        thread.start()
        
        return jsonify({'message': 'Processing started successfully', 'status': 'success'})
    except Exception as e:
        processing_progress = -1
        print(f"Error during file upload: {str(e)}")
        return jsonify({'error': f'Failed to process the upload: {str(e)}', 'status': 'error'}), 500

def process_voice_cloning(input_path, output_path, text):
    global processing_progress
    try:
        processing_progress = 10
        # Initialize TTS with the appropriate model
        tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts",
                  progress_bar=False,
                  gpu=torch.cuda.is_available())
        
        processing_progress = 30
        # Validate input audio file
        try:
            audio_data, sample_rate = librosa.load(input_path)
            if len(audio_data) < sample_rate:  # Less than 1 second
                processing_progress = -1
                error_msg = "Audio file is too short. Please provide a recording of at least 1 second."
                print(error_msg)
                return False
            if len(audio_data) > 30 * sample_rate:  # More than 30 seconds
                processing_progress = -1
                error_msg = "Audio file is too long. Please provide a recording of maximum 30 seconds."
                print(error_msg)
                return False
        except Exception as e:
            processing_progress = -1
            error_msg = f"Error reading audio file: {str(e)}. Please ensure the file is not corrupted."
            print(error_msg)
            return False
        
        processing_progress = 50
        # Generate speech with voice cloning
        try:
            tts.tts_to_file(text=text,
                            file_path=output_path,
                            speaker_wav=input_path)
            processing_progress = 100
            return True
        except Exception as e:
            processing_progress = -1
            error_msg = f"Error in voice synthesis: {str(e)}. Please try with a different voice sample or shorter text."
            print(error_msg)
            return False
            
    except Exception as e:
        processing_progress = -1
        error_msg = f"Error in voice cloning process: {str(e)}. Please try again later."
        print(error_msg)
        return False

@app.route('/download')
def download_file():
    if processing_progress != 100:
        return 'Processing not complete', 400
    
    output_path = os.path.join(OUTPUT_FOLDER, 'cloned_voice.wav')
    if not os.path.exists(output_path):
        return 'File not found', 404
    
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)