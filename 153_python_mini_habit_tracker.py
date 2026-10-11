"""153 Habit Tracker — 10 features."""
from datetime import date
habits={}
def add_habit(name): habits.setdefault(name,set())
def log_habit(name,day=None):
    if name not in habits: raise KeyError("Add habit first")
    habits[name].add(day or date.today().isoformat())
def completed_today(name): return date.today().isoformat() in habits.get(name,set())
def count(name): return len(habits.get(name,set()))
def all_habits(): return {n:sorted(ds) for n,ds in habits.items()}
def date_range_count(name,start,end): return sum(start<=d<=end for d in habits.get(name,set()))
def remove_habit(name): return habits.pop(name,None)
def best_habit(): return max(habits,key=lambda n:len(habits[n]),default=None)
def save(path="habits.txt"):
    with open(path,"w",encoding="utf-8") as f:
        for n,ds in habits.items(): f.write(f"{n}|{','.join(sorted(ds))}\n")
def summary(): return {n:len(ds) for n,ds in habits.items()}
if __name__=="__main__":
    add_habit("Read"); add_habit("Exercise"); log_habit("Read"); log_habit("Exercise")
    print("1 Add habit: add_habit(name)"); print("2 Log: log_habit(name)")
    print("3 Completed today:",completed_today("Read")); print("4 Count:",count("Read"))
    print("5 All logs:",all_habits()); print("6 Date-range count:",date_range_count("Read","2026-01-01","2026-12-31"))
    print("7 Best habit:",best_habit()); print("8 Summary:",summary())
    print("9 Save with save()"); print("10 Remove with remove_habit(name)")
