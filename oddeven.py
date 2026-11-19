
import math
import os
import random
import re
import sys

n = int(input("enter no.").strip())
if 1<=n<=100:     
   if n%2!=0:
    print("wierd")
   elif 2<=n<=5:
    print("not wierd")
   elif 6<=n<=20:
    print("wierd")  
   else:
    print("Not wierd")  
else:
    print("No. should be in 1 to 100")      