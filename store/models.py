from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	number_phone =models.CharField(max_length=17)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.email


class Image(models.Model):
	product = models.ForeignKey('Product', null=True, on_delete=models.CASCADE, related_name= 'product_image')
	photo = models.ImageField(null=True, blank=True, upload_to='media/images/')

	def __str__(self):
		return self.product.name + " photo"


@ receiver(post_save, sender=User)
def create_user_customer(sender, instance, created,**kwargs):
	if created:
		Customer.objects.create(
			user=instance
		)


def image_uplode(self, instance, filename):
	imageName, extention = filename.splite(".")
	return "product/%s.%s" % (instance.id, instance.id, extention)


class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=1200, default='this is a description for article')
	price = models.FloatField()
	active = models.BooleanField(default=True)
	stock = models.CharField(max_length=6, null=True, blank=True)
	digital = models.BooleanField(default=False, null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	image = models.ImageField(upload_to='image_uploade', blank=True)

	slug = models.SlugField(null=True, blank=True)

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Products'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 


class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address