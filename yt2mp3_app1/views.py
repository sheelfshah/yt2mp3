from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework import renderers
import os
from yt2mp3_app1.yt2mp3_convert import get_song


class PassthroughRenderer(renderers.BaseRenderer):
    media_type = ''
    format = ''
    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data

@api_view(['GET'])
def get_music(request):
    name = request.GET.get('n', '')
    if name == "":
        return None
    path = get_song(name)
    f = open(path.replace("../", ""), "rb")
    response = FileResponse(f, content_type='whatever')
    response['Content-Length'] = os.fstat(f.fileno()).st_size
    fname=path.replace("../vids/", "")
    response['Content-Disposition'] = 'attachment; filename="' + fname +'"'

    return response
