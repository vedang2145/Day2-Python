Choice = int(input("Enter Your Choice (1,2,3,4,5) : "))

if(Choice == 1):
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    result = num1 + num2
    print("Addition = ",result)

elif(Choice==2):
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))    
    result = num1 - num2
    print("Subtraction = ",result)

elif(Choice==3):
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    result = num1 * num2
    print("Multiplication = ",result)

elif(Choice==4):
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    result = num1 / num2
    print("Division = ",result)

elif(Choice==5):
    num = int(input("Enter The Number : "))
    fact = 1
    for i in range(1,num+1):
        fact = fact * i

    print("Factorial = ",fact)

else:
    print("You enter the invalid number")        
