import re
s = "<b>al{a} (ma) k[o]ta</b>"
w = re.findall(r"[<\{\(\[].*?[\]\)\}>]", s)
print(w)