from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Farm(db.Model):
    name = db.Column(db.String(120), primary_key=True)
    address = db.Column(db.String(120))

    @staticmethod
    def get_all():
        return Farm.query.all()

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<FarmList: {}>".format(self.name)
