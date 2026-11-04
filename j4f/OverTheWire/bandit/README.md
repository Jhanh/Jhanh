# 🚩 OverTheWire Bandit - Toàn tập hướng dẫn & Kho tri thức

Chào mừng bạn đến với tài liệu tự học và tổng hợp toàn diện wargame **OverTheWire: Bandit**. Đây là bộ hướng dẫn chi tiết từ căn bản đến nâng cao về hệ điều hành Linux, mạng máy tính, quản trị hệ thống và nền tảng an ninh mạng / CTF.

---

## 🌐 Thông tin máy chủ OverTheWire

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Giao thức**: `SSH`
- **Cú pháp kết nối nhanh**:
  ```bash
  ssh bandit<level>@bandit.labs.overthewire.org -p 2220
  ```

---

## 🗺️ Bản đồ kiến thức đã đạt được (Roadmap)

Chặng đường 34 màn chơi (từ Level 0 đến Level 33) được chia làm 5 chuyên đề lớn:

```
[Linux Fundamentals] ──> [Data Decoding & Crypto] ──> [Networking & SSH] ──> [Privilege Escalation] ──> [Git & Shell Escape]
    (Level 0-9)               (Level 10-13)               (Level 14-17)            (Level 18-25)               (Level 25-33)
```

### 1. Thao tác tệp tin & Linux cơ bản (Level 0 $\rightarrow$ Level 9)
- **Tên tệp đặc biệt**:
  - Tệp có khoảng trắng: đặt trong ngoặc kép `cat "spaces in this filename"`.
  - Tệp bắt đầu bằng dấu gạch ngang (`-`): dùng đường dẫn tương đối `cat ./-` hoặc phân tách tùy chọn `cat -- -`.
  - Tệp ẩn: sử dụng cờ `ls -la`.
- **Tìm kiếm tệp nâng cao với `find`**:
  - Tìm theo kích thước: `find . -size 1033c` (tính bằng byte).
  - Tìm theo quyền và người sở hữu: `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`.
- **Xử lý luồng văn bản**:
  - Đọc chuỗi ký tự người đọc được trong tệp nhị phân: `strings`.
  - Tìm dòng xuất hiện duy nhất: `sort | uniq -u`.
  - Tìm kiếm nội dung theo từ khóa: `grep "millionth" data.txt`.

### 2. Mã hóa dữ liệu & Giải nén đa tầng (Level 10 $\rightarrow$ Level 13)
- **Mã hóa dữ liệu cơ bản**:
  - Giải mã chuỗi Base64: `base64 -d`.
  - Giải mã mật mã thay thế Caesar / ROT13: `tr 'A-Za-z' 'N-ZA-Mn-za-m'`.
- **Dịch ngược dữ liệu nhị phân (Data Decompression Loop)**:
  - Chuyển đổi mã hexdump về dạng nhị phân gốc: `xxd -r`.
  - Xác định kiểu tệp bằng header/chữ ký nhị phân: `file <filename>`.
  - Giải nén tuần tự nhiều định dạng nén lồng nhau: `gzip -d`, `bzip2 -d`, `tar -xf`.

### 3. Mạng máy tính, SSL/TLS & Quản trị khóa SSH (Level 13 $\rightarrow$ Level 17)
- **Quản lý khóa bí mật (SSH Private Key)**:
  - Kết nối qua khóa riêng: `ssh -i <keyfile> user@host -p 2220`.
  - Phân quyền tệp khóa trên Windows để tránh lỗi `Permissions are too open`:
    ```powershell
    icacls .\keyfile /inheritance:r
    icacls .\keyfile /grant:r "$($env:USERNAME):(R)"
    ```
- **Tương tác mạng & Quét cổng**:
  - Kết nối dịch vụ mạng thô qua TCP: `nc localhost 30000`.
  - Quét dải cổng đang lắng nghe: `nmap -sV -p 31000-32000 localhost`.
  - Giao tiếp qua kênh mã hóa SSL/TLS:
    ```bash
    openssl s_client -connect localhost:<port> -ign_eof
    ```
- **So sánh tệp**: Sử dụng `diff file1 file2` để tìm sự thay đổi duy nhất giữa hai tập tin cấu hình.

### 4. Tự động hóa, Cron jobs & Leo thang đặc quyền (Level 18 $\rightarrow$ Level 25)
- **Vượt qua tệp khởi động ép thoát (`.bashrc`)**: Chạy lệnh non-interactive thông qua SSH client:
  ```bash
  ssh bandit18@bandit.labs.overthewire.org -p 2220 'cat readme'
  ```
- **Leo thang đặc quyền qua tệp SUID (Set User ID)**:
  - Tệp thực thi mang cờ SUID (`rwsr-xr-x`) cho phép chạy lệnh dưới quyền của chủ sở hữu tệp (`./bandit20-do cat /etc/bandit_pass/...`).
- **Phân tích tác vụ định kỳ (Cron Jobs)**:
  - Đọc cấu hình cron tại `/etc/cron.d/`.
  - Đọc và phân tích các shell script tự động chạy định kỳ để trích xuất mật khẩu hoặc tạo backdoor ghi mật khẩu vào `/tmp`.
- **Lập trình Bash Script để Brute-Force**:
  - Viết vòng lặp tự động ghép nối mật khẩu với mã PIN 4 chữ số (`0000` đến `9999`) và gửi trực tiếp qua Netcat:
    ```bash
    for pin in {0000..9999}; do echo "$pass $pin"; done | nc localhost 30002
    ```

### 5. Git toàn diện & Kỹ thuật thoát vỏ bọc (Shell Breakout) (Level 25 $\rightarrow$ Level 33)
- **Kỹ thuật Thoát Shell hạn chế (Restricted Shell Breakout)**:
  - *Thoát khỏi `more`*: Thu nhỏ cửa sổ terminal còn 4-5 dòng $\rightarrow$ `more` dừng lại chờ $\rightarrow$ bấm phím `v` để vào trình soạn thảo `vi` $\rightarrow$ thiết lập `:set shell=/bin/bash` rồi `:shell` để lấy terminal bash hoàn chỉnh.
  - *Thoát khỏi Uppercase Shell*: Tận dụng biến tham số vị trí `$0` để sinh tiến trình shell nguyên bản `/bin/sh` kế thừa quyền SUID của `bandit33`.
- **Quản trị Git chuyên sâu**:
  - Clone kho lưu trữ Git qua SSH: `git clone ssh://...:2220/...`.
  - Truy vết thông tin rò rỉ trong lịch sử: `git log`, `git log -p`, `git show <commit_hash>`.
  - Làm việc với nhánh (Branches): `git branch -a`, `git checkout dev` (hoặc `git switch dev`).
  - Làm việc với thẻ (Tags): `git tag`, `git show <tag_name>`.
  - Đẩy mã (Push) và vượt qua `.gitignore`: Dùng `git add -f <file>` để ép buộc theo dõi tệp bị chặn, sau đó `git commit` và `git push` kích hoạt Git Server Hook.

---

## 📚 Mục lục 34 bài học chi tiết

| Bài học | Chủ đề chính | Tập lệnh / Công cụ sử dụng |
| :--- | :--- | :--- |
| [Bandit 0](bandit00.md) | Giới thiệu & Kết nối SSH lần đầu | `ssh` |
| [Bandit 1](bandit01.md) | Đọc tệp có tên đặc biệt (dấu gạch ngang `-`) | `cat ./-`, `cat -- -` |
| [Bandit 2](bandit02.md) | Đọc tệp có khoảng trắng trong tên | `cat "spaces in this filename"` |
| [Bandit 3](bandit03.md) | Đọc tệp ẩn trong thư mục | `ls -la`, `cat .hidden` |
| [Bandit 4](bandit04.md) | Nhận diện tệp người đọc được bằng chữ ký tệp | `file ./*` |
| [Bandit 5](bandit05.md) | Tìm tệp theo kích thước, quyền và thuộc tính | `find . -size 1033c ! -executable` |
| [Bandit 6](bandit06.md) | Quét toàn bộ hệ thống lọc theo User, Group và Size | `find / -user ... -group ... 2>/dev/null` |
| [Bandit 7](bandit07.md) | Tìm kiếm từ khóa trong tệp văn bản lớn | `grep "millionth" data.txt` |
| [Bandit 8](bandit08.md) | Tìm dòng văn bản xuất hiện duy nhất | `sort data.txt \| uniq -u` |
| [Bandit 9](bandit09.md) | Trích xuất chuỗi ký tự trong tệp nhị phân | `strings data.txt \| grep "==="` |
| [Bandit 10](bandit10.md) | Giải mã chuỗi dữ liệu Base64 | `base64 -d data.txt` |
| [Bandit 11](bandit11.md) | Giải mã mật mã Caesar / ROT13 | `tr 'A-Za-z' 'N-ZA-Mn-za-m'` |
| [Bandit 12](bandit12.md) | Dịch ngược nén dữ liệu nhị phân đa tầng | `xxd -r`, `gzip`, `bzip2`, `tar` |
| [Bandit 13](bandit13.md) | Đăng nhập SSH bằng Private Key nội bộ | `ssh -i sshkey.private` |
| [Bandit 14](bandit14.md) | Gửi dữ liệu qua cổng mạng với Netcat | `nc localhost 30000` |
| [Bandit 15](bandit15.md) | Giao tiếp mã hóa qua cổng SSL/TLS | `openssl s_client -connect ...` |
| [Bandit 16](bandit16.md) | Quét dải cổng bằng Nmap & Kết nối SSL | `nmap -sV`, `openssl s_client` |
| [Bandit 17](bandit17.md) | So sánh sự khác biệt giữa hai tập tin | `diff passwords.old passwords.new` |
| [Bandit 18](bandit18.md) | Vượt qua tệp `.bashrc` tự ngắt kết nối SSH | `ssh ... 'cat readme'` |
| [Bandit 19](bandit19.md) | Thực thi lệnh qua tệp mang cờ SUID | `./bandit20-do id` |
| [Bandit 20](bandit20.md) | Thiết lập Netcat lắng nghe kết nối đồng thời | `nc -lvnp`, `./suconnect` |
| [Bandit 21](bandit21.md) | Khảo sát tác vụ định kỳ Cron Job cơ bản | `cat /etc/cron.d/cronjob_bandit22` |
| [Bandit 22](bandit22.md) | Đảo ngược thuật toán mã băm trong Cron Script | `md5sum`, trích xuất tên tệp |
| [Bandit 23](bandit23.md) | Viết shell script khai thác Cron tự động chạy | Viết script sao chép mật khẩu vào `/tmp` |
| [Bandit 24](bandit24.md) | Viết Bash Script Brute-Force mã PIN qua Netcat | Vòng lặp `for pin in {0000..9999}` |
| [Bandit 25](bandit25.md) | Phá vỡ vỏ bọc `more` & Trình soạn thảo `vi` | Thu nhỏ terminal $\rightarrow$ `more` $\rightarrow$ `vi` |
| [Bandit 26](bandit26.md) | Breakout Shell từ `vi` sang `bash` hoàn chỉnh | `:set shell=/bin/bash`, `:shell` |
| [Bandit 27](bandit27.md) | Khởi đầu với Git & Clone repo qua SSH | `git clone ssh://...:2220/...` |
| [Bandit 28](bandit28.md) | Truy vết mật khẩu rò rỉ trong lịch sử Commit | `git log -p`, `git show` |
| [Bandit 29](bandit29.md) | Khảo sát và chuyển đổi các nhánh Git ẩn | `git branch -a`, `git checkout dev` |
| [Bandit 30](bandit30.md) | Tìm kiếm mật khẩu ẩn trong Git Tag | `git tag`, `git show secret` |
| [Bandit 31](bandit31.md) | Vượt qua `.gitignore` & Push kích hoạt Server Hook | `git add -f key.txt`, `git push` |
| [Bandit 32](bandit32.md) | Thoát khỏi Uppercase Shell bằng biến `$0` | Gõ `$0` để sinh shell `/bin/sh` |
| [Bandit 33](bandit33.md) | Đích đến cuối cùng & Thông điệp hoàn thành | `cat README.txt` (Victory Message) |

---

## 🔑 Bảng tra cứu toàn bộ 34 mật khẩu

Bảng này cung cấp đầy đủ thông tin đăng nhập từ **Bandit 0** đến **Bandit 33**. Bạn có thể dùng bảng này để vào thẳng bất kỳ level nào phục vụ việc ôn tập, thực hành lại mà không cần phải chơi lại từ đầu:

| Cấp độ (Level) | Tên người dùng | Mật khẩu (Password) | Phương thức / Ghi chú đăng nhập |
| :---: | :---: | :--- | :--- |
| **Bandit 0** | `bandit0` | `bandit0` | Đăng nhập SSH mặc định |
| **Bandit 1** | `bandit1` | `6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR` | Mật khẩu |
| **Bandit 2** | `bandit2` | `PK8fYLZg2hnHSz83plBL1iEPKdD3QToB` | Mật khẩu |
| **Bandit 3** | `bandit3` | `7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME` | Mật khẩu |
| **Bandit 4** | `bandit4` | `xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq` | Mật khẩu |
| **Bandit 5** | `bandit5` | `6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG` | Mật khẩu |
| **Bandit 6** | `bandit6` | `pXa26xhMWaC2SvDotA4r9EgZkulOeSBW` | Mật khẩu |
| **Bandit 7** | `bandit7` | `Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3` | Mật khẩu |
| **Bandit 8** | `bandit8` | `VR1ljMayciFxbnUokuQmJFw6QC9VKtub` | Mật khẩu |
| **Bandit 9** | `bandit9` | `EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl` | Mật khẩu |
| **Bandit 10** | `bandit10` | `B0s2khmbT9u0geKuOoVGW3JZKhndE3BG` | Mật khẩu |
| **Bandit 11** | `bandit11` | `pYfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro` | Mật khẩu |
| **Bandit 12** | `bandit12` | `GROozWPO8QyN0mGrjUkID0WCYkZiQxrN` | Mật khẩu |
| **Bandit 13** | `bandit13` | `qQYQiHOBPR8zR61qxYqX45quvihF2uzk` | Mật khẩu |
| **Bandit 14** | `bandit14` | `aaWecNkG4FhxJQxz07uiwzVP6bJiYS65` | Mật khẩu (hoặc dùng khóa `bandit14.key`) |
| **Bandit 15** | `bandit15` | `pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7` | Mật khẩu |
| **Bandit 16** | `bandit16` | `kS0Hf0u5HiXFwKMKFqXvPdOTNGGa0X8V` | Mật khẩu |
| **Bandit 17** | `bandit17` | `pWXMAZoxGC8JmDMfmT5MGEsobMM3vnj2` | Mật khẩu (hoặc dùng khóa `bandit17.key`) |
| **Bandit 18** | `bandit18` | `OQxXZjELndr90zuhOTDYBEomI0SZITXI` | Cần chạy lệnh qua SSH non-interactive |
| **Bandit 19** | `bandit19` | `KpsOfPkcP7i1FlIExk2QEjyt6dw8dxZI` | Mật khẩu |
| **Bandit 20** | `bandit20` | `4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA` | Mật khẩu |
| **Bandit 21** | `bandit21` | `bW9kBv5WC3P4yoDyf12LSdGuNz5ka6hY` | Mật khẩu |
| **Bandit 22** | `bandit22` | `RYVux2rHEm9tiXHmLFzuR7Vhx6AZQMEz` | Mật khẩu |
| **Bandit 23** | `bandit23` | `gKXDTAXnIz3OBxiPjRZ2uqutUlPZrBsw` | Mật khẩu |
| **Bandit 24** | `bandit24` | `hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv` | Mật khẩu |
| **Bandit 25** | `bandit25` | `SoHfqMOEqIX2IYKVciZxvgpR9a2Djx4P` | Mật khẩu |
| **Bandit 26** | `bandit26` | `jHdv2ELQhT22BkprMNDjybZDAkw1zeBJ` | Shell `more ~/text.txt` (thu nhỏ CMD $\rightarrow$ `vi`) |
| **Bandit 27** | `bandit27` | `STJLJBRRphMxKB392CT4iOr5CbzPU9ER` | Mật khẩu |
| **Bandit 28** | `bandit28` | `y8Yd2ssKcpHpud7UvOSOxwamRMzIGIeQ` | Mật khẩu |
| **Bandit 29** | `bandit29` | `Em7eGtqaMySwNFjCpwzzHhLhospOcdt0` | Mật khẩu |
| **Bandit 30** | `bandit30` | `jq9Dfg2rXsfYsWMgFuKlXhphjdH7USgX` | Mật khẩu |
| **Bandit 31** | `bandit31` | `82NkymblpGBYmIXG6ZQ8YldBYstHpfUf` | Mật khẩu |
| **Bandit 32** | `bandit32` | `pWuj5jBQ6IgV0NXwiH6g1pXRF8S1YvbT` | Uppercase Shell (thoát bằng `$0`) |
| **Bandit 33** | `bandit33` | `u4P2CyPOwPGLe94RdD9Uo2FxFwvnFswM` | **(FINAL LEVEL)** |

---

*Tài liệu được tổng hợp và ghi chép trong quá trình thực hành trực tiếp trên hệ thống OverTheWire Bandit.*

