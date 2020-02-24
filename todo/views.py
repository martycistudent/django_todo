from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
# import the item model from .models
from .models import Item
from .forms import ItemForm



# Create your views here.
def get_todo_list(request):
    # This will return all of the objects that are stored in the item table.
    results = Item.objects.all()
    return render(request, "todo_list.html", {
        'items': results})

def create_an_item(request):
    if request.method == "POST":
        # Inside of the constructor of that item form then we can populate it
        # with the values that we receive from the post in a request object.
        # FILES is used to make sure if there's any files being uploaded
        form = ItemForm(request.POST, request.FILES)
        # Django will automatically check to see if the form is valid 
        if form.is_valid():
            # because the form knows what model is being used when we specified it in our meta class we can 
            # actually just call save and the form will automatically know to check that it was valid and where
            # this information is to be saved.
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm()

    # Return the form
    return render(request, "item_form.html", {'form': form})

 # The code below is for a form made manually in a html template.
"""
# Will create an instance of the item model
new_item = Item()
# Will get any values that are stored in the POST method. Django
# will store a POST object in the request and the POST object will
# be a dictionary and it will contain the values of the form
new_item.name = request.POST.get('name')
# if done is present in the request.POST then it will be true
# otherwise it will be false
new_item.done = 'done' in request.POST
# Will save the item. This post is now actually being stored in the
# database and being retrieved from the database as well 
new_item.save()

return redirect(get_todo_list)
"""
# We need to take in id as a parameter of request
def edit_an_item(request, id):
    # Create a new instance of an item. I want to get the object from the item
    # table model and the specific one is the primary key/PK with value equal to the ID
    item = get_object_or_404(Item, pk=id)

    if request.method == "POST":
        # Populate it with request.POST, and the item we want to update is the
        # item defined on line 55.
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        # Create a form and we pass in the item as the instance that we want to
        # construct the object from
        form=ItemForm(instance=item)

    # Request the item_form.html file and we're going to also render the actual form as well
    return render(request, "item_form.html", {'form': form})