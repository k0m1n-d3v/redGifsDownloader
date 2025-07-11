import os

# Configuration settings for RedGifs downloader

# Browser settings
BROWSER_OPTIONS = [
    '--no-sandbox',
    '--disable-blink-features=AutomationControlled',
    '--window-size=1920,1080',
    '--disable-dev-shm-usage',
    '--disable-gpu',
    '--headless',
    '--disable-web-security',
    '--disable-features=VizDisplayCompositor',
    '--disable-extensions',
    '--disable-plugins',
    '--disable-images',  # Disable images for faster loading
]

# Scraping settings
MAX_SCROLLS = int(os.getenv('MAX_SCROLLS', '200'))
SCROLL_DELAY = int(os.getenv('SCROLL_DELAY', '2'))  # seconds
PAGE_LOAD_DELAY = int(os.getenv('PAGE_LOAD_DELAY', '3'))  # seconds

# CSS selectors
THUMBNAIL_SELECTOR = 'a.tile.isVideo[href*="/watch/"]'
VIDEO_LINK_SELECTOR = 'a[href*="/watch/"]'

# Environment-based configuration
DEFAULT_START_URL = os.getenv('REDGIFS_URL', "")
DOWNLOAD_PATH = os.getenv('DOWNLOAD_PATH', './downloads') 