print("Добро пожаловать в игру")
a = input("Для того,чтобы начать игру нажмите букву Д на клавиатуре")
if a == "Д":
    print("Тогда начнем")
else:
    print("Досвидания")
print("Мы рассмотрим Конъюнкцию,Дизъюнкцию и Импликацию. Вам нужно ввести первую букву операции на клавиатуре,чтобы узнать про нее и попробовать решить задачу.")
c = input("Если готовы,то введите Д. для того,чтобы перейти к задачам введите любой другой символ")
while c == "Д":
    b = input()
    if b == "К":
        print("Конъюнкция(∧) - это логическое умножение и как в математике оно выполняется первым. Например: А = 1, В = 0 А∧В = 0 и А = 1, В = 1 А∧В = 1 ")
    elif b == "Д":
        print("Дизъюнкция(∨) - это логическое сложение. Например: А = 1, В = 0 А∨В = 1 и А = 0, В = 0 А∨В = 0")
    elif b == "И":
        print("Импликация(→) - это логическое следование, выполняется последним. Из 2-х 0 следует 1, из 2-х 1 следует 0, из 1 следует 0 и из 0 следует 1")
    else:
        break
print("Теперь задачи на прройденную тему")
print("Посторойте таблицу истиности для этого выражения: (x ⋁ y)∧z → y; и напишите в ответе сколько 0 в ней  будет")
proverka = input("Если готовы дать ответ,то введите Д, а затем ответ")
while proverka == "Д":
    otvet = input("Ответ:")
    if otvet == "1":
        print("Вы молодцы")
        break
    else:
        print("Подумайте еще раз")
