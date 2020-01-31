from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.contrib import messages
import re
import datetime
from django.urls import reverse_lazy, reverse
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError


def index(request):
    if request.method == 'GET':
        form = EncryptDataForm()

    if request.method == 'POST':
        form = EncryptDataForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            encrypted = form.cleaned_data.get("encrypted")
            try:
                if EncryptData.objects.filter(encrypted=encrypted).count() > 0:
                    messages.success(request, 'This content already exist, Please try again')
                else:
                    instance.encrypted = encrypted
                    instance.pub_date = datetime.datetime.now()
                    instance.save()
                messages.success(request, 'Success !!, Thanks for Submiting')
            except IntegrityError:
                messages.success(request, 'This content already exist, Please try again')
            return redirect(reverse('index'))
    context = {
        "form": form,
    }
    return render(request, 'index.html', context)


def list_data(request):
    list1 = EncryptData.objects.all().order_by('-id')
    context = {
        "list1": list1,
    }
    return render(request, 'encrypted.html', context)


def original_data(request):
    list1 = EncryptData.objects.all().order_by('-id')
    context = {
        "list1": list1,
    }
    return render(request, 'decrypted.html', context)


