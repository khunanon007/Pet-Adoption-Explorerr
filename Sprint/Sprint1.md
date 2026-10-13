# 🐱 Pet Adoption Explorer — Sprint 1 Report

## Final Term Project — CP352301 Script Programming

Sprint: Sprint 1 — Application Foundation & Web Prototyping
Period: Week 12
Presentation: 15–16 September 2026
Due Date: 18 September 2026
Status: Completed

Repository: https://github.com/khunanon007/Pet-Adoption-Explorerr/edit/main/Sprint/Sprint1.md
Pull Request: https://github.com/khunanon007/Pet-Adoption-Explorerr/edit/main/Sprint/Sprint1.md

---

1. Sprint Overview

Sprint 1 เป็น Sprint แรกของโปรเจกต์ Pet Adoption Explorer (ระบบศูนย์รวมสัตว์เลี้ยงตามหาบ้านใหม่)[cite: 1] มีเป้าหมายเพื่อสร้างโครงสร้างพื้นฐาน (Foundation) ของแอปพลิเคชัน พัฒนาการเชื่อมต่อเมนูหลัก และสร้าง Prototype ส่วนต่อประสานผู้ใช้ (User Interface) บน Streamlit เพื่อทดสอบฟังก์ชันการทำงานหลักก่อนนำไปเชื่อมต่อระบบฐานข้อมูลจริงใน Sprint ถัดไป

ใน Sprint นี้ ทีมพัฒนาได้สร้าง Web UI ที่ครอบคลุมฟังก์ชันการทำงานพื้นฐาน เช่น Navigation Menu[cite: 1], การแสดงรายการสัตว์เลี้ยง[cite: 4], การกรองตามหมวดหมู่[cite: 2], ระบบค้นหา[cite: 5], ระบบเปรียบเทียบสัตว์เลี้ยง[cite: 6], แบบทดสอบ Match Quiz[cite: 7], เครื่องคำนวณงบประมาณ (Budget Calculator)[cite: 8] และระบบ Favorites[cite: 9] โดยใช้ Local Sample Dataset ในการทดสอบ[cite: 3, 4]

---

2. Sprint Goal

> สร้าง Web Application Foundation ของ Pet Adoption Explorer บน Streamlit ที่สามารถแสดงข้อมูลสัตว์เลี้ยง กรองหมวดหมู่ ค้นหา เปรียบเทียบ คำนวณงบประมาณ ทำแบบทดสอบแมตช์ไลฟ์สไตล์ และจัดการ Favorite ได้อย่างปลอดภัยและมีประสิทธิภาพ

เมื่อจบ Sprint 1 ระบบสามารถ:
- เริ่มต้น Web Application ผ่าน Streamlit ได้อย่างถูกต้อง[cite: 3, 10]
- แสดง แบนเนอร์ต้อนรับ (Hero Banner) และนำเสนอระบบ[cite: 1]
- สลับหน้าการทำงานผ่าน Top Navigation Bar ได้ครบถ้วน 6 เมนูหลัก[cite: 1]
- กรองสัตว์เลี้ยงตามประเภท (Dogs, Cats, Rabbits, Rodents, Birds)[cite: 2]
- ค้นหาสัตว์เลี้ยงแบบ Partial Match และ Case-insensitive[cite: 5]
- แสดงสัตว์เลี้ยงโดดเด่นประจำวัน (Pet of the Day)[cite: 3]
- เปรียบเทียบข้อมูลสัตว์เลี้ยง 2–3 ตัวพร้อมกัน[cite: 6]
- ทำแบบทดสอบ Match Quiz เพื่อประเมินสัตว์เลี้ยงที่เหมาะสม[cite: 7]
- คำนวณประมาณการค่าใช้จ่ายแรกรับและค่าเลี้ยงดูรายเดือน (Budget Calc)[cite: 8]
- แสดงหน้าบันทึกสัตว์เลี้ยงที่ชอบ (Favorites)[cite: 9]

---bers & Roles


3. Team Mem
- ฟีฟ่า (Role: Planner) - หน้าที่หลัก: Planning, Requirements, Scope และ Documentation
- โดนัท (Role: Coder) - หน้าที่หลัก: Web Application Development (Streamlit) & Logic Implementation
- ภีม (Role: Debugger) - หน้าที่หลัก: Testing UI/UX, Edge Cases Handling & QA Verification

---

4. Sprint 1 Scope

In Scope:
- Web UI Interactive Prototype พัฒนาด้วย Streamlit[cite: 3, 10]
- Top Navigation Menu: Home, Explore, Compare, Match Quiz, Budget Calc, Favorites, Admin[cite: 1]
- Filter & Category Selection (All, Dogs, Cats, Rabbits, Rodents, Birds)[cite: 2]
- Pet of the Day Highlight[cite: 3]
- Search Function (Name / Breed Search)[cite: 5]
- Pet Comparison Tool (2–3 Pets)[cite: 6]
- Lifestyle Match Quiz (4 Questions Logic)[cite: 7]
- Budget Calculation & Cost Timeline Slider[cite: 8]
- Favorites Empty/Saved State[cite: 9]
- Local Sample Dataset (JSON/Dictionary)[cite: 3, 4]

Out of Scope:
- Real Database Integration (SQLite / PostgreSQL) (จะพัฒนาใน Sprint 2)
- User Authentication & Real Admin Management Backend
- Real Pet Adoption Application Submission System
- External API Integration / Cloud Storage for Images
- Automated Testing & CI/CD Pipeline

---

5. Sprint 1 Functional Requirements

- FR-01 — Navigation Bar: มีเมนูส่วนบนที่เลือกสลับหน้าได้ง่าย[cite: 1]
- FR-02 — Category Filter: เลือกสลับหมวดหมู่เพื่อกรองข้อมูลสัตว์เลี้ยงได้[cite: 2]
- FR-03 — Pet Highlight (Pet of the Day): แสดงข้อมูลสัตว์เลี้ยงแนะนำประจำวันพร้อมรายละเอียด เช่น สายพันธุ์, ค่าใช้จ่าย, ลักษณะที่พัก[cite: 3]
- FR-04 — Search System: ค้นหาตามชื่อหรือสายพันธุ์แบบ Case-insensitive[cite: 5]
- FR-05 — Comparison Tool: เลือกสัตว์เลี้ยงมาเปรียบเทียบคุณสมบัติต่างๆ ได้ 2–3 ตัว[cite: 6]
- FR-06 — Match Quiz: รับ Input ไลฟ์สไตล์ 4 ข้อ เพื่อวิเคราะห์ผลลัพธ์สัตว์เลี้ยงที่เหมาะสม[cite: 7]
- FR-07 — Budget Calculator: คำนวณงบประมาณแรกรับ + ค่าเลี้ยงดูรายเดือน ตามระยะเวลาที่กำหนด[cite: 8]
- FR-08 — Favorites System: จัดเก็บและแสดงสัตว์เลี้ยงที่ผู้ใช้กดบันทึก[cite: 9]

---

6. Local Sample Dataset

ข้อมูลตัวอย่างที่ใช้ในการทดสอบระบบใน Sprint 1[cite: 3, 4, 6]:

- โบบา (Boba)[cite: 3]: สายพันธุ์ French Bulldog[cite: 3] | ประเภท Dog[cite: 3] | สถานที่ Bangkok[cite: 3] | อายุ 2 ปี[cite: 3] | ที่พักที่เหมาะ Condo[cite: 3] | ค่าเลี้ยงดู/เดือน ~1,600 บาท[cite: 3]
- คุกกี้ (Cookie)[cite: 4]: สายพันธุ์ Chihuahua[cite: 4] | ประเภท Dog[cite: 4] | สถานที่ Nonthaburi[cite: 4] | อายุ 1 ปี[cite: 4] | ที่พักที่เหมาะ Condo[cite: 4] | ค่าเลี้ยงดู/เดือน ~900 บาท[cite: 4]
- ไมโล (Milo)[cite: 6]: สายพันธุ์ Golden Retriever[cite: 6] | ประเภท Dog[cite: 6] | สถานที่ Bangkok | อายุ 1.5 ปี | ที่พักที่เหมาะ House | ค่าเลี้ยงดู/เดือน ~2,800 บาท[cite: 8]
- ส้มจี๊ด: สายพันธุ์ Persian | ประเภท Cat | สถานที่ Bangkok | อายุ 2 ปี | ที่พักที่เหมาะ Condo / House | ค่าเลี้ยงดู/เดือน ~1,200 บาท

---

7. Application Architecture & Flow

User Navigation (Web Browser)
        ↓
Streamlit UI Controller
        ↓
Home | Explore | Compare | Match Quiz | Budget Calc | Favorites
        ↓
Local Sample Dataset (Memory / Session State)
        ↓
Render Component / Dynamic Calculation

---

8. Main Functions / Modules

- render_header_nav(): แสดงเมนู Navigation ด้านบน[cite: 1]
- render_home_page(): แสดง Hero Banner, Categories และ Pet of the Day[cite: 1, 2, 3]
- render_explore_page(): แสดงช่องค้นหาและการ์ดสัตว์เลี้ยงทั้งหมด[cite: 4, 5]
- render_compare_page(): แสดงส่วนเลือกและเปรียบเทียบสัตว์เลี้ยง 2-3 ตัว[cite: 6]
- render_match_quiz_page(): รับค่าตอบแบบสอบถาม 4 ข้อ และประมวลผล[cite: 7]
- render_budget_calc_page(): คำนวณค่าใช้จ่ายแรกรับ + รายเดือนย้อนหลัง/ล่วงหน้า[cite: 8]
- render_favorites_page(): แสดงรายการสัตว์เลี้ยงที่กด Save ไว้[cite: 9]

---

9. Daily Task Allocation & Update (10–15 Sep 2026)

- 10 ก.ย. 2569:
  * Planner (ฟีฟ่า): กำหนด Goal, Scope และ Requirements
  * Coder (โดนัท): วางโครงสร้างโปรเจกต์ Streamlit
  * Debugger (ภีม): กำหนด Test Cases สำหรับ UI & State
  * Update: เริ่มต้นโปรเจกต์ Pet Adoption Explorer

- 11 ก.ย. 2569:
  * Planner (ฟีฟ่า): ออกแบบ UI Wireframe & Navigation
  * Coder (โดนัท): พัฒนา Layout, Top Menu และ Home Page[cite: 1]
  * Debugger (ภีม): ทดสอบการเปลี่ยนหน้า UI บน Streamlit[cite: 1]
  * Update: ได้หน้า Home และ Navigation หลัก[cite: 1]

- 12 ก.ย. 2569:
  * Planner (ฟีฟ่า): ออกแบบโครงสร้าง Sample Dataset[cite: 3, 4]
  * Coder (โดนัท): พัฒนา Explore Page และระบบ Search[cite: 5]
  * Debugger (ภีม): ทดสอบการกรอง Category & Search[cite: 2, 5]
  * Update: ค้นหาและกรองประเภทสัตว์เลี้ยงได้[cite: 2, 5]

- 13 ก.ย. 2569:
  * Planner (ฟีฟ่า): ออกแบบ Quiz Logic & Budget Calculation[cite: 7, 8]
  * Coder (โดนัท): พัฒนา Compare, Match Quiz และ Budget Calc[cite: 6, 7, 8]
  * Debugger (ภีม): ทดสอบ Logic การคำนวณงบและ Quiz[cite: 7, 8]
  * Update: ฟังก์ชัน Compare/Quiz/Budget ทำงานได้[cite: 6, 7, 8]

- 14 ก.ย. 2569:
  * Planner (ฟีฟ่า): ตรวจสอบ DoD และเรียบเรียง เอกสาร
  * Coder (โดนัท): พัฒนาหน้า Favorites และปรับแต่ง CSS/Style[cite: 9]
  * Debugger (ภีม): ทดสอบ Session State และ Edge Cases[cite: 9]
  * Update: ระบบทำงานครบตาม Scope[cite: 1]

- 15 ก.ย. 2569:
  * Planner (ฟีฟ่า): สรุปผล Sprint 1 Report & Pitch
  * Coder (โดนัท): Refactor Code และตรวจสอบความเรียบร้อย
  * Debugger (ภีม): สรุปผล QA Pass Rate 100%
  * Update: เตรียมนำเสนอและส่งมอบ Sprint 1

---

10. QA Test Cases & Results

Sprint 1 มี Test Cases ทั้งหมด 12 Cases บน Web UI[cite: 1, 4, 5, 6, 7, 8, 9]

1. Navigation Bar Switch[cite: 1]: สามารถสลับไปยังหน้าต่างๆ ได้ถูกต้อง ไม่เกิด Error[cite: 1] | Status: PASS
2. Category Filter Click[cite: 2]: แสดงสัตว์เลี้ยงเฉพาะประเภทที่เลือก[cite: 2] | Status: PASS
3. Pet of the Day Display[cite: 3]: แสดงข้อมูลและ Tag สัตว์เลี้ยงโดดเด่นถูกต้อง[cite: 3] | Status: PASS
4. Search Game/Pet (Partial Match)[cite: 5]: พิมพ์ "Cookie" หรือ "คุกกี้" แล้วพบผลลัพธ์ถูกต้อง[cite: 4, 5] | Status: PASS
5. Search Case-Insensitive[cite: 5]: พิมพ์ "boba" หรือ "Boba" ได้ผลลัพธ์เดียวกัน[cite: 3, 5] | Status: PASS
6. Search Not Found[cite: 5]: แสดงข้อความแจ้งเมื่อไม่พบข้อมูล[cite: 5] | Status: PASS
7. Compare Selected Pets[cite: 6]: เลือกเปรียบเทียบ 2–3 ตัวแล้วแสดงการ์ดขนานกัน[cite: 6] | Status: PASS
8. Match Quiz Submit[cite: 7]: เลือกคำตอบครบ 4 ข้อ แล้วคำนวณสัตว์เลี้ยงที่เหมาะได้[cite: 7] | Status: PASS
9. Budget Calculation Slider[cite: 8]: เลื่อนระยะเวลา (1-36 เดือน) ค่าใช้จ่ายรวมคำนวณอัปเดตทันที[cite: 8] | Status: PASS
10. Favorites Empty State[cite: 9]: แสดงข้อความแจ้งเตือนเมื่อยังไม่ได้กด Save[cite: 9] | Status: PASS
11. Responsive Layout: Layout ไม่เบี้ยวเมื่อปรับขนาดหน้าจอ Browser | Status: PASS
12. App Rerun / State Persistence: แอปไม่ Crash เมื่อมีการเปลี่ยนค่าใน Input Widgets | Status: PASS

QA Summary:
- Total Test Cases: 12
- Passed: 12 (100%)
- Failed: 0
- Critical Bugs: 0

---

11. Contribution Matrix — Member Performance

- คิม (Planner): Project Planning, Requirements, Documentation, UI Design | คะแนน: 50/50
- ฟลุ๊ค (Coder): Streamlit UI Development, Navigation, Search, Calc Logic | คะแนน: 50/50
- ออม (Debugger): UI/UX QA, Logic Verification, Edge Case & State Testing | คะแนน: 50/50

Total Team Score = 150/150
Team Completion = 100%

---

12. Definition of Done (DoD) Checklists

- [x] Web Application รันบน Streamlit ได้สำเร็จโดยไม่เกิด Crash[cite: 3, 10]
- [x] เมนู Navigation ทั้งหมด (Home, Explore, Compare, Match Quiz, Budget Calc, Favorites) ทำงานได้[cite: 1]
- [x] ระบบกรองหมวดหมู่และค้นหารองรับ Partial/Case-insensitive search[cite: 2, 5]
- [x] ระบบ Match Quiz และ เครื่องคำนวณงบประมาณ ประมวลผลถูกต้อง[cite: 7, 8]
- [x] QA Test Cases ผ่าน 100%
- [x] ซอร์สโค้ดและโครงสร้างโปรเจกต์จัดเก็บอยู่บน GitHub Repository
- [x] เอกสาร Sprint 1 Report ครบถ้วนพร้อมนำเสนอ

---

13. Wow! & Whoops!

Wow! (สิ่งที่ทำได้ดี):
1. Interactive UI with Streamlit: สามารถแปลงไอเดียให้กลายเป็น Web Dashboard ที่ใช้งานง่าย น่ารัก และโต้ตอบได้รวดเร็ว[cite: 1, 3]
2. Comprehensive Features: พัฒนาฟังก์ชันตอบโจทย์ผู้รับเลี้ยงได้ครบถ้วน ทั้งการค้นหา เปรียบเทียบ คํานวณงบ และทำแบบทดสอบ[cite: 5, 6, 7, 8]

Whoops! (ปัญหาและการแก้ไข):
- Problem: การเปลี่ยนหน้าใน Streamlit ช่วงแรกทำให้ Session State หรือค่าที่กรอกไว้ใน Quiz หลุด
- Solution: ปรับการจัดการ State โดยใช้ st.session_state ในการเก็บข้อมูลข้ามหน้าเมนู ทำให้ข้อมูลคงอยู่และไม่เกิด Error[cite: 9]

---

14. Sprint 1 Final Status

===================================================
   PET ADOPTION EXPLORER — SPRINT 1 COMPLETED
===================================================

Next Step: วางแผน Sprint 2 เพื่อเชื่อมต่อระบบกับ Database จริง (SQLite) และพัฒนาส่วนจัดการข้อมูลสัตว์เลี้ยงสำหรับผู้ดูแลระบบ (Admin)
