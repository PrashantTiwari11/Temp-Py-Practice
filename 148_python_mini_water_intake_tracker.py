# 148 - Mini Water Intake Tracker: 10 practical features
daily_target_ml = 2000
intake_log = [{"time":"08:00","amount_ml":250},{"time":"10:30","amount_ml":300},{"time":"13:00","amount_ml":400},{"time":"16:00","amount_ml":250}]
# 1. Display intake log
def show_log():
    for e in intake_log: print(f"{e['time']} - {e['amount_ml']} ml")
# 2. Total intake
def total_intake(): return sum(e["amount_ml"] for e in intake_log)
# 3. Remaining to target
def remaining_intake(): return max(0, daily_target_ml - total_intake())
# 4. Progress percentage
def progress_percent(): return round(total_intake() / daily_target_ml * 100, 1) if daily_target_ml > 0 else 0
# 5. Add intake entry
def add_intake(time, amount_ml):
    if amount_ml <= 0: raise ValueError("Amount must be positive.")
    intake_log.append({"time":time,"amount_ml":amount_ml})
# 6. Change target
def set_target(amount_ml):
    global daily_target_ml
    if amount_ml <= 0: raise ValueError("Target must be positive.")
    daily_target_ml = amount_ml
# 7. Check target status
def target_reached(): return total_intake() >= daily_target_ml
# 8. Largest entry
def largest_intake(): return max(intake_log, key=lambda e: e["amount_ml"], default=None)
# 9. Average per entry
def average_intake(): return round(total_intake() / len(intake_log), 1) if intake_log else 0
# 10. Daily report
def report():
    print("WATER INTAKE REPORT")
    show_log()
    print("Total:", total_intake(), "ml")
    print("Target:", daily_target_ml, "ml")
    print("Progress:", str(progress_percent()) + "%")
    print("Remaining:", remaining_intake(), "ml")
    print("Target reached:", target_reached())
if __name__ == "__main__": report()
