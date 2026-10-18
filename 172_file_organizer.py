"""172 File Organizer: preview and sort files into extension-named folders."""
from pathlib import Path
import shutil

def destination(path):
    folder = path.suffix.lower().lstrip(".").upper() or "NO_EXTENSION"
    return path.parent / folder / path.name

def main():
    raw = input("Folder path to organize: ").strip().strip('"')
    folder = Path(raw).expanduser()
    if not folder.is_dir():
        print("Folder not found."); return
    folder = folder.resolve()
    moves = []
    for source in folder.iterdir():
        if not source.is_file() or source.name.startswith("."): continue
        target = destination(source)
        if target == source: continue
        if target.exists():
            n = 1
            while (target.parent / f"{target.stem}_{n}{target.suffix}").exists(): n += 1
            target = target.parent / f"{target.stem}_{n}{target.suffix}"
        moves.append((source, target))
    if not moves:
        print("No files to organize."); return
    print(f"Preview: {len(moves)} file(s)")
    for src, dst in moves: print(f"  {src.name} -> {dst.parent.name}/{dst.name}")
    if input("Type MOVE to confirm: ").strip() != "MOVE":
        print("Cancelled; no files moved."); return
    done = 0
    for src, dst in moves:
        try:
            dst.parent.mkdir(parents=True, exist_ok=True)
            final = dst
            n = 1
            while final.exists():
                final = dst.parent / f"{dst.stem}_{n}{dst.suffix}"; n += 1
            shutil.move(str(src), str(final)); done += 1
        except OSError as exc: print(f"Skipped {src.name}: {exc}")
    print(f"Finished: moved {done}/{len(moves)} files.")
if __name__ == "__main__": main()
