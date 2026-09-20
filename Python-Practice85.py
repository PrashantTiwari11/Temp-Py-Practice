# 79_python_design_patterns.py
# Common Design Patterns - 10 practical programs/features

class Config:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls); cls._instance.debug=True
        return cls._instance
c1,c2=Config(),Config(); print('1. Singleton same object:',c1 is c2)

class EmailNotification:
    def send(self,message): return 'Email: '+message
class SMSNotification:
    def send(self,message): return 'SMS: '+message
def notification_factory(kind): return EmailNotification() if kind=='email' else SMSNotification()
print('2. Factory:',notification_factory('email').send('Hello'))

class AddStrategy:
    def execute(self,a,b): return a+b
class MultiplyStrategy:
    def execute(self,a,b): return a*b
def calculate(strategy,a,b): return strategy.execute(a,b)
print('3. Strategy:',calculate(AddStrategy(),5,3)); print('4. Another strategy:',calculate(MultiplyStrategy(),5,3))

class Observer:
    def update(self,message): print('Observer received:',message)
class Subject:
    def __init__(self): self.observers=[]
    def attach(self,observer): self.observers.append(observer)
    def notify(self,message):
        for observer in self.observers: observer.update(message)
subject=Subject(); subject.attach(Observer()); subject.notify('New notification'); print('5. Observer: notification sent')

class OldPrinter:
    def print_text(self,text): return 'Old printer: '+text
class PrinterAdapter:
    def __init__(self,printer): self.printer=printer
    def print(self,text): return self.printer.print_text(text)
print('6. Adapter:',PrinterAdapter(OldPrinter()).print('Report'))

class User:
    def __init__(self,name,age,city): self.name,self.age,self.city=name,age,city
class UserBuilder:
    def __init__(self): self.name,self.age,self.city='Unknown',0,'Unknown'
    def set_name(self,name): self.name=name; return self
    def set_age(self,age): self.age=age; return self
    def set_city(self,city): self.city=city; return self
    def build(self): return User(self.name,self.age,self.city)
user=UserBuilder().set_name('Prashant').set_age(20).set_city('India').build(); print('7. Builder:',user.__dict__)

class Light:
    def on(self): return 'Light ON'
class TurnOnCommand:
    def __init__(self,light): self.light=light
    def execute(self): return self.light.on()
print('8. Command:',TurnOnCommand(Light()).execute())

class StudentRepository:
    def __init__(self): self.students=[]
    def add(self,name): self.students.append(name)
    def all(self): return self.students[:]
repo=StudentRepository(); repo.add('Prashant'); repo.add('Riya'); print('9. Repository:',repo.all())

class MessageService:
    def send(self,text): return 'Message: '+text
class UserService:
    def __init__(self,service): self.service=service
    def notify(self,text): return self.service.send(text)
print('10. Dependency injection:',UserService(MessageService()).notify('Welcome'))
