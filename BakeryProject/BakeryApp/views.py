from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Index(request):
    return HttpResponse("Bakery App Works")


def register(request):
    return HttpResponse("Bakery Register User Page")


def login(request):
    return HttpResponse("Login Page")


def ingredients(request):
    return HttpResponse("Add Ingredients Page")


def create_bakery_item(request):
    return HttpResponse("Create Bakery Item from a list of ingredients like Cupcake, Cake, Muffin etc")


def detail_bakery_item(request):
    return HttpResponse("Details of bakery item")


def manage_inventory(request):
    return HttpResponse("Manage Inventory")


def list_of_available_products(request):
    return HttpResponse("Get a list of available products")


def place_an_order(request):
    return HttpResponse("Place an Order")


def bill_details(request):
    return HttpResponse("Bill Details")


def order_history(request):
    return HttpResponse("Order History")
