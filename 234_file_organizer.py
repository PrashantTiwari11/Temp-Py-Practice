from pathlib import Path
import shutil

def organize(folder_path):
    folder = Path(folder_path).expanduser()
    if not folder.is_dir():
        print("Folder does not exist.")
        return
    moved = 0
    for item in folder.iterdir():
        if not item.is_file() or item.name.startswith("."):
            continue
        category = item.suffix.lower().lstrip(".") or "no_extension"
        target_folder = folder / category
        target_folder.mkdir(exist_ok=True)
        target = target_folder / item.name
        if target.exists():
            print(f"Skipped existing file: {item.name}")
            continue
        shutil.move(str(item), str(target))
        moved += 1
    print(f"Done. Files moved: {moved}")

if __name__ == "__main__":
    organize(input("Folder path to organize: ").strip())
