'''This program calculates the mean,median and mode weights of people
using a csv file
It uses the csv module and collections module to do so'''

#importing the modules
import csv
from collections import Counter

#opening the csv file using csv's reader function and the inbuilt open function
with open ('SOCR-HeightWeight.csv',newline='') as f:
  reader = csv.reader(f)
  file = list(reader)

#removing the headers
file.pop(0)

#creating a mean function
def mean(data):
  weight = []
  for f in data:
    n = f[2]
    #appending the weights to the empty weight list
    weight.append(float(n))
  # print(weight)  
  l = len(weight)
  sum = 0
  for i in weight:
    sum += i
    #calculating the mean by dividing the total sum by the length of the list
  mean = sum/l
  #printing the mean weight in a 2d.p form
  print("The mean is: ","{:.2f}".format(mean),"pounds")
 

#creating a median function
def median(data):
    l = len(data)
    weight = []
    for f in data:
      n = f[2]
      #appending the weights to the empty weight list
      weight.append(float(n))
    #sorting the weight list  
    weight.sort()  
    #checking if the list has an odd number of data or even
    if l%2 == 0 :    
      m1 = (weight[int(l/2)])
      m2 = (weight[int((l/2)+1)])
      #getting the median by dividing the sums of the 2 middle values
      median =(m1+m2)/2
    else:
      #calculating the median by getting the middle term by dividing the length of data by 2  
      median = (weight[int(l/2)])
      #printing the median weight in a 2d.p form  
    print("The median is: ","{:.2f}".format(median),"pounds")


#creating a mode function
def mode(file):
  weight = []
  for f in file:
    n = f[2]
    #appending the weights to the empty weight list
    weight.append(float(n))
    #using the Counter function to create key value pairs of values and occurances
  data = Counter(weight)
    #using the key and value using a for loop
  for h,o in data.items():
      #checking if the occurance is the maximum occurance
      if o==max(data.values()):
            #printing the mode in 2d.p
            print("The mode is: ","{:.2f}".format(h),"pounds")
            
#calling out the functions
mode(file)
median(file) 
mean(file) 
