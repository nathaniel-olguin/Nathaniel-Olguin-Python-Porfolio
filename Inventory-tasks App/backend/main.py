#IMPORTS
from fastapi import FastAPI
from pydantic import BaseModel


#VARIABLES
app = FastAPI()    #app server object
inventory = [
    {'id':1000, 'name':'Black Toner', 'quantity':150},
    {'id':1001, 'name':'Cyan Toner', 'quantity':99},
    {'id':1002, 'name':'Yellow Toner', 'quantity':27},
    {'id':1003, 'name':'Magenta Toner', 'quantity':4}
]


#pydantic   |   CLASSES
class Inventory_Items_Body(BaseModel):    #body of the inventory structure (excluding ID) ***MUTABLE***
    name: str
    quantity: int

class Inventory_Items_Id(Inventory_Items_Body):    #full object with ID
    id: int

class Inventory_Items(BaseModel):    #base outline blueprint of the inventory items 
    id: int
    name: str
    quantity: int


#FastAPI   |   FUNCTIONS
@app.get('/')    #read status requests
def api_status():
    return {'STATUS':'***SUCCESSFUL***'}
api_status()

@app.get('/inventory')    #read inventory items
def check_inventory():
    return inventory

@app.post('/inventory')    #add inventory items
def add_inventory(item: Inventory_Items):    
    inventory.append(item.dict())    #adding to the end of the inventory list of dictionaries
    return item

@app.put('/inventory/{id_number}')    #update existing inventory items
def update_inventory(id_number: int, update: Inventory_Items_Body):    #uses the body class so that the ID is not affected by the update***
    for index, item in enumerate(inventory):    #numbered list of invenotry
        if item['id'] == id_number:    #if 'item' (the id) in the 'index, item' pair of inventory is matches an existing 'id'
            #UPDATE name/quantity without altering the ID#
            inventory[index]['name'] = update.name
            inventory[index]['quantity'] = update.quantity
            
            return inventory[index]
        
    return {'***ERROR***': 'Item not found'}    #if id does not match display error message

@app.delete('/inventory/{id_number}')    #delete inventory if its id_number exists   (id_number ⇶ URL)
def remove_inventory(id_number: int):
    for item in inventory:
        if item['id'] == id_number:
            inventory.remove(item)
            
            return {'***UPDATE***': 'Item Deleted from inventory'}
            
    return {'***ERROR***': 'Item not found'}    #if id does not match display error message
