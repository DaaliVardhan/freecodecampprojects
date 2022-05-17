class Category:
  def __init__(self,cat):
    self.category=cat
    self.ledger=[]
  def deposit(self,amount,description=""):
    self.ledger.append({"amount":amount,"description":description})
    return self.ledger[0]
  def check_funds(self,amount):
    if amount>self.ledger[0]["amount"]:
      return False
    else:
      return True
    
  def withdraw(self,amount,description=""):
    if self.check_funds(amount):
      #self.ledger[0]["amount"]=self.ledger[0]["amount"]-amount
      self.ledger.append({"amount":-amount,"description":description})
      return True
    else:
      return False
  def get_balance(self):
    s=0
    for i in self.ledger:
      s+=i["amount"]
    return s
      
    
  def transfer(self,amount,b_category):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to {}".format(b_category.category))
      b_category.deposit(amount,"Transfer from {}".format(self.category))
      return True
    else:
      return False

  def __str__(self):
    line1=self.category.center(30,"*")+"\n"
    s=0
   
    for i in self.ledger:
      s+=i["amount"]
      f="{:.2f}".format(i["amount"])
      line1+=i["description"][:23].ljust(0) + f.rjust(30-len(i["description"][:23]))+"\n"
    line1+="Total: {:.2f}".format(s)
    return line1

  
  
      
def create_spend_chart(categories):
  spent_amounts = []
  for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    
  total = round(sum(spent_amounts), 2)
  p = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))
  line="Percentage spent by category\n"
  
  
  for i in reversed(range(0,110,10)):
    line+=f"{str(i)+'|':>4}"
    for j in p:
      if j>=i:
        line+=" o "
      else:
        line+="   "
    line+=" \n"
  line+=("-"*10).rjust(14)+"\n"
  arr=[]

  for i in categories:
    arr.append(i.category)

  height=(len(max(arr,key=len)))
  padded=[names.ljust(height) for names in arr]
  for name in zip(*padded):
    line+=" "*5+("  ".join(name))+"  \n"

  return line.strip("\n")





