from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext

# Create your views here.
from .models import Entries, Category, Post

def index(request):
    #최근 작성한 글 내림차순으로 5개 불러오기
    post_latest = Post.objects.order_by("-createDate")[:5]
    context = {
        "post_latest" : post_latest
    }

    return render(request, 'index.html', context=context)

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'title_image', 'content', 'category']

class CreatememoView(CreateView):
    model = Entries
    fields = ['title', 'content']
    success_url = reverse_lazy('memolist')
    template_name_suffix = '_create'

class MemolistView(ListView):
    model = Entries

class MemodetailView(DetailView):
    model = Entries

class UpdatememoView(UpdateView):
    model = Entries
    fields = ['title','content']
    template_name_suffix= '_update'

class DeletememoView(DeleteView):
    model = Entries
    #fields = '__all__'
    success_url = reverse_lazy('memolist')


def page(request):
    return render(request, 'simp_web/page.html', {})

def memo(request):
    return render(request, 'simp_web/memo.html', {})

def signup(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))

    context = {'form': form}
    return render(request, 'simp_web/signup.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/simp_web')
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'simp_web/login.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return HttpResponseRedirect('/simp_web')
            else:
                print('User not found')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'simp_web/login.html', {'form': form})

def logout(request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))

def account(request):
    return render(request, 'simp_web/account.html', {})
