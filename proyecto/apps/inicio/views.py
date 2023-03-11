from django.shortcuts import render

def inicio(request):
  context = {'titulo':'Inicio',
             'dato':'Este va a ser la pagina inicial del proyecto'}
  return render(request,'inicio.html', context)
