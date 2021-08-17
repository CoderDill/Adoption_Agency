from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

pet1 = Pet(name="Buster", species="Dog",
           photo_url="data:image/jpeg;base64,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",
           age=4)

pet2 = Pet(name="Peter Cotton Tail", species="Rabbit",
           photo_url="data:image/jpeg;base64,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",
           age=4)

db.session.add_all([pet1, pet2])
db.session.commit()