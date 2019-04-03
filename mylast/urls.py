"""mylast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path



from django.conf.urls import url

from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from commerece import views

#from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
#urlpatterns = [
   # path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#]

# urlpatterns = {
#     # ath('', admin.site.urls),
#     url(r'', admin.site.urls),
#
#     url(r'^admin/', admin.site.urls),
#     url(r'^commerece/', include('commerece.urls')),
#
# }
# urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import include, path
from rest_framework import routers
from  rest_framework.authtoken.views import ObtainAuthToken
from commerece import views
from django.conf import settings
router= routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
from django.contrib import admin
#from order import views
#routerr = routers.DefaultRouter()
#routerr.register(r'order', views.UserViewSett)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from django.conf.urls.static import static
urlpatterns = [
   # path('', include(router.urls)),
   # path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('auth/',ObtainAuthToken.as_view()),
    path('admin/',admin.site.urls),
    path('',include('commerece.urls')),

   path('seller_post/',include('order.urls')),
   path('buyer_post/', include('order.urls')),
# path('seller_post/',include('customer.urls')),
#    path('buyer_post/', include('customer.urls')),
    path('checkout/', include('transaction.urls')),

    #path('logout/', views.logout),
#path('rest-auth/', include('rest_auth.urls')),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
