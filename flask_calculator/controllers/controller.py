from flask import render_template
from app import app
from modules.calculator import add

@app.route('/add/<input_1>/<input_2>')
def add_page(input_1, input_2):
    result = add(input_1, input_2)
    return render_template('add.html', number_1=input_1, number_2=input_2, result=result)