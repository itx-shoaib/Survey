from django.shortcuts import render
from form.models import Feedback
# Create your views here.
def home(request):
    return render(request,'form.html')

def feedback(request):
    if request.method == 'POST':
        experience = request.POST.get('experience')
        offer = request.POST.get('offer')
        price = request.POST.get('price')
        delivery = request.POST.get('delivery')
        support = request.POST.get('support')
        recommend = request.POST.get('recommend')
        change = request.POST.get('change')
        email = request.POST.get('email')
        survey = Feedback(experience=experience , offer=offer , price=price , delivery=delivery , support=support , recommend=recommend , change=change , email=email)
        survey.save()
    return render(request,'form.html')