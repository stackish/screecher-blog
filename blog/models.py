import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import  Q
from django.core.validators import MinValueValidator, MaxValueValidator



User=settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		return self.filter(publish_date__lte=now)
	
	def search(self,query):
		lookups=(Q(title__icontains=query) |
		Q(content__icontains=query) |
		Q(slug__icontains=query) |
		Q(user__first_name__icontains=query) |
		Q(user__last_name__icontains=query) |
	    Q(user__username__icontains=query) |
	    Q(user__email__icontains=query) 	
				)
		return self.filter(lookups)
			
	

class BlogPostManager(models.Manager):
	def get_queryset(self):
		return BlogPostQuerySet(self.model,using=self._db)


	def published(self):
		return self.get_queryset().published()
		
		
	def search(self,query=None):
		if query is None:
			return self.get_queryset().none()
		return  self.get_queryset().published().search(query)
		
	

	
# Create your models here.
class BlogPost(models.Model):
	user=models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
	image=models.ImageField(upload_to='image/',blank=True,null=True)
	title=models.CharField(max_length=120)
	slug=models.SlugField(unique=True)
	content=models.TextField(null=True,blank=True)
	publish_date=models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True,help_text="use this format:yyyy-mm-dd")
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(User,related_name="blog_post_like",blank=True)
	
	

	objects=BlogPostManager()

	class Meta:
		ordering =['-publish_date','-updated','-timestamp']


	def __str__(self):
		return self.title
		



	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	def get_api_like_url(self):
		return f"/blog/{self.slug}/like"

	
	def get_like_count(self):
		return f"/blog/{self.slug}/getCount"

	def get_like_users(self):
		return f"/blog/{self.slug}/getUsers"


	
	def get_edit_url(self):
		
		return f"/blog/{self.slug}/modify"
	


	def get_delete_url(self):
		
		return f"/blog/{self.slug}/delete"
	
	
class CommentSection(models.Model):
	#c_id = models.UUIDField(max_length=8,primary_key=False, default=uuid.uuid4,editable=False,unique=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	blogpost=models.ForeignKey(BlogPost,on_delete=models.CASCADE,default=1)
	comment=models.TextField()
	timestamp=models.DateTimeField(auto_now_add=True)
	
	
	class Meta:
		ordering=['-timestamp']
	
	def __str__(self):
		return self.comment
		




        