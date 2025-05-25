
import unittest
import time
from tests.utils import login

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DASHBOARD_URL = "http://127.0.0.1:5500/TodoManager/dashboard.html"
def wait_for_index(driver, timeout=10):
    WebDriverWait(driver, timeout).until(EC.url_contains("dashboard.html"))
    WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located((By.ID, "preloader")))
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, "main-content")))

class TestLogout(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()

    def tearDown(self):
        self.driver.delete_all_cookies()

    def test_logout_success(self):
        driver = self.driver
        login(driver)

        driver.get(DASHBOARD_URL)
        wait_for_index(driver)

        # Click nút đăng xuất
        logout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_signout"))
        )
        driver.execute_script("arguments[0].click();", logout_btn)

        # Chờ quay lại trang login bằng presence của emailSignin
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "emailSignin"))
        )

        # Xác nhận element emailSignin tồn tại
        self.assertTrue(driver.find_element(By.ID, "emailSignin"))

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
