# 131_python_mini_fitness_tracker.py
# Mini Fitness Tracker - 10 practical features
daily_steps={"Monday":6500,"Tuesday":8200,"Wednesday":10400,"Thursday":7200,"Friday":9000,"Saturday":12000,"Sunday":5800}
print("1. Daily steps:",daily_steps)
total=sum(daily_steps.values()); print("2. Weekly total:",total)
print("3. Daily average:",round(total/len(daily_steps),2))
best=max(daily_steps,key=daily_steps.get); print("4. Best day:",best,daily_steps[best])
low=min(daily_steps,key=daily_steps.get); print("5. Lowest day:",low,daily_steps[low])
goal=8000; goal_days=[d for d,s in daily_steps.items() if s>=goal]
print("6. Goal days:",goal_days)
print("7. Below goal:",[d for d,s in daily_steps.items() if s<goal])
print("8. Goal completion:",round(len(goal_days)/len(daily_steps)*100,2),"%")
daily_steps["Next Monday"]=7500; print("9. Added data:",daily_steps["Next Monday"])
print("10. Report:",{"days_recorded":len(daily_steps),"total_steps":sum(daily_steps.values()),"average_steps":round(sum(daily_steps.values())/len(daily_steps),2)})
