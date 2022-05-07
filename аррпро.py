import random
a=random.randint(1,1000)

vopros1=int (input("Попробуй угадать число до тысячи"))
while vopros1!=a:
    if vopros1 < a:
        print("Больше")
    else:
        print("Меньше")
    vopros1=int (input("Угадай число до пяти тысячи"))                

print("Yes")