from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import  User
# Create your views here.


class IndexClass(View):
    def get(self, request):
        return HttpResponse('<h1>Xin Chào</h1>')
       # return render(request,login_name=Login)



class LoginClass(View):
    def get(self, request):
        return render(request, template_name='Login/Login.html')


class register(View):
    def get(self, requesr):
        return render(requesr, template_name="Login/register.html")

class forgotpass(View):
    def get(self, requesr):
        return render(requesr, template_name="Login/forgotpass.html")

    def post(self, request):
        user_name = request.POST.get('Ten dang nhap')
        matkhau = request.POST.get('password')
        my_user = authenticate(username=user_name, password=matkhau)
        if my_user is None:
            return HttpResponse('User không tồn tại')
        login(request, my_user)
        return render(request, 'Login/thanhcong.html')



