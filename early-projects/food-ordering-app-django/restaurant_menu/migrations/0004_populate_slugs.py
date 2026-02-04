from django.db import migrations
from django.utils.text import slugify

def populate_slugs(apps, schema_editor):
    Item = apps.get_model('restaurant_menu', 'Item')
    for item in Item.objects.all():
        if not item.slug:
            base_slug = slugify(item.meal)
            slug = base_slug
            counter = 1
            while Item.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            item.slug = slug
            item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_menu', '0002_item_slug'),  # adjust if your last migration is different
    ]

    operations = [
        migrations.RunPython(populate_slugs),
    ]
