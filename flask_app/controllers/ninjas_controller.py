from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo

# page with form to add a new Ninja
@app.route('/ninjas')
def add_ninja_form():
    list_of_dojos = Dojo.get_all()
    return render_template('ninjas.html', list_of_dojos = list_of_dojos )

# page used to collect and transfer info of a new ninja
@app.route('/ninjas/new', methods=['POST'])
def add_new_ninja():
    print(request.form)
    new_ninja = {
        'dojo_id' : request.form['dojo_id'],
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age']
    }
    ninja_id = Ninja.add_ninja( new_ninja )
    return redirect('/dojos')