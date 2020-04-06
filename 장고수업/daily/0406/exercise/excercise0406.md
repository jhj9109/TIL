# 0406

```python
from django.shortcuts import render, redirect
from .models import Review

def index(request):
    return render(request, 'articles/index.html', {'reviews': Review.objects.all()})

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    Review.objects.create( title = request.GET.get('title'), content = request.GET.get('content') )
    return redirect ('articles:detail', Review.objects.last().id)

def detail(request, pk):
    return render (request, 'articles/detail.html', {'review': Review.objects.get(id=pk)})

def edit(request, pk):
    return render (request, 'articles/edit.html', {'review': Review.objects.get(id=pk)})

def update(request, pk):
    review = Review.objects.get(id=pk)
    review.title = request.GET.get('title')
    review.content = request.GET.get('content')
    review.save()
    return redirect ('articles:detail', review.id)

def delete(request, pk):
    Review.objects.get(id=pk).delete()
    return redirect('articles:index')
```

