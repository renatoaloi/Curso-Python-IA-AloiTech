import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

CONTACT_NAME = "Arduino"

CHROME_PROFILE_PATH = os.path.abspath("chrome_profile")
ELEMENT_TO_WAIT = "//div[@id='pane-side']"
WAIT_TIME = 120 # 2 minutos
SEARCH_BOX_XPATH = "//input[@aria-label='Pesquisar ou começar uma nova conversa']"
VERIFYING_XPATH_PAI = "//*[@id='pane-side']/div/div/div"
VERIFYING_XPATH_BUSCA = "./descendant::span[contains(@class, 'matched-text')]"

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
        time.sleep(0.5)
        for c in CONTACT_NAME:
            search_box.send_keys(c)
            time.sleep(0.1)
        search_box.send_keys(webdriver.common.keys.Keys.ENTER)
        time.sleep(1)

        pai = driver.find_element(webdriver.common.by.By.XPATH, VERIFYING_XPATH_PAI)
        filhos = pai.find_elements(webdriver.common.by.By.XPATH, VERIFYING_XPATH_BUSCA)
        found = False
        for contact_to_select in filhos:
            contact = contact_to_select.find_element(webdriver.common.by.By.XPATH, "..")
            if contact.text.lower() == CONTACT_NAME.lower():
                print(f"Contato {CONTACT_NAME} encontrado!")
                driver.execute_script("arguments[0].scrollIntoView(true);", contact)
                time.sleep(1)
                contact.click()
                found = True
                break

        if not found:
            print(f"Contato {CONTACT_NAME} não encontrado na lista de resultados da busca.")

    except Exception as e:
        print(f"Erro ao raspar o Whatsapp Web: {e}")

    input("Pressione Enter para fechar o driver...")
    driver.quit()

if __name__ == "__main__":
    main()