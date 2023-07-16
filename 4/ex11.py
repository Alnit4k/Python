a = []
b = []
c = []

for i in range(10):
    an = int(input("Enter {}st number --> " .format(i+1)))
    bn = int(input("Enter --> "))
    cn = int(input("Enter --> "))
    a.append(an)
    b.append(bn)
    c.append(cn)
    
    d = a + b + c 
    
print(d[1:11])
print(d)