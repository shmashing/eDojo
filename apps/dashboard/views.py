from django.shortcuts import render, reverse, redirect
from ..users.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if(not check_user_authentication(request)):
      return redirect('users:home')

    context = {
      'user': User.objects.get(id=request.session['user_id'])
    }

    return render(request, "dashboard/index.html", context)


def check_user_authentication(request):
    try:
      if(request.session['user_logged']):
        user_id = request.session['user_id']
        return True
      else:
        return False
    except:
      return False

