from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
#decorators are only for funcion based views
#mixins are for class based views
from django.views.generic import (
                                    TemplateView,
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from blog.models import Comment,Post
from blog.forms import CommentForm,PostForm
# Create your views here.
#
###########################
#    Class based views    #
###########################

class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    def get_queryet(self):
        #__lte is less than or equal to
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post_detail'

class CreatePostView(LoginRequiredMixin,CreateView):
    #if not logged in
    login_url = 'login/'
    #if logged in
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post
class PostUpdateView(LoginRequiredMixin,UpdateView):
    #if not logged in
    login_url = 'login/'
    #if logged in
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

# class SchoolDeleteView(DeleteView):
#     model = models.SchoolModel
#     context_object_name = 'schools'
#     success_url = reverse_lazy("basic_app:list")

class DraftListView(LoginRequiredMixin,ListView):
    #if not logged in
    login_url = 'login/'
    #if logged in
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryet(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

###########################
#  Function based views   #
###########################

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
