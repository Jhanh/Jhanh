# Level 9 -> Level 10

The password for the next level is stored in the file *data.txt* in one of the few human-readable strings, preceded by several "=" characters.

Commands you may need to solve this level:
`grep`, `sort`, `uniq`, `strings`, `base64`, `tr`, `tar`, `gzip`, `bzip2`, `xxd`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 8)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit9`
- **Password**: `EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 9

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit9@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 9

- **Thử thách**: File `data.txt` ở màn này là tập tin nhị phân (binary file). Nếu bạn dùng lệnh `cat`, terminal sẽ bị loạn ký tự và đơ màn hình. Mật khẩu là một trong số ít chuỗi ký tự con người đọc được (human-readable) và có nhiều dấu bằng `=` đứng ở phía trước.

- **Lệnh mới của dân dịch ngược (Reverse Engineering) - `strings`**:
  - `strings` là công cụ chuyên dùng để "đào bới" văn bản bên trong các file nhị phân, mã thực thi hoặc file rác.
  - Tác dụng: Quét qua toàn bộ file và chỉ lọc ra các chuỗi ký tự chữ cái/con số có thể in được ra màn hình (mặc định từ 4 ký tự in được liên tiếp trở lên).
  - Cú pháp: `strings <tên_file>`

- **Kết hợp `strings` và `grep` qua Pipeline (`|`)**:
  - Lệnh `strings` trích xuất toàn bộ chữ có thể đọc, sau đó truyền thẳng qua `grep` để chỉ giữ lại các dòng chứa dấu bằng `=`:
  ```bash
  strings data.txt | grep "=="
  ```

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 10

- **Bước 1**: Liệt kê file trong thư mục:
  ```bash
  ls
  ```
  *Kết quả hiển thị*: file `data.txt`

- **Bước 2**: Trích xuất văn bản đọc được và lọc các dòng có dấu bằng:
  ```bash
  strings data.txt | grep "=="
  ```
  *Kết quả*: Màn hình sẽ in ra một vài dòng có dạng:
  ```text
  ========== the
  ========== password
  ========== is
  ========== <mật_khẩu_của_bandit10>
  ```

Dòng cuối cùng chứa chuỗi ký tự đi kèm các dấu `=` chính là mật khẩu của bandit10!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 10

```text
Password bandit10: [B0s2khmbT9u0geKuOoVGW3JZKhndE3BG]
```
