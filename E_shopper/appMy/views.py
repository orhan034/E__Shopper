from django.shortcuts import render , get_object_or_404, redirect
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def sepetSay(request):
    if request.user.is_authenticated:
        return ShopBasket.objects.filter(user = request.user)
    else:
        return None

def index(request):
    ganders = Gander.objects.all()
    products = ProductStok.objects.all()
    categorys = Category.objects.all()
    urun_turu = ProductTuru.objects.all()

        
    paginator = Paginator(products, 6) 
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
            "title":"Anasayfa",
            "products":products,
            'categorys':categorys,
            'urun_turu':urun_turu,
            'ganders':ganders,
            "shopbasket": sepetSay(request)
    }
    return render(request, 'index.html', context)

def account(request):
    ganders = Gander.objects.all()
    categorys = Category.objects.all()
    urun_turu = ProductTuru.objects.all()
    product_rasgele = ProductStok.objects.all().order_by('?')[:4]
    products = ProductStok.objects.all()

    paginator = Paginator(products, 6) 
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    products = ProductStok.objects.all()
    query = request.GET.get('query')
    if query:
        products = products.filter(
            Q(product__title__icontains = query) |
            Q(product__brand__icontains = query) |
            Q(product__text__icontains = query) |
            Q(product__slug__icontains = query)
            )


    context = {
            'title':'Ürünler',
            "products":products,
            'categorys':categorys,
            'urun_turu':urun_turu,
            'ganders':ganders,
            'product_rasgele':product_rasgele,
            "shopbasket": sepetSay(request)
        }
    return render(request, 'account.html', context)

def kategory(request, cid):
    ganders = Gander.objects.all()
    products = ProductStok.objects.all()
    categorys = Category.objects.all()
    category = Category.objects.get(slug = cid)
    categoryurun = ProductStok.objects.filter(product__category__slug = cid)
    urun_turu = ProductTuru.objects.all()

    paginator = Paginator(categoryurun, 6) 
    page_number = request.GET.get('page')
    categoryurun = paginator.get_page(page_number)

    context = {
        "title":"Ürünler",
        'category':category,
        'categoryurun':categoryurun,
        "products":products,
        'categorys':categorys,
        'urun_turu':urun_turu,
        'ganders':ganders,
        "shopbasket": sepetSay(request)
    }
    return render(request, 'category.html',context)

def gander(request,gen):
    urun_turu = ProductTuru.objects.all()
    ganders = Gander.objects.all()
    categorys = Category.objects.all()
    genurun = ProductStok.objects.filter(product__gander__slug = gen)

    
    paginator = Paginator(genurun, 6) 
    page_number = request.GET.get('page')
    genurun = paginator.get_page(page_number)

    context = {
        "title":"Ürünler",
        'ganders':ganders,
        'categorys':categorys,
        'genurun':genurun,
        'urun_turu':urun_turu,
        "shopbasket": sepetSay(request)
    }
    return render(request, 'gander.html',context)

def urunTuru(request,uin):

    urun_turu = ProductTuru.objects.all()
    ganders = Gander.objects.all()
    categorys = Category.objects.all()
    urun = ProductStok.objects.filter(product__productTuru__slug = uin)

    
    paginator = Paginator(urun, 6) 
    page_number = request.GET.get('page')
    urun = paginator.get_page(page_number)

    context = {
         "title":"Ürünler",
        'ganders':ganders,
        'categorys':categorys,
        'urun':urun,
        'urun_turu':urun_turu,
        "shopbasket": sepetSay(request)
    }
    return render(request, 'urunturu.html', context)

def detay(request,slug):
    product = get_object_or_404(ProductStok, product__slug = slug)
    prdct = Product.objects.get(slug=slug)
    comments = Comment.objects.filter(product = prdct)
    puan = 0
    if request.method == "POST":
        if request.POST.get('submit')=='sepet':
            size = request.POST.get('size')
            count = int(request.POST.get('count'))
            if product.product.category.slug == 'kiyafet':
                try:
                    prod = SizeLetter.objects.filter(product__slug=slug, size__title=size).get()
                    price_all = prod.price * count

                    shopprod = ShopBasket.objects.filter(user=request.user,sizeletter=prod)
                    if shopprod.exists():
                        shopprod = shopprod.get()
                        shopprod.count += count
                        shopprod.price_all += price_all
                        shopprod.save()
                    else:
                        shopb = ShopBasket(user = request.user, sizeletter = prod, count=count, price_all = price_all )
                        shopb.save()
                    return redirect("/detay/"+ slug +"/")
                except:
                    messages.warning(request, 'Aradığın beden mağazada bulunmamaktadır!')
             
            if product.product.category.slug == 'ayakkabi':
                try:
                    prod = SizeLetter.objects.filter(product__slug=slug, size__title=size).get()
                    price_all = prod.price * count

                    shopprod = ShopBasket.objects.filter(user=request.user,sizeletter=prod)
                    if shopprod.exists():
                        shopprod = shopprod.get()
                        shopprod.count += count
                        shopprod.price_all += price_all
                        shopprod.save()
                    else:
                        shopb = ShopBasket(user = request.user, sizeletter = prod, count=count, price_all = price_all )
                        shopb.save()
                    return redirect("/detay/"+ slug +"/")
                except:
                    messages.warning(request, 'Aradığın beden mağazada bulunmamaktadır!')

            if product.product.category.slug != 'ayakkabi' and product.product.category.slug != 'kiyafet':
                try:
                    prod = SizeLetter.objects.filter(product__slug=slug).get()
                    price_all = prod.price * count

                    shopprod = ShopBasket.objects.filter(user=request.user,sizeletter=prod)
                    if shopprod.exists():
                        shopprod = shopprod.get()
                        shopprod.count += count
                        shopprod.price_all += price_all
                        shopprod.save()
                    else:
                        shopb = ShopBasket(user = request.user, sizeletter = prod, count=count, price_all = price_all )
                        shopb.save()
                    return redirect("/detay/"+ slug +"/")
                except:
                    messages.warning(request, 'Aradığın beden mağazada bulunmamaktadır!')
            return redirect('/detay/'+ slug+'/') 
           
        elif request.POST.get('submit')=="comment":
            title = request.POST.get('title')
            text = request.POST.get('text')
            try:
                star = int(request.POST.get('star'))
            except:
                return redirect('/detay/'+ slug+'/')
           
            comment = Comment(title=title, text=text, 
                              star=star, user=request.user, product=prdct)
            comment.save()
          
            for i in comments:
                puan += i.star 
            prdct.stars = round(puan/len(comments))
            prdct.save()



            return redirect('/detay/'+ slug+'/')


    context = {
        "title":"Ürün Detay",
        'product':product,
        "comments":comments,
        "shopbasket": sepetSay(request)
    }
    return render(request, 'detail.html',context)

def cart(request):

    shopbasket = ShopBasket.objects.filter(user = request.user)

    toplam = 0
    for i in shopbasket:
        toplam +=i.price_all

    if request.method =='POST':
        for k,v in dict(request.POST).items():
            if k != "csrfmiddlewaretoken":
                try:
                    v[0] = int(v[0])
                except:
                    return redirect('cart')
                
                shopb = shopbasket.get(id=k[5:])
                if v[0] == '0':
                    shopb.delete()
                elif v[0] > 0:
                    shopb.count = int(v[0])
                    shopb.price_all = shopb.sizeletter.price * int(v[0])
                    shopb.save()
                else:
                    return redirect('cart')
        return redirect('cart')
    context = {
        "title":"Sepet",
        'shopbasket':shopbasket,
        "toplam":toplam,
    }
    return render(request, 'cart.html', context)

def ShopBasketDelete(request,id):
    shopbasket = ShopBasket.objects.get(id = id)
    shopbasket.delete()
    return redirect('cart')

def contact(request):
    contact = Contact.objects.all()
    if request.method == "POST":
        if request.POST.get("gonder")=="Kaydet":
            name = request.POST.get("name")
            email = request.POST.get("email")
            title = request.POST.get("title")
            text = request.POST.get("text")

            comm = Contact(name=name,email=email,title=title,text=text)
            comm.save()
            return redirect("contact")
    context = {
        "title":"Contact",
        "contact":contact,
        "shopbasket": sepetSay(request)
    }
    return render(request, 'contact.html', context)