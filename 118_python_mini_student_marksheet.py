# 118_python_mini_student_marksheet.py
# Mini Student Marksheet - 10 practical features
student={"name":"Prashant","roll_no":101,"marks":{"Python":85,"DSA":78,"IoT":92,"AWS":80,"DBMS":74}}
print("1. Student:",student["name"],student["roll_no"])
print("2. Marks:",student["marks"])
total=sum(student["marks"].values()); print("3. Total:",total)
average=total/len(student["marks"]); print("4. Average:",round(average,2))
hi=max(student["marks"],key=student["marks"].get); print("5. Highest:",hi,student["marks"][hi])
lo=min(student["marks"],key=student["marks"].get); print("6. Lowest:",lo,student["marks"][lo])
percentage=total/len(student["marks"]); print("7. Percentage:",round(percentage,2))
grade="A+" if percentage>=90 else "A" if percentage>=80 else "B" if percentage>=70 else "C" if percentage>=60 else "D"; print("8. Grade:",grade)
passed=[s for s,m in student["marks"].items() if m>=40]; print("9. Passed:",passed)
print("10. Marksheet:",{"name":student["name"],"roll_no":student["roll_no"],"total":total,"average":round(average,2),"percentage":round(percentage,2),"grade":grade})
