import time
from ast import parse
from django.shortcuts import render
from  django.contrib import  messages
import  json
from tkinter import messagebox
from django.db.models import Count, QuerySet
from  django.conf import settings
from django.contrib.auth import authenticate, login,user_logged_out
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from rest_framework.parsers import JSONParser
from django import template

register = template.Library()
from django.core.paginator import Paginator

from  order.models import Seller,Khan
from django.core.mail import send_mail
import numpy
from django.template.defaultfilters import linebreaks

# Create your views here.
from django.views import generic
#from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

#from commerece.serializers import UserSerializer
from commerece.serializers import UserSerializer
from .models import Album, Song ,Message
#from django.contrib.auth.models import User
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from commerece.serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from  rest_framework.authtoken.models import  Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from  rest_framework import exceptions

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from commerece.serializers import UserSerializerr ,ContactSerilizer,ConversationSerializer,ChatSerializer,MessageSerializer
from rest_framework.decorators import api_view, permission_classes



from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from  rest_framework.request import clone_request
from  commerece.models import Test
app_name = 'commerece'
from django.core.mail import BadHeaderError, send_mail
from googlevoice import Voice
from twilio.rest import Client
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

ccode = ''
def send_emaill(request):
    subject = "MAnzooor"
    message = 'hellow dear'
    to_list = ['nawaz2015@namal.edu.pk', settings.EMAIL_HOST_USER]
    from_email = settings.EMAIL_HOST_USER


    send_mail(subject, message, from_email, to_list, fail_silently=True)




        # In reality we'd use a form class
        # to get proper validation errors.
        #return HttpResponse('Make sure all fields are entered and valid.')

class IndexView(generic.ListView):
    template_name = 'commerece/base.html'
    context_object_name = 'all_albums'

    subject="MAnzooor"
    message='hellow dear'
    to_list=['manzoor2015@namal.edu.pk',settings.EMAIL_HOST_USER]
    from_email=settings.EMAIL_HOST_USER

   # send_mail(subject, message, from_email, to_list, fail_silently=True)
    index=True
    context ={
        'index':index
    }

    def get_queryset(self):
        return render(self.request,'commerece/base.html',self.context)


    def fromview(request):
        if request.session.has_key('id'):
            id = request.session['id']
        return render(request, 'commerece/home.html', {"id": id})

class contactView(generic.ListView):
    template_name = 'commerece/contact.html'
    def get_queryset(self):
        return Album.objects.all()
    def contactt(request):
        return render(request,template_name='commerece/contact.html')

class chatView(generic.ListView):
    template_name = 'commerece/chat.html'
    def get_queryset(self):
        return Album.objects.all()


def home_page_method(request, id):

    if request.session.has_key('token'):
       # return render(request, "commerece/home.html")
        return redirect('/home')

   # if(request.session['id']==''):
    else:
     return redirect(reverse('login'))





class home_page(generic.ListView):
    template_name = 'commerece/home.html'
    context_object_name = 'all_albums'


    def get_queryset(self):
        return Album.objects.all()

    def home_page_method(request):
        import pdb;
        pdb.set_trace()
        if request.method == "POST":
            import pdb;
            pdb.set_trace()



@api_view(['GET', 'POST'])
def send_sms(request):
    #template_name="commerece/register"
    #renderer_classes = [TemplateHTMLRenderer]
    number=''

    if request.method == "POST":
        number = request.POST['mobile']

    X = numpy.random.randint(0, 10, size=6)
    account_sid = "ACd3974ac779ddf5c1278e6970686a0b9a"
    auth_token = "61bee5dc8cf80ecb63cc4f186f808288"
    client = Client(account_sid, auth_token)
    code=''

    for x in X:
        code += str(x)
    ccode = code
    request.session['ccode'] = str(ccode)
    request.session['number'] = str(number)
    # message = client.messages \
    #    .create(
    #    body="Verificatoin code is:"+ ccode+".This code will expire in 5 minutes",
    #    from_='+15759151305',
    #    to='+92'+number)

    time.sleep(5)
    return redirect(reverse('register'))

    #return render(request, reverse('register'))
    # data = {
    #
    #         reverse('commerece/contact/', args=[1],)
    #     }
   # return  Response(reverse('commerece/register'))

   # print
   # message.sid

class loginView(generic.ListView):
    template_name = 'commerece/login.html'
    context_object_name = 'all_albums'
    renderer_classes = [TemplateHTMLRenderer]


    def get_queryset(self):
        return User.objects.filter(username='sana').values('id').get().get('id')

    def login_user(request):

        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                   # albums = Album.objects.filter(user=request.user)
                    token = Token.objects.create(user=user)

                    user = User.objects.filter(username=username).values('id').get().get('id')
                    request.session['id'] = str(user)
                    request.session['token'] = token.key


                    return redirect('user/'+str(user))
                   # import pdb;pdb.set_trace()
                    return render(request, 'commerece/home.html', {'user': user})
                else:
                    return render(request, 'commerece/login.html', {'error_message': 'Your account has been disabled'})
            else:
                return render(request, 'commerece/login.html', {'error_message': 'Invalid login'})
        return render(request, 'commerece/login.html')

class registerView(generic.ListView):
    template_name = 'commerece/register.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

# class rregister(generics.CreateAPIView):
#     def post(self, request, *args, **kwargs):
#         username=request.post.get('username')
#         email = request.post.get('email')
#         password = request.post.get('password')
#
#         user=User.objects.create_user(email,username,password)
#         user.save
#         token=Token.objects.create(user=user)
#         return  Response({'detail':'User has beeen created '+ token.key})


# class DetailView(generic.DetailView):
#     model = Seller
#     template_name = 'commerece/details.html'
#
#     def detail(request, id):
#         if not request.user.is_authenticated():
#             return render(request, 'commerece/login.html')
#         else:
#             user = request.user
#             ads= get_object_or_404(Seller, pk=id)
#             return render(request, 'commerece/MyAds.html', {'ads': ads, 'user': user})
# class details(generic.ListView):
#     template_name = 'commerece/MyAds.html'
#
#     def get_queryset(self):
#         return Seller.objects.all()
#     def details_get(self):
#
#         import pdb;
#         pdb.set_trace()

class chat_display(generic.ListView):
    template_name = 'commerece/chat.html'

    def get_queryset(self):
        return Seller.objects.all()

        return render(request, "commerece/MyAds.html")

@api_view(['GET', 'PUT', 'DELETE'])
def details_myads(request,id=None):
    # if request.method == "get":
    current_user = request.user


    #user = User.objects.filter(username='asif').values('id').get().get('id')
    ads_startt = Khan.objects.filter(user_key_id=current_user.id)
    ads_start = ads_startt.filter(customer='seller').order_by('id').reverse()
    ads = ads_startt.filter(customer='seller').order_by('id').reverse()[1:4]
    #last_ten = Mes.objects.filter(since=since).order_by('-id')[:10][::-1]
    count=True
    if request.session.has_key('token'):
        context = {
            'ads': ads,
            'count':count,
            'ads_start':ads_start

            # 'ss':json_string

        }

        return render(request, "commerece/MyAds.html", context)
    else:
       return  redirect('login')




@api_view(['GET', 'PUT', 'DELETE'])
def details_seller_request(request,id=None):
    # if request.method == "get":
   # user = User.objects.filter(username='asif').values('id').get().get('id')
    current_user=request.user
    adss = Khan.objects.all()
    all_user=User.objects.all()
    ads_start=adss.exclude(user_key=current_user.id,customer='buyer')[:1]
    ads = adss.exclude(user_key=current_user.id,customer='buyer')[2:7]
    seller_request='seller_request'



    count=True
    if request.session.has_key('token'):

            context = {
            'ads': ads,
            'count':count,

                'all_user':all_user,
                'ads_start':ads_start,
                'seller_request':seller_request,

            # 'ss':json_string
              }
            return render(request, "commerece/MyAds.html", context)

    else:
       return  redirect('login')
@api_view(['GET', 'PUT', 'DELETE'])
def details_order_method(request, id=None):
    # if request.method == "get":
    current_user=request.user
   # user = User.objects.filter(username='asif').values('id').get().get('id')


    # user = User.objects.filter(username='asif').values('id').get().get('id')
    ads_startt =Khan.objects.filter(user_key_id=current_user.id)
    ads_start=ads_startt.filter(customer='buyer').order_by('id').reverse()

    ads = ads_startt.filter(customer='buyer').order_by('id').reverse()[1:5]



    if request.session.has_key('token'):
        context = {
            'ads': ads,
            'ads_start':ads_start,




        }

        return render(request, "commerece/Myorder.html", context)
    else:
        return redirect('login')



def details_buyer_order(request, id=None):
    # if request.method == "get":
    current_user=request.user
   # user = User.objects.filter(username='asif').values('id').get().get('id')
    adss = Khan.objects.all()
    ads_start = adss.exclude(user_key=current_user.id,customer='seller')[:1]
    ads=adss.exclude(user_key=current_user.id,customer='seller')[2:5]
    buyer_request = 'buyer_request'



    if request.session.has_key('token'):
        context = {
            'ads': ads,
            'ads_start':ads_start,
            'buyer_request':buyer_request,

        }

        return render(request, "commerece/Myorder.html", context)
    else:
        return redirect('login')




@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def details_home_display(request, id=None):
   # authenticate_credentials(request,Token.key)

    # if request.method == "get":
    current_user=request.user


    seller_ad=Khan.objects.all()
    seller_adss=seller_ad.exclude(user_key_id=current_user.id)
    seller_ads=seller_adss.exclude(customer='buyer')


    paginator = Paginator(seller_ads, 1)  # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)


    buyer_order =seller_adss.exclude(customer='seller')
    #if not request.user.is_authenticated():

    check=True

    if request.session.has_key('token'):
        context = {

            'check':check,
            'seller_ads':seller_ads,
            'buyer_order':buyer_order,
            'contacts':contacts,

            # 'ss':json_string

        }

        return render(request, "commerece/home.html", context)

    else:
        #raise exceptions.AuthenticationFailed('Invalid token  bnbn')
        return redirect('login')


def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        # This is required for the time comparison
       # utc_now = datetime.utcnow()
        #utc_now = utc_now.replace(tzinfo=pytz.utc)

        #if token.created < utc_now - timedelta(hours=24):
         #   raise exceptions.AuthenticationFailed('Token has expired')

        return token.user, token

class UserViewSet(viewsets.ModelViewSet):
    """
   # API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #authentication_classes = (TokenAuthentication,)
   # permission_classes = (IsAuthenticated,)

class UserCreate(APIView):
    tempquestlate_name = 'commerece/login.html'
    context_object_name = 'all_albums'
    renderer_classes = [TemplateHTMLRenderer]

    @api_view(['GET', 'POST'])
    def create_list(request):
        if request.method == 'POST':
            code = request.data.get('code')
            mail =request.data.get('email')
            send_code=request.session['ccode']
            #if(code==ccode):dat
            #serializer = UserSerializerr(data=request.data)
            serializer = UserSerializerr(data=request.data)
            if (code == send_code):

                # import pdb;
                # pdb.set_trace()

                messages_complete = "You Account has been created:\n Thanks for joining us"

                if serializer.is_valid():

                    user = serializer.save()
                    subject = "From Employee"

                    to_list = [mail, settings.EMAIL_HOST_USER]
                    from_email = settings.EMAIL_HOST_USER

                    send_mail(subject, messages_complete, from_email, to_list, fail_silently=True)

                    #token = Token.objects.create(user=user)
                    albums = Album.objects.all()
                    update_profile(request,user.id)
                    #return render(request, 'commerece/login.html', {'albums': albums}, status=status.HTTP_201_CREATED)
                    return redirect(reverse('login'))



                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return render(request, 'commerece/register.html')




def logout(request):

   try:
      del request.session['id']

   except:
      pass
   return render(request,'commerece/base.html',{})
class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        del request.session['token']
        #return Response(status=status.HTTP_200_OK)
        return redirect('http://127.0.0.1:8000')

        return render(request, 'commerece/base.html', {})
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.profile.mobile_number=request.session['number']
    user.save()


class Contact_admin(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    @api_view(['GET', 'POST'])
    def contact(request):
        if request.method == 'POST':

            sender_mail= request.data.get('sender_mail')
            mobile_number= request.data.get('mobile_number')
            message=subject=request.data.get('messsage')
            messages_complete="Your Email:"+sender_mail  +"\n"+": Your Mobile Number:"+mobile_number+"\n Message :\n"+message


            #if(code==ccode):dat
            #serializer = UserSerializerr(data=request.data)
            serializer = ContactSerilizer(data=request.data)


            if serializer.is_valid():
                serializer.save()
                subject = "From Employee"

                to_list = [sender_mail, settings.EMAIL_HOST_USER]
                from_email = settings.EMAIL_HOST_USER

                send_mail(subject, messages_complete, from_email, to_list, fail_silently=True)
                #return reverse('contact')
                #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                return redirect('/contact')


            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def seller_post(request,id=None):
    template_name = 'order/seller.html'
    if request.session.has_key('token'):

        return render(request, 'order/seller.html')
    else:
        return redirect('login')

@api_view(['GET'])
def buyer_post(request,id=None):
    template_name = 'order/buyer.html'
    check=False
    if request.session.has_key('token'):

        context = {

            'check': check,

            # 'ss':json_string

        }

        return render(request, 'order/buyer.html',context)

    else:
        return redirect('login')



@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def complete_details(request, id=None,user_idd=None, diff=None):
   # authenticate_credentials(request,Token.key)

    # if request.method == "get":
    #user = User.objects.filter(username='asif').values('id').get().get('id')
    ads = Khan.objects.filter(id=id ,user_key_id=user_idd)
    #if not request.user.is_authenticated():
    seller_user=User.objects.filter(id=user_idd)


    check=False
    link=True
    condition='details'


    if request.session.has_key('token'):
        context = {
            'ads': ads,
            'check':check,
            'link':link,
             'condition':condition,
             'seller_user':seller_user,
             'diff':diff,

            # 'ss':json_string

        }

        return render(request, "commerece/Complete_details.html", context)

    else:
        #raise exceptions.AuthenticationFailed('Invalid token  bnbn')
        return redirect('login')


@api_view(['GET', 'PUT', 'DELETE'])
@register.filter(name='range')
def chat(request):
    template_name = 'commerece/chat.html'
    condition='chat'
    first_chat='first'
    current_user=request.user
    #conversation= Message.objects.filter(sender_id=current_user).annotate(Count('post_key')).values()
    conversation=Message.objects.filter(sender_id=current_user.id) | Message.objects.filter(receiver_id=current_user.id)
    # mm=conversation[1].get('receiver_id')
    list = []
    object_list =[]


    # for x in conversation:
    #     mmm=x.post_key
    #     nn=x.sender_id
    #     kk=mmm+nn
    #     if kk not in list:
    #         object_list.append(x)
    #     list.append(kk)
    #
    for x in conversation:
        if x.group_id not in list:
            object_list.append(x)
        list.append(x.group_id)

    listt = []
    user_list = []
    for use in object_list:
        key=use.receiver_id
        if key == current_user.id:
            key =use.sender_id
            keyy = User.objects.get(id=key)
            if use.sender_id not in listt:
                user_list.append(keyy)
            listt.append(use.receiver_id)
        else:
            keyy = User.objects.get(id=key)
            if use.receiver_id not in listt:
                user_list.append(keyy)
            listt.append(use.receiver_id)


    #conversation=Message.objects.values('id').annotate(Count('post_key'))



    # SELECT * FROM
    # `commerece_message`
    # WHERE
    # `sender_id` = 17
    # group
    # by
    # `post_key`
    #conversation = Message.objects.filter(sender_id=current_user, receiver=current_user).distinct('post_key').order_by( 'timestamp').reverse()
    items, item_ids = [], []
    manzoor=''

    conversation_id = conversation.values('receiver_id')[:1].get().get('receiver_id')
    chat_user=User.objects.filter(id=conversation_id)

   # conversation=User.objects.filter(id=conversation_id)

    if request.session.has_key('token'):
        context = {

             'condition':condition,
            'first_chat':first_chat,
            'conversation':object_list,
            'conversation_id': conversation_id,
            'chat_user': chat_user,
            'items_ads':item_ids,
            'user_list':user_list,




            # 'ss':json_string

        }

        return render(request, "commerece/chat.html", context)

    else:
        #raise exceptions.AuthenticationFailed('Invalid token  bnbn')
        return redirect('login')
@api_view(['GET', 'POST','PUT', 'DELETE'])
def chatt(request, post_id,user_name):



    #template_name = 'commerece/chat.html'

    condition = 'chat'

    chat_user = User.objects.filter(username=user_name)
    chat_ads = Khan.objects.filter(id=post_id)
    receiver = User.objects.filter(username=user_name).values('id').get().get('id')

    current_user=request.user
    receiver_name=User.objects.filter(username=user_name).values('username').get().get('username')
    #conversation=Message.objects.filter(sender_id=current_user , receiver=current_user)#.distinct('post_key').order_by('timestamp')
    #conversation = Message.objects.filter(sender_id=current_user).annotate(Count('post_key')).values()

    conversation = Message.objects.filter(sender_id=current_user.id) | Message.objects.filter(receiver_id=current_user)
    # mm=conversation[1].get('receiver_id')
    list = []
    object_list = []
    user_list = []

    for x in conversation:
        if x.group_id not in list:
            object_list.append(x)
        list.append(x.group_id)

    listt = []
    user_list = []
    for use in object_list:
        key = use.receiver_id
        if key == current_user.id:
            key = use.sender_id
            keyy = User.objects.get(id=key)
            if use.sender_id not in listt:
                user_list.append(keyy)
            listt.append(use.receiver_id)
        else:
            keyy = User.objects.get(id=key)
            if use.receiver_id not in listt:
                user_list.append(keyy)
            listt.append(use.receiver_id)


    info = Message.objects.filter(sender_id=current_user, post_key=post_id,
                                receiver_id=receiver) | Message.objects.filter(sender_id=receiver,
                                receiver_id=current_user, post_key=post_id).order_by('id').reverse()[1:10]

   # last_ten = Messages.objects.filter(since=since).order_by('-id')[:10][::-1]
    if request.session.has_key('token'):
        context = {
            'receiver_name': user_name,

            'condition': condition,
            'chat_user': chat_user,
            'chat_ads': chat_ads,
            'test':info,
            'current_user': current_user,
            'conversation': object_list,
            'first_chat': 'second',
             'user_list':user_list,

            # 'ss':json_string

        }


    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=current_user.id, receiver_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        #return JsonResponse(serializer.data, safe=False)
        return render(request, 'commerece/chat.html', context)
    elif request.method == 'POST':

       # data = JSONParser().parse(request)
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            info = Message.objects.filter(sender_id=current_user, post_key=post_id,
                                          receiver_id=receiver) | Message.objects.filter(sender_id=receiver,
                                                                                          receiver_id=current_user,
                                                                                          post_key=post_id).order_by('id').reverse()[1:10]
            context = {

                'condition': condition,
                'chat_user': chat_user,
                'chat_ads': chat_ads,
                'test': info,
                'receiver_name': user_name,
                'current_user': current_user,
                'conversation':object_list,
                'first_chat': 'second',
                'user_list':user_list,
            }
            return render(request, 'commerece/chat.html',context)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return render(request, 'commerece/chat.html', context)

@api_view(['GET','POST'])
def check_out(request,id=None):
    template_name = 'transaction/checkout.html'
    check=False
    if request.session.has_key('token'):
        #return redirect('order/')
        context = {
            'check': check,
        }

        return render(request, 'transaction/checkout.html',context)

    else:
        return redirect('login')
@api_view(['GET','POST'])
def search(request,id=None):
    current_user = request.user





    check = True

    seller_ad=Khan.objects.all()
    seller_adss=seller_ad.exclude(user_key_id=current_user.id)
    seller_ads=seller_adss.exclude(customer='buyer')


    buyer_order =seller_adss.exclude(customer='seller')
    #if not request.user.is_authenticated():
    context = {
        'check': check,
        'seller_ads': seller_ads,
        'buyer_order': buyer_order, }


    if request.session.has_key('token'):
        if request.method == "POST":
            catagoryy = request.POST['catagory']
            product_name = request.POST['product_name']
            city = request.POST['city']
            seller_adss = Khan.objects.all().exclude(user_key_id=current_user.id)
            sellerr=seller_adss.filter(customer='seller')
            seller_ads=sellerr.filter(catagory=catagoryy,product_name=product_name,city=city)[:10]
            buyer_orderrr = Khan.objects.all().exclude(user_key_id=current_user.id)
            buyerr = buyer_orderrr.filter(customer='buyer')

            buyer_order = buyerr.filter(catagory=catagoryy,product_name=product_name,city=city)[:10]

            context = {
            'check': check,
            'seller_ads': seller_ads,
            'buyer_order': buyer_order, }

            return render(request, "commerece/home.html", context)
        return render(request, "commerece/home.html", context)

    else:
         return redirect('login')



@api_view(['GET','POST'])
def delete_Ads(request,id=None,user_type=None):
    if request.session.has_key('token'):
        if request.method == "GET":
            obj_delete=Khan.objects.filter(id=id)
            obj_delete.delete()
            if user_type == 'seller':
                return redirect('/myads')
            else:
                return redirect('/myorder')


    return redirect('login')





