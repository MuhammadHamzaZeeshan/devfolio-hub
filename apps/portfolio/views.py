from django.shortcuts import render


my_projects = [
    {'name': 'Student Management System', 'description': 'This project is a web-based student management system using Flask and MySQL for managing student records, attendance, and departments with secure login and trigger-based logging.'},
    {'name': 'Smart Attendance System', 'description': 'This project is a real-time face recognition attendance system built with Flask, OpenCV, and MySQL, allowing secure user registration, automatic attendance marking, and a responsive web interface.'},
    {'name': 'Student Directory System', 'description': 'A beginner-friendly Django project that manages university student records with full CRUD functionality, organized program views.'}
]

def portfolio(request):
    return render(request, 'portfolio.html', {'title': 'Portfolio', 'projects': my_projects})