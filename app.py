from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'admin' and password == 'admin':
            session['user'] = username
            return redirect(url_for('welcome'))
        else:
            flash('Usuario o contraseña incorrectos.')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'user' in session:
        user = session['user']
        return render_template('welcome.html', user=user)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)