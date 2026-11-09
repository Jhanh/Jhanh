# TỔNG HỢP KIẾN THỨC MẠNG MÁY TÍNH

> [!NOTE]
> **Tài liệu học tập & tra cứu**: Giáo trình quốc tế **Computer Networking: A Top-Down Approach (9th Edition)** của *Kurose & Ross* kết hợp ghi chú học tập thực tế.

---

## 📚 Mục lục

- [📑 Bản đồ kiến trúc mạng (Roadmap)](#roadmap)
- [Chương 1: Tổng quan về mạng máy tính và Internet](#chuong-1)
- [Chương 2: Tầng ứng dụng (Application Layer)](#chuong-2)
- [Chương 3: Tầng giao vận (Transport Layer)](#chuong-3)
- [Chương 4: Tầng mạng - Mặt phẳng dữ liệu (Network Layer: Data Plane)](#chuong-4)
- [Chương 5: Tầng mạng - Mặt phẳng điều khiển (Network Layer: Control Plane)](#chuong-5)
- [Chương 6: Tầng liên kết dữ liệu và mạng cục bộ (Link Layer and LANs)](#chuong-6)
- [Chương 7: Mạng không dây và di động (Wireless & Mobile Networks)](#chuong-7)
- [Chương 8: An toàn trong mạng máy tính (Network Security)](#chuong-8)
- [🎯 Bảng tổng kết](#summary)

---

<a id="roadmap"></a>
## 📑 BẢN ĐỒ KIẾN TRÚC MẠNG (ROADMAP)

| Tầng (Layer)&emsp;&emsp; | PDU (Đơn vị dữ liệu) | Giao thức (Protocol) | Thiết bị tiêu biểu | Chức năng cốt lõi |
| :--- | :--- | :--- | :--- | :--- |
| **5. Application** | **Message** | HTTP/1.1, HTTP/2, HTTP/3, DNS, SMTP, SSH | Host, Proxy, Web Server | Hỗ trợ ứng dụng mạng, định dạng & trao đổi thông điệp |
| **4. Transport** | **Segment** | TCP (tin cậy), UDP (tốc độ cao) | Host (OS Kernel Socket) | Truyền thông tiến trình - tiến trình (Process-to-Process) |
| **3. Network** | **Datagram** | IPv4, IPv6, ICMP, OSPF, BGP, SDN | Router, Layer 3 Switch | Định tuyến & chuyển tiếp gói tin máy trạm - máy trạm (Host-to-Host) |
| **2. Data Link** | **Frame** | Ethernet (802.3), Wi-Fi (802.11), ARP, VLAN | Switch, Bridge, NIC | Truyền khung dữ liệu giữa các nút kề nhau trên cùng liên kết (Hop-by-Hop) |
| **1. Physical** | **Bit** | Cáp đồng xoắn, Cáp quang, Sóng vô tuyến | Hub, Repeater, Cáp mạng | Truyền chuỗi bit thô qua môi trường vật lý (điện áp, quang, tần số sóng) |

```text
QUÁ TRÌNH ĐÓNG GÓI (ENCAPSULATION) VÀ GIẢI ĐÓNG GÓI (DECAPSULATION)
[Sender / Client]                                           [Receiver / Server]
┌─────────────┬──────────────────────┐                      ┌─────────────┬──────────────────────┐
│ Application │         Data         │ (Message)            │ Application │        Data          │ (Message)
└─────────────┴──────────────────────┘                      └─────────────┴──────────────────────┘
                 │ (Đóng gói Header Ht)                                      ▲ (Bóc Header Ht)
                 ▼                                                           │
┌─────────────┬──────┬───────────────┐                      ┌─────────────┬──────┬───────────────┐
│ Transport   │  Ht  │     Data      │ (Segment)            │ Transport   │  Ht  │     Data      │
└─────────────┴──────┴───────────────┘                      └─────────────┴──────┴───────────────┘
                 │ (Đóng gói Header Hn)                                      ▲ (Bóc Header Hn)
                 ▼                                                           │
┌─────────────┬──────┬──────┬────────┐                      ┌─────────────┬──────┬──────┬────────┐
│ Network     │  Hn  │  Ht  │  Data  │ (Datagram)           │ Network     │  Hn  │  Ht  │  Data  │
└─────────────┴──────┴──────┴────────┘                      └─────────────┴──────┴──────┴────────┘
                 │ (Đóng gói Hl & Tl)                                        ▲ (Bóc Header Hl, Tl)
                 ▼                                                           │
┌─────────────┬──────┬──────┬──────┬──────┬──────┐          ┌─────────────┬──────┬──────┬──────┬──────┬──────┐
│ Data Link   │  Hl  │  Hn  │  Ht  │ Data │  Tl  │ (Frame)  │ Data Link   │  Hl  │  Hn  │  Ht  │ Data │  Tl  │
└─────────────┴──────┴──────┴──────┴──────┴──────┘          └─────────────┴──────┴──────┴──────┴──────┴──────┘
                 │ (Chuyển thành chuỗi bit)                                  ▲ (Gom chuỗi bit thành Frame)
                 ▼                                                           │
┌─────────────┬────────────────────────────┐                ┌─────────────┬────────────────────────────┐
│ Physical    │ 0 1 0 1 1 1 0 0 1 0 1 0... │                │ Physical    │ 0 1 0 1 1 1 0 0 1 0 1 0... │
└─────────────┴────────────────────────────┘                └─────────────┴────────────────────────────┘
                     \                                          /
                      ═════[ MÔI TRƯỜNG TRUYỀN DẪN VẬT LÝ ]═════
```

---

<a id="chuong-1"></a>
# CHƯƠNG 1: TỔNG QUAN VỀ MẠNG MÁY TÍNH VÀ INTERNET
> 📄 **Slide bài giảng:** [Chapter_1_v9.0.pdf](.pdf/Chapter_1_v9.0.pdf)

## 1.1. Bản chất của Internet & Các thành phần cấu tạo
Internet là **"Mạng của các mạng" (Network of networks)** kết nối hàng tỷ thiết bị tính toán (*Hosts / End Systems*).

- **Thiết bị đầu cuối (Hosts / End Systems)**: Máy tính bàn, laptop, smartphone, IoT, server. Chạy các chương trình ứng dụng mạng (Network Applications).
- **Đường truyền thông (Communication Links)**:
  - Cáp sợi quang (*Fiber optics*): Băng thông khổng lồ, suy hao thấp, dùng cho tuyến trục đường dài và xuyên đại dương.
  - Cáp đồng (*Twisted pair, Coaxial*): Phổ biến cho mạng LAN (cáp CAT5e/CAT6), truyền hình cáp.
  - Sóng vô tuyến (*Radio / Wi-Fi / 4G / 5G*): Linh hoạt, không dây, suy hao theo khoảng cách và vật cản.
  - Vệ tinh (*Satellite - LEO như Starlink, GEO*): Phủ sóng vùng sâu vùng xa, độ trễ phụ thuộc quỹ đạo.
- **Thiết bị chuyển mạch gói (Packet Switches)**:
  - **Router**: Chuyển tiếp gói tin giữa các mạng khác nhau (hoạt động ở Tầng 3 - Network Layer).
  - **Link-layer Switch**: Chuyển tiếp khung dữ liệu trong nội bộ mạng LAN (hoạt động ở Tầng 2 - Data Link Layer).
- **Giao thức (Protocols)**:
  - Định nghĩa **cú pháp (syntax)**, **ngữ nghĩa (semantics)**, **thứ tự** trao đổi thông điệp giữa các thực thể và **hành động** được kích hoạt khi gửi/nhận thông điệp hoặc khi có sự kiện xảy ra.
  - Chuẩn hóa bởi tổ chức **IETF** thông qua các tài liệu **RFC (Request for Comments)**.

```text
CẤU TRÚC PHÂN CẤP INTERNET (ISP TIER STRUCTURE)
    ┌───────────────────────────────────────────────────────┐
    │       Tier-1 ISPs (Toàn cầu: AT&T, Lumen, Telia)      │ <─── Không trả phí transit,
    └───────────────────────────────────────────────────────┘      kết nối ngang hàng (Peering)
           ▲               ▲                      ▲
    Transit│        Transit│               Peering│
           ▼               ▼                      ▼
    ┌─────────────────────────────┐        ┌─────────────────────────────┐
    │ Regional ISPs (Cấp khu vực) │<══════>│ Regional ISPs (Cấp khu vực) │
    └─────────────────────────────┘        └─────────────────────────────┘
           ▲                                      ▲
    Transit│                               Transit│
           ▼                                      ▼
    ┌─────────────────────────────┐        ┌─────────────────────────────┐
    │ Access ISPs (Viettel, VNPT) │        │ Access ISPs (FPT, SPT, ...) │
    └─────────────────────────────┘        └─────────────────────────────┘
      /     │      \                          /     │      \
   End     End     Data                    End     End     Data
  Hosts   Hosts   Center                  Hosts   Hosts   Center
```

> [!TIP]
> **IXP (Internet Exchange Point)**: Điểm trao đổi Internet công cộng cho phép các ISP kết nối trực tiếp (*peering*) với nhau miễn phí hoặc chi phí thấp nhằm tiết kiệm phí thuê đường truyền (*transit fees*) qua các nhà mạng cấp trên.

---

## 1.2. Các thuật ngữ mạng cốt lõi

### A. Định tuyến (Routing) vs Chuyển tiếp (Forwarding)
Hai chức năng cơ bản nhất của phần lõi mạng (Network Core):
- `Routing` (Định tuyến): Quá trình tìm đường đi logic tối ưu từ máy gửi xuyên qua toàn bộ hệ thống mạng đến máy nhận.
  - Phạm vi: **Toàn cục (Network-wide)**.
  - Do các thuật toán định tuyến (*Routing Algorithms* như OSPF, BGP) phối hợp tính toán để xây dựng nên **Bảng định tuyến (Routing Table)**.
- `Forwarding` (Chuyển tiếp): Hành động cục bộ của router khi nhận được một gói tin ở cổng vào (*input port*) và chuyển gói tin đó sang cổng xuất (*output port*) thích hợp.
  - Phạm vi: **Cục bộ (Node-local)**, diễn ra trong phần cứng router với tốc độ nano-giây dựa trên **Bảng chuyển tiếp (Forwarding Table)**.

> [!NOTE]
> **Ví dụ thực tế:**
> - **Routing** giống như việc bạn mở bản đồ Google Maps lên để lên kế hoạch chọn tuyến đường đi từ Hà Nội vào TP.HCM (tính toán toàn cục).
> - **Forwarding** giống như khi xe chạy đến từng ngã tư cụ thể, bạn nhìn biển chỉ dẫn để quyết định rẽ trái, rẽ phải hay đi thẳng (hành động cục bộ).

---

### B. Băng thông (Bandwidth) vs Thông lượng (Throughput)
- `Bandwidth` (Băng thông): Tốc độ truyền dữ liệu tối đa trên **lý thuyết** của một đường truyền vật lý trong 1 giây.
  - Đơn vị đo: bps (bits/s), Kbps, Mbps, Gbps.
  - *Ví dụ:* Là **độ rộng tối đa** của con đường cao tốc.
- `Throughput` (Thông lượng): Tốc độ truyền tải dữ liệu **thực tế** đo được giữa bên gửi và bên nhận tại một thời điểm hoặc trung bình qua thời gian.
  - Luôn luôn $\le$ Băng thông do bị ảnh hưởng bởi độ trễ, hao hụt tín hiệu, hàng đợi tắc nghẽn và giao thức điều khiển luồng.
  - Bị giới hạn trực tiếp bởi liên kết có tốc độ thấp nhất trên toàn tuyến đường (**Nguyên lý nút thắt cổ chai - Bottleneck Link**).
  - *Ví dụ:* Là **lượng xe thực tế** đang lưu thông qua con đường đó.

---

### C. Các phương thức gửi tin (Transmission / Cast Modes)
- `Unicast` (1-to-1): Truyền từ **1 máy gửi tới đúng 1 máy nhận duy nhất**.
  - Ví dụ: Duyệt web HTTP/HTTPS, tải file FTP, phiên SSH.
- `Broadcast` (1-to-all): Truyền từ **1 máy gửi tới TẤT CẢ các máy khác** trong cùng một miền quảng bá (Local Network / Broadcast Domain).
  - Thường dùng trong các giao thức khám phá cấu hình tự động.
  - Ví dụ: Gói tin **DHCP Discover** (tìm server cấp IP), gói tin **ARP Request** (tìm địa chỉ MAC đích bằng địa chỉ phát sóng `FF:FF:FF:FF:FF:FF`).
- `Multicast` (1-to-many): Truyền từ **1 máy gửi tới một NHÓM máy xác định** có đăng ký tham gia nhóm (*Multicast Group*).
  - Giúp tiết kiệm băng thông khi truyền cùng một nội dung cho nhiều người cùng lúc.
  - Ví dụ: Truyền hình trực tiếp qua mạng (IPTV), livestream hội nghị trực tuyến, cập nhật bảng định tuyến OSPF/RIP.
- `Anycast` (1-to-nearest): Gửi từ 1 máy tới **máy chủ gần nhất** về mặt định tuyến mạng trong một cụm các máy chủ cùng dùng chung 1 địa chỉ IP (được triển khai cực kỳ phổ biến trong hệ thống 13 cụm DNS Root toàn cầu và mạng phân phối nội dung CDN của Cloudflare, Google).

---

### D. Các chế độ truyền dẫn (Duplex Modes)
- `Simplex` (Đơn công): Dữ liệu chỉ có thể truyền theo **một chiều duy nhất** cố định.
  - Ví dụ: Truyền hình vệ tinh, phát thanh Radio FM, tín hiệu chuột/bàn phím gửi vào máy tính.
- `Half-duplex` (Bán song công): Dữ liệu có thể truyền theo cả 2 chiều, nhưng **KHÔNG ĐƯỢC cùng một lúc** (tại một thời điểm, thiết bị chỉ có thể gửi HOẶC nhận).
  - Ví dụ: Máy bộ đàm Walkie-Talkie (khi nói thì không thể nghe đối phương), mạng Ethernet cổ điển dùng Hub chung môi trường (áp dụng thuật toán phát hiện xung đột CSMA/CD), mạng Wi-Fi không dây chuẩn 802.11.
- `Full-duplex` (Song công toàn phần): Dữ liệu có thể gửi VÀ nhận **đồng thời tại cùng một thời điểm**.
  - Ví dụ: Cuộc gọi điện thoại (hai người có thể nói và nghe cùng lúc), mạng Ethernet hiện đại nối qua Switch (sử dụng 2 cặp dây riêng biệt: một cặp chuyên truyền TX (Transmit) và một cặp chuyên nhận RX (Receive), triệt tiêu hoàn toàn xung đột tín hiệu).

---

### E. Cấu trúc thiết bị Gateway gia đình (All-in-one Home Gateway)
Hộp thiết bị mạng quen thuộc tại mỗi gia đình (thường được gọi ngắn gọn là "Cục Modem" hay "Router Wi-Fi") thực tế là thiết bị tích hợp **3 phần cứng chuyên trách độc lập trong 1 thân máy**:
1. `Modem` (Modulator / Demodulator): Chuyển đổi tín hiệu quang (*PON / AON*) từ nhà cung cấp dịch vụ mạng (ISP) thành chuỗi bit điện số (*Digital Bits*).
2. `Router`: Định tuyến lưu lượng giữa mạng LAN nội bộ gia đình (dải IP Private `192.168.1.0/24`) và mạng Internet công cộng (WAN), chạy máy chủ **DHCP** để tự động cấp phát IP, và thực hiện biên dịch địa chỉ **NAT** để bảo mật dải IP nội bộ.
3. `Access Point (AP)`: Điểm truy cập không dây, phát sóng radio Wi-Fi để làm cầu nối cho các thiết bị không dây (smartphone, laptop) hòa vào mạng LAN có dây.

---

### F. RTT (Round-Trip Time) & TTL (Time-To-Live)

- **RTT (Round-Trip Time)**:
  - **Lý thuyết**: Là khoảng thời gian (tính bằng mili-giây, ms) cần thiết để một gói tin dữ liệu đi từ máy gửi đến máy nhận và nhận lại tín hiệu phản hồi (ACK / Reply).
  - **Ý nghĩa**: Thước đo trực tiếp phản ánh độ trễ mạng, được đo qua lệnh `ping` và là cơ sở cốt lõi để các giao thức (như TCP) tính toán thời gian chờ timeout và kiểm soát tốc độ truyền dữ liệu.

- **TTL (Time-To-Live)**:
  - **Lý thuyết**: Là cơ chế ấn định thời gian sống hoặc số bước nhảy (Hop) tối đa cho một gói tin hoặc bản ghi dữ liệu trước khi nó bị hủy bỏ.
  - **Ý nghĩa**: Ngăn chặn tình trạng gói tin bay vô tận làm tê liệt hệ thống khi xảy ra vòng lặp định tuyến (*Routing Loop*), đồng thời giúp tự động giải phóng các bản ghi tạm thời (*Cache*) đã lỗi thời.

---

## 1.3. Chuyển mạch: Circuit Switching vs Packet Switching

### A. Circuit Switching (Chuyển mạch kênh)
Tài nguyên mạng (băng thông, khe thời gian) dọc theo tuyến đường giữa 2 bên gửi-nhận được **dành riêng (dedicated)** cho nhau trong suốt phiên kết nối.
- **Ưu điểm**: Cam kết hiệu năng cố định (băng thông, độ trễ ổn định), phù hợp cho mạng điện thoại truyền thống (PSTN).
- **Nhược điểm**: Lãng phí tài nguyên khổng lồ khi các bên im lặng, quá trình thiết lập kênh tốn thời gian.
- **Phương pháp phân chia kênh (FDM & TDM)**:
  - `FDM (Frequency-Division Multiplexing - Ghép kênh theo tần số)`: Dải tần số truyền dẫn (quang, điện từ) được chia thành nhiều dải tần hẹp (*narrow frequency bands*). Mỗi cuộc gọi được phân bổ một dải tần riêng và có thể truyền liên tục theo thời gian trong dải tần đó.
    ```text
    4 Users đại diện:  [U1: User 1]   [U2: User 2]   [U3: User 3]   [U4: User 4]
    Mỗi user sở hữu trọn vẹn 1 dải băng tần hẹp và truyền liên tục theo thời gian.

    Tần số
    (frequency)
    ▲
    │ ┌────────────────────────────────────────────────────────────┐
    │ │                             U1                             │ ◄── Băng tần 1 (User 1)
    │ ├────────────────────────────────────────────────────────────┤
    │ │                             U2                             │ ◄── Băng tần 2 (User 2)
    │ ├────────────────────────────────────────────────────────────┤
    │ │                             U3                             │ ◄── Băng tần 3 (User 3)
    │ ├────────────────────────────────────────────────────────────┤
    │ │                             U4                             │ ◄── Băng tần 4 (User 4)
    │ └────────────────────────────────────────────────────────────┘
    └─────────────────────────────────────────────────────────────────► Thời gian (time)
    ```

  - `TDM (Time-Division Multiplexing - Ghép kênh theo thời gian)`: Trục thời gian được chia thành nhiều khung lặp lại, mỗi khung chia thành nhiều khe thời gian (*time slots*). Mỗi cuộc gọi được phân bổ định kỳ một hoặc nhiều khe thời gian cố định, và được phép truyền ở tốc độ tối đa của toàn bộ dải tần rộng trong suốt khe thời gian của mình.
    ```text
    4 Users đại diện:  [U1: User 1]   [U2: User 2]   [U3: User 3]   [U4: User 4]
    Mỗi user sở hữu toàn bộ 1 băng tần rộng và truyền với tốc độ tối đa trong khe thời gian của mình.

    Tần số
    (frequency)
    ▲
    │ ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
    │ │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │ ▲
    │ │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │ │ Toàn bộ
    │ │U1 │U2 │U3 │U4 │U1 │U2 │U3 │U4 │U1 │U2 │U3 │U4 │U1 │U2 │U3 │U4 │ │ băng tần
    │ │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │ │ rộng
    │ │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │ ▼
    │ └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
    └─────────────────────────────────────────────────────────────────► Thời gian (time)
      |◄── Khung 1 ──►|◄── Khung 2 ──►|◄── Khung 3 ──►|◄── Khung 4 ──►|
    ```

### B. Packet Switching (Chuyển mạch gói)
Dữ liệu được chia thành các gói nhỏ (**Packets**). Các gói tin di chuyển độc lập qua mạng và dùng chung đường truyền theo nhu cầu.
- **Cơ chế Lưu trữ và Chuyển tiếp (Store-and-Forward)**: Toàn bộ gói tin phải đến router trọn vẹn và được kiểm tra tính toàn vẹn trước khi router bắt đầu truyền bit đầu tiên ra cổng xuất.
- **Hàng đợi & Xung đột (Queuing Delay & Loss)**: Nếu tốc độ đến của các gói vượt quá dung lượng kênh ra, gói tin phải đứng chờ trong bộ đệm (*buffer*). Khi buffer đầy, các gói đến sau sẽ bị **loại bỏ (Drop / Packet Loss)**.

```text
SO SÁNH CƠ CHẾ CHUYỂN MẠCH
[Circuit Switching: Dành riêng tài nguyên]
┌──────────┐                                                   ┌──────────┐
│  Host A  │ ═════[ Dành riêng kênh 1 (FDM/TDM) ]════════════> │  Host B  │
└──────────┘                                                   └──────────┘

[Packet Switching: Store-and-Forward + Chia sẻ đường truyền]
┌──────────┐     ┌───────┬───────┐      ┌──────────┐     ┌───────┐      ┌──────────┐
│  Host A  │ ───>│ Gói 2 │ Gói 1 │ ───> │  ROUTER  │ ───>│ Gói 1 │ ───> │  Host B  │
└──────────┘     └───────┴───────┘      │ ┌──────┐ │     └───────┘      └──────────┘
                                        │ │Buffer│ │
┌──────────┐     ┌───────┐              │ │Queue │ │
│  Host C  │ ───>│ Gói A │ ────────────>│ └──────┘ │
└──────────┘     └───────┘              └──────────┘
```

| Tiêu chí | Chuyển mạch kênh (Circuit) | Chuyển mạch gói (Packet) |
| :--- | :--- | :--- |
| **Cấp phát tài nguyên** | Cố định, dành riêng (Dedicated) | Theo nhu cầu thực tế (Statistical multiplexing) |
| **Thiết lập kết nối** | Bắt buộc | Không cần thiết lập kênh vật lý trước |
| **Hiệu suất sử dụng tài nguyên** | Thấp khi dữ liệu truyền dạng cụm | Rất cao, tận dụng tối đa băng thông rảnh |
| **Hiện tượng nghẽn mạng** | Bị từ chối cuộc gọi lúc khởi tạo | Trễ tăng dần trong hàng đợi, có thể rớt gói (Drop) |

---

## 1.4. Bốn thành phần của độ trễ gói tin (Nodal Delay)
Tổng độ trễ tại một nút mạng ($d_{nodal}$) gồm 4 thành phần độc lập:

$$d_{nodal} = d_{proc} + d_{queue} + d_{trans} + d_{prop}$$

```text
CÁC THÀNH PHẦN ĐỘ TRỄ TẠI MỘT HOP ROUTER
                  Router A                                            Router B
          ┌───────────────────────┐                          ┌───────────────────────┐
          │ [1] d_proc: Kiểm tra  │                          │                       │
          │     header, CRC bit   │                          │                       │
          │          │            │                          │                       │
          │          ▼            │                          │                       │
Packet ──>│ [2] d_queue: Xếp hàng │                          │                       │
          │     chờ trong Buffer  │                          │                       │
          │          │            │                          │                       │
          │          ▼            │                          │                       │
          │ [3] d_trans: Đẩy bit  │ ═════[ 4. d_prop ]═════> │ Nhận gói tin...       │
          │     ra dây dẫn (L/R)  │      Lan truyền tín hiệu │                       │
          └───────────────────────┘      trên dây (d/s)      └───────────────────────┘
```

1. **Trễ xử lý ($d_{proc}$ - Processing Delay)**: Thời gian đọc tiêu đề gói tin, kiểm tra lỗi bit (checksum/CRC), tra bảng định tuyến để tìm cổng ra. Thường tính bằng microsecond ($\mu s$).
2. **Trễ xếp hàng ($d_{queue}$ - Queuing Delay)**: Thời gian gói tin nằm chờ trong hàng đợi để cổng xuất rảnh.
   - Định nghĩa cường độ lưu lượng: $I = \frac{L \cdot a}{R}$
   - Trong đó: $L$ = kích thước gói (bits), $a$ = tốc độ gói đến trung bình (packets/s), $R$ = tốc độ đường truyền (bps).

> [!IMPORTANT]
> **Ý nghĩa của Cường độ lưu lượng ($I = \frac{L \cdot a}{R}$)**:
> - **$I \approx 0$**: Hàng đợi gần như trống, độ trễ xếp hàng $d_{queue} \approx 0$.
> - **$I \to 1$**: Hàng đợi phình to, $d_{queue}$ tăng rất nhanh theo hàm tiệm cận.
> - **$I > 1$**: Lưu lượng đến nhanh hơn năng lực xử lý, hàng đợi tràn (*Buffer Overflow*), gói tin bị **drop**.

3. **Trễ truyền dẫn ($d_{trans}$ - Transmission Delay)**: Thời gian cần thiết để đẩy toàn bộ các bit của gói tin lên đường truyền vật lý.
   - Công thức tính:
     $$d_{trans} = \frac{L}{R}$$
   - Trong đó:
     - $L$: Dung lượng của gói tin (đo bằng bits).
     - $R$: Băng thông / tốc độ phát của liên kết (đo bằng bps hoặc bits/s).

4. **Trễ lan truyền ($d_{prop}$ - Propagation Delay)**: Thời gian cần thiết để 1 bit di chuyển từ đầu dây truyền dẫn sang đầu bên kia trong môi trường vật lý.
   - Công thức tính:
     $$d_{prop} = \frac{d}{s}$$
   - Trong đó:
     - $d$: Khoảng cách vật lý giữa hai nút mạng (đo bằng meters).
     - $s$: Vận tốc lan truyền tín hiệu trong môi trường dẫn ($s \approx 2 \times 10^8 \text{ m/s}$ trong cáp, xấp xỉ tốc độ ánh sáng).

> [!TIP]
> **Phân biệt trực quan $d_{trans}$ và $d_{prop}$ (Hãy tưởng tượng trạm thu phí):**
> - **$d_{trans}$** ví như thời gian đoàn xe đi qua cổng soát vé (xe to hay nhỏ, trạm soát nhanh hay chậm $\rightarrow$ phụ thuộc dung lượng $L$ và tốc độ $R$).
> - **$d_{prop}$** ví như thời gian chiếc xe sau khi qua trạm di chuyển từ trạm thu phí A sang trạm thu phí B trên đường cao tốc (phụ thuộc chiều dài quãng đường $d$ và tốc độ xe chạy $s$, hoàn toàn không phụ thuộc xe to hay nhỏ).

---

## 1.5. Thông lượng (Throughput) & Nút thắt cổ chai (Bottleneck)
- **Throughput**: Tốc độ thực tế truyền tải dữ liệu thành công từ máy gửi tới máy nhận tại một thời điểm (đo bằng bps, Mbps).
- **Bottleneck Link**: Đường truyền có dung lượng truyền tải nhỏ nhất trên toàn bộ hành trình end-to-end. Throughput thực tế không thể vượt quá dung lượng của liên kết cổ chai này.

```text
NGUYÊN LÝ NÚT THẮT CỔ CHAI (BOTTLENECK LINK)
┌────────────┐                          ┌────────────┐                         ┌────────────┐
│   Server   │ ═════(Rs = 100 Mbps)═══> │   Router   │ ════(Rc = 1.5 Mbps)═══> │   Client   │
└────────────┘                          └────────────┘           ▲             └────────────┘
                                                                 │
                                               Bottleneck Link: Throughput = 1.5 Mbps
```

---

## 1.6. Các tầng giao thức & Mô hình dịch vụ (Layered Architecture)
Kiến trúc mạng sử dụng mô hình phân tầng giúp mô-đun hóa hệ thống phức tạp: mỗi tầng cung cấp dịch vụ cho tầng ngay trên nó thông qua giao diện chuẩn (API).

```text
SO SÁNH MÔ HÌNH TCP/IP 5 TẦNG VÀ OSI 7 TẦNG
┌─────────────────────────┐                      ┌─────────────────────────┐
│  Mô hình TCP/IP 5 tầng  │                      │    Mô hình OSI 7 tầng   │
├─────────────────────────┤                      ├─────────────────────────┤
│ 5. Application          │ <──────────────────> │ 7. Application          │
│    (Gộp cả 3 tầng)      │                      │ 6. Presentation         │
│                         │                      │ 5. Session              │
├─────────────────────────┤                      ├─────────────────────────┤
│ 4. Transport            │ <──────────────────> │ 4. Transport            │
├─────────────────────────┤                      ├─────────────────────────┤
│ 3. Network              │ <──────────────────> │ 3. Network              │
├─────────────────────────┤                      ├─────────────────────────┤
│ 2. Data Link            │ <──────────────────> │ 2. Data Link            │
├─────────────────────────┤                      ├─────────────────────────┤
│ 1. Physical             │ <──────────────────> │ 1. Physical             │
└─────────────────────────┘                      └─────────────────────────┘
```

- **Tầng Presentation (OSI)**: Định dạng dữ liệu, nén dữ liệu, mã hóa dữ liệu. Trong TCP/IP, công việc này do chính ứng dụng đảm nhận.
- **Tầng Session (OSI)**: Đồng bộ hóa, thiết lập điểm kiểm tra (*checkpoints*) và phục hồi phiên trao đổi dữ liệu.

---

<a id="chuong-2"></a>
# CHƯƠNG 2: TẦNG ỨNG DỤNG (APPLICATION LAYER)
> 📄 **Slide bài giảng:** [Chapter_2_v9.0.pdf](.pdf/Chapter_2_v9.0.pdf)

## 2.1. Nguyên lý kiến trúc ứng dụng mạng
Tầng ứng dụng là nơi các lập trình viên triển khai phần mềm mạng chạy trên các hệ thống đầu cuối (*End Systems*). Thiết bị mạng lõi (Router, Switch) hoàn toàn không can thiệp vào tầng này.

### Mô hình triển khai:
1. **Client-Server Architecture**:
   - **Server**: Máy chủ luôn bật (*always-on*), có địa chỉ IP cố định, tài nguyên lớn (thường đặt trong các Data Center).
   - **Client**: Thiết bị người dùng, kết nối ngắt quãng, địa chỉ IP động, **không giao tiếp trực tiếp với nhau**.
2. **Peer-to-Peer (P2P) Architecture**:
   - Gần như không phụ thuộc vào máy chủ trung tâm.
   - Các cặp nút mạng bình đẳng (*peers*) giao tiếp trực tiếp và chia sẻ tài nguyên cho nhau (ví dụ: BitTorrent).
   - **Khả năng tự mở rộng (Self-scalability)**: Càng nhiều peer tham gia tải đồng thời thì năng lực cung cấp dữ liệu của toàn mạng càng tăng.

### Giao diện Lập trình Socket:
Socket là **"cánh cửa"** phần mềm trung gian giữa tiến trình ứng dụng (Application Layer - do lập trình viên điều khiển) và hệ điều hành quản lý mạng (Transport Layer - do OS kernel quản lý). Có chức năng giao quyền từ user lại cho OS (Hệ điều hành), chuyển dữ liệu về dạng mà OS có thể xử lý được, xác định chọn giao thức TCP hoặc UDP.

```text
VỊ TRÍ CỦA SOCKET TRONG MÔ HÌNH HỆ THỐNG
┌───────────────────────────────────────────────────────┐
│ Application Process (Trình duyệt, Web Server, ...)    │  <── Tầng ứng dụng (User space)
└───────────────────────────────────────────────────────┘
                       │        ▲
                       ▼        │
                  [   S O C K E T   ]                      <── Cánh cửa giao tiếp (API)
                       │        ▲
┌──────────────────────▼────────┴───────────────────────┐
│ OS Network Subsystem (TCP / UDP)                      │  <── Tầng giao vận (Kernel space)
│ IP Layer, Network Card Driver                         │
└───────────────────────────────────────────────────────┘
```

---

### Các dịch vụ tầng Giao vận sẵn có: TCP vs UDP
Trước khi tiến trình ứng dụng có thể trao đổi thông điệp qua Socket, lập trình viên bắt buộc phải lựa chọn giữa hai giao thức giao vận nền tảng của Internet:

| Tiêu chí so sánh | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Thiết lập kết nối** | **Hướng kết nối (Connection-oriented)**: Bắt buộc thiết lập phiên qua việc bắt tay 3 bước (*3-Way Handshake*) trước khi truyền dữ liệu | **Không kết nối (Connectionless)**: Chuyển dữ liệu đi ngay lập tức mà không cần kết nối trước |
| **Tính tin cậy** | **Tin cậy 100% (Reliable Data Transfer)**: Đảm bảo không mất gói, không lỗi bit, dữ liệu đến đúng thứ tự tuần tự | **Không tin cậy (Best-effort)**: Gói tin có thể bị mất, trùng lặp hoặc đến lộn xộn, không gửi lại gói mất |
| **Kiểm soát luồng & nghẽn** | **Có đầy đủ**: Kiểm soát luồng (*Flow Control*) chống tràn bộ đệm bên nhận, kiểm soát tắc nghẽn (*Congestion Control*) tự hạ tốc độ khi mạng nghẽn | **Hoàn toàn không**: Ứng dụng đẩy dữ liệu nhanh bao nhiêu thì UDP phát đi bấy nhiêu, không quan tâm mạng nghẽn |
| **Kích thước Header** | Nặng: $20 - 60$ bytes (chứa Sequence, ACK, Window size, Flags) | Cực nhẹ: Đúng $8$ bytes (chỉ gồm Port, Length, Checksum) |
| **Tốc độ & Độ trễ** | Chậm hơn, độ trễ biến thiên do tốn thời gian bắt tay và chờ truyền lại (*Retransmission*) | Tốc độ tối đa, độ trễ tối thiểu, truyền tức thì |
| **Ứng dụng tiêu biểu** | Cần tính chính xác tuyệt đối: Web (HTTP/HTTPS), Email (SMTP, IMAP), Tải file (FTP), Dòng lệnh từ xa (SSH) | Cần độ trễ thấp, chấp nhận rơi vài gói: DNS, Video call/Livestream (VoIP, Zoom), Game online thời gian thực, HTTP/3 (QUIC) |

```text
SO SÁNH CƠ CHẾ TRUYỀN DỮ LIỆU CỦA TCP VÀ UDP

1. TCP: Bắt tay 3 bước -> Truyền tin cậy, kiểm soát thứ tự chặt chẽ
   Client (Tiến trình A)                                Server (Tiến trình B)
       │                                                         │
       │ ─────── 1. SYN (Xin bắt tay) ──────────────────────────>│ (Khởi tạo Socket con)
       │ <────── 2. SYN-ACK (Đồng ý & Bắt tay lại) ──────────────│
       │ ─────── 3. ACK (Xác nhận hoàn tất) ────────────────────>│
      ═════[ KẾT NỐI ĐƯỢC THIẾT LẬP - BẮT ĐẦU TRUYỀN DỮ LIỆU ]═════
       │ ─────── Gói 1 (Seq=1) ─────────────────────────────────>│ ──> Nhận đúng -> Trả ACK 1
       │ ─────── Gói 2 (Seq=2) ──────────x (Bị rớt trên mạng)    │
       │ ─────── Gói 3 (Seq=3) ─────────────────────────────────>│ ──> Chưa nhận được Gói 2
       │ <────── Gửi lại ACK 1 đòi Gói 2 ────────────────────────│
       │ ─────── Truyền lại Gói 2 ──────────────────────────────>│ ──> Nhận đủ -> Ghép dữ liệu
       ...

2. UDP: Không cần kết nối -> Chuyển gói tin liên tục với tốc độ cao nhất
   Client (Tiến trình A)                                Server (Tiến trình B)
       │ ═══════ Datagram 1 (Chuyển đi ngay) ═══════════════════>│ (Nhận và đẩy lên App)
       │ ═══════ Datagram 2 ─────────────x (Rớt gói)             │ (Không có cơ chế báo mất)
       │ ═══════ Datagram 3 (Chuyển tiếp) ══════════════════════>│ (Nhận tiếp bình thường)
       (Không chờ phản hồi ACK, không truyền lại gói mất, tối ưu độ trễ cho thời gian thực)
```

---

## 2.2. Web và Giao thức HTTP

Giao thức **HTTP (Hypertext Transfer Protocol)** là giao thức nền tảng của mạng Web toàn cầu, hoạt động theo mô hình **Request - Response** thông qua kết nối truyền thông tin cậy của **TCP** (mặc định cổng 80 cho HTTP và cổng 443 cho HTTPS).

---

### A. Cấu trúc địa chỉ URL (Uniform Resource Locator)
Mỗi đối tượng tài nguyên trên World Wide Web (trang HTML, ảnh PNG/JPEG, video MP4, file PDF, API JSON) đều được định danh duy nhất bằng một địa chỉ **URL**.

```text
CẤU TRÚC HOÀN CHỈNH CỦA MỘT ĐỊA CHỈ URL
┌────────┬───┬───────────────────┬─────┬─────────────────┬─────────────────────┬──────────┐
│ https  │://│  api.example.com  │:443 │ /v1/users/info  │ ?id=102&format=json │ #profile │
└────────┴───┴───────────────────┴─────┴─────────────────┴─────────────────────┴──────────┘
 Protocol         Host Name        Port      Path Name         Query String        Anchor
(Giao thức)    (Tên miền / IP)    (Cổng)    (Đường dẫn)     (Tham số truy vấn)  (Vị trí neo)
```

- **Protocol (Giao thức / Scheme)**: Xác định phương thức giao tiếp để lấy tài nguyên (`http`, `https`, `ftp`, `file`).
- **Host Name (Tên miền hoặc Địa chỉ IP)**: Chỉ định máy chủ đích lưu trữ tài nguyên trên Internet (ví dụ: tên miền `api.example.com` hoặc IP `192.168.1.1`).
- **Port (Cổng kết nối)**: Cổng do ứng dụng web lắng nghe trên server (mặc định HTTP là `80`, HTTPS là `443`; nếu dùng cổng mặc định thì trình duyệt tự động ẩn đi).
- **Path Name (Đường dẫn tài nguyên)**: Đường dẫn phân cấp thư mục tới file hoặc API endpoint trên máy chủ, luôn bắt đầu bằng dấu `/` (ví dụ: `/v1/users/info`).
- **Query String (Chuỗi truy vấn)**: Bắt đầu sau dấu `?`, chứa các cặp dữ liệu `key=value` nối nhau bởi dấu `&`, dùng để truyền tham số lọc, phân trang, tìm kiếm cho server (ví dụ: `?id=102&format=json`).
- **Anchor / Fragment (Vị trí neo)**: Bắt đầu sau dấu `#`, chỉ định vị trí thẻ đánh dấu bên trong trang web để trình duyệt tự động cuộn màn hình đến đó ngay sau khi tải xong (ví dụ: `#profile`).

---

### B. Các mã trạng thái phản hồi HTTP (HTTP Status Codes)
Sau khi nhận được HTTP Request từ Client, Server luôn gửi về một dòng trạng thái (*Status Line*) chứa **Mã trạng thái gồm 3 chữ số** để thông báo kết quả xử lý. Mã trạng thái được chuẩn hóa quốc tế thành 5 nhóm lớn:

| Nhóm mã | Tên gọi & Ý nghĩa | Các mã trạng thái tiêu biểu thường gặp nhất |
| :--- | :--- | :--- |
| **`1xx`** | **Informational** (Thông tin): Tiếp nhận yêu cầu, đang tiếp tục xử lý | - `100 Continue`: Server đã nhận phần Header, Client hãy tiếp tục gửi phần Body còn lại.<br>- `101 Switching Protocols`: Server đồng ý chuyển đổi giao thức (ví dụ: nâng cấp từ HTTP/1.1 lên WebSocket). |
| **`2xx`** | **Success** (Thành công): Yêu cầu đã được server tiếp nhận, hiểu và xử lý hoàn tất | - `200 OK`: Thành công hoàn hảo, dữ liệu yêu cầu nằm trong phần body phản hồi.<br>- `201 Created`: Tạo mới tài nguyên thành công (thường trả về sau lệnh `POST`).<br>- `204 No Content`: Xử lý thành công nhưng không có dữ liệu nội dung trả về trong body. |
| **`3xx`** | **Redirection** (Điều hướng): Client cần chuyển hướng sang URL khác để hoàn tất | - `301 Moved Permanently`: Tài nguyên đã chuyển vĩnh viễn sang URL mới (trình duyệt tự lưu cache URL mới cho các lần sau).<br>- `302 Found` / `307 Temporary Redirect`: Điều hướng tạm thời sang URL khác.<br>- `304 Not Modified`: Tài nguyên trên server chưa hề bị sửa đổi kể từ thời điểm client chỉ định (dùng trong cơ chế Web Cache để tiết kiệm băng thông). |
| **`4xx`** | **Client Error** (Lỗi phía Client): Yêu cầu gửi lên bị sai cú pháp hoặc không hợp lệ | - `400 Bad Request`: Yêu cầu sai cú pháp, server không thể hiểu được.<br>- `401 Unauthorized`: Chưa đăng nhập / thiếu token xác thực danh tính.<br>- `403 Forbidden`: Đã đăng nhập nhưng server từ chối cấp quyền truy cập tài nguyên này.<br>- `404 Not Found`: Không tìm thấy tài nguyên trên server (URL sai hoặc tài nguyên đã bị xóa).<br>- `405 Method Not Allowed`: Phương thức HTTP không được hỗ trợ cho endpoint này (vd dùng POST vào URL chỉ nhận GET).<br>- `429 Too Many Requests`: Client gửi quá nhiều request trong thời gian ngắn (bị chặn bởi hệ thống Rate Limiting chống spam/DDoS). |
| **`5xx`** | **Server Error** (Lỗi phía Server): Máy chủ gặp lỗi nội bộ khi xử lý request hợp lệ | - `500 Internal Server Error`: Server gặp lỗi code hoặc sập dịch vụ nội bộ.<br>- `502 Bad Gateway`: Proxy / Gateway nhận phản hồi lỗi từ máy chủ backend phía sau.<br>- `503 Service Unavailable`: Server đang quá tải tạm thời hoặc đang bảo trì định kỳ.<br>- `504 Gateway Timeout`: Proxy / Gateway hết thời gian chờ phản hồi từ máy chủ backend.<br>- `505 HTTP Version Not Supported`: Server từ chối phiên bản giao thức HTTP mà client gửi lên. |

---

### C. Cơ chế duy trì trạng thái: Cookies & Phân loại Cookies
Bản chất của giao thức HTTP là **không lưu trạng thái (Stateless)**: Server không ghi nhớ bất kỳ điều gì về các yêu cầu trước đó của client. Để duy trì trạng thái làm việc (phiên đăng nhập tài khoản, giỏ hàng thương mại điện tử, tùy chọn cá nhân), HTTP sử dụng **Cookies**:

1. Khi client đăng nhập thành công, server tạo SessionID trong cơ sở dữ liệu và gửi header phản hồi: `Set-Cookie: id=789`
2. Trình duyệt client tự động lưu cookie này vào bộ nhớ an toàn trên máy.
3. Ở tất cả các request tiếp theo tới cùng website, trình duyệt tự động đính kèm header: `Cookie: id=789` để server nhận diện danh tính.

```text
CƠ CHẾ HOẠT ĐỘNG CỦA COOKIE & DUY TRÌ TRẠNG THÁI
┌──────────────────┐                                ┌──────────────────┐
│ Client (Browser) │                                │      Server      │
└────────┬─────────┘                                └────────┬─────────┘
         │                                                   │
         │ ──── 1. HTTP Request: Đăng nhập (user/pass) ─────>│ (Xác thực thành công)
         │                                                   │ (Tạo SessionID trong Database)
         │ <─── 2. HTTP Response: Set-Cookie: id=789 ────────│
         │                                                   │
   (Lưu cookie id=789)                                       │
         │                                                   │
         │ ──── 3. HTTP Request: Xem giỏ hàng ──────────────>│
         │         Cookie: id=789                            │ (Đọc SessionID 789 -> nhận ra user)
         │ <─── 4. HTTP Response: Dữ liệu giỏ hàng ──────────│
```

#### Phân biệt First-party Cookies vs Third-party Cookies:
- **First-party Cookies (Cookie bên thứ nhất)**:
  - Được tạo ra và sở hữu trực tiếp bởi **chính domain của trang web mà người dùng đang truy cập** (ví dụ: bạn lướt web trên `shopee.vn`, cookie được cấp bởi `shopee.vn`).
  - *Mục đích sử dụng:* Phục vụ các tính năng tiện ích cốt lõi và hoàn toàn hợp pháp của trang web như: giữ phiên đăng nhập không bị văng ra ngoài, lưu sản phẩm trong giỏ hàng, ghi nhớ ngôn ngữ hay những cài đặt ta đã chỉnh.
- **Third-party Cookies (Cookie bên thứ ba)**:
  - Được tạo ra bởi **một tên miền khác hoàn toàn với trang web bạn đang xem**. Chúng được cài cắm ngầm thông qua các banner quảng cáo, đoạn mã script phân tích (*Google Analytics*), nút like mạng xã hội hoặc "pixel theo dõi" (*Tracking Pixel* như `doubleclick.net`, `facebook.com`) được nhúng trên trang web đó.
  - *Mục đích sử dụng:* Theo dõi lịch sử và hành vi duyệt web của người dùng xuyên suốt hàng trăm website khác nhau để xây dựng hồ sơ sở thích cá nhân, từ đó phân phối các quảng cáo bám đuổi mục tiêu.
  - *Vấn đề an toàn & quyền riêng tư:* Gây lo ngại nghiêm trọng về lộ thông tin cá nhân và bị giám sát hành vi. Do đó, các trình duyệt hiện đại (Safari, Firefox, Chrome) hiện nay đã và đang tiến tới việc **chặn mặc định toàn bộ** Third-party cookies.

---

### D. Máy chủ đệm web: Web Cache (Proxy Server) & Cơ chế Conditional GET

#### 1. Web Cache (Proxy Server) là gì?
**Web Cache** (còn gọi là **Proxy Server**) là một thực thể mạng đóng vai trò trung gian đứng giữa các Client (trình duyệt người dùng trong mạng nội bộ) và Máy chủ gốc (*Origin Server* trên Internet). Web Cache sở hữu ổ cứng và bộ nhớ đệm riêng để lưu trữ bản sao của các tài nguyên web (HTML, ảnh, video, CSS) vừa được người dùng tải về gần đây.

Web Cache thường được các trường đại học, cơ quan doanh nghiệp hoặc nhà mạng viễn thông (ISP) lắp đặt ngay tại **rìa mạng nội bộ (gần người dùng nhất có thể)**.

```text
KIẾN TRÚC MÁY CHỦ ĐỆM WEB (WEB CACHE / PROXY SERVER)
[ MẠNG LAN CƠ QUAN / TRƯỜNG HỌC ]                           [ INTERNET CÔNG CỘNG ]
┌──────────┐
│ Client A │ ──────┐
└──────────┘       │
                   ▼
┌──────────┐   ┌──────────────────────────┐      Liên kết truy cập      ┌───────────────────────┐
│ Client B │ ─>│     Web Cache (Proxy)    │  (Access Link: Băng thông   │   Origin Web Server   │
└──────────┘   │ (Bộ nhớ đệm lưu bản sao) │======= bị giới hạn) =======>│  (Máy chủ gốc từ xa)  │
               └──────────────────────────┘                             └───────────────────────┘
```

#### 2. Nguyên lý hoạt động (Cache Hit vs Cache Miss):
1. Khi người dùng nhập địa chỉ web, trình duyệt gửi HTTP Request tới **Web Cache** trước tiên thay vì gửi thẳng ra Internet.
2. Web Cache kiểm tra kho dữ liệu của mình:
   - **Cache Hit (Trúng bộ nhớ đệm)**: Nếu Web Cache đã có sẵn bản sao của file và bản sao đó vẫn còn mới (*Fresh*), Web Cache lập tức gửi trả file đó về cho Client qua mạng LAN tốc độ cao. Gói tin **hoàn toàn không cần đi ra Internet**.
   - **Cache Miss (Trượt bộ nhớ đệm)**: Nếu chưa có file hoặc file đã quá cũ, Web Cache sẽ đóng vai trò như một Client, tự động thay mặt người dùng gửi HTTP Request lên Origin Server trên Internet để tải file gốc về. Sau đó, Web Cache lưu một bản sao vào bộ nhớ đệm của mình rồi mới chuyển tiếp cho Client.

#### 3. Lợi ích của Web Cache:
1. **Giảm thiểu thời gian phản hồi (*Response Time*)**: Người dùng tải trang web từ máy chủ Cache trong mạng LAN nội bộ (tốc độ Gigabit, độ trễ vài mili-giây) nhanh hơn hàng chục lần so với việc phải kéo dữ liệu từ máy chủ gốc đặt ở nửa bên kia quả địa cầu.
2. **Tiết kiệm băng thông ra ngoài Internet (*Bandwidth Saving*)**: Nếu 1.000 sinh viên cùng mở một video bài giảng, Web Cache chỉ cần tải video đó từ Internet đúng **1 lần duy nhất**, 999 sinh viên còn lại tải nội bộ đường truyền Internet của trường học không bị tắc nghẽn.
3. **Giảm tải áp lực cho Server gốc**: Giúp máy chủ của các công ty lớn không bị quá tải khi có lượng truy cập đột biến.

#### 4. Vấn đề đồng bộ dữ liệu: Cơ chế Conditional GET
Nếu tài nguyên trên Server gốc đã được cập nhật nội dung mới, làm sao Web Cache biết bản sao của mình đã bị cũ để không phục vụ dữ liệu lỗi thời cho người dùng? Giao thức HTTP giải quyết vấn đề này bằng **Conditional GET**:

```text
CƠ CHẾ ĐỒNG BỘ BẢN SAO BẰNG CONDITIONAL GET
Web Cache (Proxy)                                         Origin Web Server
       │                                                         │
       │───── 1. HTTP GET: "Nội dung này có sửa đổi gì           │
       │         từ ngày 01/01/2026 không?"                      │
       │         Header: If-Modified-Since: <date> ─────────────>│
       │                                                         │
      [ TRƯỜNG HỢP A: File trên Server gốc CHƯA HỀ BỊ THAY ĐỔI    ]
       │ <── 2. Server phản hồi: HTTP/1.1 304 Not Modified ──────│ (Không gửi lại Body file)
       │      (Tiết kiệm băng thông, dùng tiếp bản sao cũ)       │
       │                                                         │
      [ TRƯỜNG HỢP B: File trên Server gốc ĐÃ CÓ BẢN CẬP NHẬT MỚI ]
       │ <── 2. Server phản hồi: HTTP/1.1 200 OK ────────────────│ (Gửi kèm toàn bộ Body mới)
       │       Header: Last-Modified: <new_date> + [Dữ liệu mới] │
       │  (Web Cache ghi đè bản mới vào đĩa và trả cho Client)   │
```

---

### E. Tiến hóa các phiên bản HTTP (HTTP/1.0 -> HTTP/1.1 -> HTTP/2 -> HTTP/3)

```text
[HTTP/1.1 Pipelining: Bị lỗi Head-of-Line (HoL) Blocking ở Tầng Ứng dụng]
TCP Conn 1: [ Req 1 ][ Req 2 ][ Req 3 ] ===> Nếu Req 1 bị treo, Req 2 & 3 phải đợi!

[HTTP/2: Multiplexing qua luồng nhị phân (Binary Streams) trên 1 kết nối TCP]
TCP Conn 1: [ Frame 1-Req1 ][ Frame 1-Req2 ][ Frame 2-Req1 ][ Frame 1-Req3 ] ===> Không bị HoL tầng App!
(Tuy nhiên: Nếu 1 packet TCP bị rớt ở Tầng 4, toàn bộ các luồng bên trong đều bị nghẽn!)

[HTTP/3: Chạy trên nền QUIC (UDP) - Triệt tiêu hoàn toàn HoL Blocking!]
UDP Conn  : [ Stream 1 (độc lập) ]  [ Stream 2 (độc lập) ]  [ Stream 3 (độc lập) ]
            Gói tin của Stream 1 bị rớt KHÔNG làm gián đoạn Stream 2 & Stream 3!
```

- **HTTP/1.0**: Mở kết nối TCP riêng biệt cho từng đối tượng (Non-persistent). Tốn $2\text{ RTT}$ cho mỗi file ảnh/css.
- **HTTP/1.1**: **Persistent Connection** (giữ kết nối TCP mở để tải nhiều đối tượng liên tiếp). Hỗ trợ pipelining nhưng vẫn mắc lỗi **Head-of-Line Blocking** ở tầng ứng dụng (nếu tài nguyên đầu tiên xử lý chậm thì các tài nguyên phía sau bị nghẽn).
- **HTTP/2 (RFC 7540)**:
  - Chuyển sang định dạng **Binary Framing** thay vì văn bản thuần.
  - **Multiplexing**: Ghép nhiều luồng dữ liệu (Streams) chạy đồng thời trên duy nhất một kết nối TCP.
  - **Header Compression (HPACK)**: Nén tiêu đề request/response để tiết kiệm băng thông.
  - **Server Push**: Chủ động gửi kèm CSS/JS trước khi client kịp gửi yêu cầu.
- **HTTP/3 (RFC 9114)**:
  - Thay thế TCP bằng giao thức **QUIC** chạy trên nền **UDP**.
  - Giải quyết triệt để lỗi **TCP Head-of-Line Blocking**: Khi một gói UDP bị mất, chỉ luồng dữ liệu chứa gói đó bị dừng chờ truyền lại, các luồng độc lập khác vẫn hoạt động bình thường.
  - Tích hợp sẵn cơ chế đàm phán kết nối nhanh (0-RTT hoặc 1-RTT Connection Establishment).

> [!TIP]
> **Đột phá của HTTP/3**: Bằng việc chuyển dịch từ TCP sang giao thức QUIC (trên nền UDP), HTTP/3 không chỉ triệt tiêu hoàn toàn lỗi Head-of-Line Blocking mà còn hỗ trợ đổi mạng mượt mà (Connection Migration - đổi từ Wi-Fi sang 4G không bị đứt kết nối) nhờ quản lý bằng Connection ID thay vì bộ 4-tuple IP/Port.

---

## 2.3. Hệ thống phân giải tên miền (DNS - Domain Name System)
DNS là cơ sở dữ liệu phân tán có cấu trúc phân cấp, đảm nhiệm vai trò phiên dịch tên miền người dùng dễ nhớ (ví dụ: `www.google.com`) sang địa chỉ IP mà router có thể định tuyến (ví dụ: `142.250.190.46`). Hoạt động trên cổng **UDP 53** (và TCP 53 khi truyền vùng dữ liệu lớn - Zone Transfer).

```text
CÂY PHÂN CẤP 4 TẦNG HỆ THỐNG MÁY CHỦ DNS

                                 ┌───────────────────────────┐
                        [CẤP 1]  │   Root DNS Servers (.)    │  ◄── (13 cụm IP gốc A -> M toàn cầu)
                                 └─────────────┬─────────────┘
                                               │
                    ┌──────────────────────────┴──────────────────────────┐
                    │                                                     │
           ┌────────┴──────────┐                                 ┌────────┴──────────┐
 [CẤP 2]   │  .com TLD Server  │                                 │  .vn TLD Server   │     ◄── Top-Level Domain
           └────────┬──────────┘                                 └────────┬──────────┘         (Quản lý đuôi tên miền)
                    │                                                     │
        ┌───────────┴──────────────┐                         ┌────────────┴─────────────┐
[CẤP 3] │ google.com Authoritative │                         │ vnu.edu.vn Authoritative │  ◄── Authoritative Server
        └───────────┬──────────────┘                         └────────────┬─────────────┘      (Nắm giữ IP chính thức)
                    │ (maps.google.com -> IP)                             │ (fit.vnu.edu.vn -> IP)
                    ▲                                                     ▲
                    │                                                     │
                    └──────────────────────────┬──────────────────────────┘
                                               │ (Hỏi phân giải khi Cache Miss)
                                               |
                                 ┌─────────────▼─────────────┐
                        [CẤP 4]  │ Local DNS Server (Cục bộ) │  ◄── Default Name Server (ISP, 8.8.8.8)
                                 │ (Lưu Cache + Truy vấn hộ) │      (Đứng trung gian đại diện Client)
                                 └─────────────▲─────────────┘
                                               │ (1. Truy vấn đệ quy ban đầu)
                                               │
                                       ┌───────┴───────┐
                                       │  Client Host  │
                                       │ (Người dùng)  │
                                       └───────────────┘
```

### Các loại máy chủ DNS:
1. **Root DNS Servers**: Máy chủ gốc quản lý toàn cầu (13 cụm IP logic do ICANN quản lý).
2. **Top-Level Domain (TLD) Servers**: Quản lý các đuôi tên miền cấp 1 (`.com`, `.net`, `.org`, `.gov`, `.vn`).
3. **Authoritative DNS Servers**: Máy chủ có thẩm quyền chính thức của các tổ chức, nắm giữ bản ghi IP chuẩn xác của tổ chức đó.
4. **Local DNS Server (Resolving Name Server)**: Máy chủ DNS cục bộ (như `8.8.8.8` của Google, `1.1.1.1` của Cloudflare, hoặc DNS của ISP). Tiếp nhận truy vấn từ người dùng và đi lùng sục khắp cây phân cấp DNS để tìm kết quả.

### Truy vấn Đệ quy (Recursive) vs Truy vấn Lặp (Iterative):

```text
QUÁ TRÌNH TRUY VẤN DNS ITERATIVE (LẶP)
 ┌───────────────┐
 │  Client Host  ├──────◄─────────◄────────────◄───────────◄──────────────◄──────────┐
 └───────┬───────┘                                                                   │
         │ (1) Truy vấn đệ quy                                                       │
         ▼                                                                           │
┌──────────────────┐ ──── (2) Hỏi: IP của "example.com"? ────> ┌─────────────────┐   │
│ Local DNS Server │                                           │ Root DNS Server │   │
│                  │ <─── (3) Trả lời: Hãy hỏi TLD .com ────── └─────────────────┘   │
│                  │                                                                 │
│                  │ ──── (4) Hỏi: IP của "example.com"? ────> ┌─────────────────┐   │
│                  │                                           │ .com TLD Server │   │
│                  │ <─── (5) Trả lời: Hãy hỏi Auth Server ─── └─────────────────┘   │
│                  │                                                                 │
│                  │ ──── (6) Hỏi: IP của "example.com"? ────> ┌─────────────────┐   │
│                  │                                           │Authoritative DNS│   │
│                  │ <─── (7) Trả lời: 93.184.216.34 ───────── └─────────────────┘   │
└───────┬──────────┘                                                                 │
        │                                                                            │
        └────►───────►─── (8) Trả lời IP cuối cùng cho Client Host ───►─────────►────┘
```

### Các loại bản ghi DNS tài nguyên (Resource Records - RR):
Cấu trúc bản ghi: `(Name, Value, Type, TTL (Time-To-Live))`
- **Type A**: Name là Hostname, Value là địa chỉ IPv4 (vd: `google.com` $\to$ `142.250.190.46`).
- **Type AAAA**: Phiên dịch sang địa chỉ IPv6.
- **Type CNAME**: Tên miền bí danh trỏ về tên miền chuẩn Canonical Name (vd: `mail.google.com` $\to$ `ghs.google.com`).
- **Type NS**: Trỏ tới tên máy chủ Authoritative chịu trách nhiệm quản lý tên miền (vd: `google.com` $\to$ `ns1.google.com`).
- **Type MX**: Tên máy chủ xử lý thư điện tử (Mail Server) của miền.
- **Type TXT**: Dữ liệu văn bản tùy biến.

---

## 2.4. Giao thức Email: SMTP, IMAP và POP3
- **SMTP (Simple Mail Transfer Protocol - RFC 5321 - Port 25/587)**: Giao thức đẩy thư (*Push protocol*). Được dùng để gửi thư từ Client lên Mail Server và trung chuyển thư giữa các Mail Server với nhau.
- **POP3 (Post Office Protocol v3 - Port 110/995)**: Giao thức kéo (*Pull protocol*). Tải toàn bộ thư về máy cục bộ và mặc định xóa thư trên server, không đồng bộ được trạng thái đọc giữa nhiều thiết bị.
- **IMAP (Internet Message Access Protocol - RFC 3501 - Port 143/993)**: Lưu trữ và đồng bộ hóa thư trực tiếp trên server, cho phép quản lý thư mục, cờ đánh dấu từ nhiều thiết bị đồng thời.

---

## 2.5. Lập trình Socket cơ bản (Socket API)
Socket cung cấp giao diện lập trình để các tiến trình trao đổi dữ liệu:
- **TCP Socket (Stream Socket - SOCK_STREAM)**: Hướng kết nối, đảm bảo dữ liệu truyền đến nơi đúng thứ tự và nguyên vẹn.
- **UDP Socket (Datagram Socket - SOCK_DGRAM)**: Không kết nối, truyền các gói tin độc lập với độ trễ tối thiểu.

```text
MÔ HÌNH LUỒNG HOẠT ĐỘNG CỦA TCP SOCKET (CLIENT - SERVER)
┌─────────────────────────┐                                 ┌─────────────────────────┐
│       TCP Server        │                                 │       TCP Client        │
└────────────┬────────────┘                                 └────────────┬────────────┘
             │                                                           │
   socket() ─┼─> bind() ──> listen()                                     │
             │   (Lắng nghe cổng)                              socket() ─┤
             │                                                           │
   accept()  │<─────────────────── connect() ────────────────────────────┤
             │                     (Bắt tay 3 bước TCP)                  │
             │                                                           │
   read()    │<─────────────────── write() (Gửi Request) ────────────────┤
   (Đọc & xử lý yêu cầu)                                                 │
             │                                                           │
   write() ──┼───────────────────> read() (Nhận Response) ───────────────┤
   (Gửi phản hồi dữ liệu)                                                │
             │                                                           │
   read()=0  │<─────────────────── close() (Chủ động đóng kết nối) ──────┤
   (Nhận FIN)│                                                           │
             │                                                           │
   close() ──┘                                                           ▼
   (Đóng kết nối Server)
```

---

<a id="chuong-3"></a>
# CHƯƠNG 3: TẦNG GIAO VẬN (TRANSPORT LAYER)
> 📄 **Slide bài giảng:** [Chapter_3_v9.0.pdf](.pdf/Chapter_3_v9.0.pdf)

## 3.1. Dịch vụ tầng giao vận & Ghép kênh / Phân kênh

```text
SO SÁNH TẦNG MẠNG VÀ TẦNG GIAO VẬN
[ Application Process A ]     [ Application Process B ]
             \                   /
              ▼                 ▼
       ┌───────────────────────────────┐
       │ Tầng Giao vận (Transport)     │  <═══ TRUYỀN THÔNG PROCESS-TO-PROCESS
       └───────────────────────────────┘       (Nhận diện qua Cổng - Port Number)
                      │
                      ▼
       ┌───────────────────────────────┐
       │ Tầng Mạng (Network)           │  <═══ TRUYỀN THÔNG HOST-TO-HOST
       └───────────────────────────────┘       (Nhận diện qua Địa chỉ IP)
```

- **Tầng Network (Tầng Mạng)**: Chịu trách nhiệm vận chuyển gói tin từ **máy trạm này đến máy trạm kia** (*Host-to-Host*) dựa trên địa chỉ IP.
- **Tầng Transport (Tầng Giao vận)**: Thiết lập kênh truyền thông logic trực tiếp giữa các **tiến trình ứng dụng cụ thể** đang chạy trên các máy tính (*Process-to-Process*) thông qua số hiệu cổng **Port Number**.
- **Khái niệm Segment**: Là đơn vị dữ liệu (PDU) của tầng giao vận. Khi ứng dụng đẩy thông điệp (*Message*) lớn vào Socket, tầng giao vận sẽ băm nhỏ thông điệp thành các mảnh (*chunks*), gắn thêm tiêu đề giao vận (chứa `Source Port`, `Dest Port`, `Checksum`,...) để tạo thành Segment rồi đẩy xuống tầng mạng.

---

### Cơ chế Dồn kênh (Multiplexing) và Phân kênh (Demultiplexing)
Hệ điều hành cho phép hàng chục ứng dụng (trình duyệt web, ứng dụng chat, game online) cùng truy cập Internet đồng thời qua một card mạng duy nhất nhờ hai cơ chế:

```text
CƠ CHẾ DỒN KÊNH (MULTIPLEXING) VÀ PHÂN KÊNH (DEMULTIPLEXING)

[ BÊN GỬI: DỒN KÊNH - MULTIPLEXING ]
 Tiến trình Web (P1)         Tiến trình Game (P2)        Tiến trình Chat (P3)
      │                           │                           │
      ▼ (Ghi dữ liệu)             ▼ (Ghi dữ liệu)             ▼ (Ghi dữ liệu)
 [ Socket Port 80 ]          [ Socket Port 5000 ]        [ Socket Port 443 ]
      │                           │                           │
      └───────────────────────────┼───────────────────────────┘
                                  ▼
      ┌───────────────────────────────────────────────────────────┐
      │ TẦNG GIAO VẬN (TRANSPORT LAYER)                           │
      │ - Gắn Header: [ Source Port | Dest Port | Checksum | Data]│
      │ - Thu thập dữ liệu từ các socket, đóng thành các Segment  │
      └───────────────────────────┬───────────────────────────────┘
                                  │
                                  ▼ (Dồn kênh: Xếp xen kẽ thành chuỗi các gói tin)
               ┌──────────┬──────────┬──────────┬──────────┐
               │  Seg P1  │  Seg P2  │  Seg P1  │  Seg P3  │ ───> "Dòng gói tin"
               └──────────┴──────────┴──────────┴──────────┘     (Packet Stream)
                                  │
                                  ▼
      ┌───────────────────────────────────────────────────────────┐
      │ TẦNG MẠNG (NETWORK LAYER - IP)                            │
      │ - Đóng gói Segment vào IP Datagram và đẩy ra Card mạng    │
      └───────────────────────────┬───────────────────────────────┘
                                  │
                                  ▼ (Truyền chuỗi bit qua Internet)
                                  │
[ BÊN NHẬN: PHÂN KÊNH - DEMULTIPLEXING ]
                                  │
                                  ▼ (Nhận dòng gói tin từ Card mạng)
      ┌───────────────────────────────────────────────────────────┐
      │ TẦNG MẠNG (NETWORK LAYER - IP)                            │
      └───────────────────────────┬───────────────────────────────┘
                                  │ (Bóc IP Header, đẩy Segment lên)
                                  ▼
      ┌───────────────────────────────────────────────────────────┐
      │ TẦNG GIAO VẬN (TRANSPORT LAYER)                           │
      │ - Bóc tách Header, đọc trường Destination Port Number     │
      └───────────────────────────┬───────────────────────────────┘
                                  │ (Phân kênh: Phân phát từng gói về đúng Socket)
             ┌────────────────────┼────────────────────┐
             ▼                    ▼                    ▼
     [ Socket Port 80 ]   [ Socket Port 5000 ] [ Socket Port 443 ]
             │                    │                    │
             ▼                    ▼                    ▼
     Tiến trình Web (P1)  Tiến trình Game (P2) Tiến trình Chat (P3)
```

1. **Dồn kênh (Multiplexing) tại bên gửi**: Tầng giao vận thu thập dữ liệu từ nhiều socket ứng dụng khác nhau, bọc thêm tiêu đề tầng giao vận có chứa cổng nguồn (*Source Port*) và cổng đích (*Dest Port*) để tạo thành các segment, sau đó xếp xen kẽ và chuyển xuống tầng mạng.
2. **Phân kênh (Demultiplexing) tại bên nhận**: Khi nhận segment từ tầng mạng đưa lên, tầng giao vận đọc trường `Destination Port` trong header để bàn giao dữ liệu vào đúng socket của tiến trình ứng dụng đang chờ.
   - **Phân kênh không kết nối (UDP)**: Socket đích chỉ được xác định dựa trên bộ đôi: `(Dest IP, Dest Port)`. Bất kỳ client nào gửi đến cùng một Dest Port đều chui vào chung một socket UDP.
   - **Phân kênh hướng kết nối (TCP)**: Mỗi socket kết nối TCP được định danh duy nhất bởi **bộ tứ 4-tuple**: `(Source IP, Source Port, Dest IP, Dest Port)`. Máy chủ web có thể lắng nghe ở cổng 80 nhưng sẽ tạo ra các socket riêng biệt cho từng client kết nối tới.

---

### Cấu trúc 3 dải cổng mạng (Port Numbers) do OS quản lý:
Cổng (*Port*) là số nguyên 16-bit không âm, có giá trị từ $0$ đến $65535$ ($2^{16} - 1$):
- **Well-known Ports ($0 - 1023$)**: Cổng mặc định dành riêng cho các dịch vụ mạng chuẩn quốc tế (HTTP `80`, HTTPS `443`, SSH `22`, DNS `53`, SMTP `25`). Hệ điều hành yêu cầu quyền quản trị cao nhất (*Root/Administrator*) mới cho phép tiến trình mở socket lắng nghe trên dải cổng này.
- **Registered Ports ($1024 - 49151$)**: Dành cho các ứng dụng, dịch vụ phổ biến của các tổ chức/cá nhân đăng ký với IANA (MySQL `3306`, PostgreSQL `5432`, Microsoft RDP `3389`, MongoDB `27017`).
- **Dynamic / Private / Ephemeral Ports ($49152 - 65535$)**: Cổng động do Hệ điều hành tự động cấp phát ngẫu nhiên cho các ứng dụng Client khi khởi tạo kết nối ra ngoài, và tự động thu hồi khi phiên kết nối kết thúc.

---

## 3.2. Nguyên lý Truyền dữ liệu tin cậy (Reliable Data Transfer - RDT)

Vì tầng mạng IP bên dưới là môi trường không đáng tin cậy (có thể mất gói, đảo lộn thứ tự, sai lệch bit do nhiễu vật lý), tầng giao vận phải triển khai các cơ chế kiểm soát logic.

```text
CON ĐƯỜNG TIẾN HÓA CỦA CÁC PHIÊN BẢN RDT
┌───────────┐      ┌───────────┐      ┌───────────┐      ┌───────────┐      ┌───────────┐
│  RDT 1.0  │ ───> │  RDT 2.0  │ ───> │  RDT 2.1  │ ───> │  RDT 2.2  │ ───> │  RDT 3.0  │
└───────────┘      └───────────┘      └───────────┘      └───────────┘      └───────────┘
Kênh hoàn hảo     Thêm Checksum,     Thêm số thứ tự      Bỏ NAK, chỉ        Thêm Timer đếm
(Không lỗi,       phản hồi ACK/NAK   Seq 0/1 để chặn     dùng ACK kèm       ngược để xử lý
không mất gói)    để xử lý lỗi bit   trùng lặp (Dup)     Seq number         mất gói tin
```

### Bảng tổng kết tiến hóa các phiên bản RDT:

| Phiên bản RDT&emsp;&emsp; | Vấn đề kênh truyền đối mặt | Cơ chế kỹ thuật mới được bổ sung | Hạn chế còn tồn đọng |
| :--- | :--- | :--- | :--- |
| **`rdt 1.0`** | Kênh truyền phải hoàn hảo 100% | Không cần cơ chế bảo vệ nào | Không thực tế vì chưa tồn tại kênh truyền nào hoàn hảo lý tưởng (mạng thực tế luôn có nhiễu bit và rớt gói) |
| **`rdt 2.0`** | Kênh có thể bị **lỗi bit** (*bit errors*) | - Thêm **Checksum** để phát hiện lỗi bit<br>- Thêm phản hồi **ACK** (báo nhận tốt) và **NAK** (báo lỗi đòi gửi lại) | Nếu chính gói ACK hoặc NAK bị lỗi bit trên đường về, bên gửi không hiểu được và sẽ phát lại $\to$ bên nhận bị **trùng lặp gói tin (*Duplicate*)** |
| **`rdt 2.1`** | Gói ACK/NAK có thể bị lỗi bit | Bổ sung **Số thứ tự (Sequence Number: 0 hoặc 1)** vào gói tin để bên nhận nhận diện và vứt bỏ gói bị trùng lặp | Quản lý cả hai loại thông điệp ACK và NAK làm phức tạp máy trạng thái (FSM) và tiêu tốn băng thông |
| **`rdt 2.2`** | Muốn tối giản hóa thông điệp | **Loại bỏ hoàn toàn NAK**, chỉ dùng gói ACK có kèm số thứ tự gói cuối cùng nhận tốt. Nếu bên gửi nhận 2 lần cùng một ACK (*Duplicate ACK*) thì tự hiểu gói tiếp theo bị hỏng | Vẫn chỉ xử lý được lỗi bit; nếu gói tin bị **mất tích (*Lost Packet*)** trên đường truyền thì cả bên gửi và bên nhận sẽ bị **treo vĩnh viễn** chờ nhau |
| **`rdt 3.0`** | Kênh có cả **lỗi bit VÀ mất gói tin** | Bổ sung **Bộ đếm thời gian (Countdown Timer)**. Sau khoảng thời gian chờ (*Timeout*) mà chưa nhận được ACK thì tự động phát lại gói | Sử dụng cơ chế *Stop-and-Wait* (gửi 1 gói - chờ 1 gói) khiến hiệu năng sử dụng đường truyền cực kỳ lãng phí |

---

## 3.3. Kỹ thuật đường ống (Pipelining) & Các giao thức Sliding Window

Cơ chế *Stop-and-Wait* của rdt3.0 có hiệu suất sử dụng đường truyền cực kỳ tệ: bên gửi tốn thời gian nhàn rỗi chờ đợi cả một khoảng RTT (Round-Trip Time) sau mỗi gói tin đơn lẻ.
**Giải pháp Pipelining (Đường ống)**: Cho phép bên gửi phát liên tiếp nhiều gói tin cùng lúc khi chưa cần nhận ACK, thông qua kỹ thuật **Cửa sổ trượt (Sliding Window)**.

```text
CẤU TRÚC VÀ NGUYÊN LÝ HOẠT ĐỘNG CỦA CỬA SỔ TRƯỢT (SLIDING WINDOW)
                   |◄────── Cửa sổ gửi (Window Size N = 8) ───────►|
 ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
 │  0  │  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │  9  │ 10  │ 11  │ 12  │ 13  │...
 └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
 |◄──── VÙNG 1 ───►|◄──── VÙNG 2 ───►|◄────────── VÙNG 3 ─────────►|◄──── VÙNG 4 ───►|
   VÙNG 1: ĐÃ ACK    VÙNG 2: ĐÃ GỬI    VÙNG 3: ĐƯỢC PHÉP GỬI NGAY   VÙNG 4: CHƯA GỬI
   (Đã nhận ACK)     (Chờ nhận ACK)     (Trong cửa sổ, chưa gửi)     (Ngoài cửa sổ)
  (Giải phóng đệm)  (In-flight data)      (Sẵn sàng gửi ngay)       (Bị chặn truyền)
                      ▲                 ▲                             ▲
                      │                 │                             │
                  send_base        nextseqnum                   send_base + N
                   (Gói 3)          (Gói 6)                       (Gói 11)

• Ý nghĩa 3 con trỏ điều khiển:
  - send_base     = 3  : Gói nhỏ nhất đã phát nhưng CHƯA nhận được ACK (mép trái cửa sổ gửi).
  - nextseqnum    = 6  : Gói nhỏ nhất tiếp theo sẽ được phát khi có dữ liệu từ tầng trên.
  - send_base + N = 11 : Ngưỡng trên giới hạn cửa sổ; các gói từ 11 trở đi bị chặn chưa được gửi.
• Cơ chế trượt (Sliding): Khi nhận được ACK của gói 3 -> Cửa sổ trượt sang phải 1 nấc:
  send_base nhảy lên 4, send_base + N nhảy lên 12 (gói 11 chuyển vào Vùng 3 và được phép gửi).
```

### Hai trường phái xử lý lỗi trong Pipelining: Go-Back-N vs Selective Repeat

```text
[ Go-Back-N (GBN): Cửa sổ N gói, Receiver không có Buffer ]
Sender  : [ 0 ][ 1 ][ 2 ][ 3 ][ 4 ]
                      x (Gói 2 bị rớt trên mạng)
Receiver: Nhận 0 ──> ACK0 │ Nhận 1 ──> ACK1 │ Gói 3 đến ──> Vứt bỏ! │ Gói 4 đến ──> Vứt bỏ!
          (Chỉ chấp nhận gói theo đúng thứ tự tuần tự)
Sender  : Hết giờ Timer gói 2 ──> BẮT BUỘC GỬI LẠI TOÀN BỘ [ 2 ][ 3 ][ 4 ]


[ Selective Repeat (SR): Receiver có Buffer riêng cho từng gói ]
Sender  : [ 0 ][ 1 ][ 2 ][ 3 ][ 4 ]
                      x (Gói 2 bị rớt)
Receiver: Nhận 0 ──> ACK0 │ Nhận 1 ──> ACK1 │ Nhận 3 ──> Lưu Buffer, gửi ACK3 │ Nhận 4 ──> Lưu Buffer, gửi ACK4
Sender  : Chỉ hết giờ Timer của riêng gói 2 ──> CHỈ PHÁT LẠI DUY NHẤT GÓI [ 2 ]
```

| Tiêu chí | Go-Back-N (GBN) | Selective Repeat (SR) |
| :--- | :--- | :--- |
| **Cơ chế ACK** | **Cumulative ACK** (ACK dồn: nhận được ACK $n$ nghĩa là đã nhận tốt mọi gói từ 0 đến $n$). | **Individual ACK** (ACK độc lập: gói nào đến an toàn thì ACK riêng đích danh gói đó). |
| **Bộ đệm phía Receiver** | **Hoàn toàn không có Buffer** (Gói đến sai thứ tự sẽ bị loại bỏ ngay lập tức $\to$ tiết kiệm RAM). | **Bắt buộc có Buffer** để lưu tạm các gói đến trước chờ các gói thiếu được gửi lại. |
| **Quản lý Timer** | **1 Timer duy nhất** cho gói tin cũ nhất chưa được xác nhận (*send_base*). | **Mỗi gói tin đang bay** trên mạng sở hữu một Timer đếm ngược độc lập. |
| **Băng thông truyền lại** | **Lãng phí băng thông**: Chỉ 1 gói bị mất kéo theo việc phải truyền lại toàn bộ các gói phía sau. | **Tối ưu hóa băng thông**: Chỉ phát lại duy nhất đúng gói tin bị mất tích. |

> [!IMPORTANT]
> **Định lý kích thước cửa sổ Selective Repeat**:
> Để tránh hiện tượng số thứ tự (*Sequence Number*) bị trùng lặp mơ hồ giữa các gói mới và gói cũ khi ACK bị thất lạc, kích thước cửa sổ gửi/nhận $W$ của Selective Repeat bắt buộc phải thỏa mãn:
>
> $$W_{sender} + W_{receiver} \le 2^k \implies W \le 2^{k-1}$$
>
> - **$k$**: Số lượng bit dùng để đánh số Sequence Number trong tiêu đề gói tin.
> - **$W$**: Kích thước tối đa của cửa sổ trượt (phải thỏa mãn $W \le 2^{k-1}$, tức không vượt quá một nửa không gian số thứ tự).

---

## 3.4. Giao thức UDP (User Datagram Protocol - RFC 768)

UDP là giao thức tầng giao vận tối giản nhất: không rườm rà, không thiết lập kết nối trước (*Connectionless*), hoạt động theo nguyên tắc nỗ lực tối đa (*Best-effort*). Hiểu đơn giản thì *Best-effort* nghĩa là sẽ cố gắng làm nhưng không đảm bảo làm được.

### Cấu trúc UDP Header (Tổng cộng 8 Bytes):
```text
CẤU TRÚC GÓI UDP (8 BYTES HEADER)
 0                   15 16                  31
┌──────────────────────┬──────────────────────┐
│  Source Port (16b)   │   Dest Port (16b)    │
├──────────────────────┼──────────────────────┤
│     Length (16b)     │    Checksum (16b)    │
├──────────────────────┴──────────────────────┤
│          Application Data (Payload)         │
└─────────────────────────────────────────────┘
```
- **Source Port (16 bits)**: Cổng của tiến trình gửi.
- **Dest Port (16 bits)**: Cổng của tiến trình nhận.
- **Length (16 bits)**: Độ dài toàn bộ gói tin UDP (tính bằng bytes, gồm 8 bytes header + kích thước dữ liệu payload).
- **Checksum (16 bits)**: Phát hiện lỗi bit trên đường truyền.
  - *Thuật toán Checksum*: Bên gửi cộng dồn các từ nhị phân 16-bit của toàn bộ gói tin (kèm một pseudo-header IP giả lập), lấy bù 1 (*1's Complement Sum*) rồi ghi vào ô Checksum. Bên nhận cộng dồn tất cả lại: nếu kết quả toàn bit 1 (`1111...1111`) nghĩa là gói tin nguyên vẹn; nếu xuất hiện bit 0 thì gói tin đã bị lỗi và bị loại bỏ ngay lập tức (UDP không gửi cảnh báo hay đòi phát lại).

---

## 3.5. Giao thức TCP (Transmission Control Protocol - RFC 793)

### A. Cấu trúc TCP Segment Header (Tối thiểu 20 Bytes)
```text
CẤU TRÚC CHI TIẾT TCP HEADER (20 - 60 BYTES)
 0                    15 16                   31
┌───────────────────────┬───────────────────────┐
│   Source Port (16b)   │    Dest Port (16b)    │
├───────────────────────┴───────────────────────┤
│             Sequence Number (32b)             │
├───────────────────────────────────────────────┤
│          Acknowledgement Number (32b)         │
├──────┬────────┬───────┬───────────────────────┤
│ HLen │Reserved│ Flags │ Receive Window (16b)  │
├──────┴────────┴───────┼───────────────────────┤
│     Checksum (16b)    │ Urg Data Pointer(16b) │
├───────────────────────┴───────────────────────┤
│         Options (Tùy chọn, 0-40 bytes)        │
├───────────────────────────────────────────────┤
│           Application Data (Payload)          │
└───────────────────────────────────────────────┘
```

- **Source Port / Dest Port (16 bits mỗi trường)**: Cổng tiến trình gửi và cổng tiến trình nhận.
- **Sequence Number (Seq - 32 bits)**: Đếm theo **số thứ tự của byte dữ liệu đầu tiên** trong payload của segment đó (chứ không đếm theo số thứ tự của gói tin).
- **Acknowledgement Number (ACK - 32 bits)**: Chứa số thứ tự của **byte tiếp theo mà bên nhận đang mong đợi** nhận được (Cumulative ACK).
- **Header Length (HLen / Data Offset - 4 bits)**: Độ dài của header TCP tính theo số từ 32-bit (4 bytes). Header tối thiểu là 20 bytes ($\text{HLen} = 5$, tương ứng $5 \times 4 = 20\text{ bytes}$).
- **Tập hợp cờ điều khiển (Control Flags - 1 bit mỗi cờ)**:
  - `SYN (Synchronize)`: Dùng trong bước bắt tay để đồng bộ hóa số Seq khởi tạo ban đầu (*ISN*).
  - `ACK (Acknowledge)`: Thông báo trường Acknowledgement Number có giá trị hiệu lực.
  - `FIN (Finish)`: Bên gửi thông báo đã hết dữ liệu, yêu cầu đóng chiều gửi kết nối an toàn.
  - `RST (Reset)`: Hủy bỏ kết nối ngay lập tức vì phát hiện lỗi nghiêm trọng hoặc không có socket đích tương ứng.
  - `PSH (Push)`: Yêu cầu bên nhận đẩy ngay dữ liệu lên ứng dụng, không chờ gom đủ buffer.
  - `URG (Urgent)`: Báo hiệu segment chứa dữ liệu khẩn cấp.
  - `ECE / CWR`: Dùng cho cơ chế thông báo tắc nghẽn rõ ràng (*Explicit Congestion Notification - ECN*).
- **Receive Window (16 bits)**: Biến `rwnd` dùng để kiểm soát luồng, thông báo số byte bộ đệm còn trống của bên nhận.
- **Checksum (16 bits)**: Kiểm tra lỗi bit trên toàn bộ header và dữ liệu.
- **Urgent Data Pointer (16 bits)**: Trỏ tới vị trí kết thúc của dữ liệu khẩn cấp khi cờ URG được bật.

---

### B. Bắt tay 3 bước (3-Way Handshake) & Đóng kết nối 4 bước (4-Way Teardown)

```text
QUÁ TRÌNH THIẾT LẬP (3-WAY) VÀ ĐÓNG (4-WAY) KẾT NỐI TCP
┌──────────────────┐                                        ┌──────────────────┐
│      CLIENT      │                                        │      SERVER      │
└────────┬─────────┘                                        └────────┬─────────┘
         │                                                           │
         │──────── 1. SYN = 1, Seq = x ─────────────────────────────>│ (Server nhận SYN, tạo socket con)
         │                                                           │
         │<─────── 2. SYN = 1, ACK = 1, Seq = y, Ack_seq = x + 1 ────│ (Gửi SYN-ACK phản hồi)
         │                                                           │
         │──────── 3. ACK = 1, Seq = x + 1, Ack_seq = y + 1 ────────>│ (Client gửi ACK hoàn tất)
         │                                                           │
        ══════[ KẾT NỐI ĐƯỢC THIẾT LẬP - BẮT ĐẦU TRUYỀN DỮ LIỆU ]══════
         │                                                           │
         │──────── 1. FIN = 1, Seq = u ─────────────────────────────>│ (Client xin đóng chiều gửi)
         │<─────── 2. ACK = 1, Ack_seq = u + 1 ──────────────────────│ (Server ACK, chiều Server->Client mở)
         │                                                           │
         │<─────── 3. FIN = 1, Seq = v ──────────────────────────────│ (Server truyền xong, xin đóng)
         │──────── 4. ACK = 1, Ack_seq = v + 1 ─────────────────────>│ (Client gửi ACK chốt)
         ▼                                                           │
┌────────────────────────┐                                    ┌──────┴─────┐
│ Trạng thái TIME_WAIT   │                                    │   CLOSED   │
│ (Chờ 2*MSL = 60-120s)  │                                    └────────────┘
└────────────────────────┘
```

> [!NOTE]
> **Tại sao Client phải chờ ở trạng thái TIME_WAIT (2 * MSL = 60 - 120 giây) trước khi đóng hẳn?**
> - **Khái niệm MSL (Maximum Segment Lifetime)**: Là thời gian sống tối đa mà một TCP segment có thể tồn tại trên mạng Internet trước khi bị hủy bỏ (thường mặc định là 30 đến 60 giây tùy hệ điều hành).
> 1. **Bảo đảm bên đối diện nhận được ACK**: Nếu gói ACK cuối (bước 4) bị rớt, Server sẽ timeout và gửi lại gói FIN (bước 3). Khoảng chờ 2 * MSL (1 MSL cho gói ACK đi + 1 MSL cho gói FIN gửi lại quay về) giúp Client vẫn còn mở để gửi lại ACK, tránh việc đóng sớm khiến Client phản hồi gói RST gây lỗi bất thường cho Server.
> 2. **Dọn sạch các gói tin cũ trên mạng**: Đảm bảo toàn bộ các gói tin cũ của kết nối này hết hạn TTL (Time-To-Live) và chết hẳn, tránh gây nhiễu loạn cho một kết nối mới mở sau đó mà vô tình dùng trùng số cổng Port.

---

### C. Cơ chế Kiểm soát luồng (Flow Control)
- **Mục đích**: Bảo vệ bộ đệm của **Bên nhận (Receiver)** không bị tràn do bên gửi truyền dữ liệu quá nhanh (tốc độ mạng nhanh hơn tốc độ ứng dụng đọc dữ liệu từ Socket).
- **Cơ chế hoạt động**: Hoàn toàn tự động do Hệ điều hành thực hiện. Bên nhận liên tục tính toán khoảng không gian bộ nhớ còn trống của mình và ghi vào trường `Receive Window (rwnd)` gửi kèm trong mọi gói tin phản hồi về bên gửi:

```text
CƠ CHẾ BỘ ĐỆM BÊN NHẬN VÀ TÍNH TOÁN RECEIVE WINDOW (rwnd)
┌───────────────────────────────── RcvBuffer (Bộ đệm do OS cấp) ──────────────────────────────────┐
│                                                                                                 │
│ ┌───────────────────────────────┬───────────────────────────────┬─────────────────────────────┐ │
│ │   Dữ liệu đã nhận & ĐÃ ĐƯỢC   │   Dữ liệu đã nhận an toàn,    │    KHOẢNG TRỐNG CÒN LẠI     │ │
│ │   Ứng dụng đọc xong (Free)    │   ĐANG NẰM CHỜ Ứng dụng đọc   │  TRONG BỘ ĐỆM (Available)   │ │
│ └───────────────────────────────┴───────────────────────────────┴─────────────────────────────┘ │
│                                 ▲                               ▲                             ▲ │
│                                 │                               │                             │ │
└────────────────────────── LastByteRead ────────────────── LastByteRcvd ────────────── RcvBuffer ┘
                                  |◄── Dữ liệu đang chiếm đệm ───►|◄────────── rwnd ───────────►|
                                                                       (Báo lại cho bên gửi)
```

- **Công thức tính toán**:

  $$\text{rwnd} = \text{RcvBuffer} - [\text{LastByteRcvd} - \text{LastByteRead}]$$

- **Ràng buộc phía bên gửi**: Lượng dữ liệu đã phát đi nhưng chưa được ACK xác nhận không bao giờ được vượt quá giá trị `rwnd` nhận được:

  $$[\text{LastByteSent} - \text{LastByteAcked}] \le \text{rwnd}$$

- Khi ứng dụng bên nhận đọc quá chậm làm bộ đệm đầy hoàn toàn ($\text{rwnd} = 0$), bên gửi **lập tức ngừng truyền** dữ liệu mới (chỉ thỉnh thoảng gửi gói tin thăm dò 1 byte để kiểm tra xem `rwnd` đã mở lại chưa).

---

### D. Cơ chế Kiểm soát tắc nghẽn (Congestion Control)
- **Mục đích**: Bảo vệ **Hạ tầng mạng lõi (Network Core - các Router dọc đường)** không bị tràn hàng đợi gây rớt gói hàng loạt.
- Hoạt động dựa trên biến cửa sổ tắc nghẽn `cwnd (Congestion Window)` do bên gửi tự tính toán và điều chỉnh.
- Lượng dữ liệu tối đa bên gửi được phép bơm vào mạng luôn bị khống chế bởi cả hai yếu tố:

  $$\text{Cửa sổ gửi tối đa} = \min(\text{cwnd}, \text{rwnd})$$

- Nguyên lý điều khiển cơ bản: **AIMD (Additive Increase, Multiplicative Decrease)** - Tăng từ từ theo hàm cộng tuyến tính khi mạng thông thoáng, nhưng cắt giảm đột ngột theo hàm nhân khi phát hiện có dấu hiệu tắc nghẽn.

```text
CHU KỲ BIẾN THIÊN CỦA TCP CONGESTION WINDOW
 cwnd (MSS)
  ▲
  │                                 [Nhận 3 Dup ACKs]                   [Bị Timeout]
  │                                  (Tắc nghẽn nhẹ)              (Tắc nghẽn nghiêm trọng)
  │                                           │                               │
16│                                          /│ (Reno cắt đôi cwnd)          /│
  │                                         / │                             / │
12│                     /──────────────────/  │                            /  │ (Rớt thẳng về 1)
  │                    / (Congestion          │                           /   │
 8│ ssthresh = 8 ─────/   Avoidance: +1)      │      /───────────────────/    │
  │──────────────────/                        │     / (Fast Recovery: +1)     │
 6│                 /                         └────/ (ssthresh mới = 8)       │
  │                / (Slow Start:                                             │
 4│               /   Tăng hàm mũ)                                            │
 2│              /                                                            │        /────────
 1│─────────────/                                                             └───────/ (Slow Start)
  └──────────────────────────────────────────────────────────────────────────────────────────────► Thời gian (RTT)
  |◄── Slow Start ──►|◄ Congestion Avoidance ►|◄──── Fast Recovery + CA ─────►|◄─ SS ─►|◄ CA... ►|

QUY TẮC HOẠT ĐỘNG VÀ ĐIỀU CHỈNH BIẾN SSTHRESH:
 • Giá trị ban đầu của ssthresh:
   - Trong thực tế (RFC 5681) : Khởi tạo rất lớn (>= 64 KB hoặc vô hạn) để TCP Slow Start tối đa.
   - Trong ví dụ mô phỏng trên: Giả định ssthresh ban đầu = 8 MSS để dễ quan sát điểm chuyển pha.
 • 1. Slow Start (Khởi động chậm)       : Khởi tạo cwnd = 1 MSS, tăng gấp đôi mỗi RTT (1 -> 2 -> 4 -> 8...).
 • 2. Congestion Avoidance (Tránh nghẽn): Khi cwnd >= ssthresh, chuyển sang tăng tuyến tính (+1 MSS / RTT).
 • 3. Biến cố 3 Dup ACKs (Nghẽn nhẹ)    : Reno cắt đôi cwnd: ssthresh mới = 16 / 2 = 8 MSS.
                                          Vào Fast Recovery rồi tiếp tục tăng tuyến tính (+1) -> Đồ thị Răng Cưa.
 • 4. Biến cố Timeout (Nghẽn nặng)      : Đặt ssthresh mới = cwnd / 2 (ở ví dụ trên: 14 / 2 = 7 MSS).
                                          Đạp cwnd rơi thẳng về 1 MSS, bắt đầu lại Slow Start đến ssthresh mới.
```

1. **Slow Start (Khởi động chậm)**: Khởi tạo với $\text{cwnd} = 1\text{ MSS}$. Cứ mỗi lượt nhận đủ ACK trong 1 RTT, $\text{cwnd}$ tăng gấp đôi (tăng theo hàm mũ: $1 \to 2 \to 4 \to 8 \dots$).
2. **Congestion Avoidance (Tránh tắc nghẽn)**: Khi $\text{cwnd} \ge \text{ssthresh}$ (Slow Start Threshold), chuyển sang tăng tuyến tính: mỗi RTT chỉ cộng thêm đúng $1\text{ MSS}$ để thăm dò an toàn.
3. **Phản ứng khi xảy ra sự cố**:
   - **Tắc nghẽn nhẹ (Nhận được 3 gói Duplicate ACKs)**: Báo hiệu mạng vẫn còn chuyển tiếp được gói tin.
     - `TCP Tahoe`: Đặt $\text{cwnd} = 1\text{ MSS}$, đưa về Slow Start.
     - `TCP Reno`: Fast Recovery $\to \text{ssthresh} = \frac{\text{cwnd}}{2}$ (trong sơ đồ: $\frac{16}{2} = 8\text{ MSS}$), đặt $\text{cwnd} = \text{ssthresh} + 3$, tiếp tục tăng tuyến tính $+1\text{ MSS}/\text{RTT}$ (tạo đồ thị răng cưa kinh điển).
   - **Tắc nghẽn nặng (Timeout)**: Router dọc đường đã nghẽn cứng hoặc đứt cáp. Cả Reno và Tahoe đều đặt $\text{ssthresh} = \frac{\text{cwnd}}{2}$ (trong sơ đồ: $\frac{14}{2} = 7\text{ MSS}$) và đạp $\text{cwnd}$ thẳng về $1\text{ MSS}$, khởi động lại từ Slow Start.

---

### E. So sánh các thuật toán điều khiển tắc nghẽn hiện đại: Reno vs CUBIC vs BBR

```text
SO SÁNH ĐẶC TUYẾN TĂNG TRƯỞNG CỦA CÁC THUẬT TOÁN ĐIỀU KHIỂN TẮC NGHẼN

1. TCP Reno (AIMD):
   cwnd
    │          /\                  /\            Tăng tuyến tính (+1 MSS/RTT)
    │         /  \ ssthresh       /  \ ssthresh  nhưng khi mất gói thì cắt đôi
    │   /\   /    \___      /\   /    \___       ngay lập tức -> lãng phí đường truyền
    └──/──\_/─────────\────/──\_/─────────\────► Thời gian

2. TCP CUBIC (Mặc định trong Linux/Windows - Đường cong hàm bậc 3):
   cwnd
    │          .---.                .---.      Dùng hàm bậc 3 để tăng tốc cực nhanh
    │         /     \              /     \     về lại điểm tối ưu trước sự cố,
    │   .---./       \___    .---./       \___ sau đó nằm ngang thăm dò an toàn
    └──/─────────────────\──/─────────────────► Thời gian

3. TCP BBR (Google - Đo trực tiếp Max Bandwidth & Min RTT):
   Băng thông
    │ ═══════════════════════════════════════  BBR duy trì tốc độ truyền ổn định vừa
    │ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  khít dung lượng kênh mạng (Pipe Capacity).
    │                                          KHÔNG đợi đến khi rớt gói mới giảm tốc,
    └────────────────────────────────────────► triệt tiêu hoàn toàn nghẽn bộ đệm (Bufferbloat)!
```

- **TCP Reno (Cổ điển)**: Sử dụng mô hình AIMD răng cưa. Điểm yếu là tăng tốc rất chậm trên các đường truyền cáp quang băng thông lớn (*High-BDP Networks*).
- **TCP CUBIC (Mặc định trên Linux, Windows, macOS, Android)**:
  - Sử dụng hàm số bậc 3 để điều chỉnh kích thước `cwnd`.
  - Sau sự cố rớt gói, CUBIC tăng vọt rất nhanh về mức băng thông tối ưu trước đó, sau đó giảm dần tốc độ tăng khi tiệm cận đỉnh cũ để thăm dò an toàn. Giúp tận dụng tối đa băng thông mà không gây sốc mạng.
- **TCP BBR (Bottleneck Bandwidth and RTT - Phát minh bởi Google)**:
  - Khác biệt hoàn toàn với tư duy truyền thống: **Không sử dụng việc rớt gói tin để phát hiện tắc nghẽn**!
  - BBR liên tục đo đạc 2 thông số thực tế: **Băng thông tối đa tại nút thắt cổ chai (*Max Bottleneck Bandwidth*)** và **Thời gian trễ truyền hai chiều tối thiểu (*Min RTT - Round-Trip Time*)**.
  - BBR bơm dữ liệu vừa đủ để lấp đầy đường ống mà không làm tràn bộ đệm của Router, loại bỏ hoàn toàn hiện tượng nghẽn hàng đợi (*Bufferbloat*), cải thiện tốc độ mạng thực tế lên gấp nhiều lần.

---

<a id="chuong-4"></a>
# CHƯƠNG 4: TẦNG MẠNG - MẶT PHẲNG DỮ LIỆU (NETWORK LAYER: DATA PLANE)
> 📄 **Slide bài giảng:** [Chapter_4_v9.0.pdf](.pdf/Chapter_4_v9.0.pdf)

## 4.1. Khái niệm Data Plane vs Control Plane
Tầng mạng (Network Layer) chịu trách nhiệm vận chuyển gói tin từ máy gửi đến máy nhận xuyên qua toàn bộ các nút mạng trung gian (Host-to-Host communication).
- **Datagram**: Đơn vị dữ liệu giao thức (PDU) của tầng mạng, là TCP/UDP Segment nhận từ Tầng Giao vận được đóng gói thêm IP Header.
- **Mô hình dịch vụ "Best-effort" (Nỗ lực tối đa)**:
  - Tầng mạng của Internet chỉ cam kết *cố gắng hết sức* để chuyển gói tin tới đích, nhưng **hoàn toàn không bảo đảm**:
    - Không cam kết gói tin chắc chắn tới đích (có thể bị drop do tràn bộ đệm).
    - Không cam kết thứ tự gói tin (các gói có thể đến đích lộn xộn).
    - Không cam kết độ trễ tối đa hay băng thông tối thiểu.
  - Sự đơn giản của mô hình Best-effort giúp mạng lõi Internet cực kỳ linh hoạt, chi phí thiết bị rẻ và dễ mở rộng quy mô toàn cầu (mọi sự phức tạp về kiểm soát độ tin cậy được đẩy lên Tầng Giao vận TCP ở rìa mạng).

```text
SO SÁNH MẶT PHẲNG DỮ LIỆU (DATA PLANE) VÀ MẶT PHẲNG ĐIỀU KHIỂN (CONTROL PLANE)
┌───────────────────────────────────────────────────────────────────────────────┐
│                    CONTROL PLANE (Mặt phẳng điều khiển)                       │
│  - Chức năng: Định tuyến (ROUTING) - Tìm con đường tối ưu toàn cục (Global)   │
│  - Bản chất: Logic thuật toán (phần mềm), chạy trên Routing Processor (CPU)   │
│  - Thời gian xử lý: Milisecond (ms)                                           │
└──────────────────────────────────────┬────────────────────────────────────────┘
                                       │ Sinh và nạp Bảng chuyển tiếp (Forwarding Table)
                                       ▼
┌───────────────────────────────────────────────────────────────────────────────┐
│                      DATA PLANE (Mặt phẳng dữ liệu)                           │
│  - Chức năng: Chuyển tiếp (FORWARDING) - Đẩy gói từ Cổng vào ra Cổng ra       │
│  - Bản chất: Thao tác phần cứng cục bộ bên trong một Router đơn lẻ (Local)    │
│  - Thời gian xử lý: Nanosecond (ns), dùng phần cứng chuyên dụng ASIC / FPGA   │
└───────────────────────────────────────────────────────────────────────────────┘
```

---

## 4.2. Kiến trúc giải phẫu bên trong một Router

```text
KIẾN TRÚC PHẦN CỨNG BÊN TRONG MỘT ROUTER
┌───────────────────────────────────────────────────────────────────────────────┐
│                             Routing Processor (CPU)                           │
│                      (Chạy thuật toán định tuyến, quản lý)                    │
└───────────────────────────────────────────────────────────────────────────────┘
       ▲                                                                ▲
       │                                                                │
┌────────────────────────┐      ┌───────────────────┐      ┌────────────────────┐
│  Input Port (Cổng vào) │      │                   │      │ Output Port (Cổng) │
│  [Line Term]           │ ───> │ Switching Fabric  │ ───> │  [Buffer Queue]    │
│  [Data Link (MAC/CRC)] │      │  (Băng chuyền     │      │  [Data Link (MAC)] │
│  [Lookup & Forwarding] │      │   chuyển mạch)    │      │  [Line Term]       │
└────────────────────────┘      └───────────────────┘      └────────────────────┘
```

### A. Cổng vào (Input Port):
1. **Khối kết thúc đường truyền (Line Termination)**: Tiếp nhận tín hiệu vật lý (điện áp trên cáp đồng, xung ánh sáng trong sợi quang, sóng radio) và chuyển đổi thành dòng bit $0, 1$.
2. **Khối tầng liên kết (Link Layer Processing)**: Bóc mở Ethernet frame, kiểm tra tính toàn vẹn của dữ liệu bằng mã CRC, bóc bỏ Header/Trailer tầng 2 để lấy IPv4/IPv6 Datagram.
3. **Khối tra cứu địa chỉ (Lookup & Forwarding)**:
   - Đọc địa chỉ IP đích trong Datagram Header.
   - Tra cứu trong **Forwarding Table** bằng thuật toán **Longest Prefix Match (Khớp tiền tố dài nhất)** để xác định chính xác cổng ra cần chuyển tới.
   - Để đạt tốc độ xử lý hàng trăm triệu gói/giây, bảng Forwarding Table được nạp vào bộ nhớ chuyên biệt **TCAM (Ternary Content Addressable Memory)** cho phép tìm kiếm toàn bộ bảng chỉ trong 1 chu kỳ xung nhịp $O(1)$.
   - Nếu Switching Fabric đang bận, gói tin sẽ được đưa vào hàng đợi tạm tại Input Port.

### B. Băng chuyền chuyển mạch (Switching Fabric):
Bộ phận trung tâm chịu trách nhiệm đưa gói tin từ Input Port sang Output Port tương ứng. Có 3 kiến trúc kinh điển:

```text
BA KIẾN TRÚC BĂNG CHUYỀN CHUYỂN MẠCH (SWITCHING FABRIC)

1. Switching via Memory (Qua RAM)     2. Switching via Bus (Bus chung)           3. Interconnection / Crossbar
   ┌─────────┐      ┌──────────┐        ┌───────┐   ┌───────┐   ┌───────┐        In 1 ───(A)─────┼──────┼────
   │ Input 1 │      │ Output 1 │        │ In 1  │   │ In 2  │   │ In 3  │                 │      │      │
   └────┬────┘      └────▲─────┘        └───┬───┘   └───┬───┘   └───┬───┘        In 2 ────┼─────(B)─────┼────
        │  Bus hệ thống  │                  │           │           │                     │      │      │
   ┌────▼────────────────┴─────┐      ══════╪═══════════╪═══════════╪══════      In 3 ────┼──────┼─────(C)───
   │  CPU & Bộ nhớ RAM chính   │                  Bus dùng chung                          │      │      │
   └───────────────────────────┘      ══════╪═══════════╪═══════════╪══════               ▼      ▼      ▼
   - CPU đọc/ghi RAM 2 lần/gói              │           │           │                  Out 1  Out 2  Out 3
   - Băng thông bị nghẽn ở RAM          ┌───▼───┐   ┌───▼───┐   ┌───▼───┐        - Ma trận lưới 2N đường chéo
   - Chỉ xử lý 1 gói tại 1 thời         │ Out 1 │   │ Out 2 │   │ Out 3 │        - Điểm giao đóng/ngắt linh hoạt
     điểm (Router thế hệ đầu)           └───────┘   └───────┘   └───────┘        - Cho phép chuyển song song
                                        - Giới hạn bởi tốc độ bus chung            nhiều gói tin cùng lúc!
                                        - Tranh chấp đường truyền                  (Non-blocking fabric)
```

- **Hiện tượng Head-of-the-Line (HOL) Blocking ở Input Port**:
  - Xảy ra khi gói tin đứng đầu hàng đợi ở Input 1 muốn chuyển ra Output 1 (đang bận vì một Input khác đang truyền tới), khiến tất cả các gói tin phía sau trong hàng đợi của Input 1 đều bị chặn đứng dù cổng ra của chúng (ví dụ Output 2) đang hoàn toàn rảnh rỗi.

```text
HIỆN TƯỢNG NGHẼN ĐẦU HÀNG (HEAD-OF-THE-LINE - HOL BLOCKING)
Input 1 [ Gói tới Out 2 (BỊ CHẶN) ][ Gói tới Out 1 (CHỜ) ] ──┐
                                                             ├─> [ Output 1 ĐANG BẬN! ]
Input 2                            [ Gói tới Out 1 (ĐI)  ] ──┘
* Gói tới Out 2 ở Input 1 dù đường tới Out 2 rảnh nhưng vẫn phải đứng chờ gói phía trước!
```

### C. Cổng ra (Output Port) & Lập lịch hàng đợi (Queue Scheduling):
Khi tốc độ chuyển gói từ Switching Fabric tới cổng ra lớn hơn tốc độ truyền dẫn vật lý đẩy bit ra ngoài liên kết, gói tin sẽ dồn lại trong bộ đệm của Output Port:
- **Nguy cơ tràn đệm (Buffer Overflow / Packet Loss)**: Khi bộ đệm đầy, router bắt buộc phải hủy gói tin. Chính sách hủy:
  - *Drop-tail*: Gói đến sau cùng khi hàng đầy sẽ bị vứt bỏ lập tức.
  - *RED (Random Early Detection)*: Khi hàng đợi vượt qua một ngưỡng dung lượng an toàn, router chủ động vứt bỏ ngẫu nhiên một tỷ lệ nhỏ gói tin để kích hoạt TCP của các bên gửi giảm tốc sớm, tránh sụp đổ mạng hàng loạt.
- **Các thuật toán lập lịch hàng đợi (Packet Scheduling)**:
  1. **FCFS (First-Come First-Served / FIFO)**: Gói nào tới hàng đợi trước thì được truyền lên đường dây trước.
  2. **Priority Queuing (Ưu tiên)**: Phân gói tin vào các mức ưu tiên khác nhau (ví dụ: VoIP/Streaming ưu tiên cao, HTTP/Email ưu tiên thấp). Gói ưu tiên thấp chỉ được phát khi hàng đợi ưu tiên cao hoàn toàn trống.
  3. **Round Robin (Luân phiên)**: Chia thành nhiều hàng đợi theo từng lớp người dùng, luân phiên lấy 1 gói từ hàng đợi 1, rồi đến hàng đợi 2, hàng đợi 3... xoay vòng đều đặn.
  4. **Weighted Fair Queuing (WFQ - Công bằng có trọng số)**: Nâng cấp của Round Robin, mỗi hàng đợi được ấn định một trọng số $w_i$. Băng thông thực tế cấp cho luồng $i$ tỷ lệ thuận với trọng số, đảm bảo dịch vụ tối thiểu cho các luồng quan trọng khi mạng bị nghẽn nặng.

---

## 4.3. Giao thức IPv4 (Internet Protocol v4 - RFC 791)

### A. Cấu trúc Datagram Header IPv4 (20 - 60 Bytes):
```text
CẤU TRÚC GÓI IPV4 DATAGRAM HEADER
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
┌───────┬───────┬───────────────┬───────────────────────────────┐
│Version│  IHL  │Type of Service│      Total Length (16b)       │
├───────┴───────┴───────────────┼─────┬─────────────────────────┤
│      Identification (16b)     │Flags│  Fragment Offset (13b)  │
├───────────────┬───────────────┼─────┴─────────────────────────┤
│  TTL (8 bits) │ Protocol (8b) │   Header Checksum (16 bits)   │
├───────────────┴───────────────┴───────────────────────────────┤
│                  Source IP Address (32 bits)                  │
├───────────────────────────────────────────────────────────────┤
│                Destination IP Address (32 bits)               │
├───────────────────────────────────────────────────────────────┤
│                 Options (Tùy chọn, 0-40 Bytes)                │
├───────────────────────────────────────────────────────────────┤
│                Payload Data (TCP / UDP Segment)               │
└───────────────────────────────────────────────────────────────┘
```

- **Version (4 bits)**: Số hiệu phiên bản giao thức IP (IPv4 = `4` hay `0100`).
- **IHL (Internet Header Length - 4 bits)**: Độ dài của Header tính theo khối 4-byte (32-bit words). Giá trị nhỏ nhất là `5` ($5 \times 4 = 20$ Bytes khi không có Options), tối đa là `15` ($15 \times 4 = 60$ Bytes).
- **Type of Service (TOS) / DSCP + ECN (8 bits)**: Phân loại chất lượng dịch vụ (QoS) và ECN (Explicit Congestion Notification) báo hiệu tắc nghẽn sớm mà không cần drop gói.
- **Total Length (16 bits)**: Tổng chiều dài toàn bộ gói tin (Header + Payload) tính theo byte. Tối đa $2^{16} - 1 = 65,535$ Bytes (nhưng hiếm khi vượt quá MTU 1500 Bytes).
- **TTL (Time-To-Live - 8 bits)**: Mỗi khi gói đi qua một router (1 Hop), router giảm TTL đi 1. Khi $TTL = 0$, router lập tức hủy gói và gửi thông báo lỗi **ICMP Time Exceeded (Type 11, Code 0)** về máy gửi. Giúp triệt tiêu vĩnh viễn các gói tin bay vô tận trong vòng lặp định tuyến (*Routing Loop*).
- **Protocol (8 bits)**: Định danh giao thức tầng trên nằm trong payload:
  - `1`: ICMP
  - `6`: TCP
  - `17`: UDP
  - `41`: IPv6 Encapsulation (Tunneling)
  - `89`: OSPF
- **Header Checksum (16 bits)**: Mã kiểm tra lỗi áp dụng **chỉ cho phần Header** (bảo vệ địa chỉ nguồn/đích). Mỗi khi đi qua một router, vì TTL bị giảm 1 nên router phải **tính toán lại Header Checksum** trước khi chuyển tiếp.

---

### B. Cơ chế Phân mảnh và Tái ghép IPv4 (Fragmentation & Reassembly)
Mỗi liên kết tầng liên kết dữ liệu (Data Link) có một giới hạn truyền tải tối đa gọi là **MTU (Maximum Transmission Unit)**. Ví dụ: Ethernet có MTU = 1500 Bytes.
- Nếu kích thước Datagram lớn hơn MTU của đường truyền tiếp theo, Router bắt buộc phải bẻ gói tin ban đầu thành nhiều mảnh nhỏ (**Fragments**).
- **Ba trường điều khiển phân mảnh trong Header**:
  - `Identification (ID - 16 bits)`: Định danh số hiệu của gói gốc. Tất cả các mảnh cắt ra từ cùng một gói đều mang cùng giá trị ID để bên nhận gom đúng nhóm.
  - `Flags (3 bits)`:
    - Bit 0: Reserved (luôn bằng 0).
    - Bit 1 - `DF (Don't Fragment)`: Nếu $DF = 1$, router bị cấm phân mảnh. Nếu gói vượt quá MTU, router hủy gói và gửi ICMP báo lỗi.
    - Bit 2 - `MF (More Fragments)`: Nếu $MF = 1$, báo hiệu phía sau vẫn còn mảnh tiếp theo. Mảnh cuối cùng sẽ có $MF = 0$.
  - `Fragment Offset (13 bits)`: Vị trí bắt đầu của dữ liệu mảnh này so với dữ liệu của gói gốc, tính theo **đơn vị khối 8-byte** (Offset = Vị trí byte bắt đầu / 8). Do đó, dữ liệu của mỗi mảnh (trừ mảnh cuối) phải luôn chia hết cho 8!

```text
VÍ DỤ TÍNH TOÁN PHÂN MẢNH IPV4 QUA ĐƯỜNG TRUYỀN ETHERNET MTU = 1500 BYTES
Gói tin ban đầu: Tổng 4000 Bytes (Header 20 Bytes + Payload 3980 Bytes), ID = 777, DF = 0

               ┌────────────┬────────────────────────────────────────────────────────┐
  Gói gốc:     │ Header 20B │                  Dữ liệu 3980 Bytes                    │
               └────────────┴────────────────────────────────────────────────────────┘
               Length = 4000, ID = 777, DF = 0, MF = 0, Offset = 0
                                         │
                         (Đi qua Router gặp MTU = 1500 B)
                                         ▼
Mảnh 1:        ┌────────────┬──────────────────────────────────────────┐
 (1500 B)      │ Header 20B │          Dữ liệu: 1480 Bytes             │ (Bytes 0 -> 1479)
               └────────────┴──────────────────────────────────────────┘
               Length = 1500, ID = 777, MF = 1, Offset = 0 / 8 = 0

Mảnh 2:        ┌────────────┬──────────────────────────────────────────┐
 (1500 B)      │ Header 20B │          Dữ liệu: 1480 Bytes             │ (Bytes 1480 -> 2959)
               └────────────┴──────────────────────────────────────────┘
               Length = 1500, ID = 777, MF = 1, Offset = 1480 / 8 = 185

Mảnh 3:        ┌────────────┬─────────────────────────────┐
 (1040 B)      │ Header 20B │     Dữ liệu: 1020 Bytes     │ (Bytes 2960 -> 3979)
               └────────────┴─────────────────────────────┘
               Length = 1040, ID = 777, MF = 0, Offset = 2960 / 8 = 370
               (Tổng dữ liệu tái ghép: 1480 + 1480 + 1020 = 3980 Bytes)
```

> [!NOTE]
> **Vị trí Tái ghép (Reassembly)**: Quá trình ghép các mảnh lại với nhau **chỉ diễn ra duy nhất một lần tại Host đích cuối cùng**, không bao giờ diễn ra ở các router trung gian. Nếu chỉ cần thất lạc 1 mảnh duy nhất, toàn bộ gói tin gốc 4000 Bytes sẽ bị Host đích hủy bỏ hoàn toàn sau khi hết thời gian chờ (Reassembly Timer).

---

## 4.4. Địa chỉ IPv4, Kỹ thuật chia mạng con (Subnetting & CIDR)

### A. Cấu trúc địa chỉ IPv4 & Mặt nạ mạng (Subnet Mask)
IPv4 gồm **32 bits**, biểu diễn dưới dạng 4 số thập phân ngăn cách bởi dấu chấm (Dotted-decimal notation, ví dụ: `192.168.1.100`).
- Cấu trúc 2 phần: `[ Network Prefix (Phần mạng) ] [ Host ID (Phần máy) ]`
- **Chuẩn CIDR (Classless Inter-Domain Routing - RFC 4632)**: Biểu diễn dạng `a.b.c.d/x`, trong đó `/x` là số lượng bit của phần Network Prefix (tương đương số bit 1 trong Subnet Mask).

```text
PHÂN TÍCH CẤU TRÚC ĐỊA CHỈ IP 192.168.1.100/24
Địa chỉ IP:  11000000 . 10101000 . 00000001 . 01100100  (192.168.1.100)
Subnet Mask: 11111111 . 11111111 . 11111111 . 00000000  (255.255.255.0 = /24)
             <------ 24 bit Network ------>  < 8b Host >
Network ID:  192.168.1.0    (Tất cả các bit phần host = 0 - Đại diện cho toàn mạng)
Broadcast:   192.168.1.255  (Tất cả các bit phần host = 1 - Gửi tới mọi máy trong mạng)
Dải khả dụng:192.168.1.1 -> 192.168.1.254 (Dành gán cho máy tính, điện thoại, máy in...)
Số Host:     2^(32 - 24) - 2 = 2^8 - 2 = 254 địa chỉ khả dụng
```

> [!TIP]
> **Công thức vàng tính nhanh Subnetting**:
> - Tổng số địa chỉ IP trong mạng $/x$: $N = 2^{32 - x}$.
> - Số địa chỉ Host gán được cho thiết bị: $N - 2$ (trừ Network ID và Broadcast Address).
> - Bước nhảy (Block Size): $256 - \text{Giá trị Octet bị chia của Subnet Mask}$.
>   - Ví dụ: $/26 \implies$ Mask là `255.255.255.192` $\implies$ Bước nhảy = $256 - 192 = 64$.
>   - Các mạng con: `192.168.1.0/26`, `192.168.1.64/26`, `192.168.1.128/26`, `192.168.1.192/26`.

### B. Nguyên lý Khớp tiền tố dài nhất (Longest Prefix Match - LPM)
Khi một router nhận được gói tin, nó có thể thấy địa chỉ IP đích khớp với nhiều dòng trong bảng định tuyến. Luật xử lý của Router: **Luôn ưu tiên chọn dòng có Network Prefix dài nhất (số bit /x lớn nhất, con đường cụ thể nhất)**:

```text
VÍ DỤ VỀ NGUYÊN LÝ KHỚP TIỀN TỐ DÀI NHẤT (LONGEST PREFIX MATCH)
Bảng chuyển tiếp của Router:
┌───────────────────────────┬──────────────┐
│ Prefix mạng đích          │ Cổng ra      │
├───────────────────────────┼──────────────┤
│ 200.23.16.0/20            │ Interface 0  │ (Bao phủ 200.23.16.0 -> 200.23.31.255)
│ 200.23.24.0/24            │ Interface 1  │ (Bao phủ 200.23.24.0 -> 200.23.24.255)
│ 0.0.0.0/0 (Default Route) │ Interface 2  │ (Tất cả các địa chỉ còn lại)
└───────────────────────────┴──────────────┘
Gói tin 1 có IP đích: 200.23.24.50
- Khớp dòng 1 (/20): Đúng
- Khớp dòng 2 (/24): Đúng
- Khớp dòng 3 (/0) : Đúng
=> Router chọn Interface 1 vì /24 là tiền tố dài nhất (cụ thể nhất)
```

### C. Bảng phân dải IP Private (RFC 1918)
Được IANA bảo lưu riêng cho các mạng nội bộ. Mọi router trên mạng Internet công cộng đều được cấu hình để **drop ngay lập tức** các gói tin có IP đích là Private:
- **Lớp A**: `10.0.0.0/8` (`10.0.0.0` $\to$ `10.255.255.255`) - Chứa $\approx 16.7$ triệu máy.
- **Lớp B**: `172.16.0.0/12` (`172.16.0.0` $\to$ `172.31.255.255`) - Chứa $\approx 1$ triệu máy.
- **Lớp C**: `192.168.0.0/16` (`192.168.0.0` $\to$ `192.168.255.255`) - Thường dùng cho gia đình, văn phòng nhỏ.
- **Loopback Address**: `127.0.0.1/8` (Tự trỏ về chính máy mình mà không phát ra card mạng).
- **APIPA (Automatic Private IP Addressing)**: `169.254.0.0/16` (Địa chỉ Windows tự gán khi không xin được IP từ DHCP Server).

---

## 4.5. DHCP và NAT

### A. Giao thức Cấu hình Động (DHCP - Dynamic Host Configuration Protocol - RFC 2131)
Cơ chế "Plug-and-Play" cho phép thiết bị khi cắm dây mạng hoặc kết nối Wi-Fi tự động nhận đầy đủ 4 thông số mạng: Địa chỉ IP, Subnet Mask, Default Gateway (IP Router) và Local DNS Server.
- Hoạt động trên tầng ứng dụng qua giao thức **UDP**: Cổng **Server là 67**, cổng **Client là 68**.
- Quá trình xin cấp phát diễn ra qua **tiến trình DORA 4 bước**:

```text
QUÁ TRÌNH CẤP PHÁT ĐỊA CHỈ IP TỰ ĐỘNG DHCP (D-O-R-A)
[ Client mới bật máy ]                                               [ DHCP Server ]
(Chưa có IP: 0.0.0.0)                                                (IP: 192.168.1.1)
         │                                                                   │
         │───────── 1. DHCP DISCOVER (Broadcast) ───────────────────────────>│
         │   Src: 0.0.0.0:68    Dest: 255.255.255.255:67                     │
         │   "Tôi là thiết bị mới (MAC A), mạng này có DHCP Server nào không?"│
         │                                                                   │
         │<──────── 2. DHCP OFFER (Đề xuất cấu hình) ────────────────────────│
         │   Src: 192.168.1.1:67    Dest: 255.255.255.255:68                 │
         │   "Tôi có IP 192.168.1.100 cho bạn thuê, Gateway: 192.168.1.1"    │
         │                                                                   │
         │───────── 3. DHCP REQUEST (Broadcast xác nhận chọn IP) ───────────>│
         │   Src: 0.0.0.0:68    Dest: 255.255.255.255:67                     │
         │   "Tôi đồng ý thuê IP 192.168.1.100 từ DHCP Server 192.168.1.1"   │
         │   (Chuyển broadcast để các DHCP Server khác biết mà giải phóng IP đề xuất)
         │                                                                   │
         │<──────── 4. DHCP ACK (Chốt hợp đồng cấp phát) ────────────────────│
         │   Src: 192.168.1.1:67    Dest: 255.255.255.255:68                 │
         │   "Đã chốt hợp đồng thuê (Lease Time = 86400s). Bạn được dùng IP" │
         ▼                                                                   ▼
(Client cấu hình IP 192.168.1.100)                               (Lưu MAC-IP vào bảng cấp)
```

---

### B. Network Address Translation (NAT / NAPT - RFC 3022)
Do không gian địa chỉ IPv4 (32 bits $\approx 4.3$ tỷ địa chỉ) đã cạn kiệt, NAT ra đời như chiếc phao cứu sinh của Internet: Cho phép toàn bộ mạng nội bộ dùng hàng nghìn địa chỉ Private nhưng chỉ cần **duy nhất một địa chỉ IP Public** để truy cập Internet toàn cầu.
- **Nguyên lý hoạt động (Port-level NAT / NAPT)**:
  - Khi gói tin từ LAN đi ra WAN: Router NAT thay thế `[Src IP Private, Src Port]` bằng `[IP Public của Router, Port WAN mới sinh]`, sau đó lưu ánh xạ này vào **NAT Translation Table**.
  - Khi gói tin phản hồi từ Server Internet gửi về: Router NAT tra cứu Port WAN trong NAT Table để tìm ra `[IP Private, Port LAN]` tương ứng của máy nội bộ và hoán đổi địa chỉ trước khi đẩy vào mạng LAN.

```text
DÒNG CHẢY BIẾN ĐỔI GÓI TIN QUA BẢNG DỊCH ĐỊA CHỈ NAT (NAT TRANSLATION TABLE)
[ Mạng LAN Private (192.168.1.0/24) ]              [ NAT Router ]                   [ Web Server Internet ]
Máy trạm: 192.168.1.10                           WAN IP: 203.0.113.1                 IP: 142.250.190.46:80
         │                                                │                                    │
         │ (1) Gói ra: Src: 192.168.1.10:3345             │                                    │
         │             Dst: 142.250.190.46:80             │                                    │
         │───────────────────────────────────────────────>│                                    │
         │                                                │ (2) Thay Src IP:Port & lưu bảng:   │
         │                                                │ ┌───────────────────┬────────────┐ │
         │                                                │ │ WAN Side          │ LAN Side   │ │
         │                                                │ ├───────────────────┼────────────┤ │
         │                                                │ │ 203.0.113.1:50001 │ 1.10:3345  │ │
         │                                                │ └───────────────────┴────────────┘ │
         │                                                │                                    │
         │                                                │ (3) Gói gửi ra WAN:                │
         │                                                │     Src: 203.0.113.1:50001         │
         │                                                │     Dst: 142.250.190.46:80         │
         │                                                │───────────────────────────────────>│
         │                                                │                                    │
         │                                                │ (4) Web Server phản hồi:           │
         │                                                │     Src: 142.250.190.46:80         │
         │                                                │     Dst: 203.0.113.1:50001         │
         │                                                │<───────────────────────────────────│
         │                                                │                                    │
         │                                                │ (5) Tra bảng NAT: Port 50001       │
         │                                                │     -> Hoán đổi Dst: 1.10:3345     │
         │ (6) Gói trả về máy trạm:                       │                                    │
         │     Src: 142.250.190.46:80                     │                                    │
         │     Dst: 192.168.1.10:3345                     │                                    │
         │<───────────────────────────────────────────────│                                    │
```

> [!WARNING]
> **Tranh cãi kỹ thuật về NAT**:
> - *Vi phạm nguyên lý End-to-End*: Router ở Tầng 3 lại can thiệp sửa đổi số Port ở Tầng 4.
> - *Khó khăn cho kết nối ngang hàng P2P*: Máy bên ngoài Internet không thể chủ động khởi tạo kết nối tới máy trạm nằm sau NAT (cần các giải pháp kỹ thuật phụ trợ như STUN, TURN, UPnP hoặc Port Forwarding).

---

## 4.6. Giao thức IPv6 (RFC 8200)
Được thiết kế để giải quyết dứt điểm vấn đề cạn kiệt địa chỉ IPv4 với không gian địa chỉ khổng lồ: **128 bits** ($2^{128} \approx 3.4 \times 10^{38}$ địa chỉ, đủ để cấp hàng triệu địa chỉ cho từng hạt cát trên Trái Đất).

### A. Cấu trúc Datagram Header IPv6 (Cố định 40 Bytes):
```text
CẤU TRÚC TIÊU ĐỀ IPV6
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
┌───────┬───────────────┬───────────────────────────────────────┐
│Version│ Traffic Class │          Flow Label (20 bits)         │
├───────┴───────────────┼───────────────┬───────────────────────┤
│  Payload Length (16)  │ Next Hdr (8b) │   Hop Limit (8 bits)  │
├───────────────────────┴───────────────┴───────────────────────┤
│                                                               │
│                  Source IP Address (128 bits)                 │
│                                                               │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│                Destination IP Address (128 bits)              │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

- **Cải tiến vượt bậc so với IPv4**:
  1. **Kích thước Header cố định đúng 40 Bytes**: Router không cần trường Header Length (IHL) nữa, giúp các chip ASIC phần cứng xử lý gói tin với tốc độ ánh sáng.
  2. **Bỏ hoàn toàn trường Checksum**: Vì tầng Data Link (Ethernet CRC) và tầng Transport (TCP/UDP Checksum) đều đã có cơ chế kiểm tra lỗi. Việc bỏ Checksum giúp Router không phải tính toán lại mỗi khi giảm Hop Limit.
  3. **Bỏ cơ chế phân mảnh tại Router**: Router gặp gói vượt MTU sẽ lập tức drop và gửi thông điệp ICMPv6 "Packet Too Big" yêu cầu bên gửi tự thu nhỏ kích thước dữ liệu (*Path MTU Discovery*).
  4. **Flow Label (20 bits)**: Giúp nhận diện và ưu tiên luồng dữ liệu truyền theo chuỗi (ví dụ: real-time streaming) mà không cần phân tích sâu vào payload.
  5. **Bỏ hoàn toàn Broadcast**: Thay thế bằng **Multicast** và **Anycast** để tránh làm nghẽn toàn bộ mạng con.

### B. Bảng so sánh toàn diện IPv4 vs IPv6:

| Tiêu chí | IPv4 (RFC 791) | IPv6 (RFC 8200) |
| :--- | :--- | :--- |
| **Chiều dài địa chỉ** | **32 bits (4 Bytes)** $\approx 4.3 \times 10^9$ địa chỉ | **128 bits (16 Bytes)** $\approx 3.4 \times 10^{38}$ địa chỉ |
| **Định dạng hiển thị**| Dạng thập phân: `192.168.1.1` | Dạng hex: `2001:0db8:85a3::8a2e:0370:7334` |
| **Kích thước Header** | Biến đổi từ **20 đến 60 Bytes** | **Cố định chính xác 40 Bytes** |
| **Phân mảnh gói** | Router dọc đường có quyền phân mảnh | **Chỉ Host gửi mới được phép phân mảnh** |
| **Checksum tiêu đề** | Có (Router phải tính lại tại mỗi Hop) | **Đã loại bỏ hoàn toàn** |
| **Địa chỉ Broadcast** | Có (`255.255.255.255`) | **Không có** (thay thế bằng Multicast/Anycast) |
| **Cấu hình địa chỉ** | Cần DHCP hoặc gán thủ công | Hỗ trợ tự cấu hình không trạng thái **SLAAC** |

### C. Cơ chế chuyển dịch từ IPv4 sang IPv6:
Mạng Internet toàn cầu không thể chuyển đổi sang IPv6 trong một sớm một chiều:
- **Dual-Stack (Chạy song song)**: Thiết bị mạng hỗ trợ đồng thời cả hai ngăn xếp IPv4 và IPv6, tùy máy đích dùng chuẩn nào sẽ gửi gói tin chuẩn đó.
- **Tunneling (Đường hầm đóng gói)**: Khi hai nút IPv6 cần liên lạc với nhau qua mạng trung gian chỉ hỗ trợ IPv4, toàn bộ gói tin IPv6 sẽ được bọc vào trong phần Payload của một gói tin IPv4 bình thường.

```text
CƠ CHẾ ĐƯỜNG HẦM IPV6 TRUYỀN QUA MẠNG IPV4 (IPV6 TUNNELING)
 [ IPv6 Node A ] ───────────────>[ Router Biên B ] ═══════════════> [ Router Biên E ] ──────> [ IPv6 Node F ]
 (IPv6 Datagram)          Đóng gói gói IPv6 vào Payload IPv4        Bóc bỏ Header IPv4        (IPv6 Datagram)
┌────────┬──────┐         ┌───────────┬─────────────┬──────┐                                 ┌────────┬──────┐
│IPv6 Hdr│ Data │         │ IPv4 Hdr  │ IPv6 Header │ Data │                                 │IPv6 Hdr│ Data │
└────────┴──────┘         └───────────┴─────────────┴──────┘                                 └────────┴──────┘
                              (Vùng mạng chỉ có IPv4)
```

---

## 4.7. Generalized Forwarding & OpenFlow (Kiến trúc SDN)
Trong các mạng hiện đại định nghĩa bằng phần mềm SDN (Software-Defined Networking), khái niệm chuyển tiếp đã được tổng quát hóa thành cơ chế **Khớp và Thực thi (Match-plus-Action)** thông qua tiêu chuẩn **OpenFlow**:
- Thay vì chỉ tra cứu địa chỉ IP đích như Router truyền thống, các Switch/Router OpenFlow duyệt qua các trường tiêu đề từ Tầng 2, Tầng 3 đến Tầng 4 trong một bảng luật gọi là **Flow Table**:

```text
CẤU TRÚC BẢNG DÒNG LỆNH OPENFLOW (FLOW TABLE ENTRY)
┌─────────────────────────────────┬─────────────────────────────────┬──────────────────────┐
│          MATCH FIELDS           │             ACTIONS             │       COUNTERS       │
│   (Các trường điều kiện lọc)    │      (Hành động thực thi)       │   (Bộ đếm thống kê)  │
└─────────────────────────────────┴─────────────────────────────────┴──────────────────────┘
  │                                 │                                 │
  ├─ Tầng 2: MAC Src/Dst, VLAN ID   ├─ Forward: Đẩy ra cổng x, y...   ├─ Packet Count: Đếm gói
  ├─ Tầng 3: IP Src/Dst, Protocol   ├─ Drop: Hủy bỏ gói tin           ├─ Byte Count: Đếm byte
  └─ Tầng 4: TCP/UDP Port Src/Dst   ├─ Modify-Header: Sửa IP/Port/MAC └─ Duration: Tuổi thọ luật
                                    └─ Send-to-Controller: Hỏi máy chủ
```

- **Tính linh hoạt vượt bậc của Generalized Forwarding**:
  - Đóng vai trò **Router**: Match theo IP đích $\implies$ Action là Forward ra cổng kế tiếp.
  - Đóng vai trò **Switch Tầng 2**: Match theo MAC đích $\implies$ Action là Forward theo bảng CAM.
  - Đóng vai trò **Tường lửa (Firewall)**: Match theo IP/Port nguy hiểm $\implies$ Action là Drop.
  - Đóng vai trò **NAT**: Match theo IP/Port LAN $\implies$ Action là Modify Header và Forward.

---

<a id="chuong-5"></a>
# CHƯƠNG 5: TẦNG MẠNG - MẶT PHẲNG ĐIỀU KHIỂN (NETWORK LAYER: CONTROL PLANE)
> 📄 **Slide bài giảng:** [Chapter_5_v9.0.pdf](.pdf/Chapter_5_v9.0.pdf)

## 5.1. Kiến trúc Mặt phẳng Điều khiển SDN (Software-Defined Networking)
Kiến trúc mang tính cách mạng: Tách rời hoàn toàn bộ não tính toán định tuyến (Control Plane) ra khỏi thiết bị chuyển mạch vật lý (Data Plane).
- **1. Data Plane Devices**: Các switch phần cứng chỉ làm nhiệm vụ chuyển tiếp gói tin tốc độ cao theo bảng luật (*Flow Table*).
- **2. SDN Controller (Network OS)**: Máy chủ trung tâm lưu trữ bản đồ trạng thái toàn mạng, cung cấp API hai đầu:
  - *Southbound API (ví dụ: OpenFlow)*: Đẩy bảng luật từ máy chủ xuống các switch vật lý.
  - *Northbound API (RESTful)*: Cho phép các ứng dụng định tuyến, cân bằng tải, tường lửa của bên thứ ba lập trình logic mạng một cách linh hoạt.

---

## 5.2. Các thuật toán định tuyến cốt lõi (Routing Algorithms)
Mục tiêu tối thượng của thuật toán định tuyến là tìm đường đi có **chi phí thấp nhất (Least-cost path)** giữa các router trong toàn mạng.

```text
PHÂN LOẠI HAI TRƯỜNG PHÁI THUẬT TOÁN ĐỊNH TUYẾN KINH ĐIỂN
┌───────────────────────────────────────────────────────────────────────────────────┐
│                           THUẬT TOÁN ĐỊNH TUYẾN (ROUTING)                         │
└───────────────────────────────────────────────────────────────────────────────────┘
                     │                                           │
                     ▼                                           ▼
      [ LINK-STATE (Dijkstra) ]                   [ DISTANCE-VECTOR (Bellman-Ford) ]
      - Toàn cục (Global knowledge)               - Phân tán (Decentralized)
      - Mọi router đều có bản đồ topology         - Chỉ trao đổi với hàng xóm trực tiếp
      - Lan truyền thông tin qua LSA Flooding     - Trao đổi bảng khoảng cách định kỳ
      - Giao thức áp dụng: OSPF, IS-IS            - Giao thức áp dụng: RIP, BGP
```

---

### A. Thuật toán Link-State (Dijkstra Algorithm)
- **Nguyên lý**: Mỗi router thu thập trạng thái liên kết của toàn bộ các router trong mạng thông qua cơ chế phát tán gói tin **LSA Flooding (Link State Advertisement)**. Khi mọi router đều có cùng một bản đồ mạng (Topology Map), chúng sẽ chạy thuật toán Dijkstra để tìm cây đường đi ngắn nhất từ chính nó tới tất cả các nút khác.
- **Ký hiệu toán học**:
  - $c(x, y)$: Chi phí liên kết trực tiếp giữa nút $x$ và nút $y$ (nếu không nối trực tiếp, $c = \infty$).
  - $D(v)$: Chi phí đường đi hiện tại ước tính từ nút nguồn tới nút $v$.
  - $p(v)$: Nút liền trước nút $v$ trên đường đi ngắn nhất hiện tại.
  - $N'$: Tập hợp các nút đã tìm được đường đi ngắn nhất dứt khoát.

```text
MÔ HÌNH MẠNG VÍ DỤ CHẠY DIJKSTRA TỪ NÚT NGUỒN (u)
       (2)───(v)───(3)───(w)───(5)
      /        │        / │      \
    (u)     (2)│     /(3) │(1)   (z)
      \        │  /       │      /
       (1)───(x)───(1)───(y)───(2)
```

**Bảng từng bước thực thi thuật toán Dijkstra từ nút nguồn $u$:**

| Bước lặp | Tập đã duyệt $N'$ | $D(v), p(v)$ | $D(w), p(w)$ | $D(x), p(x)$ | $D(y), p(y)$ | $D(z), p(z)$ | Nút được chọn tiếp theo |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Bước 0** *(Khởi tạo)* | $\{u\}$ | 2, u | $\infty$ | **1, u** | $\infty$ | $\infty$ | Chọn $x$ (min = 1) |
| **Bước 1** | $\{u, x\}$ | 2, u | 4, x | - | **2, x** | $\infty$ | Chọn $y$ (min = 2) |
| **Bước 2** | $\{u, x, y\}$ | **2, u** | 3, y | - | - | 4, y | Chọn $v$ (min = 2) |
| **Bước 3** | $\{u, x, y, v\}$ | - | **3, y** | - | - | 4, y | Chọn $w$ (min = 3) |
| **Bước 4** | $\{u, x, y, v, w\}$ | - | - | - | - | **4, y** | Chọn $z$ (min = 4) |
| **Bước 5** | $\{u, x, y, v, w, z\}$ | - | - | - | - | - | Hoàn tất (Đã duyệt đủ 6 nút) |

**Chi tiết tính toán cập nhật từng bước:**
- **Bước 0 (Khởi tạo)**: $N' = \{u\}$. Các nút lân cận trực tiếp của $u$ là $v$ ($c=2$) và $x$ ($c=1$). Các nút $w, y, z$ chưa kề nên có chi phí $\infty$. Nút $x$ có $D(x) = 1$ nhỏ nhất $\implies$ Đưa $x$ vào $N'$.
- **Bước 1 (Xét nút $x$, $D(x)=1$)**: Cập nhật các nút kề với $x$ chưa thuộc $N'$:
  - $D(v) = \min(D(v), D(x) + c(x, v)) = \min(2, 1 + 2) = 2, p(v) = u$ (giữ nguyên).
  - $D(w) = \min(D(w), D(x) + c(x, w)) = \min(\infty, 1 + 3) = 4, p(w) = x$.
  - $D(y) = \min(D(y), D(x) + c(x, y)) = \min(\infty, 1 + 1) = 2, p(y) = x$.
  - $D(z) = \infty$ (không nối với $x$).
  - Cả $v$ và $y$ đều có chi phí nhỏ nhất bằng 2. Theo trình tự bài giảng chuẩn, ưu tiên chọn $y$ $\implies$ Đưa $y$ vào $N'$. *(Lưu ý: Nếu chọn $v$ trước thì các bước sau vẫn cho ra cây đường đi ngắn nhất hoàn toàn tương đương)*.
- **Bước 2 (Xét nút $y$, $D(y)=2$)**: Cập nhật các nút kề với $y$ chưa thuộc $N'$:
  - $D(w) = \min(D(w), D(y) + c(y, w)) = \min(4, 2 + 1) = 3, p(w) = y$.
  - $D(z) = \min(D(z), D(y) + c(y, z)) = \min(\infty, 2 + 2) = 4, p(z) = y$.
  - $D(v)$ không đổi ($2, u$).
  - Trong các nút $\{v, w, z\}$, nút $v$ có chi phí nhỏ nhất ($D=2$) $\implies$ Đưa $v$ vào $N'$.
- **Bước 3 (Xét nút $v$, $D(v)=2$)**: Cập nhật các nút kề với $v$ chưa thuộc $N'$:
  - $D(w) = \min(D(w), D(v) + c(v, w)) = \min(3, 2 + 3) = 3, p(w) = y$ (giữ nguyên vì $3 < 5$).
  - $D(z)$ không đổi ($4, y$).
  - Nút $w$ có chi phí nhỏ nhất ($D=3$) $\implies$ Đưa $w$ vào $N'$.
- **Bước 4 (Xét nút $w$, $D(w)=3$)**: Cập nhật các nút kề với $w$ chưa thuộc $N'$:
  - $D(z) = \min(D(z), D(w) + c(w, z)) = \min(4, 3 + 5) = 4, p(z) = y$ (giữ nguyên vì $4 < 8$).
  - Nút $z$ là nút duy nhất còn lại ($D=4$) $\implies$ Đưa $z$ vào $N'$.
- **Bước 5**: Tất cả các nút trong mạng đã được kết nạp vào $N'$. Thuật toán kết thúc!

```text
CÂY ĐƯỜNG ĐI NGẮN NHẤT (SHORTEST PATH TREE) THU ĐƯỢC TỪ NÚT (u)
        u ──(2)──> v                       (Đến v: u -> v,           Cost = 2)
        │
        └──(1)──> x ──(1)──> y ──(1)──> w  (Đến x: u -> x,           Cost = 1)
                             │             (Đến y: u -> x -> y,      Cost = 2)
                             │             (Đến w: u -> x -> y -> w, Cost = 3)
                             └──(2)──> z   (Đến z: u -> x -> y -> z, Cost = 4)
```

**Bảng chuyển tiếp định tuyến (Forwarding Table) tại router nguồn $u$:**

| Đích đến (Destination) | Cổng xuất phát tiếp theo (Outgoing Link) | Tuyến đường đi ngắn nhất | Tổng chi phí (Least Cost) |
| :---: | :---: | :--- | :---: |
| $v$ | $(u, v)$ | $u \to v$ | 2 |
| $x$ | $(u, x)$ | $u \to x$ | 1 |
| $y$ | $(u, x)$ | $u \to x \to y$ | 2 |
| $w$ | $(u, x)$ | $u \to x \to y \to w$ | 3 |
| $z$ | $(u, x)$ | $u \to x \to y \to z$ | 4 |

- **Độ phức tạp**: $O(N^2)$, nếu sử dụng cấu trúc Min-Heap có thể tối ưu xuống $O(N \log N)$.
- **Nguy cơ dao động tuyến (Routing Oscillations)**: Nếu trọng số liên kết được gán theo lưu lượng thực tế (Congestion-sensitive routing), thuật toán Dijkstra có thể khiến lưu lượng dồn qua dồn lại giữa các tuyến luân phiên, gây mất ổn định mạng nghiêm trọng.

---

### B. Thuật toán Distance-Vector (Bellman-Ford Algorithm)
- **Nguyên lý**: Thuật toán phân tán, không đồng bộ và lặp (**Iterative, Asynchronous, Distributed**). Mỗi router không cần biết toàn bộ bản đồ mạng mà chỉ duy trì một **Vector khoảng cách (Distance Vector - DV)** lưu khoảng cách ước tính từ nó đến tất cả các nút mạng. Định kỳ (hoặc khi có thay đổi liên kết), router gửi vector này cho các hàng xóm trực tiếp kề nó.
- **Phương trình Bellman-Ford (Công thức cốt lõi)**:

$$d_x(y) = \min_v \left[ c(x, v) + d_v(y) \right]$$

  *Trong đó*:
  - $d_x(y)$: Chi phí đường đi ngắn nhất từ nút $x$ đến nút đích $y$.
  - $c(x, v)$: Chi phí liên kết trực tiếp từ nút $x$ đến nút lân cận (hàng xóm) $v$.
  - $d_v(y)$: Chi phí đường đi ngắn nhất từ hàng xóm $v$ đến đích $y$ (do $v$ thông báo cho $x$).
  - Phép lấy $\min_v$ được duyệt qua tất cả các hàng xóm trực tiếp $v$ của nút $x$. Nút hàng xóm $v^*$ mang lại giá trị nhỏ nhất chính là **cổng ra tiếp theo (Next Hop)** trên bảng chuyển tiếp của $x$.

---

#### Ví dụ giải thuật toán Bellman-Ford trên cùng mô hình mạng 6 nút (Đối chiếu Dijkstra)

Ta sử dụng lại chính xác mô hình mạng 6 nút $\{u, v, w, x, y, z\}$ đã dùng ở mục 5.2.A để theo dõi cách các vector khoảng cách lan truyền và hội tụ:

```text
MÔ HÌNH MẠNG THỬ NGHIỆM
       (2)───(v)───(3)───(w)───(5)
      /        │        / │      \
    (u)     (2)│     /(3) │(1)   (z)
      \        │  /       │      /
       (1)───(x)───(1)───(y)───(2)
```

**Quá trình tính toán lặp từng vòng qua các thời điểm $t$:**

1. **Khởi tạo ($t = 0$)**: Mỗi nút chỉ biết chi phí liên kết trực tiếp tới các hàng xóm kề nó; các nút còn lại chưa biết đường tới mang giá trị $\infty$:
   - $D_u = [u: 0, v: 2, w: \infty, x: 1, y: \infty, z: \infty]$
   - $D_v = [u: 2, v: 0, w: 3, x: 2, y: \infty, z: \infty]$
   - $D_w = [u: \infty, v: 3, w: 0, x: 3, y: 1, z: 5]$
   - $D_x = [u: 1, v: 2, w: 3, x: 0, y: 1, z: \infty]$
   - $D_y = [u: \infty, v: \infty, w: 1, x: 1, y: 0, z: 2]$
   - $D_z = [u: \infty, v: \infty, w: 5, x: \infty, y: 2, z: 0]$

2. **Vòng lặp 1 ($t = 1$)**: Mỗi nút gửi Distance Vector của mình cho các hàng xóm trực tiếp.
   - Nút $u$ nhận $D_v$ từ hàng xóm $v$ và $D_x$ từ hàng xóm $x$, áp dụng phương trình Bellman-Ford:
     - Đến $w$: $D_u(w) = \min [ c(u, v) + D_v(w), c(u, x) + D_x(w) ] = \min [ 2 + 3, 1 + 3 ] = \min [ 5, 4 ] = 4$ (Next Hop: **x**).
     - Đến $y$: $D_u(y) = \min [ c(u, v) + D_v(y), c(u, x) + D_x(y) ] = \min [ 2 + \infty, 1 + 1 ] = 2$ (Next Hop: **x**).
     - Đến $z$: $D_u(z) = \min [ c(u, v) + D_v(z), c(u, x) + D_x(z) ] = \min [ 2 + \infty, 1 + \infty ] = \infty$.
     $\Rightarrow$ Vector tại $u$ sau vòng 1: $D_u^{(1)} = [u: 0, v: 2, w: 4, x: 1, y: 2, z: \infty]$.
   - Các nút khác cũng cập nhật song song (ví dụ: $x$ nhận $D_y$ nên phát hiện đường tới $z$: $D_x(z) = 1 + 2 = 3$; tối ưu đường tới $w$: $D_x(w) = \min [ 3, 1 + 1 ] = 2$ qua $y$).

3. **Vòng lặp 2 ($t = 2$)**: Do vector của $x$ có thay đổi, $x$ gửi vector mới cho $u$. Nút $u$ tính toán lại:
   - Đến $w$: $D_u(w) = \min [ c(u, v) + D_v(w), c(u, x) + D_x(w) ] = \min [ 2 + 3, 1 + 2 ] = \min [ 5, 3 ] = \mathbf{3}$ (Next Hop: **x**).
   - Đến $z$: $D_u(z) = \min [ c(u, v) + D_v(z), c(u, x) + D_x(z) ] = \min [ 2 + \infty, 1 + 3 ] = \mathbf{4}$ (Next Hop: **x**).
   $\Rightarrow$ Vector tại $u$ sau vòng 2: $D_u^{(2)} = [u: 0, v: 2, w: 3, x: 1, y: 2, z: 4]$.

4. **Vòng lặp 3 ($t = 3$)**: Các router gửi lại vector khoảng cách. Không có nút nào ghi nhận thêm sự thay đổi chi phí $\Rightarrow$ **Thuật toán hội tụ hoàn toàn (Quiescent State)!**

**Bảng tổng kết quá trình tiến hóa Distance Vector tại nút nguồn $u$:**

| Thời điểm | $D_u(v)$ | $D_u(w)$ | $D_u(x)$ | $D_u(y)$ | $D_u(z)$ | Sự kiện & Ghi chú |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **$t = 0$** | 2 | $\infty$ | 1 | $\infty$ | $\infty$ | Khởi tạo ban đầu (chỉ biết liên kết trực tiếp $v, x$) |
| **$t = 1$** | 2 | 4 (qua x) | 1 | 2 (qua x) | $\infty$ | Nhận DV từ $v, x$; khám phá đường tới $w$ và $y$ |
| **$t = 2$** | 2 | **3** (qua x) | 1 | 2 (qua x) | **4** (qua x) | Cập nhật đường ngắn hơn tới $w$ ($u \to x \to y \to w$) và tìm thấy $z$ |
| **$t = 3$** | 2 | 3 | 1 | 2 | 4 | Không đổi $\Rightarrow$ **Hội tụ hoàn toàn!** |

> [!TIP]
> **Đối chiếu kết quả**: Bảng chi phí cuối cùng tại $u$ $[v: 2, w: 3, x: 1, y: 2, z: 4]$ cùng các cổng ra tương ứng ($v$ đi qua cổng trực tiếp $(u, v)$; các nút $w, x, y, z$ đều chuyển tiếp qua cổng $(u, x)$ ) **trùng khớp 100% với kết quả của thuật toán Dijkstra ở mục 5.2.A**.

---

#### Vấn đề Đếm đến vô cùng (Count-to-Infinity Problem)

```text
MÔ HÌNH VẤN ĐỀ ĐẾM ĐẾN VÔ CÙNG
             (x)
            /   \
        (4)/     \(50)
          /       \
        (y) ───── (z)
             (1)
```

1. **Trạng thái bình thường**:
   - Nút $y$ đi thẳng tới $x$: $D_y(x) = 4$ (Cổng kế tiếp / Next Hop: **x**).
   - Nút $z$ đi qua $y$ ($z \to y \to x$): $D_z(x) = c(z, y) + D_y(x) = 1 + 4 = 5$ (rẻ hơn nhiều so với đi thẳng qua liên kết dự phòng $c(z, x) = 50$).

2. **Khi sự cố xảy ra (Chi phí liên kết $x - y$ tăng đột biến từ 4 lên 60)**:
   - **Thời điểm $t_0$**: Nút $y$ phát hiện liên kết trực tiếp tới $x$ tăng vọt lên 60 ($c(y, x) = 60$). Nút $y$ tính lại theo Bellman-Ford:
     - Công thức tính: $D_y(x) = \min [ c(y, x), c(y, z) + D_z(x) ] = \min [ 60, 1 + 5 ] = 6$ (chọn đi qua **z**).
     - **Lỗi logic phát sinh**: Nút $y$ không hề biết con đường chi phí bằng 5 của $z$ thực chất lại đi ngược qua chính $y$!
     - Nút $y$ gửi thông báo mới cho $z$: $D_y(x) = 6$.
   - **Thời điểm $t_1$**: Nút $z$ nhận tin từ $y$, liền tính lại chi phí về $x$:
     - Công thức tính: $D_z(x) = \min [ c(z, x), c(z, y) + D_y(x) ] = \min [ 50, 1 + 6 ] = 7$ (vẫn chọn đi qua **y**).
     - Nút $z$ gửi lại thông báo mới cho $y$: $D_z(x) = 7$.
   - **Thời điểm $t_2$**: Nút $y$ nhận tin, tính lại $D_y(x) = 1 + 7 = 8$, rồi báo tiếp cho $z$...
   - **Vòng lặp đùn đẩy (Routing Loop)**: Hai nút $y$ và $z$ liên tục đùn đẩy nhau: $6 \to 7 \to 8 \to 9 \to \dots$
   - **Khi nào thì dừng lại?** Quá trình này chỉ dừng lại khi chi phí bị đùn đẩy vượt quá mốc **50** (chi phí của liên kết trực tiếp $c(z, x) = 50$). Lúc đó $z$ mới nhận ra đi thẳng trực tiếp tới $x$ với chi phí 50 rẻ hơn đi vòng qua $y$, và hệ thống mới hội tụ lại sau tận **44 vòng lặp**!
   - **Trường hợp đứt cáp hoàn toàn**: Nếu liên kết $x - y$ bị đứt hoàn toàn ($c = \infty$) và không có liên kết dự phòng 50, hai nút sẽ đùn đẩy nhau đếm mãi cho đến khi chạm ngưỡng vô cùng quy ước của giao thức (ví dụ $\infty = 16$ trong RIP).

> [!NOTE]
> **Giải pháp Kỹ thuật Poisoned Reverse**:
> - **Quy tắc**: Nếu nút $y$ định tuyến lưu lượng đến đích $x$ thông qua nút $z$, thì trong các bản tin quảng bá gửi riêng cho $z$, $y$ sẽ nói dối rằng: **Khoảng cách từ tôi đến $x$ là vô cùng** ($D_y(x) = \infty$).
> - Nhờ đó, $z$ sẽ không bao giờ định tuyến ngược lại qua $y$ khi liên kết gặp sự cố. Tuy nhiên, Poisoned Reverse chỉ giải quyết triệt để vòng lặp giữa 2 nút kề nhau, không giải quyết được vòng lặp từ 3 nút trở lên (vòng tròn $A \to B \to C \to A$).

---

### C. So sánh đối chiếu toàn diện: Link-State (Dijkstra) vs. Distance-Vector (Bellman-Ford)

Hai trường phái định tuyến giải quyết cùng một bài toán tìm đường ngắn nhất nhưng mang triết lý thiết kế và đặc tính vận hành hoàn toàn trái ngược:

| Tiêu chí so sánh | Link-State (Dijkstra) | Distance-Vector (Bellman-Ford) |
| :--- | :--- | :--- |
| **Phạm vi thông tin (Knowledge Scope)** | **Toàn cục (Global)**: Mọi router đều có bức tranh hoàn chỉnh về bản đồ cấu trúc mạng (Topology) và chi phí của mọi liên kết. | **Phân tán / Cục bộ (Decentralized)**: Mỗi router chỉ biết chi phí nối tới hàng xóm trực tiếp và nhận vector khoảng cách ước tính từ các hàng xóm. |
| **Cơ chế lan truyền thông tin** | Phát tán bản tin trạng thái liên kết (**LSA Flooding**) tới toàn bộ router trong mạng. | Chỉ trao đổi định kỳ hoặc kích hoạt khi có biến động giữa các **hàng xóm trực tiếp** kề nhau. |
| **Độ phức tạp thông điệp (Message Complexity)** | **Lớn**: Với $n$ router và $E$ liên kết, cần gửi $O(n \cdot E)$ bản tin phát tán khắp mạng mỗi khi có liên kết thay đổi trạng thái. | **Nhỏ**: Chỉ trao đổi cục bộ giữa các nút láng giềng kề nhau (số lượng thông điệp biến động tùy thuộc vào số vòng lặp hội tụ). |
| **Thuật toán & Tốc độ hội tụ** | Chạy thuật toán Dijkstra độc lập tại mỗi router ($O(n^2)$ với mảng duyệt, hoặc $O(E \log n)$ với Min-Heap). **Hội tụ nhanh** ngay khi nhận đủ bản đồ mạng; có thể gặp hiện tượng dao động tuyến (Oscillations). | Lặp từng bước qua các vòng ($t = 0, 1, 2\dots$). Tốc độ hội tụ biến động (chậm khi có sự cố tăng chi phí/đứt cáp); có thể gặp vòng lặp định tuyến (Routing Loops) và vấn đề đếm đến vô cùng (Count-to-Infinity). |
| **Nguy cơ lỗi định tuyến** | Không bao giờ bị vòng lặp định tuyến lâu dài (chỉ có thể thoáng qua trong khi đang flood LSA). Có thể gặp **dao động tuyến (Oscillations)** nếu trọng số phụ thuộc lưu lượng. | Rất dễ rơi vào **Vòng lặp định tuyến (Routing Loops)** và vấn đề **Đếm đến vô cùng (Count-to-Infinity)** khi liên kết bị đứt hoặc tăng chi phí đột biến. |
| **Độ bền vững trước sự cố (Robustness)** | **Rất cao**: Router lỗi chỉ có thể quảng bá sai chi phí của các liên kết trực tiếp với nó; mỗi router tự tính toán bảng định tuyến riêng nên lỗi bị cô lập. | **Thấp**: Một router quảng bá sai chi phí đường đi (do lỗi cấu hình hoặc bị tấn công) sẽ làm sai lệch vector của các hàng xóm, gây hiệu ứng domino lan truyền khắp mạng. |
| **Giao thức triển khai thực tế** | **OSPF**, **IS-IS** (Mạng lõi doanh nghiệp, mạng nội bộ ISP tốc độ cao). | **RIP** (Mạng nhỏ cổ điển), **BGP** (Mở rộng thành *Path-Vector* để chống vòng lặp trên phạm vi toàn cầu). |

---

## 5.3. Định tuyến phân cấp & Các hệ thống tự trị (Autonomous Systems - AS)
Để mạng Internet toàn cầu có thể mở rộng quy mô lên hàng trăm nghìn router mà không làm cạn kiệt bộ nhớ RAM hay nghẽn băng thông do trao đổi bản tin định tuyến, Internet được chia thành các **Hệ thống tự trị (Autonomous Systems - AS)**:

- **Hệ thống tự trị (AS)**: Tập hợp các router nằm dưới sự quản lý kỹ thuật và chính sách hành chính của cùng một tổ chức duy nhất (ví dụ: ISP Viettel, VNPT, FPT, Đại học Quốc gia...). Mỗi AS được IANA cấp một số định danh toàn cầu duy nhất gọi là **ASN (Autonomous System Number)**.

```text
KIẾN TRÚC ĐỊNH TUYẾN PHÂN CẤP INTERNET (INTRA-AS vs INTER-AS)
┌──────────────────────AS 1──────────────────────┐                ┌──────────────────────AS 2──────────────────────┐
│ [Router 1a] <════════OSPF════════> [Router 1c] │                │ [Router 2c] <════════OSPF════════> [Router 2b] │
│      \                                 /       │                │      \                                 /       │
│       \                               /        │                │       \                               /        │
│        └───────> [Router 1b] <───────┘         |                │        └───────> [Router 2a] <───────┘         │
│                   (Gateway)════════════════════╪═════ eBGP ═════╪══════════════════>(Gateway)                    │
└────────────────────────────────────────────────┘       ║        └────────────────────────────────────────────────┘
                                              (Trao đổi tuyến liên vùng)
```

### A. Định tuyến nội vùng (Intra-AS / IGP - Interior Gateway Protocol)
Chạy hoàn toàn bên trong ranh giới của một AS, tập trung tối đa vào **tốc độ và hiệu năng**:
- **OSPF (Open Shortest Path First - RFC 2328)**:
  - Giao thức phổ biến nhất hiện nay trong các mạng doanh nghiệp lớn và mạng lõi ISP.
  - Sử dụng thuật toán **Link-State (Dijkstra)**, đóng gói trực tiếp trong IP Datagram (`Protocol = 89`).
  - Hỗ trợ phân cấp thành nhiều **Vùng (Areas)**: Vùng lõi trung tâm gọi là **Backbone Area (Area 0)**, các Area khác kết nối vào Backbone qua các **ABR (Area Border Routers)** để thu gọn bảng định tuyến.
  - Hỗ trợ chứng thực bảo mật (MD5/SHA) ngăn chặn chèn LSA giả mạo.
- **RIP (Routing Information Protocol)**: Sử dụng Distance-Vector, giới hạn tối đa 15 Hops, chu kỳ phát sóng 30 giây (nay chỉ dùng cho mạng cổ điển hoặc phòng lab).
- **IS-IS (Intermediate System to Intermediate System)**: Tương tự OSPF, chạy trực tiếp trên tầng liên kết, thường dùng trong mạng lõi của các Telco viễn thông quốc tế.

---

### B. Định tuyến liên vùng (Inter-AS / EGP): Giao thức BGP (Border Gateway Protocol v4 - RFC 4271)
Được mệnh danh là **chất keo kết dính toàn bộ mạng Internet toàn cầu**. Chạy trên nền **TCP cổng 179** để đảm bảo độ tin cậy tuyệt đối:
- **eBGP (External BGP)**: Chạy giữa các Router biên (Gateway Routers) của hai AS khác nhau để trao đổi thông tin khả đạt của các dải IP mạng (*Reachability information*).
- **iBGP (Internal BGP)**: Chạy giữa các router bên trong cùng một AS để truyền bá thông tin về các tuyến đường mạng quốc tế nhận được từ eBGP.

```text
CƠ CHẾ QUẢNG BÁ TUYẾN ĐƯỜNG BGP VÀ PHÁT HIỆN VÒNG LẶP QUA AS-PATH
Mạng đích X ──> [ AS 3 ] ────(eBGP)────> [ AS 2 ] ────(eBGP)────> [ AS 1 ]
                ASN: 300                 ASN: 200                 ASN: 100
                Quảng bá:                Quảng bá:                Quảng bá:
                  Prefix: X                Prefix: X                Prefix: X
                  AS-PATH: [300]           AS-PATH: [200, 300]      AS-PATH: [100, 200, 300]
                  Next-Hop: IP Router 3    Next-Hop: IP Router 2    Next-Hop: IP Router 1

* Nếu AS 1 gửi quảng bá ngược lại cho AS 3:
  AS 3 kiểm tra thấy số hiệu ASN 300 của chính mình đã nằm trong AS-PATH
  => AS 3 hủy bỏ ngay lập tức để triệt tiêu vòng lặp định tuyến toàn cầu
```

- **Các thuộc tính quan trọng của BGP Route (`Route = Prefix + Attributes`)**:
  - `AS-PATH`: Danh sách toàn bộ các ASN mà gói tin quảng bá đã đi qua. Cực kỳ quan trọng để **phát hiện và triệt tiêu vòng lặp định tuyến**.
  - `NEXT-HOP`: Địa chỉ IP của Router biên tiếp theo trên chặng đường rời khỏi AS.
- **Định tuyến theo chính sách (Policy-Based Routing)**:
  - BGP **không nhất thiết chọn con đường ngắn nhất**, mà ưu tiên tối đa các **thỏa thuận kinh tế và chính sách bảo mật** giữa các AS (ví dụ: Nhà mạng Viettel có thể cấu hình từ chối chuyển tiếp lưu lượng miễn phí hộ cho đối thủ cạnh tranh).
- **Kỹ thuật Hot-Potato Routing (Củ khoai tây nóng)**:
  - Router tìm cách tống khứ gói tin ra khỏi ranh giới AS của chính nó càng sớm càng tốt qua cổng Gateway gần nhất có chi phí nội bộ (IGP cost) thấp nhất, bất kể chặng đường tiếp theo bên ngoài dài bao nhiêu.

---

## 5.4. Giao thức ICMP và SNMP

### A. ICMP (Internet Control Message Protocol - RFC 792)
Được đóng gói trực tiếp bên trong gói tin IP (`Protocol = 1`), dùng để báo cáo các sự cố mạng và thăm dò chẩn đoán trạng thái.

| Type | Code | Ý nghĩa thông điệp | Ứng dụng thực tế |
| :---: | :---: | :--- | :--- |
| **0** | **0** | Echo Reply (Trả lời thăm dò) | Phản hồi thành công của lệnh `ping` |
| **8** | **0** | Echo Request (Yêu cầu thăm dò) | Gói tin phát đi của lệnh `ping` |
| **3** | **0** | Destination Network Unreachable | Router không có đường đi tới mạng đích |
| **3** | **1** | Destination Host Unreachable | Không tìm thấy máy đích trong mạng con (ARP thất bại) |
| **3** | **3** | Destination Port Unreachable | Máy đích không có tiến trình nào lắng nghe cổng này (UDP) |
| **11** | **0** | Time Exceeded (TTL expired in transit) | Gói tin bị giảm $TTL = 0$; cốt lõi của lệnh `traceroute` |

```text
NGUYÊN LÝ HOẠT ĐỘNG CỦA LỆNH TRACEROUTE BẰNG ICMP TIME EXCEEDED
[ Máy nguồn Client ]             [ Router R1 ]             [ Router R2 ]             [ Máy đích Server ]
         │                             │                         │                             │
         │─── 1. Gói IP (TTL = 1) ────>│                         │                             │
         │                             │(Giảm TTL = 0 -> HỦY GÓI)|                             │
         │<─── ICMP Type 11 Code 0 ────│                         │                             │
         │    (Biết được IP của R1 & đo RTT chặng 1)             │                             │
         │                                                       │                             │
         │─── 2. Gói IP (TTL = 2) ──────────────────────────────>│                             │
         │                                                       │  (Giảm TTL = 0 -> HỦY GÓI)  │
         │<─── ICMP Type 11 Code 0 ──────────────────────────────│                             │
         │    (Biết được IP của R2 & đo RTT chặng 2)                                           │
         │                                                                                     │
         │─── 3. Gói IP (TTL = 3) ────────────────────────────────────────────────────────────>│
         │                                                              (Gói tin tới đích)     │
         │<─── ICMP Port Unreachable (hoặc Echo Reply) ────────────────────────────────────────│
         ▼
```

---

### B. SNMP (Simple Network Management Protocol)
Giao thức chuẩn để quản trị viên giám sát trạng thái phần cứng, tải lưu lượng, nhiệt độ của các thiết bị mạng từ xa.
- **SNMP Manager (Client)**: Trạm điều khiển trung tâm gửi truy vấn `GetRequest`, `SetRequest`.
- **SNMP Agent (Server)**: Tiến trình chạy ngầm trên thiết bị mạng, lưu trữ thông số trạng thái trong cơ sở dữ liệu **MIB (Management Information Base)**.
- **Trap Message**: Tín hiệu cảnh báo do Agent chủ động gửi về Manager khi thiết bị gặp sự cố bất thường (mất nguồn, cổng mạng bị down).

---

<a id="chuong-6"></a>
# CHƯƠNG 6: TẦNG LIÊN KẾT DỮ LIỆU VÀ MẠNG CỤC BỘ (LINK LAYER AND LANS)
> 📄 **Slide bài giảng:** [Chapter_6_v9.0.pdf](.pdf/Chapter_6_v9.0.pdf)

## 6.1. Dịch vụ tầng liên kết & Đóng gói Khung (Framing)
Trong khi Tầng Mạng (Network Layer) chịu trách nhiệm tìm đường và chuyển tiếp gói tin từ máy gửi tới máy nhận trên phạm vi toàn cầu (**Host-to-Host**), thì **Tầng Liên kết (Data Link Layer)** chịu trách nhiệm vận chuyển gói tin qua **từng chặng đơn lẻ (Hop-by-Hop)** giữa hai nút mạng kề nhau kết nối trực tiếp qua một đường truyền vật lý.

- **Các thuật ngữ cơ bản**:
  - **Nút mạng (Nodes)**: Mọi thiết bị tham gia truyền thông ở tầng liên kết: Máy tính cá nhân, Máy chủ, Router, Switch...
  - **Đường liên kết (Links)**: Kênh truyền thông kết nối trực tiếp giữa các nút liền kề (Cáp xoắn đôi, Cáp quang, Sóng vô tuyến Wi-Fi).
  - **Khung dữ liệu (Frame)**: Đơn vị dữ liệu giao thức (PDU) của tầng liên kết, bao gồm IP Datagram từ Tầng 3 được kẹp giữa **Header** và **Trailer** tầng 2.
- **Phân loại mạng theo phạm vi địa lý**:
  > **LAN < MAN < WAN < GAN**
  - **LAN (Local Area Network)**: Mạng cục bộ trong phạm vi một phòng, tòa nhà, văn phòng (dưới 1 km).
  - **MAN (Metropolitan Area Network)**: Mạng đô thị kết nối trong phạm vi một thành phố (vài chục km).
  - **WAN (Wide Area Network)**: Mạng diện rộng kết nối xuyên quốc gia, châu lục (hàng nghìn km).
  - **GAN (Global Area Network)**: Mạng toàn cầu kết nối toàn Trái Đất và các trạm vệ tinh không gian.
- **Vị trí thực thi**: Tầng liên kết được tích hợp trực tiếp vào phần cứng **Card mạng (NIC - Network Interface Card)**, kết hợp giữa chip điều khiển phần cứng (*Link Controller*) và bộ điều khiển phần mềm của hệ điều hành.

---

## 6.2. Các kỹ thuật phát hiện và sửa sai (Error Detection & Correction)
Tín hiệu truyền trên môi trường vật lý luôn có nguy cơ bị suy hao, méo dạng hoặc nhiễu điện từ dẫn tới hiện tượng lật bit ($0 \to 1$ hoặc $1 \to 0$). Tầng liên kết bảo vệ dữ liệu bằng cách gắn thêm trường **EDC (Error-Detection and-Correction bits)** vào đuôi Frame:

```text
CƠ CHẾ BẢO VỆ DỮ LIỆU TẠI TẦNG LIÊN KẾT BẰNG EDC
Bên gửi:   [ Dữ liệu Payload (D) ] + [ Mã phát hiện lỗi (EDC) ]
                          \                   /
                           ▼                 ▼
                      [ Khung dữ liệu truyền đi ]
                                  │
                                  ▼ (Bị suy hao, nhiễu điện từ làm lật bit)
Bên nhận:  [ Dữ liệu nhận D' ]   và   [ Mã nhận EDC' ]
                   │                        │
                   |         ┌───────────────────────────────┐
                   └────────>│ BỘ KIỂM TRA MẬT MÃ / TOÁN HỌC │
                             └──────────────┬────────────────┘
                                            │
                                    ┌───────┴───────┐
                                    │               │
                                (Hợp lệ)        (Có lỗi bit)
                                    ▼                ▼
                           Nhận dữ liệu D'     Vứt bỏ Frame (Drop)
```

### A. Kiểm tra chẵn lẻ (Parity Check)
- **Single Parity (1 chiều)**: Đếm tổng số bit 1 trong khối dữ liệu, chèn thêm 1 bit Parity vào cuối sao cho tổng số bit 1 luôn là số chẵn (*Even Parity*) hoặc số lẻ (*Odd Parity*).
  - *Hạn chế*: Chỉ phát hiện được lỗi khi số lượng bit bị lật là **số lẻ** (1, 3, 5 bit). Nếu bị lật 2 bit cùng lúc, Parity Check hoàn toàn bị qua mặt.
- **Two-Dimensional Parity (2 chiều)**: Xếp các byte dữ liệu thành một ma trận $m \times n$, tính bit Parity cho từng hàng và từng cột.
  - *Ưu điểm vượt trội*: Có khả năng **phát hiện và tự động sửa sai chính xác 1 bit lỗi** tại giao điểm của hàng và cột bị sai mà không cần yêu cầu truyền lại (*Forward Error Correction - FEC*).

### B. Internet Checksum (Mã kiểm tra bù 1)
Cộng toàn bộ các khối 16-bit dữ liệu lại với nhau, cộng dồn phần nhớ (*End-around carry*) rồi lấy phần bù 1. Thường dùng trong TCP, UDP và IPv4 Header vì dễ cài đặt bằng phần mềm CPU.

### C. Mã vòng dư thừa CRC (Cyclic Redundancy Check)
Phương pháp toán học mạnh mẽ nhất, được cài đặt trực tiếp vào phần cứng của mọi card mạng Ethernet và Wi-Fi:
- **Nguyên lý toán học**: Xem chuỗi dữ liệu $D$ (gồm $d$ bits) như một đa thức nhị phân. Bên gửi và bên nhận thống nhất trước một đa thức sinh chuẩn **$G$ (gồm $r+1$ bits)**, trong đó bit đầu và bit cuối luôn bằng 1.
- **Quy tắc bên gửi**: Thêm $r$ bit 0 vào đuôi của $D$ (tương đương phép nhân $D \times 2^r$). Sau đó thực hiện phép **chia Modulo-2 (dùng phép XOR, không nhớ không mượn)** cho đa thức $G$ để thu được số dư $R$ (gồm đúng $r$ bits). Gắn $R$ vào đuôi dữ liệu để phát đi: $[D, R]$.
- **Quy tắc bên nhận**: Lấy toàn bộ chuỗi $[D, R]$ nhận được chia Modulo-2 cho $G$. Nếu số dư $= 0 \implies$ Dữ liệu nguyên vẹn; nếu số dư $\neq 0 \implies$ Bị lỗi bit, lập tức hủy Frame.

```text
VÍ DỤ TÍNH TOÁN CRC CHIA MODULO-2 BẰNG PHÉP TOÁN XOR
Cho Dữ liệu D = 101110 (6 bits), Đa thức sinh G = 1001 (r+1 = 4 bits -> r = 3 bits)
Bên gửi thêm r = 3 bit 0 vào sau D: 101110000

Thực hiện chia Modulo-2 (Phép XOR: 0 XOR 0 = 0, 1 XOR 1 = 0, khác nhau = 1):
  101110000  | 1001 (G)
  1001       |────────────
  ────       | Thương (bỏ qua)
  001010
    1001
    ────
    001100
      1001
      ────
      01010
       1001
       ────
       00110
         000 (Hết lượt chia)
         ───
         011 <─── Đây là Số dư R (gồm đúng r = 3 bits: 011)

=> Khung dữ liệu phát đi thực tế: [ D, R ] = 101110 011
Bên nhận lấy 101110011 chia cho 1001 -> Số dư chính xác bằng 000
```

---

## 6.3. Các giao thức đa truy cập (Multiple Access Protocols)
Khi nhiều nút mạng cùng chia sẻ một môi trường truyền dẫn vật lý (chung một sợi dây cáp mạng hoặc chung một dải sóng vô tuyến), nếu hai thiết bị phát tín hiệu cùng lúc sẽ xảy ra hiện tượng **Đụng độ / Xung đột (Collision)** làm hỏng dữ liệu của cả hai.

```text
BA TRƯỜNG PHÁI GIAO THỨC ĐA TRUY CẬP (MAC PROTOCOLS)
┌───────────────────────────────────────────────────────────────────────────────┐
│                    CÁC GIAO THỨC ĐA TRUY CẬP (MAC)                            │
└──────────────────────────────────────┬────────────────────────────────────────┘
         ┌─────────────────────────────┼─────────────────────────────┐
         ▼                             ▼                             ▼
[ 1. Channel Partitioning ]    [ 2. Random Access ]          [ 3. Taking-Turns ]
- Chia kênh truyền thành       - Không chia kênh cố định     - Luân phiên lấy lượt
  các phần độc lập:              Mọi nút đều có thể gửi ở      kết hợp ưu điểm cả hai:
  + TDMA: Chia thời gian         tốc độ tối đa R:              + Polling (Hỏi vòng)
  + FDMA: Chia tần số            + ALOHA / Slotted ALOHA       + Token Passing
  + CDMA: Chia theo mã           + CSMA/CD (Ethernet)            (Chuyền thẻ bài)
                                 + CSMA/CA (Wi-Fi)
```

### A. Nhóm Phân chia kênh truyền (Channel Partitioning Protocols)
Chia tài nguyên kênh truyền có tổng băng thông $R$ thành các phần nhỏ hơn độc lập (theo thời gian, tần số hoặc mã), phân bổ cố định cho từng nút mạng sử dụng độc quyền $\implies$ **Hoàn toàn triệt tiêu nguy cơ xảy ra đụng độ (Collision-free)**.

#### 1. TDMA (Time Division Multiple Access - Phân chia theo thời gian):
- **Nguyên lý**: Kênh truyền được truy cập theo các vòng lặp, mỗi vòng chia thành $N$ khe thời gian cố định có độ dài đúng bằng thời gian truyền 1 gói tin.
- **Cơ chế**: Mỗi nút mạng được phân bổ một khe thời gian cố định trong mỗi vòng. Nút chỉ được truyền dữ liệu ở tốc độ tối đa $R$ khi đến đúng khe của mình.
- **Hạn chế**: Kém linh hoạt khi tải thấp; nếu nút không có dữ liệu cần gửi thì khe thời gian của nó bị bỏ trống, trong khi các nút khác vẫn bị giới hạn tốc độ trung bình ở mức $R/N$.

#### 2. FDMA (Frequency Division Multiple Access - Phân chia theo tần số):
- **Nguyên lý**: Dải phổ tần số của kênh truyền được chia thành $N$ dải tần hẹp hơn, mỗi dải có độ rộng băng thông $R/N$.
- **Cơ chế**: Mỗi nút mạng được gán riêng một dải tần số cố định và có thể truyền dữ liệu liên tục mọi lúc mà không cần chờ đợi theo vòng.
- **Hạn chế**: Tương tự TDMA, nếu một nút không truyền thì dải tần số đó bị lãng phí; tốc độ tối đa của mỗi nút bị khóa cứng ở $R/N$ ngay cả khi tất cả các nút khác đều không hoạt động.

#### 3. CDMA (Code Division Multiple Access - Phân chia theo mã):
- **Nguyên lý**: Tất cả các nút được phép truyền **đồng thời cùng lúc trên cùng một dải tần số**, nhưng mỗi nút được gán một **chuỗi mã định danh duy nhất (Chipping Sequence / Chipping Code)** có tính chất trực giao toán học với nhau.
- **Cơ chế**: Dữ liệu của nút được nhân với chuỗi mã chip trước khi phát đi. Bên nhận dùng chính mã chip của nút gửi để giải mã (bằng phép nhân vô hướng / tích phân), triệt tiêu toàn bộ tín hiệu của các nút khác như thể chỉ là tạp âm nền ngẫu nhiên.
- **Ứng dụng thực tế**: Mạng viễn thông di động 3G (WCDMA, CDMA2000), hệ thống định vị vệ tinh GPS và truyền thông quân sự kháng nhiễu/chống nghe lén.

> [!NOTE]
> **Đặc điểm đánh đổi (Trade-off) của Channel Partitioning**:
> - **Ưu điểm**: Hoạt động cực kỳ hiệu quả, công bằng và ổn định khi mạng có **tải cao (High Load)** vì không tốn băng thông hao phí do đụng độ.
> - **Nhược điểm**: Kém hiệu quả khi mạng có **tải thấp (Low Load)** vì tài nguyên bị chia cứng nhắc, gây lãng phí băng thông rảnh rỗi và tạo độ trễ truy cập kênh không đáng có.

---

### B. Nhóm Truy cập ngẫu nhiên (Random Access Protocols)

#### 1. ALOHA và Slotted ALOHA:
- **Pure ALOHA**: Bất kỳ nút mạng nào có dữ liệu đều phát đi ngay lập tức mà không kiểm tra đường truyền. Tỷ lệ đụng độ cực cao. Hiệu suất tối đa chỉ đạt **18.4%** ($1 / 2e$).
- **Slotted ALOHA**: Thời gian được chia thành các khe (*Slots*) bằng nhau đúng bằng thời gian truyền 1 khung. Nút mạng chỉ được phép bắt đầu phát ở **điểm đầu của một khe thời gian**. Nếu đụng độ, chúng sẽ đụng độ ngay từ đầu khe. Hiệu suất tối đa tăng gấp đôi, đạt **36.8%** ($1 / e$).

#### 2. Giao thức CSMA (Carrier Sense Multiple Access):
Triết lý kinh điển: *"Nghe trước khi nói (Listen before talk)"*. Trước khi gửi, nút mạng lắng nghe kênh truyền; nếu thấy kênh đang bận (có tín hiệu), nó hoãn lại việc gửi.

#### Bảng so sánh chuyên sâu giữa CSMA/CD và CSMA/CA:

| Tiêu chí so sánh | CSMA/CD (Collision Detection) | CSMA/CA (Collision Avoidance) |
| :--- | :--- | :--- |
| **Môi trường hoạt động** | **Mạng có dây Ethernet (IEEE 802.3)** | **Mạng không dây Wi-Fi (IEEE 802.11)** |
| **Triết lý kiểm soát** | *"Nghe trước khi nói, vừa nói vừa nghe, phát hiện đụng độ thì lập tức dừng lại."* | *"Nghe trước khi nói, chủ động tránh đụng độ bằng cơ chế bảo lưu thời gian và bắt tay RTS/CTS."* |
| **Khả năng phát hiện xung đột** | **Có thể phát hiện ngay lập tức** bằng cách đo mức điện áp bất thường trên dây đồng. | **Không thể vừa phát vừa nghe** (năng lượng phát của ăng-ten chính nó quá mạnh, át hoàn toàn tín hiệu nhận yếu ớt). |
| **Hành động khi phát hiện đụng độ** | 1. Phát tín hiệu kẹt mứt (**Jam Signal 48-bit**) để báo cho toàn mạng.<br>2. Hủy truyền khung dữ liệu lập tức để tiết kiệm băng thông.<br>3. Chờ một khoảng ngẫu nhiên theo thuật toán **Binary Exponential Backoff** ($0 \le K \le 2^m - 1$) rồi thử lại. | Không phát hiện được đụng độ trực tiếp. Nếu sau một khoảng thời gian quy định không nhận được khung **ACK** phản hồi từ Access Point $\implies$ Coi như đã xảy ra đụng độ, tăng gấp đôi cửa sổ tranh chấp (*Contention Window*) và thử lại. |

---

### C. Nhóm Luân phiên lượt truyền (Taking-Turns Protocols)
- **Polling (Hỏi vòng)**: Có một nút chủ (**Master Node**) lần lượt gửi thông điệp thăm dò từng nút con (**Slave Nodes**) theo vòng tròn: *"Bạn có dữ liệu cần gửi không?"*. Nút con chỉ được truyền khi có lệnh từ Master.
  - *Nhược điểm*: Polling Overhead (lãng phí băng thông trao đổi hỏi han), Độ trễ xếp hàng, và rủi ro **Single Point of Failure** (Master chết là toàn mạng sập).
- **Token Passing (Chuyền thẻ bài)**: Các nút nối nhau thành một vòng tròn logic. Một khung dữ liệu đặc biệt gọi là **Token (Thẻ bài)** được luân chuyển tuần tự từ nút này sang nút khác. Nút nào đang nắm giữ Token mới có quyền phát dữ liệu lên đường truyền; phát xong phải trao lại Token cho nút kế tiếp.
  - *Nhược điểm*: Token Overhead, nếu chẳng may Token bị mất do nhiễu bit thì phải có quy trình bầu cử phức tạp để tái tạo Token mới.

---

## 6.4. Địa chỉ MAC và Giao thức ARP (Address Resolution Protocol)

### A. Địa chỉ MAC (Media Access Control Address)
- Địa chỉ định danh phần cứng vật lý dài **48 bits (6 Bytes)**, thường biểu diễn bằng 12 chữ số thập lục phân (Hexadecimal) ngăn cách bởi dấu hai chấm hoặc dấu gạch nối (ví dụ: `00:1A:2B:3C:4D:5E`).
- **Cấu trúc 2 nửa**:
  - **24 bits đầu (3 Bytes)**: Mã định danh duy nhất của nhà sản xuất phần cứng **OUI (Organizationally Unique Identifier)** do tổ chức IEEE quản lý cấp phép.
  - **24 bits sau (3 Bytes)**: Số sê-ri card mạng do chính hãng sản xuất tự đánh số trên dây chuyền (*Burned-in Address*).
- **Địa chỉ MAC Broadcast**: `FF:FF:FF:FF:FF:FF` (toàn bộ 48 bit là 1), gửi tới tất cả các card mạng trong cùng một mạng LAN.

> [!IMPORTANT]
> **Sự khác biệt cốt lõi giữa Địa chỉ IP và Địa chỉ MAC**:
> - **Địa chỉ IP (Tầng 3)**: Mang tính chất **phân cấp thứ bậc (Hierarchical)** giống như địa chỉ bưu điện nhà bạn (Quốc gia $\to$ Thành phố $\to$ Quận $\to$ Số nhà). Dùng để Router tìm đường dẫn đi xuyên qua các mạng khác nhau trên toàn cầu.
> - **Địa chỉ MAC (Tầng 2)**: Mang tính chất **phẳng (Flat)** giống như số Căn cước công dân (CCCD). Dù máy tính di chuyển tới bất kỳ mạng Wi-Fi hay văn phòng nào trên thế giới, địa chỉ MAC trên card mạng vẫn không đổi. Dùng cho Switch phân phát khung dữ liệu cục bộ trong cùng một mạng LAN.

---

### B. Giao thức ARP (Address Resolution Protocol - RFC 826)
- **Bản chất cốt lõi**: Hiểu đơn giản thì ARP là một giao thức **ánh xạ địa chỉ IP sang địa chỉ MAC** (hoạt động ngay giữa ranh giới Tầng 2 và Tầng 3). Khi một máy tính biết địa chỉ IP đích của máy trong cùng mạng LAN nhưng chưa biết địa chỉ MAC tương ứng để đóng gói Ethernet Frame, nó sẽ dùng ARP để truy tìm địa chỉ MAC.
- **Bảng ánh xạ ARP (ARP Table / ARP Cache)**: Giao thức ARP được thể hiện và duy trì thông qua bảng ARP Table lưu trữ tạm thời trong RAM của thiết bị với 3 thông số:
  - **IP address**: Địa chỉ IP của nút trong cùng mạng mạng LAN.
  - **MAC address**: Địa chỉ MAC tương ứng của card mạng đó.
  - **TTL (Time To Live)**: Thời gian sống của bản ghi trong bộ nhớ tạm (thường là 20 - 30 phút). Hết thời gian này, bản ghi tự động bị xóa (*Aging Timer*) để giải phóng bộ nhớ và cho phép cập nhật lại khi card mạng thay đổi.
- **Thiết bị nào sở hữu ARP Table?**:
  - Cứ thiết bị nào cần xài địa chỉ IP để giao tiếp thì chắc chắn có ARP Table (từ điện thoại, máy tính ở *Network Edge* cho đến router ở *Network Core*).
  - Các ngoại lệ duy nhất chỉ là những thiết bị trung chuyển vật lý thuần túy (như Switch thường Tầng 2, Hub, dây cáp), vì chúng chỉ chuyển tiếp dựa trên tín hiệu vật lý hoặc địa chỉ MAC mà không quan tâm đến IP.

- **Tiến trình hoạt động của ARP gồm 2 bước kinh điển**:

```text
QUÁ TRÌNH HỎI ĐÁP PHÂN GIẢI ĐỊA CHỈ ARP TRONG MẠNG CỤC BỘ
[ Máy A: IP 192.168.1.10 ]                                   [ Máy B: IP 192.168.1.20 ]
[ MAC: AA:AA:AA:AA:AA:AA ]                                   [ MAC: BB:BB:BB:BB:BB:BB ]
             │                                                            │
             │─────── 1. ARP Request (BROADCAST toàn mạng) ──────────────>│
             │   Dest MAC: FF:FF:FF:FF:FF:FF                              │
             │   "Ai giữ IP 192.168.1.20? Hãy báo MAC cho IP 1.10 biết!"  │
             │   (Mọi máy trong LAN đều nhận được gói này)                │
             │                                                            │
          ══════════(Máy B thấy đúng IP mình -> Lưu MAC A vào Cache)══════════
             │                                                            │
             │<────── 2. ARP Reply (UNICAST gửi riêng cho A) ─────────────│
             │   Dest MAC: AA:AA:AA:AA:AA:AA                              │
             │   "Tôi giữ IP 192.168.1.20 và MAC của tôi là: BB:BB...BB"  │
             ▼                                                            ▼
(Máy A lưu vào ARP Cache:                                    (Máy B đã có sẵn MAC A)
 IP 192.168.1.20 <-> BB:BB...BB)
```

---

## 6.5. Mạng cục bộ Ethernet (IEEE 802.3)
Ethernet là công nghệ mạng cục bộ có dây thống trị tuyệt đối trong suốt hơn 4 thập kỷ qua.
- **Hai đặc tính cốt lõi**:
  - **Connectionless (Không kết nối)**: Card mạng phát khung dữ liệu đi mà không cần trải qua quá trình bắt tay thiết lập kênh truyền.
  - **Unreliable (Không tin cậy)**: Khi nhận frame, nếu bộ kiểm tra CRC thấy có lỗi bit, card mạng lập tức **vứt bỏ Frame (Drop)** mà hoàn toàn không gửi thông báo lỗi hay yêu cầu gửi lại (việc phát hiện mất mát và gửi lại phụ thuộc hoàn toàn vào giao thức TCP ở tầng trên).

### Cấu trúc Khung dữ liệu Ethernet (Ethernet Frame Structure):
```text
CHI TIẾT CẤU TRÚC KHUNG DỮ LIỆU ETHERNET (802.3 FRAME)
┌───────────┬─────────────┬─────────────┬───────────┬──────────────────────┬───────────┐
│ Preamble  │  Dest MAC   │ Source MAC  │   Type    │     Data Payload     │  CRC/FCS  │
│ (8 Bytes) │  (6 Bytes)  │  (6 Bytes)  │ (2 Bytes) │  (46 -> 1500 Bytes)  │ (4 Bytes) │
└───────────┴─────────────┴─────────────┴───────────┴──────────────────────┴───────────┘
```

- **Preamble (8 Bytes)**: Gồm 7 byte `10101010` dùng để đồng bộ hóa tốc độ xung nhịp (*Clock Synchronization*) giữa máy gửi và máy nhận, kết thúc bằng 1 byte `10101011` (**SFD - Start Frame Delimiter**) báo hiệu dữ liệu thực sự bắt đầu ngay phía sau.
- **Destination & Source MAC (6 Bytes mỗi trường)**: Địa chỉ phần cứng của bên nhận và bên gửi.
- **Type (2 Bytes)**: Cho biết giao thức Tầng 3 nằm trong Payload để đưa vào đúng tiến trình xử lý:
  - `0x0800`: IPv4 Datagram
  - `0x86DD`: IPv6 Datagram
  - `0x0806`: ARP Packet
- **Data Payload (46 đến 1500 Bytes)**: Chứa gói tin IP Datagram.
  - **Quy tắc đệm dữ liệu (Padding)**: Kích thước Payload tối thiểu phải là **46 Bytes**. Nếu gói tin IP ngắn hơn 46 Bytes, card mạng phải chèn thêm các byte rác (`0x00`) cho đủ 46 Bytes.
  - **Nguyên nhân kỹ thuật**: Nhằm đảm bảo toàn bộ Ethernet Frame có độ dài tối thiểu là **64 Bytes** ($6 + 6 + 2 + 46 + 4 = 64$ Bytes). Kích thước tối thiểu 64 Bytes đảm bảo rằng máy gửi vẫn đang trong quá trình phát khung tín hiệu khi một xung đột ở xa nhất có thể phản hồi quay về, giúp cơ chế CSMA/CD phát hiện đụng độ thành công!
- **CRC / FCS (4 Bytes)**: Mã kiểm tra phần cứng 32-bit (Cyclic Redundancy Check) phát hiện lỗi bit.

> [!NOTE]
> **Tại sao Preamble (8 Bytes) không được tính vào kích thước Ethernet Frame?**
> - **Thuộc Tầng Vật lý (Layer 1)**: Preamble chỉ là chuỗi xung nhịp vật lý giúp chip thu phát PHY đồng bộ hóa tần số (*Clock Sync*). Ngay khi nhận diện xong byte báo hiệu SFD, chip PHY sẽ **bóc bỏ (strip)** toàn bộ 8 byte này trước khi chuyển giao khung dữ liệu lên Tầng 2 (MAC Controller).
> - **Không được bảo vệ bởi CRC**: Vùng tính toán của mã CRC-32 chỉ tính từ `Dest MAC` đến hết `Payload`, hoàn toàn loại trừ Preamble.
> - **Quy chuẩn IEEE 802.3**: Khung Ethernet chuẩn chỉ tính từ **Destination MAC** đến hết **CRC/FCS** (kích thước tối thiểu là **64 Bytes**, tối đa là **1518 Bytes**). Vì vậy, các công cụ phân tích mạng như Wireshark không bao giờ hiển thị 8 byte Preamble này.

---

## 6.6. Thiết bị Chuyển mạch Tầng 2 (Link-Layer Switch)
Switch là thiết bị mạng Tầng 2 giúp lọc và chuyển tiếp các frame dựa trên bảng địa chỉ MAC.

### A. Cơ chế Tự học (Self-Learning) & Bảng chuyển mạch (Switch Table / CAM Table)
Switch hoạt động theo triết lý "Cắm là chạy (*Plug-and-Play*)", hoàn toàn không cần cấu hình thủ công:
1. Khi có một frame đi vào cổng $x$, switch đọc địa chỉ **Source MAC**.
2. Nó ghi nhớ ngay cặp thông tin: `[Source MAC, Cổng x, TTL (Time-To-Live)]` vào bảng **CAM (Content Addressable Memory)**.
3. Tiếp theo, switch đọc địa chỉ **Destination MAC** trong frame để đưa ra quyết định:
   - **Đã có Destination MAC trong bảng**: Chuyển tiếp khung ra **đúng cổng đích duy nhất**.
   - **Chưa có Destination MAC trong bảng**: Thực hiện tràn luồng (**Flooding**) - gửi nhân bản khung ra tất cả các cổng còn lại (trừ cổng nhận vào).
   - **Destination MAC là Broadcast (`FF:FF...FF`)**: Gửi tràn ra tất cả các cổng còn lại.

```text
TIẾN TRÌNH TỰ HỌC (SELF-LEARNING) VÀ CHUYỂN TIẾP CỦA SWITCH TẦNG 2
        [Máy A] (Cổng 1)                         [Máy B] (Cổng 2)
           │                                        │
           └───> ┌────────────────────────────┐ <───┘
                 │       SWITCH TẦNG 2        │
           ┌───> │  (Bảng CAM ban đầu: RỖNG)  │ <───┐
           │     └────────────────────────────┘     │
        [Máy C] (Cổng 3)                         [Máy D] (Cổng 4)

Kịch bản 1: Máy A gửi frame cho Máy B (Bảng CAM đang rỗng):
- Switch nhận frame từ Cổng 1 -> Học ngay: [MAC_A -> Cổng 1].
- Switch tìm MAC_B trong bảng -> KHÔNG THẤY.
- Switch FLOODING (Chuyển bản sao ra Cổng 2, Cổng 3, Cổng 4).
- Máy C và D thấy Dest MAC không phải của mình -> Hủy frame.
- Máy B nhận frame, thấy đúng MAC mình -> Xử lý.

Kịch bản 2: Máy B phản hồi gửi frame cho Máy A:
- Switch nhận frame từ Cổng 2 -> Học ngay: [MAC_B -> Cổng 2].
- Switch tìm MAC_A trong bảng -> ĐÃ CÓ: [MAC_A -> Cổng 1].
- Switch CHUYỂN TIẾP CÓ CHỌN LỌC duy nhất ra Cổng 1.
- Cổng 3 và Cổng 4 hoàn toàn không bị làm phiền.
```

---

### B. Bảng so sánh toàn diện: Repeater/Hub vs Switch vs Router

| Tiêu chí so sánh | Bộ tập trung (Repeater / Hub) | Thiết bị chuyển mạch (Switch Tầng 2) | Bộ định tuyến (Router Tầng 3) |
| :--- | :--- | :--- | :--- |
| **Tầng hoạt động** | Tầng 1 (Physical) | Tầng 2 (Data Link) | Tầng 3 (Network) |
| **Đơn vị xử lý (PDU)** | Tín hiệu điện / Bit | Khung dữ liệu (**Frame**) | Gói tin (**Datagram**) |
| **Bảng điều khiển** | Không có (phát tán mù) | Bảng **CAM Table** (MAC $\to$ Port) | Bảng **Routing Table** (IP Prefix $\to$ Next-Hop) |
| **Miền va chạm (Collision Domain)**| **Toàn bộ các cổng chung 1 miền va chạm duy nhất** (Càng nhiều máy cắm vào mạng càng chậm do đụng độ). | **Mỗi cổng là một miền va chạm riêng biệt** (Chạy Full-duplex, triệt tiêu hoàn toàn hiện tượng xung đột). | Mỗi cổng là một miền va chạm riêng biệt. |
| **Miền quảng bá (Broadcast Domain)**| Toàn bộ Hub chung 1 miền quảng bá. | **Toàn bộ Switch chung 1 miền quảng bá** (Gói broadcast từ 1 máy sẽ tràn tới mọi máy khác). | **Chia cắt miền quảng bá** (Router chặn đứng hoàn toàn các gói tin Broadcast, không cho lọt qua cổng khác). |

---

### C. Mạng cục bộ ảo (VLAN - Virtual Local Area Network - IEEE 802.1Q)
Trong các doanh nghiệp lớn, việc tất cả các phòng ban (Kế toán, Nhân sự, Lập trình viên, Khách vãng lai) cắm chung vào các switch sẽ gây ra 2 hiểm họa lớn:
1. **Lãng phí băng thông**: Các gói tin Broadcast (ARP, DHCP) chạy tràn lan khắp toàn bộ tòa nhà.
2. **Nguy cơ mất an toàn thông tin**: Máy tính của khách có thể dễ dàng nghe lén dữ liệu nội bộ của phòng Kế toán.

- **VLAN**: Kỹ thuật phân chia một switch vật lý thành nhiều **Switch logic độc lập**. Các máy tính thuộc các VLAN khác nhau hoàn toàn bị cách ly miền quảng bá, không thể nhìn thấy nhau (muốn liên lạc bắt buộc phải đi qua Router Tầng 3 hoặc Layer-3 Switch).
- **Cổng Trunk (Trunk Port)**: Đường liên kết vật lý duy nhất nối giữa các switch với nhau, có khả năng vận chuyển lưu lượng của nhiều VLAN cùng lúc.
- **Tiêu chuẩn IEEE 802.1Q (VLAN Tagging)**: Để switch ở đầu bên kia biết được frame đang truyền thuộc về VLAN nào, switch gửi sẽ chèn thêm một thẻ phụ dài **4 Bytes (802.1Q Tag)** vào ngay sau địa chỉ Source MAC:

```text
CẤU TRÚC ETHERNET FRAME CÓ CHÈN THẺ IEEE 802.1Q VLAN TAG
┌─────────────┬─────────────┬───────────────────┬───────────┬──────────────────────┬───────────┐
│  Dest MAC   │ Source MAC  │    802.1Q Tag     │   Type    │     Data Payload     │  CRC/FCS  │
│  (6 Bytes)  │  (6 Bytes)  │     (4 Bytes)     │ (2 Bytes) │  (46 -> 1500 Bytes)  │ (4 Bytes) │
└─────────────┴─────────────┴─────────┬─────────┴───────────┴──────────────────────┴───────────┘
                                      │
                                      ▼ (Chi tiết 4 Bytes thẻ 802.1Q)
┌─────────────────────────────────────┴─────────┬───────────────┬─────────┬────────────────────┐
│                 TPID (0x8100)                 │   Priority    │   CFI   │   VLAN ID (VID)    │
│                (16 bits / 2B)                 │   (3 bits)    │ (1 bit) │     (12 bits)      │
└───────────────────────────────────────────────┴───────────────┴─────────┴────────────────────┘
```
- **VID (VLAN ID - 12 bits)**: Định danh số hiệu của mạng VLAN (cho phép tạo tối đa $2^{12} = 4096$ mạng VLAN logic trên cùng hạ tầng vật lý).

---

<a id="chuong-7"></a>
# CHƯƠNG 7: MẠNG KHÔNG DÂY VÀ DI ĐỘNG (WIRELESS & MOBILE NETWORKS)
> 📄 **Slide bài giảng:** [Chapter_7_v9.0.pdf](.pdf/Chapter_7_v9.0.pdf)

## 7.1. Đặc thù của Môi trường truyền không dây
1. **Suy giảm tín hiệu (Path Loss / Attenuation)**: Tín hiệu sóng điện từ suy hao theo khoảng cách và vật cản.
2. **Giao thoa đa nguồn (Interference)**: Dải tần số 2.4 GHz dùng chung giữa Wi-Fi, sóng Bluetooth và nhiều thiết bị gia dụng.
3. **Lan truyền đa đường (Multipath Propagation)**: Sóng phản xạ đập vào vật cản tới ăng-ten thu vào các thời điểm lệch nhau.
4. **Vấn đề trạm ẩn (Hidden Terminal Problem)**: Hai máy trạm $A$ và $C$ không nghe thấy nhau nhưng cùng giao tiếp với Access Point $B$, dẫn đến việc phát tín hiệu đồng thời làm xung đột tại $B$.

```text
HIỆN TƯỢNG TRẠM ẨN (HIDDEN TERMINAL PROBLEM)
┌──────────┐                     ┌──────────────────┐                     ┌──────────┐
│  Trạm A  │ ──────────────────> │ Access Point (B) │ <────────────────── │  Trạm C  │
└──────────┘                     └──────────────────┘                     └──────────┘
(Không nghe thấy                                                          (Không nghe thấy
 sóng của C)                                                               sóng của A)
                        Cả A và C cùng lúc phát dữ liệu tới AP B
                        ===> XUNG ĐỘT TÍN HIỆU TẠI AP B
```

---

## 7.2. Giao thức Wi-Fi (IEEE 802.11) & Cơ chế bắt tay RTS / CTS
Để giải quyết bài toán trạm ẩn, chuẩn 802.11 bổ sung cơ chế bắt tay bảo lưu kênh truyền:
1. Trạm gửi một khung tin ngắn **RTS (Request to Send)** báo trước kích thước dữ liệu và thời gian cần chiếm giữ kênh.
2. Access Point nếu đồng ý sẽ phát thanh khung **CTS (Clear to Send)** tới toàn bộ các trạm xung quanh.
3. Tất cả các trạm khác khi nghe thấy CTS sẽ tự động thiết lập bộ đếm **NAV (Network Allocation Vector)** và im lặng nhường đường cho trạm kia truyền dữ liệu.

```text
CẤU TRÚC KHUNG 802.11 FRAME (CHỨA 4 ĐỊA CHỈ MAC)
┌───────────────┬──────────┬────────┬────────┬────────┬──────────┬────────┬──────┬─────┐
│ Frame Control │ Duration │ Addr 1 │ Addr 2 │ Addr 3 │ Seq Ctrl │ Addr 4 │ Data │ CRC │
└───────────────┴──────────┴────────┴────────┴────────┴──────────┴────────┴──────┴─────┘
- Addr 1: MAC của thiết bị nhận không dây trực tiếp (AP hoặc Host)
- Addr 2: MAC của thiết bị phát không dây trực tiếp
- Addr 3: MAC của Router Gateway (nối sang mạng có dây)
- Addr 4: Dùng trong chế độ mạng Ad-hoc (Bridge-to-Bridge)
```

---

## 7.3. Mạng Di động (Cellular Networks: 4G LTE & 5G)
- **Kiến trúc 4G LTE**:
  - `UE (User Equipment)`: Thiết bị di động của người dùng.
  - `eNodeB`: Trạm thu phát sóng vô tuyến di động.
  - `EPC (Evolved Packet Core)`: Mạng lõi chuyển mạch gói gồm **MME** (quản lý di động và báo hiệu), **SGW** (Serving Gateway phục vụ chuyển tiếp dữ liệu), và **PGW** (Packet Gateway kết nối ra Internet).
- **Mạng 5G**:
  - Hỗ trợ ba trụ cột: **eMBB** (băng thông siêu rộng), **URLLC** (độ trễ siêu thấp cỡ mili-giây), và **mMTC** (kết nối hàng triệu thiết bị IoT).
  - Áp dụng kỹ thuật **Network Slicing** để chia sẻ hạ tầng vật lý thành nhiều mạng ảo phục vụ các nhu cầu khác nhau.

---

<a id="chuong-8"></a>
# CHƯƠNG 8: AN TOÀN TRONG MẠNG MÁY TÍNH (NETWORK SECURITY)
> 📄 **Slide bài giảng:** [Chapter_8_v9.0.pdf](.pdf/Chapter_8_v9.0.pdf)

## 8.1. Các mục tiêu an toàn mạng cốt lõi
- **Bảo mật (Confidentiality)**: Chỉ bên gửi và bên nhận hợp lệ mới đọc được nội dung thông điệp (sử dụng mã hóa).
- **Toàn vẹn (Integrity)**: Đảm bảo thông điệp không bị thay đổi hoặc giả mạo trên đường truyền (sử dụng hàm băm và MAC).
- **Xác thực (Authentication)**: Khẳng định chính xác danh tính của đối tác giao tiếp (chứng thực hai chiều).
- **Tính khả dụng (Availability)**: Hệ thống luôn sẵn sàng phục vụ người dùng hợp lệ.

---

## 8.2. Nguyên lý Mật mã học trong truyền thông mạng

```text
HAI PHƯƠNG PHÁP MÃ HÓA CƠ BẢN
1. Mã hóa Đối xứng (Symmetric Encryption):
               ┌───────────────────────┐                  ┌────────────────────────┐
   Bản rõ ───> │ MÃ HÓA (Khóa chung K) │ ───> Bản mã ───> │ GIẢI MÃ (Khóa chung K) │ ───> Bản rõ
               └───────────────────────┘                  └────────────────────────┘

2. Mã hóa Bất đối xứng (Asymmetric Encryption):
               ┌───────────────────────┐                  ┌────────────────────────┐
   Bản rõ ───> │  MÃ HÓA (Public Key)  │ ───> Bản mã ───> │ GIẢI MÃ (Private Key)  │ ───> Bản rõ
               └───────────────────────┘                  └────────────────────────┘
```

| Tiêu chí | Mã hóa Đối xứng (Symmetric) | Mã hóa Bất đối xứng (Asymmetric) |
| :--- | :--- | :--- |
| **Thuật toán tiêu biểu** | **AES (128, 256 bits), ChaCha20** | **RSA, ECC (Elliptic Curve Cryptography)** |
| **Tốc độ xử lý** | Rất nhanh, hỗ trợ xử lý trực tiếp bằng phần cứng CPU. | Chậm hơn hàng trăm lần do các phép tính modulo lớn. |
| **Ứng dụng thực tế** | Mã hóa dòng dữ liệu thực tế sau khi đã kết nối. | Dùng trong bước bắt tay để trao đổi khóa phiên và chữ ký số. |

> [!NOTE]
> **Mô hình Mã hóa Lai (Hybrid Encryption)**:
> Các giao thức mạng hiện đại (HTTPS, SSH) kết hợp cả hai: Sử dụng **Mã hóa Bất đối xứng** trong vài mili-giây đầu để xác thực danh tính và trao đổi một khóa bí mật ngẫu nhiên (**Khóa phiên - Session Key**). Sau đó, toàn bộ dữ liệu trao đổi tiếp theo chuyển sang dùng **Mã hóa Đối xứng (AES)** bằng chính khóa phiên đó để tối ưu hiệu năng.

---

## 8.3. Bảo mật Kênh truyền: TLS và IPsec

### A. Giao thức TLS 1.3 (Transport Layer Security - Tầng Giao vận)
Nằm kẹp giữa Tầng Ứng dụng và TCP, mã hóa toàn bộ dữ liệu trước khi đẩy xuống mạng:
- Rút ngắn thời gian bắt tay xuống còn **1 RTT (Round-Trip Time)** (hoặc 0 RTT khi kết nối lại).
- Bắt buộc dùng cơ chế trao đổi khóa **Ephemeral Diffie-Hellman**, hỗ trợ tính năng **Perfect Forward Secrecy (PFS)**.

### B. Bộ giao thức IPsec (IP Security - Tầng Mạng)
Bảo vệ dòng dữ liệu ở Tầng 3:
- **AH (Authentication Header)**: Cung cấp tính toàn vẹn và xác thực nguồn gốc (không mã hóa).
- **ESP (Encapsulating Security Payload)**: Cung cấp cả tính toàn vẹn và mã hóa payload.
- **Transport Mode** (bảo vệ truyền thông Host-to-Host) vs **Tunnel Mode** (đóng gói toàn bộ gói IP, dùng cho VPN Site-to-Site).

---

## 8.4. Tường lửa (Firewalls) và Hệ thống Giám sát (IDS / IPS)
- **Stateless Packet Filter**: Lọc gói dựa trên quy tắc tĩnh (IP nguồn/đích, Port nguồn/đích, cờ TCP).
- **Stateful Inspection Firewall**: Theo dõi trạng thái của các kết nối TCP để chỉ cho phép các gói tin phản hồi hợp lệ đi vào.
- **Application Gateway (Proxy Tầng 7)**: Đọc sâu vào nội dung thông điệp tầng ứng dụng để kiểm soát dữ liệu.
- **IDS (Intrusion Detection System)**: Lắng nghe bản sao lưu lượng để phát hiện và cảnh báo hành vi bất thường.
- **IPS (Intrusion Prevention System)**: Đặt chắn ngang đường truyền để chủ động ngăn chặn và loại bỏ các gói tin độc hại.

---

<a id="summary"></a>
# 🎯 BẢNG TỔNG KẾT

| Tầng (Layer) | PDU | Giao thức tiêu biểu | Chức năng chính | Header fields quan trọng | Cơ chế / Thuật toán nổi bật |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **5. Application** | **Message** | HTTP/1.1, HTTP/2, HTTP/3, DNS, SMTP, IMAP | Cung cấp dịch vụ mạng cho người dùng, trao đổi thông điệp | Method, Status Code, Host, Cookie, RR Type | Stateless, Multiplexing, Caching, Recursive/Iterative Query |
| **4. Transport** | **Segment** | TCP, UDP | Truyền thông tiến trình - tiến trình (Process-to-Process) | Source/Dest Port, Seq Num, Ack Num, Flags, Window, Checksum | 3-Way Handshake, Flow Control (rwnd), AIMD Congestion Control, RDT |
| **3. Network** | **Datagram** | IPv4, IPv6, ICMP, OSPF, BGP | Định tuyến & chuyển tiếp gói tin (Host-to-Host) | TTL, Protocol, Source/Dest IP, Frag Offset, Hop Limit, AS-PATH | Dijkstra, Bellman-Ford, Subnetting/CIDR, DHCP DORA, NAT, OpenFlow |
| **2. Data Link** | **Frame** | Ethernet (802.3), Wi-Fi (802.11), ARP, VLAN | Truyền khung tin giữa các nút kề nhau (Hop-by-Hop) | Source/Dest MAC, Type, CRC (FCS), VLAN ID (802.1Q) | CSMA/CD, CSMA/CA (RTS/CTS), Self-Learning MAC Table, CRC Modulo-2 |
| **1. Physical** | **Bit** | 1000BASE-T, Cáp quang single-mode, 802.11 RF | Truyền chuỗi bit thô qua môi trường vật lý | Tần số sóng, Mức điện áp, Xung ánh sáng | Điều chế tín hiệu (Modulation), FDM, TDM, Băng thông $R$ |

---
*(Tài liệu dựa theo giáo trình Computer Networking: A Top-Down Approach, 9th Edition kết hợp ghi chú cá nhân)*
