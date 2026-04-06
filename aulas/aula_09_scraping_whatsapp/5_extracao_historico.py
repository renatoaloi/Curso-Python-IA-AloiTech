import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

CONTACT_NAME = "Páscoa"

CHROME_PROFILE_PATH = os.path.abspath("chrome_profile")
ELEMENT_TO_WAIT = "//div[@id='pane-side']"
WAIT_TIME = 120 # 2 minutos
SEARCH_BOX_XPATH = "//input[@aria-label='Pesquisar ou começar uma nova conversa']"
SELECT_CONTACT_XPATH = "//span[contains(@class, 'matched-text')]"

PANEL_SIDE = "//*[@id='pane-side']"

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

        search_box = driver.find_element(webdriver.common.by.By.XPATH, SEARCH_BOX_XPATH)
        search_box.click()
        search_box.send_keys(webdriver.common.keys.Keys.CONTROL + "a")
        search_box.send_keys(webdriver.common.keys.Keys.BACKSPACE)
        time.sleep(0.5)
        for c in CONTACT_NAME:
            search_box.send_keys(c)
            time.sleep(0.1)
        time.sleep(1)

        panel_side = driver.find_element(webdriver.common.by.By.XPATH, PANEL_SIDE)
        spans_encontrados = panel_side.find_elements(webdriver.common.by.By.CLASS_NAME, "matched-text")
        for span in spans_encontrados:
            pai = span.find_element(webdriver.common.by.By.XPATH, "..")
            print(f"Texto do elemento pai: {pai.text}")
            driver.execute_script("arguments[0].scrollIntoView(true);", pai)
            time.sleep(1)
            pai.click()

            time.sleep(2)
            limit = 10
            messages = driver.find_elements(webdriver.common.by.By.CLASS_NAME, "message-in")
            results = []
            for msg in messages[-limit:]:
                try:
                    text = msg.find_element(webdriver.common.by.By.CLASS_NAME, "copyable-text").text
                    results.append(text)
                except:
                    continue
            print("\n".join(results))
            print("\n\n")

    except Exception as e:
        print(f"Erro ao raspar o Whatsapp Web: {e}")

    input("Pressione Enter para fechar o driver...")
    driver.quit()

if __name__ == "__main__":
    main()
