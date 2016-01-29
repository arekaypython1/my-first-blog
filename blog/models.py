from django.db import models
from django.utils import timezone





class Post(models.Model): #tell class to use Django models(object/class) as input and save into database
	author = models.ForeignKey('auth.User') #create field author for list of users 
	title = models.CharField(max_length=200) #create field for title under CharField method(text with limited character amount) maximum 200 characters 
	text = models.TextField() #create field for article write up under TextField method (not taking any arguments/variables)
	created_date = models.DateTimeField(default=timezone.now) # create field for entering time DateTimeField(taking argument of default timezone Asia/KL)
	published_date = models.DateTimeField(blank=True, null=True) # create field for entering time, method argument blank

	def publish(self): #not sure yet how it works
		self.published_date = timezone.now()
		self.save()

	def __str__(self): #return title in title properties each time __str__ method is called 
		return self.title
	
	 
