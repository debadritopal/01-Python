num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
opp=input("Enter operation: ")
result=0
ctrl=True
if(opp.lower()=="addition"):
    result=num1+num2
elif(opp.lower()=="subtraction"):
    result=num1-num2
elif(opp.lower()=="multipilication"):
    result=num1*num2
elif(opp.lower()=="division"):
    result=num1/num2    
elif(opp.lower()=="modulus"):
    result=num1%num2
elif(opp.lower()=="exponent"):
    result=num1**num2
else:
    print("Invalid operation")
    ctrl=False
if(ctrl):
    print(f"{opp} result: {result}")