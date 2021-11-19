from django.db.models import CharField, ForeignKey, Model, CASCADE


class Author(Model):
    name = CharField(max_length=55)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Book(Model):
    name = CharField(max_length=255, db_index=True)
    author = ForeignKey(Author, on_delete=CASCADE)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
