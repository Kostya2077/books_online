from django.db.models import CharField, ForeignKey, Model, CASCADE, AutoField
from django.db.models import signals
from django.dispatch import receiver
from django.db import connection
import json

class Author(Model):
    name = CharField(max_length=55, db_index=True, unique=True, verbose_name="Имя")
    books = CharField(max_length=9999, default="[]", verbose_name="Книги")

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


    class Meta:
        ordering = ["name"]
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(Model):
    name = CharField(max_length=255, db_index=True, null=False, unique=True, verbose_name="Название")
    author = ForeignKey(Author, on_delete=CASCADE, null=False, verbose_name="Автор")


    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


    class Meta:
        ordering = ["name", "author"]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


@receiver(signals.pre_save, sender=Book)
def update_author(sender, instance, *args,**kwargs):
    autor = Author.objects.get(id=instance.author_id)
    data = json.loads(autor.books)
    if instance.name not in data:
        data.append(instance.name)
        autor.books = json.dumps(data)
        autor.save()
