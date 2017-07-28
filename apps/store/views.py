from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "store/index.html")

# def average_rating():
#     for store in Store.objects.all():
#         store.avg_rating()
#
# average_rating()
