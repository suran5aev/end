from django.shortcuts import render,redirect,get_object_or_404
from apps.base.models import Base, Popular_category,Our_chef,News, Our_advantages, Menu, Dessert, Sea_Food, BEVERAGE
from apps.telegram.models import Telegram
from apps.telegram.views import get_text
from apps.telegram.forms import PERSONE_CHOISE, TIME_CHOISE
# Create your views here.



def index(request):
    base = Base.objects.latest('id')
    advantages = Our_advantages.objects.all()
    category = Popular_category.objects.all()
    chef = Our_chef.objects.all().order_by('?')[:3]
    news = News.objects.all().order_by('?')[:2]
    menu = Menu.objects.all().order_by('?')[:6]
    dessert = Dessert.objects.all()
    sea_food = Sea_Food.objects.all()
    beve = BEVERAGE.objects.all()

    if request.method == "POST":
        phone = request.POST.get('phone')
        persone = request.POST.get("persone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        Telegram.objects.create(phone=phone, persone=persone, date=date, time=time)

        get_text(f"""Оставлена заявка 💬:
                 
Номер телефона: {phone}

Количество людей: {persone}

Дата: {date}

Время: {time}
""")
        return redirect('index')

    return render(request, 'base/index-dark.html', {
        'base': base,
        'category': category,
        'chef': chef,
        'news': news,
        'advantages' : advantages,
        'PERSONE_CHOISE': PERSONE_CHOISE,
        'TIME_CHOISE': TIME_CHOISE,
        'menu': menu,
        'dessert':dessert,
        'sea_food':sea_food,
        'beve':beve,
    })
    
def chef_detail(request, id):
    base = Base.objects.latest('id')
    chef = Our_chef.objects.get(id=id)
    return render(request, 'base/chef-details-dark.html', locals())


def dish_detail(request, id):
    base = Base.objects.latest('id')
    menu = Menu.objects.get(id=id)
    dess = Dessert.objects.latest('id')
    sea_food = Sea_Food.objects.latest('id')
    beve = BEVERAGE.objects.latest('id')
    return render(request, 'base/food-menu-2-dark.html', locals())


def errors(request, exeption):
    return render(request, '404/404.html, status=404')
