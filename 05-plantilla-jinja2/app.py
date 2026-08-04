from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def inicio():
    nombre_usuario = "LESTER MIRANDA"
    return render_template('inicio.html', usuario=nombre_usuario)

if __name__ == '__main__':
    app.run(debug=True)
