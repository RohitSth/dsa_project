from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login') # This decorator ensures that the user is logged in
def home(request):
    return render(request, 'sort/home.html')

