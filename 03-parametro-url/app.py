from flask import Flask

app = Flask(__name__)

@app.route('/estudiante/<nombre>')
def returnar_estudiante(nombre):
    return f'Hola, perfil de {nombre}'

if __name__ == '__main__':
    app.run(debug=True)