from django.db import models

class Shop(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	url = models.URLField()
	email = models.EmailField()
	payment_system = models.CharField(max_length=100)
	# e.g. IBAN or Bitcoin address

class Client(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	payment_system = models.CharField(max_length=100)

class Sales(models.Model):
	shop = models.ForeignKey(Shop)
	client = models.ForeignKey(Client)
	date = models.DateTimeField('date sold')
# represents a good or a service
class Valuable(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	shop = models.ForeignKey(Shop)


class ValuablePriceSegment(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=500)
	minimum_price = models.IntegerField()
	minimum_percentage = models.IntegerField()
	valuable = models.ForeignKey(Valuable)
#	W = models.ManyToManyField(X) consider instead
	payment_system = models.CharField(max_length=100)
	# e.g. IBAN or Bitcoin address

class ValuedPurchase(models.Model):
	valuable_price_segment = models.ForeignKey(ValuablePriceSegment)
	client = models.ForeignKey(Client)
	amount = models.IntegerField()
	percentage = models.IntegerField()
	sale = models.ForeignKey(Sales)


class Stock(models.Model):
	valuable = models.ForeignKey(Valuable)
	shop = models.ForeignKey(Shop)
	quantity = models.IntegerField()

