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
els=[]; s=[300]
def n():
    s[0]+=1; return s[0]

def add(e):
    els.append(base(e,n())); return els[-1]

GRAY="#868e96"; DARK="#1e1e1e"; MID="#495057"; LIGHT="#adb5bd"; MUT="#757575"
RED="#c92a2a"; W="#ffffff"; PANEL="#f1f3f5"; CARD="#e9ecef"

# --- shell (same as H1) ---
add(text("ttl",30,30,"R1 — My Files (wireframe v1)",20,400,25,strokeColor=DARK))
add(rect("win",80,90,1040,920,strokeColor=GRAY,strokeWidth=1,roundness={"type":3}))
add(rect("bar",80,90,1040,50,strokeColor=MID,strokeWidth=1,backgroundColor=CARD,fillStyle="solid"))
add(rect("tg",92,102,32,26,strokeColor=DARK,strokeWidth=2,roundness={"type":3}))
for i,y in enumerate([109,115,121]):
    add(arrow(f"b{i+1}",98,y,[[0,0],[20,0]],strokeColor=DARK,strokeWidth=1,endArrowhead=None))
add(rect("logo",134,100,30,30,strokeColor=GRAY,strokeWidth=1,strokeStyle="dashed"))
lbl_text["srchl"]="global search..."
els+=labeled(rect("srch",430,100,300,30,strokeColor=LIGHT,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}),"srchl",14,MUT,505,107,150,18,n())
add(ell("bell",990,102,26,26,strokeColor=DARK,strokeWidth=1))
lbl_text["bdgl"]="3"
els+=labeled(ell("bdg",1010,98,18,18,strokeColor=DARK,backgroundColor=DARK,fillStyle="solid",strokeWidth=1),"bdgl",14,W,1015,101,8,18,n())
add(ell("avt",1038,102,26,26,strokeColor=GRAY,strokeWidth=1,strokeStyle="dashed"))
# --- sidebar (My Files highlighted) ---
add(rect("sbd",80,140,170,870,strokeColor=GRAY,strokeWidth=1,backgroundColor=PANEL,fillStyle="solid"))
add(text("sbhome",98,163,"Home",16,45,20,strokeColor=DARK))
lbl_text["sbfilesl"]="My Files"
els+=labeled(rect("sbfiles",90,198,150,30,strokeColor=DARK,strokeWidth=2,backgroundColor=CARD,fillStyle="solid",roundness={"type":3}),"sbfilesl",16,DARK,140,203,80,20,n())
add(text("sbplans",98,245,"Plans",16,45,20,strokeColor=DARK))
lbl_text["sbnewl"]="+ Create Plan"
els+=labeled(rect("sbnew",94,277,142,32,strokeColor=MID,strokeWidth=1,strokeStyle="dashed",roundness={"type":3}),"sbnewl",14,DARK,140,284,100,18,n())
add(text("sbrole",98,980,"— Researcher —",14,110,18,strokeColor=MUT))
# --- content area ---
add(rect("ctnt",265,155,840,845,strokeColor=LIGHT,strokeWidth=1,strokeStyle="dashed",roundness={"type":3}))
add(text("ctlbl",950,162,"page content (shell)",14,150,18,strokeColor=LIGHT))
# --- heading ---
add(text("head",290,175,"My Files",24,130,30,strokeColor=DARK))
add(text("sub",292,210,"ไฟล์ทั้งหมดที่คุณอัปโหลด (จากทุก task/proposal)",14,320,18,strokeColor=MUT))
# --- filter row ---
lbl_text["propl"]="Proposal: ทั้งหมด ▾"
els+=labeled(rect("prop",290,245,180,30,strokeColor=MID,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}),"propl",14,MID,350,252,140,18,n())
lbl_text["srch2l"]="ค้นหาไฟล์..."
els+=labeled(rect("srch2",490,245,240,30,strokeColor=LIGHT,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}),"srch2l",14,MUT,570,252,120,18,n())
lbl_text["stfl"]="สถานะ AI: ทั้งหมด ▾"
els+=labeled(rect("stf",750,245,170,30,strokeColor=MID,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}),"stfl",14,MID,805,252,130,18,n())
# --- table ---
TX,TW=290,790
add(rect("tbl",TX,295,TW,400,strokeColor=GRAY,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}))
hdrs=[("h1",310,"ชื่อไฟล์"),("h2",545,"Proposal · Task"),("h3",715,"ขนาด"),("h4",790,"อัปโหลด"),("h5",890,"ผลตรวจ AI"),("h6",1005,"จัดการ")]
for hid,hx,ht in hdrs:
    add(text(hid,hx,305,ht,14,120,18,strokeColor=DARK))
add(rect("hsep",TX,327,TW,1,strokeColor=GRAY,strokeWidth=1))
# name, proposal·task, size, date, ai status (p=pending ok=complete warn=missing), warn row
rows=[("survey_data_v2.xlsx","NSF · เก็บข้อมูลสนาม","2.4 MB","12 Sep 2026","p",False),
      ("ethics_form.pdf","NSF · ethics form","320 KB","10 Sep 2026","ok",False),
      ("chapter3_draft.docx","Synthesis · draft บทที่ 3","1.1 MB","8 Sep 2026","warn",True),
      ("literature_matrix.xlsx","Synthesis · รีวิววรรณกรรม","640 KB","2 Sep 2026","ok",False),
      ("budget_update.xlsx","Seed · ปรับ budget","88 KB","28 Aug 2026","ok",False),
      ("consent_th.pdf","NSF · เอกสาร consent","210 KB","25 Aug 2026","warn",True)]
AI={"p":("⏳ กำลังตรวจ",MUT,"dashed"),"ok":("✅ ครบ",DARK,"solid"),"warn":("⚠️ ขาดบางรายการ",RED,"solid")}
for i,(name,ptag,size,date,st,warn) in enumerate(rows):
    y=340+i*58
    scol=RED if warn else GRAY
    add(rect(f"rsep{i+1}",TX,y+48,TW,1,strokeColor=PANEL,strokeWidth=1))
    if warn:
        add(rect(f"rhl{i+1}",TX,y-8,TW,56,strokeColor=RED,strokeWidth=1,strokeStyle="dashed"))
    # file icon + name
    add(rect(f"fic{i+1}",308,y,16,20,strokeColor=scol,strokeWidth=1,strokeStyle="dashed"))
    add(text(f"fn{i+1}",334,y+2,name,14,190,18,strokeColor=DARK))
    # proposal · task tag
    lbl_text[f"tg{i+1}l"]=ptag
    els+=labeled(rect(f"tg{i+1}",540,y,180,24,strokeColor=GRAY,strokeWidth=1,backgroundColor=PANEL,fillStyle="solid",roundness={"type":3}),f"tg{i+1}l",12,MID,585,y+5,130,16,n())
    add(text(f"sz{i+1}",715,y+2,size,14,60,18,strokeColor=MUT))
    add(text(f"dt{i+1}",790,y+2,date,14,90,18,strokeColor=MUT))
    # AI badge — heart of the page
    bt,bc,bsty=AI[st]
    lbl_text[f"ai{i+1}l"]=bt
    els+=labeled(rect(f"ai{i+1}",885,y,150,26,strokeColor=bc,strokeWidth=2,strokeStyle=bsty,
                      backgroundColor=(PANEL if st!="warn" else W),fillStyle="solid",roundness={"type":3}),
                 f"ai{i+1}l",13,bc,915,y+5,110,17,n())
    # preview / download buttons
    lbl_text[f"pv{i+1}l"]="👁"
    els+=labeled(rect(f"pv{i+1}",1000,y,34,26,strokeColor=MID,strokeWidth=1,strokeStyle="dashed",backgroundColor=W,fillStyle="solid",roundness={"type":3}),f"pv{i+1}l",12,MID,1010,y+5,16,17,n())
    lbl_text[f"dl{i+1}l"]="⬇"
    els+=labeled(rect(f"dl{i+1}",1040,y,34,26,strokeColor=MID,strokeWidth=1,strokeStyle="dashed",backgroundColor=W,fillStyle="solid",roundness={"type":3}),f"dl{i+1}l",12,MID,1050,y+5,16,17,n())
# --- flow note ---
lbl_text["flwl"]="อัปโหลดจาก Task Detail (R4) → ไฟล์มาโผล่ที่นี่อัตโนมัติ"
els+=labeled(rect("flw",290,715,460,32,strokeColor=MID,strokeWidth=1,strokeStyle="dashed",roundness={"type":3}),"flwl",14,MID,350,722,380,18,n())
# --- annotations ---
# A: AI column is the heart -> points at a badge
lbl_text["circAl"]="A"
els+=labeled(ell("circA",60,760,30,30,strokeColor=RED,strokeWidth=2),"circAl",16,RED,70,765,10,20,n())
add(text("annA",100,764,"คอลัมน์ผลตรวจ AI = หัวใจของหน้านี้\n✅ ครบ / ⚠️ ขาดบางรายการ / ⏳ กำลังตรวจ",14,300,36,strokeColor=MID))
add(arrow("arrA",130,760,[[0,0],[790,-380]],strokeColor=RED,strokeWidth=1))
# B: warning row highlight
lbl_text["circBl"]="B"
els+=labeled(ell("circB",60,860,30,30,strokeColor=DARK,strokeWidth=1),"circBl",16,DARK,70,865,10,20,n())
add(text("annB",100,864,"แถว ⚠️ เน้นขอบแดง — กดไฟล์เพื่อดู\nรายการที่ขาด / แก้ไขแล้วอัปโหลดใหม่",14,290,36,strokeColor=MID))
add(arrow("arrB",130,858,[[0,0],[690,-480]],strokeColor=GRAY,strokeWidth=1))
# C: flow
lbl_text["circCl"]="C"
els+=labeled(ell("circC",60,950,30,30,strokeColor=DARK,strokeWidth=1),"circCl",16,DARK,70,955,10,20,n())
add(text("annC",100,954,"flow: ไฟล์ที่อัปโหลดใน Task Detail\nจะถูกผูกกับ task/proposal นั้นทันที",14,270,36,strokeColor=MID))
add(arrow("arrC",130,948,[[0,0],[320,-215]],strokeColor=GRAY,strokeWidth=1))

ids=[e["id"] for e in els]; assert len(ids)==len(set(ids)), "dup ids"
out="/home/nummmm/Projects/uni/open_sci_dpm/diagrams/wireframe/v1/R1-my-files.excalidraw"
with open(out,"w") as f: json.dump(els,f,ensure_ascii=False,indent=1)
print(out, len(els), "elements")
