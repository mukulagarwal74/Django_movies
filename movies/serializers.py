from rest_framework import serializers
from .models import Movie, Cast, Genre, Director
class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MainSeializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'
    movie = MovieSerializer(read_only=True, many=True)
    cast = CastSerializer(read_only=True,many=True)
    director = DirectorSerializer(read_only=True,many=True)
    genre = GenreSerializer(read_only=True,many=True)
    
# class CastSerializer(serializers.ModelSerializer):
# # class CastSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Cast
#         fields = ('name', 'gender', 'age')

# # class DirectorSerializer(serializers.HyperlinkedModelSerializer):
# class DirectorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Director
#         fields = ('name', 'gender', 'age')

# # class GenreSerializer(serializers.HyperlinkedModelSerializer):
# class GenreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = ('genre',)

# class MovieSerializer(serializers.ModelSerializer):
#     cast = CastSerializer(read_only=True,many=True)
#     class Meta:
#         model = Movie
#         fields = ('name', 'id')

# class MovieSerializer(serializers.ModelSerializer):
#     # cast = CastSerializer(read_only=True,many=True)
#     # cast = CastSerializer(read_only=True, many=True)
#     class Meta:
#         model = Movie
#         fields = ('name', 'id')