from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices, bedroom_choices, state_choices

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
    'listings': paged_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request, listing_id):
   listing = get_object_or_404(Listing, pk=listing_id)

   context = {
      'listing': listing
   }

   return render(request,'listings/listing.html',context)

def search(request):
   queryset_list = Listing.objects.order_by('-list_date')

   # Search từ khóa
   if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords:
         # Kiếm từ khóa trong phần description
         queryset_list = queryset_list.filter(description__icontains=keywords)

   # Search thành phố
   if 'city' in request.GET:
      city = request.GET['city']
      if city:
         # Kiếm thành phố trong phần vị trí 
         queryset_list = queryset_list.filter(city__iexact=city)
   
   # Search tiểu bang
   if 'state' in request.GET:
      state = request.GET['state']
      if state:
         # Kiếm tiểu bang trong phần vị trí 
         queryset_list = queryset_list.filter(state__iexact=state)

   # Search phòng ngủ
   if 'bedrooms' in request.GET:
      bedrooms = request.GET['bedrooms']
      if bedrooms:
         # Số phòng ngủ lên đến
         queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

   # Search giá
   if 'price' in request.GET:
      price = request.GET['price']
      if price:
         # Giá lên đến
         queryset_list = queryset_list.filter(price__lte=price)

   context = {
      'state_choices': state_choices,
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices,
      'listings': queryset_list,
      'values':request.GET
   }

   return render(request,'listings/search.html', context)