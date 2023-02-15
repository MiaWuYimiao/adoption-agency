from models import Pet, db
from app import app

app.app_context().push()
# Create pets table
db.drop_all()
db.create_all()

Pet.query.delete()

# Add sample pets
pet1 = Pet(name="Woofly", species="Cat", photo_url="https://images.ctfassets.net/440y9b545yd9/7jnBjgsgS8KFPqMZ9KW2lG/3ec550bbe9bbc1010b022c869b537074/cat-banner.png")
pet2 = Pet(name="Porchetta", species="What")
pet3 = Pet(name="Snargle", species="Dog", photo_url="https://media.istockphoto.com/id/1068752692/photo/german-shepherd-dog-puppy.jpg?s=170667a&w=is&k=20&c=o4EtaA8i-CLoELYLIfGmAJdIDJaolC59YlA5OJMPba8=")

db.session.add_all([pet1, pet2, pet3])
db.session.commit()