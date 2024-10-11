from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu",code=302)

@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ярославцев Богдан Всеволодович. Лабораторные работы</title>
    </head>
    <style>
    a {
        color: black;
        text-shadow: 1px 1px 0px white, -1px -1px 0px white, 1px -1px 0px white, -1px 1px 0px white;
        font-size: 23px;
        text-decoration: none;
    }
    body {
        background: #eb99fc5b;
    }
    </style>
    <body>
        <header>
            WEB-программирование, часть 2. Список лабораторных
        </header>
            
        <main>
            <h2 style="margin-left: 1.2%;margin-bottom: -7px;">Меню</h2>
            <div>
                <ol>
                    <li>
                        <a href="/lab1">Лабораторная работа 1</a>
                    </li>
                
                </ol>
            </div>
        </main>


        <footer>
            <hr>
            &copy;Ярославцев Богдан, ФБИ-24, 3 курс, 2024   
        </footer>
    </body>
</html>
"""
@app.route("/lab1")
def lab1():
    return """
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ярославцев Богдан Всеволодович. Лабораторная 1</title>
    </head>
    <style>
    a {
        color: black;
        text-shadow: 1px 1px 0px white, -1px -1px 0px white, 1px -1px 0px white, -1px 1px 0px white;
        font-size: 23px;
        text-decoration: none;
    }
    body {
        background: #eb99fc5b;
    }
    </style>
    <body>
        <header>
            НГТУ ФБ, Лабораторная работа 1
        </header>
        <p>Flask — фреймворк для создания веб-приложений на языке программирования Python, 
        использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к 
        категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, 
        сознательно предоставляющих лишь самые базовые возможности.</p>

        <a href="/menu">Menu</a>
        
        <h2>Реализованные роуты</h2>
        <div>
            <ol>
                <li>
                    <a href="lab1/oak">Дуб</a>
                </li>
                <li>
                    <a href="lab1/student">Студент</a>
                </li>
                <li>
                    <a href="lab1/python">Python</a>
                </li>
                <li>
                    <a href="lab1/japan">Япония</a>
                </li>
            
            </ol>
        </div>

        <footer>
            <hr>
            &copy;Ярославцев Богдан, ФБИ-24, 3 курс, 2024   
        </footer>
    </body>
</html>
"""
@app.route('/lab1/oak')
def oak():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img style="border-radius: 10px;" src="''' + url_for('static',filename='oak2.jfif') + '''">
    </body>
</html>  
'''
@app.route('/lab1/student')
def student():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='logo.css') + '''">
    </head>
    <body>
        <h1>Ярославцев Богдан Всеволодович</h1>
        <img style="border-radius: 10px;" src="''' + url_for('static',filename='logo.jpeg') + '''">
    </body>
</html>
'''
@app.route('/lab1/python')
def python():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='python.css') + '''">
    </head>
    <body>
        <h1>Python: Простой и мощный язык программирования</h1>
    
        <p >Python — это высокоуровневый язык программирования, созданный Гвидо ван Россумом в 1991 году. Он известен своей простотой и читаемостью кода, что делает его идеальным 
        выбором как для начинающих, так и для опытных разработчиков.</p>

        <p>Python — это универсальный язык, который может использоваться для решения широкого спектра задач. Он подходит для веб-разработки, научных вычислений, анализа данных, 
        машинного обучения и автоматизации задач.</p>

        <p>Одной из сильных сторон Python является его активное и дружелюбное сообщество. Разработчики со всего мира делятся своими знаниями, создают библиотеки и инструменты, а 
        также помогают друг другу в решении проблем.</p>
        <img style="border-radius: 10px;" src="''' + url_for('static',filename='fon.jpg') + '''">
    </body>
</html>
'''

@app.route('/lab1/japan')
def japan():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='japan.css') + '''">
    </head>
    <body>
        <h1>Фудзияма: Священная гора Японии</h1>
    
        <p>Фудзияма — самая известная гора Японии, симметричная и почти идеально конусообразная, высотой 3776 метров. Она является символом страны и неотъемлемой частью японской культуры.</p>

        <p>В японской мифологии Фудзияма ассоциируется с божеством огня Сусаноо. Традиционно считается, что гора является домом для богов, и многие японцы посещают ее, чтобы поклониться и получить
        благословение.</p>

        <p>Фудзияма окружена живописными пейзажами, включая леса, горные озера и водопады. Национальный парк Фудзияма-Хаконе-Идзу — популярное место для пеших прогулок и альпинизма.</p>
        <img style="border-radius: 10px;" src="''' + url_for('static',filename='fud.jpg') + '''">
    </body>
</html>
'''
@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id>= len(flower_list):
        return "Такого цветка нет", 404
    else:
        return "Цветок: " + flower_list[flower_id]

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    if not name:
        return "Вы не задали имя цветка", 400
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name}</p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''
@app.route('/lab2/flowers/')
def show_all_flowers():
    return f'''
<!doctype html>
<html>
    <body>
    <h1> Все цветы </h1>
    <p> Всего цветов: {len(flower_list)} </p>
    <ul>
        {"".join(f"<li>{flower}</li>" for flower in flower_list)}
    </ul>
    </body>
</html>
'''


@app.route('/lab2/example')
def example():
    name = 'Ярославцев Богдан'
    numlab = '2'
    group = 'ФБИ-24'
    numbCourse = '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('example.html', name=name, numlab=numlab, group=group, numbCourse=numbCourse, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = 'О <b>сколько</b> <u>нам</u> <i>открытий чудных...'
    return render_template('filter.html', phrase=phrase)

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    sum = a + b
    minus = a - b
    mul = a * b
    if b == 0:
        delenie = "Делить на ноль нельзя"
    else:
        delenie = a / b
    #div_result = "Деление на ноль невозможно" if b == 0 else num1 / num2
    stepen = a ** b
    return f'''
<!doctype html>
<html>
    <body style="background: #eb99fc5b;">
    <h1> Расчет с параметрами </h1>
    <p style="color: black;text-shadow: 1px 1px 0px white, -1px -1px 0px white, 1px -1px 0px white, -1px 1px 0px white;font-size: 23px;text-decoration: none;margin: 10px">{a} + {b} = {sum}</p>
    <p style="color: black;text-shadow: 1px 1px 0px white, -1px -1px 0px white, 1px -1px 0px white, -1px 1px 0px white;font-size: 23px;text-decoration: none;margin: 10px">{a} - {b} = {minus}</p>
    <p style="color: black;text-shadow: 1px 1px 0px white, -1px -1px 0px white, 1px -1px 0px white, -1px 1px 0px white;font-size: 23px;text-decoration: none;margin: 10px">{a} * {b} = {mul}</p>
    <p style="color: black;text-shadow: 1px 1px 0px white, -1px -1px 0px white, 1px -1px 0px white, -1px 1px 0px white;font-size: 23px;text-decoration: none;margin: 10px">{a} / {b} = {delenie}</p>
    <p style="color: black;text-shadow: 1px 1px 0px white, -1px -1px 0px white, 1px -1px 0px white, -1px 1px 0px white;font-size: 23px;text-decoration: none;margin: 10px">{a} <sup> {b} </sup>= {stepen}</p>
    </body>
</html>
'''
@app.route('/lab2/calc/')
def redirect_to_default():
    return redirect('/lab2/calc/1/1')
@app.route('/lab2/calc/<int:a>')
def redirect_with_default_b(a):
    return redirect(f'/lab2/calc/{a}/1')