# 📚 Learning Log — Pet Adoption Explorer

## Final Term Project — CP352301 Script Programming

Learning Log นี้ใช้สำหรับบันทึกสิ่งที่สมาชิกในกลุ่มได้เรียนรู้จากการพัฒนา Pet Adoption Explorer ในแต่ละ Sprint ตั้งแต่ Sprint 1 จนถึง Sprint สุดท้าย[cite: 1]

เนื้อหาจะถูก Update หลังจากจบแต่ละ Sprint เพื่อบันทึกทั้ง Technical Learning, Project Management, Teamwork, Problems และ Lessons Learned

---

# 📌 Learning Log Structure

ในแต่ละ Sprint จะบันทึกหัวข้อหลักดังนี้:

1. Sprint Overview
2. What We Did
3. What We Learned
4. Problems & Challenges
5. How We Solved Them
6. Teamwork & Process Learning
7. Technical Learning
8. Instructor / Team Feedback
9. Lessons Learned
10. How We Will Apply This Learning

---

# 🚀 Sprint 1 — Application Foundation & Web Prototyping

**Period:** 10–15 September 2026  
**Status:** Completed

## 1. Sprint Overview

Sprint 1 เป็นช่วงเริ่มต้นของการพัฒนา Project โดยมีเป้าหมายเพื่อสร้าง Web Application Foundation และทำความเข้าใจกระบวนการทำงานของทีม

ใน Sprint นี้ทีมพัฒนา Interactive Prototype ด้วย Streamlit เพื่อทดลองโครงสร้างการทำงานและ Navigation ของระบบ Pet Adoption Explorer ก่อนนำไปพัฒนาเชื่อมต่อฐานข้อมูลใน Sprint ถัดไป[cite: 1, 3]

---

## 2. What We Did

สิ่งที่ทีมดำเนินการใน Sprint 1:

- กำหนด Sprint Goal, Scope และ Functional Requirements
- แบ่ง Role ของสมาชิก (Planner: คิม, Coder: ฟลุ๊ค, Debugger: ออม)
- ออกแบบ UI Wireframe & Top Navigation Bar[cite: 1]
- พัฒนาหน้า Home Page, Hero Banner และ Categories Filter[cite: 1, 2]
- พัฒนาส่วนแสดง Pet of the Day Highlight[cite: 3]
- พัฒนาหน้า Explore และระบบ Search เบื้องต้น[cite: 4, 5]
- พัฒนาส่วน Compare สัตว์เลี้ยง (2-3 ตัว)[cite: 6]
- พัฒนาโครงร่างแบบทดสอบ Match Quiz (4 ข้อ)[cite: 7]
- พัฒนาเครื่องคำนวณงบประมาณ (Budget Calc) และ Time Slider[cite: 8]
- พัฒนาหน้า Favorites Empty State[cite: 9]
- ทดสอบ UI Layout และ Session State การเปลี่ยนหน้า[cite: 1, 9]
- จัดทำ Documentation และ GitHub Repository

---

## 3. What We Learned

### Project Planning
การกำหนด Scope และ Requirements ของ Web Dashboard ล่วงหน้า ช่วยให้สมาชิกมองเห็นภาพรวมของระบบร่วมกัน และลดความสับสนในการเลือกฟังก์ชันที่จะพัฒนาใน Sprint แรก

### Streamlit Development
ได้เรียนรู้การแบ่งแยก UI Component บน Streamlit ออกเป็นส่วนๆ เพื่อให้อ่านง่ายและบำรุงรักษาสะดวก เช่น:
- `render_header_nav()`[cite: 1]
- `render_home_page()`[cite: 1]
- `render_explore_page()`[cite: 5]
- `render_compare_page()`[cite: 6]
- `render_match_quiz_page()`[cite: 7]
- `render_budget_calc_page()`[cite: 8]

### State Management & Input Handling
เรียนรู้ว่าในการพัฒนา Web App ด้วย Streamlit การ Re-run ของโค้ดเมื่อผู้ใช้เปลี่ยน Input Widget จำเป็นต้องอาศัยการจัดการ Session State เพื่อป้องกันไม่ให้ข้อมูลหรือสถานะการกดสลับเมนูหลุดหาย[cite: 9]

---

## 4. Problems & Challenges

### Problem 1 — Navigation Page Switching State Loss
เมื่อผู้ใช้คลิกสลับเมนูบน Top Navigation Bar ค่าที่เลือกไว้ในแบบทดสอบ หรือสัตว์เลี้ยงที่กดเลือกเปรียบเทียบถูก Reset[cite: 1, 6, 7, 9]

### Problem 2 — Dynamic Layout Control
การจัดวางการ์ดสัตว์เลี้ยงในหน้า Explore ให้ตอบสนองและเรียงสวยงามตามขนาดหน้าจอ[cite: 4, 5]

---

## 5. How We Solved Them

### Solution 1 — Streamlit Session State
ใช้งาน `st.session_state` สำหรับจัดเก็บเมนูปัจจุบัน และค่าการเลือกสัตว์เลี้ยงของผู้ใช้ข้ามหน้า[cite: 9]

### Solution 2 — Column Layouts
ใช้งาน `st.columns` เพื่อจัดโครงสร้างการ์ดสัตว์เลี้ยงแบบ Grid ให้แสดงผลได้เรียบร้อย[cite: 4]

---

## 6. Teamwork & Process Learning

การแบ่ง Role เป็น Planner (คิม), Coder (ฟลุ๊ค), Debugger (ออม) ทำให้การสื่อสารในทีมมีความชัดเจน โดย Planner จะส่งมอบ Requirements และ UI Flow ให้ Coder พัฒนา จากนั้น Debugger จะนำ Test Cases มาสอบทานและแจ้งข้อผิดพลาดกลับไปแก้ไขได้อย่างรวดเร็ว

---

## 7. Technical Learning

- **Streamlit:** Pages, Columns, Session State, Interactive Widgets[cite: 1, 9, 10]
- **Python Data Structures:** Dictionaries & Lists สำหรับจัดการ Sample Pet Data[cite: 3]
- **Git/GitHub:** Feature Branching, Pull Requests และ Commit History

---

## 8. Lessons Learned & Next Step

1. การทำ Prototype ด้วย Streamlit ช่วยให้ได้การตอบสนองเชิง UI เร็วมาก[cite: 3, 10]
2. ข้อมูลชั่วคราว (Sample Data) ควรเตรียมโครงสร้าง Field ให้ตรงกับ Database ที่จะใช้จริงใน Sprint 2
3. ควรเพิ่ม Unit Tests สำหรับประมวลผลคำนวณงบประมาณและแบบทดสอบแมตช์[cite: 7, 8]

---

# 🚀 Sprint 2 — Web UI, API/Database Integration & Interactive Features

**Period:** 20–24 September 2026  
**Status:** Completed

## 1. Sprint Overview

**Sprint Goal:**  
พัฒนา Pet Adoption Explorer จาก Prototype ใน Sprint 1 ให้เป็น Web Application ที่เชื่อมต่อฐานข้อมูล SQLite จริง พร้อมพัฒนา Match Quiz Logic และ Dynamic Budget Engine[cite: 7, 8]

---

## 2. What We Did

- สร้างและเชื่อมต่อฐานข้อมูล SQLite (`pet_adoption.db`)
- พัฒนา Pet Service Layer เพื่อแยก Business Logic ออกจาก Streamlit UI
- เชื่อมต่อระบบค้นหาสัตว์เลี้ยงจากฐานข้อมูล (Real-time Partial Match & Case-insensitive)[cite: 5]
- พัฒนาระบบ Filter สัตว์เลี้ยงตามหมวดหมู่ (Dogs, Cats, Rabbits ฯลฯ)[cite: 2]
- พัฒนา Match Quiz Engine คำนวณคะแนนจับคู่สัตว์เลี้ยงจากไลฟ์สไตล์ 4 ข้อ[cite: 7]
- พัฒนา Budget Calculator คำนวณยอดรวมแรกรับ + ยอดสะสมรายเดือนตาม Slider (1-36 เดือน)[cite: 8]
- พัฒนาระบบบันทึก Favorites ด้วย Global Session State[cite: 9]
- เขียน Automated Unit Tests ด้วย `pytest` ครอบคลุม Database และ Service Logic

---

## 3. What We Learned

### Database Integration
เรียนรู้การออกแบบ Relational Database สำหรับเก็บข้อมูลสัตว์เลี้ยง รวมถึงการเขียน SQL Queries ผ่าน Python `sqlite3` และการจัดการ Connection อย่างปลอดภัย

### Service-Oriented Architecture
เรียนรู้ประโยชน์ของการแยก Data Layer (Database) และ Presentation Layer (Streamlit UI) ออกจากกันด้วย Service Layer (`pet_service.py`) ซึ่งช่วยให้เขียน Test Cases ได้ง่ายและระบุจุดเกิด Bug ได้รวดเร็ว

---

## 4. Problems & Challenges & Solutions

| Problem | Impact | Solution | Result |
|---|---|---|---|
| ค่า Saved Favorites หลุดเมื่อสลับหน้า[cite: 9] | สัตว์เลี้ยงที่บันทึกไว้ในหน้า Favorites หายไป[cite: 9] | ประกาศ `st.session_state.favorites` เป็น Global State ตั้งแต่เปิด App | เก็บข้อมูลสัตว์เลี้ยงโปรดข้ามเมนูได้ตลอดการใช้งาน[cite: 9] |
| สัตว์เลี้ยงบางตัวไม่มี URL รูปภาพ | การ์ดแสดงผลรูปเบี้ยวหรือเกิด Error | ใส่ Default Fallback Image URL ใน Data Processing Layer | การ์ดสัตว์เลี้ยงแสดงผลสวยงามสม่ำเสมอทุกใบ |
| การค้นหาภาษาไทย/อังกฤษ ไม่พบคีย์เวิร์ด[cite: 5] | ผู้ใช้ค้นหาแล้วไม่เจอข้อมูล[cite: 5] | ทำ String Normalization และใช้ `LIKE %query%` ใน SQL Query[cite: 5] | ค้นหาชื่อและสายพันธุ์ได้อย่างยืดหยุ่น[cite: 5] |

---

## 5. Technical Learning Summary (Sprint 2)

- **SQLite:** Schema Design, CRUD Operations, Parameterized Queries
- **Pandas & Data Processing:** Data Normalization, Missing Values Clean-up
- **State Management:** Complex Session State Persistence on Multi-page Streamlit[cite: 9]
- **Testing:** `pytest` for Database & Service Layer Testing

---

# 🚀 Sprint 3 — Data Analysis, Visualization & Advanced Features

**Period:** 25–29 September 2026  
**Status:** Completed

## 1. Sprint Overview

**Sprint Goal:**  
เพิ่ม Analysis Layer วิเคราะห์ข้อมูลสัตว์เลี้ยงด้วย Pandas และนำเสนอผ่าน Altair Visualizations บนหน้า Statistics Page พร้อมพัฒนาระบบ Multi-condition Filtering, Advanced Sorting และ Pet Comparison[cite: 5, 6, 8]

---

## 2. What We Did

- เพิ่ม Analysis Layer (`src/analysis/statistics.py`) แยกส่วนคำนวณสถิติ
- สรุปค่าสถิติ Descriptive Statistics (Mean, Median, Min, Max ของค่าเลี้ยงดูรายเดือนและอายุ)[cite: 3, 8]
- พัฒนากราฟแสดงสถิติบนหน้า Statistics Page ด้วย Altair (Category Distribution, Cost Analysis, Suitable Housing Proportion, Age Distribution)[cite: 2, 3, 8]
- พัฒนา Advanced Multi-condition Filtering (กรองประเภท + สถานที่ + ที่พัก + งบประมาณ)[cite: 2, 3, 5, 8]
- พัฒนาระบบ Advanced Sorting (เรียงตามค่าเลี้ยงดู, อายุ, ชื่อ)[cite: 3, 4, 8]
- พัฒนาตารางเปรียบเทียบข้อมูลสัตว์เลี้ยงเชิงลึก (Pet Comparison Table)[cite: 6]
- เขียน Test Cases สำหรับ Analysis Layer และ Data Normalization

---

## 3. What We Learned

### Data Analysis & Visualization
เรียนรู้การใช้ Pandas DataFrame แปลงข้อมูลจาก SQLite มาวิเคราะห์หาความสัมพันธ์และสถิติเชิงพรรณนา พร้อมใช้ Altair สร้าง Interactive Charts ที่เชื่อมต่อกับ Streamlit UI ได้อย่างลื่นไหล

### Modular Architecture
การแยก `statistics.py` ออกมาจาก UI ช่วยให้สามารถทดสอบความถูกต้องของค่านวณสถิติ (เช่น Mean, Standard Deviation) ได้อย่างแม่นยำโดยไม่ต้องผ่านหน้าจอ Web

---

## 4. Problems & Challenges & Solutions

| Problem | Impact | Solution | Result |
|---|---|---|---|
| สัตว์เลี้ยงบางตัวไม่มี Initial Cost ทำให้ Pandas คำนวณ Mean เกิด `NaN`[cite: 8] | สถิติบน UI แสดงผล Error | ใช้ Numeric Coercion และกรองเฉพาะ Valid Numeric Data มาคำนวณ | แสดงค่าสถิติได้ถูกต้อง และระบุ N/A สำหรับข้อมูลที่ไม่สมบูรณ์ |
| เมื่อ Filter แล้วไม่พบข้อมูล (Empty Dataset)[cite: 5] | กราฟ Altair เกิด Error บน UI | เพิ่ม Empty Dataset Check ก่อน Render กราฟ | แสดง Informative Message แจ้งผู้ใช้ได้อย่างปลอดภัย[cite: 5] |

---

## 5. Technical Learning Summary (Sprint 3)

- **Pandas Analysis:** Descriptive Statistics, GroupBy, Value Counts & Proportion
- **Altair Data Visualization:** Interactive Bar Charts, Binned Distribution Charts & Donut Charts
- **Advanced UI Filtering:** Complex Query Building & State Retention[cite: 5]

---

# 🚀 Final Sprint — Integration, Testing & Final Delivery

**Period:** 2–6 October 2569  
**Status:** Planned

## 1. Sprint Overview

Final Sprint เน้นการตรวจสอบความสมบูรณ์ของระบบทั้งหมด (Full Integration & Regression Testing), การแก้ไขข้อผิดพลาดสะสม (Bug Fixing), การปรับแต่ง UI/UX Performance และการจัดเตรียมเอกสารพร้อมสำหรับการส่งมอบ Final Project Delivery[cite: 1]

---

## 2. Planned Activities

- ทำ Full Regression Testing ครอบคลุมการทำงานตั้งแต่ Sprint 1–3
- ตรวจสอบความเสถียรของ Session State ในระบบ Favorites, Comparison และ Match Quiz[cite: 6, 7, 9]
- ตรวจสอบความถูกต้องของ Visualizations และ Statistics บนหน้า Statistics Page
- Refactor Code และทำความสะอาด Repository บน GitHub
- จัดทำ Final Documentation, Presentation Slide และ Live Demo Script

---

## 3. Anticipated Challenges & Prevention

- **Challenge:** Integration Regressions ระหว่างการเชื่อมโยงระบบ
- **Prevention:** รัน Automated Test Suite (`pytest`) ทุกครั้งก่อน Merge Code เข้า Main Branch

---

# 📊 Overall Project Learning Summary

| Area | Sprint 1 | Sprint 2 | Sprint 3 | Final Sprint |
|---|:---:|:---:|:---:|:---:|
| **Project Planning & DoD** | Completed | Completed | Completed | Planned |
| **Streamlit Web UI / UX**[cite: 3, 10] | Completed | Completed | Completed | Planned |
| **SQLite Database / Service Layer** | N/A | Completed | Completed | Planned |
| **Logic Engines (Quiz / Budget)**[cite: 7, 8] | Prototype | Completed | Completed | Planned |
| **Pandas & Data Analysis** | N/A | Basic | Advanced | Planned |
| **Altair Data Visualization** | N/A | N/A | Completed | Planned |
| **Automated Testing (`pytest`)** | Manual | Completed | Completed | Planned |
| **Git / GitHub Workflow** | Completed | Completed | Completed | Planned |

---

# 🧠 Final Project Reflection

> (จะสรุปบทเรียนและประสบการณ์การพัฒนาซอฟต์แวร์ของทีมภาพรวมเมื่อสิ้นสุด Final Sprint)
