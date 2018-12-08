from django.shortcuts import render
from hello.forms import InputForm
from .models import User

# Create your views here.
def index(request):
    message = ''
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_name = request.POST.get('user_name')
            passwd = request.POST.get('passwd')

            try:
                user = User ()
                user.user_name = user_name
                user.passwd = passwd
                user.save()
                message = user_name + 'welcome'
            except:
                message = 'すでに同じユーザ名が存在します'
        else:
                message = 'Error!'
    else:
        form = InputForm()
    return render (request, "index.html", {'form': form, 'message': message})

if User.objects.filter(user_name=user_name, passwd=passwd).exists():
    message = 'Welcome!' + user_name
else:
    message = 'Not found user name and password'