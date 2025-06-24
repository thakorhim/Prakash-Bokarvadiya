from flask import Flask, request, jsonify
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Error handler for all exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"An error occurred: {str(e)}")
    return jsonify(error=str(e)), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status='healthy'), 200

if __name__ == '__main__':
    try:
        # Run the Flask application
        app.run(
            host='0.0.0.0',  # Listen on all available interfaces
            port=5000,        # Port 5000 is commonly used for Flask
            debug=False       # Disable debug mode for production
        )
    except Exception as e:
        logger.critical(f"Failed to start the server: {str(e)}")