from django.shortcuts import render, redirect
from django.http import HttpResponse
# import my model
from .models import Players, UploadedImage
# import the form module
from .forms import ImageUploadForm, PlayerInfoForm
# Create your views here.

# the view gets all the members in the database(model)


def members(request):
    # get all the data in the model(table)
    team_members = Players.objects.all().values()
    # get all the images from model
    images = UploadedImage.objects.all()

    # code to handle the player form data
    if request.method == 'POST':
        InfoForm = PlayerInfoForm(request.POST, request.FILES)
        if InfoForm.is_valid():
            InfoForm.save()
    else:
        InfoForm = PlayerInfoForm()
    context = {
        # create a dictionary and store the values from the model
        "team": team_members, "images": images, "AddPlayerForm": InfoForm
    }
    return render(request, "team.html", context)

# the view gets the info the current member in the database(model)


def detail_view(request, player_id):
    # get player with the id passed as argument to the view in the url
    player = Players.objects.get(id=player_id)
    context = {
        "current_player_data": player,
    }
    return render(request, "playerdetail.html", context)

# code to handle image upload

# the view uploads an image to the model


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

# the view returns list of images in the model


def image_list(request, img_id):
    images = UploadedImage.objects.get(pk=img_id)
    return render(request, 'image_list.html', {'images': images})
