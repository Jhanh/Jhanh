# Level 8 -> Level 9

The password for the next level is stored in the file *data.txt* and is the only line of text that occurs only once

Commands you may need to solve this level:
`grep`, `sort`, `uniq`, `strings`, `base64`, `tr`, `tar`, `gzip`, `bzip2`, `xxd`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 7)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit8`
- **Password**: `VR1ljMayciFxbnUokuQmJFw6QC9VKtub`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 8

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit8@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 8

- **Thử thách**: Trong file `data.txt`, hầu hết các dòng chữ đều bị lặp đi lặp lại rất nhiều lần. Mật khẩu của chúng ta là **dòng chữ duy nhất chỉ xuất hiện đúng 1 lần** (occurs only once).

- **Hai lệnh mới quan trọng - `sort` và `uniq`**:
  1. `sort`: Sắp xếp toàn bộ các dòng theo thứ tự bảng chữ cái (A -> Z).
  2. `uniq`: Công cụ kiểm tra các dòng trùng lặp.
     - Tham số `-u` (unique): Chỉ in ra dòng nào xuất hiện duy nhất 1 lần (loại bỏ toàn bộ các dòng bị lặp lại).

- **Lưu ý cốt lõi về lệnh `uniq`**:
  - `uniq` **chỉ phát hiện được các dòng trùng lặp nếu chúng nằm liền kề nhau**! Nếu các dòng giống nhau nằm rải rác cách xa nhau, `uniq` sẽ không nhận diện được.
  - Vì vậy, quy tắc bất biến trong Linux là: **luôn dùng `sort` để gom các dòng giống nhau lại cạnh nhau trước, rồi mới dùng `uniq`**.

- **Sử dụng đường ống Pipe (`|`)**:
  ```bash
  sort data.txt | uniq -u
  ```

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 9

- **Bước 1**: Liệt kê file trong thư mục:
  ```bash
  ls
  ```
  *Kết quả hiển thị*: file `data.txt`

- **Bước 2**: Sắp xếp nội dung file và lọc ra dòng duy nhất không bị trùng lặp:
  ```bash
  sort data.txt | uniq -u
  ```
  *Kết quả*: Màn hình sẽ chỉ in ra một dòng duy nhất không trùng với bất kỳ ai!

Dòng chữ duy nhất đó chính là mật khẩu của bandit9!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 9

```text
Password bandit9: [EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl]
```
