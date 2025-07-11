import undetected_chromedriver as uc
import os
from config import BROWSER_OPTIONS


class BrowserManager:
    """Manages browser initialization and configuration."""
    
    def __init__(self):
        self.driver = None
    
    def initialize_browser(self):
        """Initialize and configure the Chrome browser using undetected_chromedriver."""
        options = uc.ChromeOptions()
        for option in BROWSER_OPTIONS:
            options.add_argument(option)
        
        # Set Chrome binary path if available
        chrome_bin = os.getenv('CHROME_BIN')
        if chrome_bin and os.path.exists(chrome_bin):
            options.binary_location = chrome_bin
            print(f"Using Chrome binary: {chrome_bin}")
        
        # Set ChromeDriver path if available
        chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
        if chromedriver_path and os.path.exists(chromedriver_path):
            print(f"Using ChromeDriver: {chromedriver_path}")
            self.driver = uc.Chrome(
                options=options,
                driver_executable_path=chromedriver_path
            )
        else:
            # Use undetected_chromedriver for better bot detection avoidance
            self.driver = uc.Chrome(options=options)
        
        return self.driver
    
    def close_browser(self):
        """Close the browser and clean up resources."""
        if self.driver:
            self.driver.quit()
            self.driver = None
    
    def navigate_to(self, url):
        """Navigate to a specific URL."""
        if self.driver:
            self.driver.get(url) 