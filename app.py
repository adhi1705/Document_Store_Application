import io
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import os
import boto3

app = Flask(__name__)
AWS_ACCESS_KEY_ID = 'AKIASVFBKVWARUOMP2KH'
AWS_SECRET_ACCESS_KEY = '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'
AWS_BUCKET_NAME = 'myadhibucket'

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'email' in request.form and 'filename' in request.form and 'file' in request.files:
        email = request.form['email']
        filename = request.form['filename']
        file = request.files['file']
        s3_filename = f'{email}_{filename}'
        s3.upload_fileobj(file, AWS_BUCKET_NAME, s3_filename)

        flash('File uploaded successfully', 'success')
    else:
        flash('Please fill in all fields', 'error')
    
    return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search_files():
    email = request.form['email']
    search_query = request.form['search_query']
    objects = s3.list_objects_v2(Bucket=AWS_BUCKET_NAME, Prefix=f'{email}_{search_query}')
    results = [{'key': obj['Key'], 'file_name': obj['Key']} for obj in objects.get('Contents', [])]

    return render_template('search_results.html', files=results)

@app.route('/download/<path:key>')
def download_file(key):
    bucket_name="myadhibucket"
    file_obj = s3.get_object(Bucket=bucket_name, Key=key)
    # Get the file data and content type
    file_data = file_obj['Body'].read()
    content_type = file_obj['ContentType']
    print(content_type)
    # Send the file as a response
    return send_file(
        io.BytesIO(file_data),
        mimetype=content_type,
        as_attachment=True,
        download_name=key.split(' ')[-1]+'.docx'
    )
if __name__ == '__main__':
    app.secret_key = 'adrandomkeyhi'
    app.run(debug=True, port=8001)