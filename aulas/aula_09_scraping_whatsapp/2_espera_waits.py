import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

CHROME_PROFILE_PATH = os.path.abspath("chrome_profile")
ELEMENT_TO_WAIT = "//div[@id='pane-side']"
WAIT_TIME = 120 # 2 minutos

def main():
    try:
        manager = ChromeDriverManager().install()
        options = Options()
        options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
        service = webdriver.chrome.service.Service(manager)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://web.whatsapp.com")

        print("Aguardando elemento do Whatsapp Web ficar visível...")
        wait = WebDriverWait(driver, WAIT_TIME)
        wait.until(EC.presence_of_element_located((
            webdriver.common.by.By.XPATH, 
            ELEMENT_TO_WAIT
        )))
        print("Elemento do Whatsapp Web visível!")
    except Exception as e:
        print(f"Erro ao raspar o Whatsapp Web: {e}")

    input("Pressione Enter para fechar o driver...")
    driver.quit()

if __name__ == "__main__":
    main()
