menu={
    "Coffee:":100,
    "Tea:":80,
    "Pizza:":200,
    "Biscuit":20,
    "Pasta:":150
    }
global total
total=0
print("*******WELCOME TO CAFE*******")
print("MENU:")
for key,value in menu.items():
    print(f"{key}{value}")
while True:
    order=input("Please Tell Me your Order Sir:")
    if order=="Tea":
        total=total+80
    elif order=="Coffee":
        total=total+100
    elif order=="Pizza":
        total=total+200
    elif order=="Biscuit":
        total=total+20
    elif order=="pasta":
        total=total+150
    else:
        pass
            
    reorder=input(f"Your order \"{order}\" Conformed Anything Else?")
    if reorder=="Yes":
        pass
    else:
        print("Your Order SuccessFull Please wait Some Time",)
        print("TOTAL BILL:",total)
        break
    

