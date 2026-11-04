# Level 4 -> Level 5

The password for the next level is stored in the only human-readable file in the *inhere* directory. Tip: if your terminal is messed up, try the "reset" command.

Commands you may need to solve this level:
`ls`, `cd`, `cat`, `file`, `du`, `find`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 3)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit4`
- **Password**: `xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 4

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit4@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 4

- **Thử thách**: Bên trong thư mục `inhere` có nhiều tập tin (từ `-file00` đến `-file09`), nhưng chỉ có **duy nhất 1 file** là con người có thể đọc được (human-readable). Các file còn lại đều là dữ liệu nhị phân (binary/data rác).
- **Lưu ý**: Nếu lỡ dùng `cat` đọc trúng file nhị phân khiến terminal bị loạn phông chữ, bạn chỉ cần gõ lệnh `reset` rồi nhấn Enter để khôi phục màn hình.

- **Lệnh mới - `file` (Kiểm tra định dạng tập tin)**:
  - Trong Linux, phần mở rộng (đuôi file như `.txt`, `.exe`) không quyết định loại file, mà do nội dung bên trong quyết định.
  - Lệnh `file` kiểm tra trực tiếp nội dung bên trong để cho biết tập tin đó thực chất là gì (hình ảnh, mã thực thi, văn bản thuần ASCII, hay dữ liệu nhị phân).
  - Cú pháp: `file <tên_file>`

- **Ký tự đại diện `*` (Wildcard)**:
  - Dấu `*` đại diện cho "tất cả mọi file".
  - Kết hợp đường dẫn tương đối và dấu sao: `file ./*` sẽ kiểm tra định dạng của toàn bộ các file trong thư mục hiện tại cùng một lúc.
  - File chứa mật khẩu hợp lệ sẽ có kết quả định dạng là: **`ASCII text`**.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 5

- **Bước 1**: Di chuyển vào thư mục `inhere`:
  ```bash
  cd inhere
  ```

- **Bước 2**: Liệt kê các file để quan sát:
  ```bash
  ls
  ```
  *Kết quả hiển thị*: các file có dạng `-file00`, `-file01`, ..., `-file09`.

- **Bước 3**: Kiểm tra định dạng của tất cả các file cùng lúc:
  ```bash
  file ./*
  ```
  *Kết quả*: Quan sát danh sách và tìm file nào có đuôi thông báo là `ASCII text`.

- **Bước 4**: Đọc file dạng `ASCII text` vừa tìm được:
  ```bash
  cat ./<tên_file_ASCII_text>
  ```
  *(Ví dụ nếu file tìm được là `-file07`: `cat ./-file07`)*

Màn hình sẽ in ra chuỗi mật khẩu tiếp theo, đó chính là mật khẩu của bandit5!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 5

```text
Password bandit5: [6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG]
```
