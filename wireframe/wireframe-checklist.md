# Wireframe Checklist — Research Progress Tracking System

รายการหน้า UI ที่ต้องวาด wireframe สำหรับเว็บแอปพลิเคชัน แยกตามบทบาทผู้ใช้ 3 ประเภท
อ้างอิง: `diagrams/use-case.html`

## บทบาทผู้ใช้ (3 Types)

| Type | คือใคร | สิ่งที่ทำได้ (จาก use-case) |
|------|--------|---------------------------|
| **Researcher** | นักวิจัย | Login/Logout, View Plan, View Progress, รับ Notification, Create/Update/Delete/Commit Plan, อัปโหลดไฟล์ |
| **Committee** | คณะกรรมการ (มี Chief เป็นอีกระดับ) | Login/Logout, View Plan, View Progress, **Approve Plan** |
| **Admin** | ผู้ดูแลระบบ | ทำได้ทุกอย่างเท่า Researcher + Approve Plan + Generate Plan (inherited จาก use-case: `Admin --|> Researcher`) |

> **ความเห็น:** เนื่องจาก Admin inherit จาก Researcher ใน use-case ให้วาด UI ของ Admin เป็น "UI ของ Researcher + แถบ Approve เพิ่ม" ได้เลย **ไม่ต้องวาดแยกทุกหน้า** — ประหยัดได้หลาย wireframe โดยเพิ่มเพียง annotation ในแต่ละหน้าว่า "Admin เห็นอะไรเพิ่ม"

---

## Flow รวม (เริ่มจาก Login เสมอ)

```
Login
  ├─ (Researcher) → Home Researcher → My Files / Plan Detail / Create Plan
  │                                      └─ Task Detail (modal) → อัปโหลด → AI ตรวจ → Submit
  ├─ (Committee)  → Home Committee → Approve Plan List → Proposal Review Detail
  │                                                      └─ Approve / Reject + comment
  └─ (Admin)      → ทางเลือกของ Researcher ทั้งหมด + ทางของ Committee
```

---

## หน้าที่ใช้ร่วมกัน (Shared)

### ✅ S1. Login / Sign in
- **ทำอะไร:** ยืนยันตัวตน แล้ว redirect ไป Home ตาม role
- **ควรมี:**
  - ช่อง email/username + password, ปุ่ม Sign in
  - (ถ้ามี) ปุ่ม login ผ่านบัญชีมหาวิทยาลัย / SSO
  - Error state: รหัสผ่านผิด, ไม่มีสิทธิ์
- **Flow:** Login → ระบบเช็ก role → `Researcher → H1`, `Committee → H2`, `Admin → H1 (โหมด admin)`
- **ความเห็น:** แอปภายในมหาลัยน่าจะใช้ SSO/LDAP อยู่แล้ว — ถ้าใช่ ให้วาด wireframe แบบ 1 ปุ่มกด + fallback form ก็พอ ไม่ต้องออกแบบ register (สร้าง user โดย Admin หรือ sync จากระบบกลาง)

### ✅ S2. Navbar / App Shell (วาดครั้งเดียว)
- **ทำอะไร:** โครงหน้าทุกจอ — ไม่ใช่หน้าเอกสาร แต่ควรวาดก่อนหน้าอื่น
- **ทรง shell ที่ตกลงกัน (จาก human review, 2026-09-16):** top bar ด้านบน (โลโก้, แท็บเมนูตาม role, bell, profile/Logout) + **ปุ่ม toggle ☰ เปิด/ปิด sidebar ด้านซ้าย** — sidebar เป็น shortcut ไปหน้าอื่น ๆ
- **ควรมี:** โลโก้, เมนูหลัก (เปลี่ยนตาม role), notification bell, โปรไฟล์/Logout
- **เมนูตาม role:**
  - Researcher: Home, My Files, Plans
  - Committee: Home, Approve Plans
  - Admin: ของ Researcher + Approve Plans (+ จัดการ user ถ้ามี)
- **ความเห็น:** Notification ควรเป็น dropdown ใน navbar ไม่ใช่หน้าแยก (use-case มี `GetNotification` ครอบคลุมแล้ว) — ลดจำนวนหน้าลง 1

---

## Type 1: Researcher

### ✅ H1. Home (Researcher)
- **ทำอะไร:** Dashboard ภาพรวมงานของตัวเอง ให้เห็นว่า "ต้องทำอะไรต่อ" ภายใน 5 วินาที
- **ควรมี:**
  - การ์ดสรุป: จำนวน proposal ของฉัน, task ที่ค้าง, task ใกล้ครบกำหนด
  - ลิสต์ "Task ที่ต้องทำเร็ว ๆ นี้" (เรียงตาม due date) กดเข้า Task Detail ได้
  - Notification ล่าสุด 3–5 รายการ
  - ปุ่ม prominent: **+ Create Plan**
- **Flow:** Login → มาที่นี่ → กด task → Task Detail (R4) หรือกด Create Plan (R2)
- **ความเห็น:** อย่าให้หน้าแรกฉลุยทุกอย่าง — หัวใจคือ "กิจกรรมที่รออยู่ของฉัน" ส่วนภาพรวมทั้ง proposal ให้อยู่ในหน้า Plan Detail ซึ่งมี view หลายแบบอยู่แล้ว

### ✅ R1. My Files
- **ทำอะไร:** แสดงไฟล์ทั้งหมดที่ตัวเองเคยอัปโหลด
- **ควรมี:**
  - ตาราง/ลิสต์: ชื่อไฟล์, ขนาด, วันที่อัปโหลด, **ผูกกับ task/proposal ไหน**, สถานะการตรวจของ AI (✅ ครบ / ⚠️ ไม่ครบ / ⏳ กำลังตรวจ)
  - Filter ตาม proposal, search
  - ปุ่ม preview/download
- **Flow:** อัปโหลดจาก Task Detail → ไฟล์มาโผล่ที่นี่ / มาหน้านี้เพื่อเช็กย้อนหลังว่าอัปโหลดอะไรไปแล้ว
- **ความเห็น:** สถานะ "ผลตรวจของ AI" คือคอลัมน์ที่มีค่าที่สุดของหน้านี้ — ถ้า user ต้องกดเข้าไปทีละ task เพื่อดูว่าไฟล์ถูกตรวจแล้วหรือยัง หน้านี้จะไร้ประโยชน์

### ✅ R2. Create Plan
- **ทำอะไร:** อัปโหลด Proposal → ให้ AI Generate Plan → ตรวจ/แก้ → บันทึก (use-case: `CreatePlan include GeneratePlan`)
- **ควรมี (แบ่งเป็น 3 สเต็ปในหน้าเดียว หรือ wizard):**
  1. **Upload:** dropzone อัปโหลด proposal (PDF/docx)
  2. **Generating:** progress/ล้อหมุน + ข้อความ "AI กำลังวิเคราะห์ proposal…" (state นี้ห้ามลืม — ใช้เวลานาน)
  3. **Review:** task ที่ AI generate มา แสดงเป็นลิสต์ที่ **แก้ไขได้** (เพิ่ม/ลบ/แก้ชื่อ task), ปุ่ม Save / Regenerate
- **Flow:** Create Plan → upload → AI generate → ตรวจแก้ → Save → ไป Plan Detail (R3)
- **ความเห็น:** จุดชี้ขาดของ UX คือขั้น Review — อย่าให้ผล AI ล็อกเป็นสุดยอดความจริง นักวิจัยต้องแก้ได้ก่อน commit ไม่งั้นจะไม่มีใครเชื่อใจฟีเจอร์นี้

### ✅ R3. Plan Detail (Task Overview)
- **ทำอะไร:** แสดง task ทั้งหมดใน proposal หนึ่ง ๆ เลือกดูได้ 4 มุมมอง
- **ควรมี:**
  - หัวหน้า: ชื่อ proposal, สถานะ (Draft / Committed / Approved), ปุ่ม **Commit Plan**
  - **View switcher 4 แบบ:**
    - **Summary** — สรุป % ความคืบหน้า, task แยกตามสถานะ
    - **Timeline** — Gantt-lite แนวเวลา
    - **Kanban** — คอลัมน์ To do / In progress / Done
    - **Calendar** — task กระจายตามปฏิทินเดือน
  - กด task แต่ละอัน → เปิด Task Detail (R4)
- **Flow:** Home / Create Plan → หน้านี้ → กด task → Task Detail (R4)
- **ความเห็น:** วาดเป็น **wireframe เดียว มี 4 mockup ของเฉพาะพื้นที่เนื้อหา** พอ ไม่ต้องวาด 4 หน้าเต็ม (โครงหน้า + header เหมือนกันหมด) ใน 4 view นี้ Kanban กับ Calendar สร้างงานเยอะสุดตอน implement — ถ้าต้องการคุม scope แนะนำทำ Summary + Timeline ก่อน แล้วค่อยเพิ่ม (แจ้งผู้ใช้ได้เลยว่าเป็น phase 2)

### ✅ R4. Task Detail (Modal / Pop-up)
- **ทำอะไร:** รายละเอียด task หนึ่ง ๆ + วงจร "อัปโหลด → AI ตรวจ → ส่ง"
- **ควรมี:**
  - ชื่อ task, due date, สถานะ
  - **Description ที่ AI generate:** task นี้ต้องทำ/อัปโหลดอะไรบ้าง
  - **Subtask checklist** (AI สร้าง): แต่ละข้อมี checkbox — AI ตรวจไฟล์แล้ว **tick ให้เอง** เมื่อเอกสารที่อัปโหลดมีของครบ
  - โซนอัปโหลดไฟล์ + ลิสต์ไฟล์ที่อัปโหลดแล้ว
  - ผลตรวจของ AI: ข้อไหนครบ/ข้อไหนขาด (ข้อขาด highlight สีเหลือง/แดง)
  - ปุ่ม **Submit** — ถ้า checklist ยังไม่ครบ แสดง **warning "ยังขาดรายการ X, Y — ยืนยันส่งหรือไม่?"** แต่ยังส่งได้
- **Flow:** อัปโหลดไฟล์ → AI ตรวจ → checklist อัปเดต → Submit (มี/ไม่มี warning) → กลับ Plan Detail สถานะ task เปลี่ยน
- **ความเห็น:**
  - ต้องระบุใน wireframe ให้ชัดว่า AI tick นั้นเป็น **คำแนะนำ ไม่ใช่คำตัดสิน** — ควรให้ user ยกเลิก tick ของ AI ได้ (AI เดาผิดได้) ไม่งั้นจะเกิดกรณี "ไฟล์จริงมีครบแต่ AI บอกไม่ครบ" แล้ว user ตัน
  - Warning ตอน Submit ไม่ครบ: ให้เป็น dialog ยืนยัน ไม่ใช่ block — ตรงกับสเปกที่บอกว่า "ยังไม่ครบก็ส่งได้"

---

## Type 2: Committee

### ✅ H2. Home (Committee)
- **ทำอะไร:** Dashboard ของกรรมการ — เห็นงานที่รอตัดสิน
- **ควรมี:**
  - สรุป: รอ approve กี่รายการ, approve ไปแล้วกี่รายการ, อายุของรายการที่รอนานสุด
  - ลิสต์ "รอพิจารณา" สั้น ๆ (กดเข้า Proposal Review ได้เลย)
  - กิจกรรมล่าสุด (researcher คนไหน submit อะไรเมื่อไหร่)
- **Flow:** Login → มาที่นี่ → กดรายการ → Proposal Review Detail (C2)
- **ความเห็น:** สามารถรวม Home Committee กับ Approve Plan List (C1) เป็นหน้าเดียวได้ ถ้าอยากลดจำนวนหน้า — แต่แยกไว้ก็ดี เพราะ Home ให้บริบท "งานเยอะแค่ไหน" ส่วน List คือเครื่องมือทำงานจริง

### ✅ C1. Approve Plan List
- **ทำอะไร:** ลิสต์ proposal ทั้งหมดที่กรรมการต้องพิจารณา
- **ควรมี:**
  - ตาราง: ชื่อ proposal, ชื่อผู้ส่ง (researcher), วันที่ส่ง, สถานะ (รอพิจารณา / อนุมัติแล้ว / ถูกปฏิเสธ), progress %
  - Filter ตามสถานะ, sort ตามวันที่ส่ง
  - Badge แยกสีตามสถานะ, แถวที่รอนานเกินไปเน้นพิเศษ
- **Flow:** Login / Home Committee → หน้านี้ → กดแถว → Proposal Review Detail (C2)
- **ความเห็น:** default view ควรกรอง "รอพิจารณา" ไว้ก่อน — กรรมการส่วนใหญ่เข้ามาเพื่องานค้าง ไม่ใช่ไปไล่ดูของเก่า

### ✅ C2. Proposal Review Detail
- **ทำอะไร:** ดูรายละเอียด proposal + ตัดสิน approve/reject — layout คล้าย Task Detail แต่เป็นระดับโปรเจกต์
- **ควรมี:**
  - ข้อมูล proposal: ชื่อ, ผู้เสนอ, วันที่, ไฟล์ proposal ต้นฉบับ (preview/download)
  - Plan ที่ AI generate: task ทั้งหมด + ความคืบหน้าแต่ละ task (มุมมองเดียวพอ — แนะนำ Summary, ไม่ต้องมี 4 view แบบฝั่ง researcher)
  - Checklist สถานะต่อ task (ครบ/ไม่ครบ/ส่งช้า)
  - กล่อง comment
  - **ปุ่มตัดสิน: Approve / Reject (+ ต้องใส่ comment เมื่อ reject)**
  - ประวัติการพิจารณาก่อนหน้า (ถ้าเคยถูก reject แล้วแก้ใหม่)
- **Flow:** Approve Plan List → หน้านี้ → Approve/Reject → กลับ List, สถานะเปลี่ยน, researcher ได้รับ notification
- **ความเห็น:**
  - วาดจาก **layout เดียวกับ R4** ให้ได้มากที่สุด — ต่างกันที่เนื้อหาเป็นระดับโปรเจกต์ + ปุ่มตัดสิน ทำให้ design system ซ้ำกัน ลดงาน implement
  - Reject ที่บังคับใส่ comment เป็นเรื่องสำคัญ — researcher ต้องรู้ว่าต้องแก้อะไร ไม่งั้นวงจร reject→แก้→ส่งใหม่จะวนไม่รู้จบ
  - เรื่อง **Chief**: use-case มี `Chief --|> Committee` — ถ้า Chief มีอำนาจพิเศษ (เช่น final approve หลังกรรมการทั่วไปเห็นชอบ) ต้องเพิ่ม state ในหน้านี้ แนะนำให้เคลียร์สเปกข้อนี้ก่อนวาด

---

## Type 3: Admin

> **ความเห็นรวม:** ตาม use-case (`Admin --|> Researcher`) Admin ใช้ UI ของ Researcher ได้ทั้งหมด + เข้าถึงงานฝั่ง Committee ได้ ไม่ต้องออกแบบหน้าแยกเต็มรูปแบบ

### ✅ A1. Admin Home / User & Role Management *(เดิมชื่อ Home Admin)*
- **ทำอะไร:** ภาพรวมระบบ + จัดการผู้ใช้
- **ควรมี:**
  - สถิติระบบ: จำนวน researcher, committee, proposal ทั้งหมด, plan ที่รอ approve
  - ตารางจัดการ user: สร้าง/แก้ไข user, **กำหนด role** (Researcher / Committee / Chief / Admin), เปิด-ปิดการใช้งาน
  - ปุ่ม switch เข้าโหมดดูแบบ Researcher/Committee (หรือแค่เห็นเมนูทุกอันใน navbar)
- **Flow:** Login (role = admin) → หน้านี้ → จัดการ user หรือกดเข้าไปดู proposal ของใครก็ได้
- **ความเห็น:** การกำหนด role ต่อ user คือฟีเจอร์เดียวที่ **จำเป็น** ต้องออกแบบสำหรับ Admin — ส่วน "ดูได้ทุก proposal" มาฟรีจากการให้สิทธิ์ Committee ในตัว อย่าออกแบบหน้า admin แยกซ้ำซ้อนกับหน้าธรรมดา

---

## Checklist รวม (ติ๊กเมื่อวาดเสร็จ)

| # | หน้า | Type | สถานะ |
|---|------|------|-------|
| S1 | Login / Sign in | Shared | ✅ |
| S2 | Navbar / App Shell | Shared | ✅ |
| H1 | Home (Researcher) | Researcher | ✅ |
| R1 | My Files | Researcher | ✅ |
| R2 | Create Plan (+ AI Generate) | Researcher | ✅ |
| R3 | Plan Detail (Summary/Timeline/Kanban/Calendar) | Researcher | ✅ |
| R4 | Task Detail (Modal + Checklist + Submit warning) | Researcher | ✅ |
| H2 | Home (Committee) | Committee | ✅ |
| C1 | Approve Plan List | Committee | ✅ |
| C2 | Proposal Review Detail (Approve/Reject) | Committee | ✅ |
| A1 | Admin Home + User/Role Management | Admin | ☐ |

**รวม 11 wireframe** (เทียบกับ 10 ก่อนหน้า: แยก Navbar ออกมาชัดเจน + เพิ่ม Admin Home)

---

## ประเด็นที่เคลียร์แล้ว (2026-09-16)

1. **บทบาทของ Chief** → แค่กรรมการอาวุโส ไม่มีขั้นตอน approve พิเศษ — C2 ไม่ต้องมี state พิเศษ
2. **User มาจากไหน** → user **sign up เองด้วยอีเมลมหาลัย** (ไม่ใช่ SSO, ไม่ใช่ Admin สร้าง) — S1 ต้องมี flow Sign up, A1 จัดการ role ของ user ที่ sign up แล้ว
3. **Commit Plan** → แก้ได้หลัง commit แต่ **ต้องขอ approve ใหม่** (สถานะกลับเป็นรอพิจารณา) — R3/C1 ต้องมีสถานะ "รอ approve ใหม่" หรือกลับไป Draft→Committed ได้
4. **AI tick checklist** → user **แก้/ยกเลิก tick ของ AI ได้** — R4 แสดง tick เป็นคำแนะนำ
