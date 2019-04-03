from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from commerece import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from commerece.views import Logout

urlpatterns = [
    url(r'commerece/$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'home/$', views.details_home_display, name='details_home_display'),
    url(r'contact/$', views.contactView.contactt, name='contactt'),
    url(r'contact/message$', views.Contact_admin.contact, name='contact'),

    #url(r'lagout/$', views.logout, name='lagout'),
    url(r'inbox/(?P<post_id>[0-9]+)/(?P<user_name>[\w\-]+)', views.chatt, name='chatt'),
    url(r'inbox/', views.chat, name='chat'),
 #   url(r'inbox/(?P<string>[\w\-]+)$', views.chat_message, name='chat_message'),
  #  url('chat/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
  #  path('api/messages', views.message_list, name='message-list'),
   # url(r'send/$',views.send_emaill, name='send_email'),









   url(r'register/create$', views.UserCreate.create_list, name='create_user_list'),

    url(r'register/send$', views.send_sms, name='send_sms'),
  # url(r'register/api$', view=views.rregister.as_view()),
    url(r'^login/login_user$', views.loginView.login_user, name='login_user'),
  #  url(r'^login/login_user/(?P<id>[0-9]+)/$', views.loginView.login_user, name='login_user'),
    url(r'^login/$', views.loginView.as_view(), name='login'),
    url(r'^login/user/(?P<id>[0-9]+)/$', views.home_page_method, name='home_page_method'),
    #url(r'^login/user/(?P<id>[0-9]+)/check$', views.loginn, name='loginn'),
    url(r'register/$', views.registerView.as_view(), name='register'),
   # url(r'^login/user/(?P<int>[0-9]+)/logout/$', views.logout, name='logout'),
   url(r'myads/$', views.details_myads, name='details_myads'),
    url(r'myorder/$', views.details_order_method, name='details_order_method'),

url(r'seller_request/$', views.details_seller_request, name='details_seller_request'),
url(r'buyer_order/$', views.details_buyer_order, name='details_buyer_order'),

    url(r'seller_post/$', views.seller_post, name='seller_post'),
    url(r'buyer_post/$', views.buyer_post, name='buyer_post'),

    url(r'^logout/', Logout.as_view(),name="Lagout"),
    url(r'seller_request/(?P<id>[0-9]+)/(?P<user_idd>[0-9]+)/(?P<diff>[\w\-]+)',views.complete_details, name="complete_details"),
    url(r'buyer_order/(?P<id>[0-9]+)/(?P<user_idd>[0-9]+)/(?P<diff>[\w\-]+)', views.complete_details, name="complete_details"),
    url(r'checkout/$', views.check_out, name='check_out'),
    url(r'search/$', views.search, name='search'),
    url(r'delete/(?P<id>[0-9]+)/(?P<user_type>[\w\-]+)',views.delete_Ads, name='delete_ads'),



]
#AIzaSyAq-ujHaiq-3WfIa0KDqJY_aew7pzGxdmc
