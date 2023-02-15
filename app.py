from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from form import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "hello"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    """Render home page"""

    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Renders pet form(GET) or handles pet form submission"""

    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Renders page to show pet information and edit pet form or handles edit pet form submission"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")

    else:
        return render_template("show_pet_info.html", pet=pet,form=form)