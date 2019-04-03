# from django.contrib.auth.models import User
# from rest_framework import serializers
#
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django import forms
from commerece.models import Test
from commerece.models import Contact, Conversation, Chat,Message


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'password', 'email')


class UserSerializerr(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # password = serializers.CharField(min_length=8)
    password = serializers.CharField(min_length=6, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class TestSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Test;
        fields = ['first_name', 'last_name']


class ContactSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Contact;
        fields = ['name', 'mobile_number', 'messsage', 'sender_mail']


class ConversationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Conversation
        fields = ('id', 'post_key', 'user_one', 'user_two')


class ChatSerializer(serializers.ModelSerializer):

    #conversation = serializers.RelatedField( read_only=True)


    class Meta:
        model = Chat
        fields = ('id', 'message', 'conversation_id')
class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp','post_key','sender_name','receiver_name','group_id','sender_image','receiver_image']
