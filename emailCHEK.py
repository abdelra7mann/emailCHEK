import re
user_Email = input('place write your Email ') 
x = re.findall(r"[A-z0-9\.]+@[a-z]+\.com|net", user_Email)
print(x)
if x :
  print("This is A Valid Email")
else:
  print("This is Not A Valid Email")
