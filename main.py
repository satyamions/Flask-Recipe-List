import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    image_filename = db.Column(db.String(255), nullable=True)

class RecipeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    image = FileField('Image')
    submit = SubmitField('Submit')

@app.route('/')
def index():
    recipes = Recipe.query.all()
    return render_template('index_template.html', recipes=recipes)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        image_filename = None
        if form.image.data:
            image = form.image.data
            image_filename = image.filename
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
        recipe = Recipe(
            name=form.name.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
            image_filename=image_filename
        )
        db.session.add(recipe)
        db.session.commit()
        flash('Recipe added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_recipe_template.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    form = RecipeForm(obj=recipe)
    if form.validate_on_submit():
        recipe.name = form.name.data
        recipe.ingredients = form.ingredients.data
        recipe.instructions = form.instructions.data
        if form.image.data:
            image = form.image.data
            image_filename = image.filename
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
            recipe.image_filename = image_filename
        db.session.commit()
        flash('Recipe updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('update_recipe_template.html', form=form)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    if recipe.image_filename:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], recipe.image_filename))
    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
