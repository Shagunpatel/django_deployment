from django.shortcuts import render
from trial.models import School,Student
from django.views.generic import View,TemplateView,DetailView,ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
# Create your views here.

class SchoolListView(ListView):
    context_object_name="schools"
    print("HII")
    # ListView returns the list named school_list(default name) we can assign by context_object_name
    model=School
    print(model,ListView)
    # template_name="trial/school_list.html" # default school_list.html if present don't mention this
class SchoolDetailView(DetailView):
    context_object_name="school_detail"
    # DetailView returns the object named schools(default name) we can assign by context_object_name
    model=School
    template_name="trial/school2.html" # default school_detail.html if present don't mention this
class SchoolCreateView(CreateView):
    fields=("name","principal","location")
    model=School
class SchoolUpdateView(UpdateView):
    fields=("name","principal")
    model=School
class SchoolDeleteView(DeleteView):
    context_object_name="school_del"
    model=School
    # template_name="trial/school_confirm_delete.html"
    success_url=reverse_lazy("trial:list")
