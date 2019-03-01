import re
s = "<b>ala ma kota</b>"
w = re.findall(r"<.*?>", s)
print(w)