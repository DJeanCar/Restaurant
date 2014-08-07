from rest_framework import serializers
from .models import City, Restaurant, Establishment, Category

class CitySerializer(serializers.ModelSerializer):

	class Meta:
		model = City

class RestaurantSerializer(serializers.ModelSerializer):

	class Meta:
		model = Restaurant
		fields = ('id', 'name', 'description')

class EstablishmentSerializer(serializers.ModelSerializer):

	restaurant = RestaurantSerializer()

	class Meta:
		model = Establishment
		fields = ('address',)

class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category