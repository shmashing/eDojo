from __future__ import unicode_literals
from django.db import models
from ..users.models import User
from ..dashboard.models import Review
# Create your models here.

class StoreManager(models.Manager):
    def create_store(self, data, user_id, default):
        errors = {}
        if not data['name']:
            errors['name'] = 'A store must have a name so the user can find you'
        if self.filter(name=data['name']):
            errors['name_exist'] = 'Your store name must be unique'
        if not data['description']:
            errors['description'] = 'Description field must not be empty'
        if len(errors):
            return errors
        else:
            user = User.objects.get(id=user_id)
            if not self.filter(user=user):
                User.objects.filter(id=user_id).update(status=True)
            if data['logo']:
                return self.create(name=data['name'], description=data['description'], logo=data['logo'], rating=0,
                                    user=user)
            else:
                return self.create(name=data['name'], description=data['description'], logo=default, rating=0,
                                    user=user)

    def edit_store(self, data, store_id):
        errors = {} #YOU NEED TO MAKE THE VALUE OF INPUT THE STORE OBJ FIELD SO ITS NEVER EMPTY
        if not data['name']:
            errors['name'] = 'A store must have a name so the user can find you'
        if self.exclude(id=store_id).filter(name=data['name']):
            errors['name_exist'] = 'Your store name must be unique'
        if not data['description']:
            errors['description'] = 'Description field must not be empty'
        if len(errors):
            return errors
        else:
            if data['logo']:
                return self.filter(id=store_id).update(name=data['name'], description=data['description'], logo=data['logo'], rating=0,
                                    user=user)
            else:
                return self.filter(id=store_id).update(name=data['name'], description=data['description'], logo=default, rating=0,
                                    user=user)


class ProductManager(models.Manager):
    def create_product(self, data, store_id):
        errors = {}
        if not data['name']:
            errors['name'] = 'Product must have a name'
        if not data['price']:
            errors['price'] = 'Product must have a price'
        if not data['description']:
            errors['description'] = 'Product must have a description'
        if not data['image']:
            errors['image'] = 'Product must have an image'
        if len(errors):
            return errors
        else:
            store = Store.objects.get(id=store_id)
            return self.create(name=data['name'], price=data['price'], description=data['description'],
                            image=data['image'], store=store)

    def edit_product(self, product_id):
        errors = {}
        if not data['name']:
            errors['name'] = 'Product must have a name'
        if not data['price']:
            errors['price'] = 'Product must have a price'
        if not data['description']:
            errors['description'] = 'Product must have a description'
        if not data['image']:
            errors['image'] = 'Product must have an image'
        if len(errors): #YOU NEED TO MAKE THE VALUE OF INPUT THE PRODUCT OBJ FIELD SO ITS NEVER EMPTY
            return errors
        else:
            return self.filter(id=product_id).update(name=data['name'], price=data['price'], description=data['description'],
                            image=data['image'], store=store)

class ProductCategoryManager(models.Manager):
    def create_cat_pro(self, product, data):
        for val in data['catagories']:
            if Category.objects.filter(name=val):
                category = Category.objects.get(name=val)
                self.create(product=product, category=category)
            else:
                category = Category.objects.create(name=val)
                self.create(product=product, category=category)


class Store(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=1000)
    logo = models.TextField(max_length=1000, default='')
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name='stores')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = StoreManager()
    def avg_rating(self):
        total_products = self.products.all()
        total_ratings = Review.objects.filter(product__in=total_products)
        total = 0
        for value in total_ratings.rating.all():
            total += value
        avg = total / total_ratings.rating.count()
        return avg  #SEE VIEWS

class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.CharField(max_length=25)
    description = models.TextField(max_length=1000)
    image = models.TextField(max_length=1000)
    store = models.ForeignKey(Store, related_name='products')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = ProductManager()

class Category(models.Model):
    name = models.CharField(max_length=25)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Product_Category(models.Model):
    product = models.ForeignKey(Product, related_name='categories')
    category = models.ForeignKey(Category, related_name='products')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = ProductCategoryManager()
