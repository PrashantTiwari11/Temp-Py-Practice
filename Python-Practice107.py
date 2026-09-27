# 105_python_json_config_manager.py
# JSON Configuration Manager - 10 practical features
import json
from pathlib import Path
import tempfile

config = {
    "app": "StudentPortal",
    "version": 1.0,
    "debug": True,
    "features": ["attendance", "marks", "assignments"]
}

with tempfile.TemporaryDirectory() as folder:
    file = Path(folder) / "config.json"

    print("1. JSON string:", json.dumps(config, indent=2))
    file.write_text(json.dumps(config, indent=2), encoding="utf-8")
    print("2. File saved:", file.exists())

    loaded = json.loads(file.read_text(encoding="utf-8"))
    print("3. Loaded config:", loaded)
    print("4. App name:", loaded["app"])

    loaded["version"] = 1.1
    print("5. Updated version:", loaded["version"])

    loaded["theme"] = "dark"
    print("6. Added theme:", loaded["theme"])

    loaded["features"].append("results")
    print("7. Features:", loaded["features"])

    print("8. Debug enabled:", loaded.get("debug", False))

    file.write_text(json.dumps(loaded, indent=2), encoding="utf-8")
    print("9. Updated JSON saved:", file.exists())

    print("10. Summary:", {
        "app": loaded["app"],
        "version": loaded["version"],
        "feature_count": len(loaded["features"])
    })
