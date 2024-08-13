"""
a  30
b  40
c  50
d  70
"""

d = {}

for i in range(4):
    key, value = input().split()
    print(key,value)
    d.update({key:int(value)})

print(d)
