from django.db.models import CharField, ForeignKey, Model, CASCADE, IntegerField
from django.db.models import signals
from django.dispatch import receiver


class Author(Model):
    name = CharField(max_length=55, db_index=True, unique=True, verbose_name="Имя")
    count_books = IntegerField(default=0, verbose_name="Количество книг")

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
        ordering = ["name"]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


@receiver(signals.pre_save, sender=Book)
def add_book_author(sender, instance, *args,**kwargs):
    author = Author.objects.get(id=instance.author_id)
    author.count_books = int(author.count_books) + 1
    author.save()


@receiver(signals.pre_delete, sender=Book)
def remove_book_author(sender, instance, *args,**kwargs):
    author = Author.objects.get(id=instance.author_id)
    author.count_books = int(author.count_books) - 1
    author.save()
