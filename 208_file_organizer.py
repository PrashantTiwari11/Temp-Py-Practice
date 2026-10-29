from pathlib import Path
import shutil, sys

def main():
    folder=Path(sys.argv[1]).expanduser() if len(sys.argv)>1 else Path(".")
    if not folder.is_dir(): print("Not a folder:",folder); return
    groups={}
    for p in folder.iterdir():
        if p.is_file(): groups.setdefault(p.suffix.lower().lstrip(".") or "no_extension",[]).append(p)
    for ext,paths in sorted(groups.items()):
        print(f"{ext}/ ({len(paths)} file(s))")
        for p in paths: print("  ",p.name)
    if not groups: print("No files to organize."); return
    if input("Move files into extension folders? Type YES to confirm: ")!="YES": print("Preview only; no files moved."); return
    for ext,paths in groups.items():
        dest=folder/ext; dest.mkdir(exist_ok=True)
        for p in paths:
            target=dest/p.name
            if target.exists(): print("Skipped existing file:",target)
            else: shutil.move(str(p),str(target))
    print("Organization complete.")

if __name__ == "__main__": main()
