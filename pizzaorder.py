size = input("What size pizza you want(S/M/L)?")
bill=0
if size == 'S' or size == 's':
    bill += 150
    print("small pizza price is Rs.100.")
elif size == 'M' or size == 'm':
     bill += 230
     print("Medium pizza price is Rs.200.")
else:
     bill += 320
     print("Large pizza price is Rs.300.")
add_pepperoni =input("Do you want pepperoni(Y/N)?")
if add_pepperoni =='Y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        bill += 60
    else:
        bill +=20
extra_cheese= input("Do you want extra cheese(Y/N)?")
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 30

extra_drinks= input("Do you want extra drinks(Y/N)?")
if extra_drinks == 'Y' or extra_drinks == 'y':
    bill += 30

extra_fries= input("Do you want fries(Y/N)?")
if extra_fries == 'Y' or extra_fries == 'y':
    bill += 20

print(f"your final bill is {bill}")