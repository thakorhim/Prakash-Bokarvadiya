# Storage module for handling file operations and logging
# This module manages data persistence and transaction logging

import json
import logging
from datetime import datetime

class Storage:
    """Class to handle data storage and logging operations"""
    def __init__(self, filename='stock.json'):
        # Initialize storage with filename
        self.filename = filename
        self.setup_logging()

    def setup_logging(self):
        """Configure logging system for transaction tracking"""
        logging.basicConfig(
            filename='transactions.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def load_data(self):
        """Load data from JSON file, return empty dict if file not found"""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self, data):
        """Save data to JSON file with proper formatting"""
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
        
    def log_transaction(self, message):
        """Log a transaction with timestamp"""
        logging.info(message)