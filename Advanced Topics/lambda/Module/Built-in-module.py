# importing buil-in module math 
import math 

# Using square root in math 
print(math.sqrt(25)) 

# Using pi function 
print(math.pi) 

# 2 radians = 114.59 degrees 
print(math.degrees(2)) 

# 60 degrees = 1.04 radians 
print(math.radians(60)) 

#sine of 2 radians 
print(math.sin(2)) 

#cosine of 0.5 radians 
print(math.cos(0.5)) 

# Tangent of 0.23 radians 
print(math.factorial(4)) 

# importing built in module random 
import random 

# printing random integer between 0 and 5 
print(random.randint(0,5)) 

# print random floating point number between 0 and 1 
print(random.random()) 

# random number between 0 and 100 
print (random.random() * 100)

list = [1,4,True, 800, 'python', 27, 'hello']

print(random.choice(list)) 


# importing built in module datetime 
import datetime 
from datetime import date 
import time 

print(time.time()) 

print(date.fromtimestamp(454554))