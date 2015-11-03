# coding: utf-8
from flask_wtf import Form

from wtforms.fields import TextField, FileField, PasswordField
from wtforms.fields import IntegerField, BooleanField, SelectField
from wtforms.fields import TextAreaField, FieldList, FormField
from wtforms.ext.dateutil.fields import DateTimeField
from wtforms.validators import ValidationError, InputRequired, EqualTo,\
    Email, Optional

class IngrForm(Form):

    ingr = TextField(u'Название ингредиента')
    measure = TextField(u'В чём измеряется?')
    qty = TextField(u'Количество')
    tags = TextField(u'Тэги')
    meat = BooleanField(u'Мясо?')


class StageForm(Form):

    text = TextAreaField(u'Описание этапа')
    image = FileField(u'Приложите изображение')
    ingrs = FieldList(FormField(IngrForm), min_entries=1)


class RecipieForm(Form):

    recipie = TextField(u'Название рецепта')
    preamble = TextAreaField(u'Вводная информация')
    stages = FieldList(FormField(StageForm), min_entries=1)
    image = FileField(u'Приложите изображение')
