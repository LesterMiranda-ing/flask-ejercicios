from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Pagina Principal'

@app.route('/contacto')
def contacto():
    return 'Pagina de Contacto'

@app.route('/cursos')
def cursos():
    return 'Pagina de Cursos'

if __name__ == '__main__':
    app.run(debug=True)