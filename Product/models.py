from django.db import models
from shop.settings import AUTH_USER_MODEL

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    date_created = models.DateTimeField(auto_created=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name
    
    
    
    

class Cart(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.cart)
     
    
    def validate_product(self, request):
        cart = CartItem.objects.filter(cart=request.data).acount()
        return cart
        
