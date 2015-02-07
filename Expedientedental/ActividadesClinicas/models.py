from django.db import models


# Create your models here.


class interrogatorio(models.Model):
	nombre_paciente	= models.ForeignKey('Nombre.paciente')
	nombre_doctor	= models.ForeignKey('Nombre.medico')
	credencial_paciente = models.ForeignKey('credencial_paciente.paciente')
	ultima_visita_medico = models.CharField(max_length=100, null=False)
	medicamento_ultimos_dos_anios = models.CharField(max_length=100, null=False)
	alergico_a_medicamentos = models.CharField(max_length=100, null=False)
	alergico_a_anestesicos = models.CharField(max_length=100, null=False)
	padece_enfermedades = models.CharField(max_length=100, null=False)
	enfermedad_trasmision_sexual = models.CharField(max_length=100, null=False)
	otra_enfermedad = models.CharField(max_length=100, null=False)
	esta_embarazada = models.CharField(max_length=100, null=False)
	observaciones = models.TextField()
	resumen_clinico = models.TextField()

	


class Odontograma(models.Model):
	class Odontograma
 	id_odonto=model.CharField()
 	id_paciente=model.CharField(foreign_key=True,maxlenght_lenght=5)
 	nomDi=model.CharField(foreignkey=True,maxlenght_lenght=30)

 	def __unicode__(self):
 		pieza="% %"% (self.nomDi)
 		return pieza

 


class Ldiagnosticos(models.Model):
	CIE10=models.CharField(foreign_key=True,max_length=15)
	CDi=models.CharField(primary_key=True,max_length=15)
	nomDi=models.CharField(max_length=30)
	def __unicode__(self):
		CO="% %"%(self.CIE10)
		return CO



class LDPP(models.Model):
	id_paciente=models.CharField(foreign_key=True,max_length=5)
	nom_pacient=models.CharField(foreign_key=True,max_length=50)
	id_med=models.CharField(foreign_key=True, max_length=5)
	codigoDiagnostico=models.CharField(foreign_key=True,max_length=15)
	CIE10=models.CharField(foreign_key=True,max_length=15)
	nomDiagnostico=models.CharField(foreignkey=True,max_length=30)



