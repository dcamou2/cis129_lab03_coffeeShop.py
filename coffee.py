#main 
#declare variables and constantsfor this program
#Input: Get imput from customer
#Processing: Calculate the total cost
#Output: Dispaly the reciept to the customer
#end main

coffee = 5
muffin = 4
coke = 2
cookie = 7

a=int(input("How many coffees would you like? "))
b=int(input("How many muffins would you like? "))
c=int(input("How many coke's would you like? "))
d=int(input("How many cookies would you like? "))

ax=coffee*a
bx=muffin*b
cx=coke*c
dx=cookie*d
taxx=(ax+bx+cx+dx)*0.06
total=ax+bx+cx+dx+taxx

print("***********************************")
print("Number of coffees bought: ")
print(a)
print("Number of muffins bought: ")
print(b)
print("Number of coke's bought: ")
print(c)
print("Number of cookies bought: ")
print(d)
print("***********************************")
print("  ")
print("***********************************")
print("My Coffee and Muffin Shop Receipt")
print(a,"Coffee at $5 each: $",ax)
print(b,"Muffins at $4 each: $",bx)
print(c,"Coke's at $2 each: $",cx)
print(d,"Cookies at $7 each: $",dx)
print("6% tax: ",f'{taxx:.2f}')
print("---------")
print("Total: $",f'{total:.2f}')
print("***********************************")
