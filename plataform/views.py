from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Immobile, City, Visit


class HomeListView(ListView):
    model = Immobile

    def get(self, request, *args, **kwargs):
        immobile = Immobile.objects.all()
        cities = City.objects.all()
        min_price = request.GET.get('preco_minimo')
        max_price = request.GET.get('preco_maximo')
        city = request.GET.get('cidade')
        type_immobile = request.GET.getlist('tipo')

        if min_price or max_price or type_immobile or city:
            if not min_price:
                min_price = 0
            if not max_price:
                max_price = 999999
            if not type_immobile:
                type_immobile = ['A', 'C']
            immobile = Immobile.objects.filter(value__gte=min_price).filter(value__lte=max_price).filter(type_immobile__in=type_immobile).filter(city=city)

        context = {
            'immobile': immobile,
            'cities': cities,
        }
        return render(request, 'plataform/home.html', context)
    

class ImmobileDetailView(DetailView):
    model = Immobile

    def get(self, request, *args, **kwargs):
        immobile = get_object_or_404(Immobile, id=kwargs['id'])
        suggestions = Immobile.objects.filter(city=immobile.city).exclude(id=kwargs['id'])[:2]
        
        context = {
            'immobile': immobile,
            'suggestions': suggestions,
        }
        return render(request, 'plataform/detail.html', context)


def schedules_visit(request):
    if request.method == 'POST':
        user = request.user
        day = request.POST.get('dia')
        time = request.POST.get('horario')
        immobile_id = int(request.POST.get('id_imovel'))

        visit = Visit(user=user, day=day, time=time)
        visit.immobile = Immobile.objects.get(id=immobile_id)
        visit.save()
        return redirect('schedules')
    return redirect('home')


class SchedulesListView(LoginRequiredMixin, ListView):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        schedules = Visit.objects.filter(user=request.user)
        return render(request, 'plataform/schedules.html', {'schedules': schedules})


def cancel_schedule(request, id):
    visit = get_object_or_404(Visit, id=id)
    visit.status = "C"
    visit.save()
    return redirect('schedules')
    