from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/menu')
def menuMexicana():
    return render_template('menu.html')

@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

if __name__ == '__main__':
    app.run(debug=True)