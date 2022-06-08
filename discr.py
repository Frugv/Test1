from flask import Flask, render_template, request
from form import LoginForm
from conf import Config

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def form():
    form = LoginForm()
    return render_template('form.html', title='Ввод переменных', form=form)

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        a = int(request.form['A'])
        b = int(request.form['B'])
        c = int(request.form['C'])
        D = (b ** 2) - 4 * a * c
        if D < 0:
            message = "Дискриминант получился меньше 0, поэтому уравнение не имеет корней!"
            return render_template('result1.html', message=message)
        elif D == 0:
            x = -b/(2*a)
            return render_template('result2.html', x=x)
        else:
            x1 = (-b + (D ** (0.5))) / (2 * a)
            x2 = (-b - (D ** (0.5))) / (2 * a)
            return render_template('result3.html', x1=x1, x2=x2)

if __name__ == "__main__":
    app.run()