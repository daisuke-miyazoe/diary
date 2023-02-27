from django.views import generic
from .forms import Inquiryform

class IndexView(generic.TemplateView):
    template_name = 'index.html'


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = Inquiryform