from django.shortcuts import render
from pages_app.models import StoredFile

def index(request):
    return render(request, 'index.html')


def home_videos(request):

    if request.method == 'POST':
        file = request.FILES['file']
        stored_file = StoredFile.objects.create(file=file)

        print(stored_file)
        
    files = StoredFile.objects.all()

    context = {
        'files': files
    }

    return render(request, 'pages/home-videos.html', context)