from django.urls import path
from .views import (
    home,
    flower_api_view,
    product_api_view,
    basket_api_view,
    entourage_api_view,
    branch_api_view,
    package_api_view,
    houseplant_api_view,
    order_api_view,
    gift_api_view,
    send_email_views
)

app_name = "products"

urlpatterns = [
    path("", home),
    path(
        "flowers/", 
        flower_api_view,
        name="flowers"
    ),
    path("products/", 
         product_api_view,
         name="products"
    ),
    path("baskets/", 
         basket_api_view,
         name="baskets"
    ),
    path("entourages/", 
         entourage_api_view,
         name="entourages"
    ),
    path("branches/", 
         branch_api_view,
         name="braches"
    ),
    path("packages/", 
         package_api_view,
         name="packages"
    ),
    path("houseplants/", 
         houseplant_api_view,
         name="houseplants"
    ),
    path("orders/", 
         order_api_view,
         name="orders"
    ),
    path("gifts/", 
         gift_api_view,
         name="gifts"
    ),
    path("index/",
         send_email_views,
         name="index"
         )
]


