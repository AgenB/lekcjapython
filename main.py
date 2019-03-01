import re
s = "fgdbgsdddgbfdbgfgbvdfvgjdhfgbfdx"
w = re.findall(r"(?<=j)d.", s)
print(w)