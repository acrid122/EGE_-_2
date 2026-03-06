with open('24_26549.txt') as f:
    s = f.readline().strip().split('2025')

#['XX', 'XZZX', 'ZXYTXC', 'ZYZ', 'XTYY', 'XZYXYYX',  'XYXYX']
s = 'XX2025XZZX2025ZXYTXC2025ZYZ2025XTYY2025XZYXYYX2025XYXYX'.split('2025')

'''
XX2025XZZX2025
025XZZX2025ZXYTXC2025
025ZXYTXC2025ZYZ2025
025ZYZ2025XTYY2025
025XTYY2025XZYXYYX2025

025XZYXYYX2025XYXYX
'''

maxs = float('-inf')

for i in range(len(s) - 2):
    if i != 0:
        k = '025' + '2025'.join(s[i : i + 2]) + '2025'
    else:
        k = '2025'.join(s[i : i + 2]) + '2025'
    if k.count('Y') >= 2:
        maxs = max(maxs, len(k))

print(maxs)

s = 'XX2025XZZX2025ZXYTXC2025ZYZ2025XTYY2025XZYXYYX2025XYXYX2025'
print(s, s.split('2025'))
#['XX', 'XZZX', 'ZXYTXC', 'ZYZ', 'XTYY', 'XZYXYYX', 'XYXYX', '']

with open('24_26549.txt') as f:
    s = f.readline().strip().split('2025')

maxs = float('-inf')

for i in range(len(s) - 50):
    if i != 0:
        k = '025' + '2025'.join(s[i : i + 50]) + '2025'
    else:
        k = '2025'.join(s[i : i + 50]) + '2025'
    if k.count('Y') >= 140:
        maxs = max(maxs, len(k))

print(maxs)

s ='2025'
print(s.split('2025'))
maxs = float('-inf')
for l in range(len(s)):
    if s[l] == 'G':
        r = l + 1
        count_odd = 0
        while r < len(s):
            if s[r].isdigit() and int(s[r]) % 2 != 0:
                count_odd += 1
            if count_odd == 46:
                break
            if s[r] == 'G':
                break
            r += 1
        if count_odd >= 45:
            maxs = max(maxs, r - l)
    else:
        l += 1

print(maxs)

with open('24_26077.txt') as f:
    s = f.readline().strip()

#s = 'G3126481276F3891274671280GG2716835GGG378216G78213' #3 нечет

'''
G31264812
G271683
G378216
G78213
'''

s = s.split('G')
print(s)

#['', '3126481276F3891274671280', '', '2716835', '', '', '378216', '78213']
maxs = float('-inf')

for i in s:
    count_odd = 0
    for j in range(len(i)):
        if i[j].isdigit() and int(i[j]) % 2 != 0:
            count_odd += 1
        if count_odd == 46:
            break
    if count_odd == 45:
        '''
        '3126481276F3891274671280' - 8 индекс
        '378216' - 5 индекс. G378216
        '''
        maxs = max(maxs, j + 2)
    if count_odd == 46:
        maxs = max(maxs, j + 1)

print(maxs)


with open('24.5_19717.txt') as f:
    s = f.readline().strip()

#s = 'MKDJJASMDASKLJDASMDASKOLJDMDSADMDADAMDSAM'
#print(s.split('M'))
maxs = float('-inf')
#['', 'KDJJAS', 'DASKLJDAS', 'DASKOLJD', 'DSAD', 'DADA', 'DSA', '']
s = s.split('M')
for i in range(len(s) - 278):
    #print(s[i : i + 3])
    maxs = max(maxs, len('M'.join(s[i : i + 279])))

print(maxs)

with open('24_16333.txt') as f:
    s = f.readline().strip()

table = str.maketrans('CDFGHE', 'BBBBBA')
s = s.translate(table)

#s = 'BBAABABABABBAABABABBABBABABBABABABABBBA'

'''
BBAABABABABBA
BBAABABABBA
BBABBA
BBABABBA
BBABABABABBBA
'''
s = s.split('BBA')
print(s)
#['', 'ABABABA', 'ABABA', '', 'BA', 'BABABAB', '']
print(len(max(s, key = len)) + 6)

with open('24_16333.txt') as f:
    s = f.readline().strip()

table = str.maketrans('RW24', 'QQ11')
s = s.translate(table)

#s = 'QQ1Q1Q1QQQ1Q111Q1Q1Q1QQ1QQ111QQ1Q1Q1Q1QQQ11Q1Q1Q'

'''
Q1Q1Q1Q
Q1Q1
1Q1Q1Q1
Q1Q
Q1
Q1Q1Q1Q1Q
Q1
1Q1Q1Q
'''
#['', '1Q1Q1', 'Q1Q111Q1Q1Q1', '1', '111', '1Q1Q1Q1', 'Q11Q1Q1Q']
#['Q', 'Q1Q1Q1Q', 'QQ1Q1', '11Q1Q1Q1Q', 'Q1Q', 'Q1', '11Q', 'Q1Q1Q1Q1Q', 'QQ1', '1Q1Q1Q']

while 'QQ' in s or '11' in s:
    s = s.replace('QQ', 'Q*Q').replace('11', '1*1')
s = s.split('*')
#['Q', 'Q1Q1Q1Q', 'Q', 'Q1Q1', '1', '1Q1Q1Q1Q', 'Q1Q', 'Q1', '1', '1Q', 'Q1Q1Q1Q1Q', 'Q', 'Q1', '1Q1Q1Q']
#print(s)

print(len(max(s, key = len)))
'''
QQQ -> Q*QQ
'''