# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the Flask application on port 5002
EXPOSE 5002

# Run the application
CMD ["python", "app.py"]
