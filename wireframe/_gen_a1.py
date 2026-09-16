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
GRN="#2f9e44"; GRNBG="#b2f2bb"; YEL="#f08c00"; YELBG="#fff3bf"; BLU="#2563eb"

# --- shell ---
add(text("ttl",30,30,"A1 — Admin Home + User/Role Management (wireframe v1)",20,460,25,strokeColor=DARK))
add(rect("win",80,90,1040,920,strokeColor=GRAY,strokeWidth=1,roundness={"type":3}))
add(rect("bar",80,90,1040,50,strokeColor=MID,strokeWidth=1,backgroundColor=CARD,fillStyle="solid"))
add(rect("tg",92,102,32,26,strokeColor=DARK,strokeWidth=2,roundness={"type":3}))
for i,y in enumerate([109,115,121]):
    add(arrow(f"b{i+1}",98,y,[[0,0],[20,0]],strokeColor=DARK,strokeWidth=1,endArrowhead=None))
add(rect("logo",134,100,30,30,strokeColor=GRAY,strokeWidth=1,strokeStyle="dashed"))
lbl_text["srchl"]="global search..."
els+=labeled(rect("srch",430,100,300,30,strokeColor=LIGHT,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}),"srchl",14,MUT,505,107,150,18,n())
lbl_text["vwl"]="View as: Admin ▾"
els+=labeled(rect("vw",850,102,122,26,strokeColor=DARK,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}),"vwl",14,DARK,880,108,100,18,n())
add(ell("bell",990,102,26,26,strokeColor=DARK,strokeWidth=1))
lbl_text["bdgl"]="1"
els+=labeled(ell("bdg",1010,98,18,18,strokeColor=DARK,backgroundColor=DARK,fillStyle="solid",strokeWidth=1),"bdgl",14,W,1015,101,8,18,n())
add(ell("avt",1038,102,26,26,strokeColor=GRAY,strokeWidth=1,strokeStyle="dashed"))
# --- sidebar (menu ของ Admin = Researcher + Committee + Users) ---
add(rect("sbd",80,140,170,870,strokeColor=GRAY,strokeWidth=1,backgroundColor=PANEL,fillStyle="solid"))
lbl_text["sbhomel"]="Home"
els+=labeled(rect("sbhome",90,158,150,30,strokeColor=DARK,strokeWidth=2,backgroundColor=CARD,fillStyle="solid",roundness={"type":3}),"sbhomel",16,DARK,140,163,50,20,n())
add(text("sbfiles",98,205,"My Files",16,70,20,strokeColor=DARK))
add(text("sbplans",98,240,"Plans",16,45,20,strokeColor=DARK))
add(text("sbappr",98,275,"Approve Plans",16,115,20,strokeColor=DARK))
add(arrow("sbdiv",92,320,[[0,0],[146,0]],strokeColor=LIGHT,strokeWidth=1,endArrowhead=None))
lbl_text["sbusr"]="Users & Roles"
els+=labeled(rect("sbusrb",90,335,150,32,strokeColor=DARK,strokeWidth=2,backgroundColor=DARK,fillStyle="solid",roundness={"type":3}),"sbusr",16,W,140,341,110,20,n())
add(text("sbrole",98,980,"— Admin —",14,80,18,strokeColor=MUT))
# --- greeting ---
add(text("greet",290,180,"Admin Dashboard",24,240,30,strokeColor=DARK))
add(text("sub",292,215,"ภาพรวมระบบ + จัดการผู้ใช้และ role",14,260,18,strokeColor=MUT))
# --- stat cards ---
cards=[("c1",290,"i1","ct1","Researchers","cn1","12 คน",DARK,505),
       ("c2",495,"i2","ct2","Committee","cn2","5 คน",DARK,710),
       ("c3",700,"i3","ct3","Proposals ทั้งหมด","cn3","34",DARK,915),
       ("c4",905,"i4","ct4","รอ Approve","cn4","3",RED,1095)]
for cid,cx,iid,tid,ttl_,nid,num,ncol,ax in cards:
    add(rect(cid,cx,250,190,80,strokeColor=GRAY,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}))
    add(rect(iid,cx+12,262,18,18,strokeColor=GRAY,strokeWidth=1,strokeStyle="dashed"))
    add(text(tid,cx+40,263,ttl_,14,130,18,strokeColor=MUT))
    add(text(nid,cx+12,292,num,20,120,25,strokeColor=ncol))
    add(text(ax,ax,292,"→",16,20,20,strokeColor=MID))
# --- user management header ---
add(text("uhead",290,355,"จัดการผู้ใช้",18,110,22,strokeColor=DARK))
add(text("usub",292,384,"user sign up ด้วยอีเมลมหาลัยเอง — admin กำหนด role ให้",14,350,18,strokeColor=MUT))
lbl_text["usrl"]="ค้นหา user..."
els+=labeled(rect("usrch",680,352,160,28,strokeColor=LIGHT,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}),"usrl",14,MUT,730,359,110,18,n())
lbl_text["ufiltl"]="Role: All ▾"
els+=labeled(rect("ufilt",850,352,110,28,strokeColor=MID,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}),"ufiltl",14,MID,880,359,80,18,n())
# --- user table ---
add(rect("tbl",290,410,800,380,strokeColor=GRAY,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}))
add(text("th1",300,422,"ชื่อ / อีเมล",14,90,18,strokeColor=MUT))
add(text("th2",560,422,"Role",14,40,18,strokeColor=MUT))
add(text("th3",760,422,"สถานะ",14,50,18,strokeColor=MUT))
add(text("th4",880,422,"การจัดการ",14,80,18,strokeColor=MUT))
add(arrow("thline",300,452,[[0,0],[780,0]],strokeColor=LIGHT,strokeWidth=1,endArrowhead=None))
# highlight แถว pending (แถวที่ 4)
add(rect("rowp",295,638,790,52,strokeColor=YEL,strokeWidth=1,backgroundColor=YELBG,fillStyle="solid",roundness={"type":3}))
users=[("ดร. สมชาย ใจดี","somchai@uni.ac.th","Researcher ▾",True,True),
       ("ผศ. สมหญิง รักงาน","somying@uni.ac.th","Committee ▾",True,True),
       ("ศ. อานนท์ ประธาน","anant@uni.ac.th","Chief ▾",True,True),
       ("มานะ ตั้งใจ","mana@uni.ac.th","ยังไม่ได้กำหนด",True,True),
       ("อดิศร เก่า","adisak@uni.ac.th","Researcher ▾",False,False)]
for i,(name,mail,role,active,pending) in enumerate(users):
    y=470+i*58
    ncol=RED if pending else DARK
    add(text(f"un{i+1}",300,y,name,14,150,18,strokeColor=ncol))
    add(text(f"um{i+1}",300,y+22,mail,14,160,18,strokeColor=MUT))
    if pending:
        lbl_text[f"ur{i+1}l"]=role
        els+=labeled(rect(f"ur{i+1}",560,y-2,130,26,strokeColor=YEL,strokeWidth=1,strokeStyle="dashed",backgroundColor=YELBG,fillStyle="solid",roundness={"type":3}),f"ur{i+1}l",14,RED,575,y+6,120,18,n())
    else:
        lbl_text[f"ur{i+1}l"]=role
        els+=labeled(rect(f"ur{i+1}",560,y-2,120,26,strokeColor=GRAY,strokeWidth=1,backgroundColor=PANEL,fillStyle="solid",roundness={"type":3}),f"ur{i+1}l",14,DARK,575,y+6,110,18,n())
    # toggle เปิด-ปิดการใช้งาน
    add(rect(f"ut{i+1}",760,y+2,36,18,strokeColor=GRN if active else GRAY,strokeWidth=1,
             backgroundColor=GRNBG if active else PANEL,fillStyle="solid",roundness={"type":3}))
    add(ell(f"uk{i+1}",760+(19 if active else 2),y+4,14,14,strokeColor=DARK if active else GRAY,
            backgroundColor=DARK if active else GRAY,fillStyle="solid",strokeWidth=1))
    add(text(f"ue{i+1}",880,y,"แก้ไข",14,45,18,strokeColor=BLU))
# --- annotations ---
anns=[("circA","A",60,1040,"annA","Admin เห็นเมนูครบ: ของ Researcher\n+ Approve Plans + Users & Roles","arrA",[[0,0],[55,-680]]),
      ("circB","B",400,1040,"annB","กด Role ▾ → เลือก Researcher /\nCommittee / Chief / Admin","arrB",[[0,0],[185,-560]]),
      ("circC","C",660,1040,"annC","toggle เปิด-ปิดการใช้งาน user","arrC",[[0,0],[105,-560]]),
      ("circD","D",900,1040,"annD","user ที่ sign up เองแล้ว\nรอ admin กำหนด role","arrD",[[0,0],[-480,-370]])]
for cid,letter,cx,cy,aid,atxt,arid,pts in anns:
    lbl_text[cid+"l"]=letter
    els+=labeled(ell(cid,cx,cy,30,30,strokeColor=DARK,strokeWidth=1),cid+"l",16,DARK,cx+10,cy+5,10,20,n())
    w=250 if "\n" in atxt else 230
    h=36 if "\n" in atxt else 18
    add(text(aid,cx+40,cy+2,atxt,14,w,h,strokeColor=MID))
    if arid: add(arrow(arid,cx+15,cy-2,pts,strokeColor=GRAY,strokeWidth=1))

scene={"type":"excalidraw","version":2,"source":"https://excalidraw.com",
       "elements":els,"appState":{"viewBackgroundColor":"#ffffff","gridSize":None},"files":{}}
out="/home/nummmm/Projects/uni/open-sci/wireframe/v1/A1-admin-home-user-role.excalidraw"
with open(out,"w") as f: json.dump(scene,f,ensure_ascii=False,indent=1)
assert all(set(e)>= {"type","id","x","y","width","height"} for e in els)
ids=[e["id"] for e in els]; assert len(ids)==len(set(ids)), "dup ids"
print(out, len(els), "elements")
