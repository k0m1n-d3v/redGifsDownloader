import argparse
import os
from browser_manager import BrowserManager
from scraper import RedGifsScraper
from downloader import VideoDownloader
from config import DEFAULT_START_URL, DOWNLOAD_PATH


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='RedGifs Downloader')
    parser.add_argument(
        '--url', 
        type=str, 
        default=DEFAULT_START_URL,
        help='RedGifs user URL to scrape (default: from config)'
    )
    parser.add_argument(
        '--download-path', 
        type=str, 
        default=DOWNLOAD_PATH,
        help='Path to save downloaded videos (default: from config)'
    )
    return parser.parse_args()


def main():
    """Main function to orchestrate the RedGifs downloader."""
    args = parse_arguments()
    
    # Set environment variables for config
    os.environ['REDGIFS_URL'] = args.url
    os.environ['DOWNLOAD_PATH'] = args.download_path
    
    print(f"🎯 URL: {args.url}")
    print(f"📁 Ścieżka pobierania: {args.download_path}")
    
    browser_manager = BrowserManager()
    scraper = None
    downloader = VideoDownloader()
    
    try:
        # Initialize browser
        driver = browser_manager.initialize_browser()
        scraper = RedGifsScraper(driver)
        
        # Scrape thumbnail links
        thumbnail_links = scraper.scroll_and_collect_thumbnails(args.url)
        
        # Extract video links
        video_links = scraper.extract_video_links(thumbnail_links)
        
        # Download videos
        downloader.download_videos(video_links, args.url)
        
    except Exception as e:
        print(f"❌ Wystąpił błąd: {e}")
    finally:
        # Clean up browser
        browser_manager.close_browser()


if __name__ == "__main__":
    main()