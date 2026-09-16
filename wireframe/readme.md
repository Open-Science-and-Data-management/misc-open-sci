# Wireframe — Research Progress Tracking System

Wireframe ทั้งหมดของเว็บแอป แยกตามบทบาทผู้ใช้ 3 ประเภท (Researcher / Committee / Admin)
spec รายหน้า (ควรมี / ความเห็น) อยู่ที่ `wireframe-checklist.md` — ไฟล์นี้เป็นภาพรวมและวิธีใช้งานโฟลเดอร์

อ้างอิง: `docs/requirement-report.md` และ `docs/diagrams/use-case.html`

## โครงสร้าง

```
wireframe/
├── readme.md                ← ไฟล์นี้
├── wireframe-checklist.md   ← แหล่งความจริง: รายการหน้า + spec แต่ละหน้า
├── _gen_<id>.py             ← generator script (1 ไฟล์ต่อ 1 wireframe)
├── wrap.py                  ← utility แปลง elements array เปล่า ๆ เป็น scene ที่โหลดได้
└── v1/                      ← ไฟล์ .excalidraw จริง 1 ไฟล์ต่อ 1 หน้า UI
```

## หน้าทั้งหมด (11 หน้า)

| # | หน้า | Type | ไฟล์ |
|---|------|------|------|
| S1 | Login / Sign in | Shared | *(ยังไม่มีไฟล์แยกใน `v1/`)* |
| S2 | Navbar / App Shell | Shared | *(วาดรวมใน shell ของทุกหน้า ไม่มีไฟล์แยก)* |
| H1 | Home (Researcher) | Researcher | `v1/H1-home-researcher.excalidraw` |
| R1 | My Files | Researcher | `v1/R1-my-files.excalidraw` |
| R2 | Create Plan (+ AI Generate) | Researcher | `v1/R2-create-plan.excalidraw` |
| R3 | Plan Detail (Summary/Timeline/Kanban/Calendar) | Researcher | `v1/R3-plan-detail.excalidraw` |
| R4 | Task Detail (Modal + Checklist + Submit warning) | Researcher | `v1/R4-task-detail.excalidraw` |
| H2 | Home (Committee) | Committee | `v1/H2-home-committee.excalidraw` |
| C1 | Approve Plan List | Committee | `v1/C1-approve-plan-list.excalidraw` |
| C2 | Proposal Review Detail (Approve/Reject) | Committee | `v1/C2-proposal-review-detail.excalidraw` |
| A1 | Admin Home + User/Role Management | Admin | `v1/A1-admin-home-user-role.excalidraw` |

**บทบาท:** Researcher (ทำ/ส่ง plan, อัปโหลดไฟล์) · Committee + Chief (approve plan) · Admin (= Researcher + approve + จัดการ user/role, ตาม use-case `Admin --|> Researcher`)

**Flow รวม:** Login → redirect ตาม role → Researcher: H1 → R2/R3 → R4 (อัปโหลด → AI ตรวจ → Submit) · Committee: H2 → C1 → C2 (Approve/Reject)

## วิธีสร้าง/แก้ wireframe

**ห้ามเขียนไฟล์ `.excalidraw` ตรง ๆ** — สร้างผ่าน generator script เสมอ:

1. ก๊อปโครง helper จาก `_gen_h1.py` มาเป็น `_gen_<id>.py` (`base()` / `rect()` / `ell()` / `arrow()` / `text()` / `labeled()` / `add()`)
2. สคริปต์ dump scene JSON ไปที่ `v1/<ID>-<name>.excalidraw` ตรง ๆ (indent=1, ensure_ascii=False)
3. ท้ายสคริปต์มี assert: ทุก element มี `type/id/x/y/width/height` และไม่มี id ซ้ำ
4. รัน: `python3 _gen_<id>.py` (ไม่ต้องพึ่ง dependency ภายนอก)

ทุกครั้งที่เพิ่ม/แก้หน้า → อัปเดตตารางใน `wireframe-checklist.md` ด้วยเสมอ

## ธรรมเนียมการวาด

- Shell เดียวกันทุกหน้า: หน้าต่าง 1040×920 ที่ (80,90), top bar สูง 50, toggle ☰ 32×26, sidebar กว้าง 170 (bg `#f1f3f5`), เนื้อหาเริ่ม x=290
- สี: `GRAY #868e96`, `DARK #1e1e1e`, `MID #495057`, `LIGHT #adb5bd`, `MUT #757575`, `RED #c92a2a`, `PANEL #f1f3f5`, `CARD #e9ecef`
- ไอคอน placeholder = rectangle เส้นประ (`strokeStyle: dashed`)
- Annotation ท้ายหน้า: วงกลม A/B/C… + คำอธิบาย + arrow ชี้กลับไปที่ element
- fontSize ต่ำสุด 14, ชื่อหน้า `"H1 — ชื่อหน้า (wireframe v1)"` fontSize 20
