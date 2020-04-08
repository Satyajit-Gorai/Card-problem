no_of_cards=int(input("enter the number of cards:- "))
stk = []
for i in range(1,no_of_cards + 1):
    stk.append(i)
    
def stack():
    del stk[0]
    x = stk.pop(0)
    stk.append(x)
     
for i in range(len(stk)-1):
    stack()
    
for i in range(len(stk)):
    print(stk[i])
