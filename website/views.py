from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

@login_required(login_url='login')
def home(request):
    records= Record.objects.all()
    return render(request, 'home.html' , {'records':records})

def login_user(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Successful Login")
            return redirect('home')
        else:
            messages.success(request,"Retry, some error occured")
            return redirect('login')
    else:
        return render(request, 'login.html' , {})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password1')
            user= authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"Account created successfully")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html' , {'form':form})
    return render(request, 'register.html' , {'form':form})

@login_required(login_url='login')
def customer_record(request,pk):
    record = Record.objects.get(id=pk)
    return render(request, 'record.html' , {'customer_record':record})

def delete_record(request, pk):

	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		if delete_it.user == request.user:
			delete_it.delete()
			messages.success(request, "Record Deleted Successfully...")
			return redirect('home')
		else:
			messages.success(request, "You Can't Delete That Record...")
			return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				new_record = form.save(commit=False)
				# Set the user field to the currently logged-in user
				new_record.user = request.user
				# Now save the record with the user assigned
				new_record.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')




