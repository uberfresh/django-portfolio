from django.shortcuts import render
from django.utils import timezone
from django.views import generic,View
from .models import PostModal
from .forms import PublishForm

# Create your views here.


class PostList(generic.ListView):
        template_name = 'blog/post_list.html'
        
        def get_queryset(self):
        	return PostModal.objects.all()
       
        
        def get_context_data(self,**kwargs):
        	context = super().get_context_data(**kwargs)
        	context['posts'] = PostModal.objects.all().order_by('-pub_date')
        	context['post_count'] = PostModal.objects.all().count()
        	return context

	    

	   

class Post(generic.DetailView):
	model = PostModal
	template_name = 'blog/post.html'
	context_object_name = 'post'
	def get_queryset(self):
		return PostModal.objects.all()



class PublishForm(View):
	form_class = PublishForm()
	
	template_name = 'blog/publish_post.html'
	context ={}
        
	