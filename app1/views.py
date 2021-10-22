from django.shortcuts import render,redirect
from .models import contact as ct
from django.utils.timezone import datetime
from .forms import userCreationForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import service as sc
from .models import orderdetails as od


def home(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        com=request.POST.get("comments")
        time=datetime.now()
        a=ct(name=name,email=email,comments=com)
        a.save()
    bc=od.objects.all()
    for x in bc:
                if str(x.percentage_of_work_complete) =='100' and x.sent_mail!=True:
                            id=x.id
                            ts=od.objects.filter(id=id)
                            subject = 'successfully finished the bike service '
                            message = f'Hi {x.name}, you booked { x.type_of_service} service for your bike{x.type} its completed .So It ready to Delivery'
                            email_from = settings.EMAIL_HOST_USER
                            recipient_list = [str(x.email), ]
                            send_mail( subject, message, email_from, recipient_list )
                            ts.update(sent_mail=True)



    return render(request,"app1/home.html")

def register(request):
     if request.method =='POST':
        form=userCreationForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'welcome to '
            message = f'Hi {request.POST.get("username")}, thank you for registering in bike service.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [str(request.POST.get("email")), ]
            send_mail( subject, message, email_from, recipient_list )
            alter=" you Registered successfully "
            return redirect(("/login"))
        else:
            alter="use password length maximun 8 and password must be complex and use both numeric and alpha charecters or use different username and email"
     else:
        alter="use password length maximun 8 and password must be complex and use both numeric and alpha charecters or use different username and email"
        form=userCreationForm()

     context={"form":form,"alt":alter}
     return render(request,"registration/register.html",context)
@login_required
def dash(request):
    context={}
    return render(request,"app1/show.html",context)
@login_required
def service(request):
    b=sc.objects.all()

    context={"b":b}
    return render(request,"app1/show.html",context)
@login_required
def myorder(request):
    current_user=request.user
    b=od.objects.filter (name=current_user.username)
    mss=''
    for x in b:
        if str(x.percentage_of_work_complete)=="100" and x.sent_mail:
                mss+='Mail already sent your mail Id'
        else:
            mss+=''
    context={"b":b,'ba':mss}
    return render(request,"app1/order.html",context)

@login_required
def bookingform(request,ser):
    scrv=ser
    test=str(scrv)

    a=sc.objects.get(name=test)

    if request.method == 'POST':
        current_user=request.user
        service=request.POST.get("service")
        type=request.POST.get("type")
        amount=request.POST.get("amount")
        payment=request.POST.get("pay")
        time_spend=request.POST.get("time")
        book_date=request.POST.get("slot")
        time=datetime.now()

        a=od(name=request.user,email=current_user.email,type_of_service=service,paid_method=payment,vechile_type=type,order_placed_time=time,booked_slot=book_date,percentage_of_work_complete=0)
        a.save()
        subject = 'successfully finished the bike service Booking '
        message = f'Hi {request.user.username}, you are successfully booked { service } service for your bike{ type } on {book_date}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [str(request.user.email), ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect(("/dashboard/order"))
    context={"sc":a,"t":test}



    return render(request,"registration/test.html",context)






