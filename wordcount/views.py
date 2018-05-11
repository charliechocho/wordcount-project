from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    send_text = request.GET['fulltext']
    word_cnt = send_text.split()

    worddict = {}

    for word in word_cnt:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word] = 1

    new_worddict = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':send_text, 'amt_word':len(word_cnt), 'word_cnt':new_worddict})

def about(request):
    abouttext = """
        This is a little project I'm undertaking as part
        of the Django2 training I'm currently taking!
        What this page does is let you copy text into the
        text area on the hompage and by pressing the Count
        button it will count the amounts of words and also
        let you know how many times each unique word is used
        throughout the text!
        Enjoy!!
        /Mattias
        """
    return render(request, 'about.html', {'sndabouttext':abouttext})
