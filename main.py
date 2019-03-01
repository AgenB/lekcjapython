import re
s = "gdfgd89.25.166.111gdfgfd"
w = re.search(r"[0-9A-Fa-f]+", s)
print(w)