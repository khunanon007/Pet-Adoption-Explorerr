# Pet Adoption Explorer

> **Final Term Project**

เว็บแอปพลิเคชันสำหรับสำรวจ ค้นหา และเปรียบเทียบข้อมูลสัตว์เลี้ยงที่ต้องการบ้านใหม่ เพื่อช่วยให้ผู้ใช้งานค้นหาสัตว์เลี้ยงที่เหมาะสมกับความต้องการของตนเองได้ง่ายขึ้น

## 1. Project Overview

### Problem

ข้อมูลสัตว์เลี้ยงที่รอการรับเลี้ยงอาจมีรายละเอียดกระจายอยู่หลายแห่ง ทำให้ผู้ใช้งานค้นหาและเปรียบเทียบสัตว์เลี้ยงได้ไม่สะดวก

### Proposed Solution

**Pet Adoption Explorer** เป็นเว็บแอปพลิเคชันที่ช่วยให้ผู้ใช้งานสำรวจข้อมูลสัตว์เลี้ยง ค้นหาตามเงื่อนไข และดูรายละเอียดประกอบการตัดสินใจรับเลี้ยง

## 2. Project Goals

- พัฒนาเว็บแอปพลิเคชันสำหรับสำรวจสัตว์เลี้ยง
- จัดการและแสดงข้อมูลสัตว์เลี้ยง
- รองรับการค้นหาและกรองข้อมูล
- ช่วยให้ผู้ใช้งานเปรียบเทียบข้อมูลสัตว์เลี้ยง
- ออกแบบโครงสร้างโปรแกรมให้แยกตามหน้าที่
- ทดสอบและปรับปรุงการทำงานของระบบ

## 3. Technology Stack

| Technology | Purpose |
|:--|:--|
| Python | Programming Language |
| Streamlit | Web Application Interface |
| JSON | Sample Data Storage |
| Git | Version Control |
| GitHub | Source Code Repository |

*หมายเหตุ: รายการเทคโนโลยีนี้เป็นตัวอย่างเบื้องต้น ควรตรวจสอบกับโค้ดจริงของโปรเจกต์ก่อนส่งงาน*

## 4. Application Architecture & Flow

```text
User Navigation (Web Browser)
          ↓
Streamlit UI
          ↓
Pet Service (BLL)
          ↓
JSON Storage (DAL)
          ↓
Pet Data Model
          ↓
Process and Display Pet Information
```

## 5. Project Structure

```text
Pet-Adoption-Explorer/
├── src/
│   ├── bll/
│   │   └── pet_service.py
│   ├── dal/
│   │   └── json_storage.py
│   ├── models/
│   │   └── pet.py
│   └── app.py
├── data/
├── tests/
├── README.md
└── requirements.txt
```

## 6. Main Modules

| Module | Responsibility |
|:--|:--|
| `app.py` | Application entry point |
| `pet_service.py` | Business logic for pet operations |
| `json_storage.py` | Reading and storing pet data |
| `pet.py` | Pet data model |

## 7. Sprint 2

### Objective

พัฒนาและจัดระเบียบส่วนประกอบหลักของระบบ Pet Adoption Explorer เพื่อให้สามารถจัดการข้อมูลสัตว์เลี้ยงและนำข้อมูลไปแสดงผลในแอปพลิเคชันได้

### Main Tasks

- Organize project structure
- Implement pet data model
- Implement JSON storage
- Develop pet service
- Integrate application modules
- Test core functionality

## 8. Testing

การทดสอบควรครอบคลุมการอ่านข้อมูลสัตว์เลี้ยง การค้นหา การจัดการข้อมูลที่ไม่ถูกต้อง และการทำงานร่วมกันของแต่ละโมดูล

ผลการทดสอบควรบันทึกตามผลที่เกิดขึ้นจริง

## 9. Code Editor

ใช้ Code Editor สำหรับสร้าง แก้ไข และจัดการไฟล์ Python ของโปรเจกต์ โดยสามารถใช้ Visual Studio Code หรือ GitHub Web Editor ได้

ตัวอย่างไฟล์ที่พัฒนา:

- `src/app.py`
- `src/bll/pet_service.py`
- `src/dal/json_storage.py`
- `src/models/pet.py`

## 10. Project Status

สถานะของแต่ละ Sprint ควรอัปเดตตามความคืบหน้าจริงของทีม

| Sprint | Status |
|:--|:--|
| Sprint 1 | Update based on actual progress |
| Sprint 2 | Update based on actual progress |
| Sprint 3 | Update based on actual progress |
| Final Sprint | Update based on actual progress |

---

**Pet Adoption Explorer — Helping People Discover Pets for Adoption**
