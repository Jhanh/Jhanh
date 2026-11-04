# Level 7 -> Level 8

The password for the next level is stored in the file *data.txt* next to the word *millionth*

Commands you may need to solve this level:
`grep`, `sort`, `uniq`, `strings`, `base64`, `tr`, `tar`, `gzip`, `bzip2`, `xxd`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 6)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit7`
- **Password**: `Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 7

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit7@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 7

- **Thử thách**: Mật khẩu nằm trong file `data.txt` ngay cạnh từ khóa `millionth`. Tuy nhiên, file `data.txt` này cực kỳ đồ sộ (hàng chục nghìn dòng dữ liệu). Nếu dùng `cat data.txt`, màn hình sẽ cuộn vô tận và không thể tìm thủ công bằng mắt.

- **Lệnh mới kinh điển - `grep` (Tìm kiếm nội dung văn bản)**:
  - `grep` là công cụ quan trọng bậc nhất trong Linux dùng để quét và lọc ra các dòng có chứa chuỗi ký tự mà bạn mong muốn.
  - Cú pháp cơ bản:
    ```bash
    grep "<từ_khóa>" <tên_file>
    ```
  - Áp dụng vào thử thách:
    ```bash
    grep "millionth" data.txt
    ```

- **Mở rộng: Khái niệm Ký hiệu đường ống Pipe (`|`)**:
  - Dấu `|` dùng để nối hai lệnh lại với nhau: lấy kết quả của lệnh bên trái truyền thẳng làm đầu vào cho lệnh bên phải.
  - Bạn cũng có thể dùng cú pháp tương đương:
    ```bash
    cat data.txt | grep "millionth"
    ```

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 8

- **Bước 1**: Liệt kê file trong thư mục:
  ```bash
  ls
  ```
  *Kết quả hiển thị*: file `data.txt`

- **Bước 2**: Dùng `grep` để tìm chính xác dòng chứa từ khóa `millionth`:
  ```bash
  grep "millionth" data.txt
  ```
  *Kết quả*: Màn hình sẽ in ra đúng dòng duy nhất có định dạng:
  ```text
  millionth    <mật_khẩu_của_bandit8>
  ```

Chuỗi ký tự nằm cạnh chữ `millionth` chính là mật khẩu của bandit8!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 8

```text
Password bandit8: [VR1ljMayciFxbnUokuQmJFw6QC9VKtub]
```
