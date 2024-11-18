from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from home.models import Shop,Fruit,AdminShop
from django.contrib.auth import authenticate, login as auth_login,logout
# Create your views here.


def home(request):
    shopdata = Shop.objects.all()
    fruitdata = Fruit.objects.all()
    dataShop ={
        'shopdata':shopdata,
        'fruitsdata':fruitdata
        
    }
    return render(request, 'index.html',dataShop)

def fruit(request, shop_id):
    
    shopdata = get_object_or_404(Shop, id=shop_id)
    
    
    fruitdata = Fruit.objects.filter(shop=shopdata)

    user_belongs_to_shop = False
    if request.user.is_authenticated:
        user_belongs_to_shop = AdminShop.objects.filter(user=request.user, shop=shopdata).exists()

    if user_belongs_to_shop:
        return redirect('editfruit',shop_id)

    
    dataShop = {
        'fruitsdata': fruitdata,
        'shop': shopdata
    }

    return render(request, 'fruit.html', dataShop)

def editfruit(request,shop_id):

    shopdata = get_object_or_404(Shop, id=shop_id)
    fruitdata = Fruit.objects.filter(shop=shopdata)

    if 'delete' in request.POST:
        
        fruit = get_object_or_404(Fruit, id=request.POST.get('fruitid'))
        fruit.delete()
        return redirect('editfruit',shop_id)
    elif 'add' in request.POST:

        fn = request.POST.get('fruitname')
        price = request.POST.get('price')
        sn=shopdata

        Fruit.objects.create(shop=sn,fruit_name=fn,price=price)


        return redirect('editfruit',shop_id)



    dataShop = {
        'fruitsdata': fruitdata,
        'shop': shopdata
    }

    return render(request, 'editfruit.html', dataShop)










def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid login credentials.")

    return render(request, 'adlogin.html')

def user_logout(request):
    logout(request)

    return redirect('home')