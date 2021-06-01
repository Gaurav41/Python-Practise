# import os
# files = os.listdir("C:\\Users\\NCS\\Desktop")
#
# for f in files:
#     print(f )

# import string
#
# s = "Hellow word !$%6 "
# print(string.punctuation)
# #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(string.whitespace)

import re
# str = "         33hello world  "
# print(str.strip())

import re

pattern = re.compile("htt.s")
str = "dsf https//"
x = re.match(pattern,str)
print(x.pos)
