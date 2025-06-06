from flask import Flask
from flask_cors import CORS
from db import db

from api.users import user_bp
from api.courses import course_bp

app = Flask(__name__)
CORS(app)

# DB config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(course_bp)

# create db
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
