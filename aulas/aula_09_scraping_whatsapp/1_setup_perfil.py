import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

CHROME_PROFILE_PATH = os.path.abspath("chrome_profile")

def main():
    manager = ChromeDriverManager().install()
    options = Options()
    options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
    service = webdriver.chrome.service.Service(manager)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://web.whatsapp.com")
    input("Pressione Enter para fechar o driver...")
    driver.quit()

if __name__ == "__main__":
    main()
