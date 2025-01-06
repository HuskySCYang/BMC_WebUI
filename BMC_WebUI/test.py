
from collections import Counter
'''
s='aabbbccde'
s=sorted(s)
'''


s=[4,7,7,8,8,9,10]
'''
print(s)
gg=Counter(list(s))
print(gg)

for i,j in gg.most_common(3):
    print (i,j)
    if j != 1:
        for k in s:
            if k == i:
                print([s.index(k)])

'''



s1=s[::3]
print(s1)
