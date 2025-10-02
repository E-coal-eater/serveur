from flask import Flask, render_template, request, redirect, url_for
app= Flask(__name__)
@app.route("/")

def home():
    return render_template('patapim.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')  # récupère la valeur du champ username
        password = request.form.get('password')  # récupère la valeur du champ password
        
        # Simple vérification
        if username == 'BrimBrim Patapim' and password == '123456789':
            return redirect(url_for('brimbrim'))
        else:
            return 'Nan Zaza paye pas stp', 401
    
    # Si GET, afficher le formulaire HTML
    return render_template('patapim.html')

@app.route('/brimbrim')
def brimbrim():
    return render_template('brimbrim.html')

if __name__ == '__main__':
    app.run(debug=True)
