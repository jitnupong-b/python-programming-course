#ValueError Exception
try:
    age = int(input("กรอกอายุ: "))
    print(f"ปีหน้าคุณจะอายุ {age + 1} ปี")
except ValueError:
    print("กรุณากรอกอายุเป็นตัวเลขจำนวนเต็ม เช่น 20")


#ZeroDivisionException
try:
    numerator = float(input("กรอกตัวตั้ง: "))
    denominator = float(input("กรอกตัวหาร: "))

    result = numerator / denominator
    print(f"ผลลัพธ์ = {result}")

except ValueError:
    print("กรุณากรอกตัวเลขให้ถูกต้อง")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")
    

#FileNotFoundException, PermissionException
try:
    filename = input("ชื่อไฟล์: ")

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    print("เนื้อหาในไฟล์")
    print(content)

except FileNotFoundError:
    print(f"ไม่พบไฟล์ชื่อ {filename}")

except PermissionError:
    print("ไม่มีสิทธิ์เข้าถึงไฟล์นี้")
    

# raise ใช้สำหรับ สั่งให้ Python สร้าง exception ขึ้นเอง เมื่อข้อมูลหรือสถานการณ์ไม่เป็นไปตามกติกาที่โปรแกรมกำหนด
# แม้คำสั่งนั้นจะไม่ผิดไวยากรณ์และ Python ยังทำงานต่อได้ตามปกติก็ตาม

try:
    score = float(input("กรอกคะแนน 0-100: "))

    if not 0 <= score <= 100:
        raise ValueError("คะแนนต้องอยู่ระหว่าง 0 ถึง 100")

except ValueError as error:
    print(f"ข้อมูลไม่ถูกต้อง: {error}")

else:
    print(f"บันทึกคะแนน {score} เรียบร้อย")

finally:
    print("จบการตรวจสอบคะแนน")


