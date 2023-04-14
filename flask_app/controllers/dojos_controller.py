from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.dojos_model import Dojo

# front page, it will redirect to /dojos page
@app.route('/')
def index():
    return redirect('/dojos')

# form to add a dojo, add a ninja, and also displays list of dojos
@app.route('/dojos')
def select_dojos():
    list_of_dojos = Dojo.get_all()
    return render_template('dojos.html', list_of_dojos = list_of_dojos)

# page to collect and transfer new dojo being created
@app.route('/dojos/new', methods=['POST'])
def add_new_dojo():
    new_dojo = {
        'name' : request.form['name']
    }
    dojo_id = Dojo.add_dojo( new_dojo )
    return redirect('/dojos')

# displays the dojo with all its current ninjas
@app.route('/dojos/<int:id>')
def display_dojo_with_ninjas(id):
    data = {
        'dojo_id' : id
    }
    current_dojo = Dojo.get_one_with_ninjas( data )
    return render_template('dojo_and_ninjas.html', current_dojo = current_dojo)