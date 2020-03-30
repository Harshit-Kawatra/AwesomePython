def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1/num2

print("Choose operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice:")

num1= float(input("Enter first number"));
num2= float(input("Enter second number"))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice=='3':
    print(num1,"X",num2,"=",mul(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",divide(num1,num2))
else :
    print("Invalid input")