
print("Input capital: ")
capital = int(input())
print("Input interest: ")
interest = float(input())
print("Input years: ")
years = int(input())

count=1
total=0
paidout=0

quota = capital*(interest/100*pow(1+interest/100,years)/(1+interest/100, years)-1)
paidout += quota
while count != years:
    print("Year: ",count," - quota : ",quota,"€ - Paid out: ",total=total+paidout)

    count += 1