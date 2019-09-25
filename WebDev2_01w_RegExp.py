import re
# ---
# re.search(pattern, string)	      #Search in the string
b = '1 python 2 django 3 flask 4 python'
print(re.search('python', b))
print(re.search('python$', b).group())
# ---
# re.match(pattern, string)           #Search in the begin of the string
a = 'hello python hello django hello flask'
res = re.match('hello', a)
print(res)
print(res.group())
print(res.span())
print(re.match('django', a))         #Just in the begining of the string
# ---
# re.findall(pattern, string)       #Этот метод возвращает список всех найденных совпадений
a = '1 hello 2 python 3 hello 4 django'
res = re.findall(r'.',a)
res1 = re.findall(r'\w',a)
res2 = re.findall(r'\w+',a)
b = 'hello python hello django'
res3 = re.findall(r'^\w+',b)
res4 = re.findall(r'\w+$',b)
res5 = re.findall(r'\b\w',a)
res6 = re.findall(r'\w'*3,a)
print(res)
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print()
print(res6)
print()

# re.compile(pattern, repl, string) #Мы можем собрать регулярное выражение в отдельный объект,
                                    #который может быть использован для поиска
c = re.compile('hello')
print(c)
res = c.findall(a)
print(res)
# ---
# re.split(pattern, string, [maxsplit=0]) #Этот метод разделяет строку по заданному шаблону
res = re.split('hello', a, maxsplit=5)
print(res)
# re.sub(pattern, repl, string)     #Этот метод ищет шаблон в строке и заменяет его на указанную подстроку
a = 'hello python hello django hello flask'
p = re.compile(r'(exe|py|htm|html)')
print(p.sub('files', 'i can use exe', count=1))
print()
p1 = re.compile('[a-z]+')
m = p1.match(a)
print(m)
print(m.group())
print(m.span())
p2 = re.compile('[0-9]+')
print(p2.findall(b))
# ---
# Functions in regular expressions
def change(m):
    val = int(m.group())
    return hex(val)
p = re.compile('\d+')
print(p.sub(change, '1000 pages in 10 sites'))
print()
# Difference between + and *
# without and with ''

e = 'serezha@mail.ru anna@gmail.com vova@openedu.ru'
res = re.findall(r'@\w+',e)
res2 = re.findall(r'(@\w+[.]\w+)',e)
res3 = re.findall(r'@\w+[.]\w+',e)
res4 = re.findall(r'@\w+[.](\w+)',e)
print(res)
print(res2)
print(res3)
print(res4)
print()

# Diapozon
d='Anna 2223344 Serezha 3332244 Marina 4443322'
res = re.findall(r'(\d{3})(\d{2})(\d{2})',d)
res2 = re.findall(r'\b[AaSM]\w+', d)
res3 = re.findall(r'\b[^AaSM ]\w+', d)
print(res)
print(res2)
print(res3)
a = 'Papa u Vasi silen v matematike'
res = re.findall(r'[pPvV]\w+',a)
res2 = re.findall(r'^[pPvV]\w*',a)
res3 = re.findall(r'@\w+[.]\w+',a)
res4 = re.findall(r'[^pPvV]\w*',a)
res5 = re.findall(r'\b[^pPvV ]\w+',a)
print(res)
print(res2)
print(res3)
print(res4)
print(res5)
print()
# findinter()
a = 'hello python hello django hello flask'
print(a)
iter = re.finditer('hello', a)
print(iter)
for i in iter:
    print(i.span(), i.group()) # go through the cicle and remove from RAM
print()

import re
s = '<!DOCTYPE html><html><head><title></title></head><body><h1> ' \
    '<font color="#00FF00">OpenEdu </font></h1><font color="#FF0000">' \
    '<p> adress 1: Kronverkskiy 49</p><p> adress 2: Lomonosova 9</p><p> ' \
    'adress 3: Birxhevaya 14</p><p> adress 4: Grivzova 14 </p> </font></body> </html>'
res = re.findall(r'[KLBG]\w+ \d+', s)
print(res, type(res))
print('---')
print(', '.join(list(map(str, res))))
print('---')
subs = ' str. '
res2 = str(list(map(str, res)))
print(res2, type(res2))

resStr = ''
resStrSpr = ''
resStr2 = ''
for i in res:
    resStr += i + ', '
    resStrSpr += i + ','
print((resStr[0:-2]))
print(resStrSpr, type(resStrSpr))
subs = ' str.'
l = resStrSpr.split(' ')
print(l, type(l))
res = subs.join(l)
res1 = res.split(',')
res1 = res1[:-1]

for j in res1:
    resStr2 += j + ', '
print(resStr2[0:-2])

# res = subs.join(l)
# print(res)
