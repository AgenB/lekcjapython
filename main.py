import re
s = "gdfgd89.25.166.111gdfgfd"
w = re.search(r"(\d{1,3}\.){3}\d{1,3}", s)
print(w)