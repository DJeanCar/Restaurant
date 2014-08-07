from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework_nested import routers as rnested
from .viewSets import CityViewSet, RestaurantViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'ciudades', CityViewSet)

category_router = rnested.NestedSimpleRouter(router, r'ciudades', lookup="ciudades")
category_router.register(r'restaurants', RestaurantViewSet)

city_router = rnested.NestedSimpleRouter(router, r'ciudades', lookup="ciudades")
city_router.register(r'categorias', CategoryViewSet)
#city_router.register(r'restaurants', RestaurantViewSet)





urlpatterns = patterns('',
	url(r'^api/', include(router.urls)),
	url(r'^api/', include(city_router.urls)),
	url(r'^api/', include(category_router.urls)),
)	
