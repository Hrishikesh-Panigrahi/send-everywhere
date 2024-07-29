from django.shortcuts import render
import os
import uuid
from sendEverywhere import settings
from .models import File

def create_folder(folder_path):
  """Creates a folder if it doesn't exist."""
  if not os.path.exists(folder_path):
    os.mkdir(folder_path)


# Create your views here.
def index(request):
    if request.method == "POST":
        random_uuid = uuid.uuid4()
        file = request.FILES["file"]
        
        # extract extenion of the file
        split_tup = os.path.splitext(file.name)
        
        # extract the file name and extension
        file_name = split_tup[0]
        file_extension = split_tup[1]
        
        # then combine the uuid and the extension
        filename = f"{random_uuid}{file_extension}"

        # save the file in the media folder with name as filename
        try:
            create_folder(os.path.join(settings.MEDIA_ROOT, "file/"))
        except:
            print("Folder already exists")

        with open(os.path.join(settings.MEDIA_ROOT, "file/", filename), "wb") as f:
            for chunk in file.chunks():
                f.write(chunk)
        path = os.path.join(settings.MEDIA_ROOT, "file/", filename)
        
        fileobject = File(uuid= random_uuid, file = file, name = file_name, path = path)
        fileobject.save()
    
    elif request.method == "GET":
        request_code = request.GET.get("request_code")

        fileobject = File.objects.get(request_code = request_code)
        print(fileobject)

    else:
        return render(request, "index.html")