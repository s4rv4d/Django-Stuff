from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from . import models
from . import forms
from groups.models import Group
from django.contrib.auth import get_user_model
from django.contrib import messages
#j
#current logged in user
User = get_user_model()
# Create your views here.
#SelectRelatedMixin is used so that we can use select_related
class PostlistView(SelectRelatedMixin,generic.ListView):
    context_object_name = 'post_list'
    model = models.Post
    select_related = ('group','user')
    queryset = models.Post.objects.all()

    def get_context_data(self,**kwargs):
        context = super(PostlistView, self).get_context_data(**kwargs)
        context["user_groups"] = Group.objects.filter(members__in=[self.request.user])
        context["all_groups"] = Group.objects.all()
        return context


class UserPosts(LoginRequiredMixin,generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            #basically tryin to get the current user object linked with logged in user
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetailView(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields = ('message','group')
    model = models.Post

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')

    def get_query(self):
        queryset = super().get_query()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs)
