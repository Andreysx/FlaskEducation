from flask import Flask, render_template, request

app = Flask(__name__)


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



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
