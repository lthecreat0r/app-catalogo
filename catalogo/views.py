from django.shortcuts import render, get_list_or_404
from .models import Obra
def index(request):
    context = {
        "obras": obras,
    }

    return render(
        request,
        "catalogo/index.html",
        context
    )



def detalhes(request, id):

    obra = get_object_or_404(Obra, id=id)

    context = {
        "obra": obra_encontrada,
    }

    return render(
        request,
        "catalogo/detalhes.html",
        context
    )