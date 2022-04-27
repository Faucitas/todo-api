from app.extentions import ma
from app.database import (Model, Column, String, Boolean, Integer)


class Task(Model):
    __tablename__ = 'tasks'
    _id = Column(Integer, primary_key=True)
    description = Column(String(120), nullable=False)
    complete = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<Task %r>' % self.description


class TaskSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Task

    _id = ma.auto_field()
    description = ma.auto_field()
    complete = ma.auto_field()