from django.shortcuts import render

def home(request):
    d = {
        'author' : 'Rahim',
        'age' : 20,
        'list' : [10, 20, 30],
        'courses' : [
            {
                'id' : 1,
                'name' : 'python',
                'fee' : 1000
            },
            {
                'id' : 2,
                'name' : 'django',
                'fee' : 5000
            },
        ]
    }
    return render(request, 'home.html', d)      