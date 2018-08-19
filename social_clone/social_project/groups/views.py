from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
# or this way is also valid
# from django.views.generic import (
#                                     TemplateView,
#                                     ListView,
#                                     DetailView,
#                                     CreateView,
#                                     UpdateView,
#                                     DeleteView,
# )
from .models import Group, GroupMember
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.

class CreateGroup(LoginRequiredMixin,generic.CreateView):
        model = Group
        fields = ('name','description')
        redirect_field_name = 'groups/group_detail.html'

class SingleGroup(generic.DetailView):
    model = Group
    context_object_name = 'group_detail_context'
    template_name = 'groups/group_detail.html'

class ListGroups(generic.ListView):
    model = Group
    context_object_name = 'group_list_context'
    template_name = 'groups/group_list.html'

class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,'Warning already a member!')
        else:
            messages.success(self.request,'You are now a member!')
        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        # group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
        # or
        try:
            membership = GroupMember.objects.filter(
            user = self.request.user,
            group__slug = self.kwargs.get('slug')
            ).get()
        except GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry you are\'nt in this group')
        else:
            membership.delete()
            messages.success(self.request,'Successfully left this group')
        return super().get(request,*args,**kwargs)
