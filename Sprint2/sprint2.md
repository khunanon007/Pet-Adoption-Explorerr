# 🐱 Pet Adoption Explorer — Sprint 2 Report

## Final Term Project — CP352301 Script Programming

Sprint: Sprint 2 — Web UI, API/Database Integration & Interactive Features
Period: 20–24 September 2569
Status: Completed

---

1. Sprint Overview

Sprint 2 เป็นการพัฒนาต่อยอดจาก Sprint 1 โดยเปลี่ยนจากการใช้ Local Sample Dataset ชั่วคราว ให้เป็น Web Application ที่เชื่อมต่อกับระบบฐานข้อมูล SQLite จริง พร้อมปรับปรุงการทำงานของระบบให้สมบูรณ์ยิ่งขึ้น[cite: 3, 4, 8]

ใน Sprint นี้ทีมได้พัฒนาและเชื่อมต่อระบบหลัก ได้แก่

- Web UI ด้วย Streamlit (ปรับปรุง Performance และ State Management)[cite: 3, 10]
- SQLite Database สำหรับจัดเก็บข้อมูลสัตว์เลี้ยง ค่าเลี้ยงดู และผลลัพธ์ Match Quiz[cite: 7, 8]
- Data Processing & Service Layer
- Advanced Dynamic Search และ Category Filter[cite: 2, 5]
- Interactive Pet Comparison Tool[cite: 6]
- Match Quiz Logic & Dynamic Pet Matching[cite: 7]
- Budget Calculator Engine พร้อม Dynamic Cost Calculation[cite: 8]
- Favorites Management System (Session & Local Sync)[cite: 9]
- Automated Testing สำหรับ Core Modules และ Database

ระบบถูกออกแบบให้แยกส่วนการทำงานอย่างชัดเจน:

Web Browser (User UI)
        ↓
Streamlit UI Controller
        ↓
Pet Application Service
        ↓
Data Processing Layer
        ↓
SQLite Database

---

2. Sprint Goal

> พัฒนา Pet Adoption Explorer จาก Prototype ใน Sprint 1 ให้เป็น Web Application ที่สมบูรณ์ สามารถเชื่อมต่อ จัดเก็บ และอ่านข้อมูลจากฐานข้อมูล SQLite ได้จริง พร้อมคำนวณงบประมาณและวิเคราะห์แบบทดสอบอย่างแม่นยำ[cite: 7, 8]

เมื่อจบ Sprint 2 ระบบสามารถ:

- เริ่มต้น Web Application ผ่าน Streamlit และโหลดข้อมูลจาก SQLite ได้[cite: 3, 10]
- แสดงผลและสลับหน้าผ่าน Navigation Bar (Home, Explore, Compare, Match Quiz, Budget Calc, Favorites, Admin)[cite: 1]
- ค้นหาสัตว์เลี้ยงแบบ Real-time รองรับทั้งชื่อและสายพันธุ์ (Case-insensitive & Partial Match)[cite: 5]
- กรองหมวดหมู่สัตว์เลี้ยงตามประเภท (Dogs, Cats, Rabbits, Rodents, Birds)[cite: 2]
- เปรียบเทียบข้อมูลสัตว์เลี้ยง 2–3 ตัวขนานกัน[cite: 6]
- ประมวลผล Match Quiz จากไลฟ์สไตล์ผู้ใช้ 4 ข้อ เพื่อแนะนำสัตว์เลี้ยงที่เหมาะสม[cite: 7]
- คำนวณงบประมาณการเลี้ยงดู (ค่าใช้จ่ายแรกรับ + ค่าเลี้ยงดูรายเดือนตามระยะเวลาที่กำหนด)[cite: 8]
- บันทึกและดึงรายการสัตว์เลี้ยงโปรดในหน้า Favorites[cite: 9]
- ป้องกันและจัดการ Application Crash จาก Database Error หรือ Empty Search State[cite: 5, 9]

---

3. Team Members & Roles

- โดนัท (Role: Planner) - หน้าที่หลัก: Sprint Planning, Scope, Architecture, Documentation และติดตามความคืบหน้า
- ภีม (Role: Coder) - หน้าที่หลัก: Web Application, Streamlit UI, SQLite Database, Service Layer & Core Logic
- ฟีฟ่า (Role: Debugger / QA) - หน้าที่หลัก: Testing, QA, Edge Cases Testing, State Verification & Bug Tracking

---

4. Sprint 2 Scope

In Scope:

Web Application:
- Streamlit Web Dashboard (Multi-page Layout)[cite: 1, 10]
- Top Navigation Bar (Home, Explore, Compare, Match Quiz, Budget Calc, Favorites, Admin)[cite: 1]
- Pet Cards Display & Category Filter[cite: 2, 4]
- Pet Comparison Component[cite: 6]
- Interactive Match Quiz Flow[cite: 7]
- Budget Calculation Engine & Time Slider[cite: 8]
- Favorites State Management[cite: 9]

Database & Logic:
- SQLite Database Integration (Pets Table, Budget Factors Table)
- Database CRUD Operations
- Data Processing & Type Validation
- Quiz Scoring & Recommendation Algorithm[cite: 7]
- Dynamic Budget Calculator Engine[cite: 8]

Testing & Quality:
- Unit Tests สำหรับ Database Operations
- Service Layer Tests
- Edge Case & Input Handling Tests

Out of Scope:
- User Authentication / Multi-user Login
- Real Online Payment System
- External Cloud Storage Integration for Images
- Complex Machine Learning Recommendation Engine

---

5. System Architecture

                ┌────────────────────┐
                │    Web Browser     │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │    Streamlit UI    │
                │  (Pet Dashboard)   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │    Pet Service     │
                └──────┬───────┬─────┘
                       │       │
             ┌─────────┘       └─────────┐
             ▼                           ▼
    ┌─────────────────┐         ┌─────────────────┐
    │ Quiz Engine     │         │ Budget Engine   │
    └────────┬────────┘         └────────┬────────┘
             │                           │
             └───────────┬───────────────┘
                         ▼
                ┌────────────────────┐
                │  Data Processing   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │  SQLite Database   │
                └────────────────────┘

---

## 6. Project Structure

```text
Pet-Adoption-Explorer/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── pet_adoption.db
│
├── docs/
│   ├── CHANGELOG.md
│   ├── LEARNINGLOG.md
│   ├── Plan.md
│   └── Project_Pitch.md
│
├── Sprint1/
│   └── Sprint_1.md
│
├── Sprint2/
│   └── Sprint_2.md
│
├── src/
│   ├── __init__.py
│   ├── app.py
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── header.py
│   │   ├── pet_card.py
│   │   └── styles.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── pet_service.py
│   │   └── quiz_engine.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── data_processing.py
│
└── tests/
    ├── test_database.py
    ├── test_pet_service.py
    ├── test_quiz_engine.py
    └── test_data_processing.py
```

7. Tools & Technologies

- Python: ภาษาหลักในการพัฒนา
- Streamlit: Framework สำหรับสร้าง Web Application UI[cite: 3, 10]
- SQLite: ฐานข้อมูล Relational Database สำหรับเก็บข้อมูลสัตว์เลี้ยง
- Pandas: Data Processing & Transformation
- pytest: Automated Testing
- Git & GitHub: Version Control และ Project Management

---

8. SQLite Database Design

8.1 Pets Table

Field                 | Type    | Description
----------------------|---------|---------------------------------
pet_id                | INTEGER | Primary Key
name                  | TEXT    | ชื่อสัตว์เลี้ยง[cite: 3, 4]
breed                 | TEXT    | สายพันธุ์[cite: 3]
category              | TEXT    | ประเภท (Dog, Cat, Rabbit ฯลฯ)[cite: 2, 3]
location              | TEXT    | สถานที่เลี้ยงอยู่ (เช่น Bangkok)[cite: 3]
age_years             | REAL    | อายุ (ปี)[cite: 3, 4]
suitable_housing     | TEXT    | ที่พักที่เหมาะสม (Condo/House)[cite: 3]
initial_cost          | REAL    | ค่าใช้จ่ายแรกรับ (บาท)[cite: 8]
monthly_cost          | REAL    | ประมาณการค่าเลี้ยงดูต่อเดือน (บาท)[cite: 3, 8]
description           | TEXT    | ข้อความอธิบายลักษณะ/นิสัย[cite: 3]
tags                  | TEXT    | สแนปแท็ก เช่น "ติดส้นเท้า", "ตัวเล็ก"[cite: 4]
image_url             | TEXT    | รูปภาพประกอบ[cite: 3, 4]
is_featured           | INTEGER | สถานะสัตว์เลี้ยงโดดเด่นประจำวัน (0/1)[cite: 3]

---

9. Data Processing & Service Layer

สร้าง: `src/utils/data_processing.py` และ `src/services/pet_service.py`

หน้าที่หลัก:
- Normalize ข้อมูลจาก Database เป็น Dataframe หรือ Dictionary ที่พร้อมใช้งานบน Streamlit
- จัดการ Tag สัตว์เลี้ยง และแปลงค่าว่าง (Missing Values) ให้มีค่า Default
- จัดการ Logic การ Filter ตามหมวดหมู่ (Category)[cite: 2] และการค้นหา (Search)[cite: 5]
- คำนวณยอดเงินรวมในเครื่องคำนวณงบประมาณ:
  Total Cost = Initial Cost + (Monthly Cost × Months)[cite: 8]

---

10. Web Application Pages Detail

- Home Page:
  * Hero Banner ต้อนรับผู้ใช้[cite: 1]
  * เมนูกรองหมวดหมู่ (ALL PETS, DOGS, CATS, RABBITS, RODENTS, BIRDS)[cite: 2]
  * แสดง Pet of the Day (สัตว์เลี้ยงโดดเด่นประจำวัน เช่น โบบา French Bulldog)[cite: 3]
  * แสดงการ์ดรายการสัตว์เลี้ยงหาบ้านใหม่[cite: 4]

- Explore Page:
  * ช่องค้นหาชื่อหรือสายพันธุ์แบบ Real-time[cite: 5]
  * กรองตามสถานที่ และงบประมาณต่อเดือน[cite: 4, 5]

- Compare Page:
  * เลือกสัตว์เลี้ยง 2–3 ตัวมาเปรียบเทียบค่าใช้จ่าย, ลักษณะที่พัก และจุดเด่น[cite: 6]

- Match Quiz Page:
  * แบบทดสอบ 4 ข้อ (ประเภทสัตว์, ที่อยู่อาศัย, เวลาที่มีให้, งบประมาณ)[cite: 7]
  * คำนวณคะแนนแล้วแสดงสัตว์เลี้ยงที่เหมาะสมที่สุด[cite: 7]

- Budget Calc Page:
  * เลือกรอบเวลา (1–36 เดือน) ผ่าน Slider[cite: 8]
  * คำนวณสรุปค่าใช้จ่ายแรกรับ + ค่าเลี้ยงดูสะสมรายเดือน[cite: 8]

- Favorites Page:
  * แสดงรายการสัตว์เลี้ยงที่กด Save ไว้ หากยังไม่มีจะแสดง State เตือนอย่างเป็นมิตร[cite: 9]

---

11. Daily Task Allocation & Update (20–24 Sep 2569)

| วันที่ | Planner — โดนัท | Coder — ภีม | Debugger / QA — ฟีฟ่า | Daily Update |
|---|---|---|---|---|
| **20 ก.ย. 2569** | วาง Architecture, Scope และ Database Schema | ปรับปรุงโครงสร้าง Repository สำหรับ SQLite | กำหนด Test Plan สำหรับ Database & UI State | **เริ่มต้น Sprint 2 และออกแบบ Schema** |
| **21 ก.ย. 2569** | ตรวจสอบ Data Flow ระหว่าง UI และ DB | สร้าง SQLite Database และตัวประมวลผลข้อมูล | ทดสอบการ Insert/Read Data จาก SQLite | **เชื่อมต่อ SQLite เข้ากับ Streamlit สำเร็จ** |
| **22 ก.ย. 2569** | ตรวจสอบ Requirement ของ Quiz & Budget Engine[cite: 7, 8] | พัฒนา Match Quiz Logic และ Budget Calculator Engine[cite: 7, 8] | ทดสอบ Edge Cases ของการคำนวณงบและ Quiz[cite: 7, 8] | **Quiz และ Budget Calculator ทำงานแม่นยำ[cite: 7, 8]** |
| **23 ก.ย. 2569** | ตรวจสอบ Feature Scope และ UI Usability | ปรับปรุง Search, Compare Page และ Session State Favorites[cite: 5, 6, 9] | ทดสอบ Search Empty State และ Navigation Flow[cite: 1, 5] | ** UI/UX และระบบ Favorites มีความเสถียร[cite: 9]** |
| **24 ก.ย. 2569** | ตรวจสอบ DoD และสรุป Sprint 2 Report | Refactor Code และแก้ไขข้อผิดพลาดสุดท้าย | สรุปผลการทดสอบผ่าน pytest Pass 100% | **สรุปผล Sprint 2 และเตรียมส่งมอบงาน** |

---

12. QA Test Cases & Results

Sprint 2 มี Automated Tests และ Manual Verification รวม **12 Cases**:

# | Test Area | Test Case | Expected Result | Status
--|-----------|-----------|-----------------|:-----:
1 | Database | SQLite Initialization & Seeding | สร้าง Tables และโหลดข้อมูลตั้งต้นสำเร็จ | PASS
2 | Database | Read Pets Query | ดึงข้อมูลสัตว์เลี้ยงพร้อม Field ครบถ้วน | PASS
3 | Service | Search Pet ("Boba" / "โบบา")[cite: 3, 5] | ค้นพบข้อมูลถูกต้องแบบ Case-insensitive[cite: 3, 5] | PASS
4 | Service | Category Filtering (Dogs/Cats)[cite: 2] | กรองข้อมูลตรงตามหมวดหมู่ที่เลือก[cite: 2] | PASS
5 | UI Logic | Pet Comparison (2-3 Pets)[cite: 6] | แสดงการ์ดเปรียบเทียบเรียงขนานกันได้[cite: 6] | PASS
6 | Quiz Engine| Match Quiz Calculation[cite: 7] | วิเคราะห์คำตอบ 4 ข้อและแนะนำสัตว์เลี้ยงตรงไลฟ์สไตล์[cite: 7] | PASS
7 | Budget Calc| Total Cost Calculation Slider[cite: 8] | คำนวณ (Initial + Monthly × Month) ถูกต้อง[cite: 8] | PASS
8 | Favorites | Add/Remove Favorite State[cite: 9] | บันทึกและลบข้อมูลจาก Favorites โดย State ไม่หลุด[cite: 9] | PASS
9 | Edge Case | Search Not Found[cite: 5] | แสดง Empty State Warning โดยไม่ Crash[cite: 5] | PASS
10| Edge Case | Missing Image Handle | แสดง Default Cover Image เมื่อไม่มี URL | PASS
11| Performance| Database Query Response | โหลดข้อมูลขึ้น Streamlit ภายใน < 1 วินาที | PASS
12| State     | Navigation Page Switching[cite: 1] | สลับหน้าเมนูโดย Session State ไม่สูญหาย[cite: 1, 9] | PASS

QA Result Summary:
- Total Test Cases: 12
- Passed: 12 (100%)
- Failed: 0
- Critical Bugs: 0

---

13. Contribution Matrix — Member Performance

สมาชิก | Role | งานที่รับผิดชอบ | คะแนน
-------|------|----------------|:-----:
**โดนัท** | Planner | Sprint Planning, System Architecture, Requirements, DoD & Documentation | **50/50**
**ภีม** | Coder | Streamlit UI Development, SQLite DB Integration, Service Layer & Core Engines | **50/50**
**ฟีฟ่า** | Debugger QA | Test Case Design, Edge Cases Handling, Database Testing & QA Verification | **50/50**

Total Team Score = 150/150
Team Completion = 100%

---

14. Definition of Done (DoD) Checklists

- [x] Web Application รันบน Streamlit ได้อย่างราบรื่น[cite: 3, 10]
- [x] เชื่อมต่อกับ SQLite Database และอ่าน/เขียนข้อมูลได้จริง
- [x] หน้า Top Navigation ทั้งหมดทำงานได้ครบถ้วน[cite: 1]
- [x] ระบบกรองหมวดหมู่ ค้นหา เปรียบเทียบ คำนวณงบ และ Match Quiz ทำงานได้ถูกต้อง[cite: 2, 5, 6, 7, 8]
- [x] ระบบจัดการ Favorites ด้วย Session State สมบูรณ์[cite: 9]
- [x] Automated Tests ผ่านทั้งหมด
- [x] จัดทำเอกสาร Sprint 2 Report เรียบร้อย
- [x] โค้ดถูก Commit และ Push ขึ้น GitHub Repository

---

15. Wow! & Whoops!

Wow! (สิ่งที่ทำได้ดี):
1. SQLite Database Integration: สามารถเปลี่ยนจาก Static Sample Data มาเป็นระบบฐานข้อมูลจริงได้อย่างเรียบร้อย
2. Dynamic Budget Engine: ระบบคำนวณงบประมาณปรับเปลี่ยนตาม Slider ได้อย่างลื่นไหลและเข้าใจง่าย[cite: 8]
3. Reliable Session State Handling: แก้ไขปัญหา Session รั่วไหลระหว่างเปลี่ยนหน้า UI ได้ 100%[cite: 9]

Whoops! (ปัญหาและการแก้ไข):
- Problem: ในช่วงแรกของการสลับหน้าเมนู ค่าใน Favorites หลุดหายเนื่องจาก Streamlit Re-run
- Solution: ใช้ `st.session_state` ประกาศเป็น Global State ประจำ Session ทำให้เก็บข้อมูลสัตว์เลี้ยงโปรดไว้ได้ตลอดการใช้งาน[cite: 9]

---

16. Sprint 2 Final Status

===================================================
   PET ADOPTION EXPLORER — SPRINT 2 COMPLETED
===================================================
