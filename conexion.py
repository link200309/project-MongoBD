from pymongo import MongoClient

# Conexión a un servidor MongoDB en localhost, en el puerto 27017
client = MongoClient('localhost', 27017)

# Conexión a una base de datos específica
db = client['tbd-security']

def log_in(username, password):
    collection = db['Usern']
    document_user = collection.find_one({"nombre":username, "password":password})
    return document_user 

def obtener_interfaces(document_user):
    collection_userN_Rol = db['UserN_Rol']
    #collection_Rol = db['Rol']
    collection_Rol_Funcion = db['Rol_Funcion']
    #collection_Funcion = db['Funcion']
    collection_Funcion_UI = db['Funcion_UI']
    collection_UI = db['UI']
        
    document_userN_Rol = collection_userN_Rol.find({"id_user":document_user['_id']})
    
    Rols_ids = []
    for doc in document_userN_Rol:
        Rols_ids.append(doc['id_rol']) 
    
    document_Rol_Funcion = collection_Rol_Funcion.find({"id_rol":{"$in": Rols_ids}})
    
    funcions_ids = []
    for doc in document_Rol_Funcion:
        funcions_ids.append(doc['id_funcion'])      
    
    document_Funcion_UI = collection_Funcion_UI.find({"id_funcion":{"$in": funcions_ids}})
    
    UI_ids = []
    for doc in document_Funcion_UI:
        UI_ids.append(doc['id_UI'])  
            
    document_UI = collection_UI.find({"_id":{"$in": UI_ids}})
    
    UIs_name = []
    for doc in document_UI:
        UIs_name.append(doc['nombre'])
                
    return UIs_name
