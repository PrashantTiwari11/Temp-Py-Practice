# 137 - Job Application Tracker: 10 practical features
applications = [
    {"company": "TechNova", "role": "Python Intern", "status": "Applied", "date": "2026-09-20"},
    {"company": "CodeWorks", "role": "Backend Intern", "status": "Interview", "date": "2026-09-22"},
    {"company": "DataNest", "role": "Data Analyst Intern", "status": "Rejected", "date": "2026-09-25"},
    {"company": "CloudBase", "role": "Cloud Intern", "status": "Offer", "date": "2026-09-28"},
]
# 1. Display applications
def show_applications():
    for a in applications:
        print(f"{a['company']} | {a['role']} | {a['status']} | {a['date']}")
# 2. Count applications
def count_applications(): return len(applications)
# 3. Search by company
def search_company(query):
    return [a for a in applications if query.lower() in a["company"].lower()]
# 4. Filter by status
def filter_status(status):
    return [a for a in applications if a["status"].lower() == status.lower()]
# 5. Count each status
def status_summary():
    result = {}
    for a in applications: result[a["status"]] = result.get(a["status"], 0) + 1
    return result
# 6. Add an application
def add_application(company, role, status="Applied", date="Not set"):
    allowed = {"Applied", "Interview", "Rejected", "Offer", "Withdrawn"}
    if status not in allowed: raise ValueError("Invalid status.")
    applications.append({"company": company, "role": role, "status": status, "date": date})
# 7. Update application status
def update_status(company, new_status):
    allowed = {"Applied", "Interview", "Rejected", "Offer", "Withdrawn"}
    if new_status not in allowed: raise ValueError("Invalid status.")
    for a in applications:
        if a["company"].lower() == company.lower():
            a["status"] = new_status
            return True
    return False
# 8. Get interview-stage applications
def interview_applications(): return filter_status("Interview")
# 9. Calculate offer rate
def offer_rate():
    return round(len(filter_status("Offer")) / len(applications) * 100, 1) if applications else 0
# 10. Print dashboard
def report():
    print("JOB APPLICATION DASHBOARD")
    show_applications()
    print("Total:", count_applications(), "| Statuses:", status_summary(), "| Offer rate:", str(offer_rate()) + "%")
if __name__ == "__main__": report()
