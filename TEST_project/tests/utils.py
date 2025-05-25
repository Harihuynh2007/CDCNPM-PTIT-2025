
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver, email="tanhaorn@gmail.com", password="123456ae"):
    driver.get("http://127.0.0.1:5500/TodoManager/login.html")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "emailSignin")))
    driver.find_element(By.ID, "emailSignin").send_keys(email)
    driver.find_element(By.ID, "passwordSignin").send_keys(password)

    driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "btn_signin"))
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard.html"))
