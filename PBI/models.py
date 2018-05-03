from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)


class UserManger(BaseUserManager):
	def create_user(self, USUARIO, NOMBRE_APELLIDO, DNI, password=None, is_active=True, is_staff=True, is_admin=True):
		if not USUARIO:
			raise ValueError("Se debe tener un usuario")
		if not password:
			raise ValueError("El usuario debe tener Password")
		if not DNI:
			raise ValueError("EL usuario debe tener un DNI")	
		
		user_obj = self.model(
			
			USUARIO = self.normalize_email(USUARIO),
			NOMBRE_APELLIDO = NOMBRE_APELLIDO,
			DNI = DNI 
		)

		user_obj.set_password(password) #cambia la pass
		user_obj.staff = is_staff 
		user_obj.admin = is_admin 
		user_obj.active = is_active 
		user_obj.save(using=self._db)
		return user_obj

	def create_staffuser(self, USUARIO, NOMBRE_APELLIDO, DNI, password=None):
		user = self.create_user(
			USUARIO,
			NOMBRE_APELLIDO,
			DNI,
			password = password,
			is_staff = True

		)
		return user

	def create_superuser(self, USUARIO, NOMBRE_APELLIDO, DNI, password=None):
		user = self.create_user(
			USUARIO,
			NOMBRE_APELLIDO,
			DNI,
			password = password,
			is_staff = True,
			is_admin = True
		)
		return user

class User(AbstractBaseUser):
	USUARIO = models.CharField(max_length=255, unique=True)
	NOMBRE_APELLIDO = models.CharField(max_length=255, blank=True, null=True)
	DNI = models.CharField(max_length=12, unique=True, blank=True, null=True)
	active = models.BooleanField(default=True) #para logearse
	staff = models.BooleanField(default=False) #usuario base
	admin = models.BooleanField(default=False) #usuario admin
	timestamp = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'USUARIO'
	#USUARIO y pass son requeridos
	REQUIRED_FIELDS = ['DNI', 'NOMBRE_APELLIDO']

	objects = UserManger()

	def __str__ (self):
		return self.USUARIO
	def get_full_name(self):
		return self.USUARIO
	def get_short_name(self):
		return self.USUARIO
	def has_perm(self, perm, obj=None):
		return True
	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.staff
	@property
	def is_admin(self):
		return self.admin
	@property
	def is_active(self):
		return self.active










# Create your models here.
class Tipo(models.Model):
	"""docstring for Tipo"""
	DESCRIPCION=models.CharField(max_length=100)
	def __str__(self):
		return self.DESCRIPCION
		
class Padrones(models.Model):
	NOMBREPADRON=models.CharField(max_length=60)
	def __str__(self):
		return self.NOMBREPADRON

class DatosComunes(models.Model):
	NOMBRE_APELLIDO=models.CharField(max_length=100)
	FECHA_NACIMIENTO=models.DateField(null=True)
	TIPO_DOCUMENTO=models.CharField(max_length=20)
	NUMERO_DOCUMENTO=models.CharField(max_length=20)
	def __str__(self):
		return self.NOMBRE_APELLIDO

class Domicilio(models.Model):
	CALLE=models.CharField(max_length=100)
	NUMERO=models.CharField(max_length=60)
	PISO=models.CharField(max_length=60)
	DEPARTAMENTO=models.CharField(max_length=60)
	LOCALIDAD=models.CharField(max_length=60)
	PADRON=models.ForeignKey(Padrones)
	PERSONA=models.ForeignKey(DatosComunes)

class Automotores(models.Model):
	CUIL=models.CharField(max_length=100)
	MATRICULA=models.CharField(max_length=100)
	MATRICULA_ANTERIOR=models.CharField(max_length=100)
	MARCA=models.CharField(max_length=100)
	MODELO=models.CharField(max_length=100)
	PERSONA=models.ForeignKey(DatosComunes)

class Comercio(models.Model):
	COMERCIO_ID=models.CharField(max_length=100)
	NOMBRE_FANTASIA=models.CharField(max_length=100)
	DOMICILIO_COMERCIO=models.CharField(max_length=100)
	PERSONA=models.ForeignKey(DatosComunes)

class DatosEspecificos(models.Model):
	DESCRIPCION=models.CharField(max_length=100)
	TIPO_DATO=models.ForeignKey(Tipo)
	FECHA_IMPORTACION=models.CharField(max_length=100)
	PADRON=models.ForeignKey(Padrones)
	PERSONA=models.ForeignKey(DatosComunes)

