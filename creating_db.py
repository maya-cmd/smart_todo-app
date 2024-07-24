from app import app, db
from app import Tasks  # Import your model(s)

with app.app_context():
    db.create_all()
