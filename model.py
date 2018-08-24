import peewee

db = peewee.SqliteDatabase("notes.db")


class Note(peewee.Model):
    id = peewee.PrimaryKeyField()
    color = peewee.CharField()
    shape = peewee.CharField()
    midi_val = peewee.IntegerField()
    common_notation = peewee.CharField()
    hex = peewee.CharField()
    svg = peewee.CharField()

    class Meta:
        database = db

    def __str__(self):
        return f"{self.midi_val} {self.color} {self.shape}"


def initialize_db():
    db.connect()
    db.create_tables([Note], safe=True)
    db.close()
