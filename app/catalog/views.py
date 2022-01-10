from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

from .models import AllWord, Antonym, Synonym, WordStructure

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_wordstructures = WordStructure.objects.all().count()
    num_words = AllWord.objects.all().count()

    context = {
        'num_wordstructures': num_wordstructures,
        'num_words': num_words,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class WordStructureView(generic.ListView):
    model = WordStructure
    paginate_by = 20

class WordStructureDetailView(generic.DetailView):
    model = WordStructure