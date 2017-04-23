from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/calcularComision', methods = ['POST'])
def comision():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        ventas = float(request.form['ventas'])

        if (ventas < 25000):
            comision = 0.03 * ventas
        elif (ventas >= 25000 and ventas < 50000):
            comision  = ventas * 0.05
        elif (ventas >= 50000 and ventas < 75000):
            comision = ventas * 0.07
        elif (ventas >= 75000 and ventas < 100000):
            comision = ventas * 0.1
        elif (ventas >= 100000):
            comision = ventas * 0.15

        reporte = "%s, %s, %4.2f, %4.2f" %(nombre, apellido, ventas, comision)
        report = open("csv.csv", "a+")
        report.write(reporte + "\n")
        report.close()
    return render_template('calculadora.html', nom=nombre, ape=apellido , comi=comision)




if __name__ == "__main__":
    app.run()
