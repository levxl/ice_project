from .models import Doc, IceFatContent
from django.views.generic.base import View
from django.views.generic import ListView
from django.shortcuts import render



def home(request):
    return render(request, 'myapp/index.html')

def catalog(request):
    return render(request, 'myapp/doc_list.html')


class IceFatContent:
    """Жирность"""
    def get_fat_content(self):
        return IceFatContent.objects.all()

    def get_filter(self):
        return Doc.objects.filter()

class IceView(IceFatContent, ListView):
    def get(self, request):
        ice  = Doc.objects.all()
        return render(request, "myapp/doc_list.html", {"doc_list" : ice})

class Search(ListView):
    paginate_by = 3

    def get_queryset(self):
        return Doc.objects.filter(title__icontains=self.request.GET.get("q"))



