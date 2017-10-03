import textwrap
import socket

from django.http import HttpResponse
from django.views.generic.base import View


class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Hello</h1>
                <p>Running on '''+socket.gethostname()+'''</p>
                <img src="../media/theimage.png" alt="NO PICTURE">
            </body>
            </html>
        ''')
        return HttpResponse(response_text)
