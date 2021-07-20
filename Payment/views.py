from project.settings import CURRENCY, STRIPE_PUBLIC_KEY
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
import stripe
from clothpayment.views import *
from clothpayment.models import *

# Create your views here.

class PaymentView(TemplateView):    
     template_name = 'payment.html'
     def get_context_data(self,**kwargs):        
        context = super().get_context_data(**kwargs)        
        context['key'] = settings.STRIPE_PUBLIC_KEY    
        return context

stripe.api_key = settings.STRIPE_SECRET_KEY

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = 500,
            currency = 'INR',
            description = 'Jeans Payment',
            source = request.POST['stripeToken']
        )
    return render(request, 'paymentSuccess.html')

