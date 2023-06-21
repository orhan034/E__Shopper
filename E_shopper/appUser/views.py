from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from appMy.views import sepetSay
# Create your views here.

def loginUser(request):
    context = {'title':'Giriş Yap'}
    if request.method == 'POST':
        if request.POST.get('submit')=="Giriş Yap":
            username = request.POST.get('username')
            password = request.POST.get('password')
            harfet = False
            for harf in username:
                if harf == '@':
                    harfet = True
            if username[-4:] == '.com' and harfet:
                try:
                    user = User.objects.get(email = username)
                    username = user.username
                except:
                    messages.success(request, 'Email bulunamadı!')
                    return redirect('loginUser')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.success(request, 'Kullanıcı adı veya şifre hatalı!')

    if request.POST.get('submit')=='Kayit Ol':
        if request.method == 'POST':
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            harfup = False
            harfnum = False
            if password1==password2:
                for harf in password1:
                    if harf.isupper():
                        harfup = True
                    if harf.isnumeric():
                        harfnum = True
                if harfup and harfnum and len(password1)>=6:
                    if not User.objects.filter(username=username):
                        if not User.objects.filter(email=email):
                            user = User.objects.create_user(first_name = name,
                                                            last_name = surname, email=email,
                                                            username=username, password=password1)
                            user.save()
                            userprofil = UserInfo(user=user)
                            userprofil.save()
                            context.update({'basari':'Kayıt işlemi başarılı!!'})
                            # return redirect('loginUser')
                        else:
                            messages.warning(request, 'Bu email zaten kullanılıyor!')
                            return redirect('loginUser')          
                    else:
                        messages.warning(request, 'Bu kullanıcı adı zaten kullanılıyor!')
                        return redirect('loginUser')          
                else:
                    messages.warning(request, 'Şifre en az bir büyük harf içermeli!')
                    messages.warning(request, 'Şifre rakam içermeli!')
                    messages.warning(request, 'Şifre en az 6 karakter içermelidir!')
                    return redirect('loginUser')     
            else:
                messages.warning(request, 'Şifreler aynı değil!')    
                return redirect('loginUser') 
    return render(request, 'user/login.html', context)

def profil(request):
    user = User.objects.get(username = request.user)
    profils = UserInfo.objects.get(user = user)
    
    if request.method == 'POST':
        if request.POST['formbutton'] == 'profilChange':
            job = request.POST.get('job')
            deneyim = request.POST.get('deneyim')
            email = request.POST.get('email') 
            website = request.POST.get('website') 
            tel = request.POST.get('tel') 
            address = request.POST.get('address') 
            profils.job = job
            if deneyim is None:
               profils.deneyim = deneyim
            user.email = email
            profils.web_site = website
            profils.phone = tel
            profils.address = address
            profils.save()
            user.save()
            return redirect('profil')

        if request.POST['formbutton'] == 'imageChange':
            image = request.FILES.get('image')
            profils.image = image
            profils.save()
            return redirect('profil')
        
        if request.POST['formbutton'] == 'sifreChange':
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            password3 = request.POST['password3']
            user = User.objects.get(username = request.user)
            if user.check_password(password1):
                if password2==password3:
                    user.set_password(password3)
                    user.save()
                
                return redirect('loginUser')
    context = {
        'title':"Profil",
        "user":user,
        'profils':profils,
        "shopbasket": sepetSay(request)
    }
    return render(request, "user/profil.html", context)

def logoutUser(request):
    logout(request)
    return redirect('index')