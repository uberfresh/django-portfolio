from django.shortcuts import render,get_object_or_404
from django.views import generic,View
# Create your views here.
from django.urls import reverse_lazy
from .models import Upload
from .forms import ImageForm

from django.http import HttpResponseRedirect
class Image(generic.CreateView):
	form_class = ImageForm
	query_pk_and_slug = True
	template_name = 'imagedetection/image.html'
	def post(self,request):
		form = self.form_class(request.POST or None , request.FILES or None)
		obj = form.save()
		obj.save()
		return super().form_valid(form)
	

	
    

class ImageShow(generic.DetailView):
	model = Upload
	template_name = 'imagedetection/imageshow.html'

	def get(self, request, *args, **kwargs):
		post= get_object_or_404(Upload, pk=kwargs['pk'])
		context = {'post': post}
		return render(request, self.template_name, context)