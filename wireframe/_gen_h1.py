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

# --- shell ---
add(text("ttl",30,30,"H1 — Home (Researcher) (wireframe v1)",20,400,25,strokeColor=DARK))
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
# --- sidebar ---
add(rect("sbd",80,140,170,870,strokeColor=GRAY,strokeWidth=1,backgroundColor=PANEL,fillStyle="solid"))
lbl_text["sbhomel"]="Home"
els+=labeled(rect("sbhome",90,158,150,30,strokeColor=DARK,strokeWidth=2,backgroundColor=CARD,fillStyle="solid",roundness={"type":3}),"sbhomel",16,DARK,140,163,50,20,n())
add(text("sbfiles",98,205,"My Files",16,70,20,strokeColor=DARK))
add(text("sbplans",98,240,"Plans",16,45,20,strokeColor=DARK))
lbl_text["sbnewl"]="+ Create Plan"
els+=labeled(rect("sbnew",94,272,142,32,strokeColor=MID,strokeWidth=1,strokeStyle="dashed",roundness={"type":3}),"sbnewl",14,DARK,140,279,100,18,n())
add(text("sbrole",98,980,"— Researcher —",14,110,18,strokeColor=MUT))
# --- content area ---
add(rect("ctnt",265,155,840,845,strokeColor=LIGHT,strokeWidth=1,strokeStyle="dashed",roundness={"type":3}))
add(text("ctlbl",950,162,"page content (shell)",14,150,18,strokeColor=LIGHT))
# --- greeting ---
add(text("greet",290,180,"Good morning, ดร. สมชาย",24,290,30,strokeColor=DARK))
add(text("sub",292,215,"ภาพรวมงานวิจัยและ task ของคุณวันนี้",14,240,18,strokeColor=MUT))
# --- summary cards ---
cards=[("c1",290,"i1","ct1","Proposals ของฉัน","cn1","3 proposals","ca1",505),
       ("c2",565,"i2","ct2","งานค้าง","cn2","2 tasks overdue","ca2",780),
       ("c3",840,"i3","ct3","ใกล้ครบกำหนด","cn3","4 due this week","ca3",1055)]
for cid,cx,iid,tid,ttl_,nid,num,aid,ax in cards:
    add(rect(cid,cx,250,250,80,strokeColor=GRAY,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}))
    add(rect(iid,cx+12,262,18,18,strokeColor=GRAY,strokeWidth=1,strokeStyle="dashed"))
    add(text(tid,cx+40,263,ttl_,14,140,18,strokeColor=MUT))
    add(text(nid,cx+12,292,num,20,160,25,strokeColor=DARK))
    add(text(aid,ax,292,"→",16,20,20,strokeColor=MID))
# --- task section ---
add(text("thead",290,355,"Task ที่ต้องทำเร็ว ๆ นี้",18,220,22,strokeColor=DARK))
lbl_text["filtl"]="Filter: All"
els+=labeled(rect("filt",620,352,110,28,strokeColor=MID,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}),"filtl",14,MID,650,359,90,18,n())
lbl_text["pbtnl"]="+ Create Plan"
els+=labeled(rect("pbtn",880,350,160,34,strokeColor=DARK,strokeWidth=2,backgroundColor=CARD,fillStyle="solid",roundness={"type":3}),"pbtnl",16,DARK,930,358,110,20,n())
add(rect("tl",290,400,750,250,strokeColor=GRAY,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}))
rows=[("เก็บข้อมูลสนามเพิ่มเติม","NSF Grant","due Fri",False),
      ("แก้ revision ตามโน้ต","Synthesis Paper","due Mon",False),
      ("อัปโหลด ethics form","NSF Grant","overdue 2d",True),
      ("ส่ง draft บทที่ 3","Synthesis Paper","due in 3d",False),
      ("นัดประชุม committee","Seed Grant","due in 6d",False)]
for i,(name,tag,due,red) in enumerate(rows):
    y=415+i*50; col=RED if red else DARK; scol=RED if red else GRAY
    add(rect(f"cb{i+1}",300,y,18,18,strokeColor=col,strokeWidth=1))
    add(text(f"tn{i+1}",328,y,name,14,200,18,strokeColor=col))
    lbl_text[f"tb{i+1}l"]=tag
    els+=labeled(rect(f"tb{i+1}",560,y-2,170,22,strokeColor=scol,strokeWidth=1,backgroundColor=PANEL,fillStyle="solid",roundness={"type":3}),f"tb{i+1}l",14,RED if red else MID,600,y+4,110,18,n())
    add(text(f"td{i+1}",950,y,due,14,90,18,strokeColor=RED if red else MID))
# --- plans section ---
add(text("phead",290,668,"Plans ของฉัน",18,130,22,strokeColor=DARK))
plans=[("pc1",290,"pn1","NSF Grant Proposal","pb1","Draft",440,90,"pr1","prf1",92,"pp1","40%","pd1","due 30 Sep 2026"),
       ("pc2",565,"pn2","Synthesis Paper","pb2","รอ Approve",665,110,"pr2","prf2",184,"pp2","80%","pd2","due 15 Oct 2026"),
       ("pc3",840,"pn3","Seed Grant","pb3","Approved",990,90,"pr3","prf3",230,"pp3","100%","pd3","due 1 Dec 2026")]
for cid,cx,nid,name,bid,st,bx,bw,prid,prfid,fill,pid,pct,did,due in plans:
    add(rect(cid,cx,700,250,130,strokeColor=GRAY,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}))
    add(text(nid,cx+10,710,name,16,150,20,strokeColor=DARK))
    lbl_text[bid+"l"]=st
    els+=labeled(rect(bid,bx,708,bw,22,strokeColor=GRAY,strokeWidth=1,backgroundColor=PANEL,fillStyle="solid",roundness={"type":3}),bid+"l",14,MID,bx+10,713,bw-20,18,n())
    add(rect(prid,cx+10,750,230,12,strokeColor=MID,strokeWidth=1))
    add(rect(prfid,cx+10,750,fill,12,strokeColor="transparent",backgroundColor=MID,fillStyle="solid",strokeWidth=0))
    add(text(pid,cx+10,768,pct,14,40,18,strokeColor=MID))
    add(text(did,cx+10,795,due,14,110,18,strokeColor=MUT))
# --- notifications ---
add(rect("nbox",290,860,750,125,strokeColor=GRAY,strokeWidth=1,backgroundColor=W,fillStyle="solid",roundness={"type":3}))
add(text("ntitle",300,868,"Notification ล่าสุด",16,150,20,strokeColor=DARK))
add(text("ni1",300,895,"แผน 'Synthesis Paper' ถูกส่งให้ committee แล้ว",14,320,18,strokeColor=MID))
add(text("ni2",300,920,"task 'อัปโหลด ethics form' เลยกำหนด 2 วัน",14,300,18,strokeColor=MID))
add(text("ni3",300,945,"ความคืบหน้า NSF Grant อัปเดตโดย admin",14,280,18,strokeColor=MID))
# --- annotations ---
anns=[("circH","H",60,1040,"annH","Admin เข้าหน้านี้ได้ในโหมด admin",None,None),
      ("circE","E",400,1040,"annE","กดแถว → เปิด Task Detail (R4)","arrE",[[0,0],[185,-380]]),
      ("circF","F",630,1040,"annF","กดการ์ด → Plan Detail (R3)","arrF",[[0,0],[95,-203]]),
      ("circG","G",890,1040,"annG","Notification เต็มรูปแบบอยู่ที่\ndropdown ของ bell (top bar)","arrG",[[0,0],[98,-908]])]
for cid,letter,cx,cy,aid,atxt,arid,pts in anns:
    lbl_text[cid+"l"]=letter
    els+=labeled(ell(cid,cx,cy,30,30,strokeColor=DARK,strokeWidth=1),cid+"l",16,DARK,cx+10,cy+5,10,20,n())
    w=250 if "\n" in atxt else 230
    h=36 if "\n" in atxt else 18
    add(text(aid,cx+40,cy+2,atxt,14,w,h,strokeColor=MID))
    if arid: add(arrow(arid,cx+15,cy-2,pts,strokeColor=GRAY,strokeWidth=1))

scene={"type":"excalidraw","version":2,"source":"https://excalidraw.com",
       "elements":els,"appState":{"viewBackgroundColor":"#ffffff","gridSize":None},"files":{}}
out="/home/nummmm/Projects/uni/open_sci_dpm/diagrams/wireframe/v1/H1-home-researcher.excalidraw"
with open(out,"w") as f: json.dump(scene,f,ensure_ascii=False,indent=1)
assert all(set(e)>= {"type","id","x","y","width","height"} for e in els)
ids=[e["id"] for e in els]; assert len(ids)==len(set(ids)), "dup ids"
print(out, len(els), "elements")
