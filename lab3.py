from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', "Аноним")
    age = request.cookies.get('age', "Неизвестный")
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)

@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'red')
    return resp
@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/lab3/form1')
def form1():
    errors={}
    user = request.args.get('user')
    if user == '':
        errors['user']= 'Заполните поле!'
    
    age = request.args.get('age') 
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')
@lab3.route('/lab3/pay')
def pay():
        price=0
        drink = request.args.get('drink')
        #Пусть кофе стоит 120 рублей, черный чай - 80 рублей, зеленый - 70 рублей.
        if drink == 'coffee':
             price= 120
        elif drink == 'black-tea':
             price = 80
        else:
             price=70
        #Добавка молодка удорожает напиток на 30 рублей, а сахар - на 10.
        if request.args.get('milk') == 'on':
             price += 30
        if request.args.get('sugar') == 'on':
             price += 10
        return render_template('lab3/pay.html', price=price)
@lab3.route('/lab3/success')
def success():
    price = request.args.get('price')
    return render_template('lab3/success.html', price=price)

@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    back_color = request.args.get('back_color')
    font_size = request.args.get('font_size')
    varstyle= request.args.get('varstyle')
    if color or back_color or font_size:
        resp = make_response (redirect ('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if back_color:
            resp.set_cookie('back_color', back_color)
        if font_size:
           resp.set_cookie('font_size', font_size) 
        if varstyle:
            resp.set_cookie('varstyle', varstyle) 
        return resp
    color = request.cookies.get ( 'color')
    back_color = request.cookies.get('back_color')
    font_size = request.cookies.get('font_size', '16')
    varstyle = request.cookies.get('varstyle')
    resp = make_response(render_template ('lab3/settings.html', color=color, back_color=back_color, 
                                             font_size=font_size, varstyle=varstyle))
    return resp

@lab3.route('/lab3/ticket')
def ticket():
    pas_name = request.args.get('pas_name')
    polka_type = request.args.get('polka_type')
    with_bedding = request.args.get('with_bedding')
    with_luggage = request.args.get('with_luggage')
    age = request.args.get('age')
    point = request.args.get('point')
    destination_point = request.args.get('destination_point')
    travel_date = request.args.get('travel_date')
    medstrax = request.args.get('medstrax')
    if pas_name and polka_type and age and point and destination_point and travel_date:
        age = int(age)
        
        ticket_price = 1000 if age >= 18 else 700  
        if polka_type in ['lower', 'lower_side']:
            ticket_price += 100
        if with_bedding == 'on':
            ticket_price += 75
        if with_luggage == 'on':
            ticket_price += 250
        if medstrax == 'on':
            ticket_price += 150
        ticket_type = "Детский билет" if age < 18 else "Взрослый билет"
        return render_template('lab3/check.html', 
                               pas_name=pas_name, 
                               ticket_type=ticket_type,
                               ticket_price=ticket_price,
                               point=point,
                               destination_point=destination_point,
                               travel_date=travel_date)
    return render_template('lab3/ticket.html')

@lab3.route('/lab3/clear_cookies')
def clear_cookies():
    resp = make_response(redirect('/lab3/settings'))
    
    
    resp.delete_cookie('color')
    resp.delete_cookie('back_color')
    resp.delete_cookie('font_size')
    resp.delete_cookie('varstyle')
    
    return resp

car = [
    {'name': 'Toyota Camry', 'price': 2500000, 'brand': 'Toyota', 'color': 'Белый'},
    {'name': 'BMW X5', 'price': 6500000, 'brand': 'BMW', 'color': 'Чёрный'},
    {'name': 'Mercedes-Benz C-Class', 'price': 5500000, 'brand': 'Mercedes-Benz', 'color': 'Серебристый'},
    {'name': 'Audi A4', 'price': 4000000, 'brand': 'Audi', 'color': 'Синий'},
    {'name': 'Ford Focus', 'price': 1500000, 'brand': 'Ford', 'color': 'Красный'},
    {'name': 'Hyundai Solaris', 'price': 1200000, 'brand': 'Hyundai', 'color': 'Серый'},
    {'name': 'Volkswagen Tiguan', 'price': 3200000, 'brand': 'Volkswagen', 'color': 'Зелёный'},
    {'name': 'Lexus RX', 'price': 7000000, 'brand': 'Lexus', 'color': 'Чёрный'},
    {'name': 'Nissan Qashqai', 'price': 2300000, 'brand': 'Nissan', 'color': 'Белый'},
    {'name': 'Kia Sportage', 'price': 2400000, 'brand': 'Kia', 'color': 'Синий'},
    {'name': 'Mazda CX-5', 'price': 2800000, 'brand': 'Mazda', 'color': 'Красный'},
    {'name': 'Chevrolet Tahoe', 'price': 5500000, 'brand': 'Chevrolet', 'color': 'Чёрный'},
    {'name': 'Subaru Forester', 'price': 2600000, 'brand': 'Subaru', 'color': 'Серый'},
    {'name': 'Volvo XC60', 'price': 4800000, 'brand': 'Volvo', 'color': 'Белый'},
    {'name': 'Renault Duster', 'price': 1400000, 'brand': 'Renault', 'color': 'Зелёный'},
    {'name': 'Peugeot 3008', 'price': 3000000, 'brand': 'Peugeot', 'color': 'Серебристый'},
    {'name': 'Mitsubishi Outlander', 'price': 2700000, 'brand': 'Mitsubishi', 'color': 'Чёрный'},
    {'name': 'Skoda Octavia', 'price': 1800000, 'brand': 'Skoda', 'color': 'Синий'},
    {'name': 'Jeep Grand Cherokee', 'price': 6000000, 'brand': 'Jeep', 'color': 'Белый'},
    {'name': 'Cadillac Escalade', 'price': 8500000, 'brand': 'Cadillac', 'color': 'Чёрный'}
]
@lab3.route('/lab3/search')
def search():
    return render_template('lab3/search.html')
@lab3.route('/lab3/res')
def res():
    min_price = request.args.get('min_price', type=int)
    max_price = request.args.get('max_price', type=int)
    filtered_phones = [phone for phone in car if min_price <= phone["price"] <= max_price]
    return render_template('lab3/result.html', phones=filtered_phones)