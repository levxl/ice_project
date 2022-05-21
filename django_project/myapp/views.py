from .models import *
from django.shortcuts import render
from django.views.generic import ListView, DetailView


def home(request):
    return render(request, 'myapp/index.html')

class IceFatsContent:
    """Жирность"""
    def get_fat_content(self):
        return IceFatContent.objects.all()

    def get_filter(self):
        return Fillers.objects.filter()

class IceView(IceFatsContent, ListView):
    def get(self, request):
        doc = Doc.objects.all()
        return render(request, "myapp/doc_list.html", {"doc":doc})



class Search(ListView):
    paginate_by = 3
    def get_queryset(self):
        return Doc.objects.filter(title__icontains=self.request.GET.get("q"))

class FilterIceView(IceFatContent, ListView):
    def get_queryset(self):
        queryset = Doc.objects.filter(Fillers=self.request.GET.getlist())
        return queryset