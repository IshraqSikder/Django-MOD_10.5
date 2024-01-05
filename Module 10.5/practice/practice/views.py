from django.shortcuts import render
import datetime
def home(request):
    
    d = {
        'author' : 'rahim',
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
        ],
        'number' : 123456789,
        'date' : datetime.datetime.now(),
        
    }
    return render(request, 'home.html', d)