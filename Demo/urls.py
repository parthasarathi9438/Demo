"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app import views
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewset)
router.register(r'groups', views.GroupViewset)
router.register('app', views.ProductModelviewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    #modelviewset
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('product_modelviewset/',include('app.urls')),
    #apiview
    path('product/',views.ProductOperations.as_view(), name="product"),
    path('one_product/<product>',csrf_exempt(views.OneProductOperation.as_view()), name="oneproductoperation"),
    #viewset
    path('product_viewset/',views.ProductOperationsViewset.as_view({'get':'list'}), name="productoperationsviewset"),
    path('save_product_viewset/', views.ProductOperationsViewset.as_view({'post':'create'}), name="saveproductoperationsviewset"),
    path('read_data_one/<int:pk>/',views.ProductOperationsOne.as_view({'get':'retrieve'})),
    path('update_data_one/<int:pk>/',views.ProductOperationsOne.as_view({'put':'update'})),
    path('delete_data_one/<int:pk>/',views.ProductOperationsOne.as_view({'delete':'destroy'})),
]
