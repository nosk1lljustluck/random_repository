class supermarket():
    def __init__(self, supermarket_name):
        self.supermarket_name=supermarket_name
        self.profit=0
    
    def get_profit(self):
        return self.profit
    
    def buy(self):
        while True:
            a=input("What you want to buy? (press 0 to quit): ")
            if a=="0":break
            c=int(input("How much amount do you want to buy? "))
            buy_new_good=dict[a]()
            if buy_new_good.can_buy(c):buy_new_good.buy(c)
            self.profit+=buy_new_good.get_price()*c
    
class fresh_fruit():
    def __init__(self):
        self.price=2000
        self.available_amount=3000
    
    def get_price(self):
        return self.price
    
    def can_buy(self, amount):
        return 1 if self.available_amount>amount else 0
    
    def buy(self, amount):
        self.available_amount-=amount
        print("Here is your product, thanks! ")
        
class vegetables():
    def __init__(self):
        self.price=500
        self.available_amount=1500
        
    def get_price(self):
        return self.price
    
    def can_buy(self, amount):
        return 1 if self.available_amount>amount else 0
    
    def buy(self, amount):
        self.available_amount-=amount
        print("Here is your product, thanks! ")

dict={
      "fresh fruit": fresh_fruit,
      "vegetables": vegetables
      
      }   
    
LIDL=supermarket("Lidl")
LIDL.buy()
print(LIDL.get_profit())
        