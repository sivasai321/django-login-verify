from linecache import cache
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_http_methods


user='sivasai'
pswd='pass123'
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def login(request):
    if 'uname' in request.session:
        return redirect(to='home')
    if request.method == 'POST':
        
        uname = request.POST['uname']
        password = request.POST['password']
        if len(uname)==0 and len(password)==0:
            messages.info(request,'Enter Valid username and password')
            return render(request, 'login.html')
        else:
            if uname == user:
                if password == pswd:
                    print
                    request.session['uname'] = uname
                    return redirect(to='home')
                else:
                    psmsg = 'Password is incorrect'
                    return render(request, 'login.html', {'psmsg':psmsg})
            else:
                unmsg = 'Username is incorrect'
                return render(request, 'login.html', {'unmsg':unmsg})
                
            
    else:   
        return render(request, 'login.html')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def home(request):
    if 'uname' in request.session:
        pdt1=Product()
        pdt1.name='MacBook Air'
        pdt1.description="MacBook Air with M1 is an incredibly portable laptop — it’s nimble and quick, with a silent, fanless design and a beautiful Retina display."
        pdt1.img='https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/macbook-air-midnight-select-20220606?wid=452&hei=420&fmt=jpeg&qlt=95&.v=1653084303665'
        pdt1.price=119999
        
        pdt2=Product()
        pdt2.name='Air Pods Pro'
        pdt2.description='And what better way to celebrate those powerful buds than with an ad featuring none other than Harry Styles and a nod to Apple'
        pdt2.img='https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/MME73?wid=200&hei=200&fmt=jpeg&qlt=95&.v=1632861342000'
        pdt2.price=20599
        
        pdt3=Product()
        pdt3.name='iPhone 13 Pro'
        pdt3.description='iPhone 13 Pro takes a huge leap forward, bringing incredible speed to everything you do and dramatic new photo and video capabilities.'
        pdt3.img='https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone13pro-digitalmat-gallery-1-202203_GEO_EMEA?wid=364&hei=333&fmt=png-alpha&.v=1645574660318'
        pdt3.price=119900
        
        pdt4=Product()
        pdt4.name='iPad Pro'
        pdt4.description='The ultimate iPad experience. With next-level M1 performance, and fast wireless.'
        pdt4.img='https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/ipadpro11-digitalmat-gallery-1-202111_GEO_IN?wid=364&hei=333&fmt=png-alpha&.v=1635806334000'
        pdt4.price=71900
        
        pdt5=Product()
        pdt5.name='Apple Watch SE'
        pdt5.description='Track all your favourite workouts, like swimming, running, Pilates and Tai Chi'
        pdt5.img='https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/watch-se-digitalmat-gallery-1-202203_GEO_IN?wid=364&hei=333&fmt=png-alpha&.v=1647778278941'
        pdt5.price=29999
        
        pdt6=Product()
        pdt6.name='Apple Homepod mini'
        pdt6.description='Jam-packed with innovation, HomePod mini delivers unexpectedly big sound '
        pdt6.img='https://www.apple.com/v/homepod-mini/g/images/overview/sound_homepod_white__e5a2pshb9l26_large.png'
        pdt6.price=8999
        
        pdts=[pdt1,pdt2,pdt3,pdt4,pdt5,pdt6]
        return render(request, 'home.html',{'pdts':pdts})
    else:
        return redirect(to='login')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    request.session.flush()
    return redirect(to='login')