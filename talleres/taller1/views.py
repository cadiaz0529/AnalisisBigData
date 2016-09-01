from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm
import cgi, cgitb

import json

def index(request):
	lista=[]
	form = cgi.FieldStorage() 
	palabra = form.getvalue('consulta_xquery')
	lista.append(palabra)
	context={'lista_prueba':lista}
	return render(request, 'taller1/index.html', contexto)


# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = PostForm()
#     return render(request, 'post.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Post(text=post_text, author=request.user)
        post.save()

        #filtrado_regex.main(post.text)

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
)