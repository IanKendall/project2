from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AllWord, Antonym, Synonym, WordStructure
from .serializers import WordStructureSerializer
from rest_framework.decorators import api_view


# Create your views here.

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

class HelloApiView(APIView):
    """Test Api View"""
    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete',
            'Is similar to a traditional Django View',
            'Gives the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

''' class WordDataView(viewsets.ModelViewSet):
    queryset = WordStructure.objects.all().order_by('word')
    serializer_class = WordStructureSerializer '''


class WordDataView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'catalog/worddata_list.html'

    def get(self, request):
        queryset = WordStructure.objects.all()
        return Response({'worddatas': queryset})

# API instructions here
@api_view(['GET', 'POST'])
def worddata_list(request):
    if request.method == 'GET':
        worddatas = WordStructure.objects.all()

        word = request.GET.get('word', None)
        if word is not None:
            worddatas = worddatas.filter(word_icontains=word)

        word_structure_serializer = WordStructureSerializer(worddatas, many=True)
        return JsonResponse(word_structure_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        word_data = JSONParser().parse(request)
        word_serializer = WordStructureSerializer(data=word_data)
        if word_serializer.is_valid():
            word_serializer.save()
            return JsonResponse(word_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(word_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def worddata_detail(request, pk):
    try:
        word = WordStructure.objects.get(pk=pk)
    except WordStructure.DoesNotExist:
        return JsonResponse({'message': 'The word structure does not exist for this Id'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        word_structure_serializer = WordStructureSerializer(word)
        return JsonResponse(word_structure_serializer.data)

    elif request.method == 'PUT':
        word_data = JSONParser().parse(request)
        word_structure_serializer = WordStructureSerializer(word, data=word_data)
        if word_structure_serializer.is_valid():
            word_structure_serializer.save()
            return JsonResponse(word_structure_serializer.data)
        return JsonResponse(word_structure_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        word.delete()
        return JsonResponse({'message': 'Word structure was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
        




