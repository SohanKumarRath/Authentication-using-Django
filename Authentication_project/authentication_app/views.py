from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
# Create your views here.
def signupView(req):
    if req.method=='POST':
        form=SignupForm(req.POST)
        if form.is_valid():
            form.save()
    else:
        form=SignupForm()
    return render(req,'signupform.html',{'form':form})
