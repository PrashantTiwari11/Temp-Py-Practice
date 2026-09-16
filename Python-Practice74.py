# 68_api_and_json_basics.py
# APIs and JSON Basics - 10 practical programs/features
import json
from urllib.parse import urlencode,urlparse,parse_qs
user={'name':'Prashant','age':20,'course':'Computer Engineering'}
print('1. Dictionary:',user)
text=json.dumps(user,indent=2);print('2. JSON:',text)
decoded=json.loads(text);print('3. Decoded name:',decoded['name'])
students=[{'name':'Aman','marks':82},{'name':'Riya','marks':91}];print('4. JSON list:',json.dumps(students))
query=urlencode({'search':'python','page':2});print('5. Query:',query)
parsed=urlparse('https://example.com/products?search=python&page=2');print('6. Host:',parsed.netloc)
print('7. Query values:',parse_qs(parsed.query))
nested={'student':{'name':'Prashant','skills':['Python','SQL','Git']}};print('8. Nested skill:',nested['student']['skills'][0])
try:json.loads('{invalid json}')
except json.JSONDecodeError:print('9. Invalid JSON handled safely.')
request={'method':'GET','endpoint':'/users','params':{'limit':10}};print('10. API request object:',request)
