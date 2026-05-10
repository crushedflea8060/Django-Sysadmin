from django.shortcuts import render
from .models import Post, User
import os
import requests
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# thank you mr django i will
class BlogListView(ListView):
   model = Post
   template_name = 'home.html'


class BlogDetailView(DetailView):
   model = Post
   template_name = 'post_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
   model = Post
   template_name = 'post_new.html'
   fields = '__all__'
def login_view(req):
   client_id = os.getenv("CLIENT_ID")
   redirect_uri = os.getenv("URI")
   ion_auth_url = f"https://ion.tjhsst.edu/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope=read+openid"
   return redirect(ion_auth_url)
def callback_view(req):
   code = req.get.GET("code")
   id = os.getenv("ION_CLIENT_SECRET")
   response = requests.post("https://ion.tjhsst.edu/oauth/token/", data={
   "grant_type":"authorization_code",
   "code":code,
   "client_id":id,
   "client_secret": secret,
   "redirect_uri" = os.getenv("URI")
   })
   data = response.json
   access_token = data.get("access_token")
   profile_response = requests.get("https://ion.tjhsst.edu/api/profile", headers={"Authorization:" f"Bearer {access_token}")
   username = profile_data.get("ion_username")
   user, created = User.objects.get_or_create(username=username)
   profile, profile_created = Profile.objects.get_or_create(user=user)
   login(req, user)
   return redirect("/")
