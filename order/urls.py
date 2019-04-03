from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from order import views


# router = routers.DefaultRouter()
# router.register(r'login', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

#router.register(r'accounts', AccountViewSet)
# urlpatterns = router.urls

urlpatterns = [
    url(r'^$', views.IndexVieww.as_view(), name='index'),
   url(r'^check$', views.SellerPost.list, name='list'),
  url(r'^submit$', views.BuyerPost.list_order, name='list_order'),
   # url(r'lagout/$', views.logout, name='lagout'),

   #url(r'^register/$', views.registerView.as_view(), name='register'),


]


