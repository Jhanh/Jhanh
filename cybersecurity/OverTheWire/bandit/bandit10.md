# Level 10 -> Level 11

The password for the next level is stored in the file *data.txt*, which contains base64 encoded data

Commands you may need to solve this level:
`grep`, `sort`, `uniq`, `strings`, `base64`, `tr`, `tar`, `gzip`, `bzip2`, `xxd`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 9)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit10`
- **Password**: `B0s2khmbT9u0geKuOoVGW3JZKhndE3BG`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 10

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit10@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 10

- **Thử thách**: Mật khẩu nằm trong file `data.txt`, nhưng nội dung bên trong đã bị mã hóa theo định dạng **Base64**. Nếu chỉ dùng `cat data.txt`, bạn sẽ chỉ thấy một đoạn mã hóa vô nghĩa.

- **Khái niệm cơ bản về Base64**:
  - Base64 là chuẩn mã hóa dùng 64 ký tự (A-Z, a-z, 0-9, `+`, `/` và thường kết thúc bằng dấu `=`) để biến dữ liệu bất kỳ thành văn bản an toàn khi truyền tải trên mạng.
  - **Lưu ý cốt lõi**: Base64 chỉ là **mã hóa chuyển đổi định dạng (Encoding)** chứ không phải mã hóa bảo mật (Encryption), do đó ai cũng có thể giải mã ngược lại được mà không cần chìa khóa bí mật (key).

- **Lệnh mới - `base64` (Giải mã dữ liệu Base64)**:
  - Cú pháp giải mã: Dùng cờ `-d` (viết tắt của `--decode`):
    ```bash
    base64 -d <tên_file>
    ```

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 11

- **Bước 1**: Liệt kê file trong thư mục:
  ```bash
  ls
  ```
  *Kết quả hiển thị*: file `data.txt`

- **Bước 2**: Giải mã nội dung file bằng lệnh `base64 -d`:
  ```bash
  base64 -d data.txt
  ```
  *(Cách khác tương đương qua pipe: `cat data.txt | base64 -d`)*

  *Kết quả*: Màn hình sẽ giải mã chuỗi Base64 và in ra văn bản gốc:
  ```text
  The password is <mật_khẩu_của_bandit11>
  ```

Chuỗi ký tự phía sau chính là mật khẩu của bandit11!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 11

```text
Password bandit11: [pYfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro]
```
