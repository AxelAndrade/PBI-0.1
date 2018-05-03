from django.shortcuts import render
from .forms import estruc_excel
from .models import DatosComunes 
# Create your views here.
def inicio (request):
	form = estruc_excel(request.POST or None)
	context = {"form":form}


	# if (form.is_value):
	# 	from_data= form.cleaned_data
	# 	# asd= 


	return render (request, "inicio.html", context)  
