h={"a":56,"b":65,"c":"surbhi"}
print(h["a"])
#print(dir(h))
print(h.items())
h["sonam"]=[2,4]

for i in h:
    print(i)
for i,j in h.items():
    print(i,j)
