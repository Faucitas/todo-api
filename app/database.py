from app.extentions import db

# Common DB aliases
Column = db.Column
String = db.String
Boolean = db.Boolean
Integer = db.Integer


class Model(db.Model):
    __abstract__ = True
    @classmethod
    def get_all(cls, **kwargs):
        if kwargs:
            return cls.query.filter_by(**kwargs)
        return cls.query.all()

    @classmethod
    def get(cls, id):
        return cls.query.get_or_404(id)