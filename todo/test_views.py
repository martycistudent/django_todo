from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item



class TestViews(TestCase):

    def test_get_home_page(self):
        # This is a built-in helper that will fake a request to the URL
        # that we pass in as an argument. Store the output of that in page variable.
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")

    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
    
    def test_get_edit_item_page(self):
        # Create an instance of the item model. The view expects an ID of an
        # actual object that it can retrieve from the database.
        item = Item(name="Create a test")
        # It won't save it in a real database, save in a test database
        item.save()

        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
    
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
    
    # Testing form submissions
    def test_post_create_an_item(self):
        # Create a new item using post on line and then we should be able to retrieve that exact same item 
        response = self.client.post("/add", {"name": "Create a test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
    
    def test_post_edit_an_item(self):
        item = Item(name="Create a test")
        item.save()
        id = item.id

        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        item = get_object_or_404(Item, pk=id)
        self.assertEqual("A different name", item.name)

    def test_toggle_status(self):
        item = Item(name="Create a test")
        item.save()
        id = item.id

        respsonse = self.client.post("/toggle/{0}".format(id))
        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.done, True)