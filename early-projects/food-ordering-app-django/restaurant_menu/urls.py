from django.urls import path
from .views import MenuList, MenuItemDetail

urlpatterns = [
    path('', MenuList.as_view(), name='home'),  # 🏠 Home / Menu List
    path('menu_item/<slug:slug>/', MenuItemDetail.as_view(), name='menu_item_details'),  # 🍽️ Item Detail
]
