from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
@login_required(login_url="login")
def recipe(request):
    if request.method=="POST":
        data = request.POST
        rname = data.get("rname")
        rdesc = data.get("rdesc")
        rimg = request.FILES.get("rimg")
        user = request.user

        Rece.objects.create(
            rname = rname,
            rdesc = rdesc,
            rimg = rimg,
            user = user
        )
        return redirect("recipe_success")

    rec = Rece.objects.all()

    if request.GET.get("search"):
        rec = rec.filter(rname__icontains = request.GET.get("search"))

    context = {
        "recipes":rec
    }
   
    return render(request,"vege.html",context)


@login_required(login_url="login")
def recipe_success(request):
    return render(request, "recipe_success.html")


@login_required(login_url="login")
def delete_r(request,id):
    rec = Rece.objects.get(id=id)
    rec.delete()
    return redirect("rece")


@login_required(login_url="login")
def update_r(request,id):
    rec = Rece.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        rname = data.get("rname")
        rdesc = data.get("rdesc")
        rimg = request.FILES.get("rimg")        

        rec.rname = rname
        rec.rdesc = rdesc
        if rimg:
             rec.rimg = rimg

        rec.save()

        return redirect("rece")

    context = {
        "recipe":rec
    }

    return render(request,"update.html",context)


def Login(request):
    if request.method == "POST":
        data = request.POST
        uname = data.get("uname")
        password = data.get("password")

        if not User.objects.filter(username = uname).exists():
            messages.error(request,"Username Not Exists")
            return redirect("login")
        
        user = authenticate(username=uname, password = password)
        
        if user is None:
            messages.error(request,"Wrong Password")
            return redirect("login")


        else:
            login(request,user)
            return redirect("rece")

    return render(request,"login.html")


def Logout(request):
    logout(request)
    return redirect("login")

def Register(request): 

    if request.method == "POST":
        data = request.POST
        fname = data.get('fname')
        lname = data.get('lname')
        uname = data.get('uname')
        password = data.get('password')

        if (User.objects.filter(username = uname).exists()):
            messages.error(request,"Username Already Exists")
            return redirect("register")

        user = User.objects.create(
            first_name = fname,
            last_name = lname,
            username = uname        
            )

        user.set_password(password)
        user.save()
        messages.info(request,"Account Created SuccessFully")
        return redirect("register")


    return render(request,"register.html")

from django.db.models import Q

def get_student(request):
    queryset = Student.objects.all()


    if request.GET.get("search"):
        data = request.GET.get("search")
        queryset = queryset.filter(Q(student_name__icontains = data) | Q(department__department__icontains = data))

    paginator = Paginator(queryset, 25) 

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    
    return render(request,"student.html",{"queryset":page_obj})


from django.db.models import Sum

def see_marks(request,student_id):
    qs = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total = qs.aggregate(total = Sum('marks'))
    return render(request,"see_marks.html",{"queryset":qs,"total":total})



from .utils import *

def send_mail(request):
    subject = "JUST CHECKING CODE"
    message = "This is spam message if you click onn this your pc is hacked now!!!"
    file_path = f"{settings.BASE_DIR}/main.html"
    reci = ['bhargavbaldaniya777@gmail.com']
    send_mail_attch(subject,message,reci,file_path)
    return render(request,"email.html")
