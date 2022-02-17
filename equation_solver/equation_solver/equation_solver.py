def transformation(dictionary):
    for key in dictionary:
        if dictionary[key] >= 0:
            dictionary[key] = "+" + str(dictionary[key])
    equation = str(dictionary["x^2"]) + "*x^2" + str(dictionary["x"]) + "*x" + str(dictionary["x^0"]) + "=0"
    if equation[0] == "+":
        equation = equation[1:len(equation)]
    equation = equation.replace(" ", "")
    equation = equation.replace("+", " + ")
    equation = equation.replace("-", " - ")
    equation = equation.replace("=", " = ")
    print("Преобразованный вариант:", equation)

def coun(dictionary, buff, sign):
    import re 
    res = re.findall(r'x\^?\d?', buff) 
    if len(res) > 1:
        print("Уравнение не квадратное")
        return 0
    if len(res) == 1:
        if res[0] in dictionary:
            key = res[0]
            buff = buff.replace(res[0], "")
            if buff == '':
                buff = 1
            num = int(buff)
        else:
            print("Уравнение не квадратное")
            return 0
    else:
        if buff.isdigit():
            num = int(buff)
            key = "x^0"
    if sign == "False":
        num *= -1
    dictionary[key] += num
    return dictionary

def tyt(equation, dictionary, buff, sign):
    buff = equation[i:j]
    dictionary = coun(dictionary, buff, sign)
    if dictionary == 0:
        return 0

#def splitting(equation, dictionary):dgdhsdh

def select_dictionary(equation):
    print(equation)
    dictionary = {"x^2": 0,
                  "x": 0,
                  "x^0": 0}
    i = 0
    j = 0
    sign = "True"
    if equation[i] == "-":
        i += 1
        j += 1
        sign = "False"
    while equation[j] != "=":
        if equation[j] == "+":
            buff = equation[i:j]
            dictionary = coun(dictionary, buff, sign)
            if dictionary == 0:
                return 0
            sign = "True"
            i = j+1
        if equation[j] == "-":
            buff = equation[i:j]
            dictionary = coun(dictionary, buff, sign)
            if dictionary == 0:
                return 0
            sign = "False"
            i = j+1
        j += 1
    buff = equation[i:j]
    dictionary = coun(dictionary, buff, sign)
    if dictionary == 0:
                return 0
    i = j+1
    j += 1
    sign = "False"
    if equation[i] == "-":
        i += 1
        j += 1
        sign = "True"
    while j < len(equation):
        if equation[j] == "+":
            buff = equation[i:j]
            dictionary = coun(dictionary, buff, sign)
            if dictionary == 0:
                return 0
            sign = "False"
            i = j+1
        if equation[j] == "-":
            buff = equation[i:j]
            dictionary = coun(dictionary, buff, sign)
            if dictionary == 0:
                return 0
            sign = "True"
            i = j+1
        j += 1
    buff = equation[i:j]
    dictionary = coun(dictionary, buff, sign)
    if dictionary == 0:
                return 0
    transformation(dictionary)
    return dictionary
       
def counter(a, b, c):
    D = b**2 - 4*a*c
    if D >= 0:
        res = [int((-b + D**(1/2))/(2*a)), int((-b - D**(1/2))/(2*a))]
    #if D == 0:
       # res = int(-b/(2*a))
    if D < 0:
        D = D*(-1)
        buff = complex(int(-b/(2*a)), int(D**(1/2)/(2*a)))
        res = [buff, buff.conjugate()]
    return res

def reform(equation): #работает (за искл зелененького)  16.02.22
    import re
    equation = equation.replace(" ", "")
    #if re.findall(r'[!-@]', equation): -------любой символ из скобок. как?
        #print("Вы использовали запрёщённые символы. Простите (")
       # return 0
    counter = 0
    for i in range(0, len(equation)):
        if equation[i].isalpha() and equation[i] != 'x':
            print('МОя знать только буква x. Другие буква я не знать (Ж')
            return 0
        if equation[i] == '=':
            counter += 1
            if i == len(equation):
                print('После знака равенства не должно быть пусто(')
                return 0
            j = i
    if counter == 0:
        print('Что за уравнение без знака равенства? (:')
        return 0
    if counter > 1:
        print('Кажется, вы перебрали со знаками равенства (:')
        return 0
    return equation

def function():
    equation = input("Давайте уравнение: ")
    equation = reform(equation)
    if equation != 0:
        dictionary = select_dictionary(equation)
        if dictionary != 0:
            a = int(dictionary["x^2"])
            b = int(dictionary["x"])
            c = int(dictionary["x^0"])
            if a == 0:
                print('Кажется, уравнение не квадратное')
            else:
                res = counter(a, b, c)
                print('Ответ:', res, '\n(все значения округлены до целого, не пугайтесь)')

function()

