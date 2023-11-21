
from django.http import JsonResponse
from django.http import HttpResponse
import json

from autenticate.models import articulos
# Create your views here.

from django.core.serializers import serialize

# Obtener la lista de objetos Articulo


# Serializar la lista de objetos a JSON


# Imprimir la cadena JSON resultante



def api(request):
    
    lista = articulos.objects.all()
    cadena_json = serialize('json', lista)

    datos_json = json.loads(cadena_json)
    nuevo_json = []

    for articulo_json in datos_json:
        
        campos = articulo_json['fields']
        nuevo_json.append({
            'id': articulo_json['pk'],
            'title': campos['title'].replace("", ""),
            'price': campos['price'],
            'description': campos['description'],
            'category': campos['category'].replace("", ""),
            'image': campos['image']
        })


    #return HttpResponse("hello<script>console.log("+json.dumps(nuevo_json)+"); console.log(JSON.parse(`"+json.dumps(nuevo_json)+"`))</script>")
    #return HttpResponse("<div id=text></div><script>document.getElementById('text').innerHTML = JSON.parse(`"+json.dumps(nuevo_json)+"`).toString</script>")
    return JsonResponse(json.dumps(nuevo_json), safe=False)