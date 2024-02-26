from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from Lesson_3.Semminar_3.form_1 import RegistrationForm

app2 = Flask(__name__)
app2.config['SECRET_KEY'] = '34d6e6651cb8716eaf6afcfdef78bb5a289c162daf3acd5cc304d0968028cd7f'
csrf = CSRFProtect(app2)

# Задание 5
# Создать форму регистрации для пользователя.
# Форма должна содержать поля: имя, электронная почта,
# пароль (с подтверждением), дата рождения, согласие на
# обработку персональных данных.
# Валидация должна проверять, что все поля заполнены
# корректно (например, дата рождения должна быть в
# формате дд.мм.гггг).
# При успешной регистрации пользователь должен быть
# перенаправлен на страницу подтверждения регистрации.

@app2.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        return render_template('succespage.html')
    return render_template('test.html', form=form)

