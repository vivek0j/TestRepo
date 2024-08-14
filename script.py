from datetime import datetime

def now():
  return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

if __name__==__main__:
  print(f'Hi, Current time is {now()}')
