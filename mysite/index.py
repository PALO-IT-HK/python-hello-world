from django.http import HttpResponse

def homePageView(request):
  print('hihi')
  return HttpResponse(
    """
    <html>
      <head>
        <title>Python Hello World</title>
      </head>
      <body>
        HELLO WORLD!
      </body>
    </html>
    """
  )
