from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context ={
        'all_heroes':all_heroes
    }
    return render(request,'superheroes/index.html', context)

def detail(request,hero_id):
    single_hero = Superhero.objects.get(pk = hero_id)
    context ={
        'single_hero':single_hero
    }
    return render(request,'superheroes/detail.html', context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catch_phrase = request.POST.get('catchphrase')

        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability = primary, secondary_ability= secondary, catch_phrase = catch_phrase)
        new_hero.save()

        return HttpResponseRedirect(reverse('superheroes:index'))

    else:
        return render(request,'superheroes/create.html')

def edit(request,hero_id):
    edit_hero = Superhero.objects.get(pk = hero_id)
    context ={
        'edit_hero':edit_hero
    }
    return render(request,'superheroes/edit.html', context)


def delete(request,hero_id):
    delete_hero = Superhero.objects.get(pk = hero_id)
    context ={
        'delete_hero':delete_hero
    }
    return render(request,'superheroes/delete.html', context)






