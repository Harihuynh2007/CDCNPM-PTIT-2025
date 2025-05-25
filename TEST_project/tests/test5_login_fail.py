
import unittest
from utils import login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL trang đăng nhập
LOGIN_URL = "http://127.0.0.1:5500/TodoManager/login.html"

class TestLoginFail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()

    def tearDown(self):
        self.driver.delete_all_cookies()

    def test_login_wrong_password(self):
        driver = self.driver
        driver.get(LOGIN_URL)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "emailSignin"))
        )

        # Nhập email đúng, mật khẩu sai
        driver.find_element(By.ID, "emailSignin").send_keys("tanhaorn@gmail.com")
        driver.find_element(By.ID, "passwordSignin").send_keys("wrongpassword")

        # Click đăng nhập
        driver.execute_script(
            "arguments[0].click();",
            driver.find_element(By.ID, "btn_signin")
        )

        # Chờ hiển thị thông báo lỗi
        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//div[contains(text(), 'Sai tên đăng nhập hoặc mật khẩu')]"
            ))
        )
        # Xác nhận lỗi và URL không chuyển trang
        self.assertEqual(error_element.text, "Sai tên đăng nhập hoặc mật khẩu")
        self.assertIn("login.html", driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == "__main__":
    unittest.main()
