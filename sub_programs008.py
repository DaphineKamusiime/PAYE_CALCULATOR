
   #PAYE CALCULATOR
payment=float(input("enter your pay"))
if payment>0 and payment<25000:
    paye=0
elif payment>250000 and payment <350000:
    paye=0.1*(payment-250000)
elif payment<450000 and payment>350000:
    paye=10000+(0.2(payment-350000))
else:
    paye=30000+(0.3*(payment-450000))
print("paye= ",paye)       
   
   
   
   
   
    
