from django.shortcuts import render
from django.views import View
from bancoDeDados.models import area,local,cargaTipo,carga
from bancoDeDados.forms import cargaForm

# Create your views here.
class paginaSimples(View):
    template_name = 'home.html'
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name,{})

class bancoDeDados(View):
    template_name = 'bancoDeDados.html'
    listaObjetos ={ 'obj' : area.objects.filter(chaveArea=None)}

    def get(self,request,*args, **kwargs):
        return render(request,self.template_name,self.listaObjetos)

class areaVisualisacao(View):
    template_name = 'area.html'
    
    def get(self,request,id1,*args, **kwargs):
        listaObjetos ={ 'obj' : area.objects.get(id=id1),
                        'subAreas' : area.objects.filter(chaveArea=id1),
                        'locais' : local.objects.filter(chaveLocal=id1) }
        return render(request,self.template_name,listaObjetos)


class localVisualisacao(View):
    template_name = 'local.html'
    
    def get(self,request,id1,id2,*args, **kwargs):
        listaObjetos ={ 'obj' : local.objects.get(id=id2),
                        'cargas' : carga.objects.filter(chaveCarga=id2) }
        return render(request,self.template_name,listaObjetos)

'''
class adicionarCarga(View):
    template_name = 'criarFormulario.html'

    def get(self,request,id1,*args,**kwargs):
        context = {'tipo' : cargaTipo.objects.all(),
                   'local' : local.objects.get(id=id1) }
        return render(request,self.template_name,context)


    def post(self,request,id1,*args, **kwargs):
        print(request.POST)
        context = {'tipo' : cargaTipo.objects.all(),
                   'local' : local.objects.get(id=id1) }
        carga.objects.create(tipoDaCarga=request.POST['tipo'],
                            descricao=request.POST['descricao'],
                            potencia=int(request.POST['potencia']),
                            chaveCarga=local.objects.get(id=id1))

        return render(request,self.template_name,context)
'''
def adicionarCarga(request):
    form = cargaForm(request.POST or None)
    return render(request,'criarFormulariotop.html',{'form':form})     
    ##falta fazer receber e salvar
