num1=int(input("enter 1st integer:"))
num2=int(input("enter 2nd integer:"))
 
HCF = 1
 
for i in range(2,num1+1):
    if(num1%i==0 and num2%i==0):
        HCF = i
 
print("First Number is: ",num1)
print("Second Number is: ",num2)
print("HCF of the numbers is: ",HCF)
