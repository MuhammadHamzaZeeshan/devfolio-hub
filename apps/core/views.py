from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {'title': 'Home', 'name': 'Hamza Zeeshan', 'bio': 'I’m Muhammad Hamza Zeeshan, a 4th year computer science student at the University of Karachi. I am currently learning software development and also work on automation, data mining and analysis. I love learning new technologies, always excited to take on new and creative projects!'})
