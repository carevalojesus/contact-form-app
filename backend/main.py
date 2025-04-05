from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import date, datetime
import uuid
import json
import os

# Modelo de datos para el contacto
class ContactBase(BaseModel):
    nombre: str
    apellidos: str
    correo: EmailStr
    celular: str
    fecha_nacimiento: date
    genero: str
    direccion: str

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: str
    fecha_registro: datetime

    class Config:
        orm_mode = True

# Creación de la aplicación FastAPI
app = FastAPI(title="API de Contactos", 
              description="API para gestionar contactos y exportar a vCard",
              version="1.0.0")

# Configuración de CORS para permitir solicitudes del frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulamos una base de datos con un archivo JSON
DB_FILE = "contacts.json"

# Función para cargar contactos desde el archivo
def load_contacts():
    if not os.path.exists(DB_FILE):
        return []
    
    try:
        with open(DB_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error al cargar contactos: {e}")
        return []

# Función para guardar contactos en el archivo
def save_contacts(contacts):
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(contacts, file, default=str, ensure_ascii=False, indent=2)


# Rutas para la API
@app.get("/")
def read_root():
    return {"message": "API de Contactos funcionando correctamente"}

@app.get("/contacts/", response_model=List[Contact])
def get_contacts():
    contacts = load_contacts()
    return contacts

@app.post("/contacts/", response_model=Contact, status_code=201)
def create_contact(contact: ContactCreate):
    contacts = load_contacts()
    
    # Creamos un nuevo contacto con ID y fecha de registro
    new_contact = {
        **contact.dict(),
        "id": str(uuid.uuid4()),
        "fecha_registro": datetime.now()
    }
    
    contacts.append(new_contact)
    save_contacts(contacts)
    return new_contact

@app.get("/contacts/{contact_id}", response_model=Contact)
def get_contact(contact_id: str):
    contacts = load_contacts()
    for contact in contacts:
        if contact["id"] == contact_id:
            return contact
    raise HTTPException(status_code=404, detail="Contacto no encontrado")

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: str):
    contacts = load_contacts()
    initial_length = len(contacts)

    contacts =[contact for contact in contacts if contact["id"] != contact_id]

    if len(contacts) == initial_length:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    save_contacts(contacts)
    return {"message": "Contacto eliminado correctamente"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main.app", host="0.0.0.0", port=8000, reload=True)
