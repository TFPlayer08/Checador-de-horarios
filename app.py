from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#app.secret_key = 'tu_clave_secreta_aqui'  # Necesario para sessions y flash

@app.route("/")
def index():
    return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if not request.form.get("username"):
            flash('El nombre de usuario es obligatorio!')
            return redirect(url_for('index'))
        
        elif not request.form.get("password"):
            flash('La contraseña es obligatoria!')
            return redirect(url_for('index'))
        
        elif not request.form.get("confirm_password"):
            flash('La confirmación de la contraseña es obligatoria!')
            return redirect(url_for('index'))
        
        elif request.form.get("password") != request.form.get("confirm_password"):
            flash('Las contraseñas no coinciden!')
            return redirect(url_for('index'))
        
        # Aquí puedes agregar la lógica para guardar el usuario
        flash('Usuario registrado exitosamente!')
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route("/estadisticas")
def statistics():
    return render_template("estadisticas.html")

@app.route("/vacaciones", methods=["GET", "POST"])
def vacations():
    return render_template("vacaciones.html")

@app.route("/inicio", methods=["GET", "POST"])
def inicio():
    return render_template("inicio.html")
if __name__ == '__main__':
    app.run(debug=True)