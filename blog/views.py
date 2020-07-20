from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Bike, Scooty, Bicycle, Mobile
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.urls import reverse_lazy

model_dict = {
    "Post":Post, 
    "Bike":Bike, 
    "Scooty":Scooty, 
    "Bicycle":Bicycle, 
    "Mobile":Mobile
    }


#get my fields
def my_get_model_fields(model):
    all_f = [field.name for field in model._meta.get_fields()] 
    rf = ['id', 'date_posted']
    all_f.remove('author')
    for f in all_f: 
        if f in rf or f.endswith('_ptr'):
            all_f.remove(f)
    return all_f

"""subcat view"""
#ListView
class SubcatListView(ListView):

    template_name = 'blog/subcat_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    """overriding "dispatch" func to set model passed as arg in URL"""
    def dispatch(self, request, *args, **kwargs):
        self.model = model_dict[ kwargs.get('model', None) ]
        return super(SubcatListView, self).dispatch(request, *args, **kwargs)

    """ "get_queryset" also Required to override model name """
    def get_queryset(self):
        return self.model.objects.filter()

    def get_context_data(self, **kwargs):
        """override "get_context_data" to pass model_name to subcat_list.html"""
        context = super().get_context_data(**kwargs)
        context['class_name'] = self.model._meta.model_name.title() # kwargs.get('model', None) 
        return context

#DetailView
class SubcatDetailView(DetailView):
    """overriding "dispatch" func to set model passed as arg in URL"""

    # template_name = <app>/<model>_<viewtype>.html
    context_object_name = 'post'
    template_name = 'blog/subcat_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.model = model_dict[ kwargs.get('model', None) ]
        return super(SubcatDetailView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter()

    def get_context_data(self, **kwargs):
        """override "get_context_data" to pass model_name to subcat_list.html"""
        context = super().get_context_data(**kwargs)
        context['class_name'] = self.model._meta.model_name.title() # kwargs.get('model', None) 
        return context

#CreateView
class SubcatCreateView(LoginRequiredMixin, CreateView):
    # model = Bike
    
    # fields = my_get_model_fields(Bike)
    template_name = 'blog/subcat_form.html'

    def form_valid(self, form):
        """check form author and current logged in user is same"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        """overriding "dispatch" func to set model passed as arg in URL"""
        self.model = model_dict[ kwargs.get('model', None) ]
        return super(SubcatCreateView, self).dispatch(request, *args, **kwargs)

    def get_form_class(self):
        """overriding "get_form_class" func to get fields for model passed in URL"""
        self.fields = my_get_model_fields(model_dict[self.model._meta.model_name.title()])
        return super(SubcatCreateView, self).get_form_class()

#UpdateView
class SubcatUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    template_name = 'blog/subcat_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def dispatch(self, request, *args, **kwargs):
        """overriding "dispatch" func to set model passed as arg in URL"""
        self.model = model_dict[ kwargs.get('model', None) ]
        return super(SubcatUpdateView, self).dispatch(request, *args, **kwargs)

    def get_form_class(self):
        """overriding "get_form_class" func to get fields for model passed in URL"""
        self.fields = my_get_model_fields(model_dict[self.model._meta.model_name.title()])
        return super(SubcatUpdateView, self).get_form_class()

#DeleteView
class SubcatDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def dispatch(self, request, *args, **kwargs):#model
        """overriding "dispatch" func to set model passed as arg in URL"""
        self.model = model_dict[ kwargs.get('model', None) ]
        return super(SubcatDeleteView, self).dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):#class_name
        """override "get_context_data" to pass model_name to subcat_list.html"""
        context = super().get_context_data(**kwargs)
        context['class_name'] = self.model._meta.model_name.title() # kwargs.get('model', None) 
        return context

    def get_success_url(self):
        return reverse_lazy('subcat-list', kwargs={'model':self.model._meta.model_name.title()})

