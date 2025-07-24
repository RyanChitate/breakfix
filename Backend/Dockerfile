# Use an official Python base image
FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Copy requirements file and install
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Expose port 8000 to the host
EXPOSE 8000

# Command to run when container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
