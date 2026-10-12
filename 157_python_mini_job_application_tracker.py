"""157 Job Application Tracker: 10 features."""
apps=[]
def add(company,role,status="Applied",date=""): apps.append({"company":company,"role":role,"status":status,"date":date})
def all_apps(): return apps.copy()
def by_status(status): return [a for a in apps if a["status"].lower()==status.lower()]
def search_company(query): return [a for a in apps if query.lower() in a["company"].lower()]
def update_status(index,status): apps[index-1]["status"]=status
def status_counts():
    out={}
    for a in apps: out[a["status"]]=out.get(a["status"],0)+1
    return out
def interviews(): return by_status("Interview")
def followups(): return [a for a in apps if a["status"].lower() in {"applied","assessment"}]
def remove(index): return apps.pop(index-1)
def export_csv(path="job_applications.csv"):
    import csv
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["company","role","status","date"]); w.writeheader(); w.writerows(apps)
if __name__=="__main__":
    add("TechNova","Python Intern","Applied","2026-10-01"); add("DataWorks","Junior Developer","Interview","2026-10-03"); add("CloudBridge","Support Engineer","Assessment","2026-10-05")
    print("1 All:",all_apps()); print("2 Applied:",by_status("Applied")); print("3 Search:",search_company("data"))
    update_status(1,"Interview"); print("4 Updated:",apps[0]); print("5 Status counts:",status_counts())
    print("6 Interviews:",interviews()); print("7 Follow-ups:",followups())
    print("8 Remove with remove(index)"); print("9 Export CSV with export_csv()")
    print("10 Add using add(company, role, status, date)")
