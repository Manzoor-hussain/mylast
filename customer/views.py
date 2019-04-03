from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer

from customer.serializers import UserSerializer,CommonSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from order.models import Seller
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from django.urls import reverse
class IndexVieww(generic.ListView):
    template_name = 'customer/seller.html'
    context_object_name = 'all_albums'
    renderer_classes = [TemplateHTMLRenderer]



    def order(self,request,id):
        if  request.session.has_key('id'):
            user = User.objects.get(request.id)
            profile=user.profile.image
            return render('order/base.html')
        else:
            return redirect(reverse('login'))
    #
    # import pdb
    # pdb.set_trace()
    def get_queryset(self):
     return User.objects.all()

class SellerPost(APIView):
    template_name = 'customer/seller.html'
    context_object_name = 'all_albums'
    renderer_classes = [TemplateHTMLRenderer]

    @api_view(['GET', 'POST'])
    def list_seller(request):

        if request.method == 'POST':
            serializer = CommonSerializer(data=request.data)


            if serializer.is_valid():
                serializer.save()
                return redirect('myads/')
            #  return render(request, 'commerece/MyAds.html', {'ads': seller},status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuyerPost(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    @api_view(['GET', 'POST'])
    def list_order(request):

        if request.method == 'POST':
            serializer = CommonSerializer(data=request.data)

            if serializer.is_valid():
                seller = serializer.save()
                return redirect('myorder/')
                return render(request, 'commerece/Myorder.html', {'ads': seller}, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def logout(request):
    try:
        del request.session['id']

    except:
        pass
    return redirect(reverse('login'))


from django.shortcuts import render

# Create your views here.
