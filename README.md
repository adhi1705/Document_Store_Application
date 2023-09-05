# Document_Store_Application
# Document Store Application

This is a simple web application that allows users to upload, search, and download files stored in an Amazon S3 bucket. The application is built using Flask, a Python web framework, and uses the Boto3 library to interact with Amazon S3.

## Features

### Upload Feature
- Users can upload files to the S3 bucket.
- Required input fields: Email and Filename.
- File is uploaded with the naming convention: `<email>_<filename>.txt`.
- An alert is displayed upon successful upload.

### Search Feature
- Users can search for files in the S3 bucket.
- Required input fields: Email and Search Query.
- Results are displayed in a list.

### Download Feature
- Users can download files from the S3 bucket.
- Files can be downloaded based on the search results.
- The application determines the content type and file extension for downloaded files.

## Prerequisites
- Python 3.x
- Flask
- Boto3 (for AWS S3 interaction)

## Setup
1. Install Python 3.x on your system.
2. Install Flask and Boto3 using `pip install flask boto3`.
3. Replace the AWS credentials (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_BUCKET_NAME`) in the code with your own credentials.
4. Run the application using `python app.py`.

## Usage
1. Access the application by opening a web browser and navigating to `http://localhost:8001/` (or the public IP of your EC2 instance if deployed).
2. Use the Upload, Search, and Download features as described above.

## Deployment
- To deploy this application on an Amazon EC2 instance, follow the steps mentioned in the provided instructions.

## Author
Adhiyaman A
