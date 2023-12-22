from django.urls import path

from core.libs.utils import func1
from .api import *;

from .views import genMpMiniQrcode, getRandomString, jump, qecodeGenerate, home, sendMpMiniSubscribe

urlpatterns = [
    path("j/<str:path>", jump, name="jump"),
    path("qr", qecodeGenerate, name="qrcode"),
    path("", home),
    path('wxmini/send',sendMpMiniSubscribe),
    path('wxmini/qr',genMpMiniQrcode),
    path('api/random',getRandomString)
]

func1()