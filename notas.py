'''
python manage.py runserver PUERTO //iniciar servidor

python manage.py startapp NOMBRE // para crear una nueva 'app' es decir una especie de modulo

en views podemos enviar archivos HTML

(dentro de myapp>views)// devuelve simplemente un texto hello world
from django.http import HttpResponse
def hello(request): 
    return HttpResponse("<puedo poner etiquetas>texto")

puedo crear en main un archivo urls.py para no tener que definirlo n el urls.py del fwebsite
from django.urls import path
from . import views //para importar las funciones
urlpatterns = [
    path('ruta',funcion)
]
y deberia importarlo en urls.py del fwebsite
from django.ulrs import path,include

(dentro de fwebsite>urls.py)
from main.views import hello
path('ruta', hello) 
path('ruta',include('rtuas que quiero importar //main.urls'))

en main > models

creo una tabla
class Project(models.Model):
    name = models.CharField(max_length=Number)
    
class Task(models.Model):
    name = models.CharField(max_length=Number)
    desc = models.textField()
    project = models.Foreignkey(Project, on_delete = models.CASCADE) //para agregar una foreign key que relacione las taks con un proyecto
    
    
a todas las tablas debo registrarlas en fwebsite > settings
INSTALLED_APPS = [
    [...]
    'myapp'
]

una vez hecho esto deberia hacer las migraciones a la base de datos
python manage.py makemigrations (opcional)nombre de la carpeta

puedo abrir una shell de django con python manage.py shell

from main.models import TABLAS(Project en este caso)
p=Project(name="aplicacion movil") //crea un proyecto llamado aplicacion movil
p.save() //lo guarda

Project.object.all() //devuelve todos los datos de la tabla
Project.object.get(parametro a buscar ej id=1, name="nombre", etc)

para consultar todas las tarea que le pertenezcan al project con id 1
p.task_set.all()
p.tast_set.create(name="nombre")

en urls de main

path('ruta/<str:nombre_variable_que_quiero_obtener>', views.funcion) //para peticiones get

 en views tambien de main
 
def hello(request,nombre_variable_que_quiero_obtener): //al hacer esto, SI O SI necesito pasar la variable al acceder a la ruta
    print(nombre_variable_que_quiero_obtener)
    return HttpResponse("<etiqueta>Texto %s" %nombre_variable_que_quiero_obtener) //esto va a remplazar %s por el texto que tenga nombre_variable_que_quiero_obtener

from .models import Project
from django.http import JsonReponse

def projects(request): //debo convertirlo a una lista
    projects = list(Project.object.values())
    return JsonResponse(projects, safe=false)
    
from django.shortcuts import get_object_or_404

def tasks(req,id):
    //task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)
    
en main admin.py

from .models import Project, Task

admin.site.register(Project)

en models para ver correctamente la informacion

clas Project(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        
en main debo crear la carpeta templates, en donde voy a poner todos mis archivos html y css

en views.py de main 
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


para poder mandar variables a html
definida la variable en el def index
def index(request):
    title = 'cosa'
    projects = Project.objects.all()
    return render(request,'index.html',{
        variable_a_pasar: projects
    })


en html puedo poner dentro de una etiqueta {{variable_a_pasar}}
ya que el framework lo permite asi hacerlo, ya que es un template engine que usa jinja

JINJA LOOPS
{% for variable in projects %} //projects ya es una variable_a_pasar

<h1>{{variable.name}}</h1>

{% endfor %}

puedo hacer condicionales en jinja, ejemplo si task tuviese un booleano Done

en el bucle de task poodria hacer

{% for task in tasks %}

<h1>{{task.title}} - {{task.project.name}}</h1>

{% if task.done == True %}
<p>tarea pendiente</p>
{% else %}
<p>tarea realizada</p>
{% endif %}

etiqueta compuesta
<h1>{% if task.done == False%}Cosa{% else %}Otra cosa{% endif %} {{task.title}}</h1>

<h3>{{task.description}}</h3>

{% endfor %}

templates transferibles //template inheritance

debo crear un archivo.html con los elementos que van a ser 'repetidos' como un navbar

en base despues de escribir el codigo debo poner

{% block content %}
{% endblock %}

y en el archivo a importar
{% extends 'archivo.html'%}
{% block content %}  
codigo html
{% endblock %}

formularios

lo mejor es crear un archivo .py
from django import forms

class CreateNewTask(forms.Form): //esto es para enviarlo al html, y el html lo va a interpretar y transformarlo, no va a enviarlo al servidor
    title = forms.CharField(label="Titulo de la Tarea", max_length=200)
    description = forms.CharField(label="descripcion de la tarea", widget=forms.Textarea)
    
en views.py
import .forms import CreateNewTask

def create_task(request):
    return render(request, 'create_task.html',{
        'form': CreateNewTask() //esto nos va a permitir generar un formulario en html
    })

pasandoselo mediante jinja al html create_Task.html

<form actions> //tal cual como esta asi envia todo mediante una peticion GET en la url
    {{form.as_p}} //el as p simplemente mete cada coso dentro de una etiqueta p
    <button>
        save
    </button>
</form>

y asi mismo puedo ver lo que me da el get en la funcion create_Task con un
print(request.get)
o tambien puedo hacer print(request.GET['clave']) para ver o almacenar una calve en especifico

ya directamente para crear la tarea es simple
Task.object.create(title=request.GET['title'],description=request.GET['description'],projectkey=1) //crea una tarea en el proyecto 1

pero por supuesto siempre deberia enviar las cosas mediante POST

en el <form method=post>

deberia hacer una comprobacion para manejar las peticiones get y post en views.py>create_task

if request.method = get
    que se renderize la interfaz, return render(request, 'a.html',{'form': CreateNewTask()})
    
else:
    Task.object.create(title=request.POST['title'],description=request.POST['description'],project_id=2)
    return redirect('tasks/')
    
//ahora esto deberia funcionar tanto en get como en post
para evitar problemas de estafa django agrega seguridad, en la etiqueta <form method=POST> deberia ademas agregar
{% csrf_token %}

crear un projecto con un formulario POST

def create_project(request):
    return render(request, 'projects/create_project.html')
    
puedo generar nombres para las urls main>urls.py
urlpatterns = [
    path('', views.index, name='index') con esto internamente ya no tengo que hacer la redireccion en codigo, puedo poner el nombre, para que solo la ruta quede en el path y no tener que hacerlo y cambiarlo en cada linea de codigo cada vez que lo necesite
]

para hacer esto tambien en html tengo que hacerlo con jinja {% url 'nombre' %}

los contenidos estaticos static son los que no cambian como css imagenes audio, pdf, js

en settings.py esta especificado donde se guardan los archivos estaticos
y para cargar una imagen por ejemplo en jinja tengo que usar img src={% static 'url'%}

en la carpeta main debo crear la carpeta static

y en el archivo html ademas tengo que hacer 
{% load static %}
en el html tambien, en el head tengo que especificar de la misma forma el archivo css
link rel=stylesheet href="{% static 'css/archivo.css' %}" //suponemos que el load statics esta siempre arriba de todo y dentro de la carpeta main static existe una carpeta llamada css
    
'''