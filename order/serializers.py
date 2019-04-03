from django.contrib.auth.models import User, Group
from rest_framework import serializers
from  order.models import Seller,Buyer,Khan


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','id', 'username', 'email', 'groups')
class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = ('catagory','product_name','product_quality','product_quentity','product_shiping',
                  'product_price','description','province','city','product_image','user_key','latitude','langitude')
class BuyerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buyer
        fields = ('catagory','product_name','product_quality','product_quentity','product_shiping',
                  'product_price','description','province','city','product_image','user_key','latitude','langitude')


class KhanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Khan
        fields = ('catagory','product_name','product_quality','product_quentity','product_shiping',
                  'product_price','description','province','city','product_image','product_image_one','user_key','latitude','langitudee','customer','expire')


