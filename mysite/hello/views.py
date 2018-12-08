from django.shortcuts import render
from hello.forms import InputForm
from hello.models import User

# Create your views here.

def index(request):
    message = ''

    if request.method == 'POST':
        form = InputForm(request.POST)

        if form.is_valid():
            user_name = request.POST.get('user_name')
            passwd = request.POST.get('passwd')

            if User.objects.filter(user_name=user_name, passwd=passwd).exists():
            # if user_name == 'admin' and passwd == 'admin':
                message = 'ようそこ！' + user_name + 'さん'
            else:
                message = 'IDまたはパスワードが違います'
    else:
        form = InputForm()


    return render(request, 'index.html', {'form': form, 'message': message})

def register(request):
    message = ''

    if request.method == 'POST':
        form = InputForm(request.POST)

        if form.is_valid():
            user_name = request.POST.get('user_name')
            passwd = request.POST.get('passwd')

            try:
                user = User()
                user.user_name = user_name
                user.passwd = passwd
                user.save()
            except:
                message = '同じユーザ存在します'
        else:
            message = 'エラー'
    else:
        form = InputForm()


    return render(request, 'register.html', {'form': form, 'message': message})