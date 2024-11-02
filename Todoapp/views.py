from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
# Create your views here.
def todo_list(request):
    todos=Todo.objects.order_by('-id')
   
    return render(request,'todo/index.html',{'todos':todos})


def create_todo(request):
    if request.method =='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        Todo.objects.create(title=title,  description=description)
    return redirect('todo_list')

def complete_todo(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.completed=True
    todo.save()
    return redirect('todo_list')
    
def Delete_todo(request, todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')




def update_todo(request, todo_id):
   
    todo = get_object_or_404(Todo, id=todo_id)

    if request.method == 'POST':
       
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo/update_todo.html', {'todo': todo})
