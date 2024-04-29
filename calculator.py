# calculator 
def add(a,b):
    return a +b
def sub(a,b):
    return a - b
def mul(a,b):
    return a *b
def div(a,b):
    if b == 0 :
        return "error"
    else:
        return a / b
    
print("1 for addition")
print("2 for subtraction")
print("3 for multipication")
print("4  for divison")
while True:
    choice = input("enter ur number in between (1/2/3/4):  ")
    if choice in ('1','2','3','4'):
        a = float(input("Enter ur first number:"))
        b = float(input("Enter ur second number:"))

        if choice == '1':
            print("addition of two number is =",add(a,b))
        elif choice == '2':
            print("subtraction  of two number is =", sub(a,b))
        elif choice == '3':
            print("multipication of two number is =",mul(a,b))
        elif choice == '4':
            print("divison of two number is =", div(a,b))
        break
    else:
        print("invalid")
