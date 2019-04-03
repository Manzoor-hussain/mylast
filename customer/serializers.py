from django.contrib.auth.models import User, Group
from rest_framework import serializers
from customer.models import Customerr


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','id', 'username', 'email', 'groups')
class CommonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customerr
        fields = ('catagory','product_name','product_quality','product_quentity','product_shiping',
                  'product_price','description','province','city','product_image','product_image_one','Identity','latitude','langitude','type','expire')
