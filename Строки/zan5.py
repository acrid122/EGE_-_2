v = 'Hello, World'
table = str.maketrans('led', '123') #такой способ работает так: l -> 1, e -> 2, d -> 3
print(v.translate(table))

table1 = str.maketrans({
    'l' : '1',
    'e' : '2',
    'd' : '3'
})

print(v.translate(table1))

table2 = str.maketrans('led', '123', 'ow')
print(v.translate(table2))

print(v.replace('l', '')) #замена на пустую строку равносильна удалению
table3 = str.maketrans('od', '89', 'l')
print(v.translate(table3))
table4 = str.maketrans('l', '7', 'o')
print(v.translate(table4))

'''
Создайте строку "a b c d". Используйте split() (по пробелам), затем translate(str.maketrans("abcd", "ABCD")) на списке (map), join(" "), и ljust(10, '-'), выведите.
Здравствуйте, эту не смог сделать
'''

sp = ['123', '123', '43', '56']
#map - встроенная ф-ия, которая позволяет применить какую-то функцию ко всем элементам итерируемого объекта
print(list(map(int, sp)))

def p(x):
    return x + 2

#лямбда-ф-ии - анонимные ф-ии в одну строку, с короткой реализаций

d = lambda x: x + 2
print(d(2))

sp1 = [123, 46]
print(list(map(p, sp1)))

s = 'a b c d'
sp = s.split()
print(sp)


print(list(map(lambda x: x.translate(str.maketrans("abcd", "ABCD")), sp)))

'''
Парсер системного лога
Дан лог сервера: "2023-10-15 14:23:45 [ERROR] User 'admin' failed login from IP 192.168.1.100".
Извлеките IP-адрес (последнее слово), замените точки на дефисы, проверьте startswith("192"), примените upper() и 
выведите в f-строке f"🚨 Подозрительный IP: {ip:>15} 🚨". Обработайте случай, если IP нет (try-except).
'''

s = "2023-10-15 14:23:45 [ERROR] User 'admin' failed login from IP 192.168.1.100"
try:
    ind = s.find("IP") + 3
    print(s[ind])
    sip = s[ind:]
    sip = sip.replace(".", "-")
    print(sip)
    print(sip.startswith("192"))
    print(s.upper())
    print(f"🚨 Подозрительный IP: {sip:>15} 🚨")
    
except IndexError:
    print("Айпишника нет")

'''
Анализ чата Discord
Сообщение: "@Alice Hello! Today is a great day! 🎉 #python".
Найдите index первого "@", извлеките имя пользователя (до пробела), замените "Alice" на "Developer", 
примените title(), затем rfind("!") и ljust(25, '*'), выведите в f-строке f"💬 {username}: {message}".
'''

s = "@Alice Hello! Today is a great day! 🎉 #python"
ind = s.index("@")
ind2 = s.index(" ")
username = s[ind + 1 : ind2]
username = username.replace(username, 'Developer')
s = s.title().ljust(25, '*')
print(s)
message = s[ind2 + 1:]
print(s.rfind("!"))
print(f"💬 {username}: {message}")

s1 = "@Alice Hello! Today is a great day! 🎉 #python"
ind = s.index("@")
ind2 = s.index(" ")
s2 = s[ind + 1 : ind2]
s2 = s2.replace(s2, 'Developer')
print(f"💬 {s2.title().ljust(25, '*')}, {s1[ind2 + 1 :]}")

'''
3. Обработка ошибок API
Ответ API: '{"status": "error", "code": 404, "message": "User not found"}'.
Используйте find('"message":'), rsplit('"', 2) srror}".
'''
s = '{"status": "error", "code": 404, "message": "User not found"}'
ind = s.find('"message":')
sp = s.rsplit('"', 2)
error = sp[1]
error = error.capitalize().center(40, '=')
print(error.istitle())
print(f"❌ API Error: {error}")


'''
Лог: "[SECURITY] 2023-10-15T10:30:00Z | Failed brute force | IP: 203.0.113.42 | Attempts: 127".
Используйте rfind("IP:"), split("|") для части с IP, strip("IP: "), translate(str.maketrans(".", "-")), zfill(15) и rjust(20, ' '). 
Обработайте если IP нет. Выведите f"🔒 Блокировка: {ip}".
'''
s = "[SECURITY] 2023-10-15T10:30:00Z | Failed brute force | IP: 203.0.113.42 | Attempts: 127"
try:
    print(s.rfind("IP:"))
    lst = s.split("|")
    print(lst[2][5])
    ip = lst[2].strip("IP: ").translate(str.maketrans(".", "-")).zfill(15).rjust(20, ' ')
    print(f"🔒 Блокировка: {ip}")
   

except IndexError:
    print("Ошибка!")

'''
5. Анализ GitHub issues
Заголовок: "Fix #42: Memory leak in Python 3.11 parser".
Проверьте startswith("Fix"), используйте split("#") для номера issue (ошибки), zfill(3) на номере, replace("Fix", "🔧 RESOLVED"), 
title() и center(50, '-'). Выведите в f-строке.
'''


s = "Fix #42: Memory leak in Python 3.11 parser"
print(s.startswith("Fix"))
sp = s.split("#")
ind = sp[1].index(':')
number = sp[1][:ind].zfill(3)
print(f"{sp[0].replace("Fix", "🔧 RESOLVED").title().center(50, '-')} {number}")