from flask import Flask, redirect, url_for
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
    <body>
        <header>
            НГТУ ФБ, Лабораторная работа 1
        </header>
        <p>Flask — фреймворк для создания веб-приложений на языке программирования Python, 
        использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к 
        категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, 
        сознательно предоставляющих лишь самые базовые возможности.</p>

        
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