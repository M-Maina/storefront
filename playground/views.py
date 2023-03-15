from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Customer
from django.db.models import Q, F

# Create your views here.


def index(request):
    #customer = Customer.objects.filter(Customer.email)
    
    #To obtain greater than in queries eg price__gt=20, price__lt=20, price__eq=20
    
    #product = Customer.objects.filter(pk=0).first() #This returns None
    #exists = Customer.objects.filter(pk=0).exists()
    # #query_set = Product.objects.all() #gets all the objects from a given table 
    # try:
    #     product = Customer.objects.get(pk=0) # django refers to that object/item alone
    # except ObjectDoesNotExist:
    #     pass
    
    #product = Customer.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    
    #product = Customer.objects.filter(first_name=F('email'))
    
    #product = Customer.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    
    
    
    #customer = Customer.objects.order_by('email')
    
    #customer = Customer.objects.earliest('phone')
    
    #queryset = Customer.objects.all()[:25]
    
    #queryset = Customer.objects.values('id', 'first_name')[:25]
    
    #queryset = Customer.objects.only('id', 'last_name')[:25]
    
    #queryset =Product.objects.select_related('promotions').select_related('collection').all()
    #{{ product.collection.title }}
    
    #queryset = Customer.objects.prefetch_related('collection').all()
    
    #queryset = Customer.objects.select_related('collection__someOtherField').all()
    
    #queryset = Order.objects.select_related('Customer').order_by('-placed_at')[:5]
    
    #{{ order.id }}  - {{ order.customer.first_name }}
    
    
    # for product in query_set:
    #     print(product)
    return render(request, 'playground/hello.htm', {'customers': queryset })