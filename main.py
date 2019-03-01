import re
s = "fgdbgsdddgbfdbgfgbvdfvgdhfgbfdx"
w = re.findall(r"d.(?!f)", s)
print(w)