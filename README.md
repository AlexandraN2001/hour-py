# Hour-Py Docker App 🌐
Hour-Py is a simple web application built with Flask in Python. It responds with a message displaying the current date and time in the format:
Hello, World! Current time is: YYYY-MM-DD HH:MM:SS.

This application is containerized with Docker, making it easy to deploy across various environments. 🚀
# Deployment on Docker Hub 🌍
The Dockerized version of this app is available on Docker Hub:

👉 alenac07/python
# Project Structure 📁
The project structure is as follows:

hour-py/

├── Dockerfile           # Dockerfile to build the container image

├── README.md            # Project documentation

├── app.py               # Main Flask application code

├── requirements.txt     # Python dependencies for the app

# Requirements 📋
To run this project locally or with Docker, you will need:
## Python 🐍
Version 3.7 or higher.
## Flask
Specified in the requirements.txt file.
## Docker 🐳
To run the containerized app.
## Git
To clone the repository.
# How to Clone and Run
## Step 1: Clone the Repository
Clone the repository using:

git clone https://github.com/alenac07/hour-py.git

cd hour-py

# Step 2: Install Dependencies and Run Locally
If you want to run the application locally:
1. Make sure Python is installed.
2. Install the dependencies listed in requirements.txt

pip install -r requirements.txt

4. Run the application:
   
python app.py

The application will be available at:

👉 http://localhost:5000

# Deploying with Docker 🚀
## Step 1: Pull the Image

Download the Docker image from Docker Hub

docker pull alenac07/python:latest

## Step 2: Run the Container

Run the container with the following command:

docker run -d -p 5000:5000 alenac07/python:latest

## Step 3: Access the Application
Open your browser and go to:

👉 http://localhost:5000

You will see a message like this:

Hello, World! Current time is: YYYY-MM-DD HH:MM:SS
# Docker Hub 📦
Find the Dockerized version of the project on Docker Hub:

👉 Docker Hub: https://hub.docker.com/r/alenac07/python  

# Notes 📝
-This project is ideal for exploring Flask and Docker in basic projects.
-You can easily customize the application or add new routes in the app.py file.
-It’s a lightweight and portable solution for web applications built with Flask.
