from __future__ import unicode_literals
<<<<<<< HEAD
import bcrypt
import re
=======
>>>>>>> b6d8c9cf9043437fa47ffa391d84e5afc3b6fe21
from django.db import models
import bcrypt, re
EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z0-9.,-]*$')
# Create your models here.
class UserManager(models.Manager):
<<<<<<< HEAD
  def login(self, postData):
    username = postData['username']
    password = postData['password']
  
    try:
      user = User.objects.get(username=username.lower())
      new_hash = bcrypt.hashpw(password.encode(), user.password.encode())

      if(new_hash == user.password):
        return [True, user]

      else:
        return [False, "Password doens't match username"]
     
    except:
      return [False, "Incorrect Username/Password"]

  def register(self, postData):
    user_valid = {'valid':True, 'errors':['','',' ',' ',''], 'user':None}

    try:
      User.objects.get(username=postData['username'].lower())
      user_valid['valid']=False
      user_valid['errors'][2] = 'Username Taken'

    except:
      pass
    
    try:
      User.objects.get(email=postData['email'].lower())
      user_valid['valid']=False
      user_valid['errors'][3] = 'Email Taken'
    
    except:
      pass

    email = str(postData['email'].lower())
    if(not EMAIL_REGEX.match(email)):
      user_valid['valid']=False
      user_valid['errors'][3] = 'Please enter a valid email'


    first_name = postData['first_name']
    if(len(first_name) < 3) or (not NAME_REGEX.match(first_name)):
      user_valid['valid']=False
      user_valid['errors'][0] = 'Please enter a valid first name'


    last_name = postData['last_name']
    if(len(last_name) < 2) or (not NAME_REGEX.match(last_name)):
      user_valid['valid']=False
      user_valid['errors'][1] = 'Please enter a valid last name'

    username = postData['username'].lower()
    if(str(username) == '') or (not NAME_REGEX.match(first_name)):
      user_valid['valid']=False
      user_valid['errors'][2] = 'Please enter a username'

    clearPassNoHash = postData['password']
    if(len(clearPassNoHash)<8):
      user_valid['valid']=False
      user_valid['errors'][4] = 'Password must be 8 characters or more'
   
    if(user_valid['valid']):
      clearPassNoHash = clearPassNoHash.encode()
      hashPass = bcrypt.hashpw(clearPassNoHash, bcrypt.gensalt())
      user = User.objects.create(first_name=str(first_name), 
                                 last_name=str(last_name), 
                                 username=username, 
                                 email=str(email).lower(), 
                                 password=hashPass
      )

      user.save()
      user_valid['user'] = user

    for error in user_valid['errors']:
      print(error)

    return user_valid

class User(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  username = models.CharField(max_length=45)
  email = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  objects = UserManager()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)



=======
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
>>>>>>> b6d8c9cf9043437fa47ffa391d84e5afc3b6fe21
