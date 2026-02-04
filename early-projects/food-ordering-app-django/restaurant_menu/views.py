from django.views.generic import ListView, DetailView
from .models import Item

CATEGORY_EMOJIS = {
    "starters": "🥟",
    "salads": "🥗",
    "main_dishes": "🍽️",
    "deserts": "🍰"
}


class MenuList(ListView):
    model = Item
    template_name = "restaurant_menu/menu_list.html"
    context_object_name = "menu_items"
    queryset = Item.objects.filter(status=1).order_by('category', 'meal')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add emoji to each menu item
        for item in context['menu_items']:
            item.emoji = CATEGORY_EMOJIS.get(item.category, "🍽️")
        return context


class MenuItemDetail(DetailView):
    model = Item
    template_name = "restaurant_menu/menu_item_details.html"
    context_object_name = "item"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = context['item']
        item.emoji = CATEGORY_EMOJIS.get(item.category, "🍽️")
        return context
