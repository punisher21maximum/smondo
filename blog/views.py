from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail


from django.urls import reverse_lazy
from .models import (Post, 
    Bike, Scooty, #Bicycle, 
    Mobile,  MobileCharger, #MobileCover,
    Laptop, Mouse, Keyboard,
    Novel, Engg, School,
    #new
    Stationery, Electronics, Furniture,
    Vehicle, HouseHold, Other
    )

# import filters
from . filters import ( 
                        BikesFilter, ScootysFilter, 
                        MobilesFilter, MobileChargersFilter, 
                        LaptopsFilter,  MousesFilter, KeyboardsFilter,
                        NovelsFilter, EnggsFilter, SchoolsFilter,
                        #new
                        StationerysFilter, ElectronicsFilter, FurnituresFilter,
                        VehiclesFilter, HouseHoldsFilter, OthersFilter
                        )

# import ends    
model_dict = {
    "post" : Post, 
    "bike": Bike, "scooty" : Scooty,  
    "mobile" : Mobile, "mobilecharger" : MobileCharger,
    "laptop" : Laptop,  "mouse" : Mouse, "keyboard" : Keyboard,
    "novel" : Novel, "engg": Engg, "school": School,
    #new
    "stationery" : Stationery, "electronics" : Electronics, 
    "furniture" : Furniture, "vehicle" : Vehicle, 
    "household" : HouseHold, "other" : Other
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

#get my filter
def get_model_filter_func(model_name):

    model_filter_dict = {
    # "post" : Post, 
    "bike": BikesFilter, "scooty" : ScootysFilter,  
    "mobile" : MobilesFilter, "mobilecharger" : MobileChargersFilter,
    "laptop" : LaptopsFilter,  "mouse" : MousesFilter, "keyboard" : KeyboardsFilter,
    "novel" : NovelsFilter, "engg":EnggsFilter, "school":SchoolsFilter,
    #new
    "stationery" : StationerysFilter, "electronics" : ElectronicsFilter, 
    "furniture" : FurnituresFilter, "vehicle" : VehiclesFilter, 
    "household" : HouseHoldsFilter, "other" : OthersFilter
    }

    return model_filter_dict[model_name]



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
        context['class_name'] = self.model._meta.model_name.lower() # kwargs.get('model', None)
        ModelFilter = get_model_filter_func(self.model._meta.model_name.lower())
        context['filter'] =  ModelFilter(self.request.GET, queryset=self.get_queryset())
        return context

#DetailView
class SubcatDetailView(DetailView):
    """overriding "dispatch" func to set model passed as arg in URL"""

    # template_name = <app>/<model>_<viewtype>.html
    context_object_name = 'post'
    template_name = 'blog/subcat_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.model = model_dict[ kwargs.get('model', None).lower() ]
        return super(SubcatDetailView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter()

    def get_context_data(self, **kwargs):
        """override "get_context_data" to pass model_name to subcat_list.html"""
        context = super().get_context_data(**kwargs)
        context['class_name'] = self.model._meta.model_name.lower() # kwargs.get('model', None) 
        ModelFilter = get_model_filter_func(self.model._meta.model_name.lower())
        context['filter'] =  ModelFilter(self.request.GET, queryset=self.get_queryset())
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
        self.fields = my_get_model_fields(model_dict[self.model._meta.model_name.lower()])
        return super(SubcatCreateView, self).get_form_class()

    # def get_context_data(self, **kwargs):
    #     """override "get_context_data" to pass model_name to subcat_list.html"""
    #     context = super().get_context_data(**kwargs)
    #     context['class_name'] = self.model._meta.model_name.lower() # kwargs.get('model', None) 
    #     ModelFilter = get_model_filter_func(self.model._meta.model_name.lower())
    #     context['filter'] =  ModelFilter(self.request.GET, queryset=self.get_queryset())
    #     return context

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
        self.fields = my_get_model_fields(model_dict[self.model._meta.model_name.lower()])
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
        context['class_name'] = self.model._meta.model_name.lower() # kwargs.get('model', None) 
        return context

    def get_success_url(self):
        return reverse_lazy('subcat-list', kwargs={'model':self.model._meta.model_name.lower()})


####################### My Posts ##########################
class UserSubcatListView(SubcatListView):
    
    template_name = 'blog/user_subcat_list.html' # <app>/<model>_<viewtype>.html

    """ "get_queryset" also Required to override model name """
    def get_queryset(self):
        return self.model.objects.filter(author = self.request.user)

