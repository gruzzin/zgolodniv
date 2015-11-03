from flask import Blueprint, render_template, request
from flask import current_app as app

from zgolodniv.models import Product, Stage, Recipie
from zgolodniv.forms import RecipieForm

from pprint import pprint

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        form = RecipieForm(class_='form-horizontal')
        return render_template('form_test.html', form=form)
    elif request.method == 'POST':
        return pprint(request.form)
