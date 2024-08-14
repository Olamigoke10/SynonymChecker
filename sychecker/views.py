from django.shortcuts import render
from .forms import SynonymForm
from PyDictionary import PyDictionary

dictionary = PyDictionary()

# Create your views here.
def synonyms_view(request):
    synonyms = None
    if request.method == "POST":
        form = SynonymForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            synonyms = dictionary.synonym(word)
        else:
            form = SynonymForm()
    return render(request, 'base/main.hmtl', {'form':form, 'synonyms':synonyms})