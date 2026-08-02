import re
from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def formulario():
    # 1. PASO CLAVE: Inicializar la variable al principio de la función
    error = None 

    if request.method == 'POST':
        nombre = request.form.get('nombre', 'Visitante').strip()
        
        if not nombre:
            error = 'Por favor, ingresa un nombre válido.'
        elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            error = 'Error: El nombre solo puede contener letras y espacios.'
        
        # Ojo: Verificamos si NO hubo error para retornar la respuesta exitosa
        if not error:
            return f'<h1>Hola, {nombre} tu formulario fue procesado con éxito</h1>'

    # 2. Agregamos la 'f' al inicio de f''' para que reconozca la variable {error}
    html_form = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Formulario GET/POST</title>
    </head>
    <body>
        <h2>Formulario de Entrada</h2>

        <!-- Si 'error' tiene texto, muestra el párrafo rojo. Si es None, muestra string vacío '' -->
        {f"<p style='color: red;'>{error}</p>" if error else ""}

        <form method='POST'>
            <label for='nombre'>Nombre:</label>
            <input type='text' id='nombre' name='nombre' placeholder="Escribe algo...">
            <button type='submit'>Enviar</button>
        </form>
    </body>
    </html>
    '''
    return render_template_string(html_form)


if __name__ == '__main__':
    app.run(debug=True)