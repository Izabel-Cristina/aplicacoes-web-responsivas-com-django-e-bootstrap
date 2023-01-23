from django.shortcuts import render,HttpResponse

# Create your views here.
def get_bootstrap(request):
    return render(request, 'exemplos/16_forms_parte_I.html')

def processa_formulario_v1(request):
    email = request.POST.get("email")
    password = request.POST.get("senha")
    return HttpResponse("{}----- e-----{}".format(email,password))