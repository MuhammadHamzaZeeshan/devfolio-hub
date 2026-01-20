from django.shortcuts import render


my_skills = ['Python', 'Django', 'JavaScript', 'React', 'HTML', 'CSS']
my_experience = [
        {'role': 'Data Science Intern', 'company': '10Pearls', 'duration': 'Dec 2025 - Present', 'description': 'Developed workflows to predict next 3 days AQI.', 'is_current': True},
        {'role': 'Database Management Intern', 'company': 'Karachi University', 'duration': 'Dec 2024 - Feb 2025', 'description': 'Managed and maintained student records for 45,000+ students.', 'is_current': False}
        ]
def resume(request):
    return render(request, 'resume.html', {'title': 'Resume', 'skills': my_skills, 'experience': my_experience
        })
