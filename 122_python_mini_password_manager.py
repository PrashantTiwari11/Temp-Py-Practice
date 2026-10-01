# 122_python_mini_password_manager.py
# Mini Password Manager Demo - 10 practical features
# Educational example using demo passwords only.

accounts = {
    "github": {"username": "prashant_dev", "password": "DemoPass123"},
    "email": {"username": "student@example.com", "password": "StudyPass456"},
    "college": {"username": "student101", "password": "College789"},
}

print("1. Accounts:", list(accounts))
print("2. Account count:", len(accounts))

keyword = "git"
print("3. Search:", [name for name in accounts if keyword in name.lower()])

site = "github"
print("4. GitHub exists:", site in accounts)

print("5. GitHub username:", accounts["github"]["username"])

for site, data in accounts.items():
    print("6.", site, "password length:", len(data["password"]))

accounts["linkedin"] = {"username": "student_dev", "password": "LinkedIn123"}
print("7. Added:", accounts["linkedin"])

accounts["github"]["password"] = "NewDemoPass456"
print("8. Updated GitHub password.")

accounts.pop("college")
print("9. Remaining accounts:", list(accounts))

print("10. Summary:", {
    "total_accounts": len(accounts),
    "sites": sorted(accounts.keys())
})
