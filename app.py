from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
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
            НГТУ ФБ, Лабораторная 1
        </header>

        <main>
            
        </main>


        <footer>
            <hr>
            &copy;Ярославцев Богдан, ФБИ-24, 3 курс, 2024   
        </footer>
    </body>
</html>
"""