# Level 0 -> Level 1

The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

---

## 1. THÔNG TIN KẾT NỐI

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit0`
- **Password**: `bandit0`

---

## 2. GIẢI THÍCH CÁC LỆNH CẦN DÙNG

- **`ssh` (Secure Shell)**:
  - **Ý nghĩa**: Công cụ kết nối và điều khiển máy tính từ xa qua giao diện dòng lệnh.
  - **Cú pháp**: `ssh <user>@<host> -p <port>`

- **`ls` (viết tắt của "list")**:
  - **Ý nghĩa**: Liệt kê danh sách tất cả các tập tin (file) và thư mục đang có ở vị trí hiện tại.

- **`cat` (viết tắt của "concatenate")**:
  - **Ý nghĩa**: Đọc và in toàn bộ nội dung của một file văn bản trực tiếp ra màn hình.
  - **Cú pháp**: `cat <tên_file>` (ví dụ: `cat readme`)

- **`exit` (hoặc `logout`)**:
  - **Ý nghĩa**: Thoát khỏi phiên làm việc SSH và ngắt kết nối với máy chủ.

---

## 3. CÂU LỆNH KẾT NỐI SSH

Mở Terminal / PowerShell / Command Prompt trên máy tính của bạn và gõ:

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

**Giải thích chi tiết:**
- `ssh`: Khởi chạy chương trình SSH.
- `bandit0@...`: Chỉ định đăng nhập vào tài khoản `bandit0` tại máy chủ `bandit.labs.overthewire.org`.
- `-p 2220`: Tham số `-p` (port) chỉ định cổng kết nối là 2220 (mặc định của SSH là 22).

---

## 4. CÁC BƯỚC LẤY PASSWORD CHO LEVEL 1

Sau khi đã vào được bên trong máy chủ (dấu nhắc `bandit0@bandit:~$`):

- **Bước 1**: Kiểm tra xem xung quanh có file nào:
  ```bash
  ls
  ```
  *Kết quả hiển thị*: file có tên là `readme`.

- **Bước 2**: Xem nội dung của file readme để lấy mật khẩu:
  ```bash
  cat readme
  ```
  *Kết quả*: Màn hình sẽ in ra một chuỗi ký tự ngẫu nhiên (chính là password của bandit1).

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 1

```text
Password bandit1: [6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR]
```
