from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'IamACookie'  # Cambia esto a una clave más segura

# Usuario y contraseña por defecto
USERNAME = 'MC'
PASSWORD = '123456'

@app.route('/')
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))  # Si ya está autenticado, redirigir a dashboard
    return render_template('login.html')  # Mostrar página de login

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        session['username'] = username  # Guardar el usuario en la sesión
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', error='Usuario o contraseña incorrectos')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:  # Verificar si el usuario está en sesión
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))  # Redirigir al login si no está autenticado

@app.route('/logout')
def logout():
    session.pop('username', None)  # Eliminar la sesión de usuario
    return redirect(url_for('login'))  # Redirigir al login

if __name__ == '__main__':
    app.run(debug=True)
