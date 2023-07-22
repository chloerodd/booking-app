from django.shortcuts import render, redirect
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView 
from .models import Service as DBService
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Review
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"
    
class Service:
    def __init__(self, name, image, details):
        self.name = name
        self.image = image
        self.details = details
        
        
services = [
    Service("Classic Lashes", "https://i.ibb.co/k5RzFq3/IMG-3425.jpg", "Classic lash extensions are a type of eyelash extensions applied on a 1:1 ratio, which means one extension is attached to one natural lash. One extension is dipped into the adhesive and applied to one of your natural lashes, unlike strip cluster lashes, which are applied to the skin of the eyelid. Classic lash extensions are also known as individual lashes or 1 to 1 lash extensions."),
    Service("Hybrid Lashes","https://i.ibb.co/P57gktQ/IMG-3426.jpg", "Hybrid lashes are classic lashes (1:1) and volume lashes (2-6:1) mixed to give length and volume to sparse lashes."),
    
]

class ServiceList(TemplateView):
    template_name = "service_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["services"] = DBService.objects.filter(name__icontains=name)
        else:
            context["services"] = DBService.objects.all()
        return context
    
    
class ServiceDetail(DetailView):
    model = DBService
    template_name = "service_detail.html"
    
@method_decorator(login_required, name='dispatch')    
class ServiceCreate(CreateView):
    model = DBService
    fields = ['name', 'img', 'details']
    template_name = "service_create.html"
    def get_success_url(self):
        return reverse('service_detail', kwargs={'pk': self.object.pk})
 
@method_decorator(login_required, name='dispatch')    
class ServiceUpdate(UpdateView):
    model = DBService
    fields = ['name', 'img', 'details']
    template_name = "service_update.html"
    def get_success_url(self):
        return reverse('service_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required, name='dispatch')
class ServiceDelete(DeleteView):
    model = DBService
    template_name = "service_delete_confirmation.html"
    success_url = "/services/"
    
    
def reviews_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        text = request.POST.get('text')
        review = Review.objects.create(name=name, rating=rating, text=text)
        return redirect('reviews_page')  # Redirect back to the reviews page after submitting the review
    else:
        reviews = Review.objects.all()
        return render(request, 'reviews_page.html', {'reviews': reviews})
    
    
class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("service_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)