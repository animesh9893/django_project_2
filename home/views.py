from django.shortcuts import render,redirect
from .models import User

# this is default format of data
default_data=data={
	'user_name':'Guest',
	'password':None,
	'status':False,
	'user_name_exist':True,
	'password_is_correct':True,
}

# this is real type of data
data={
	'user_name':'Guest',
	'password':None,
	'status':False,
	'user_name_exist':True,
	'password_is_correct':True,
}

# this function validate the password
def valid_password(password):
	return True

# Create your views here.
def home(request):
	global data
	return render(request,'home/home.html',data)

def log_in(request):
	global data
	print("Log in")
	# getting data from html
	user_name = request.POST.get('user_name')
	password = request.POST.get('password')
	# checking username and password is valid
	if user_name!=None and password!=None:
		print(user_name,password)
		u=list(User.objects.filter(user_name=user_name,password=password))
		if len(u)==0:
			print("Not Log in")
			# if username and password both wrong
			if len(list(User.objects.filter(user_name=user_name)))==0:
				data['user_name_exist']=False
				data['password_is_correct']=False
			# if only password is wrong
			elif len(list(User.objects.filter(user_name=user_name,password=password)))==0:
				data['password_is_correct']=False
				data['user_name_exist']=True
		# if all things are right
		if len(u)==1:
			print("Log in done")
			data['user_name']=user_name
			data['password']=password
			data['status']=True
			data['user_name_exist']=True
			data['password_is_correct']=True
	if not data['status']:
		return render(request,'home/log_in.html',data)
	else:
		return redirect(home)

def sign_up(request):
	global data
	global default_data
	data=default_data
	sign_up_data=data
	sign_up_data['user_name']=""
	sign_up_data['password']=""
	sign_up_data['password_match']=True
	sign_up_data['password_is_valid']=True
	sign_up_data['user_name_available']=True
	user_name = request.POST.get('user_name')
	password = request.POST.get('password')
	password_1 = request.POST.get('password_1')

	if user_name!=None and password!=None and password_1!=None:
		sign_up_data['user_name']=user_name
		sign_up_data['password']=password
		print(user_name,password,password_1)
		is_user_name_available = len(list(User.objects.filter(user_name=user_name)))
		# if username is aldready taken 
		if is_user_name_available!=0:
			sign_up_data['password_match']=False
			sign_up_data['password_is_valid']=False
			sign_up_data['user_name_available']=False
		# if password not match
		elif password_1!=password:
			sign_up_data['password_match']=False
			sign_up_data['password_is_valid']=False
			sign_up_data['user_name_available']=True
		# if password is not valid
		elif not valid_password(password):
			sign_up_data['password_match']=True
			sign_up_data['password_is_valid']=False
			sign_up_data['user_name_available']=True
		else:
			u=User(user_name=user_name,password=password)
			u.save()
			data['user_name']=user_name
			data['password']=password
			data['status']=True
			print("User created")
	if data['status']==True:
		return redirect(log_in)
	else:
		return render(request,'home/sign_up.html',sign_up_data)


def log_out(request):
	global data
	global default_data
	data=default_data
	return redirect(home)