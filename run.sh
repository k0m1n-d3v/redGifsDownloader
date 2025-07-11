#!/bin/bash

# RedGifs Downloader - Docker Runner Script

# Default values
DEFAULT_URL="https://www.redgifs.com/users/local-sperm-bank"
DEFAULT_DOWNLOAD_PATH="./downloads"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Parse command line arguments
URL=${1:-$DEFAULT_URL}
DOWNLOAD_PATH=${2:-$DEFAULT_DOWNLOAD_PATH}

# Validate URL
if [[ ! $URL =~ ^https://www\.redgifs\.com/users/ ]]; then
    print_error "Invalid RedGifs URL. Must be in format: https://www.redgifs.com/users/username"
    exit 1
fi

# Create download directory if it doesn't exist
if [ ! -d "$DOWNLOAD_PATH" ]; then
    print_info "Creating download directory: $DOWNLOAD_PATH"
    mkdir -p "$DOWNLOAD_PATH"
fi

# Get absolute path for download directory
DOWNLOAD_PATH=$(realpath "$DOWNLOAD_PATH")

print_info "Starting RedGifs Downloader with undetected-chromedriver"
print_info "URL: $URL"
print_info "Download path: $DOWNLOAD_PATH"

# Export environment variables for docker-compose
export REDGIFS_URL="$URL"
export DOWNLOAD_PATH="$DOWNLOAD_PATH"

# Run with docker-compose
docker-compose up --build

print_info "Download completed! Check $DOWNLOAD_PATH for downloaded files." 