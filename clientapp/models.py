from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TicketRegister(models.Model):
	organization=models.CharField(max_length=100)
	subject=models.CharField(max_length=100)
	message=models.CharField(max_length=300)
	prioritylevel=models.CharField(max_length=100)
	datetime=models.DateTimeField(auto_now=True)

class TicketCreation(models.Model):

	creator = models.ForeignKey(User,db_column='username',on_delete=models.CASCADE)
	organization=models.CharField(max_length=150)
	contact=models.CharField(max_length=12)
	summary=models.CharField(max_length=200)
	description=models.CharField(max_length=300)
	assignee=models.CharField(max_length=150,blank=True)
	duedate=models.DateField(auto_now=True)
	time=models.TimeField(auto_now=True)
	priority=models.CharField(max_length=100)
	category=models.CharField(max_length=100)
	Related=models.CharField(max_length=150)
	created=models.DateField(auto_now=True)
	updated=models.DateField(auto_now=True)
	status1=models.CharField(max_length=100,blank=True)
	status2=models.CharField(max_length=100,blank=True)


class OrgInsertion(models.Model):
	organizationname=models.CharField(max_length=100)