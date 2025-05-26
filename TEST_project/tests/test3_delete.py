
import unittest
import time
from tests.utils import login

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

# URL của trang quản lý task
INDEX_URL = "http://127.0.0.1:5500/TodoManager/index.html"

def wait_for_index(driver, timeout=10):
    WebDriverWait(driver, timeout).until(EC.url_contains("index.html"))
    WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located((By.ID, "preloader")))
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, "main-content")))

class TestDeleteTask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()

    def tearDown(self):
        self.driver.delete_all_cookies()

    def test_delete_task(self):
        driver = self.driver
        login(driver)

        # Điều hướng đến index và chờ load xong
        driver.get(INDEX_URL)
        wait_for_index(driver)

        # Đảm bảo có task "Học Selenium" trước khi xóa
        tasks = driver.find_elements(By.XPATH, "//p[text()='Học Selenium']")
        if not tasks:
            add_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                    "//i[@data-status='todo' and contains(@class,'fa-plus')]"
                ))
            )
            driver.execute_script("arguments[0].click();", add_btn)
            # Chờ form hiển thị
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "title"))
            )
            
            driver.find_element(By.ID, "title").send_keys("Học Selenium")
            driver.find_element(By.ID, "category").send_keys("Kiểm thử")
            driver.find_element(By.ID, "description").send_keys("Tự động hóa xóa task")
            due_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            driver.execute_script("document.getElementById('due_date').value = arguments[0];", due_date)
            

            save_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "btn_add"))
            )
            time.sleep(1)

            driver.execute_script("arguments[0].click();", save_btn)

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[text()='Học Selenium']"))
            )

        delete_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                "//p[text()='Học Selenium']/ancestor::div[contains(@class,'task-item')]"
                "//i[contains(@class,'task-item-trash')]"
            ))
        )
        time.sleep(1)
        driver.execute_script("arguments[0].click();", delete_icon)

        # Chờ task biến mất hoàn toàn
        WebDriverWait(driver, 10).until_not(
            EC.presence_of_element_located((By.XPATH, "//p[text()='Học Selenium']"))
        )

        # Xác nhận không còn element nào
        remaining = driver.find_elements(By.XPATH, "//p[text()='Học Selenium']")
        self.assertEqual(len(remaining), 0, "Task 'Học Selenium' vẫn tồn tại sau khi xóa")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
