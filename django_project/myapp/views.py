import queue
from unicodedata import category
from .models import Doc, IceFatContent, Category
from django.views.generic import ListView
from django.shortcuts import render


def home(request):
    return render(request, 'myapp/index.html')

def catalog(request):
    return render(request, 'myapp/doc_list.html')


class IceFatsContent:
    """Жирность"""
    def get_fat_content(self):
        return IceFatContent.objects.all()

    def get_filter(self):
        return Category.objects.filter()

class IceView(IceFatsContent,ListView):
    model = Doc
    queryset = Doc.objects.filter()

class Search(ListView):
    paginate_by = 3
    def get_queryset(self):
        return Doc.objects.filter(title__icontains=self.request.GET.get("q"))

class FilterIceView(IceFatContent, ListView):
    def get_queryset(self):
        queryset = Doc.objects.filter(category__in=self.request.GET.getlist("category"))
        return queryset