from django.shortcuts import redirect,render,get_object_or_404,get_list_or_404
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
	context = {'object_list':Post.objects.all().order_by('-pub_date') }
	def get(self,request,*args,**kwargs):
	
		if request.user.pk and not AboutUser.objects.filter(username__username = request.user.username).exists():
			return redirect('account:about',username= request.user.username)
		else:
			return render(request,self.template_name,self.context)

	
	
class ArticleView(generic.DetailView):
	model = Post
	template_name = 'blog/article.html'

	def get(self, request, *args, **kwargs):
		post= get_object_or_404(Post, slug=kwargs['slug'])
		about = get_object_or_404(AboutUser,username = post.author)
		context = {'post': post,'about':about}
		return render(request, self.template_name, context)


class PublishPostView(generic.CreateView):
	form_class = PublishForm
	template_name = 'blog/publish_post.html'
	def post(self,request):
		form = self.form_class(request.POST or None , request.FILES or None)
		obj = form.save()
		obj.author = self.request.user
		obj.save()
		return super().form_valid(form)

class UpdatePostView(generic.UpdateView):
	model = Post
	form_class = PublishForm
	template_name = 'blog/publish_post.html'

class DeletePostView(generic.DeleteView):
	model = Post
	template_name = 'blog/delete.html'
	success_url = '/blog/'
   
   
class ProfileView(generic.View):
	template_name = 'blog/profile.html'
    
	def get(self,request,*args,username):
		context={}
		posts = Post.objects.filter(author__username = username)
		about = get_object_or_404(AboutUser,username__username=username)
		context['about'] = about
		if posts:
			context['posts'] = posts
       	
		return render(request,self.template_name,context)


	






		
		