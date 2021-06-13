from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.views import generic,View
from .models import Post
from account.models import AboutUser
from .forms import PublishForm

from django.contrib.auth.models import User

# Create your views here.


class BlogView(generic.ListView):
	model = Post
	template_name = 'blog/blog.html'
	queryset = Post.objects.all().order_by('-pub_date')
    
	
   

class ArticleView(generic.DetailView):
	model = Post
	template_name = 'blog/article.html'

	def get(self, request, *args, **kwargs):
		post= get_object_or_404(Post, slug=kwargs['slug'])
		about = get_object_or_404(AboutUser,username = post.author)
		context = {'post': post,'about':about}
		return render(request, 'blog/article.html', context)


class PublishPostView(generic.CreateView):
	form_class = PublishForm
	query_pk_and_slug = True
	template_name = 'blog/publish_post.html'
	def post(self,request):
		form = self.form_class(request.POST or None , request.FILES or None)
		obj = form.save()
		obj.author = self.request.user
		obj.save()
		return super().form_valid(form)
	
         

		
		