from flask import Blueprint, render_template, request, abort

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/lab7.html')

films = [
    {
        'title': 'The Dark Knight',
        'title_ru': 'Темный рыцарь',
        'year': 2008,
        'description': 'Кристофер Нолан представил один из самых культовых фильмов о Бэтмене. \
            Фильм рассказывает о противостоянии Бэтмена (Кристиан Бейл) и Джокера (Хит Леджер), \
            который стал одной из самых ярких ролей в истории кино. Сюжет поражает своими нюансами \
            и философскими размышлениями о добре и зле.'
    },
    {
        'title': 'Pulp Fiction',
        'title_ru': 'Криминальное чтиво',
        'year': 1994,
        'description': 'Квентин Тарантино создал культовый фильм, который стал классикой жанра. \
            Сюжет состоит из нескольких переплетающихся историй о преступниках, гангстерах и \
            обычных людях. Фильм знаменит своим нелинейным повествованием, яркими персонажами \
            и остроумными диалогами.'
    },
    {
        'title': 'The Shawshank Redemption',
        'title_ru': 'Побег из Шоушенка',
        'year': 1994,
        'description': 'Фильм Фрэнка Дарабонта по рассказу Стивена Кинга рассказывает историю \
            двух заключенных, которые находят надежду и дружбу в тюрьме Шоушенк. Главные роли \
            исполнили Тим Роббинс и Морган Фриман. Фильм поражает своей глубиной, эмоциональной \
            силой и философией о свободе.'
    },
    {
        'title': 'Inglourious Basterds',
        'title_ru': 'Бесславные ублюдки',
        'year': 2009,
        'description': 'Квентин Тарантино снял эпическую историю о группе еврейских солдат, \
            которые пытаются уничтожить нацистских лидеров во время Второй мировой войны. \
            Фильм знаменит своими динамичными сценами, яркими персонажами и неожиданными поворотами.'
    },
    {
        'title': 'The Lord of the Rings: The Fellowship of the Ring',
        'title_ru': 'Властелин колец: Братство кольца',
        'year': 2001,
        'description': 'Первая часть эпической трилогии Питера Джексона по роману Дж.Р.Р. Толкина. \
            Фильм рассказывает о путешествии хоббита Фродо, который должен уничтожить Кольцо Всевластья. \
            Фильм поражает своими визуальными эффектами, эмоциональной глубиной и масштабными сценами.'
    }
]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if 0 <= id < len(films):
        return films[id]
    else:
        abort(404)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if 0 <= id < len(films):
        del films[id]
        return '', 204
    else:
        abort(404)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if 0 <= id < len(films):
        film = request.get_json()
        films[id] = film
        return films[id]
    else:
        abort(404)
        
@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    if not film:
        abort(404)
    films.append(film)
    return {'id': len(films) - 1}, 201