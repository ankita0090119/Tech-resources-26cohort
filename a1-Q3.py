low = int(input ("Please, Enter the Lowest Range Value: "))  
high = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (low,high + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
      else:  
        print (number)
