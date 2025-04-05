# Sistema de Gestión de Contactos

Esta aplicación permite gestionar contactos personales, con funcionalidades para registrar, visualizar y exportar contactos en formato vCard.

## Características

- Registro de datos completos de contacto (nombre, apellidos, correo, celular, fecha de nacimiento, género, dirección)
- Visualización de contactos en una tabla ordenada
- Exportación individual o masiva en formato vCard
- Interfaz responsiva y amigable
- API RESTful con FastAPI
- Validación de datos en ambos, frontend y backend

## Estructura del proyecto

```
sistema-gestion-contactos/
│
├── backend/
│   ├── main.py                 # API de FastAPI
│   ├── requirements.txt        # Dependencias del proyecto
│   └── contacts.json           # Base de datos (se crea automáticamente)
│
├── frontend/
│   └── index.html              # Interfaz de usuario
│
└── README.md                   # Este archivo
```

## Requisitos previos

- Python 3.8 o superior
- Navegador web moderno
- Conexión a internet (para cargar Bootstrap desde CDN)

## Instalación y ejecución

### Paso 1: Configurar el Backend

1. **Clonar o descargar el repositorio**

2. **Crear un entorno virtual (recomendado)**
   ```bash
   # Crear entorno virtual
   python -m venv venv
   
   # Activar entorno virtual
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instalar las dependencias**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Iniciar el servidor**
   ```bash
   uvicorn main:app --reload
   ```
   El servidor se ejecutará en `http://127.0.0.1:8000`

### Paso 2: Acceder al Frontend

Simplemente abre el archivo `frontend/index.html` en tu navegador web.

Si estás ejecutando todo en máquina local, no deberías tener problemas con CORS. Para un entorno de producción, considera configurar correctamente las políticas de CORS en el backend.

## Documentación de la API

La API está documentada automáticamente gracias a FastAPI:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### Endpoints disponibles

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/contacts/` | Obtener todos los contactos |
| POST | `/contacts/` | Crear un nuevo contacto |
| GET | `/contacts/{contact_id}` | Obtener un contacto específico |
| DELETE | `/contacts/{contact_id}` | Eliminar un contacto |
| GET | `/contacts/{contact_id}/vcard` | Obtener vCard de un contacto específico |
| GET | `/export/vcard` | Exportar todos los contactos en formato vCard |

## Uso de la aplicación

### Registrar un contacto

1. Completa todos los campos del formulario
2. Haz clic en "Registrar Contacto"
3. Verás una notificación de éxito y serás redirigido a la lista de contactos

### Ver contactos

1. Haz clic en la pestaña "Ver Contactos"
2. Se mostrará una tabla con todos los contactos registrados

### Exportar contactos

- Para exportar un contacto individual, haz clic en el botón "vCard" en la fila correspondiente
- Para exportar todos los contactos, haz clic en "Exportar todos como vCard"

### Eliminar un contacto

1. Haz clic en el botón "Eliminar" en la fila del contacto
2. Confirma la eliminación en el diálogo que aparece

## Personalización

### Base de datos

Por defecto, la aplicación utiliza un archivo JSON como base de datos. Para entornos de producción, considera implementar una base de datos más robusta como PostgreSQL o MongoDB.

### Interfaz de usuario

La interfaz utiliza Bootstrap 5 y puede personalizarse modificando las clases y estilos en el archivo `index.html`.

## Solución de problemas

- Si encuentras problemas de CORS, asegúrate de que el backend esté configurado correctamente para permitir solicitudes del origen del frontend.
- Verifica que el servidor esté ejecutándose en el puerto 8000, que es el configurado por defecto en el frontend.
- Para cualquier error en los formularios, revisa la consola del navegador para obtener más información.

## Contribuir

Las contribuciones son bienvenidas. Por favor, siente libre de mejorar esta aplicación y enviar pull requests.