# 🐱 Pet Adoption Explorer — Project Pitch

## Final Term Project — CP352301 Script Programming

---

# 1. Project Overview

**Pet Adoption Explorer** คือ Web Application สำหรับศูนย์รวมข้อมูลสัตว์เลี้ยงตามหาบ้านใหม่ ซึ่งพัฒนาเพื่อเป็นระบบตัวกลางในการรวบรวม จัดการ วิเคราะห์งบประมาณการเลี้ยงดู และจับคู่สัตว์เลี้ยงให้ตรงกับไลฟ์สไตล์ของผู้รับเลี้ยงผ่าน Web Dashboard

ระบบพัฒนาด้วย Python และ Streamlit โดยเชื่อมต่อและจัดเก็บข้อมูลสัตว์เลี้ยงผ่าน SQLite Database[cite: 3, 8, 10]

ผู้ใช้สามารถเข้าถึงระบบผ่าน Web Browser เพื่อค้นหา กรองหมวดหมู่ เรียงลำดับ เปรียบเทียบ ทำแบบทดสอบแมตช์ไลฟ์สไตล์ คำนวณงบประมาณ และวิเคราะห์ข้อมูลสถิติต่างๆ ของสัตว์เลี้ยงได้ภายในระบบเดียว[cite: 1, 2, 5, 6, 7, 8]

โปรเจกต์พัฒนาด้วยแนวทาง **Incremental Development** โดยแบ่งการพัฒนาออกเป็น Sprint และเพิ่มความสามารถของระบบอย่างต่อเนื่อง ตั้งแต่ Web UI Prototype ใน Sprint 1 ไปสู่ SQLite Integration, Quiz Engine และ Budget Engine ใน Sprint 2 และขยายไปสู่ Data Analysis Layer, Altair Visualization และ Advanced Features ใน Sprint 3[cite: 1, 5, 6, 7, 8]

---

# 2. Problem Statement

การหาบ้านใหม่ให้สัตว์เลี้ยงและการตัดสินใจรับเลี้ยงสัตว์ในปัจจุบันยังมีอุปสรรคสำคัญหลายประการ เช่น

- ข้อมูลสัตว์เลี้ยงกระจายตัวและขาดมาตรฐาน (เช่น อายุ, สายพันธุ์, ที่อยู่อาศัยที่เหมาะสม, ค่าใช้จ่ายประจำเดือน)[cite: 3, 4, 8]
- ผู้รับเลี้ยงขาดข้อมูลในการประเมินความพร้อมทางการเงินล่วงหน้า (Initial Cost & Monthly Maintenance Cost)
- ผู้รับเลี้ยงไม่ทราบว่าไลฟ์สไตล์และที่อยู่อาศัยของตนเอง (เช่น คอนโด/บ้านเดี่ยว, เวลาว่าง) เหมาะสมกับสัตว์เลี้ยงประเภทใด[cite: 3, 7]
- ขาด tools ในการเปรียบเทียบข้อดี-ข้อจำกัดของสัตว์เลี้ยงแต่ละตัวขนานกัน

หากผู้ใช้ต้องการหาบ้านใหม่ให้น้องๆ การค้นหาข้อมูลจากหลายแหล่งอาจยุ่งยาก และเสร็จสิ้นด้วยการรับเลี้ยงที่ไม่พร้อม จนเกิดปัญหาน้องถูกทิ้งขว้างในภายหลัง

ดังนั้นกลุ่มจึงพัฒนา **Pet Adoption Explorer** เพื่อรวบรวมข้อมูลสัตว์เลี้ยง จัดการฐานข้อมูลอย่างเป็นระบบ และนำเสนอผ่าน Web Dashboard ที่ช่วยให้ผู้ใช้สามารถค้นหา ทำแบบทดสอบวิเคราะห์ความเข้ากันได้ คำนวณงบประมาณ และวิเคราะห์ข้อมูลภาพรวมได้อย่างสะดวกแม่นยำ[cite: 1, 7, 8]

---

# 3. Project Objectives

โปรเจกต์นี้มีวัตถุประสงค์หลักดังนี้

1. พัฒนา Web Application สำหรับศูนย์รวมข้อมูลสัตว์เลี้ยงตามหาบ้านใหม่
2. จัดเก็บและจัดการข้อมูลสัตว์เลี้ยงอย่างเป็นระบบด้วย SQLite Database
3. พัฒนาระบบค้นหา (Search) สัตว์เลี้ยงตามชื่อและสายพันธุ์แบบ Real-time
4. พัฒนาระบบ กรอง (Filter) ตามประเภทสัตว์เลี้ยง สถานที่ และเงื่อนไขที่พัก[cite: 2, 3, 5]
5. พัฒนาระบบ จัดเรียง (Sort) ตามค่าเลี้ยงดู อายุ และชื่อ[cite: 3, 4, 8]
6. พัฒนา Match Quiz Engine วิเคราะห์ความเหมาะสมระหว่างผู้รับเลี้ยงกับสัตว์เลี้ยง
7. พัฒนา Dynamic Budget Calculator คำนวณประมาณการค่าใช้จ่ายแรกรับและรายเดือนสะสม
8. พัฒนา Pet Comparison Tool เปรียบเทียบข้อมูลสัตว์เลี้ยง 2-3 ตัวขนานกัน[cite: 6]
9. พัฒนาระบบ Favorites สำหรับบันทึกสัตว์เลี้ยงที่สนใจด้วย Session State
10. จัดทำ Data Processing และ Normalization ข้อมูลก่อนนำไปวิเคราะห์
11. คำนวณ Descriptive Statistics และทำ Exploratory Data Analysis (EDA) ข้อมูลสัตว์เลี้ยง[cite: 3, 8]
12. นำเสนอข้อมูลภาพรวมผ่าน Data Visualization ด้วย Altair[cite: 2, 3, 8]
13. รองรับ Error Handling และ Empty State เพื่อป้องกัน Application Crash[cite: 5, 9]
14. ทดสอบระบบด้วย Automated Testing (`pytest`) และ Integration QA
15. พัฒนาโปรเจกต์ตามแนวทาง Incremental Development ผ่านแต่ละ Sprint
16. ใช้ Git และ GitHub สำหรับ Version Control และการทำงานร่วมกันภายในทีม

---

# 4. Target Users

ระบบถูกออกแบบสำหรับผู้ใช้ที่ต้องการสำรวจและรับเลี้ยงสัตว์เลี้ยง เช่น

- ผู้ที่กำลังมองหาและค้นหาสัตว์เลี้ยงหาบ้านใหม่[cite: 1, 5]
- ผู้ที่ต้องการประเมินงบประมาณและค่าใช้จ่ายก่อนตัดสินใจรับเลี้ยง
- ผู้ที่ต้องการทดสอบไลฟ์สไตล์ของตนเองว่าเหมาะกับสัตว์เลี้ยงชนิดใด
- ผู้ที่ต้องการเปรียบเทียบสัตว์เลี้ยงหลายๆ ตัวก่อนเลือกรับเลี้ยง[cite: 6]
- ผู้ที่ต้องการดูข้อมูลสถิติและภาพรวมสัตว์เลี้ยงตามหาบ้านใหม่[cite: 2, 3, 8]

โปรเจกต์นี้เน้นการนำเสนอข้อมูล การจับคู่ และการคำนวณงบประมาณ ไม่ได้ออกแบบมาเพื่อเป็นระบบซื้อขายสัตว์เลี้ยงเชิงพาณิชย์

---

# 5. Target Application Format

## Web Application

The system will be developed as a **Web Application** using Streamlit, accessible through a web browser.

The application will provide a user-friendly and visually appealing interface to help users explore pets and make informed adoption decisions.

### Application Overview

```text
User
  │
  ▼
Web Browser
  │
  ▼
Pet Adoption Explorer
  │
  ├── Home / Hero Banner
  │
  ├── Category Filter
  │   └── Dogs, Cats, Rabbits, Rodents, Birds
  │
  ├── Pet of the Day Highlight
  │
  ├── Explore
  │   └── Search, Multi-Filter, Sort
  │
  ├── Match Quiz Engine
  │
  ├── Budget Calculator Engine
  │
  ├── Pet Comparison Tool
  │
  ├── Favorites List (Saved Pets)
  │
  └── Statistics & Data Visualization
      └── Altair Charts
```

### Key Features

- **Home / Hero Banner:** Introduces the application and guides users to explore pets.
- **Category Filter:** Filters pets by animal categories, including dogs, cats, rabbits, rodents, and birds.
- **Pet of the Day:** Highlights a selected pet each day.
- **Explore:** Allows users to search, apply multiple filters, and sort pet listings.
- **Match Quiz Engine:** Recommends pets based on users' preferences and lifestyle.
- **Budget Calculator:** Helps users estimate the costs of caring for a pet.
- **Pet Comparison Tool:** Allows users to compare pet characteristics.
- **Favorites List:** Lets users save pets they are interested in.
- **Statistics & Data Visualization:** Presents adoption-related data through interactive charts created with Altair.

### Technology Stack

- **Framework:** Streamlit
- **Interface:** Web Browser
- **Data Visualization:** Altair
- **Application Logic:** Python

---

# 6. Project Evolution

โปรเจกต์ถูกพัฒนาตามลำดับจากระบบ Prototype พื้นฐานไปสู่ Web Application ที่มีความสามารถด้าน Data Analysis

Sprint 1
Web UI Prototype & Foundation[cite: 1, 3]
      ↓
Local Sample Dataset[cite: 3]
      ↓
Sprint 2
Streamlit Web Application[cite: 3, 10]
      ↓
SQLite Database Integration
      ↓
Pet Service Layer & Search Logic
      ↓
Match Quiz & Budget Engines
      ↓
Sprint 3
Data Processing & Normalization
      ↓
EDA / Descriptive Statistics[cite: 3, 8]
      ↓
Altair Data Visualization[cite: 2, 3, 8]
      ↓
Advanced Multi-Filtering & Sorting
      ↓
Advanced Pet Comparison Table[cite: 6]
      ↓
Integrated Dashboard
      ↓
Final Sprint
Final Integration + Full Regression QA + Final Delivery[cite: 1]

---

# 7. Main Features

## 7.1 Home Page & Category Navigation
- แบนเนอร์Hero ต้อนรับ และการนำเสนอระบบ[cite: 1]
- ปุ่มสลับกรองหมวดหมู่สัตว์เลี้ยง (ALL PETS, DOGS, CATS, RABBITS, RODENTS, BIRDS)[cite: 2]
- ส่วนแสดงสัตว์เลี้ยงโดดเด่นประจำวัน (Pet of the Day) พร้อมรายละเอียดสายพันธุ์ ที่พัก และงบประมาณ[cite: 3]

## 7.2 Search & Multi-Condition Filtering
- ค้นหาสัตว์เลี้ยงจากชื่อหรือสายพันธุ์แบบ Real-time (Case-insensitive & Partial Match)[cite: 5]
- กรองหลายเงื่อนไขพร้อมกัน: หมวดหมู่ + สถานที่ + ที่พักที่เหมาะ (Condo/House) + งบประมาณสูงสุดต่อเดือน[cite: 2, 3, 5, 8]

## 7.3 Advanced Sorting
- เรียงลำดับรายการสัตว์เลี้ยงตาม: ประมาณการค่าเลี้ยงดูต่อเดือน (น้อยไปมาก/มากไปน้อย)[cite: 8], อายุ[cite: 3, 4] และชื่อ[cite: 3, 4]

## 7.4 Match Quiz Engine
- แบบทดสอบ 4 ข้อ วิเคราะห์ความเข้ากันได้จากไลฟ์สไตล์ผู้ใช้ (ประเภทที่สนใจ, ที่อยู่อาศัย, เวลาว่าง, งบประมาณ)[cite: 7]
- ประมวลผลคะแนนเพื่อแนะนำสัตว์เลี้ยงที่เหมาะสมที่สุด[cite: 7]

## 7.5 Dynamic Budget Calculator Engine
- เลือกรอบเวลาการประเมิน (1–36 เดือน) ผ่าน Interactive Slider[cite: 8]
- คำนวณสรุปค่าใช้จ่ายแรกรับ (Initial Cost) + ค่าเลี้ยงดูสะสมรายเดือน (Monthly Cost)[cite: 8]

## 7.6 Pet Comparison Tool
- เลือกสัตว์เลี้ยง 2–3 ตัวเพื่อนำมาเปรียบเทียบข้อมูลสำคัญ (ค่าแรกรับ, ค่าใช้จ่ายรายเดือน, เงื่อนไขที่พัก, นิสัย) ขนานกันในรูปแบบตาราง[cite: 3, 6, 8]

## 7.7 Favorites System
- บันทึกสัตว์เลี้ยงที่สนใจไว้ในหน้า Favorites โดยใช้ Global Session State ในการจัดเก็บข้อมูลตลอดการใช้งาน

## 7.8 Statistics Dashboard & Visualization
- คำนวณค่าสถิติเชิงพรรณนา (Count, Mean, Median, Min, Max ของค่าใช้จ่ายและอายุ)[cite: 3, 8]
- แสดงผลกราฟ Altair Visualizations เช่น Category Distribution[cite: 2], Cost Analysis by Category[cite: 2, 8], Suitable Housing Proportion[cite: 3] และ Age Distribution[cite: 3, 4]

## 7.9 Empty State & Error Handling
- จัดการกรณีไม่พบข้อมูลจากการค้นหา/กรอง หรือรายการ Favorites ว่างเปล่า โดยแสดง Informative Message เตือนผู้ใช้โดยไม่ทำให้ระบบ Crash[cite: 5, 9]

---

# 8. Data Sources & Database Structure

## SQLite Database (`pet_adoption.db`)
ระบบจัดเก็บข้อมูลไว้ในฐานข้อมูล Relational SQLite โดยมี Fields หลักได้แก่:

- `pet_id`: รหัสสัตว์เลี้ยง (Primary Key)
- `name`: ชื่อสัตว์เลี้ยง[cite: 3, 4]
- `breed`: สายพันธุ์[cite: 3]
- `category`: ประเภท (Dog, Cat, Rabbit, Rodent, Bird)[cite: 2, 3]
- `location`: สถานที่ (เช่น Bangkok, Nonthaburi)[cite: 3, 4]
- `age_years`: อายุ (ปี)[cite: 3, 4]
- `suitable_housing`: ที่พักที่เหมาะ (Condo / House)[cite: 3]
- `initial_cost`: ค่าใช้จ่ายแรกรับ (บาท)[cite: 8]
- `monthly_cost`: ประมาณการค่าเลี้ยงดูต่อเดือน (บาท)[cite: 3, 8]
- `description`: คำอธิบายลักษณะ/นิสัย[cite: 3]
- `tags`: แท็กสแนปสั้นๆ[cite: 4]
- `image_url`: รูปภาพประกอบ[cite: 3, 4]
- `is_featured`: สถานะสัตว์เลี้ยงโดดเด่น (0/1)[cite: 3]

---

# 9. Data Processing & Quality Principles

ข้อมูลจากฐานข้อมูลจะถูกนำมาเข้ากระบวนการ Data Processing ด้วย Pandas ก่อนนำไปคำนวณสถิติและสร้าง กราฟ Visualizations

หลักการสำคัญ:
- ทำ Data Normalization และแปลงชนิดข้อมูล (Type Conversion)
- จัดการ Missing Values หรือ Field ที่ไม่มีข้อมูลอย่างปลอดภัยด้วย Numeric Coercion
- ไม่กำหนด Missing Cost เป็น 0 โดยอัตโนมัติ เพื่อป้องกันไม่ให้ค่าเฉลี่ยงบประมาณผิดเพี้ยน
- ตรวจสอบความสอดคล้องกันระหว่าง Database, Service Layer และ UI Rendering

---

# 10. Data Analysis & Visualizations

Sprint 3 เพิ่มส่วน Data Analysis เพื่อนำข้อมูลสัตว์เลี้ยงในฐานข้อมูลมาวิเคราะห์และนำเสนอ

กระบวนการโดยรวม:

SQLite Database
       ↓
Pet Service Query
       ↓
Data Processing & Cleaning
       ↓
Analysis Layer (`statistics.py`)
       ↓
Descriptive Statistics & Proportion Calculations
       ↓
Altair Visualizations
       ↓
Streamlit Dashboard Page

องค์ประกอบของ Visualization:
1. **Category Distribution:** Bar Chart แสดงจำนวนสัตว์เลี้ยงหาบ้านแยกตามประเภท[cite: 2]
2. **Monthly Cost Analysis:** Bar Chart แสดงค่าเฉลี่ยค่าเลี้ยงดูรายเดือนของแต่ละหมวดหมู่[cite: 2, 8]
3. **Housing Proportion:** Donut/Pie Chart แสดงสัดส่วนสัตว์เลี้ยงที่เหมาะกับ Condo vs House[cite: 3]
4. **Age Distribution:** Binned Bar Chart แสดงการกระจายตัวของอายุสัตว์เลี้ยง[cite: 3, 4]

---

# 11. System Architecture

The system architecture of Pet Adoption Explorer is illustrated below.

```text
                 ┌──────────────────────┐
                 │     Web Browser      │
                 │         User         │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Streamlit Web UI   │
                 │      Dashboard      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │     Pet Service      │
                 │  Application Logic   │
                 └──────────┬───────────┘
                            │
                ┌───────────┴───────────┐
                ▼                       ▼
      ┌──────────────────┐   ┌──────────────────┐
      │  Match Quiz      │   │   Budget Engine  │
      │     Engine       │   │                  │
      └─────────┬────────┘   └─────────┬────────┘
                │                      │
                └──────────┬───────────┘
                           ▼
                 ┌──────────────────────┐
                 │   Data Processing    │
                 │   & Normalization    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   SQLite Database    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Analysis Layer    │
                 │      Statistics      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Altair Charts     │
                 │   Visualization      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Streamlit UI      │
                 │  Display Results     │
                 └──────────────────────┘
```

## Component Responsibilities

- **Web Browser:** Allows users to access and interact with the application.
- **Streamlit Web UI:** Displays the dashboard and provides the user interface.
- **Pet Service:** Handles application logic and coordinates pet-related operations.
- **Match Quiz Engine:** Recommends suitable pets based on user preferences.
- **Budget Engine:** Estimates the costs of pet ownership.
- **Data Processing & Normalization:** Cleans and prepares data for consistent use.
- **SQLite Database:** Stores pet information and application data.
- **Analysis Layer:** Processes data and calculates statistical insights.
- **Altair Charts:** Visualizes statistical results through charts.
- **Streamlit UI:** Presents the results to users in the web application.

## System Workflow

The user interacts with the application through the Streamlit interface. The Pet Service coordinates the application logic and connects to the relevant engines and data-processing components. Data is stored in SQLite and used by the Analysis Layer to generate statistical insights. Altair then visualizes the results, which are displayed through the Streamlit interface.

# 12. Technology Stack

| Technology | Purpose |
| --- | --- |
| Python | ภาษาหลักในการพัฒนาโปรเจกต์ |
| Streamlit | Web Application Framework สำหรับ Dashboard[cite: 3, 10] |
| Pandas | Data Processing, Cleaning และ Data Analysis |
| SQLite | Relational Database สำหรับเก็บข้อมูลสัตว์เลี้ยง |
| Altair | Data Visualization Framework สำหรับสร้างกราฟแบบ Interactive |
| pytest | Automated Testing Framework |
| Git / GitHub | Version Control และ Team Collaboration |

---

# 13. Project Structure

```text
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
│   ├── app.py
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── statistics.py
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── header.py
│   │   ├── pet_card.py
│   │   ├── statistics_page.py
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
├── Sprint3/
│   └── Sprint_3.md
└── Final Sprint/
    └── Final_Sprint.md
