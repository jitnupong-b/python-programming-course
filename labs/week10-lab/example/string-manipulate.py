# Python String Examples Based on Course Slides
# Complete working examples with explanations

# ===========================
# 1. STRING CREATION AND BASIC OPERATIONS
# ===========================

print("=== STRING CREATION ===")
# Different ways to create strings
name = "India"
graduate = 'B.E.'
multiline = """This is a
multiline string
example"""

print(f"name = {name}")
print(f"graduate = {graduate}")
print(f"multiline = {multiline}")

# ===========================
# 2. READING AND CONVERTING
# ===========================

print("\n=== READING AND CONVERTING ===")
# Note: Using input() instead of raw_input() for Python 3
name = input("Enter your name: ")
print(f"Hello {name}")

# Converting string to number
apple = input("Enter a number: ")
try:
    x = int(apple) - 10
    print(f"Result: {x}")
except ValueError:
    print("Please enter a valid number!")

# ===========================
# 3. STRING INDEXING
# ===========================

print("\n=== STRING INDEXING ===")
fruit = 'banana'
print(f"fruit = {fruit}")
print(f"fruit[1] = {fruit[1]}")  # 'a'

n = 3
w = fruit[n - 1]  # fruit[2]
print(f"n = {n}")
print(f"w = fruit[n-1] = {w}")  # 'n'

# Show indexing diagram
print("\nIndexing visualization:")
print("b a n a n a")
print("0 1 2 3 4 5")
print("-6-5-4-3-2-1")

# ===========================
# 4. TRAVERSING STRINGS
# ===========================

print("\n=== TRAVERSING STRINGS ===")
message = "hello"
index = 0

print("Method 1: Using for loop with enumerate")
for i, char in enumerate(message):
    print(f"message[{i}] = {char}")

print("\nMethod 2: Manual indexing")
index = 0
for char in message:
    print(f"message[{index}] = {char}")
    index += 1

# ===========================
# 5. CONCATENATION AND MULTIPLICATION
# ===========================

print("\n=== CONCATENATION AND MULTIPLICATION ===")
str1 = 'Hello'
str2 = 'World!'

# Concatenation
result = str1 + str2
print(f"str1 + str2 = {result}")

# Multiplication
repeat = str1 * 3
print(f"str1 * 3 = {repeat}")

# ===========================
# 6. APPENDING STRINGS
# ===========================

print("\n=== APPENDING STRINGS ===")
greeting = 'hello'
name = input("Enter your name: ")
greeting += name
greeting += ". welcome to pune"
print(greeting)

# ===========================
# 7. ITERATING AND COUNTING
# ===========================

print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = 'Hello World'
for letter in text:
    if letter == 'l':
        count += 1
print(f"{count} letters 'l' found in '{text}'")

# ===========================
# 8. MEMBERSHIP TEST
# ===========================

print("\n=== MEMBERSHIP TEST ===")
print("'a' in 'program':", 'a' in 'program')  # True
print("'at' not in 'battle':", 'at' not in 'battle')  # False

# ===========================
# 9. STRING IMMUTABILITY 
# ===========================

print("\n=== STRING IMMUTABILITY ===")
str1 = "Hello"
print(f"str1 is {str1}")
print(f"id of str1 is {id(str1)}")

str2 = "world"
print(f"str2 is {str2}")
print(f"id of str2 is {id(str2)}")

str1 += str2
print(f"str1 after modification: {str1}")
print(f"id of str1 is {id(str1)}")  # Different ID - new object created

str3 = str1
print(f"str3 is {str3}")
print(f"id of str3 is {id(str3)}")  # Same ID as current str1

# ===========================
# 10. ESCAPE CHARACTERS
# ===========================

print("\n=== ESCAPE CHARACTERS ===")
print("New line example:")
print("Line 1\nLine 2")

print("Tab example:")
print("Column1\tColumn2\tColumn3")

print("Backslash example:")
print("Path: C:\\Users\\Python")

print("Quote examples:")
print('He said, "What\'s there?"')
print("He said, \"What's there?\"")
print('''He said, "What's there?"''')

# Raw strings
print("\nRaw string example:")
print("Normal: This is \\x61 \\ngood example")
print(r"Raw: This is \x61 \ngood example")

# ===========================
# 11. STRING FORMATTING
# ===========================

print("\n=== STRING FORMATTING ===")

# % formatting
name = "ashish"
age = 8
print("Using %% formatting:")
print("name=%s and age=%d" % (name, age))
print("name=%s and age=%d" % ("ankita", 6))

# .format() method
print("\nUsing .format() method:")
id_num = 10
name = 'shankar'
sal = 20000

# Different format styles
str1 = '{},{},{}'.format(id_num, name, sal)
print(str1)  # 10,shankar,20000

str2 = '{} - {} - {}'.format(id_num, name, sal)
print(str2)  # 10 - shankar - 20000

str3 = 'id={}\nname={}\nsal={}'.format(id_num, name, sal)
print(str3)

# ===========================
# 12. STRING METHODS EXAMPLES
# ===========================

print("\n=== STRING METHODS ===")
text = "welcome to the world of python"

# Case methods
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
print(f"Capitalize: {text.capitalize()}")

# Search methods
print(f"Find 'world': {text.find('world')}")
print(f"Count 'o': {text.count('o')}")
print(f"Starts with 'welcome': {text.startswith('welcome')}")
print(f"Ends with 'python': {text.endswith('python')}")

# Modification methods
print(f"Replace 'python' with 'java': {text.replace('python', 'java')}")
words = text.split()
print(f"Split into words: {words}")
print(f"Join with '-': {'-'.join(words)}")

# Validation methods
test_str = "Hello123"
print(f"\nValidation methods for '{test_str}':")
print(f"isalnum(): {test_str.isalnum()}")
print(f"isalpha(): {test_str.isalpha()}")
print(f"isdigit(): {test_str.isdigit()}")
print(f"isupper(): {test_str.isupper()}")
print(f"islower(): {test_str.islower()}")

# ===========================
# 13. ORD() AND CHR() FUNCTIONS
# ===========================

print("\n=== ORD() AND CHR() FUNCTIONS ===")
ch = 'R'
print(f"ord('{ch}') = {ord(ch)}")
print(f"chr(82) = {chr(82)}")

# ASCII table example
print("\nASCII values for A-Z:")
for i in range(65, 71):  # A-F
    print(f"chr({i}) = {chr(i)}")

# ===========================
# 14. STRING COMPARISON
# ===========================

print("\n=== STRING COMPARISON ===")
print("ASCII: A-Z = 65-90, a-z = 97-122")

comparisons = [
    ("'AbC' == 'AbC'", 'AbC' == 'AbC'),
    ("'abC' != 'Abc'", 'abC' != 'Abc'),
    ("'abc' > 'Abc'", 'abc' > 'Abc'),
    ("'abC' < 'abc'", 'abC' < 'abc'),
    ("'TED' == 'ted'", 'TED' == 'ted'),
    ("'tend' <= 'tent'", 'tend' <= 'tent'),
    ("'main' <= 'main'", 'main' <= 'main')
]

for comparison, result in comparisons:
    print(f"{comparison}: {result}")

# ===========================
# 15. STRING SLICING
# ===========================

print("\n=== STRING SLICING ===")
text = "python"
print(f"Original string: {text}")

# Basic slicing
print(f"text[1:5] = {text[1:5]}")  # ytho
print(f"text[:6] = {text[:6]}")    # python
print(f"text[:] = {text[:]}")      # python
print(f"text[1:20] = {text[1:20]}")# ython

# Negative indexing
print(f"text[-1] = {text[-1]}")    # n
print(f"text[-6] = {text[-6]}")    # p
print(f"text[-2:] = {text[-2:]}")  # on
print(f"text[:-2] = {text[:-2]}")  # pyth
print(f"text[-5:-2] = {text[-5:-2]}")  # yth

# Stride examples
long_text = "welcome to the world of python"
print(f"\nSlicing with stride:")
print(f"Original: {long_text}")
print(f"text[2:10] = {long_text[2:10]}")      # lcome to
print(f"text[2:10:2] = {long_text[2:10:2]}")  # loet
print(f"text[2:13:4] = {long_text[2:13:4]}")  # le

# Reverse string
print(f"text[::-1] = {long_text[::-1]}")      # Reverse
print(f"text[::-3] = {long_text[::-3]}")      # Every 3rd char in reverse

# ===========================
# 16. STRING MODULE
# ===========================

print("\n=== STRING MODULE ===")
import string

# String constants
print("String module constants:")
print(f"ascii_letters: {string.ascii_letters}")
print(f"digits: {string.digits}")
print(f"punctuation: {string.punctuation}")
print(f"ascii_lowercase: {string.ascii_lowercase}")
print(f"ascii_uppercase: {string.ascii_uppercase}")

# Working with constants
print(f"'g' in string.ascii_lowercase: {'g' in string.ascii_lowercase}")
print(f"'5' in string.digits: {'5' in string.digits}")

# ===========================
# 17. PROGRAMMING EXAMPLES
# ===========================

print("\n=== PROGRAMMING EXAMPLES ===")

# Example 1: Alphabet triangle pattern
print("1. Alphabet Triangle Pattern:")
for i in range(1, 7):
    for j in range(i):
        print(chr(65 + j), end='')
    print()

# Example 2: Name and PAN validation
print("\n2. Name and PAN Validation:")
def validate_pan_name():
    name = input("Enter your name: ")
    pan = input("Enter PAN number: ")
    
    # Validate name (only alphabets and spaces)
    if name.replace(' ', '').isalpha():
        print(f"Name '{name}' is valid")
    else:
        print(f"Name '{name}' is invalid")
    
    # Basic PAN validation (5 letters + 4 digits + 1 letter)
    if (len(pan) == 10 and 
        pan[:5].isalpha() and 
        pan[5:9].isdigit() and 
        pan[9].isalpha()):
        print(f"PAN '{pan}' format is valid")
    else:
        print(f"PAN '{pan}' format is invalid")

# Uncomment to test interactively:
# validate_pan_name()

# Example 3: Message encryption with key
print("\n3. Message Encryption:")
def encrypt_message(message, key):
    encrypted = ""
    for char in message:
        if char.isalpha():
            # Shift character by key value
            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                encrypted += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            encrypted += char
    return encrypted

# Test encryption
original = "Hello World"
key = 3
encrypted = encrypt_message(original, key)
print(f"Original: {original}")
print(f"Encrypted (key={key}): {encrypted}")

# Example 4: String reversal
print("\n4. String Reversal Methods:")
text = "programming"
print(f"Original: {text}")
print(f"Method 1 (slicing): {text[::-1]}")

# Method 2: Using loop
reversed_str = ""
for char in text:
    reversed_str = char + reversed_str
print(f"Method 2 (loop): {reversed_str}")

# Method 3: Using join and reversed
print(f"Method 3 (join): {''.join(reversed(text))}")

print("\n=== ALL EXAMPLES COMPLETED ===")


"""
### 1) ข้อ 1: สวัสดีคนที่กรอกชื่อ
เขียนโปรแกรมที่:
- รับชื่อจากผู้ใช้
- แสดงผลเป็นข้อความว่า “สวัสดี, <ชื่อ>!”
- จากนั้นแสดงชื่อด้วยตัวพิมพ์ใหญ่ทั้งหมด

ตัวอย่าง:
- Input: `pim`
- Output:
  - สวัสดี, pim!
  - PIM

คำแนะนำ:
- ใช้ `input()`
- ใช้ `.upper()`

---

### 2) ข้อ 2: นับจำนวนตัวอักษร 'a' ในคำ
เขียนโปรแกรมที่:
- รับข้อความจากผู้ใช้
- นับจำนวนตัวอักษร `'a'` ในข้อความ
- แสดงผลจำนวนที่นับได้

ตัวอย่าง:
- Input: `banana`
- Output: `มีตัวอักษร a ทั้งหมด 3 ตัว`

คำแนะนำ:
- ใช้ loop `for`
- ใช้ `if letter == 'a'`

---

### 3) ข้อ 3: แยกคำและแปลงเป็นข้อความใหม่
เขียนโปรแกรมที่:
- รับประโยคจากผู้ใช้
- แยกประโยคออกเป็นคำ ๆ
- ต่อคำด้วยเครื่องหมาย `-`
- แสดงผลข้อความที่ถูกจัดรูปแบบใหม่

ตัวอย่าง:
- Input: `python is easy`
- Output: `python-is-easy`

คำแนะนำ:
- ใช้ `split()`
- ใช้ `'-'.join()`

---

### 4) ข้อ 4: ตรวจสอบรหัสผ่านแบบง่าย
เขียนโปรแกรมที่:
- รับข้อความจากผู้ใช้
- ตรวจว่าเป็นตัวเลขทั้งหมดหรือไม่
- ถ้าเป็นตัวเลขทั้งหมด ให้แสดง “Valid number”
- ถ้าไม่ใช่ ให้แสดง “Please enter a valid number!”

ตัวอย่าง:
- Input: `12345`
- Output: `Valid number`

- Input: `abc123`
- Output: `Please enter a valid number!`

คำแนะนำ:
- ใช้ `isdigit()`
- ใช้ `try/except` ถ้าต้องแปลงเป็น int

---

### 5) ข้อ 5: เขียนโปรแกรมจัดรูปแบบข้อมูลคน
เขียนโปรแกรมที่:
- รับชื่อ-นามสกุลจากผู้ใช้
- แยกชื่อและนามสกุลออกจากกัน
- แสดงผลเป็น:
  - ชื่อเต็ม
  - นามสกุล
  - ชื่อย่อ (ตัวแรกของชื่อและนามสกุล)
  - จำนวนคำทั้งหมดในชื่อเต็ม

ตัวอย่าง:
- Input: `pim chai`
- Output:
  - ชื่อเต็ม: pim chai
  - ชื่อ: pim
  - นามสกุล: chai
  - ชื่อย่อ: p.c.
  - จำนวนคำ: 2

คำแนะนำ:
- ใช้ `split()`
- ใช้ index ของ list
- ใช้ slicing เช่น `name[0]`

---
"""
