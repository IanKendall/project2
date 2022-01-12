from rest_framework import serializers
from catalog.models import WordStructure

class WordStructureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WordStructure
        fields = ('id', 'word', 'phonics', 'links', 'irregulars', 'hash')