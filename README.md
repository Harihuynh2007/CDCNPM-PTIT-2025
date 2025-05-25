# 🧪 Bộ Test Tự Động - TodoManager (Selenium + Unittest)

Đây là tập hợp các test case tự động sử dụng **Python**, **Selenium WebDriver**, và **Unittest** để kiểm thử giao diện người dùng của ứng dụng TodoManager.

## 📁 Cấu trúc thư mục

```
.
├── config.py                  # Cấu hình đường dẫn dự án
├── run_test.py               # File chính để chạy toàn bộ test
├── test1_login.py            # Test đăng nhập thành công
├── test2_add_task.py         # Test thêm task mới
├── test3_delete.py           # Test xóa task
├── test4_logout.py           # Test đăng xuất
├── test5_login_fail.py       # Test đăng nhập thất bại
└── README.md                 # Tài liệu hướng dẫn này
```

> ⚠️ Lưu ý: Mặc định các file test sử dụng **trình duyệt Microsoft Edge**. Bạn có thể sửa lại thành `webdriver.Chrome()` nếu cần.

## ⚙️ Yêu cầu cài đặt

- Python >= 3.8
- Trình duyệt Microsoft Edge hoặc Chrome
- EdgeDriver hoặc ChromeDriver tương thích
- Cài các thư viện:

```bash
pip install selenium
```

## 🚀 Cách chạy test

### 1. Chạy tất cả test:

```bash
python run_test.py
```

### 2. Chạy từng file riêng:

```bash
python test1_login.py
```

## 🧪 Chi tiết các test

| File | Mục đích | Mô tả |
|------|----------|-------|
| `test1_login.py` | Đăng nhập thành công | Kiểm tra login với email và mật khẩu đúng |
| `test2_add_task.py` | Thêm task | Thêm task mới vào cột "To do" |
| `test3_delete.py` | Xóa task | Xóa task có tên "Học Selenium" nếu tồn tại |
| `test4_logout.py` | Đăng xuất | Kiểm tra người dùng có quay lại trang login sau khi logout |
| `test5_login_fail.py` | Login sai | Kiểm tra không đăng nhập khi nhập sai mật khẩu |

## 📝 Ghi chú

- Truy cập ứng dụng tại: `http://127.0.0.1:5500/TodoManager/login.html`
- Nếu dùng Live Server trong VSCode, hãy đảm bảo đã bật tại đúng thư mục `TodoManager`
- Có thể cấu hình thêm các path trong `config.py` nếu tổ chức lại cấu trúc

## 📤 Tác giả

- **Tên:** Huỳnh Minh Hải
- **Dự án:** Kiểm thử TodoManager (học phần Công nghệ phần mềm)
