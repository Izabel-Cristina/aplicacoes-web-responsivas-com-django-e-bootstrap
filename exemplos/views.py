from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
import re
from .form_exemplos import FormExemplo
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


    if validou_form(email,senha):
        return HttpResponseRedirect("/")
    else:
        if not validou_email(email):
            email_st = 'is-invalid'
        if not validou_senha(senha):
            senha_st = 'is-invalid'

        context = {
            "email": email,
            "senha": senha,
            "email_st": email_st,
            "senha_st": senha_st

        }
        return render(request, 'exemplos/16_forms_parte_i.html', context)

def processa_formulario_v2(request):
    form = FormExemplo()
    if request.method == 'POST':
        form = FormExemplo(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['senha']
            msg = form.cleaned_data["mensagem"]
            return HttpResponse("Formulário validado com sucesso. {} - {} - {}".format(email, pwd, msg))
    return render(request, 'exemplos/17_forms_parte_ii.html', {'form':form})

