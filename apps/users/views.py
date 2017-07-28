from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import *
# Create your views here.


def index(request):
    try:
      if(request.session['user_logged']):
        return redirect(reverse('books:home', kwargs={'id':request.session['user_id']}))

    except:
      pass

    request.session['user_logged'] = False
    request.session['user_id'] = None
    return render(request, "users/index.html")

def log_in(request):
    user_valid = User.objects.login(dict(request.POST.items()))
    if(user_valid[0]):
      request.session['user_logged'] = True
      request.session['user_id'] = user_valid[1].id
      return redirect('dash:home')
    else:
      messages.add_message(request, messages.INFO, user_valid[1])
      return redirect('users:home')
    

def register(request):
    return render(request, "users/register.html")

def add_user(request):
    user_valid = User.objects.register(dict(request.POST.items()))
    if(user_valid['valid']):
      messages.add_message(request, messages.INFO, 'Thanks for registering!', extra_tags='registered')
      return redirect('users:home')

    else:
      for message in user_valid['errors']:
        messages.add_message(request, messages.INFO, message)
      return redirect('users:register')

def edit_user(request):
    if(not check_user_authentication(request)):
      return redirect('users:home')

    context = {
      'user': User.objects.get(id=request.session['user_id'])
    }    


    return render(request, 'users/edit_account.html', context)

def logout(request):

    request.session.flush()
    return render(request, 'users/logout.html')

def check_user_authentication(request):
    try:
      if(request.session['user_logged']):
        user_id = request.session['user_id']
        return True
      else:
        return False
    except:
      return False

