from django.shortcuts import redirect, render
import os
import uuid
from sendEverywhere import settings
from .models import File
from django.http import FileResponse
from . import task
from django.contrib.auth import authenticate, get_user, login, logout
from django.contrib.auth.models import User


def create_folder(folder_path):
    """Creates a folder if it doesn't exist."""
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


def download(request_code):
    obj = File.objects.get(request_code=request_code)
    filename = obj.model_attribute_name.path
    response = FileResponse(open(filename, 'rb'))
    return response


def index(request):
    context = {}
    context.update({
        "active_nav": "home",
        "user": request.user
    })

    if request.method == "POST" and request.FILES["file"]:

        random_uuid = uuid.uuid4()
        file = request.FILES["file"]

        # extract extenion of the file
        split_tup = os.path.splitext(file.name)
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

        try:
            fileobject = File(uuid=random_uuid, file=file,
                              name=file_name, path=path)
            fileobject.save()
        except:
            context.update({
                "error": "Couldnt upload file"
            })
            return render(request, "index.html", context)

        if "request_code" in request.POST:
            context.update({
                "request_code": fileobject.request_code
            })

        elif "request_link" in request.POST:
            context.update({
                "Link": "localhost:8000" + fileobject.file.url
            })

        return render(request, "index.html", context)
        # task.removeFile.apply_async_on_commit()

    elif request.method == "GET" and request.GET.get("request_code"):
        request_code = request.GET.get("request_code")
        try:
            obj = File.objects.get(request_code=request_code)
            filename = obj.path
            response = FileResponse(
                open(filename, 'rb'), as_attachment=True, filename=obj.file.name)
            context = {
                "codeSubmitted": obj
            }
            return response
        except:
            context = {
                "error": "Request code doesn't exist"
            }
            return render(request, "index.html", context)
    else:
        return render(request, "index.html")


def about(request):
    context = {
        'active_nav': 'about',
    }
    return render(request, "about.html", context)


def services(request):
    context = {
        'active_nav': 'services',
    }
    return render(request, "services.html", context)


def contact(request):
    context = {
        'active_nav': 'contact',
    }
    return render(request, "contact.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return redirect("register")
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        firstName = request.POST.get("firstName")
        # lastName = request.POST.get("lastName")
        email = request.POST.get("email")

        user = User.objects.create_user(
            email=email, username=username, password=password, first_name=firstName)
        user.save()
        return redirect("index")
    return render(request, "register.html")
