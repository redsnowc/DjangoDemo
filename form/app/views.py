from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

from .forms import RegisterForm, AuthModelFrom

# Create your views here.


class Register(View):
    TEMPLATE = 'register.html'

    def get(self, request):
        form = AuthModelFrom()
        # form = RegisterForm()
        return render(request, self.TEMPLATE, {'form': form})

    def post(self, request):
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        #
        # print(request.POST)
        # print(username)
        # print(password)
        form = AuthModelFrom(request.POST)
        # form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            print(password)

            # 保存
            form.save()
        else:
            return render(request, self.TEMPLATE, {"form": form})

        return redirect(reverse('register'))


