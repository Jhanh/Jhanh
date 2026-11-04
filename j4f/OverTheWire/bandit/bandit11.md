# Level 11 -> Level 12

The password for the next level is stored in the file *data.txt*, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

Commands you may need to solve this level:
`grep`, `sort`, `uniq`, `strings`, `base64`, `tr`, `tar`, `gzip`, `bzip2`, `xxd`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 10)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit11`
- **Password**: `pYfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 11

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit11@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 11

- **Thử thách**: Mật khẩu nằm trong file `data.txt`, nhưng toàn bộ chữ cái (cả in hoa lẫn in thường) đã bị xoay dịch chuyển đi 13 vị trí. Đây chính là thuật toán mã hóa cổ điển kinh điển: **ROT13** (biến thể của mật mã Caesar).

- **Khái niệm mật mã ROT13**:
  - Bảng chữ cái tiếng Anh có 26 chữ cái. ROT13 thay thế mỗi ký tự bằng ký tự đứng sau nó 13 vị trí trong bảng chữ cái.
  - Ví dụ: `A` -> `N`, `B` -> `O`, ..., `N` -> `A`.
  - Đặc tính độc đáo: Vì $13 + 13 = 26$, nên áp dụng mã hóa ROT13 một lần nữa sẽ giải mã thành chữ gốc!

- **Lệnh mới - `tr` (Translate - Chuyển đổi và ánh xạ ký tự)**:
  - `tr` là công cụ chuyên dùng để thay thế hoặc ánh xạ các ký tự từ bảng này sang bảng khác thông qua dòng lệnh.
  - Cú pháp cơ bản:
    ```bash
    tr '<ký_tự_gốc>' '<ký_tự_thay_thế>'
    ```
  - Áp dụng để giải mã ROT13:
    Ta ánh xạ bảng chữ cái chuẩn `A-Za-z` sang bảng chữ cái dịch 13 bước `N-ZA-Mn-za-m`:
    ```bash
    cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
    ```

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 12

- **Bước 1**: Liệt kê file trong thư mục:
  ```bash
  ls
  ```
  *Kết quả hiển thị*: file `data.txt`

- **Bước 2**: Đọc và giải mã ROT13 bằng lệnh `tr`:
  ```bash
  cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
  ```
  *Kết quả*: Màn hình sẽ chuyển đổi toàn bộ ký tự về dạng văn bản gốc:
  ```text
  The password is <mật_khẩu_của_bandit12>
  ```

Chuỗi ký tự phía sau chính là mật khẩu của bandit12!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 12

```text
Password bandit12: [GROozWPO8QyN0mGrjUkID0WCYkZiQxrN]
```
