from django.shortcuts import render
from .models import Post, User
import os
import requests
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
# thank you mr django i will
class BlogListView(ListView):
   model = Post
   template_name = 'home.html'


class BlogDetailView(DetailView):
   model = Post
   template_name = 'post_detail.html'
class BlogCreateView(CreateView):
   model = Post
   template_name = 'post_new.html'
   fields = '__all__'
def login_view(req):
   client_id = os.getenv("CLIENT_ID")
   redirect_uri = os.getenv("URI")
   ion_auth_url = f"https://ion.tjhsst.edu/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope=read+openid"
   return redirect(ion_auth_url)
