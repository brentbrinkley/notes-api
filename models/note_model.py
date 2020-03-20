import os
import peewee

db_proxy = peewee.Proxy()

# --------------------------------------------
# Heroku config provided by heroku
# --------------------------------------------

if "HEROKU" in os.environ:
    import urllib.parse as urlparse
    import psycopg2

    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    db = peewee.PostgresqlDatabase(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
    )
    db_proxy.initialize(db)
else:
    db = peewee.SqliteDatabase("notes.db")
    db_proxy.initialize(db)

# --------------------------------------------
# Note Model
# --------------------------------------------
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
