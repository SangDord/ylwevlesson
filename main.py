from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training_prof(prof):
    return render_template('training_prof.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    prof_list = ['инженер-исследователь',
                 'пилот',
                 'строитель',
                 'экзобиолог',
                 'врач',
                 'инженер по терраформарованию',
                 'климатолог',
                 'специалист по радиационной защите',
                 'астрогеолог',
                 'инженер жизнеобеспечения',
                 'метеоролог',
                 'оператор марсохода',
                 'киберинженер',
                 'штурман',
                 'пилот дронов']
    return render_template('list_prof.html', list=list, prof_list=prof_list)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    params = {}
    params['title'] = 'Анкета'
    params['surname'] = input('Введите фамилию| ')
    params['name'] = input('Введите имя| ')
    params['education'] = input('Какое у вас образование?| ')
    params['profession'] = input('Какая у вас профессия?| ')
    params['sex'] = input('Ваш пол?| ')
    params['motivation'] = input('Ваша мотивация?| ')
    params['ready'] = input('Готовы ли вы остаться на Марсе?| (y/n) ').lower() == 'y'
    for k, v in params.items():
        if not v and k != 'ready':
            params[k] = 'None'
    return render_template('auto_answer.html', **params)


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')