import json

def base(e, seed):
    d = {"angle":0,"backgroundColor":"transparent","fillStyle":"solid","strokeWidth":2,
         "strokeStyle":"solid","roughness":1,"opacity":100,"groupIds":[],"frameId":None,
         "roundness":None,"seed":seed,"version":1,"versionNonce":seed,"isDeleted":False,
         "boundElements":None,"updated":1,"link":None,"locked":False}
    d.update(e)
    if d.get("strokeWidth")==0: d["strokeColor"]="transparent"
    return d

def rect(id,x,y,w,h,**kw):
    e={"type":"rectangle","id":id,"x":x,"y":y,"width":w,"height":h}; e.update(kw); return e

def ell(id,x,y,w,h,**kw):
    e={"type":"ellipse","id":id,"x":x,"y":y,"width":w,"height":h}; e.update(kw); return e

def arrow(id,x,y,pts,**kw):
    e={"type":"arrow","id":id,"x":x,"y":y,"width":abs(pts[1][0]),"height":abs(pts[1][1]),
       "points":pts,"lastCommittedPoint":None,"startArrowhead":None,"endArrowhead":kw.pop("endArrowhead","arrow"),
       "startBinding":None,"endBinding":None}
    e.update(kw); return e

def text(id,x,y,t,fs,w,h,**kw):
    e={"type":"text","id":id,"x":x,"y":y,"width":w,"height":h,"text":t,"fontSize":fs,
       "fontFamily":1,"textAlign":kw.pop("textAlign","left"),"verticalAlign":"top",
       "containerId":None,"baseline":int(fs*0.9),"lineHeight":1.25}
    e.update(kw); return e

def labeled(shape, lbl, fs, tcolor, cx, cy, lw, lh, seed):
    shape["boundElements"]=[{"id":lbl,"type":"text"}]
    t=text(lbl,cx,cy,lbl_text[lbl],fs,lw,lh,strokeColor=tcolor,textAlign="center",verticalAlign="middle")
    t["containerId"]=shape["id"]; t["seed"]=seed; return [shape,t]

lbl_text={}
els=[]; s=[3000]
def n():
    s[0]+=1; return s[0]

def add(e):
    els.append(base(e,n())); return els[-1]

GRAY="#868e96"; DARK="#1e1e1e"; MID="#495057"; LIGHT="#adb5bd"; MUT="#757575"
RED="#c92a2a"; W="#ffffff"; PANEL="#f1f3f5"; CARD="#e9ecef"

def primary_btn(id,x,y,w,h,label,fs=16,lw=130,lh=20):
    lbl_text[id+"l"]=label
    return labeled(rect(id,x,y,w,h,strokeColor=DARK,strokeWidth=2,backgroundColor=CARD,
                        fillStyle="solid",roundness={"type":3}),id+"l",fs,DARK,
                   x+w/2-lw/2,y+h/2-lh/2,lw,lh,n())

def ghost_btn(id,x,y,w,h,label,fs=14,lw=130,lh=18):
    lbl_text[id+"l"]=label
    return labeled(rect(id,x,y,w,h,strokeColor=MID,strokeWidth=1,backgroundColor=W,
                        fillStyle="solid",roundness={"type":3}),id+"l",fs,MID,
                   x+w/2-lw/2,y+h/2-lh/2,lw,lh,n())

def disabled_btn(id,x,y,w,h,label,fs=14,lw=110,lh=18):
    lbl_text[id+"l"]=label
    return labeled(rect(id,x,y,w,h,strokeColor=LIGHT,strokeWidth=1,strokeStyle="dashed",
                        backgroundColor=PANEL,fillStyle="solid",roundness={"type":3}),id+"l",fs,MUT,
                   x+w/2-lw/2,y+h/2-lh/2,lw,lh,n())

# ============ title + state captions ============
add(text("ttl",30,30,"R2 — Create Plan + AI Generate (wireframe v1)",20,420,25,strokeColor=DARK))
add(text("capA",40,62,"(A) Generating / Streaming state",14,240,18,strokeColor=MUT))
add(text("capB",980,62,"(B) Review state",14,140,18,strokeColor=MUT))

# ============ shells: (A) ox=40, (B) ox=980 ; active step 2 / 3 ============
for ox, active in [(40,2),(980,3)]:
    P=f"{'a' if ox==40 else 'b'}"
    add(rect(P+"win",ox,90,880,950,strokeColor=GRAY,strokeWidth=1,roundness={"type":3}))
    add(rect(P+"bar",ox,90,880,50,strokeColor=MID,strokeWidth=1,backgroundColor=CARD,fillStyle="solid"))
    add(rect(P+"tg",ox+12,102,32,26,strokeColor=DARK,strokeWidth=2,roundness={"type":3}))
    for i,y in enumerate([109,115,121]):
        add(arrow(f"{P}mb{i+1}",ox+18,y,[[0,0],[20,0]],strokeColor=DARK,strokeWidth=1,endArrowhead=None))
    add(rect(P+"logo",ox+54,100,30,30,strokeColor=GRAY,strokeWidth=1,strokeStyle="dashed"))
    lbl_text[P+"srchl"]="global search..."
    els+=labeled(rect(P+"srch",ox+330,100,260,30,strokeColor=LIGHT,strokeWidth=1,backgroundColor=W,
                      fillStyle="solid",roundness={"type":3}),P+"srchl",14,MUT,ox+400,107,130,18,n())
    add(ell(P+"bell",ox+780,102,26,26,strokeColor=DARK,strokeWidth=1))
    lbl_text[P+"bdgl"]="3"
    els+=labeled(ell(P+"bdg",ox+800,98,18,18,strokeColor=DARK,backgroundColor=DARK,fillStyle="solid",
                     strokeWidth=1),P+"bdgl",14,W,ox+805,101,8,18,n())
    add(ell(P+"avt",ox+828,102,26,26,strokeColor=GRAY,strokeWidth=1,strokeStyle="dashed"))
    # --- sidebar ---
    add(rect(P+"sbd",ox,140,150,900,strokeColor=GRAY,strokeWidth=1,backgroundColor=PANEL,fillStyle="solid"))
    add(text(P+"sbhome",ox+18,205,"Home",16,45,20,strokeColor=DARK))
    add(text(P+"sbfiles",ox+18,240,"My Files",16,70,20,strokeColor=DARK))
    lbl_text[P+"sbplansl"]="Plans"
    els+=labeled(rect(P+"sbplans",ox+10,272,130,32,strokeColor=DARK,strokeWidth=2,backgroundColor=CARD,
                      fillStyle="solid",roundness={"type":3}),P+"sbplansl",16,DARK,ox+45,279,60,20,n())
    lbl_text[P+"sbnewl"]="+ Create Plan"
    els+=labeled(rect(P+"sbnew",ox+14,322,122,32,strokeColor=MID,strokeWidth=1,strokeStyle="dashed",
                      roundness={"type":3}),P+"sbnewl",13,DARK,ox+25,330,100,16,n())
    add(text(P+"sbrole",ox+18,1000,"— Researcher —",14,110,18,strokeColor=MUT))
    # --- header: title + breadcrumb ---
    CX,PX=ox+160,ox+640
    add(text(P+"htitle",CX,160,"สร้างแผนใหม่ — NSF Grant Proposal",18,330,22,strokeColor=DARK))
    add(text(P+"hsub",CX+2,186,"AI แตก proposal (3 เดือน) → plan + task รายสัปดาห์",13,270,16,strokeColor=MUT))
    steps=[("1 Upload ✓",0),("2 Generating",125),("3 Review",250)]
    for i,(slab,dx) in enumerate(steps):
        sid=f"{P}st{i+1}"; act=(i+1==active)
        lbl_text[sid+"l"]=slab
        els+=labeled(rect(sid,CX+dx,210,110,26,strokeColor=DARK if act else GRAY,
                          strokeWidth=2 if act else 1,
                          backgroundColor=CARD if act else W,fillStyle="solid",
                          roundness={"type":3}),sid+"l",13,DARK if act else MUT,
                     CX+dx+12,216,86,16,n())
        if i<2:
            add(arrow(f"{P}sa{i+1}",CX+dx+112,223,[[0,0],[11,0]],strokeColor=GRAY,strokeWidth=1))
    # --- right: properties panel ---
    add(rect(P+"pp",PX,240,225,660,strokeColor=GRAY,strokeWidth=1,backgroundColor=W,
             fillStyle="solid",roundness={"type":3}))
    add(text(P+"pptitle",PX+10,250,"Properties",16,90,20,strokeColor=DARK))

# ============ STATE A: generating / streaming (ox=40) ============
ox=40; CX,PX=ox+160,ox+640
add(ell("spin",CX+10,248,22,22,strokeColor=MID,strokeWidth=2,strokeStyle="dashed"))
add(text("spintxt",CX+42,249,"AI กำลังวิเคราะห์ proposal…",16,220,20,strokeColor=DARK))
# streaming block (partial)
add(rect("ablk1",CX,290,460,150,strokeColor=GRAY,strokeWidth=1,backgroundColor=W,
         fillStyle="solid",roundness={"type":3}))
add(text("ablk1t",CX+10,300,"📅 Week 1 (1–7 Oct) — task ทบทวนงาน",16,270,20,strokeColor=DARK))
add(text("ablk1s",CX+355,295,"▍ streaming…",12,80,15,strokeColor=MID))
add(text("ablk1b",CX+10,330,"task: ทบทวน literature + ร่างแบบสัมภาษณ์\nส่งสัปดาห์นี้: outline งานวิจัย▍",14,420,36,strokeColor=MID))
# skeleton blocks
for i,y in enumerate([455,570,685]):
    add(rect(f"askel{i+1}",CX,y,460,100,strokeColor=LIGHT,strokeWidth=1,strokeStyle="dashed",
             backgroundColor=W,fillStyle="solid",roundness={"type":3}))
    add(rect(f"askel{i+1}t",CX+12,y+14,140,12,strokeWidth=0,backgroundColor=CARD,fillStyle="solid"))
    for j,bw in enumerate([320,390,350]):
        add(rect(f"askel{i+1}b{j+1}",CX+12,y+36+j*20,bw,10,strokeWidth=0,backgroundColor=CARD,fillStyle="solid"))
# action bar (disabled while generating)
lbl_text["ainpl"]="prompt เพิ่มเติมก่อน generate… (ไม่บังคับ)"
els+=labeled(rect("ainp",CX,880,460,36,strokeColor=LIGHT,strokeWidth=1,backgroundColor=W,
                  fillStyle="solid",roundness={"type":3}),"ainpl",14,MUT,CX+10,890,270,18,n())
disabled_btn("asave",CX,930,140,34,"Save Plan")
disabled_btn("aregen",CX+160,930,180,34,"↻ Regenerate ทั้งก้อน",lw=150)
add(text("anote",CX+355,940,"ยังกดไม่ได้ระหว่าง generate",12,140,15,strokeColor=LIGHT))
# properties panel A: skeleton rows
for i,y in enumerate([300,380,460,540,620,700]):
    add(rect(f"apl{i+1}",PX+10,y,70,12,strokeWidth=0,backgroundColor=CARD,fillStyle="solid"))
    add(rect(f"apv{i+1}",PX+10,y+24,150,14,strokeWidth=0,backgroundColor=PANEL,fillStyle="solid"))

# ============ STATE B: review (ox=980) ============
ox=980; CX,PX=ox+160,ox+640
blocks=[("bb1",240,"📅 Week 1 (1–7 Oct) — เตรียมงาน","task: ทบทวน literature + ร่างแบบสัมภาษณ์\nส่งสัปดาห์นี้: outline งานวิจัย"),
        ("bb2",364,"📅 Week 2 (8–14 Oct) — เก็บข้อมูล","task: เก็บข้อมูลภาคสนาม 10 ชุด\nส่งสัปดาห์นี้: รายงานความคืบหน้าครั้งที่ 1"),
        ("bb3",488,"📅 Week 3 (15–21 Oct) — วิเคราะห์","task: วิเคราะห์ข้อมูลเบื้องต้น\nส่งสัปดาห์นี้: draft บทวิเคราะห์"),
        ("bb4",612,"📅 Week 4 (22–28 Oct) — เขียนรายงาน","task: เขียน draft บทที่ 1–2\nส่งสัปดาห์นี้: draft ให้ advisor ตรวจ")]
for bid,y,bt,bb in blocks:
    add(rect(bid,CX,y,460,112,strokeColor=GRAY,strokeWidth=1,backgroundColor=W,
             fillStyle="solid",roundness={"type":3}))
    add(text(bid+"t",CX+10,y+10,bt,16,300,20,strokeColor=DARK))
    add(text(bid+"b",CX+10,y+40,bb,14,360,36,strokeColor=MID))
    ghost_btn(bid+"ed",CX+388,y+8,62,24,"✎ Edit",12,54,16)
lbl_text["baddl"]="+ เพิ่ม task (week)"
els+=labeled(rect("badd",CX,736,460,30,strokeColor=MID,strokeWidth=1,strokeStyle="dashed",
                  roundness={"type":3}),"baddl",14,MUT,CX+180,742,100,18,n())
# action bar B
lbl_text["binpl"]="prompt เพิ่มเติมสำหรับ AI… (ไม่บังคับ)"
els+=labeled(rect("binp",CX,880,460,36,strokeColor=LIGHT,strokeWidth=1,backgroundColor=W,
                  fillStyle="solid",roundness={"type":3}),"binpl",14,MUT,CX+10,890,250,18,n())
primary_btn("bsave",CX,930,150,38,"💾 Save Plan",lw=120)
ghost_btn("bregen",CX+170,930,190,38,"↻ Regenerate ทั้งก้อน",14,160,18)
# properties panel B: real rows
rows=[("resp","ผู้รับผิดชอบ"),("time","ระยะเวลา plan"),("due","กำหนดส่ง"),
      ("proj","โปรเจกต์ (proposal)"),("stat","สถานะ plan"),("prio","จำนวน task")]
for i,(rid,rlbl) in enumerate(rows):
    y=300+i*95
    add(text("bpr"+rid,PX+10,y,rlbl,13,150,16,strokeColor=MUT))
    vy=y+22
    if rid=="resp":
        add(ell("bprrespav",PX+10,vy+1,18,18,strokeColor=GRAY,strokeWidth=1,strokeStyle="dashed"))
        add(text("bprrespv",PX+36,vy,"ดร. สมชาย ใจดี",14,130,18,strokeColor=DARK))
    elif rid=="due":
        add(rect("bprdueic",PX+10,vy+1,16,16,strokeColor=GRAY,strokeWidth=1))
        add(text("bprduev",PX+34,vy,"30 Dec 2026",14,110,18,strokeColor=DARK))
    elif rid=="proj":
        lbl_text["bprprojtagl"]="NSF Grant"
        els+=labeled(rect("bprprojtag",PX+10,vy-2,100,24,strokeColor=MID,strokeWidth=1,
                          backgroundColor=PANEL,fillStyle="solid",roundness={"type":3}),
                     "bprprojtagl",13,MID,PX+25,vy+3,70,16,n())
    elif rid=="stat":
        lbl_text["bprstattagl"]="Draft"
        els+=labeled(rect("bprstattag",PX+10,vy-2,80,24,strokeColor=DARK,strokeWidth=1,
                          backgroundColor=CARD,fillStyle="solid",roundness={"type":3}),
                     "bprstattagl",13,DARK,PX+30,vy+3,50,16,n())
    elif rid=="prio":
        lbl_text["bprpriotagl"]="12"
        els+=labeled(rect("bprpriotag",PX+10,vy-2,70,24,strokeColor=RED,strokeWidth=1,
                          backgroundColor=W,fillStyle="solid",roundness={"type":3}),
                     "bprpriotagl",13,RED,PX+30,vy+3,40,16,n())
    else:
        add(text("bprtimev",PX+10,vy,"3 เดือน (≈ 12 tasks)",14,140,18,strokeColor=DARK))

# ============ edit-block modal (outside shell) ============
add(rect("modal",420,1080,440,290,strokeColor=DARK,strokeWidth=2,backgroundColor=W,
         fillStyle="solid",roundness={"type":3}))
add(text("mtit",432,1092,"✎ Edit block — Week 3 (15–21 Oct)",16,270,20,strokeColor=DARK))
add(text("mx",832,1092,"✕",14,20,18,strokeColor=MUT))
add(text("mlbl1",432,1122,"เนื้อหาเดิม (แก้ได้เอง)",12,160,15,strokeColor=MUT))
add(rect("mta",432,1140,416,64,strokeColor=GRAY,strokeWidth=1,backgroundColor=PANEL,
         fillStyle="solid",roundness={"type":3}))
add(text("mtat",440,1148,"task: วิเคราะห์ข้อมูลเบื้องต้น\nส่งสัปดาห์นี้: draft บทวิเคราะห์",13,390,34,strokeColor=DARK))
add(text("mlbl2",432,1216,"Prompt สำหรับ AI…",12,140,15,strokeColor=MUT))
lbl_text["mprompt"]="เช่น \"เพิ่ม task สัมภาษณ์ pilot ก่อนเก็บข้อมูลจริง\""
els+=labeled(rect("minp",432,1236,416,32,strokeColor=LIGHT,strokeWidth=1,backgroundColor=W,
                  fillStyle="solid",roundness={"type":3}),"mprompt",13,MUT,442,1244,340,16,n())
primary_btn("mregen",432,1284,150,36,"↻ Regenerate",14,lw=110,lh=18)
ghost_btn("mcancel",592,1284,100,36,"Cancel",14,60,18)
add(text("mnote",702,1294,"regenerate เฉพาะบล็อกนี้",12,150,15,strokeColor=MUT))
add(arrow("marr",820,1078,[[0,0],[360,-480]],strokeColor=GRAY,strokeWidth=1))

# ============ annotations ============
anns=[("a1","A",60,1100,"State A: AI อ่าน proposal → stream\nข้อความออกมาเป็นบล็อก ๆ",280,36,
       "a1arr",90,1096,[[0,0],[140,-830]]),
      ("a2","B",60,1180,"State B: แต่ละบล็อก = task ของ 1 week\n(1 plan มีหลาย task) กด ✎ Edit เพื่อแก้ไข",290,36,
       "a2arr",90,1176,[[0,0],[1050,-666]]),
      ("a3","C",60,1260,"Properties panel: แก้ค่าเร็ว ๆ\nไม่ต้องเลื่อนหาในเนื้อหา",260,36,
       "a3arr",90,1256,[[0,0],[590,-376]]),
      ("a4","D",60,1340,"กด Edit → modal: แก้ข้อความเอง\nหรือใส่ prompt ให้ AI regenerate เฉพาะบล็อกนั้น",300,36,
       "a4arr",90,1336,[[0,0],[320,-90]])]
for cid,letter,cx,cy,atxt,aw,ah,arid,ax,ay,pts in anns:
    lbl_text[cid+"l"]=letter
    els+=labeled(ell(cid,cx,cy,30,30,strokeColor=DARK,strokeWidth=1),cid+"l",16,DARK,
                 cx+10,cy+5,10,20,n())
    add(text("t"+cid,cx+40,cy+2,atxt,14,aw,ah,strokeColor=MID))
    add(arrow(arid,ax,ay,pts,strokeColor=GRAY,strokeWidth=1))

scene={"type":"excalidraw","version":2,"source":"https://excalidraw.com",
       "elements":els,"appState":{"viewBackgroundColor":"#ffffff","gridSize":None},"files":{}}
out="/home/nummmm/Projects/uni/open_sci_dpm/diagrams/wireframe/v1/R2-create-plan.excalidraw"
with open(out,"w") as f: json.dump(scene,f,ensure_ascii=False,indent=1)
assert all(set(e)>={"type","id","x","y","width","height"} for e in els)
ids=[e["id"] for e in els]; assert len(ids)==len(set(ids)), "dup ids"
print(out, len(els), "elements")
