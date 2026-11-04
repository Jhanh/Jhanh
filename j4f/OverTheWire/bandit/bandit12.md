# Level 12 -> Level 13

The password for the next level is stored in the file *data.txt*, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to predict directory name, or use mktemp -d. Then copy the datafile using cp, and rename it using mv (read the manpages!)

Commands you may need to solve this level:
`grep`, `sort`, `uniq`, `strings`, `base64`, `tr`, `tar`, `gzip`, `bzip2`, `xxd`, `mkdir`, `cp`, `mv`, `file`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 11)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit12`
- **Password**: `GROozWPO8QyN0mGrjUkID0WCYkZiQxrN`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 12

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit12@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 12

- **Thử thách**: File `data.txt` là một **hexdump** (bản ghi mã thập lục phân) của một tập tin bị **nén lồng nhau nhiều lớp liên tiếp** (như búp bê Nga Matryoshka). Ta phải chuyển hexdump ngược lại thành file nhị phân, sau đó bóc tách từng lớp nén cho tới khi lộ ra văn bản gốc.
- **Thao tác trong thư mục tạm `/tmp`**:
  - Thư mục hiện tại của `bandit12` không cho phép ghi/tạo file mới. Vì vậy ta cần tạo một thư mục riêng trong `/tmp` để làm việc.

- **Các công cụ nén & giải nén cốt lõi trong Linux**:
  1. `xxd -r`: Đảo ngược hexdump trở lại thành dữ liệu nhị phân ban đầu (`xxd -r data.txt > data1`).
  2. `file <tên_file>`: **Công cụ quan trọng nhất của màn này!** Dùng để "soi" xem file đang bị nén theo định dạng nào.
  3. `mv`: Đổi tên file để thêm đuôi mở rộng phù hợp (các lệnh giải nén như `gzip`, `bzip2` bắt buộc file phải có đúng đuôi file mới chịu làm việc).
  4. Các lệnh giải nén:
     - **gzip**: Cần đổi đuôi thành `.gz` (`mv file file.gz`), giải nén bằng `gzip -d file.gz`
     - **bzip2**: Cần đổi đuôi thành `.bz2` (`mv file file.bz2`), giải nén bằng `bzip2 -d file.bz2`
     - **tar**: Giải nén bằng `tar -xf file`

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 13

### Bước 1: Tạo thư mục làm việc trong `/tmp` và sao chép file sang
```bash
# Tạo một thư mục riêng cho bạn trong /tmp và di chuyển vào đó:
mkdir /tmp/myworkspace_bandit12
cd /tmp/myworkspace_bandit12

# Copy file data.txt sang thư mục hiện tại:
cp ~/data.txt .
```

### Bước 2: Khôi phục file nhị phân từ hexdump
```bash
xxd -r data.txt > data1
```

### Bước 3: Vòng lặp giải nén từng lớp (Bóc hành)
Dùng lệnh `file` để xem định dạng của file hiện tại:
```bash
file data1
```
Tùy thuộc vào kết quả `file` báo, bạn áp dụng lệnh giải nén tương ứng:

- **Nếu là `gzip compressed data`**:
  ```bash
  mv data1 data1.gz
  gzip -d data1.gz
  # Giải nén xong sẽ xuất hiện lại file data1
  ```

- **Nếu là `bzip2 compressed data`**:
  ```bash
  mv data1 data1.bz2
  bzip2 -d data1.bz2
  # Giải nén xong sẽ xuất hiện lại file data1
  ```

- **Nếu là `POSIX tar archive`**:
  ```bash
  tar -xf data1
  # Sẽ bung ra file mới (ví dụ data2.bin), tiếp tục dùng lệnh file để kiểm tra file mới đó
  ```

👉 **Cứ lặp lại quy trình**: Kiểm tra bằng `file` -> Đổi tên đúng đuôi bằng `mv` -> Giải nén cho tới khi kết quả hiển thị: **`ASCII text`**.

### Bước 4: Đọc mật khẩu
Khi file cuối cùng là `ASCII text`, đọc nội dung bằng `cat`:
```bash
cat <tên_file_cuối_cùng>
```

Màn hình sẽ in ra chuỗi mật khẩu của bandit13!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 13

```text
Password bandit13: [qQYQiHOBPR8zR61qxYqX45quvihF2uzk]
```
