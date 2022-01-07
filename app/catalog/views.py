from django.shortcuts import render

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