from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateTimeLocalField
from wtforms.validators import DataRequired, Email, EqualTo, length

#
# Задание 4
# Создать форму регистрации для пользователя.
# Форма должна содержать поля: имя, электронная почта,
# пароль (с подтверждением), дата рождения, согласие на
# обработку персональных данных.
# Валидация должна проверять, что все поля заполнены
# корректно (например, дата рождения должна быть в
# формате дд.мм.гггг).
# При успешной регистрации пользователь должен быть
# перенаправлен на страницу подтверждения регистрации.

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    birth_date = DateTimeLocalField('Date of birth', validators=[DataRequired()])
    permission = BooleanField('Consent to processing of personal data', validators=[DataRequired()])

