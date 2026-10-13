# 📋 Pet Adoption Explorer — Project Plan

## Final Term Project — CP352301 Script Programming

---

# 1. Project Plan Overview

**Pet Adoption Explorer** เป็น Web Application สำหรับศูนย์รวมข้อมูลสัตว์เลี้ยงตามหาบ้านใหม่ ช่วยจัดการ วิเคราะห์งบประมาณการเลี้ยงดู และจับคู่สัตว์เลี้ยงให้ตรงกับไลฟ์สไตล์ของผู้รับเลี้ยงผ่าน Web Dashboard โดยผู้ใช้สามารถเข้าถึงระบบผ่าน Web Browser[cite: 1, 3]

Project นี้พัฒนาโดยใช้แนวทาง **Incremental Development** โดยแบ่งการพัฒนาออกเป็นหลาย Sprint และเพิ่มความสามารถของระบบทีละส่วน

การวางแผนระดับ Project นี้ใช้สำหรับกำหนด:
- เป้าหมายของแต่ละ Sprint
- ขอบเขตงานในภาพรวม
- ลำดับการพัฒนา
- Deliverables หลัก
- กำหนดเวลา
- สถานะของแต่ละ Sprint

รายละเอียดการดำเนินงานของแต่ละ Sprint จะถูกจัดเก็บแยกไว้ในไฟล์ของ Sprint นั้น ๆ

---

# 2. Project Development Approach

Project ใช้แนวทางการพัฒนาแบบ **Incremental Development**

Project Planning
        ↓
Sprint 1 (Web Prototype Foundation)
        ↓
Review / Feedback
        ↓
Sprint 2 (SQLite Database & Core Engines)
        ↓
Review / Feedback
        ↓
Sprint 3 (Data Analysis & Advanced Features)
        ↓
Review / Feedback
        ↓
Final Sprint (Integration & Delivery)
        ↓
Final Project Complete

ในแต่ละ Sprint ทีมจะ:
1. กำหนดเป้าหมายของ Sprint
2. กำหนดขอบเขตงาน
3. พัฒนาและทดสอบระบบ
4. Review ผลลัพธ์
5. รับ Feedback
6. ปรับปรุงระบบและ Documentation
7. นำผลลัพธ์ไปใช้เป็นพื้นฐานของ Sprint ถัดไป

แนวทางนี้ช่วยให้ทีมสามารถพัฒนา Project ทีละส่วน และสามารถตรวจสอบผลลัพธ์ของแต่ละช่วงก่อนขยาย Scope ไปยัง Sprint ถัดไป

---

# 3. Project Timeline

| Sprint | ช่วงเวลา | เป้าหมายหลัก | Status |
|---|---|---|:---:|
| **Sprint 1** | 10–15 September 2026 | Application Foundation & Web UI Prototype[cite: 1, 3] | ✅ Completed |
| **Sprint 2** | 20–24 September 2026 | Web UI + SQLite Database + Logic Engines | ✅ Completed |
| **Sprint 3** | 25–29 September 2026 | Data Analysis, Visualization & Advanced Features[cite: 5, 6, 8] | ✅ Completed |
| **Final Sprint** | Planned | Final Integration, Final QA & Delivery[cite: 1] | ⏳ Planned |

---

# 4. Sprint 1 — Web Foundation & Prototyping

## Objective
สร้าง Foundation และ Interactive Web Prototype ของ Pet Adoption Explorer เพื่อเตรียมโครงสร้างพื้นฐานและทดสอบ Navigation ของระบบก่อนเชื่อมต่อฐานข้อมูล[cite: 1, 3]

## Main Scope
- Streamlit Layout & Header Navigation Bar (7 Menus)[cite: 1]
- Home Page, Hero Banner & Pet of the Day Highlight[cite: 1, 3]
- Category Filter Buttons (Dogs, Cats, Rabbits ฯลฯ)[cite: 2]
- Search Component & Pet Cards Layout[cite: 4, 5]
- Pet Comparison Tool Prototype[cite: 6]
- Match Quiz UI Layout[cite: 7]
- Budget Calculator Engine Prototype & Timeline Slider[cite: 8]
- Favorites State Management Handling[cite: 9]

## Main Deliverable
Web Application Interactive Prototype ที่สามารถใช้งานเมนูหลักได้ราบรื่นผ่าน Browser[cite: 1, 3]

## Data Source
ใช้ **Local Sample Dataset** (Dictionary / JSON)[cite: 3]

## Status
**✅ Completed**

รายละเอียดการดำเนินงานของ Sprint 1: `Sprint1/Sprint_1.md`

---

# 5. Sprint 2 — Database Integration & Core Engines

## Objective
พัฒนา Foundation จาก Sprint 1 ให้กลายเป็น Web Application ที่เชื่อมต่อกับฐานข้อมูล SQLite จริง พร้อมพัฒนา Match Quiz Logic และ Budget Calculator Engine[cite: 7, 8]

## Main Scope
- **SQLite Database:** จัดเก็บข้อมูลสัตว์เลี้ยง (`pet_adoption.db`)
- **Pet Service Layer:** แยก Business Logic ออกจาก UI
- **Search System:** ค้นหาชื่อและสายพันธุ์แบบ Real-time (Case-insensitive & Partial Match)[cite: 5]
- **Category Filter:** กรองรายการสัตว์เลี้ยงตามประเภท[cite: 2]
- **Match Quiz Engine:** ประมวลผลคะแนนการจับคู่สัตว์เลี้ยงจากแบบสอบถาม 4 ข้อ[cite: 7]
- **Budget Calculator Engine:** คำนวณค่าใช้จ่ายแรกรับ + ยอดสะสมรายเดือนตาม Slider (1–36 เดือน)[cite: 8]
- **Favorites Management:** จัดเก็บรายการสัตว์เลี้ยงโปรดผ่าน `st.session_state` ข้ามหน้าเมนู[cite: 9]
- **Automated Testing:** Unit Tests สำหรับ Database, Service และ Logic Engines ผ่าน `pytest`

## Main Deliverable
Web Application ที่เชื่อมต่อฐานข้อมูล SQLite ดึง ค้นหา กรอง และคำนวณข้อมูลได้อย่างแม่นยำ[cite: 5, 7, 8]

## Status
**✅ Completed**

รายละเอียดการดำเนินงานของ Sprint 2: `Sprint2/Sprint_2.md`

---

# 6. Sprint 3 — Data Analysis, Visualization & Advanced Features

## Objective
นำข้อมูลสัตว์เลี้ยงจากระบบมาวิเคราะห์และนำเสนอในรูปแบบ Statistics และ Data Visualization ด้วย Pandas และ Altair พร้อมเพิ่มความสามารถในการ Filter, Sort และเปรียบเทียบข้อมูลเชิงลึก[cite: 5, 6, 8]

## Main Scope
- **Analysis Layer:** สร้าง `src/analysis/statistics.py` สำหรับคำนวณสถิติโดยเฉพาะ
- **Descriptive Statistics:** คำนวณ Mean, Median, Min, Max ของค่าเลี้ยงดูและอายุ[cite: 3, 8]
- **Data Visualization:** สร้าง Altair Interactive Charts (Category Distribution, Cost Analysis, Suitable Housing Proportion, Age Distribution)[cite: 2, 3, 8]
- **Advanced Filtering:** กรองหลายเงื่อนไขพร้อมกัน (Category + Location + Housing + Max Cost)[cite: 2, 3, 5, 8]
- **Advanced Sorting:** เรียงลำดับตามค่าใช้จ่าย, อายุ และชื่อ[cite: 3, 4, 8]
- **Advanced Pet Comparison:** ตารางเปรียบเทียบข้อมูลเชิงลึก 2-3 ตัวขนานกัน[cite: 6]
- **Empty State Handling:** จัดการกรณี Filter แล้วไม่พบข้อมูลให้ออกมาปลอดภัย ไม่ Crash[cite: 5]

## Main Deliverable
Statistics Dashboard พร้อมชุดข้อมูลวิเคราะห์เชิงลึก กราฟ Altair และระบบค้นหาขั้นสูง[cite: 5]

## Status
**✅ Completed**

รายละเอียดการดำเนินงานของ Sprint 3: `Sprint3/Sprint_3.md`

---

# 7. Final Sprint — Integration, QA & Final Delivery

## Objective
เตรียมระบบทั้งหมดให้พร้อมสำหรับ Final Project Delivery, Full Regression Testing และการนำเสนอฉบับสมบูรณ์[cite: 1]

## Main Scope
- Final Integration & System Stabilization
- Full Regression Testing ผ่าน `pytest` และ Manual Test Cases
- Bug Fixing & Performance Review (UI State Persistence & Query Optimization)[cite: 9]
- Repository Refactoring & Cleanup
- Final Documentation (README, Pitch, Plan, Change Log, Learning Log, Sprint Reports)
- Final Presentation Slides & Demo Flow Preparation

## Main Deliverable
Pet Adoption Explorer เวอร์ชัน Final ที่สมบูรณ์ เสถียร พร้อมสำหรับการส่งมอบและนำเสนอ

## Status
**⏳ Planned**

รายละเอียดการดำเนินงานของ Final Sprint: `Final Sprint/Final_Sprint.md`

---

# 8. Project Technology Roadmap

| Technology | Sprint 1 | Sprint 2 | Sprint 3 | Final Sprint |
|---|:---:|:---:|:---:|:---:|
| **Python** | ✅ | ✅ | ✅ | ✅ |
| **Streamlit (Web Dashboard)** | ✅ | ✅ | ✅ | ✅ |
| **SQLite Database** | - | ✅ | ✅ | ✅ |
| **Pet Service Layer** | - | ✅ | ✅ | ✅ |
| **Pandas (Data Processing)** | - | ✅ | ✅ | ✅ |
| **Match Quiz Logic Engine**[cite: 7] | Prototype | ✅ | ✅ | ✅ |
| **Budget Calculator Engine**[cite: 8] | Dynamic UI | ✅ | ✅ | ✅ |
| **Altair (Data Visualization)** | - | - | ✅ | ✅ |
| **Advanced Filtering & Sorting**[cite: 5] | Basic | Basic | ✅ | ✅ |
| **pytest (Automated Testing)** | Manual | ✅ | ✅ | ✅ |
| **Final Regression & CI Review** | - | - | - | Planned |

---

# 9. Project Deliverables Roadmap

| Deliverable | Sprint | Status |
|---|---|:---:|
| Project Pitch & Master Plan | Sprint 1 | ✅ Completed |
| Web UI Prototype & Layout[cite: 1, 3] | Sprint 1 | ✅ Completed |
| SQLite Database & Service Layer | Sprint 2 | ✅ Completed |
| Search & Category Filter System[cite: 2, 5] | Sprint 2 | ✅ Completed |
| Match Quiz & Budget Engines[cite: 7, 8] | Sprint 2 | ✅ Completed |
| Favorites Session State Management[cite: 9] | Sprint 2 | ✅ Completed |
| Analysis Layer (`statistics.py`) | Sprint 3 | ✅ Completed |
| Statistics Dashboard & Altair Visualizations | Sprint 3 | ✅ Completed |
| Advanced Multi-condition Filtering & Sorting[cite: 5] | Sprint 3 | ✅ Completed |
| Advanced Pet Comparison Tool[cite: 6] | Sprint 3 | ✅ Completed |
| Full Regression Testing & QA | Final Sprint | ⏳ Planned |
| Final Presentation & Repository Release | Final Sprint | ⏳ Planned |

---

## Project Structure

```text
Pet-Adoption-Explorer/
│
├── README.md
│
├── docs/
│   ├── Project_Pitch.md
│   ├── Plan.md
│   ├── CHANGELOG.md
│   └── LEARNINGLOG.md
│
├── src/
│   ├── app.py
│   ├── analysis/
│   ├── components/
│   ├── database/
│   ├── services/
│   └── utils/
│
├── tests/
│
├── Sprint1/
│   └── Sprint_1.md
│
├── Sprint2/
│   └── Sprint_2.md
│
├── Sprint3/
│   └── Sprint_3.md
│
└── Final Sprint/
    └── Final_Sprint.md
```


---

# 11. Team Planning & Role Rotation

ทีมมีสมาชิก 3 คน และใช้ **Role Rotation** ในการแบ่งความรับผิดชอบในแต่ละ Sprint

| สมาชิก | ชื่อเล่น | Sprint 1 Role | Sprint 2 Role | Sprint 3 Role | Final Sprint Role |
|---|---|---|---|---|---|
| นางสาวกุณทิกา จุลฤกษ์ | **โดนัท** | Planner | Debugger / QA | Coder | Planner |
| นายภาคิไณ มุระดา | **ภีม** | Coder | Planner | Debugger / QA | Coder |
| นายคุณานนท์ ถาเอ็นยวน | **ฟีฟ่า** | Debugger / QA | Coder | Planner | Debugger / QA |

---

# 12. Sprint Status Overview

```text
Sprint 1        ✅ Completed
Sprint 2        ✅ Completed
Sprint 3        ✅ Completed
Final Sprint    ⏳ Planned
