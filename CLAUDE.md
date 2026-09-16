# CLAUDE.md — Research Progress Tracking System

โปรเจกต์เอกสาร/wireframe สำหรับระบบติดตามงานวิจัย (Research Progress Tracking System)
ทุกเอกสารอ้างอิง `docs/requirement-report.md` และ use-case ที่ `docs/diagrams/use-case.html`

## โครงสร้าง

```
docs/          requirement-report.md, diagrams (use-case), ref/
wireframe/     wireframe-checklist.md (แหล่งความจริงของรายการหน้า UI ทั้งหมด)
wireframe/v1/  ไฟล์ .excalidraw จริง 1 ไฟล์ต่อ 1 หน้า UI
```

## Excalidraw Wireframe Setup

**ห้ามเขียนไฟล์ `.excalidraw` ตรง ๆ** — ทำผ่าน generator script เสมอ:

1. สร้าง `wireframe/_gen_<id>.py` (เช่น `_gen_a1.py`) โดยก๊อปโครง helper จากไฟล์ `_gen_h1.py`:
   - `base()` / `rect()` / `ell()` / `arrow()` / `text()` — สร้าง element พร้อม default fields
   - `labeled(shape, lbl, ...)` — ข้อความใน shape โดยข้อความจริงเก็บใน `lbl_text[lbl]`
   - `add(e)` — เพิ่ม element + ตรวจ id ซ้ำ
2. สคริปต์จะ dump เป็น scene JSON (`type: excalidraw`, `version: 2`, `appState.viewBackgroundColor: #ffffff`) ไปที่ `wireframe/v1/<ID>-<name>.excalidraw` ตรง ๆ (indent=1, ensure_ascii=False)
3. ท้ายสคริปต์ต้องมี assert: ทุก element มี `type/id/x/y/width/height` และไม่มี id ซ้ำ
4. รัน: `python3 _gen_<id>.py` (ใช้ python3 ธรรมดา ไม่ต้องพึ่ง dependency ภายนอก)

`wireframe/wrap.py` = utility หาต้องแปลง elements array เปล่า ๆ ให้เป็น scene ที่โหลดได้ (Obsidian Excalidraw plugin ใช้อ่านไฟล์พวกนี้)

### ธรรมเนียมการวาด (ทำตามไฟล์เดิม)

- Shell เดียวกันทุกหน้า: หน้าต่าง 1040×920 ที่ (80,90), top bar สูง 50, toggle ☰ 32×26, sidebar กว้าง 170 (bg PANEL `#f1f3f5`), เนื้อหาเริ่ม x=290
- สี: `GRAY #868e96`, `DARK #1e1e1e`, `MID #495057`, `LIGHT #adb5bd`, `MUT #757575` (ข้อความรอง), `RED #c92a2a` (overdue/error), `PANEL #f1f3f5`, `CARD #e9ecef`
- ไอคอน placeholder = rectangle เส้นประ (`strokeStyle: dashed`)
- Annotation กำกับท้ายหน้า: วงกลมตัวอักษร A/B/C… + ข้อความอธิบาย + arrow ชี้กลับไปที่ element
- fontSize ต่ำสุด 14, ชื่อหน้าบนสุดรูปแบบ `"H1 — ชื่อหน้า (wireframe v1)"` fontSize 20
- ตัวอักษรไทยใช้ได้ปกติ (ensure_ascii=False)

### เมื่อเพิ่ม/แก้หน้า

- อัปเดตตาราง checklist ใน `wireframe/wireframe-checklist.md` ด้วยเสมอ (คอลัมน์สถานะ)
- Wireframe ใหม่ควรอ่าน spec จาก checklist ก่อน — แต่ละหน้ามีหัวข้อ "ควรมี" และ "ความเห็น" ที่ตกลงกันแล้ว
- ประเด็นที่เคลียร์แล้วอยู่ท้าย checklist (Chief ไม่มี approve พิเศษ, user sign up เองด้วยอีเมลมหาลัย, commit แล้วแก้ได้แต่ต้องขอ approve ใหม่, AI tick checklist แก้ได้)

### MCP Excalidraw (https://mcp.excalidraw.com)

มี server excalidraw ผ่าน MCP ต่ออยู่ — ใช้เมื่อต้องการ**เรนเดอร์ให้ดูสดในแชท** (`create_view` / `export_to_excalidraw`)
ไม่ใช่ทางการสร้างไฟล์ใน repo (ผ่าน JSON ยักใหญ่ ไม่คุ้ม context) — ไฟล์จริงใน `wireframe/v1/` ยังสร้างด้วย generator script เหมือนเดิม
