from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)

@lab1.route("/index")
def start():
    return redirect("/menu",code=302)

@lab1.route("/menu")
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
                    <li>
                        <a href="/lab2">Лабораторная работа 2</a>
                    </li>
                    <li>
                        <a href="/lab3">Лабораторная работа 3</a>
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


@lab1.route("/lab1")
def lab():
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


@lab1.route('/lab1/oak')
def oak():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img style="border-radius: 10px;" src="''' + url_for('static',filename='lab1/oak2.jfif') + '''">
    </body>
</html>  
'''


@lab1.route('/lab1/student')
def student():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/logo.css') + '''">
    </head>
    <body>
        <h1>Ярославцев Богдан Всеволодович</h1>
        <img style="border-radius: 10px;" src="''' + url_for('static',filename='lab1/logo.jpeg') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/python')
def python():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/python.css') + '''">
    </head>
    <body>
        <h1>Python: Простой и мощный язык программирования</h1>
    
        <p >Python — это высокоуровневый язык программирования, созданный Гвидо ван Россумом в 1991 году. Он известен своей простотой и читаемостью кода, что делает его идеальным 
        выбором как для начинающих, так и для опытных разработчиков.</p>
        <p>Python — это универсальный язык, который может использоваться для решения широкого спектра задач. Он подходит для веб-разработки, научных вычислений, анализа данных, 
        машинного обучения и автоматизации задач.</p>
        <p>Одной из сильных сторон Python является его активное и дружелюбное сообщество. Разработчики со всего мира делятся своими знаниями, создают библиотеки и инструменты, а 
        также помогают друг другу в решении проблем.</p>
        <img style="border-radius: 10px;" src="''' + url_for('static',filename='lab1/fon.jpg') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/japan')
def japan():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/japan.css') + '''">
    </head>
    <body>
        <h1>Фудзияма: Священная гора Японии</h1>
    
        <p>Фудзияма — самая известная гора Японии, симметричная и почти идеально конусообразная, высотой 3776 метров. Она является символом страны и неотъемлемой частью японской культуры.</p>
        <p>В японской мифологии Фудзияма ассоциируется с божеством огня Сусаноо. Традиционно считается, что гора является домом для богов, и многие японцы посещают ее, чтобы поклониться и получить
        благословение.</p>
        <p>Фудзияма окружена живописными пейзажами, включая леса, горные озера и водопады. Национальный парк Фудзияма-Хаконе-Идзу — популярное место для пеших прогулок и альпинизма.</p>
        <img style="border-radius: 10px;" src="''' + url_for('static',filename='lab1/fud.jpg') + '''">
    </body>
</html>
'''