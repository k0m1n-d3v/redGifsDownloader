import subprocess
import os
from typing import Set
from config import DOWNLOAD_PATH


class VideoDownloader:
    """Handles video downloading using yt-dlp."""
    
    def __init__(self):
        self.downloaded_count = 0
        self.failed_count = 0
        self._ensure_download_directory()
    
    def _ensure_download_directory(self):
        """Ensure the download directory exists."""
        os.makedirs(DOWNLOAD_PATH, exist_ok=True)
        print(f"📁 Pliki będą zapisywane w: {DOWNLOAD_PATH}")
    
    def download_videos(self, video_links: Set[str]) -> None:
        """Download all videos from the provided links."""
        print(f"Znaleziono {len(video_links)} filmów.")
        
        for idx, url in enumerate(sorted(video_links), 1):
            print(f"Pobieram {idx}/{len(video_links)}: {url}")
            if self._download_single_video(url):
                self.downloaded_count += 1
            else:
                self.failed_count += 1
        
        self._print_summary()
    
    def _download_single_video(self, url: str) -> bool:
        """Download a single video and return success status."""
        try:
            subprocess.run([
                "yt-dlp", 
                url,
                "-o", f"{DOWNLOAD_PATH}/%(title)s.%(ext)s",
                "--no-check-certificates"
            ], check=True)
            return True
        except subprocess.CalledProcessError:
            print(f"❌ Błąd podczas pobierania: {url}")
            return False
    
    def _print_summary(self) -> None:
        """Print download summary."""
        print(f"\n📊 Podsumowanie:")
        print(f"✅ Pobrano: {self.downloaded_count}")
        print(f"❌ Błędów: {self.failed_count}")
        print(f"📁 Lokalizacja: {DOWNLOAD_PATH}")
        print("\n🎉 Gotowe!") 