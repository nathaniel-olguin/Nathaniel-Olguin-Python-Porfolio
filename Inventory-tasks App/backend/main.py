from fastapi import FastAPI


#VARIABLES
app = FastAPI()
inventory = [
    {'id':1000, 'name':'Bar Soap', 'quantity':3},
    {'id':1001, 'name':'Shampoo', 'quantity':1},
    {'id':1002, 'name':'Conditioner', 'quantity':1},
    {'id':1003, 'name':'Face Wash', 'quantity':2}
]


#FUNCTIONS
@app.get('/')    #looking for requests
def api_status():
    return {'STATUS':'***SUCCESSFUL***'}

api_status()

@app.get('/inventory')    #looking for inventory requests
def check_inventory():
    return inventory
