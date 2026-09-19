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