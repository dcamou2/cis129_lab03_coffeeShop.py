#main 
#declare variables and constantsfor this program
#Input: Get imput from customer
#Processing: Calculate the total cost
#Output: Dispaly the reciept to the customer
#end main

coffee = 5
muffin = 4

a=int(input("How many coffees would you like? "))
b=int(input("How many muffins would you like? "))

ax=coffee*a
bx=muffin*b
cx=(ax+bx)*0.06
total=ax+bx+cx

print("***********************************")
print("Number of coffees bought: ")
print(a)
print("Number of muffins bought: ")
print(b)
print("***********************************")
print("  ")
print("***********************************")
print("My Coffee and Muffin Shop Receipt")
print(a,"Coffee at $5 each: $",ax)
print(b,"Muffins at $4 each: $",bx)
print("6% tax: ",cx)
print("---------")
print("Total: $",total)
print("***********************************")