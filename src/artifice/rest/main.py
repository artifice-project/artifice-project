from app import app as application
from app import db as database


database.create_all()

application.run(
    port=10000,
    debug=True
)
