from django.shortcuts import render
from django.views import generic,View

# Create your views here.
class Index(View):
	def get(self, request):
		return render(request,'base/index.html')
       
       

class ProjectsView(generic.ListView):
	
	template_name = 'base/projects.html'
