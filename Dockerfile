# Base image
FROM python:3.9-slim

# Work dir
WORKDIR /app

# Cpy the code of the app in the container 
COPY . .

# Install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Open app port
EXPOSE 5000

# Start application with command
CMD ["python", "simple_app.py"]