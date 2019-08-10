from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreateNewList
from .models import ToDoList, Item

# Create your views here.

def home(response):
    return render(response, 'main/home.html', {})

@login_required
def myLists(response):
    td = response.user.todolist.all()
    
    if response.method == 'POST': #check if it is posting or getting something
        if response.POST.get("addList"):
            txt = response.POST.get("add-list")
            print(txt)
            response.user.todolist.create(name=txt)
    
        elif response.POST.get('delList'): #determine which html button was clicked to run a function if it has one.
            txt = response.POST.get("delete-list") #from the response add the value of input field named delete-list
            #print(txt)
            for item in td: 
                if txt == item.name: #check if the value of the input is equal to any of the users lists
                    item.delete() #if its equal delete list
    else:
        return render(response, 'main/view.html', {})
    
    return render(response, 'main/view.html', {})

@login_required
def listItems(response, id):
    ls = ToDoList.objects.get(id=id) #when items get created via the model we can access them with modelname.objects.method()

    if response.method == 'POST':
        print(response.POST)
        if response.POST.get("save"): #save is the name of the html button, this button will return a dictionary which we can use its values to create delete etc
            for item in ls.item_set.all():
                if response.POST.get('c' + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                
                item.save()
        
        elif response.POST.get("newItem"): #newItem is the name of the html button
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False, user=response.user)

        elif response.POST.get("delItem"): #this is the value of the input named delete
            txt = response.POST.get("delete-item")
            for item in ls.item_set.all():
                if txt == item.text:
                    item.delete()
        else:
            print("Oops, seems there was an error.")
        
    return render(response, 'main/listItems.html', {'ls':ls})


def new_user_welcome(response):
    return render(response, 'main/welcome.html' ,{})