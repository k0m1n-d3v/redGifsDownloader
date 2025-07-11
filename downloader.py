import subprocess
import os
import re
from typing import Set
from config import DOWNLOAD_PATH


class VideoDownloader:
    """Handles video downloading using yt-dlp."""
    
    def __init__(self):
        self.downloaded_count = 0
        self.failed_count = 0
        self._ensure_download_directory()
    
    def _extract_username_from_url(self, url: str) -> str:
        """Extract username from RedGifs URL."""
        # Pattern to match /users/username in the URL
        pattern = r'/users/([^/?]+)'
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        else:
            # Fallback: use a default name if pattern doesn't match
            return "unknown_user"
    
    def _get_user_download_path(self, url: str) -> str:
        """Get the download path for a specific user."""
        username = self._extract_username_from_url(url)
        user_path = os.path.join(DOWNLOAD_PATH, username)
        os.makedirs(user_path, exist_ok=True)
        return user_path
    
    def _ensure_download_directory(self):
        """Ensure the download directory exists."""
        os.makedirs(DOWNLOAD_PATH, exist_ok=True)
        print(f"📁 Pliki będą zapisywane w: {DOWNLOAD_PATH}")
    
    def download_videos(self, video_links: Set[str], source_url: str = None) -> None:
        """Download all videos from the provided links."""
        print(f"Znaleziono {len(video_links)} filmów.")
        
        # Get user-specific download path
        user_download_path = self._get_user_download_path(source_url) if source_url else DOWNLOAD_PATH
        print(f"📁 Pobieram do folderu użytkownika: {user_download_path}")
        
        for idx, url in enumerate(sorted(video_links), 1):
            print(f"Pobieram {idx}/{len(video_links)}: {url}")
            if self._download_single_video(url, user_download_path):
                self.downloaded_count += 1
            else:
                self.failed_count += 1
        
        self._print_summary(user_download_path)
    
    def _download_single_video(self, url: str, download_path: str) -> bool:
        """Download a single video and return success status."""
        try:
            subprocess.run([
                "yt-dlp", 
                url,
                "-o", f"{download_path}/%(title)s.%(ext)s",
                "--no-check-certificates"
            ], check=True)
            return True
        except subprocess.CalledProcessError:
            print(f"❌ Błąd podczas pobierania: {url}")
            return False
    
    def _print_summary(self, download_path: str) -> None:
        """Print download summary."""
        print(f"\n📊 Podsumowanie:")
        print(f"✅ Pobrano: {self.downloaded_count}")
        print(f"❌ Błędów: {self.failed_count}")
        print(f"📁 Lokalizacja: {download_path}")
        print("\n🎉 Gotowe!") 