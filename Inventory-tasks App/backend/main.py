#IMPORTS
from fastapi import FastAPI
from pydantic import BaseModel


#VARIABLES
app = FastAPI()    #app server object
inventory = [
    {'id':1000, 'name':'Bar Soap', 'quantity':3},
    {'id':1001, 'name':'Shampoo', 'quantity':1},
    {'id':1002, 'name':'Conditioner', 'quantity':1},
]


#pydantic   |   FUNCTIONS
class inventory_items(BaseModel):    #structure for inventory
    id: int
    name: str
    quantity: int


#FastAPI   |   FUNCTIONS
@app.get('/')    #read status requests
def api_status():
    return {'STATUS':'***SUCCESSFUL***'}
api_status()

@app.get('/inventory')    #read inventory requests
def check_inventory():
    return inventory

@app.post('/inventory')    #add inventory items
def add_inventory(item: inventory_items):    
    inventory.append(item.dict())    #adding to the end of the inventory dictionary
    return item

@app.put('/inventory/{id_number}')    #update existing inventory items    ***CURRENTLY CAUSING internal runtime error 500***
def update_inventory(id_number: int, update: inventory_items):
    for index, item in enumerate(inventory):    #numbered list of invenotry
        if item['id'] == id_number:    #if 'item' (the id) in the 'index, item' pair of inventory is matches an existing 'id'
            inventory[index] = updated.dict()
            return updated
    return {'***ERROR***': 'Item not found'}    #if id does not match display error message

@app.delete('/inventory/{id_number}')    #delete inventory if its id_number exists
def remove_inventory(id_number: int):
    for item in inventory:
        if item['id'] == id_number:
            inventory.remove(item)
            return {'***UPDATE***': 'Item Deleted from inventory'}
    return {'***ERROR***': 'Item not found'}
