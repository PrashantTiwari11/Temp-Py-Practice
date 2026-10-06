# 141 - Mini Study Planner: 10 practical features
subjects=[{"name":"Python","hours":6,"completed":4,"priority":"High"},{"name":"AWS","hours":5,"completed":2,"priority":"High"},{"name":"Compiler Design","hours":4,"completed":3,"priority":"Medium"},{"name":"IoT","hours":3,"completed":3,"priority":"Low"}]
# 1. Display subjects
def show_subjects():
    for s in subjects: print(f"{s['name']} | {s['completed']}/{s['hours']} hrs | {s['priority']}")
# 2. Count subjects
def subject_count(): return len(subjects)
# 3. Incomplete subjects
def incomplete_subjects(): return [s for s in subjects if s['completed']<s['hours']]
# 4. High-priority subjects
def high_priority(): return [s for s in subjects if s['priority'].lower()=='high']
# 5. Completion percentage
def completion(s): return round(min(s['completed']/s['hours'],1)*100,1) if s['hours'] else 0
# 6. Rank by progress
def rank_by_progress(): return sorted(subjects,key=completion,reverse=True)
# 7. Add study hours
def add_study_hours(name,hours):
    for s in subjects:
        if s['name'].lower()==name.lower(): s['completed']+=hours; return True
    return False
# 8. Add subject
def add_subject(name,hours,priority='Medium'): subjects.append({'name':name,'hours':hours,'completed':0,'priority':priority})
# 9. Total planned/completed hours
def total_hours(): return sum(s['hours'] for s in subjects),sum(s['completed'] for s in subjects)
# 10. Report
def report():
    show_subjects(); planned,done=total_hours(); print('Subjects:',subject_count(),'Planned:',planned,'Completed:',done); print('Incomplete:',[s['name'] for s in incomplete_subjects()])
if __name__=='__main__': report()
