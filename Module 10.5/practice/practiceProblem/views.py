from django.shortcuts import render

# Create your views here.
def about(request):
    
    d = {
        'name' : 'Ishraq Uddin Sikder',
        'id' : 2024,
        'list' : ['I','love','Python'],
        'title' : 'I am a programmer',
        'description' : 'Happy 2024! Chances are that set up for success in the new year with this extended guide to crafting a self-improvement strategy that works, combining and extending all of my previous blog posts on the topic.'
    }
    return render(request,'about.html',d)