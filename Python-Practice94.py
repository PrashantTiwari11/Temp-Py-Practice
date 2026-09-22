# 87_python_data_cleaning.py
# Data Cleaning - 10 practical programs/features
raw_names = ["  Prashant ", "AMAN", "Riya  ", "", "  raj"]
raw_ages = ["20", " 21", "unknown", "19", "", "22"]
raw_emails = ["p@example.com", "invalid", "r@example.com", ""]

print("1. Trimmed:", [x.strip() for x in raw_names])
print("2. Standardized:", [x.strip().title() for x in raw_names if x.strip()])
emails = [x.strip() for x in raw_emails if x.strip()]
print("3. Non-empty emails:", emails)

ages = []
for value in raw_ages:
    try: ages.append(int(value.strip()))
    except ValueError: pass
print("4. Valid ages:", ages)

duplicates = ["Aman", "Riya", "Aman", "Raj", "Riya"]
print("5. Remove duplicates:", list(dict.fromkeys(duplicates)))

def valid_email(e): return "@" in e and "." in e.split("@")[-1]
print("6. Valid emails:", [e for e in emails if valid_email(e)])

data = {"name": "Prashant", "age": None, "city": "", "course": "B.Tech"}
print("7. Missing values:", sum(v is None or v == "" for v in data.values()))

scores = [40, 60, 80, 100]
lo, hi = min(scores), max(scores)
print("8. Normalized:", [(x-lo)/(hi-lo) for x in scores])

values = [10, 11, 12, 13, 14, 15, 100]
q1, q3 = 11, 15
iqr = q3 - q1
filtered = [x for x in values if q1-1.5*iqr <= x <= q3+1.5*iqr]
print("9. IQR filtered:", filtered)

records = [{"name": "  Prashant", "marks": "85"}, {"name": "Riya ", "marks": "91"}, {"name": "", "marks": "invalid"}]
clean = []
for r in records:
    try: marks = int(r["marks"])
    except ValueError: continue
    name = r["name"].strip()
    if name: clean.append({"name": name.title(), "marks": marks})
print("10. Clean records:", clean)
