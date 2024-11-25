from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LinkForm

# Create your views here.

@login_required
def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)

        if form.is_valid():
            link =form.save()

            return redirect('/')
