from django.views.generic import TemplateView, ListView

from .models import Title


class HelloView(TemplateView):
    template_name = "hello.html"


class ListTitles(ListView):
    model = Title
   # queryset = Title.objects.order_by("price")
    template_name = "list_titles.html"  # def is  demo/title_list.html
    context_object_name = "titles"  # def is object_list