total = 100
print("Your total is", total)
payed_amount = int(input("Enter the amount you want to pay: "))

def total_new(total, payed_amount):
    total = total - payed_amount
    print("Your due amount is", total)

if payed_amount == total:
    print("Your payment is complete")
else:
    total_new(total, payed_amount)
