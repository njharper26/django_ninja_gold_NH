from django.shortcuts import render, redirect
from time import gmtime, strftime

from random import randrange

def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
        request.session['log'] = []

    print request.session['log']
    
    context = {
        'count' : request.session['count'],
        'log' : request.session['log']
    }
    
    return render(request, 'ninja/index.html', context)

def process(request, word):
    print word
    time = strftime("%a, %d %b %Y %I:%M:%p", gmtime())

    if word == 'farm':
        earn = randrange(10, 20 , 1)
        activity = "Earned " + str(earn) + " golds from the Farm!  " + time
    elif word == 'cave':
        earn = randrange(5, 10 , 1)
        activity = "Earned " + str(earn) + " golds from the Cave!  " + time
    elif word == 'house':
        earn = randrange(2, 5 , 1)
        activity = "Earned " + str(earn) + " golds from the House!  " + time
    elif word == 'casino':
        earn = randrange(-50, 50 , 1)
        if earn >= 0:
            activity = "Earned " + str(earn) + " golds from the Casino!  " + time
        else:
            activity = "Oh No!!! Lost " + str(earn) + " golds from the Casino.  " + time
    
    if earn >= 0:
        color = 'text-success'
    else:
        color = 'text-danger'
    
    log = {
        'activity' : activity,
        'color' : color
    }

    request.session['count'] += earn
    request.session['log'].append(log)

    return redirect('/')

def reset(request):
    del request.session['count']
    del request.session['log']

    return redirect('/')