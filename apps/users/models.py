from __future__ import unicode_literals
from django.db import models
import bcrypt, re
EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# Create your models here.
class UserManager(models.Manager):
    def create_user(self, data):
        errors = {}
        if not data['first_name'] or len(data['first_name']) < 2 or not data['last_name'] or len(data['last_name']) < 2:
            errors['name'] = 'Invalid Name'
        if not data['email'] or not EMAIL_REGEX.match(data['email']):
            errors['email'] = 'Invalid Email'
        if self.filter(email=data['email']):
            errors['email_exist'] = 'Email exist already'
        if not data['password'] or len(data['password']) < 4:
            errors['password'] = 'Invalid password'
        if data['password'] != data['confirm_password']:
            errors['confirm_password'] = 'password doesnt match'
        if len(errors):
            return errors
        else:
            hash_password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            return self.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=hash_password)

    def validate_user(self, data):
        errors = {}
        if self.filter(email=data['email']):
            user = self.get(email=data['email'])
            hash_password = bcrypt.hashpw(data['password'].encode(), user.password.encode())
            if hash_password == user.password:
                return user
            else:
                errors['password'] = 'Invalid password'
        else:
            errors['email'] = 'Invalid email'
        return errors

   



class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    picture = models.TextField(max_length=1000, default='')
    status = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = UserManager()
