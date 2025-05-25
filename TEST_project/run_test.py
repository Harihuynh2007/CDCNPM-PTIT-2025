import unittest

# Tìm và chạy tất cả các test case trong thư mục tests
if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("tests")  # Tự động tìm test trong thư mục 'tests'

    test_runner = unittest.TextTestRunner(verbosity=2)  # Hiển thị log chi tiết
    test_runner.run(test_suite)
