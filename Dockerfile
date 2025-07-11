FROM python:3.11-slim

# Install system dependencies and Chromium
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set Chrome binary path for undetected-chromedriver
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Install yt-dlp globally
RUN pip install yt-dlp

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create downloads directory
RUN mkdir -p /downloads

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DOWNLOAD_PATH=/downloads

# Run the application
ENTRYPOINT ["python", "main.py"] 