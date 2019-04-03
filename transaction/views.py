from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer

from order.serializers import UserSerializer,SellerSerializer,BuyerSerializer
from  rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from  order.models import Seller
from rest_framework.response import Response
from  rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from  django.urls import reverse

@api_view(['GET','POST'])
def payment(request,id=None):
    template_name = 'transaction/payment.html'
    check=False
    if request.session.has_key('token'):
        #return redirect('order/')
        context = {
            'check': check,
        }

        return render(request, 'transaction/payment.html',context)

    else:
        return redirect('login')

