from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image
import os
import fitz  # PyMuPDF
from docx import Document
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['EXTRACTED_DATA'] = {}  # Store extracted data

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return ""

def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Error extracting text from pdf: {e}")
        return ""

def extract_text_from_docx(docx_path):
    try:
        doc = Document(docx_path)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return text
    except Exception as e:
        print(f"Error extracting text from docx: {e}")
        return ""

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            file.save(file_path)
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext in ['.png', '.jpg', '.jpeg', '.tiff', '.bmp']:
                text = extract_text_from_image(file_path)
            elif file_ext == '.pdf':
                text = extract_text_from_pdf(file_path)
            elif file_ext == '.docx':
                text = extract_text_from_docx(file_path)
            else:
                return jsonify({'error': 'Unsupported file type'}), 400
            
            # Store extracted text in the app config dictionary
            app.config['EXTRACTED_DATA'][filename] = text
            
            # Create a mock auto-fill response using extracted text
            auto_fill_data = {
                "name": extract_info_from_text(text, "Name"),
                "address": extract_info_from_text(text, "Address"),
                # Add other fields as needed
            }
            
            if text:
                return jsonify({'extracted_text': text, 'auto_fill_data': auto_fill_data})
            else:
                return jsonify({'error': 'Failed to extract text from document'}), 500
        except Exception as e:
            print(f"Error saving file: {e}")
            return jsonify({'error': 'Failed to save file'}), 500

def extract_info_from_text(text, field_name):
    # A mock function to simulate extracting specific fields
    # Replace this with your actual extraction logic
    if field_name.lower() in text.lower():
        return text.lower().split(field_name.lower())[1].split("\n")[0].strip()
    return ""

if __name__ == '__main__':
    app.run(debug=True)