from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


# Create your models here.

class WordStructure(models.Model):
    """Defines how to pronounce a word, derived from the Model class."""

    # Fields
    word = models.CharField(max_length=30, null=False)
    phonics = models.CharField(max_length=90, null=False, help_text='letter sounds')
    links = models.CharField(max_length=60, null=False, help_text='how letter sounds relate to letters')
    irregulars = models.CharField(max_length=10, null=False, help_text='irregular sounds')
    hash = models.CharField(max_length=20, help_text='word as a number related to consonant sounds')

    # Metadata
    class Meta:
        ordering = ['word', 'phonics']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('word-structure-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.word


class AllWords(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    word = models.CharField(max_length=30, null=False)

    # Metadata
    class Meta:
        ordering = ['word']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('all-words-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.word


class Synonyms(models.Model):
    """connection from WordStructure to AllWords, derived from the Model class."""

    # Fields
    word_structure = models.ForeignKey(WordStructure, on_delete=models.PROTECT)
    all_words = models.ForeignKey(AllWords, on_delete=models.PROTECT)

    # Metadata
    class Meta:
        ordering = ['word_structure', 'all_words']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('synonyms-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.word_structure

    
class Antonyms(models.Model):
    """connection from WordStructure to AllWords, derived from the Model class."""

    # Fields
    word_structure = models.ForeignKey(WordStructure, on_delete=models.PROTECT)
    all_words = models.ForeignKey(AllWords, on_delete=models.PROTECT)

    # Metadata
    class Meta:
        ordering = ['word_structure', 'all_words']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('antonyms-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.word_structure
