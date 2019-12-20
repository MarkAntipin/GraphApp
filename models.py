import peeweedbevolve
from peewee import (
    Model, AutoField, CharField, IntegerField
)
from playhouse.shortcuts import model_to_dict
from playhouse.postgres_ext import PostgresqlExtDatabase, ArrayField

from settings.config import PG_CONN

db = PostgresqlExtDatabase(**PG_CONN, server_side_cursors=True)


class BaseModel(Model):

    def as_dict(self, **kwargs):
        return model_to_dict(self, **kwargs)

    class Meta:
        database = db


class Words(BaseModel):
    id = AutoField(index=True, primary_key=True)
    word = CharField(index=True, unique=True)
    word_length = IntegerField()


if __name__ == '__main__':
    peeweedbevolve.evolve(
        db,
        interactive=False,
        ignore_tables=['basemodel']
    )
