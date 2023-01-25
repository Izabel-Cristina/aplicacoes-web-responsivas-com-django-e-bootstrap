from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
import re

# Create your views here.
def get_bootstrap(request):
    return render(request, 'exemplos/16_forms_parte_i.html')

#Validar senha:
def validou_senha(senha):
    regex ='^(?=.*[A-Z])(?=.*[!#@$%&])(?=.*[0-9])(?=.*[a-z]).{4,15}$'
    if (re.search(regex,senha)):
        return True
    else:
        return False

def validou_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex,email)):
        return True
    else:
        return False
def validou_form(email,senha):
    if validou_email(email) and validou_senha(senha):
        return True
    else:
        return False


def processa_formulario_v1(request):
    email = request.POST.get("email")
    senha = request.POST.get("senha")

    email_st = 'is_valid'
    senha_st = 'is_valid'

    context = {
        "email": email,
        "senha": senha

    }

    if validou_form(email,senha):
        return HttpResponseRedirect("/")
    else:
       return render(request, 'exemplos/16_forms_parte_i.html', context)


