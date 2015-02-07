from django.db import models

# Create your models here.


class interrogatorio(models.Model)
	Nombre_paciente	= models.ForeignKey('Nombre.paciente')
	Nombre_doctor	= models.ForeignKey('Nombre.medico')
	#Ap_Paterno	= models.CharField(foreingkey=True,max_length=30)
	#Ap_Materno	= models.CharField(foreingkey=True,max_length=30)
	#Especialidad= models.CharField(foreingkey=True,max_length=40)
	#Nombre		= models.CharField(foreingkey=True,max_length=40)
	#Ap_Paterno	= models.CharField(foreingkey=True,max_length=30)
	#Ap_Materno	= models.CharField(foreingkey=True,max_length=30)

	
class Odontograma
	id_odonto=model.CharField()
	id_paciente=model.CharField(foreign_key=True,maxlenght_lenght=5)
	nom_pacient=model.CharField(foreign_key=True,maxlenght_lenght=50)
	app=model.CharField(foreign_key=True,maxlenght_lenght=50)
	apm=model.CharField(foreign_key=True, maxlenght_lenght=50)
	nomdoc=model.CharField(foreign_key=True,maxlenght_lenght=50)
	appdoc=model.CharField(foreign_key=True,maxlenght_lenght=50)
	FeHo=model.DateTimeField(auto_now_add=True)
	nomPdental=model.CharField(maxlenght_lenght=20)
	CIE10=model.CharField(maxlenght_lenght=15)
	notas=model.TextField()

	def __unicode__(self):
		Odontograma="% %"%(self.id_odonto,nomdoc,nom_pacient)
		return Odontograma


class Ldiagnosticos
	CIE10=model.CharField(foreign_key=True,maxlenght_lenght=15)
	CDi=model.CharField(primary_key=True,maxlenght_lenght=15)
	nomDi=model.CharField(maxlenght_lenght=30)
	def __unicode__(self):
		CO="% %"%(self.CIE10)
			return CO



class LDPP
	id_paciente=model.CharField(foreign_key=True,maxlenght_lenght=5)
	nom_pacient=CharField(foreign_key=True,maxlenght_lenght=50)
	id_med=model.CharField(foreign_key=True, maxlenght_lenght=5)
	CDi=model.CharField(foreign_key=True,maxlenght_lenght=15)
	CIE10=model.CharField(foreign_key=True,maxlenght_lenght=15)
	nomDi=model.CharField(foreignkey=True,maxlenght_lenght=30)


