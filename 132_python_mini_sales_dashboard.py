# 132_python_mini_sales_dashboard.py
# Mini Sales Dashboard - 10 practical features
sales=[
    {"product":"Laptop","category":"Electronics","units":3,"price":55000},
    {"product":"Mouse","category":"Accessories","units":10,"price":500},
    {"product":"Keyboard","category":"Accessories","units":7,"price":900},
    {"product":"Monitor","category":"Electronics","units":4,"price":12000},
]
print("1. Sales:",sales)
print("2. Product types:",len(sales))
for item in sales: item["revenue"]=item["units"]*item["price"]
print("3. Revenue per product:",[(x["product"],x["revenue"]) for x in sales])
total=sum(x["revenue"] for x in sales); print("4. Total revenue:",total)
print("5. Units sold:",sum(x["units"] for x in sales))
best=max(sales,key=lambda x:x["revenue"]); print("6. Highest revenue:",best["product"],best["revenue"])
print("7. Revenue ranking:",[(x["product"],x["revenue"]) for x in sorted(sales,key=lambda x:x["revenue"],reverse=True)])
print("8. Electronics:",[x["product"] for x in sales if x["category"]=="Electronics"])
category_revenue={}
for item in sales: category_revenue[item["category"]]=category_revenue.get(item["category"],0)+item["revenue"]
print("9. Category revenue:",category_revenue)
print("10. Average revenue:",round(total/len(sales),2))
