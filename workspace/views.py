from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from pprint import pprint
from news.models import News
from workspace.forms import NewsForm, NewsModelForm ,LoginForm,RegisterForm,ChangeProfileForm,ChangePsswordForm
from pprint import pprint
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required(login_url='/workspace/login/')
def workspace(request):
    news = News.objects.all()
    page = int(request.GET.get('page', 1))  
    page_size = int(request.GET.get('page_size', 4))
 
    pagin = Paginator(news, page_size)
    news = pagin.get_page(page) 

    return render(request, 'workspace/index.html', {'news': news})

def create_news(request):
    form = NewsModelForm()

    if request.method == 'POST':
        form = NewsModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            # messages.success(request, f'The prad "{news.name}" has been successfully added!')
            return redirect('/workspace/')
         
    return render(request, 'workspace/create_news.html', {'form': form})

@login_required(login_url='/workspace/login/')
def delete_news(request, id):
    news = get_object_or_404(News, id=id)
    news.delete()
    return redirect('/workspace/')
@login_required(login_url='/workspace/login/')

def ubdate_news(request, id):
    news = get_object_or_404(News, id=id)
    form = NewsModelForm(instance=news)

    if request.method == 'POST':
        form = NewsModelForm(data=request.POST, files=request.FILES, instance=news)
        if form.is_valid():
            form.save()  
            messages.success(request, f'The product "{news.name}" has been successfully updated!')
            return redirect('/workspace/')

    return render(request, 'workspace/ubdate_news.html', {
        'news': news,
        'form': form,
    })
    
def logout_profile(request):
    if request.user.is_authenticated:
        logout(request)
    
    messages.success(request, f'Good bye!')
    return redirect('/') 


def login_profile(request):
    if request.user.is_authenticated:
        return redirect("/workspace/")

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Welcome "{user.get_full_name()}"')
                return redirect("/workspace/")

            message = "The user does not exist or the password is incorrect."
            return render(
                request, "auth/login.html", {"form": form, "message": message}
            )

    return render(request, "auth/login.html", {"form": form})

def register(request):
    if request.user.is_authenticated:
        return redirect('/workspace/')
    
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome "{user.get_full_name()}"')
            return redirect('/workspace/')
        
        messages.error(request, f'Fix some errors below!')
    return render(request, 'auth/register.html', {'form': form})


@login_required(login_url='/workspace/login/')
def profile(request):

    form = ChangeProfileForm(instance=request.user)

    if request.method == 'POST':
        form = ChangeProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully changed profile')
            return redirect('/workspace/')

    return render(request, 'auth/profile.html', {'form': form})


@login_required(login_url='/workspace/login/')
def change_password(request):

    form = ChangePsswordForm(user=request.user)

    if request.method == 'POST':

        form = ChangePsswordForm(user=request.user, data=request.POST)

        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            
            user = request.user
            user.set_password(new_password)
            user.save()

            login(request, user)

            messages.success(request, f'Successfully changed password')
            return redirect('/workspace/')

    return render(request, 'auth/change_password.html', {'form': form})