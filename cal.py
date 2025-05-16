value1=float(input("enter first value"))
op=input("enter operator  + - / * ")
value2=float(input("enter second value"))

if op=="+":
    result=value1+value2
    print("addition of two number",result)
elif op=="-":
    result=value1-value2
    print("subtraction of two number",result)
elif op=="*":
    result=value1*value2
    print("multiplication of two number",result)
elif op=="/":
    if value2!=0:
        result=value1/value2
        print("division of two numbers",result)
else:
    print("your entered wrong operator ")


        
