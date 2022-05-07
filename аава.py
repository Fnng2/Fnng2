import random
a=random.randint(1,3)
if a==1:
    b='бумага'
if a==2:
    b="камень"
if a==3:
    b="ножницы"

vopros1=input("Выбери камень, ножницы или бумага")
print(b)
if vopros1==b:
    print("ничья")
if vopros1=="камень":
    if b=="бумага":
        print("ты проиграл")
    if b=="ножницы":
        print("ты выйграл")
if vopros1=="ножницы":
    if b=="камень":
        print("ты проиграл")
    if b=="бумага":
        print("ты выйграл")
if vopros1=="бумага":
    if b=="ножницы":
        print("ты проиграл")
    if b=="камень":
        print("ты выйграл")