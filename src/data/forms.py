from flask_wtf import FlaskForm
import wtforms


class SingUpForm(FlaskForm):
    first_name = wtforms.StringField("Ім'я")
    last_name = wtforms.StringField("Прізвище")
    email = wtforms.EmailField("Електрона пошта", validators=[wtforms.validators.Email(), wtforms.validators.DataRequired])
    password = wtforms.PasswordField("Пароль", validators=[wtforms.validators.length(6)])
    submit = wtforms.SubmitField("Зареєструватись")


class LoginForm(FlaskForm):
    email = wtforms.EmailField("Елект", validators=[wtforms.validators.Email(), wtforms.validators.DataRequired()])
    password = wtforms.PasswordField("Пароль", validators=[wtforms.validators.length(6)])
    submit = wtforms.SubmitField("Увійти")