# Задание №7
# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.

# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.

# Данные о новостях должны быть переданы в шаблон через
# контекст.


from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


@app.route("/")
def news_page():
    newses = [{'title': 'Emergency',
               'information': 'City in fire',
               'date': date(2007, 6, 14)},
              {'title': 'Elections',
               'information': 'presidential elections',
               'date': date(2024, 3, 12)},
              {'title': 'New-virus',
               'information': 'Covid-24131',
               'date': date(2020, 4, 12)},
              ]
    # context = {"news": _newses}
    # return render_template("index7HW.html", newses=newses)
    return render_template("index7HW2.html", newses=newses)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
