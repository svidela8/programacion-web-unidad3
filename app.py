from enum import nonmember

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():

    promedio = None
    estado = ""
    if request.method == 'POST':

        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"
                
    return render_template('ejercicio1.html',
                           promedio = promedio,
                           estado = estado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():

    nombre_mayor = ""
    cantidad = 0

    if request.method == 'POST':

        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        largo1 = len(nombre1)
        largo2 = len(nombre2)
        largo3 = len(nombre3)

        if largo1 >= largo2 and largo1 >= largo3:
            nombre_mayor = nombre1
            cantidad = largo1

        elif largo2 >= largo1 and largo2 >= largo3:
            nombre_mayor = nombre2
            cantidad = largo2

        else:
            nombre_mayor = nombre3
            cantidad = largo3

    return render_template(
        'ejercicio2.html',
        nombre_mayor = nombre_mayor,
        cantidad = cantidad
    )

if __name__ == '__main__':
    app.run(debug=True)