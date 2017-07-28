from __future__ import unicode_literals
from django.db import models
from ..users.models import User
from ..store.models import Product, Store
# Create your models here.

class CartManager(models.Manager):
    def add_to_cart(self, user_id, product_id):
        user = User.objects.get(id=user_id)
        product = Product.objects.get(id=product_id)
        if self.filter(user=user, product=product):
            return False
        else:
            self.create(user=user, product=product)
    

class ReviewManager(models.Manager):
    def create_review(self, data, user_id, product_id):
        errors = {}
        if not data['review']:
            errors['review'] = 'Enter a review'
        if not data['rating']:
            errors['rating'] = 'Select a rating'
        if len(errors):
            return errors
        else:
            user = User.objects.get(id=user_id)
            product = Product.objects.get(id=product_id)
            if self.filter(user=user, product=product):
                return False
            else:
                self.create(review=data['review'], rating=int(data['rating']), user=user, product=product)

class FollowingManager(models.Manager):
    def add_following(self, user_id, store_id):
        user = User.objects.get(id=user_id)
        store = Store.objects.get(id=store_id)
        if self.filter(user=user, store=store):
            return False
        else:
            self.create(user=user, store=store)



class Cart(models.Model):
    user = models.ForeignKey(User, related_name='products')
    product = models.ForeignKey(Product, related_name='users')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = CartManager()

class Review(models.Model):
    review = models.CharField(max_length=25)
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name='product_reviews')
    product = models.ForeignKey(Product, related_name='user_reviews')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = ReviewManager()

class Following(models.Model):
    user = models.ForeignKey(User, related_name='stores_following')
    store = models.ForeignKey(Store, related_name='users_following')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = FollowingManager()
