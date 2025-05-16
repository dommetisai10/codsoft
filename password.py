#generate password
import random
digits=['0','1','2','3','4','5','6','7','8','9']
alphabets=['a','b','c','d','e','f','g','h','i','j','k',
           'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['@','#','$','*']
All=digits+alphabets+symbols
length=12
for i in range(0,length):
    password=''.join(random.choices(All))
    print(password,end='')
