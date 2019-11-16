'''
UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ
DESENVOLVIVENTO DO PROJETO G ELETRICA
DESENVOLVEDOR: PAULO AFONSO GASPAR
'''


from django.db import models

# Create your models here.

#cargaTipo: É o modelo  dos tipos de carga possíveis. Ex: luminária, ar condicionado... 
class cargaTipo(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self):
        """String for representing the Model object."""
        return self.nome

#carga: É o modelo das cargas elétricas no ambiente.
class carga(models.Model): 
    #tipoDaCarga: é o tipo da carga. Só pode ser escolhido um dos tipos de carga disponiveis.
    tipoDaCarga = models.CharField(max_length=80, blank=True,
                                  choices = cargaTipo.objects.all().values_list('nome','nome'))
    
    #descricao: descrição dessa carga. Características físicas e de funcionamento.
    descricao = models.CharField(max_length=300)
    #potencia: A Potência em Watts.
    potencia = models.IntegerField() 
    #chaveCarga: marcar o local que a carga esta instalada.
    chaveCarga = models.ForeignKey('local',models.CASCADE)
    #notas: Espaço disponivel para observações sobre a carga. 
    #opcional.
    notas = models.CharField(max_length=300,blank=True,null=True)
    #tempoUsoDiario: Tempo em horas em que a carga está ativada durante o período de 1 dia.
    #opcional.
    tempoUsoDiario = models.FloatField(blank=True,null=True)
    #mediaConsumo: Média de gasto mensal da carga. 
    #opcional.
    mediaConsumo = models.IntegerField(blank=True,null=True)
    #xPosicao e yPositcao: coordenadas da posição da carga na sala.
    #opcional. Será desenvolvido sistema para coordenadas futuramente.
    xPosicao = models.IntegerField(blank=True,null=True)
    yPosicao = models.IntegerField(blank=True,null=True)
    #imagem: foto da carga.
    #opcional.
    imagem = models.ImageField(upload_to='geletrica_data/pictures/',blank=True,null=True)
    #sinalAlerta: marcar caso carga deve ficar sob vistoria especial.
    sinalAlerta = models.BooleanField(default = False)

    def __str__(self):
        """String for representing the Model object."""
        return self.descricao
    


class local(models.Model):
    #nome: nome do local: Ex: A-101
    nome = models.CharField(max_length=80)
    #chaveLocal: marcar a area onde o local pertence
    chaveLocal = models.ForeignKey('area',models.CASCADE)
    #descricao: descrição do local.
    #opcional
    descricao = models.CharField(max_length=300)
    #potenciaProjeto: potencia total de projeto.
    #opcional
    potenciaProjeto = models. IntegerField(blank=True, null=True)

    tensaoCircuitoLuminaria = models. DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    correnteCircuitoLuminaria = models. DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    potenciaCircuitoLuminaria = models. DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    
    #sinalAlerta: marcar caso local deve ficar sob vistoria especial.
    sinalAlerta = models.BooleanField(default = False)

    def __str__(self):
        """String for representing the Model object."""
        return self.nome

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('local-detail', args=[str(self.chaveLocal)])

class area(models.Model):
    #nome: nome do a area: Ex: Bloco A
    nome = models.CharField(max_length=80)
    #chaveArea: Caso seja uma subarea de uma area principal, marcar a area
    chaveArea = models.ForeignKey('self',models.CASCADE,blank=True,null=True)
    #descricao: descrição da area.
    #opcional
    descricao = models.CharField(max_length=300,blank=True,null=True)
    #potenciaProjeto: potencia total de projeto.
    #opcional
    potenciaProjeto = models. IntegerField(blank=True, null=True)
    #sinalAlerta: marcar caso area deve ficar sob vistoria especial.
    sinalAlerta = models.BooleanField(default = False)

    def __str__(self):
        """String for representing the Model object."""
        return self.nome

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('local-detail', args=[str(self.chaveLocal)])



