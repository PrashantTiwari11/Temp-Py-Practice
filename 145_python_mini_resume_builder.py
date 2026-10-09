# 145 - Mini Resume Builder: 10 practical features
profile = {"name":"Your Name","email":"you@example.com","phone":"000-000-0000","summary":"Computer Engineering student interested in software development.","skills":["Python","SQL","HTML","Git"],"education":["B.Tech Computer Engineering"],"projects":["Expense Tracker","Student Management System"],"certifications":["Python Basics"]}
# 1. Display contact details
def show_contact():
    print(profile["name"], profile["email"], profile["phone"], sep=" | ")
# 2. Update a field
def update_field(field, value):
    if field not in profile: raise KeyError("Unknown profile field.")
    profile[field] = value
# 3. Add skill without duplicates
def add_skill(skill):
    if skill and skill.lower() not in [s.lower() for s in profile["skills"]]: profile["skills"].append(skill)
# 4. Remove skill
def remove_skill(skill):
    for item in profile["skills"]:
        if item.lower() == skill.lower(): profile["skills"].remove(item); return True
    return False
# 5. Add project
def add_project(project):
    if project and project not in profile["projects"]: profile["projects"].append(project)
# 6. Add education
def add_education(course):
    if course: profile["education"].append(course)
# 7. Add certification
def add_certification(certificate):
    if certificate: profile["certifications"].append(certificate)
# 8. Generate plain-text resume
def generate_resume():
    sections = [profile["name"], profile["email"], profile["phone"], "", "SUMMARY", profile["summary"], "", "SKILLS", ", ".join(profile["skills"]), "", "EDUCATION"]
    sections += ["- " + x for x in profile["education"]]
    sections += ["", "PROJECTS"] + ["- " + x for x in profile["projects"]]
    sections += ["", "CERTIFICATIONS"] + ["- " + x for x in profile["certifications"]]
    return "\n".join(sections)
# 9. Save resume to text file
def save_resume(filename="resume.txt"):
    with open(filename, "w", encoding="utf-8") as f: f.write(generate_resume())
    return filename
# 10. Completeness checklist
def completeness_check():
    return {key: bool(profile.get(key)) for key in ("name","email","phone","summary","skills","education","projects")}
if __name__ == "__main__":
    print(generate_resume())
    print("Checklist:", completeness_check())
