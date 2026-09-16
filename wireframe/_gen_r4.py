# R4 — Task Detail (Modal + Checklist + Submit warning)
# modal เปิดจากการกด task ใน R3 = งานส่งรายสัปดาห์, AI checklist ระบุสิ่งที่ PDF ต้องมี
import json

def base(e, seed):
    d = {"angle":0,"backgroundColor":"transparent","fillStyle":"solid","strokeWidth":2,
         "strokeStyle":"solid","roughness":1,"opacity":100,"groupIds":[],"frameId":None,
         "roundness":None,"seed":seed,"version":1,"versionNonce":seed,"isDeleted":False,
         "boundElements":None,"updated":1,"link":None,"locked":False}
    d.update(e)
    return d

raw = [
{"type":"text","id":"t0","x":600,"y":30,"text":"R4 — Task Detail (Modal)","fontSize":28},
{"type":"rectangle","id":"bg","x":40,"y":110,"width":560,"height":560,"backgroundColor":"#f1f3f5","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1,"opacity":60},
{"type":"text","id":"bgt","x":60,"y":122,"text":"(Plan Detail R3 — modal เปิดทับหน้านี้)","fontSize":14,"strokeColor":"#757575","opacity":60},
{"type":"rectangle","id":"bgr1","x":60,"y":160,"width":520,"height":30,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#adb5bd","strokeWidth":1,"opacity":60},
{"type":"rectangle","id":"bgr2","x":60,"y":200,"width":520,"height":30,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#adb5bd","strokeWidth":1,"opacity":60},
{"type":"rectangle","id":"bgr3","x":60,"y":240,"width":520,"height":30,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#4a9eed","strokeWidth":2},
{"type":"text","id":"bgr3t","x":72,"y":248,"text":"Task สัปดาห์ที่ 3 — รายงานความคืบหน้า","fontSize":14},

{"type":"rectangle","id":"md","x":660,"y":100,"width":700,"height":780,"backgroundColor":"#ffffff","fillStyle":"solid","strokeWidth":2},
{"type":"rectangle","id":"mhead","x":660,"y":100,"width":700,"height":50,"backgroundColor":"#f1f3f5","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"text","id":"mt","x":676,"y":114,"text":"Task: รายงานความคืบหน้า — สัปดาห์ที่ 3","fontSize":18},
{"type":"text","id":"mx","x":1322,"y":106,"text":"x","fontSize":20,"strokeColor":"#495057"},
{"type":"text","id":"mmeta","x":676,"y":160,"text":"Due: 20 ก.ย. 2026 · งานส่งประจำสัปดาห์","fontSize":14,"strokeColor":"#757575"},
{"type":"rectangle","id":"mchip","x":1240,"y":156,"width":100,"height":22,"backgroundColor":"#ffd8a8","fillStyle":"solid","strokeWidth":1,"label":{"text":"In progress","fontSize":14}},

{"type":"rectangle","id":"desc","x":676,"y":192,"width":668,"height":66,"backgroundColor":"#fff3bf","fillStyle":"solid","strokeColor":"#f59e0b","strokeWidth":1},
{"type":"text","id":"dt1","x":690,"y":200,"text":"Description (AI generate):","fontSize":14},
{"type":"text","id":"dt2","x":690,"y":222,"text":"งานส่งรายสัปดาห์ — อัปโหลด PDF สรุปความคืบหน้า ไฟล์ต้องมีรายการด้านล่างครบ","fontSize":14},
{"type":"text","id":"clh","x":676,"y":272,"text":"Subtask checklist (AI สร้าง) — สิ่งที่ PDF สัปดาห์นี้ต้องมี:","fontSize":14,"strokeColor":"#495057"},

{"type":"rectangle","id":"cr1","x":676,"y":300,"width":668,"height":44,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"rectangle","id":"cb1","x":688,"y":314,"width":16,"height":16,"backgroundColor":"#b2f2bb","fillStyle":"solid","strokeColor":"#22c55e","strokeWidth":1},
{"type":"text","id":"tk1","x":688,"y":312,"text":"✓","fontSize":16,"strokeColor":"#15803d"},
{"type":"text","id":"ct1","x":714,"y":314,"text":"สรุปความคืบหน้าประจำสัปดาห์","fontSize":14},
{"type":"text","id":"tg1","x":1252,"y":314,"text":"AI tick","fontSize":14,"strokeColor":"#757575"},

{"type":"rectangle","id":"cr2","x":676,"y":352,"width":668,"height":44,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"rectangle","id":"cb2","x":688,"y":366,"width":16,"height":16,"backgroundColor":"#b2f2bb","fillStyle":"solid","strokeColor":"#22c55e","strokeWidth":1},
{"type":"text","id":"tk2","x":688,"y":364,"text":"✓","fontSize":16,"strokeColor":"#15803d"},
{"type":"text","id":"ct2","x":714,"y":366,"text":"ตาราง Gantt เทียบแผน vs ผลจริง","fontSize":14},
{"type":"text","id":"tg2","x":1252,"y":366,"text":"AI tick","fontSize":14,"strokeColor":"#757575"},

{"type":"rectangle","id":"cr3","x":676,"y":404,"width":668,"height":44,"backgroundColor":"#fff3bf","fillStyle":"solid","strokeColor":"#ef4444","strokeWidth":2},
{"type":"rectangle","id":"cb3","x":688,"y":418,"width":16,"height":16,"strokeColor":"#ef4444","strokeWidth":1},
{"type":"text","id":"ct3","x":714,"y":418,"text":"หลักฐานการทดลอง (ภาพ / ผลลัพธ์)","fontSize":14,"strokeColor":"#c92a2a"},
{"type":"text","id":"tg3","x":1216,"y":418,"text":"ยังไม่พบในไฟล์","fontSize":14,"strokeColor":"#c92a2a"},

{"type":"rectangle","id":"cr4","x":676,"y":456,"width":668,"height":44,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"rectangle","id":"cb4","x":688,"y":470,"width":16,"height":16,"backgroundColor":"#b2f2bb","fillStyle":"solid","strokeColor":"#22c55e","strokeWidth":1},
{"type":"text","id":"tk4","x":688,"y":468,"text":"✓","fontSize":16,"strokeColor":"#15803d"},
{"type":"text","id":"ct4","x":714,"y":470,"text":"แผนงานสัปดาห์ถัดไป","fontSize":14},
{"type":"text","id":"tg4","x":1252,"y":470,"text":"AI tick","fontSize":14,"strokeColor":"#757575"},

{"type":"text","id":"cnote","x":676,"y":512,"text":"tick ของ AI = คำแนะนำ ไม่ใช่คำตัดสิน — กดยกเลิก tick ได้หาก AI เดาผิด","fontSize":14,"strokeColor":"#2563eb"},

{"type":"rectangle","id":"up","x":676,"y":538,"width":668,"height":76,"strokeColor":"#868e96","strokeWidth":1,"strokeStyle":"dashed"},
{"type":"text","id":"upt","x":842,"y":568,"text":"อัปโหลดไฟล์ (PDF / docx) — ลากมาวาง หรือกดเลือกไฟล์","fontSize":14,"strokeColor":"#757575"},
{"type":"rectangle","id":"f1","x":676,"y":628,"width":668,"height":34,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"text","id":"f1t","x":688,"y":636,"text":"weekly-report-w3.pdf · 1.2 MB","fontSize":14},
{"type":"rectangle","id":"f1c","x":1196,"y":635,"width":130,"height":20,"backgroundColor":"#ffd8a8","fillStyle":"solid","strokeWidth":1,"label":{"text":"AI ตรวจแล้ว 3/4","fontSize":14}},
{"type":"rectangle","id":"f2","x":676,"y":670,"width":668,"height":34,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"text","id":"f2t","x":688,"y":678,"text":"gantt-w3.png · 120 KB","fontSize":14},
{"type":"rectangle","id":"f2c","x":1196,"y":677,"width":130,"height":20,"backgroundColor":"#b2f2bb","fillStyle":"solid","strokeWidth":1,"label":{"text":"ตรงกับข้อ 2","fontSize":14}},
{"type":"text","id":"fnote","x":676,"y":834,"text":"ส่งได้แม้ checklist ยังไม่ครบ (ขึ้น warning ยืนยันก่อน)","fontSize":14,"strokeColor":"#757575"},
{"type":"rectangle","id":"sub","x":1210,"y":824,"width":130,"height":38,"backgroundColor":"#e9ecef","fillStyle":"solid","strokeWidth":2,"label":{"text":"Submit","fontSize":16}},

{"type":"arrow","id":"click","x":585,"y":255,"width":70,"height":-25,"points":[[0,0],[70,-25]],"strokeColor":"#4a9eed","strokeWidth":2,"endArrowhead":"arrow","label":{"text":"กด task","fontSize":14}},

{"type":"text","id":"wlab","x":40,"y":730,"text":"เมื่อกด Submit แต่ checklist ยังไม่ครบ:","fontSize":16,"strokeColor":"#495057"},
{"type":"rectangle","id":"wd","x":40,"y":760,"width":560,"height":300,"backgroundColor":"#ffffff","fillStyle":"solid","strokeWidth":2},
{"type":"text","id":"wt","x":60,"y":780,"text":"ยืนยันการส่ง?","fontSize":18},
{"type":"text","id":"wb1","x":60,"y":820,"text":"ยังขาดรายการ: หลักฐานการทดลอง (1 รายการ)","fontSize":14,"strokeColor":"#c92a2a"},
{"type":"text","id":"wb2","x":60,"y":844,"text":"AI ไม่พบเนื้อหานี้ในไฟล์ที่อัปโหลด","fontSize":14,"strokeColor":"#757575"},
{"type":"rectangle","id":"wb1x","x":60,"y":905,"width":440,"height":22,"backgroundColor":"#fff3bf","fillStyle":"solid","strokeColor":"#f59e0b","strokeWidth":1,"label":{"text":"หลักฐานการทดลอง (ภาพ / ผลลัพธ์)","fontSize":14}},
{"type":"rectangle","id":"wbtn1","x":300,"y":980,"width":130,"height":36,"backgroundColor":"#e9ecef","fillStyle":"solid","strokeWidth":1,"label":{"text":"กลับไปแก้","fontSize":14}},
{"type":"rectangle","id":"wbtn2","x":450,"y":980,"width":130,"height":36,"backgroundColor":"#ffc9c9","fillStyle":"solid","strokeWidth":2,"label":{"text":"ยืนยันส่ง","fontSize":14}},
{"type":"text","id":"wnote","x":60,"y":1026,"text":"เป็น warning ไม่ใช่ block — ยืนยันแล้วส่งได้ สถานะ task เปลี่ยนเป็น Submitted","fontSize":14,"strokeColor":"#757575"},
]

els = []; s = [9000]
def n():
    s[0] += 1; return s[0]

for e in raw:
    lbl = e.pop("label", None)
    el = base(e, n()); els.append(el)
    if el["type"] == "arrow":
        el.update({"lastCommittedPoint":None,"startBinding":None,"endBinding":None,
                   "startArrowhead":None,"endArrowhead":el.get("endArrowhead")})
    elif el["type"] == "text":
        fs = el["fontSize"]; lines = el["text"].split("\n")
        el.update({"fontFamily":1,"textAlign":"left","verticalAlign":"top","containerId":None,
                   "width":int(max(len(l) for l in lines)*fs*0.5),
                   "height":int(len(lines)*fs*1.25),"baseline":int(fs*0.9),"lineHeight":1.25})
    if lbl:
        t = lbl["text"]; fs = lbl.get("fontSize", 16)
        w = int(len(t)*fs*0.55); h = int(fs*1.25); tid = el["id"]+"l"
        el["boundElements"] = [{"id":tid,"type":"text"}]
        els.append(base({"type":"text","id":tid,"x":el["x"]+el["width"]//2-w//2,
                         "y":el["y"]+el["height"]//2-h//2,"width":w,"height":h,"text":t,
                         "fontSize":fs,"fontFamily":1,"textAlign":"center","verticalAlign":"middle",
                         "containerId":el["id"],"baseline":int(fs*0.9),"lineHeight":1.25}, n()))

scene = {"type":"excalidraw","version":2,"source":"https://excalidraw.com",
         "elements":els,"appState":{"viewBackgroundColor":"#ffffff","gridSize":None},"files":{}}
out = "/home/nummmm/Projects/uni/open_sci_dpm/diagrams/wireframe/v1/R4-task-detail.excalidraw"
with open(out, "w") as f:
    json.dump(scene, f, ensure_ascii=False, indent=1)

assert all(set(e) >= {"type","id","x","y","width","height"} for e in els)
ids = [e["id"] for e in els]; assert len(ids) == len(set(ids)), "dup ids"
print(out, len(els), "elements")
