from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
from lab2 import lab2
app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)

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
                    <li>
                        <a href="/lab2">Лабораторная работа 2</a>
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

@app.errorhandler(404)
def not_found(err):
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
         <h2>Ошибка 404 - такой страницы не существует</h2>
        <footer>
            &copy; Ярославцев Богдан, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''
@app.errorhandler(500)
def not_found(err):
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <h2>Ошибка 500 - сервер не смог обработать запрос</h2>
         <footer>
            &copy; Ярославцев Богдан, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''