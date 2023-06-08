'''
Operatori:
aritmetici: +, -, *, /, %
de comparare: < >,==, !=, >=, <=
logici: and ,or , !

Flow control - if , else.
'''

a=3
b=5
print( a + b ) # 3+5=>8
print(a == b) #a este egal cu b => False
print(a < b and a < 4) #True si True => True
print(a < b or a < 2) #True sau False => True

# cu mama sau cu tata sau (cu bunicul si bunica)

mama= False
tata = False
bunicul = True
bunica = True
print (mama or tata or (bunicul and bunica))