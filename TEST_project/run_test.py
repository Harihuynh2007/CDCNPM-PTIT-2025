import unittest

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("tests")  # Đúng vì thư mục 'tests' đã có test

    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
