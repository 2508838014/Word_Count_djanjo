# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def count(request):
    total_word=request.GET["text"]
    total_word_number=len(total_word)
    word_count={}
    for word in total_word:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    sorted_word = sorted(word_count.items(),key=lambda w:w[1],reverse=True)

    return render(request,'count.html',{'total':total_word_number,'word':total_word,'number':sorted_word})