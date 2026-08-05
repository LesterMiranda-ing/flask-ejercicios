from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/saludo', methods=['GET', 'POST'])
def saludo():
    nombre = request.form['nombre']
    return render_template('saludo.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)