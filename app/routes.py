from app import app
from app.forms import Calculo
from flask import render_template

@app.route('/', methods=['GET', 'POST'])
def login():
    form = Calculo()
    if form.validate_on_submit():
        hon = form.valor.data
        iva_valor=0.16
        riva = 0.106666
        risr = 0.10
        sub = hon + (hon * iva_valor)
        sub1 = "%.2f" % sub
        neto = sub - (hon * riva) - (hon * risr)
        neto1 = "%.2f" % neto
        valores = {
            'hon':hon,
            'iva_valor':iva_valor,
            'riva':riva,
            'risr':risr,
            'sub':sub,
            'sub1':sub1,
            'neto':neto,
            'neto1':neto1
        }
        return render_template('login.html', title='Resultado',valores=valores)
    return render_template('index.html', title='Calculadora', form=form)