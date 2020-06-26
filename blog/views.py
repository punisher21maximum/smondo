from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Enotes, QuesPaper, Pracs
from django.contrib.auth.models import User

from .filters import EnotesFilter, QuesPaperFilter, PracsFilter

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 9




class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

from django.core.mail import EmailMessage
from django.core.mail import send_mail
def test_email():
    subject = 'Testing email'
    message = "how are you man"
    from_e = "vishal7x7@gmail.com"
    to_email = "vishal7x7@gmail.com"
    send_mail(subject, message, "vishal7x7@gmail.com", ["vishal7x7@gmail.com"],
        auth_user="vishal7x7@gmail.com", auth_password="Maxeffort@21")
class PostDetailView(DetailView):
    model = Post
    # test_email()



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'blog_file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'blog_file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



#enotes

class EnotesListView(ListView):
    # model = Enotes
    template_name = 'blog/enotes-home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'enotes'
    # ordering = ['-date_posted']
    paginate_by = 3

    def get_context_data(self,**kwargs):
        context = super(EnotesListView,self).get_context_data(**kwargs)
        context['filter'] = EnotesFilter(self.request.GET,queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return Enotes.objects.all()

class EnotesDetailView(DetailView):
    model = Enotes


class EnotesCreateView(LoginRequiredMixin, CreateView):
    model = Enotes
    fields = ['topic', 'unit', 'notes_author', 'author_name', 'fileMy',
    'sub', 'sub_new', 'branch', 'academic_year', 'desc']
    template_name = 'blog/enotes_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return "blog-home/"

class EnotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Enotes
    fields = ['topic', 'unit', 'notes_author', 'author_name', 'fileMy',
    'sub', 'sub_new', 'branch', 'academic_year', 'desc']
    template_name = 'blog/enotes_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        enotes = self.get_object()
        if self.request.user == enotes.author:
            return True
        return False

class EnotesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Enotes
    success_url = '/enotes/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        model_name = self.get_object()
        if self.request.user == model_name.author:
            return True
        return False

# Ques paper : QuesPaper


class QuesPaperListView(ListView):
    # model = QuesPaper
    template_name = 'blog/ques_ppr-home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'quespprs'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_context_data(self,**kwargs):
        context = super(QuesPaperListView,self).get_context_data(**kwargs)
        context['filter'] = QuesPaperFilter(self.request.GET,queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return QuesPaper.objects.all()

class QuesPaperDetailView(DetailView):
    model = QuesPaper
    template_name = 'blog/quespaper_detail.html'

class QuesPaperCreateView(LoginRequiredMixin, CreateView):
    model = QuesPaper
    fields = ['sem_exam', 'total_marks', 'exam_date', 'exam_type', 'fileMy',
    'sub', 'sub_new', 'branch', 'academic_year', 'desc']
    template_name = 'blog/enotes_form.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return "ques-paper-home/"

class QuesPaperUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = QuesPaper
    fields = ['sem_exam', 'total_marks', 'exam_date', 'exam_type', 'fileMy',
    'sub', 'sub_new', 'branch', 'academic_year', 'desc']
    template_name = 'blog/enotes_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        qp = self.get_object()
        if self.request.user == qp.author:
            return True
        return False

class QuesPaperDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = QuesPaper
    success_url = '/quespaper/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        model_name = self.get_object()
        if self.request.user == model_name.author:
            return True
        return False


#pracs
class PracsListView(ListView):
    # model = Pracs
    template_name = 'blog/pracs-home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'pracs'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_context_data(self,**kwargs):
        context = super(PracsListView,self).get_context_data(**kwargs)
        context['filter'] = PracsFilter(self.request.GET,queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return Pracs.objects.all()

class PracsDetailView(DetailView):
    model = Pracs


class PracsCreateView(LoginRequiredMixin, CreateView):
    model = Pracs
    fields = ['topic', 'question', 'pracs_author', 'author_name', 'fileMy',
    'sub', 'sub_new', 'branch', 'academic_year', 'desc']
    template_name = 'blog/enotes_form.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return "pracs-home/"

class PracsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pracs
    fields = ['topic', 'question', 'pracs_author', 'author_name', 'fileMy',
    'sub', 'sub_new', 'branch', 'academic_year', 'desc']
    template_name = 'blog/enotes_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        prac = self.get_object()
        if self.request.user == prac.author:
            return True
        return False

class PracsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pracs
    success_url = '/pracs/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        model_name = self.get_object()
        if self.request.user == model_name.author:
            return True
        return False