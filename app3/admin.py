from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(user_register)
admin.site.register(artworker)
admin.site.register(craftworker)
admin.site.register(artproduct)
admin.site.register(craftproduct)
admin.site.register(cart)
admin.site.register(wishlist)
admin.site.register(orderitem)
admin.site.register(Order)
admin.site.register(PasswordReset)
admin.site.register(Feedback)
