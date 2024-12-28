from flask import Blueprint, render_template, redirect, request, session, url_for
from db import db
from db.models import users, articles
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import or_

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def lab():
    return render_template('lab9/index.html')

@lab9.route('/lab9/name', methods=['GET', 'POST'])
def lab9_name():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        return redirect(url_for('lab9.lab9_age'))
    return render_template('lab9/name.html')

@lab9.route('/lab9/age', methods=['GET', 'POST'])
def lab9_age():
    if request.method == 'POST':
        session['age'] = request.form.get('age')
        return redirect(url_for('lab9.lab9_gender'))
    return render_template('lab9/age.html')

@lab9.route('/lab9/gender', methods=['GET', 'POST'])
def lab9_gender():
    if request.method == 'POST':
        session['gender'] = request.form.get('gender')
        return redirect(url_for('lab9.lab9_preference1'))
    return render_template('lab9/gender.html')

@lab9.route('/lab9/preference1', methods=['GET', 'POST'])
def lab9_preference1():
    if request.method == 'POST':
        session['preference1'] = request.form.get('preference1')
        return redirect(url_for('lab9.lab9_preference2'))
    return render_template('lab9/preference1.html')

@lab9.route('/lab9/preference2', methods=['GET', 'POST'])
def lab9_preference2():
    if request.method == 'POST':
        session['preference2'] = request.form.get('preference2')
        return redirect(url_for('lab9.lab9_result'))
    return render_template('lab9/preference2.html')

@lab9.route('/lab9/result')
def lab9_result():
    name = session.get('name', 'Друг')
    age = int(session.get('age', 18))
    gender = session.get('gender', 'мужчина')
    preference1 = session.get('preference1', 'вкусное')
    preference2 = session.get('preference2', 'сладкое')

    # Определяем возрастную группу
    if age < 18:
        age_group = 'ребёнок'
    else:
        age_group = 'взрослый'

    # Формируем подарок и картинку
    if preference1 == 'вкусное':
        if preference2 == 'сладкое':
            gift = 'мешочек конфет'
            image = 'lab9/candy.avif'
        elif preference2 == 'сытное':
            gift = 'пицца'
            image = 'lab9/pizza.jpg'
    elif preference1 == 'красивое':
        if preference2 == 'яркое':
            gift = 'букет цветов'
            image = 'lab9/flowers.jpg'
        elif preference2 == 'стильное':
            gift = 'дизайнерская вещь'
            image = 'lab9/design.jpg'
    else:
        gift = 'подарок'
        image = 'lab9/gift.jpg'

    # Формируем поздравление
    if age_group == 'ребёнок':
        if gender == 'мужчина':
            greeting = f"Поздравляю тебя, {name}, желаю, чтобы ты быстро вырос, был умным и счастливым. Вот тебе подарок — {gift}."
        else:
            greeting = f"Поздравляю тебя, {name}, желаю, чтобы ты быстро выросла, была умной и счастливой. Вот тебе подарок — {gift}."
    else:
        if gender == 'мужчина':
            greeting = f"Поздравляю тебя, {name}, желаю крепкого здоровья, мудрости и успехов во всех начинаниях. Вот тебе подарок — {gift}."
        else:
            greeting = f"Поздравляю тебя, {name}, желаю крепкого здоровья, мудрости и успехов во всех начинаниях. Вот тебе подарок — {gift}."

    return render_template('lab9/result.html', greeting=greeting, image=image)