from django.shortcuts import render
from django.views import generic,View
from .models import Projects

# Create your views here.
class Index(View):
	def get(self, request):
		return render(request,'base/index.html')
       
       

class ProjectsView(generic.ListView):
	model = Projects
	template_name = 'base/projects.html'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['projects'] = Projects.objects.all().order_by('-pub_date')
		return context


		
