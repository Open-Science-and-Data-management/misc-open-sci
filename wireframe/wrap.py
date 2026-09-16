#!/usr/bin/env python3
"""Wrap a bare elements-array .excalidraw file into a loadable Excalidraw scene."""
import json, sys

for path in sys.argv[1:]:
    d = json.load(open(path))
    if isinstance(d, list):
        scene = {
            "type": "excalidraw",
            "version": 2,
            "source": "https://excalidraw.com",
            "elements": d,
            "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None},
            "files": {},
        }
        json.dump(scene, open(path, "w"), ensure_ascii=False)
        print(f"wrapped {len(d)} elements -> {path}")
    else:
        d["elements"] = [e | {"fontFamily": 2} if e.get("type") == "text" else e for e in d["elements"]]
        json.dump(d, open(path, "w"), ensure_ascii=False)
        print(f"fontFamily -> 2 (Nunito) for {path}")
