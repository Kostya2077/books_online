from django.db.models import CharField, ForeignKey, Model, CASCADE, IntegerField, F, AutoField
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
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, db_index=True, unique=True, null=False, verbose_name="Название")
    author = ForeignKey(Author, on_delete=CASCADE, null=False, verbose_name="Автор", to_field="name")


    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


    class Meta:
        ordering = ["name"]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


"""СЧЁТЧИК КОЛИЧЕСТВА КНИГ АВТОРА"""

"""при сохранении прибавляем 1 в поле count_books класса Author"""
@receiver(signals.pre_save, sender=Book)
def add_book_author(sender, instance, *args,**kwargs):
    Author.objects.filter(name=instance.author).update(count_books=F('count_books')+1)
    """
    если перед сохранением книга была у другого автора, убираем 1 книгу у того автора,
    у которого она была
    """
    found_book = Book.objects.filter(name=instance.name)
    if found_book:
        Author.objects.filter(name=found_book[0].author).update(count_books=F('count_books') - 1)


"""при удалении убираем 1 книгу из поля count_books класса Author"""
@receiver(signals.pre_delete, sender=Book)
def remove_book_author(sender, instance, *args,**kwargs):
    Author.objects.filter(name=instance.author).update(count_books=F('count_books')-1)
