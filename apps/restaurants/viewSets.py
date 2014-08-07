from django.shortcuts import get_object_or_404, Http404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import link

from .models import City, Restaurant, Establishment, Category
from .serializers import *



class CityViewSet(viewsets.ModelViewSet):

	model = City
	serializer_class = CitySerializer


class RestaurantViewSet(viewsets.ModelViewSet):

	model = Restaurant

	def list(self, request, ciudades_pk):
		"""
		Muesta la lista de restaurants en una ciudad
		"""	
		establishments = Establishment.objects.filter(city__pk = ciudades_pk).order_by('restaurant__name').distinct('restaurant__name')
		restaurants = [establishment.restaurant for establishment in establishments]
		serializer = RestaurantSerializer(restaurants, many=True)
		return Response(serializer.data)
		
	def retrieve(self, request, ciudades_pk ,pk):
		"""
		Muestra el detalle de un restaurant de una ciudad
		"""
		restaurant = get_object_or_404(Restaurant, pk = pk)

		if restaurant.establishment_set.filter(city__pk = ciudades_pk):
			serializer = RestaurantSerializer(restaurant)
			return Response(serializer.data)
		else:
			raise Http404

	@link()
	def establecimientos(self, request,ciudades_pk ,pk=None):
		establishment = get_object_or_404(Establishment, pk = pk, city__pk = ciudades_pk)
		establishment = Establishment.objects.filter(restaurant__pk = establishment.restaurant.id,  city__pk = ciudades_pk)
		serializer = EstablishmentSerializer(establishment, many=True, context={'request': request})
		return Response(serializer.data)




class CategoryViewSet(viewsets.ModelViewSet):

	model = Category

	def list(self, request, ciudades_pk):
		"""
		Muesta la lista de restaurants en una ciudad
		"""
		categorys = Category.objects.all()
		serializer = CategorySerializer(categorys, many=True)
		return Response(serializer.data)
		
	def retrieve(self, request,ciudades_pk ,pk):
		"""
		Muestra el detalle de un restaurant de una ciudad
		"""
		print Establishment.objects.filter(restaurant__category__pk = pk, city__pk=ciudades_pk)
		category = get_object_or_404(Category, pk = pk)
		serializer = CategorySerializer(category)
		return Response(serializer.data)

	@link()
	def restaurants(self, request,ciudades_pk ,pk=None):
		establishments = Establishment.objects.filter(city__pk = ciudades_pk, restaurant__category__pk = pk)
		restaurants = [establishment.restaurant for establishment in establishments]
		serializer = RestaurantSerializer(restaurants, many=True)
		return Response(serializer.data)