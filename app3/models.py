from django.db import models


# Create your models here.
class user_register(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phn_no=models.IntegerField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    image=models.ImageField()


class artworker(models.Model):
    name=models.CharField(max_length=20)
    phn_no=models.IntegerField()
    address=models.TextField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    image=models.ImageField()
    id_proof=models.ImageField()

class craftworker(models.Model):
    name=models.CharField(max_length=20)
    phn_no=models.IntegerField()
    address=models.TextField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    image=models.ImageField()
    id_proof=models.ImageField()

class artproduct(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField(max_length=30)
    category=models.CharField(max_length=20)
    artistname=models.CharField(max_length=20)
    image=models.ImageField()
    created_date=models.DateField()
    size=models. IntegerField()
    price=models.IntegerField()
    quantity=models.IntegerField()

class craftproduct(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField(max_length=20)
    category=models.CharField(max_length=20)
    artistname=models.CharField(max_length=20)
    image=models.ImageField()
    created_date=models.DateField()
    size=models.IntegerField()
    price=models.IntegerField()
    quantity=models.IntegerField()

class cart(models.Model):
    user_details=models.ForeignKey(user_register,on_delete=models.CASCADE)
    art_product=models.ForeignKey(artproduct,on_delete=models.CASCADE,null=True,blank=True)
    craft_product=models.ForeignKey(craftproduct,on_delete=models.CASCADE,null=True,blank=True)
    total_quantity=models.IntegerField(default=1)
    total_price=models.IntegerField(default=0)

class wishlist(models.Model):
    user_details=models.ForeignKey(user_register,on_delete=models.CASCADE)
    art_product=models.ForeignKey(artproduct,on_delete=models.CASCADE,null=True,blank=True)
    craft_product=models.ForeignKey(craftproduct, on_delete=models.CASCADE, null=True, blank=True)
    product_name=models.CharField(max_length=15)
    product_quantity=models.IntegerField(default=1)
    product_price=models.IntegerField(default=0)
    product_image=models.ImageField()

class Order(models.Model):
    STATUS_CHOICES=[
    ('on the way','On the way'),
    ('delivered','Delivered'),
    ('cancelled','Cancelled'),
    ('returned','Returned')
    ]
    user = models.ForeignKey(user_register, on_delete=models.CASCADE)
    address = models.TextField()
    total_amount = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='on the way')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

class orderitem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    art_product=models.ForeignKey(artproduct, on_delete=models.CASCADE,null=True,blank=True)
    craft_product=models.ForeignKey(craftproduct, on_delete=models.CASCADE, null=True, blank=True)
    quantity=models.IntegerField()
    price=models.FloatField()

class PasswordReset(models.Model):
    user=models.ForeignKey(user_register,on_delete=models.CASCADE)
    token=models.CharField(max_length=4)



class Feedback(models.Model):
    user = models.ForeignKey(user_register,on_delete=models.CASCADE)
    message = models.TextField()
    reply = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f"Feedback from {self.user.username}"




