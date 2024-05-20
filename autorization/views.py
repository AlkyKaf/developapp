from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import View

from autorization.forms import UserCreationForms


class RegisterView(View):
    template_name = 'autorization/register.html'

    def get(self, request):
        content = {
            'form': UserCreationForms(),
        }
        return render(request, self.template_name, content)

    def post(self, request):
        form = UserCreationForms(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # email = form.cleaned_data.get('email')#, email=email
            # user = authenticate(username=username, password1=password)
            # login(request, user)
            return redirect(to='login')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
