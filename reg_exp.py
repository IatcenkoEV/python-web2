import re
# re.search(pattern, string)	      #Найти в строке string первую строчку, подходящую под шаблон pattern
# re.match(pattern, string)         #Этот метод ищет по заданному шаблону в начале строки
# re.findall(pattern, string)       #Этот метод возвращает список всех найденных совпадений
# re.compile(pattern, repl, string) #Мы можем собрать регулярное выражение в отдельный объект, 
                                    #который может быть использован для поиска
# re.split(pattern, string, [maxsplit=0]) #Этот метод разделяет строку по заданному шаблону
# re.sub(pattern, repl, string)     #Этот метод ищет шаблон в строке и заменяет его на указанную подстроку
p = re.compile(r'(exe|py|htm|html)')
p.sub('files','i can use exe')
print(p.sub)
