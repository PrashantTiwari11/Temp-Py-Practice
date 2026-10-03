# 129_python_mini_event_planner.py
# Mini Event Planner - 10 practical features
events = [
    {"name":"Python Workshop","date":"2026-10-10","attendees":25,"budget":5000},
    {"name":"IoT Seminar","date":"2026-10-15","attendees":40,"budget":8000},
    {"name":"Coding Contest","date":"2026-10-20","attendees":60,"budget":12000},
]
print("1. Events:", events)
print("2. Event count:", len(events))
keyword="python"; print("3. Search:", [e for e in events if keyword in e["name"].lower()])
print("4. Sorted by date:", sorted(events, key=lambda e:e["date"]))
largest=max(events,key=lambda e:e["attendees"]); print("5. Largest event:",largest["name"],largest["attendees"])
print("6. Total attendees:",sum(e["attendees"] for e in events))
print("7. Total budget:",sum(e["budget"] for e in events))
print("8. Budget over 7000:",[e["name"] for e in events if e["budget"]>7000])
events.append({"name":"Web Development Meetup","date":"2026-10-25","attendees":30,"budget":6000})
print("9. Added event:",events[-1])
attendees=sum(e["attendees"] for e in events); budget=sum(e["budget"] for e in events)
print("10. Average budget per attendee:",round(budget/attendees,2))
