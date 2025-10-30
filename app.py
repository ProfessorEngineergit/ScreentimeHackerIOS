#!/usr/bin/env python3
"""
ScreenTime Hacker iOS - Web Application
Extract screen time passcode from iPhone backup files for educational purposes.
"""

import os
import hashlib
import struct
import plistlib
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = '/tmp/uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'plist', 'log', 'db', 'sqlite'}


def allowed_file(filename):
    """Check if file has allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_screentime_code(file_path):
    """
    Extract screen time passcode from iPhone backup file.
    
    The screen time passcode is stored in the restrictions plist file.
    This function attempts to extract and crack the passcode hash.
    
    Args:
        file_path: Path to the backup file
        
    Returns:
        dict: Result containing success status and passcode or error message
    """
    try:
        # Try to parse as plist file
        with open(file_path, 'rb') as f:
            try:
                plist_data = plistlib.load(f)
            except Exception:
                # If not a valid plist, try reading as text
                f.seek(0)
                content = f.read()
                return {'success': False, 'error': 'File format not recognized. Please upload a valid backup file.'}
        
        # Look for screen time related keys
        # Common keys: RestrictionsPasswordKey, RestrictionsPasswordSalt
        if 'RestrictionsPasswordKey' in plist_data and 'RestrictionsPasswordSalt' in plist_data:
            password_key = plist_data['RestrictionsPasswordKey']
            password_salt = plist_data['RestrictionsPasswordSalt']
            
            # Brute force the passcode (only 0000-9999 for 4-digit codes)
            passcode = brute_force_passcode(password_key, password_salt)
            
            if passcode:
                return {
                    'success': True,
                    'passcode': passcode,
                    'message': 'Screen time passcode successfully extracted!'
                }
            else:
                return {
                    'success': False,
                    'error': 'Could not crack the passcode. It might be longer than 4 digits.'
                }
        else:
            return {
                'success': False,
                'error': 'No screen time passcode data found in this file. Please upload the correct backup file (usually named com.apple.springboard.plist or similar).'
            }
            
    except Exception as e:
        return {
            'success': False,
            'error': f'Error processing file: {str(e)}'
        }


def brute_force_passcode(password_key, password_salt):
    """
    Brute force the screen time passcode.
    
    Args:
        password_key: The hashed password key from the plist
        password_salt: The salt used for hashing
        
    Returns:
        str: The passcode if found, None otherwise
    """
    # Try 4-digit codes (0000-9999)
    for code in range(10000):
        passcode = f"{code:04d}"
        
        # Create the hash using the same method iOS uses
        # iOS uses PBKDF2 with HMAC-SHA1
        test_hash = hashlib.pbkdf2_hmac(
            'sha1',
            passcode.encode('utf-8'),
            password_salt,
            1000  # iOS uses 1000 iterations
        )
        
        if test_hash == password_key:
            return passcode
    
    # Try 6-digit codes (000000-999999) if 4-digit didn't work
    for code in range(1000000):
        passcode = f"{code:06d}"
        
        test_hash = hashlib.pbkdf2_hmac(
            'sha1',
            passcode.encode('utf-8'),
            password_salt,
            1000
        )
        
        if test_hash == password_key:
            return passcode
    
    return None


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and extract passcode."""
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file uploaded'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extract the passcode
        result = extract_screentime_code(filepath)
        
        # Clean up the uploaded file
        try:
            os.remove(filepath)
        except Exception:
            pass
        
        return jsonify(result)
    
    return jsonify({'success': False, 'error': 'Invalid file type. Please upload a .plist, .log, .db, or .sqlite file.'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
