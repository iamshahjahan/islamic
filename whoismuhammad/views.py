from django.shortcuts import render
from django.http import HttpResponse	

from whoismuhammad.models import Hadith

# Create your views here.

def index(request):

	hadiths = Hadith.objects.all()

	return render(request,"whoismuhammad/index.html",{'hadiths' : hadiths,'length_hadith':len(hadiths)})


