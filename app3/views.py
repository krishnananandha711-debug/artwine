from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils import timezone
from django.contrib import messages


# Create your views here.
def home(re):
    return render(re,'home.html')
def registeration(re):
    return render(re,'registeration.html')
def register(re):
    return render(re,'register.html')
def user_create(re):
    if re.method == 'POST':
        a=re.POST['n1']
        b=re.POST['n2']
        c=re.POST['n3']
        d=re.POST['n4']
        e=re.POST['n5']
        f=re.FILES['n6']
        user_register.objects.create(name=a,email=b,phn_no=c,username=d,password=e,image=f).save()

    return render(re,'register.html')
def artist_page(re):
    artist_id=re.session.get('artid')
    if not artist_id:
        return redirect(login)
    art=artworker.objects.get(name=artist_id)
    return render(re,'artist.html',{'art':art})
def user_page(re):
    user_id=re.session.get('uid')
    if not user_id:
        return redirect(login)
    user=user_register.objects.get(name=user_id)
    return  render(re,'userpage.html',{'user':user})
def login(re):
    if re.method=="POST":
        a=re.POST['n4']
        b=re.POST['n5']
        try:
            data=user_register.objects.get(name=a)
            if data.password==b:
                re.session['uid']=a
                return redirect(user_page)
            else:
                return HttpResponse('invalid login')
        except Exception:
            try:
                art=artworker.objects.get(name=a)
                if art.password==b:
                    re.session['artid']=a
                    return redirect(artist_page)
                else:
                    return HttpResponse('invalid artist')
            except Exception:
                try:
                    craft=craftworker.objects.get(name=a)
                    if craft.password==b:
                        re.session['craftid']=a
                        return redirect(craftworker_page)
                    else:
                        return HttpResponse('invalid craftworker')
                except Exception:
                    if a=="admin" and b=="admin":
                       re.session['aid']=a
                       return redirect(admin_page)

    return render(re,'login.html')
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = user_register.objects.get(email=email)
        except:
            messages.info(request,"Email id not registered")
            return redirect(forgot_password)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user=user, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
            # return render(request, 'emailsent.html')
        except:
            messages.info(request,"Network connection failed")
            return redirect(forgot_password)

    return render(request, 'forgot.html')

def reset_password(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    # usr = User.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')
        if repeat_password == new_password:
            password_reset.user.password=new_password
            password_reset.user.save()
            # password_reset.delete()
            return redirect(login)
    return render(request, 'reset.html',{'token':token})




def admin_page(re):
    return render(re,'adminpage.html')
def view_user(re):
    data=user_register.objects.all()
    return render(re,'viewuser.html',{'data':data})
def search_user(re):
    if re.method == 'POST':
        a=re.POST['n1']
        data=user_register.objects.filter(name=a)
        return render(re,'search.html',{'data':data})
    return render(re,'search.html')
def delete_user(re,id):
    data=user_register.objects.get(pk=id)
    data.delete()
    return redirect(view_user)
def artist_create(re):
    if re.method == 'POST':
        a=re.POST['a1']
        b=re.POST['a2']
        c=re.POST['a3']
        d=re.POST['a4']
        e=re.POST['a5']
        f=re.FILES['a6']
        g=re.FILES['a7']
        artworker.objects.create(name=a,phn_no=b,address=c,username=d,password=e,image=f,id_proof=g).save()

    return render(re,'artist_register.html')
def view_artist(re):
    data=artworker.objects.all()
    return render(re,'viewartist.html',{'data':data})
def delete_artist(re,id):
    data=artworker.objects.get(pk=id)
    data.delete()
    return redirect(view_artist)
def userview_artist(re):
    data=artworker.objects.all()
    return render(re,'userview_artist.html',{'data':data})
def view_artprofile(re):
        aname=re.session['artid']
        data=artworker.objects.get(name=aname)
        return render(re,'artistprofile.html',{'data':data})

def search_artworker(re):
    if re.method == 'POST':
        a=re.POST['n1']
        data=artworker.objects.filter(address=a)
        return render(re,'search_artworker.html',{'data':data})
    return render(re,'search_artworker.html')
def craft_create(re):
    if re.method == 'POST':
        a=re.POST['c1']
        b=re.POST['c2']
        c=re.POST['c3']
        d=re.POST['c4']
        e=re.POST['c5']
        f=re.FILES['c6']
        craftworker.objects.create(name=a,phn_no=b,address=c,username=d,password=e,image=f).save()

    return render(re,'craft_register.html')

def view_craft(re):
    data=craftworker.objects.all()
    return render(re,'viewcraft.html',{'data':data})
def delete_craft(re,id):
    data=craftworker.objects.get(pk=id)
    data.delete()
    return redirect(view_craft)
def craftworker_page(re):
    craft_id=re.session.get('craftid')
    if not craft_id:
        return redirect(login)
    craft=craftworker.objects.get(name=craft_id)
    return render(re,'craftworker.html',{'craft':craft})
def userview_craft(re):
    data=craftworker.objects.all()
    return render(re,'userview_craft.html',{'data':data})

def search_craftworker(re):
    if re.method == 'POST':
        a=re.POST['n1']
        data=craftworker.objects.filter(address=a)
        return render(re,'search_craftworker.html',{'data':data})
    return render(re,'search_craftworker.html')
def artproduct_create(re):
    if re.method == 'POST':
        a=re.POST['p1']
        b=re.POST['p2']
        c=re.POST['p3']
        d=re.POST['p4']
        e=re.POST['p5']
        f=re.POST['p6']
        g=re.POST['p7']
        h=re.POST['p8']
        i=re.FILES['p9']
        artproduct.objects.create(title=a,description=b,category=c,artistname=d,created_date=e,size=f,price=g,quantity=h,image=i).save()

    return render(re,'artproduct.html')
def view_artproduct(re):
    if 'artid' in re.session:
        artist_id=re.session['artid']
        data=artproduct.objects.filter(artistname=artist_id)
        return render(re,'view_artproduct.html',{'data':data})
def update_artproduct(re,id):
    data=artproduct.objects.get(pk=id)
    if re.method ==  'POST':
        s=sampleform2(re.POST,re.FILES,instance=data)
        if s.is_valid():
            s.save()
            return  redirect(view_artproduct)
    else:
        s=sampleform2(instance=data)
    return render(re,'update_artproduct.html',{'form':s,'d':data})
def userview_artproduct(re,id):
        data=artproduct.objects.filter(artistname=id)
        return render(re,'userview_artproduct.html',{'data':data})
def user_search_artworker(re):
    if re.method == 'POST':
        a=re.POST['n1']
        data=artworker.objects.filter(address=a)
        return render(re,'user_search_artworker.html',{'data':data})
    return render(re,'user_search_artworker.html')


def user_profile(re):
    uname = re.session['uid']
    data = user_register.objects.get(name=uname)
    return render(re, 'user_profile.html', {'data': data})
def update_userprofile(re,id):
    data=user_register.objects.get(pk=id)
    if re.method ==  'POST':
        s=sampleform4(re.POST,re.FILES,instance=data)
        if s.is_valid():
            s.save()
            return  redirect(user_profile)
    else:
        s=sampleform4(instance=data)
    return render(re,'update_userprofile.html',{'form':s,'d':data})
def craft_profile(re):
    cname = re.session['craftid']
    data = craftworker.objects.get(name=cname)
    return render(re,'craftprofile.html',{'data':data})
def craftproduct_create(re):
    if re.method == 'POST':
        a=re.POST['cr1']
        b=re.POST['cr2']
        c=re.POST['cr3']
        d=re.POST['cr4']
        e=re.POST['cr5']
        f=re.POST['cr6']
        g=re.POST['cr7']
        h=re.POST['cr8']
        i=re.FILES['cr9']
        craftproduct.objects.create(title=a,description=b,category=c,artistname=d,created_date=e,size=f,price=g,quantity=h,image=i).save()

    return render(re,'craftproduct.html')
def view_craftproduct(re):
    if 'craftid' in re.session:
        craftworker_id=re.session['craftid']
        data=craftproduct.objects.filter(artistname=craftworker_id)
        return render(re,'view_craftproduct.html',{'data':data})
def update_craftproduct(re,id):
    data=craftproduct.objects.get(pk=id)
    if re.method ==  'POST':
        s=sampleform3(re.POST,re.FILES,instance=data)
        if s.is_valid():
            s.save()
            return  redirect(view_craftproduct)
    else:
        s=sampleform3(instance=data)
    return render(re,'update_craftproduct.html',{'form':s,'d':data})
def userview_craftproduct(re,id):
        data=craftproduct.objects.filter(artistname=id)
        return render(re,'userview_craftproduct.html',{'data':data})
def adminview_craft_profile(re,id):
        data = get_object_or_404(craftworker,id=id)
        return render(re,'admin_craftprofile.html',{'data':data})
def adminview_craftproduct(re,id):
    data=craftproduct.objects.filter(artistname=id)
    return render(re,'adminview_craftproduct.html',{'data':data})
def adminview_art_profile(re, id):
    data = get_object_or_404(artworker,id=id)
    return render(re, 'adminview_artprofile.html', {'data': data})


def adminview_artproduct(re, id):
    data = artproduct.objects.filter(artistname=id)
    return render(re, 'adminview_artproduct.html', {'data': data})
def user_search_craftworker(re):
    if re.method == 'POST':
        a=re.POST['n1']
        data=craftworker.objects.filter(address=a)
        return render(re,'user_search_craftworker.html',{'data':data})
    return render(re,'user_search_craftworker.html')
def adminview_userprofile(re,id):
    data = user_register.objects.filter(id=id)
    return render(re,'adminview_userprofile.html',{'data':data})

def addtocart(re,pid,ptype):
    if 'uid' not in re.session:
        return HttpResponse('please login')
    username=re.session['uid']
    user=user_register.objects.get(username=username)
    if ptype == "art":
        product=artproduct.objects.get(id=pid)



        item=cart.objects.filter(user_details=user,art_product=product).first()
        if item:
            item.total_quantity+=1
            item.total_price=item.total_quantity * product.price
            item.save()
        else:

            cart.objects.create(user_details=user,art_product=product,total_quantity=1,total_price=product.price)

        return HttpResponse('art product added')
    elif ptype == "craft":
        product = craftproduct.objects.get(id=pid)

        item = cart.objects.filter(user_details=user, craft_product=product).first()
        if item:
            item.total_quantity += 1
            item.total_price = item.total_quantity * product.price
            item.save()
        else:

            cart.objects.create(user_details=user, craft_product=product, total_quantity=1, total_price=product.price)

        return HttpResponse('craft product added')
def view_cart(re):
    if 'uid' not in re.session:
        return HttpResponse("please login first")
    user=user_register.objects.get(username=re.session['uid'])
    items=cart.objects.filter(user_details=user)
    total=sum(item.total_price or 0 for item in items)
    return render(re,'view_cart.html',{'item':items,'total':total})
def addtowishlist(re,pid,ptype):
    if 'uid' not in re.session:
        return HttpResponse('please login')
    username=re.session['uid']
    user = user_register.objects.get(username=username)
    if ptype == "art":
        product=artproduct.objects.get(id=pid)
        existing = wishlist.objects.filter(user_details=user,art_product=product).first()
    else:
        product=craftproduct.objects.get(id=pid)
        existing=wishlist.objects.filter(user_details=user,craft_product=product).first()
    if existing:
        return  HttpResponse("already in favorites")
    if ptype == "art":
        wishlist.objects.create(user_details=user,art_product=product)
    else:
        wishlist.objects.create(user_details=user,craft_product=product)
    return  HttpResponse("added to favorites")


def view_wishlist(re):
    if 'uid' not in re.session:
        return HttpResponse('please login')
    user=user_register.objects.get(username=re.session['uid'])
    items=wishlist.objects.filter(user_details=user)
    return render(re,'view_wishlist.html',{'item':items})
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse

def move_to_cart(request, wid):
    if 'uid' not in request.session:
        return HttpResponse("Please login")

    user = get_object_or_404(user_register, username=request.session['uid'])
    wish_item = get_object_or_404(wishlist, id=wid, user_details=user)

    # ---------- ART PRODUCT ----------
    if wish_item.art_product:
        cart_item, created = cart.objects.get_or_create(
            user_details=user,
            art_product=wish_item.art_product,
            defaults={
                'total_quantity': wish_item.product_quantity,
                'total_price': wish_item.product_price
            }
        )

        if not created:
            cart_item.total_quantity += wish_item.product_quantity
            cart_item.total_price += wish_item.product_price
            cart_item.save()

    # ---------- CRAFT PRODUCT ----------
    elif wish_item.craft_product:
        cart_item, created = cart.objects.get_or_create(
            user_details=user,
            craft_product=wish_item.craft_product,
            defaults={
                'total_quantity': wish_item.product_quantity,
                'total_price': wish_item.product_price
            }
        )

        if not created:
            cart_item.total_quantity += wish_item.product_quantity
            cart_item.total_price += wish_item.product_price
            cart_item.save()

    # ---------- REMOVE FROM WISHLIST ----------
    wish_item.delete()

    return redirect('view_cart')


def increment(re,cid):
    if 'uid' not in re.session:
        return HttpResponse("please login first")
    item=cart.objects.get(id=cid)
    item.total_quantity += 1
    if item.art_product is not None:
        price=item.art_product.price
    elif item.craft_product is not None:
        price=item.craft_product.price
    else:
        return HttpResponse("product not found")
    item.total_price=item.total_quantity * price
    item.save()
    return redirect('view_cart')
def decrement(re,cid):
    if 'uid' not in re.session:
        return HttpResponse("please login first")
    item=cart.objects.get(id=cid)
    if item.total_quantity > 1:
        item.total_quantity -= 1
        if item.art_product is not None:
            price=item.art_product.price
        elif item.craft_product is not None:
            price=item.craft_product.price
        else:
            return HttpResponse("product not found")
        item.total_price=item.total_quantity * price
        item.save()
    else:
        item.delete()
    return redirect('view_cart')

def checkout(re):
    if 'uid' not in re.session:
        return HttpResponse('please login')
    user=user_register.objects.get(username=re.session['uid'])
    items=cart.objects.filter(user_details=user)
    total=sum(item.total_price for item in items)
    return render(re,'checkout.html',{'user':user,'items':items,'total':total})

import razorpay
def place_order(re):
    if 'uid' not in re.session:
        return redirect('login')

    username = re.session['uid']
    user = user_register.objects.get(username=username)
    items = cart.objects.filter(user_details=user)

    if not items:
        return HttpResponse("Cart is empty")

    total = sum(item.total_price for item in items)
    total_paise = int(total * 100)

    if re.method == 'POST':
        address = re.POST['order_address']



        client = razorpay.Client(
            auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))

        payment = client.order.create({
            'amount': total_paise,
            'currency': 'INR',
            'payment_capture': '1'
        })

        # Store in session for verification after payment
        re.session['order_data'] = {
            'user': username,
            'address': address,
            'total': total,
            'razorpay_order_id': payment['id']
        }

        return render(re, 'pay_now.html', {
            'payment': payment,
            'user': user,
            'items': items,
            'total': total,

        })

    return redirect('checkout')

def payment_success(re):
    if 'order_data' not in re.session:
        return  HttpResponse('invalid session')
    data=re.session['order_data']
    user=user_register.objects.get(username=data['user'])
    items=cart.objects.filter(user_details=user)

    order=Order.objects.create(
        user=user,
        address=data['address'],
        total_amount=data['total']
    )
    for item in items:
        if item.art_product:
            orderitem.objects.create(
                order=order,
                art_product=item.art_product,
                quantity=item.total_quantity,
                price=item.art_product.price
            )

            # For CRAFT product
        elif item.craft_product:
            orderitem.objects.create(
                order=order,
                craft_product=item.craft_product,
                quantity=item.total_quantity,
                price=item.craft_product.price
            )
    items.delete()
    del re.session['order_data']

    return render(re,'order_success.html',{'order':order})

from django.utils import timezone
from datetime import timedelta
def order_details(re):
    username = re.session['uid']
    user = user_register.objects.get(username=username)

    orders = Order.objects.filter(user=user)
    q = re.GET.get('q', '')
    status = re.GET.get('status', '')
    date_filter = re.GET.get('date_filter', '')

    if q:
        orders = orders.filter(id__icontains=q)

    if status:
        orders = orders.filter(status__iexact=status)

    if date_filter == '30':
        thirty_days_ago = timezone.now() - timedelta(days=30)
        orders = orders.filter(date__gte=thirty_days_ago)

    return render(re, 'order.html', {'orders':orders})

def admin_orders(request):
    orders = Order.objects.all().order_by('-id')

    return render(request, 'admin_orders.html', {'orders': orders})
def update_order_status(request, oid):
    order = Order.objects.get(id=oid)

    if request.method == "POST":
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        return redirect('admin_orders')

    return render(request, 'update_order_status.html', {'order': order})











def samform(re):
    if re.method=='POST':
        s=sampleform(re.POST,re.FILES)
        if s.is_valid():
            print('success')
            s.save()
            return HttpResponse('data saved')
    s=sampleform()
    return  render(re,'book_forms.html',{'data':s})

def view_profile(re):
    aname = re.session['artid']
    data = artworker.objects.get(name=aname)
    return render(re, 'artistprofile.html', {'data': data})
def update_artdata(re,id):
    data=artworker.objects.get(pk=id)
    if re.method ==  'POST':
        s=sampleform(re.POST,re.FILES,instance=data)
        if s.is_valid():
            s.save()
            return  redirect(view_artprofile)
    else:
        s=sampleform(instance=data)
    return render(re,'update_art.html',{'form':s,'d':data})
def update_craftdata(re,id):
    data=craftworker.objects.get(pk=id)
    if re.method ==  'POST':
        s=sampleform1(re.POST,re.FILES,instance=data)
        if s.is_valid():
            s.save()
            return  redirect(craft_profile)
    else:
        s=sampleform1(instance=data)
    return render(re,'update_craft.html',{'form':s,'d':data})
def artist_viewuser(re):
    data=user_register.objects.all()
    return render(re,'artist_viewuser.html',{'data':data})
def craftworker_viewuser(re):
    data=user_register.objects.all()
    return render(re,'craftworker_viewuser.html',{'data':data})

def send_feedback(re):
    if 'uid' not in re.session:
        return redirect("login")
    user = user_register.objects.get(username=re.session['uid'])

    if re.method == "POST":
        message = re.POST.get("message")

        Feedback.objects.create(user=user,message=message)
        return redirect("feedback_success")
    return render(re,'send_feedback.html')
def feedback_success(re):
    return render(re,'feedback_success.html')
def admin_required(view_function):
    def wrapper(re,*args,**kwargs):
        if re.session.get("is_admin") !=True:
            return redirect('view_feedbacks')
        return view_function(re,*args,**kwargs)
    return wrapper
def view_feedbacks(re):
    feedbacks = Feedback.objects.all()
    return render(re,'view_feedbacks.html',{'feedbacks':feedbacks})
def reply_feedback(re,feedback_id):
    feedback = get_object_or_404(Feedback,id=feedback_id)

    if re.method == "POST":
        feedback.reply = re.POST.get("reply")
        feedback.save()
        return redirect("view_feedbacks")
    return render(re,'reply_feedback.html',{'feedback':feedback})
def my_feedbacks(re):
    if 'uid' not in re.session:
        return redirect("login")
    user = user_register.objects.get(username=re.session['uid'])
    feedbacks = Feedback.objects.filter(user=user)

    return render(re,'my_feedback.html',{'feedbacks':feedbacks})







def logout(re):
    if 'uid' in re.session and 'aid' in re.session:
        re.session.flush()
        return redirect('home')
    return redirect('logout')



