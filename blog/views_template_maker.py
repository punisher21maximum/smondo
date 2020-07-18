class MobileListView(ListView):
    model = Mobile
    template_name = 'blog/mobile_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6


class MobileDetailView(DetailView):
    model = Mobile


class MobileCreateView(LoginRequiredMixin, CreateView):
    model = Mobile
    
    fields = my_get_model_fields(Mobile)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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