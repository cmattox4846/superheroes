from django.shortcuts import render
from django.http import HttpResponse

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

def create(request,hero_id):
    create_hero = Superhero.objects.
    context ={
        'create_hero':create_hero
    }
    return render(request,'superheroes/create.html', context)

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






