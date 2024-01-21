from django.shortcuts import render , redirect
from .models import Activities, UserHobby
from django.views.generic import DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .forms import userForm
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def Activities_view(request):
    activities = Activities.objects.all()
    context = {
        "activities" : activities,
        
    }

    return render(request, "templates/MainPage.html", context)

class activity_detail(DetailView):
    model = Activities
    template_name = "templates/activity_detail.html"
    context_object_name = "activity"

@method_decorator(login_required(login_url='login'), name='dispatch')
class HobbyView(LoginRequiredMixin,CreateView):
    model = UserHobby
    form_class = userForm                              
    template_name = "templates/formularz_page.html"
    success_url = "succes"





def ForumView(request):
        model = UserHobby.objects.all()
        context = {
        'model': model
        }
    
        return render(request, 'templates/forum_page.html', context)

class SuccesView(TemplateView):
     template_name = "templates/success.html"


class UpdatePost(UpdateView):
    model = UserHobby
    template_name = "templates/update_hobby.html"
    fields = "__all__"
    success_url = reverse_lazy('forum')

class PostDelete(DeleteView):
    model = UserHobby
    template_name = 'templates/delete_hobby.html'  
    success_url = reverse_lazy('forum')



def user_posts(request):

    posts = UserHobby.objects.filter(author=request.user)
    all_posts = UserHobby.objects.all

    return render(request, "templates/user_posts.html", context={'posts':posts,
                                                                 'all_posts': all_posts})
        



def registration(request):
    form = RegisterForm()
    if request.method =='POST':                               #REJESTRACJA
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f"User {user} created")
            return redirect("login")

        
    context = {'form': form}
    return render(request, 'templates/register_page.html', context)


def sign_in(request):
    if request.method == "POST":
        form = LoginForm(request , data=request.POST)                   #LOGOWANIE
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
            return redirect("main")
    else:
        form = LoginForm()
    
    return render(request, "templates/login_page.html", {
        'form': form,})

def logoutuser(request):
    logout(request)                        #WYLOGOWANIE
    return redirect('main')



    
