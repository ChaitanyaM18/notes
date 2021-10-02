from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
import qrcode
import os

@login_required
def home(request):
    return render(request, "home.html")

# @login_required
def generateQr(request):
    qr_images = []
    if request.method == 'POST':
        qr_argument = request.POST.get('qr')
        start_ = int(request.POST.get('start_'))
        end_ = int(request.POST.get('end_'))
        for item in range(start_,end_+1):
            qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
            qr.add_data("http://127.0.0.1:8000/?"+qr_argument+"_"+str(item))
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save('./assets/media/qr_codes/'+qr_argument+"_"+str(item)+".png")
            image_path = os.path.join('/media/qr_codes/'+qr_argument+"_"+str(item)+".png")
            image_name = qr_argument+"_"+str(item)+".png"
            qr_obj = QRModel(image_path=image_path,image_name=image_name)
            qr_obj.save()
            qr_images.append(image_path)
        return render(request, "qr/qr.html", {"qr_images":QRModel.objects.all()})
