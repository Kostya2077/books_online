from rest_framework import serializers
from .models import *


""" Сериализатор базового класса Book для перевода данных в формат JSON """
class BookSerializer(serializers.ModelSerializer):


    class Meta:
        model = Book
        fields = ["name", "author"]
