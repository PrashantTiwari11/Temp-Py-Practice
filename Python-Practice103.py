# 101_python_log_analyzer.py
# Log Analyzer - 10 practical features

logs = [
    "INFO User login successful",
    "ERROR Database connection failed",
    "WARNING Low disk space",
    "INFO File uploaded",
    "ERROR Authentication failed",
    "INFO User logout",
    "WARNING High memory usage",
    "INFO Backup completed",
]

print("1. Total logs:", len(logs))
info = [x for x in logs if x.startswith("INFO")]
print("2. INFO count:", len(info))
errors = [x for x in logs if x.startswith("ERROR")]
print("3. ERROR count:", len(errors))
warnings = [x for x in logs if x.startswith("WARNING")]
print("4. WARNING count:", len(warnings))
print("5. Error messages:", [x.split(" ", 1)[1] for x in errors])
keyword = "failed"
print("6. Keyword matches:", [x for x in logs if keyword in x.lower()])
print("7. Severity summary:", {"INFO": len(info), "WARNING": len(warnings), "ERROR": len(errors)})
print("8. First error:", errors[0] if errors else "None")
print("9. Critical records:", [x for x in logs if "Database" in x or "Authentication" in x])
print("10. Report:", f"{len(errors)} errors, {len(warnings)} warnings, {len(info)} info messages")
