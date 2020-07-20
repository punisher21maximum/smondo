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

model_dict = {
    "Post":Post, 
    "Bike":Bike, 
    "Scooty":Scooty, 
    "Bicycle":Bicycle, 
    "Mobile":Mobile
    }

# from .filters import EnotesFilter, QuesPaperFilter, PracsFilter

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = 9


# class UserPostListView(ListView):
#     model = Post
#     template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     paginate_by = 5

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Post.objects.filter(author=user).order_by('-date_posted')

# from django.core.mail import EmailMessage
# from django.core.mail import send_mail


# class PostDetailView(DetailView):
#     model = Post
#     # test_email()

# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = '__all__'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = '__all__'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Post
#     success_url = '/'
#     template_name = 'blog/post_confirm_delete.html'

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False



# def about(request):
#     return render(request, 'blog/about.html', {'title': 'About'})

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
        print(model_dict[ kwargs.get('model', None) ])
        self.model = model_dict[ kwargs.get('model', None) ]
        return super(SubcatListView, self).dispatch(request, *args, **kwargs)

    """ "get_queryset" also Required to override model name """
    # def get_queryset(self):
    #     return self.model.objects.filter()

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

class SubcatUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bike
    fields = my_get_model_fields(Bike)

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

"""Bike cat"""
#Bike 
class BikeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bike
    fields = my_get_model_fields(Bike)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class BikeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bike
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

"""Scooty cat"""
#Scooty
class ScootyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Scooty
    fields = my_get_model_fields(Scooty)
    template_name = 'blog/bike_form.html'  # <app>/<model>_<viewtype>.htm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class ScootyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Scooty
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

"""MobileCat"""
#mobile
class MobileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Mobile
    fields = my_get_model_fields(Mobile)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class MobileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mobile
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# #enotes

# class EnotesListView(ListView):
#     # model = Enotes
#     template_name = 'blog/enotes-home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'enotes'
#     # ordering = ['-date_posted']
#     paginate_by = 3

#     def get_context_data(self,**kwargs):
#         context = super(EnotesListView,self).get_context_data(**kwargs)
#         context['filter'] = EnotesFilter(self.request.GET,queryset=self.get_queryset())
#         return context

#     def get_queryset(self):
#         return Enotes.objects.all()

# class EnotesDetailView(DetailView):
#     model = Enotes


# class EnotesCreateView(LoginRequiredMixin, CreateView):
#     model = Enotes
#     fields = ['topic', 'unit', 'notes_author', 'author_name', 'fileMy',
#     'sub', 'sub_new', 'branch', 'academic_year', 'desc']
#     template_name = 'blog/enotes_form.html'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def get_absolute_url(self):
#         return "blog-home/"

# class EnotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Enotes
#     fields = ['topic', 'unit', 'notes_author', 'author_name', 'fileMy',
#     'sub', 'sub_new', 'branch', 'academic_year', 'desc']
#     template_name = 'blog/enotes_form.html'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         enotes = self.get_object()
#         if self.request.user == enotes.author:
#             return True
#         return False

# class EnotesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Enotes
#     success_url = '/enotes/'
#     template_name = 'blog/post_confirm_delete.html'

#     def test_func(self):
#         model_name = self.get_object()
#         if self.request.user == model_name.author:
#             return True
#         return False

# # Ques paper : QuesPaper

