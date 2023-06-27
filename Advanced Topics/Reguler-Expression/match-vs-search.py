import re 

line = 'Cats are smart than dogs'

matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
    print("match --> matchObj.group() : "), matchObj.group()
else:
   print("No match!!") 

searchObj = re.search(r'dogs', line, re.M|re.I)
if searchObj:
    print("match --> matchObj.group() : ", searchObj.group())
else:
   print("No match!!") 