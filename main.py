import re
s = "<b>ala{a} (m[costam]a) k[o]ta</b>"
w = re.search(r"(?P<cos>[a]).(?P=cos)", s)
print(w)