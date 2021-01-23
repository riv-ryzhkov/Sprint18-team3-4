from .models import Author
from rest_framework import serializers, generics


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic')


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorDetailSerializer