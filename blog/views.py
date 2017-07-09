from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/pt_list.html', {})
