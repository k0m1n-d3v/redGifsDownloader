import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import MAX_SCROLLS, SCROLL_DELAY, PAGE_LOAD_DELAY, THUMBNAIL_SELECTOR, VIDEO_LINK_SELECTOR


class RedGifsScraper:
    """Handles scraping of RedGifs user pages and video links."""
    
    def __init__(self, driver):
        self.driver = driver
    
    def scroll_and_collect_thumbnails(self, start_url):
        """Scroll through the user page and collect all thumbnail links."""
        self.driver.get(start_url)
        time.sleep(PAGE_LOAD_DELAY)
        
        seen_links = set()
        
        for i in range(MAX_SCROLLS):
            previous_count = len(seen_links)
            thumbnails = self.driver.find_elements(By.CSS_SELECTOR, THUMBNAIL_SELECTOR)
            
            for thumb in thumbnails:
                href = thumb.get_attribute("href")
                if href and "/watch/" in href:
                    seen_links.add(href)
            
            current_count = len(seen_links)
            print(f"🔄 Scroll {i+1}/{MAX_SCROLLS} — linków: {current_count}")
            
            if current_count == previous_count:
                print("⏹️ Brak nowych filmów — koniec scrollowania.")
                break
            
            if thumbnails:
                ActionChains(self.driver).move_to_element(thumbnails[-1]).perform()
            else:
                self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
            
            time.sleep(SCROLL_DELAY)
        
        print(f"✅ Zebrano {len(seen_links)} unikalnych linków do filmów.")
        return seen_links
    
    def extract_video_links(self, thumbnail_links):
        """Extract direct video links from thumbnail pages."""
        video_links_to_download = set()
        
        for idx, link in enumerate(sorted(thumbnail_links), 1):
            print(f"\n➡️ [{idx}/{len(thumbnail_links)}] Przetwarzam {link}")
            self.driver.get(link)
            time.sleep(PAGE_LOAD_DELAY)
            
            anchors = self.driver.find_elements(By.CSS_SELECTOR, VIDEO_LINK_SELECTOR)
            for anchor in anchors:
                video_links_to_download.add(anchor.get_attribute("href"))
        
        return video_links_to_download 