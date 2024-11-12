# Use a base Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file (if you have additional dependencies)
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files to the container
COPY . .

# Expose port 8080
EXPOSE 8080

# Command to run the Flask app
CMD ["python", "Hour.py"]
