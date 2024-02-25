from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)

app.secret_key = '4622baf278446899a4fe4e223fdcfc1c5771d4e9ea1ec20904336e9dcff79878'
# сгенерировано с помощью secrets.token_hex() в строке интерпретаора Python


# Задание №5
# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

@app.route('/calculator/', methods=['GET', 'POST'])
def calculating():
    if request.method == 'POST':
        num_1 = float(request.form['num_1'])
        num_2 = float(request.form.get('num_2'))
        operation = request.form.get('operation')
        result = 0
        if operation == '+':
            result = num_1 + num_2
        elif operation == '-':
            result = num_1 - num_2
        elif operation == '/':
            result = num_1 / num_2
        else:
            result = num_1 * num_2
        return f'Результат вашей операции:  {num_1} {operation} {num_2} = {result} '
    return render_template('calculator.html')


#
# Задание №6
# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


@app.route('/age/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age > 0 and age < 100:

           return render_template('age_result.html', age=age, name=name.capitalize())
        else:
            return render_template('age_error.html', age=age)
    return render_template('age.html')


@app.route('/name/')
def name_page():
    name_ = 'Ivan'
    return render_template('greetings.html', name=name_)


# Задание №7
# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат


@app.route('/task7/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        number = float(request.form.get('number'))
        data = {"number": number, "square": number ** 2}
        return render_template('square.html', data=data)
    return render_template('task7.html')

# Задание №8
# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".


@app.route('/flashh/', methods=['GET', 'POST'])
def flashh():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('flashh'))
    return render_template('flashh.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
