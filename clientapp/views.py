from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User,auth
from .models import TicketRegister,TicketCreation,OrgInsertion
from django.views.generic import ListView
from django.http import JsonResponse
from django.views.generic import View
from django.contrib import messages

# Create your views here.
def home(response):
	return render(response,"register/home.html")

def register(response):
	if response.method=="POST":
		form=RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			messages.success(response,'Registered Successfully')
			return render(response,"registration/login.html")	
	else:
		form=RegisterForm()
		
			
	

	return render(response,"register/register.html",{"form":form})

def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request, user)
			return redirect("index")
		else:
			messages.info(request,"Invalid")
			return redirect("login")
	else:
		return render(request,"registration/login.html")

def homepage(request):
	print(request.user)
	return render(request,'homepage.html')



def dashboard(response):
	return render(response,"dashboard.html")

			
def index(request):
	count=TicketCreation.objects.all().count()

	countticket=TicketCreation.objects.filter(assignee=request.user).count()

	context={'count':count,'countticket':countticket}
	
	print(TicketCreation.objects.filter(assignee=request.user).count())
	return render(request,"dashboard/index.html",context)




class TicketInsert(View):
	def get(self,request):
		
		organization1=request.GET.get('organization',None)
		subject1=request.GET.get('subject',None)
		message1=request.GET.get('message',None)
		prioritylevel1=request.GET.get('prioritylevel',None)

		obj=TicketRegister.objects.create(

			organization=organization1,
			subject=subject1,
			message=message1,
			prioritylevel=prioritylevel1,


			)
		print(obj)
		userss={'id':obj.id,'organization':organization,'subject':subject,'message':message,'prioritylevel':prioritylevel}

		data={'userss':userss}

		return JsonResponse(data)

# class TicketView(ListView):
# 	model=TicketCreation
# 	template_name='dashboard/ticket.html'
# 	context_object_name='objs'

# 	model=OrgInsertion
# 	org_name='dashboard/ticket.html'
# 	context_object_name='orgobj'

	

# 	print(TicketCreation.objects.all().count());
	
	

	
class TicketInsertion(View):
	def get(self,request):

		creator1=request.user
		organization1=request.GET.get('organization',None)
		contact1=request.GET.get('contact',None)
		summary1=request.GET.get('summary',None)
		description1=request.GET.get('description',None)
		assignee1=request.GET.get('assignee',None)
		duedate1=request.GET.get('duedate',None)
		time1=request.GET.get('time',None)
		priority1=request.GET.get('priority',None)
		category1=request.GET.get('category',None)
		related1=request.GET.get('Related',None)

		
		obj=TicketCreation.objects.create(

			creator=creator1,
			organization=organization1,
			contact=contact1,
			summary=summary1,
			description=description1,
			assignee=assignee1,
			duedate=duedate1,
			time=time1,
			priority=priority1,
			category=category1,
			Related=related1,


			)
		print(obj)
		userss={'id':obj.id,
					'creator':creator,
					'organization':organization,
					'contact':contact,
					'summary':summary,
					'description':description,
					'assignee':assignee,
					'duedate':duedate,
					'time':time,
					'priority':priority,
					'category':category,
					'Related':Related
				}

		data={'userss':userss}

		return JsonResponse(data)




class OrgnameInsertion(View):
	def get(self,request):

			
		organizationname1=request.GET.get('organizationname',None)
		
		obj=OrgInsertion.objects.create(

			
			organizationname=organizationname1,

			)
		print(obj)
		userss={'id':obj.id,
					
					'organizationname':organizationname,
					
				}

		data={'userss':userss}

		return JsonResponse(data)

class TicketView(ListView):
	# template_name='dashboard/ticket.html'

	# model=OrgInsertion
	# # org_name='dashboard/ticket.html'
	# context_object_name='orgobj'

# 	 	model=TicketCreation
# 	 	template_name='dashboard/ticket.html'
# 	 	context_object_name='objs'
# 	 	print(context_object_name)
# def get_context_data(self, **kwargs):
# 		model=OrgInsertion
# 		context = super().get_context_data(**kwargs)
# 		context['orgobj'] = OrgInsertion.objects.all()
# 		return context

	def get(self, request, *args, **kwargs):
			ti = TicketCreation.objects.all()
			oj = OrgInsertion.objects.all()
			context = {'orgobj': oj, 'objs': ti}
			return render(request, "dashboard/ticket.html", context=context)




# def head(self, *args, **kwargs):
# 	model=TicketCreation
# 	template_name='dashboard/ticket.html'
#  	# context_object_name='objs'

#  	som_var= self.get_queryset().latest('publication_date') 



	#return context_object_name

	# def get_queryset(self):
	# 	context1=list(OrgInsertion.objects.all())
	# 	print (getattr(context1,'id'))
	# 	#context1['orgobjs']=list(OrgInsertion.objects.all())
	# 	return context1

	# def get_context_data(self,**kwargs):
	# 	context=super(OrgInsertion.self).get_context_data(**kwargs)
	# 	context['orgobj']=OrgInsertion.objects.all()
	# 	print(context)
	# 	return context


	# def get_context_data(self,**kwargs):
	# 	context=super(TicketView.self).get_context_data(**kwargs)
	# 	context['obj']=TicketCreation.objects.all()
	# 	print(context)
	# 	return context

class OrgView(ListView):
	model=OrgInsertion
	template_name='dashboard/ticket.html'
	context_object_name='orgobjs'
