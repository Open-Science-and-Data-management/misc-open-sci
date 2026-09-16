# R3 — Plan Detail (Summary / Timeline / Kanban / Calendar)
# เดียวกับที่วาดใน session: หน้าเต็ม 1 (Summary) + mockup เฉพาะ content area อีก 3 view
import json

def base(e, seed):
    d = {"angle":0,"backgroundColor":"transparent","fillStyle":"solid","strokeWidth":2,
         "strokeStyle":"solid","roughness":1,"opacity":100,"groupIds":[],"frameId":None,
         "roundness":None,"seed":seed,"version":1,"versionNonce":seed,"isDeleted":False,
         "boundElements":None,"updated":1,"link":None,"locked":False}
    d.update(e)
    return d

raw = [
# ---------- 1) หน้าเต็ม: App Shell + Summary view ----------
{"type":"text","id":"t0","x":250,"y":30,"text":"R3 — Plan Detail (4 Views)","fontSize":28},
{"type":"text","id":"lab1","x":40,"y":76,"text":"1) หน้าเต็ม — โครงหน้า (App Shell S2) + Summary view","fontSize":16,"strokeColor":"#495057"},
{"type":"rectangle","id":"fr","x":40,"y":90,"width":760,"height":620,"strokeWidth":2},
{"type":"rectangle","id":"tb","x":40,"y":90,"width":760,"height":40,"backgroundColor":"#f1f3f5","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"arrow","id":"l1","x":56,"y":106,"width":24,"height":0,"points":[[0,0],[24,0]],"strokeWidth":2,"endArrowhead":None},
{"type":"arrow","id":"l2","x":56,"y":113,"width":24,"height":0,"points":[[0,0],[24,0]],"strokeWidth":2,"endArrowhead":None},
{"type":"arrow","id":"l3","x":56,"y":120,"width":24,"height":0,"points":[[0,0],[24,0]],"strokeWidth":2,"endArrowhead":None},
{"type":"rectangle","id":"lg","x":96,"y":99,"width":26,"height":22,"backgroundColor":"#e9ecef","fillStyle":"solid","strokeWidth":1},
{"type":"text","id":"m1","x":140,"y":102,"text":"Home","fontSize":14},
{"type":"text","id":"m2","x":196,"y":102,"text":"My Files","fontSize":14},
{"type":"text","id":"m3","x":276,"y":102,"text":"Plans","fontSize":14},
{"type":"ellipse","id":"bell","x":706,"y":100,"width":20,"height":20,"strokeWidth":1},
{"type":"ellipse","id":"av","x":742,"y":99,"width":22,"height":22,"backgroundColor":"#e9ecef","fillStyle":"solid","strokeWidth":1},
{"type":"text","id":"pt","x":60,"y":148,"text":"Proposal: ระบบติดตามงานวิจัย (ชื่อจาก proposal)","fontSize":18},
{"type":"rectangle","id":"bd","x":560,"y":148,"width":100,"height":26,"backgroundColor":"#ffd8a8","fillStyle":"solid","strokeWidth":1,"label":{"text":"Committed","fontSize":14}},
{"type":"rectangle","id":"cb","x":676,"y":146,"width":112,"height":30,"backgroundColor":"#e9ecef","fillStyle":"solid","strokeWidth":2,"label":{"text":"Commit Plan","fontSize":14}},
{"type":"text","id":"sn","x":60,"y":184,"text":"สถานะ: Draft → Committed → Approved · แก้หลัง commit ได้ แต่ต้องขอ approve ใหม่","fontSize":14,"strokeColor":"#757575"},
{"type":"rectangle","id":"tab1","x":60,"y":220,"width":110,"height":30,"backgroundColor":"#e9ecef","fillStyle":"solid","strokeWidth":1,"label":{"text":"Summary","fontSize":14}},
{"type":"text","id":"tab2","x":200,"y":227,"text":"Timeline","fontSize":14,"strokeColor":"#868e96"},
{"type":"text","id":"tab3","x":296,"y":227,"text":"Kanban","fontSize":14,"strokeColor":"#868e96"},
{"type":"text","id":"tab4","x":380,"y":227,"text":"Calendar","fontSize":14,"strokeColor":"#868e96"},
{"type":"arrow","id":"tline","x":60,"y":250,"width":720,"height":0,"points":[[0,0],[720,0]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"rectangle","id":"pc","x":60,"y":270,"width":720,"height":70,"backgroundColor":"#f1f3f5","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"text","id":"pct1","x":75,"y":282,"text":"ความคืบหน้ารวม","fontSize":14},
{"type":"text","id":"pct2","x":75,"y":304,"text":"62%","fontSize":22},
{"type":"rectangle","id":"barbg","x":210,"y":306,"width":550,"height":14,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"rectangle","id":"barfill","x":210,"y":306,"width":341,"height":14,"backgroundColor":"#4a9eed","fillStyle":"solid","strokeColor":"#4a9eed","strokeWidth":1},
{"type":"rectangle","id":"sc1","x":60,"y":355,"width":230,"height":58,"backgroundColor":"#f1f3f5","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1,"label":{"text":"To do — 4","fontSize":16}},
{"type":"rectangle","id":"sc2","x":310,"y":355,"width":230,"height":58,"backgroundColor":"#f1f3f5","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1,"label":{"text":"In progress — 3","fontSize":16}},
{"type":"rectangle","id":"sc3","x":560,"y":355,"width":220,"height":58,"backgroundColor":"#f1f3f5","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1,"label":{"text":"Done — 5","fontSize":16}},
{"type":"text","id":"lh","x":60,"y":430,"text":"Task ทั้งหมด — กดที่ task เพื่อเปิด Task Detail (R4)","fontSize":14,"strokeColor":"#495057"},
{"type":"rectangle","id":"r1","x":60,"y":455,"width":720,"height":36,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"text","id":"r1t","x":72,"y":466,"text":"1. เก็บข้อมูล / สำรวจตลาด","fontSize":14},
{"type":"rectangle","id":"r1c","x":680,"y":462,"width":86,"height":22,"backgroundColor":"#b2f2bb","fillStyle":"solid","strokeWidth":1,"label":{"text":"Done","fontSize":14}},
{"type":"rectangle","id":"r2","x":60,"y":497,"width":720,"height":36,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"text","id":"r2t","x":72,"y":508,"text":"2. ออกแบบระบบ","fontSize":14},
{"type":"rectangle","id":"r2c","x":680,"y":504,"width":86,"height":22,"backgroundColor":"#b2f2bb","fillStyle":"solid","strokeWidth":1,"label":{"text":"Done","fontSize":14}},
{"type":"rectangle","id":"r3","x":60,"y":539,"width":720,"height":36,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"text","id":"r3t","x":72,"y":550,"text":"3. พัฒนาโปรโตไทป์","fontSize":14},
{"type":"rectangle","id":"r3c","x":680,"y":546,"width":86,"height":22,"backgroundColor":"#ffd8a8","fillStyle":"solid","strokeWidth":1,"label":{"text":"In progress","fontSize":14}},
{"type":"rectangle","id":"r4","x":60,"y":581,"width":720,"height":36,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"text","id":"r4t","x":72,"y":592,"text":"4. ทดสอบ + เขียนรายงาน","fontSize":14},
{"type":"rectangle","id":"r4c","x":680,"y":588,"width":86,"height":22,"backgroundColor":"#e9ecef","fillStyle":"solid","strokeWidth":1,"label":{"text":"To do","fontSize":14}},
{"type":"text","id":"ann","x":60,"y":632,"text":"→ กด task เพื่อเปิด Task Detail (R4) — AI checklist + อัปโหลดไฟล์","fontSize":14,"strokeColor":"#2563eb"},
{"type":"text","id":"adm","x":60,"y":658,"text":"(Admin: หน้าเดียวกัน + เมนู Approve Plans เพิ่มใน navbar)","fontSize":14,"strokeColor":"#757575"},

# ---------- 2) Timeline (Gantt-lite) ----------
{"type":"text","id":"tlab","x":880,"y":196,"text":"2) Timeline (Gantt-lite) — เปลี่ยนเฉพาะ content area","fontSize":16,"strokeColor":"#495057"},
{"type":"rectangle","id":"tfr","x":880,"y":230,"width":680,"height":440,"strokeWidth":2},
{"type":"text","id":"mo1","x":1000,"y":244,"text":"ส.ค.","fontSize":14,"strokeColor":"#868e96"},
{"type":"text","id":"mo2","x":1180,"y":244,"text":"ก.ย.","fontSize":14,"strokeColor":"#868e96"},
{"type":"text","id":"mo3","x":1360,"y":244,"text":"ต.ค.","fontSize":14,"strokeColor":"#868e96"},
{"type":"arrow","id":"vl1","x":1080,"y":240,"width":0,"height":390,"points":[[0,0],[0,390]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"arrow","id":"vl2","x":1260,"y":240,"width":0,"height":390,"points":[[0,0],[0,390]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"arrow","id":"vl3","x":1440,"y":240,"width":0,"height":390,"points":[[0,0],[0,390]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"arrow","id":"today","x":1230,"y":240,"width":0,"height":390,"points":[[0,0],[0,390]],"strokeColor":"#ef4444","strokeWidth":2,"strokeStyle":"dashed","endArrowhead":None},
{"type":"text","id":"tdt","x":1206,"y":220,"text":"วันนี้","fontSize":14,"strokeColor":"#c92a2a"},
{"type":"rectangle","id":"b1","x":920,"y":290,"width":180,"height":28,"backgroundColor":"#e9ecef","fillStyle":"solid","strokeWidth":1,"label":{"text":"Task 1","fontSize":14}},
{"type":"rectangle","id":"b2","x":1040,"y":335,"width":200,"height":28,"backgroundColor":"#e9ecef","fillStyle":"solid","strokeWidth":1,"label":{"text":"Task 2","fontSize":14}},
{"type":"rectangle","id":"b3","x":1180,"y":380,"width":260,"height":28,"backgroundColor":"#ffd8a8","fillStyle":"solid","strokeWidth":1,"label":{"text":"Task 3 (กำลังทำ)","fontSize":14}},
{"type":"rectangle","id":"b4","x":1300,"y":425,"width":170,"height":28,"backgroundColor":"#ffc9c9","fillStyle":"solid","strokeWidth":1,"label":{"text":"เกินกำหนด","fontSize":14}},
{"type":"rectangle","id":"b5","x":950,"y":470,"width":160,"height":28,"backgroundColor":"#b2f2bb","fillStyle":"solid","strokeWidth":1,"label":{"text":"Task 5","fontSize":14}},
{"type":"text","id":"tleg","x":880,"y":684,"text":"แถบ = task · เส้นประแดง = วันนี้ · แถบแดง = overdue","fontSize":14,"strokeColor":"#757575"},

# ---------- 3) Kanban ----------
{"type":"text","id":"klab","x":40,"y":750,"text":"3) Kanban — คอลัมน์ตามสถานะ (ลากย้ายได้)","fontSize":16,"strokeColor":"#495057"},
{"type":"rectangle","id":"kfr","x":40,"y":780,"width":760,"height":440,"strokeWidth":2},
{"type":"rectangle","id":"kc1","x":60,"y":800,"width":230,"height":380,"backgroundColor":"#f1f3f5","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"rectangle","id":"kc2","x":310,"y":800,"width":230,"height":380,"backgroundColor":"#f1f3f5","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"rectangle","id":"kc3","x":560,"y":800,"width":230,"height":380,"backgroundColor":"#f1f3f5","fillStyle":"solid","strokeColor":"#868e96","strokeWidth":1},
{"type":"text","id":"kh1","x":145,"y":810,"text":"To do","fontSize":16},
{"type":"text","id":"kh2","x":380,"y":810,"text":"In progress","fontSize":16},
{"type":"text","id":"kh3","x":645,"y":810,"text":"Done","fontSize":16},
{"type":"rectangle","id":"kt1","x":70,"y":850,"width":210,"height":58,"backgroundColor":"#ffffff","fillStyle":"solid","strokeWidth":1},
{"type":"text","id":"kt1a","x":80,"y":858,"text":"ทดสอบระบบ","fontSize":14},
{"type":"text","id":"kt1b","x":80,"y":880,"text":"โดย 30 ก.ย.","fontSize":14,"strokeColor":"#757575"},
{"type":"rectangle","id":"kt2","x":70,"y":918,"width":210,"height":58,"backgroundColor":"#ffffff","fillStyle":"solid","strokeWidth":1},
{"type":"text","id":"kt2a","x":80,"y":926,"text":"เขียนรายงาน","fontSize":14},
{"type":"text","id":"kt2b","x":80,"y":948,"text":"โดย 15 ต.ค.","fontSize":14,"strokeColor":"#757575"},
{"type":"rectangle","id":"kt3","x":70,"y":986,"width":210,"height":58,"backgroundColor":"#ffffff","fillStyle":"solid","strokeWidth":1},
{"type":"text","id":"kt3a","x":80,"y":994,"text":"เตรียมนำเสนอ","fontSize":14},
{"type":"text","id":"kt3b","x":80,"y":1016,"text":"โดย 30 ต.ค.","fontSize":14,"strokeColor":"#757575"},
{"type":"rectangle","id":"ki1","x":320,"y":850,"width":210,"height":58,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#f59e0b","strokeWidth":1},
{"type":"text","id":"ki1a","x":330,"y":858,"text":"พัฒนาโปรโตไทป์","fontSize":14},
{"type":"text","id":"ki1b","x":330,"y":880,"text":"โดย 20 ก.ย.","fontSize":14,"strokeColor":"#757575"},
{"type":"rectangle","id":"ki2","x":320,"y":918,"width":210,"height":58,"backgroundColor":"#ffffff","fillStyle":"solid","strokeWidth":1},
{"type":"text","id":"ki2a","x":330,"y":926,"text":"เก็บข้อมูลเพิ่ม","fontSize":14},
{"type":"text","id":"ki2b","x":330,"y":948,"text":"โดย 25 ก.ย.","fontSize":14,"strokeColor":"#757575"},
{"type":"rectangle","id":"kd1","x":570,"y":850,"width":210,"height":58,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#22c55e","strokeWidth":1},
{"type":"text","id":"kd1a","x":580,"y":858,"text":"ออกแบบระบบ","fontSize":14},
{"type":"text","id":"kd1b","x":580,"y":880,"text":"เสร็จ 10 ก.ย.","fontSize":14,"strokeColor":"#757575"},
{"type":"rectangle","id":"kd2","x":570,"y":918,"width":210,"height":58,"backgroundColor":"#ffffff","fillStyle":"solid","strokeColor":"#22c55e","strokeWidth":1},
{"type":"text","id":"kd2a","x":580,"y":926,"text":"เก็บข้อมูลตลาด","fontSize":14},
{"type":"text","id":"kd2b","x":580,"y":948,"text":"เสร็จ 1 ก.ย.","fontSize":14,"strokeColor":"#757575"},
{"type":"text","id":"kann","x":60,"y":1192,"text":"การ์ด = task · กดเพื่อเปิด Task Detail (R4)","fontSize":14,"strokeColor":"#757575"},

# ---------- 4) Calendar ----------
{"type":"text","id":"clab","x":880,"y":750,"text":"4) Calendar — task กระจายตามปฏิทินเดือน","fontSize":16,"strokeColor":"#495057"},
{"type":"rectangle","id":"cfr","x":880,"y":780,"width":680,"height":440,"strokeWidth":2},
{"type":"text","id":"cnav1","x":920,"y":796,"text":"<","fontSize":20},
{"type":"text","id":"cnav2","x":1150,"y":800,"text":"กันยายน 2026","fontSize":16},
{"type":"text","id":"cnav3","x":1400,"y":796,"text":">","fontSize":20},
{"type":"text","id":"dow","x":915,"y":832,"text":"จ          อ          พ         พฤ         ศ         ส        อา","fontSize":14,"strokeColor":"#868e96"},
{"type":"rectangle","id":"grid","x":900,"y":860,"width":640,"height":300,"strokeColor":"#868e96","strokeWidth":1},
{"type":"arrow","id":"gv1","x":991,"y":860,"width":0,"height":300,"points":[[0,0],[0,300]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"arrow","id":"gv2","x":1083,"y":860,"width":0,"height":300,"points":[[0,0],[0,300]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"arrow","id":"gv3","x":1174,"y":860,"width":0,"height":300,"points":[[0,0],[0,300]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"arrow","id":"gv4","x":1266,"y":860,"width":0,"height":300,"points":[[0,0],[0,300]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"arrow","id":"gv5","x":1357,"y":860,"width":0,"height":300,"points":[[0,0],[0,300]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"arrow","id":"gv6","x":1449,"y":860,"width":0,"height":300,"points":[[0,0],[0,300]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"arrow","id":"gh1","x":900,"y":920,"width":640,"height":0,"points":[[0,0],[640,0]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"arrow","id":"gh2","x":900,"y":980,"width":640,"height":0,"points":[[0,0],[640,0]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"arrow","id":"gh3","x":900,"y":1040,"width":640,"height":0,"points":[[0,0],[640,0]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"arrow","id":"gh4","x":900,"y":1100,"width":640,"height":0,"points":[[0,0],[640,0]],"strokeColor":"#868e96","strokeWidth":1,"endArrowhead":None},
{"type":"rectangle","id":"ch1","x":905,"y":895,"width":80,"height":18,"backgroundColor":"#ffd8a8","fillStyle":"solid","strokeWidth":1},
{"type":"rectangle","id":"ch2","x":1090,"y":955,"width":80,"height":18,"backgroundColor":"#ffd8a8","fillStyle":"solid","strokeWidth":1},
{"type":"rectangle","id":"ch3","x":1272,"y":1015,"width":80,"height":18,"backgroundColor":"#b2f2bb","fillStyle":"solid","strokeWidth":1},
{"type":"rectangle","id":"ch4","x":1000,"y":1075,"width":80,"height":18,"backgroundColor":"#e9ecef","fillStyle":"solid","strokeWidth":1},
{"type":"rectangle","id":"ch5","x":1455,"y":895,"width":80,"height":18,"backgroundColor":"#b2f2bb","fillStyle":"solid","strokeWidth":1},
{"type":"text","id":"cann","x":900,"y":1180,"text":"chip = task มี due ตรงวันนั้น · กด chip → Task Detail (R4)","fontSize":14,"strokeColor":"#757575"},
]

els = []; s = [7000]
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
out = "/home/nummmm/Projects/uni/open_sci_dpm/diagrams/wireframe/v1/R3-plan-detail.excalidraw"
with open(out, "w") as f:
    json.dump(scene, f, ensure_ascii=False, indent=1)

assert all(set(e) >= {"type","id","x","y","width","height"} for e in els)
ids = [e["id"] for e in els]; assert len(ids) == len(set(ids)), "dup ids"
print(out, len(els), "elements")
