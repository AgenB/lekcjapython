import re
x = re.search(r"\d\d-\d\d\d", "gfdfnfdxbgfh gfxbxfgh gfxhbxfgbh44-543")
print(x.string[x.start():x.end()])