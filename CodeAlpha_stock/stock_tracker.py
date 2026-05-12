import matplotlib.pyplot as plt
stocks={
    "GOOGLE":180,
    "RELIANCE":350,
    "AMAZON":140,
    "TSLA":300
}
protfolio={}
total=0

n=int(input("How Many Stocks Do You Want To Enter?"))

for i in range(n):
    name=input("Enter Stock Name:").upper()
    qty=int(input("Enter Quantity:"))

    if name in stocks:
        protfolio[name]=qty
    else:
        print("Stock Not Found!")

investment_values=[]

for stock,qty in protfolio.items():
    price=stocks[stock]
    investment=price*qty
    investment_values.append(investment)
    total+=investment

print("Total Investment:",total)

with open("protfolio.txt","w")as file:
    file.write("Total Investment = "+str(total))

stock_names=list(protfolio.keys())

plt.bar(stock_names,investment_values)
plt.title("Stock Protfolio Investment")
plt.xlabel("Stocks")
plt.ylabel("Investment Value")
plt.show()


