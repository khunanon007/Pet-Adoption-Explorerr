# 🐱 Pet Adoption Explorer — Sprint 3 Report

## Final Term Project — CP352301 Script Programming

Sprint: Sprint 3 — Data Analysis, Visualization & Advanced Features  
Period: 25–29 September 2026  
Duration: 5 Days  
Status: Completed  

Repository: https://github.com/Phanuwatphk/Pet-Adoption-Explorer  

---

1. Sprint Overview

Sprint 3 เป็นการพัฒนาต่อยอดจาก Sprint 2 ซึ่งทีมได้พัฒนา Web Application ด้วย Streamlit พร้อมเชื่อมต่อฐานข้อมูล SQLite จริงเรียบร้อยแล้ว[cite: 3, 8]

เป้าหมายหลักของ Sprint 3 คือการนำข้อมูลสัตว์เลี้ยงที่มีอยู่ในระบบมาจัดเตรียม วิเคราะห์ และนำเสนอในรูปแบบ Statistics และ Data Visualization (เช่น สถิติจำนวนสัตว์เลี้ยงตามหมวดหมู่[cite: 2], ช่วงงบประมาณค่าเลี้ยงดู[cite: 8], และอัตราความเหมาะสมจาก Match Quiz[cite: 7]) รวมถึงเพิ่มความสามารถในการ Filter, Sort และเปรียบเทียบข้อมูลสัตว์เลี้ยงให้ละเอียดยิ่งขึ้น[cite: 5, 6]

ใน Sprint นี้มีการเพิ่ม Analysis Layer เข้ามาในระบบ โดยแยกส่วนการคำนวณและวิเคราะห์ข้อมูลออกจาก UI เพื่อให้สามารถนำข้อมูลจาก Pet Service มาวิเคราะห์ด้วย Pandas และนำผลลัพธ์ไปแสดงบน Statistics Page ของ Streamlit Dashboard

งานที่พัฒนาใน Sprint 3 ประกอบด้วย:
- Data Processing และ Data Normalization ข้อมูลสัตว์เลี้ยง
- Data Preparation สำหรับการวิเคราะห์
- Exploratory Data Analysis (EDA) ข้อมูลสัตว์เลี้ยง
- Descriptive Statistics (ค่าเฉลี่ยค่าเลี้ยงดู[cite: 3, 8], ค่าเฉลี่ยอายุ[cite: 3, 4])
- Frequency และ Proportion Analysis ของหมวดหมู่ (Dogs, Cats ฯลฯ)[cite: 2] และประเภทที่พัก (Condo/House)[cite: 3]
- Statistics Dashboard & Data Visualization
- Advanced Pet Comparison (เปรียบเทียบข้อมูลสัตว์เลี้ยงเชิงลึก)[cite: 6]
- Advanced Multi-condition Filtering & Sorting[cite: 5]
- Unit Testing และ Integration Testing
- Empty State และ Missing Data Handling[cite: 5, 9]

---

2. Sprint Goal

> พัฒนา Pet Adoption Explorer ให้สามารถนำข้อมูลสัตว์เลี้ยงจากระบบมาวิเคราะห์และนำเสนอในรูปแบบ Statistics และ Data Visualization พร้อมเพิ่มความสามารถในการสำรวจ เปรียบเทียบ และกรองข้อมูลได้อย่างแม่นยำและสะดวกขึ้น[cite: 5, 6, 8]

เมื่อจบ Sprint 3 ระบบสามารถ:
- เตรียมและ Normalize ข้อมูลสัตว์เลี้ยงจาก SQLite
- แปลงข้อมูลให้อยู่ในรูปแบบที่เหมาะสมต่อการวิเคราะห์ด้วย Pandas
- คำนวณ Descriptive Statistics ของประมาณการค่าเลี้ยงดูต่อเดือนและอายุ[cite: 3, 8]
- วิเคราะห์ Frequency และ Proportion ของหมวดหมู่สัตว์เลี้ยงและลักษณะที่พักที่เหมาะ[cite: 2, 3]
- วิเคราะห์ช่วงงบประมาณแรกรับ (Initial Cost) และค่าเลี้ยงดูรายเดือน (Monthly Cost)[cite: 8]
- แสดง Statistics และ Visualization บน Dashboard (เช่น Distribution Chart)
- เปรียบเทียบข้อมูลเชิงลึกของสัตว์เลี้ยง 2-3 ตัว[cite: 6]
- Filter สัตว์เลี้ยงด้วยหลายเงื่อนไขพร้อมกัน (หมวดหมู่[cite: 2], สถานที่[cite: 3], ที่พัก[cite: 3], งบประมาณ[cite: 8])
- Sort สัตว์เลี้ยงตามค่าเลี้ยงดู, อายุ, และชื่อ[cite: 3, 4, 8]
- จัดการ Missing Values และ Empty Dataset ได้อย่างปลอดภัย[cite: 5, 9]

---

3. Team Members & Roles

| สมาชิก | Role | หน้าที่หลัก |
|---|---|---|
| **ภีม** | Planner | กำหนด Sprint Goal, Scope, Requirements, Definition of Done, แบ่งงาน และจัดทำ Documentation |
| **ฟีฟ่า** | Coder | พัฒนา Data Processing, Analysis, Statistics, Visualization และ Advanced Features |
| **โดนัท** | Debugger | ออกแบบและดำเนินการทดสอบ ตรวจสอบผลลัพธ์ วิเคราะห์ปัญหา และยืนยันการแก้ไข Bug |

---

4. Sprint 3 Scope

4.1 Data Processing & Data Preparation:
- Normalize ข้อมูลสัตว์เลี้ยงจาก SQLite
- แปลง Pet ID เป็น Integer, Age เป็น Float, Monthly/Initial Cost เป็น Float[cite: 3, 8]
- แยกแยะและกรอง Tags/Attributes ของสัตว์เลี้ยง[cite: 4]
- เก็บ Optional Fields ที่ไม่มีข้อมูลเป็น None โดยไม่สร้างข้อมูลเท็จ
- แปลงข้อมูล Numeric ใน Analysis Layer ด้วย Pandas

4.2 Exploratory Data Analysis (EDA):
- Monthly Cost: Count, Mean, Median, Min, Max, Standard Deviation[cite: 8]
- Category: Frequency, Proportion, Average Monthly Cost by Category[cite: 2, 8]
- Suitable Housing: Proportion ของ Condo vs House[cite: 3]
- Age Distribution: Distribution ของอายุสัตว์เลี้ยงหาบ้านใหม่[cite: 3, 4]

4.3 Statistical Analysis:
- ใช้ Descriptive Statistics เป็นหลักในการสรุปภาพรวมงบประมาณค่าเลี้ยงดู[cite: 8]
- คำนวณความถี่และสัดส่วนของประเภทสัตว์เลี้ยงที่กำลังตามหาบ้าน[cite: 2, 4]

---

5. Analysis Layer Architecture

โครงสร้างหลัก:
Pet-Adoption-Explorer/
├── src/
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── statistics.py
│   ├── components/
│   │   ├── dashboard.py
│   │   └── statistics_page.py
│   ├── services/
│   │   └── pet_service.py
│   └── utils/
│       └── data_processing.py

การทำงาน:
Pet Data (SQLite) -> Pet Service -> Analysis Layer (Pandas/Statistics) -> Visualization (Altair) -> Streamlit UI

---

6. System Architecture & Data Flow

SQLite Database
        ↓
Pet Service
        ↓
Pandas DataFrame (Analysis Layer)
        ↓
Statistics & Distribution Calculations
        ↓
Altair Visualization Components
        ↓
Streamlit Dashboard Page

---

7. Project Structure

Pet-Adoption-Explorer/
│
├── README.md
├── requirements.txt
├── .gitignore
├── pytest.ini
│
├── data/
│   └── pet_adoption.db
│
├── docs/
│   ├── Project_Pitch.md
│   ├── Plan.md
│   ├── CHANGELOG.md
│   └── LEARNINGLOG.md
│
├── src/
│   ├── __init__.py
│   ├── app.py
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── statistics.py
│   │
│   ├── components/
│   │   ├── dashboard.py
│   │   ├── statistics_page.py
│   │   └── styles.py
│   │
│   ├── database/
│   │   └── database.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── pet_service.py
│   │   └── quiz_engine.py
│   │
│   └── utils/
│       └── data_processing.py
│
├── tests/
│   ├── test_database.py
│   ├── test_pet_service.py
│   ├── test_quiz_engine.py
│   ├── test_statistics.py
│   └── test_data_processing.py
│
├── Sprint1/
│   └── Sprint_1.md
├── Sprint2/
│   └── Sprint_2.md
└── Sprint3/
    └── Sprint_3.md

---

8. Tools & Technologies

- Python: ภาษาหลักในการพัฒนา
- Streamlit: Web Application Framework[cite: 3, 10]
- Pandas: DataFrame, Data Analysis & Processing
- SQLite: Relational Database
- Altair: Data Visualization Framework
- pytest: Automated Testing Framework
- Git & GitHub: Version Control

---

9. Dashboard Statistics & Visualization

Statistics Page แสดง Summary Metrics และ Visualizations 5 ส่วนหลัก:
1. Category Distribution: แสดงสัดส่วนสัตว์เลี้ยงตามหมวดหมู่ (Bar Chart)[cite: 2]
2. Monthly Cost Analysis by Category: แสดงค่าเฉลี่ยค่าใช้จ่ายรายเดือนแยกตามประเภท (Bar Chart)[cite: 2, 8]
3. Suitable Housing Proportion: สัดส่วนความเหมาะสมของที่อยู่อาศัย (Pie/Donut Chart)[cite: 3]
4. Age Distribution: การกระจายตัวของอายุสัตว์เลี้ยง (Binned Bar Chart)[cite: 3, 4]
5. Initial vs Monthly Cost Comparison: เปรียบเทียบค่าใช้จ่ายแรกรับกับค่าใช้จ่ายรายเดือน (Scatter Plot)[cite: 8]

---

10. Advanced Features

10.1 Advanced Filtering:
- กรองหลายเงื่อนไขพร้อมกัน: หมวดหมู่ (Category)[cite: 2] + สถานที่ (Location)[cite: 3] + ที่พัก (Housing)[cite: 3] + งบประมาณสูงสุดต่อเดือน (Max Monthly Cost)[cite: 8]

10.2 Advanced Sorting:
- เรียงลำดับตาม: ค่าเลี้ยงดูต่อเดือน (น้อยไปมาก/มากไปน้อย)[cite: 8], อายุ[cite: 3, 4], ชื่อ[cite: 3, 4]

10.3 Advanced Pet Comparison:
- เลือกสัตว์เลี้ยง 2-3 ตัวเปรียบเทียบตารางค่าใช้จ่าย (Initial & Monthly Cost)[cite: 6, 8], เงื่อนไขการเลี้ยงดู และนิสัยขนานกัน[cite: 3, 6]

---

11. Daily Task Allocation & Actual Result (25–29 Sep 2026)

| วันที่ | Planner — ภีม | Coder — ฟีฟ่า | Debugger — โดนัท ผลการดำเนินงาน |
|---|---|---|---|---|
| **25 ก.ย. 2569** | กำหนด Goal, Scope และ Requirements | ตรวจสอบ Data Flow และเตรียม Analysis Architecture | ออกแบบ Test Cases สำหรับ Statistics & Visualizations | **Planning & Preparation** ✅ |
| **26 ก.ย. 2569** | ติดตามงาน Data Processing & Analysis | พัฒนา Analysis Layer (`statistics.py`) และ Data Normalization | ทดสอบ Data Processing, Pandas Functions และ Edge Cases | **Data Processing & Analysis** ✅ |
| **27 ก.ย. 2569** | ตรวจสอบ Requirements หน้า Statistics Page | พัฒนา Statistics Page และ Render Altair Charts | ทดสอบการแสดงผล Metrics และ Charts บน UI | **Statistics & Visualization** ✅ |
| **28 ก.ย. 2569** | ติดตาม Advanced Filters & Comparison | พัฒนา Multi-condition Filtering, Sorting และ Comparison Table[cite: 5, 6] | ทดสอบ Filter Combination, Sorting และ State Persistence[cite: 5, 9] | **Advanced Features Completed** ✅ |
| **29 ก.ย. 2569** | ตรวจสอบ DoD และจัดทำ Final Report | Refactor Code และปรับแต่ง UI Performance | ทำ Final Integration QA และรัน pytest Pass 100% | **Final QA & Report Completed** ✅ |

---

12. QA Test Cases & Results

| Test ID | Test Case | Expected Result | Result |
|---|---|---|:---:|
| S3-TC-01 | Data Processing Normalization | แปลงข้อมูลจาก SQLite ลง Pandas DataFrame ได้ถูกต้อง | PASS |
| S3-TC-02 | Missing Values Handling | สัตว์เลี้ยงที่ไม่มีรูปหรือ Tag ไม่ทำให้แอป Crash | PASS |
| S3-TC-03 | Descriptive Statistics Calc | คำนวณค่าเฉลี่ย, Median, Min, Max ของค่าเลี้ยงดูถูกต้อง[cite: 8] | PASS |
| S3-TC-04 | Category Frequency & Proportion | นับจำนวนและสัดส่วนประเภทสัตว์เลี้ยงตรงกับ DB[cite: 2] | PASS |
| S3-TC-05 | Multi-condition Filter Test | กรอง Category + Location + Housing ได้ผลลัพธ์ตรงเป้า[cite: 2, 3, 5] | PASS |
| S3-TC-06 | Advanced Sorting Test | เรียงลำดับตาม Monthly Cost จากน้อยไปมากถูกต้อง[cite: 8] | PASS |
| S3-TC-07 | Pet Comparison Table Render | แสดงตารางเปรียบเทียบค่าใช้จ่าย 2-3 ตัวได้ถูกต้อง[cite: 6, 8] | PASS |
| S3-TC-08 | Empty Dataset Handling | เมื่อไม่พบสัตว์เลี้ยง ระบบแสดง Informative State โดยไม่ Crash[cite: 5] | PASS |
| S3-TC-09 | Statistics Page Rendering | Render Visualizations และ Metrics ได้สมบูรณ์ | PASS |
| S3-TC-10 | Integration Test | UI, Service, Analysis Layer ทำงานร่วมกันได้ราบรื่น | PASS |

QA Summary:
- Total Test Cases: 10
- Passed: 10 (100%)
- Failed: 0

---

13. Contribution Matrix — Member Performance

| สมาชิก | Role | งานที่รับผิดชอบ | คะแนน |
|---|---|---|:---:|
| **ภีม** | Planner | Sprint Planning, Requirements, Scope, DoD & Documentation | **50/50** |
| **ฟีฟ่า** | Coder | Analysis Layer, Statistics Page, Altair Charts & Advanced Filters | **50/50** |
| **โดนัท** | Debugger | Test Case Design, QA Testing, Edge Case Handling & Bug Verification | **50/50** |

Total Team Score = 150/150
Team Completion = 100%

---

14. Definition of Done (DoD) Checklists

- [x] มีการสร้าง Analysis Layer (`statistics.py`) แยกส่วนคำนวณออกจาก UI
- [x] แสดงหน้า Statistics พร้อม Summary Metrics และ Visualizations
- [x] ระบบ Filter หลายเงื่อนไข และ Sorting ทำงานได้ถูกต้อง[cite: 5]
- [x] ระบบ Compare เปรียบเทียบข้อมูลสัตว์เลี้ยงเชิงลึกทำงานได้เรียบร้อย[cite: 6]
- [x] ผ่าน QA Test Cases ทั้งหมด (10/10 Pass)
- [x] ซอร์สโค้ดและเอกสาร Sprint 3 Report อัปเดตขึ้น GitHub Repository เรียบร้อย

---

15. Wow! & Whoops!

Wow! (สิ่งที่ทำได้ดี):
1. Clean Analysis Architecture: แยกส่วนการวิเคราะห์ข้อมูลด้วย Pandas ออกจาก UI ทำให้โค้ดสะอาด อ่านง่าย และเขียน Unit Test ได้สะดวก
2. Meaningful Data Insights: ไม่ใช่แค่แสดงรายการสัตว์เลี้ยง แต่ยังช่วยวิเคราะห์ภาพรวมงบประมาณค่าเลี้ยงดู ทำให้ผู้รับเลี้ยงวางแผนการเงินได้จริง[cite: 8]

Whoops! (ปัญหาและการแก้ไข):
- Problem: สัตว์เลี้ยงบางตัวไม่มีการระบุค่าใช้จ่ายแรกรับ (Initial Cost) ทำให้ Pandas คำนวณ Mean เกิด NaN
- Solution: ใช้ Numeric Coercion และกรองเฉพาะ Record ที่มีค่าตัวเลขมาคำนวณ พร้อมแสดง N/A State บน UI สำหรับข้อมูลที่ไม่สมบูรณ์

---

16. Sprint 3 Final Status

===================================================
   PET ADOPTION EXPLORER — SPRINT 3 COMPLETED
===================================================
