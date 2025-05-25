
import unittest
import time
from utils import login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

class TestAddTask(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()

    def tearDown(self):
        self.driver.delete_all_cookies()

    def test_add_task(self):
        driver = self.driver
        login(driver)  

        driver.get("http://127.0.0.1:5500/TodoManager/index.html")
        WebDriverWait(driver, 10).until(EC.url_contains("index.html"))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "preloader")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "main-content")))

        # Click vào nút '+' trên bảng "To do"
        add_task_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//i[@class='fas fa-plus board-header-icon' and @data-status='todo']"))
        )
        driver.execute_script("arguments[0].click();", add_task_button)

        # Chờ form mở hoàn toàn
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "add-task-content"))
        )
        time.sleep(1)

        # Nhập thông tin công việc
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "title"))).send_keys("Học Selenium")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "category"))).send_keys("Kiểm thử")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "description"))).send_keys("Làm bài tập kiểm thử tự động")
        

        # Sửa lỗi nhập ngày
        valid_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        due_date_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "due_date")))
        driver.execute_script("arguments[0].value = arguments[1];", due_date_input, valid_date)

        # Nhấn nút lưu công việc
        save_task_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn_add")))
        driver.execute_script("arguments[0].click();", save_task_button)

        # Kiểm tra công việc mới xuất hiện trong danh sách "To do"
        task_list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Học Selenium')]"))
        )
        self.assertTrue(task_list)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
