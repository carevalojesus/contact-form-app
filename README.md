# Sistema de Gestión de Contactos

Esta aplicación permite gestionar contactos personales, con funcionalidades para registrar, visualizar, editar, importar y exportar contactos.

## Características

- Registro de datos completos de contacto (nombre, apellidos, correo, celular, fecha de nacimiento, género, dirección)
- Visualización de contactos con cálculo automático de edad
- Edición de contactos existentes
- Importación de contactos desde archivos Excel (.xls, .xlsx) o CSV (.csv)
- Exportación individual o masiva en formato vCard
- Interfaz responsiva y amigable con Bootstrap 5
- API RESTful con FastAPI
- Validación de datos en frontend y backend

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

## Funcionalidades

### 1. Registro de contactos
- Formulario completo con validación
- Todos los campos son obligatorios
- El botón "Registrar Contacto" envía los datos a la API

### 2. Visualización de contactos
- Tabla con todos los contactos registrados
- Muestra la edad calculada automáticamente a partir de la fecha de nacimiento
- Botones para editar, exportar como vCard o eliminar cada contacto

### 3. Edición de contactos
- Modificación de cualquier dato del contacto
- Modal con formulario precargado con los datos actuales
- Validación de campos antes de guardar cambios

### 4. Importación de contactos
- Importación desde archivos Excel (.xls, .xlsx) o CSV (.csv)
- Validación de estructura de columnas
- Plantilla descargable para facilitar la creación de archivos compatibles

### 5. Exportación de contactos
- Exportación individual como vCard
- Exportación de todos los contactos como vCard
- El formato vCard es compatible con la mayoría de aplicaciones de contactos

## Documentación de la API

La API está documentada automáticamente gracias a FastAPI:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### Endpoints disponibles

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/contacts/` | Obtener todos los contactos con edad calculada |
| POST | `/contacts/` | Crear un nuevo contacto |
| GET | `/contacts/{contact_id}` | Obtener un contacto específico |
| PUT | `/contacts/{contact_id}` | Actualizar un contacto existente |
| DELETE | `/contacts/{contact_id}` | Eliminar un contacto |
| GET | `/contacts/{contact_id}/vcard` | Obtener vCard de un contacto específico |
| GET | `/export/vcard` | Exportar todos los contactos en formato vCard |
| POST | `/import/excel` | Importar contactos desde Excel o CSV |

## Solución de problemas comunes

### Problemas de CORS
Si encuentras errores de CORS, asegúrate de que el backend esté configurado correctamente para permitir solicitudes del origen del frontend. La configuración actual permite solicitudes de cualquier origen para facilitar el desarrollo.

### Errores de importación
- Asegúrate de que tu archivo Excel o CSV tenga encabezados exactamente iguales a: `nombre`, `apellidos`, `correo`, `celular`, `fecha_nacimiento`, `genero`, `direccion`
- La función de importación intenta manejar diferentes formatos de fecha, pero es recomendable usar el formato ISO (YYYY-MM-DD)
- Si tienes problemas, usa la plantilla descargable como base

### Problemas con dependencias
Si encuentras errores relacionados con las bibliotecas Python, asegúrate de instalar exactamente las versiones especificadas en `requirements.txt`:
```bash
pip install -r requirements.txt --no-cache-dir
```

## Extensiones y personalizaciones

### Cambiar el almacenamiento de datos
Por defecto, la aplicación utiliza un archivo JSON como base de datos. Para entornos de producción, considera implementar una base de datos relacional:

1. Añade SQLAlchemy a `requirements.txt`
2. Modifica las funciones de almacenamiento en `main.py`
3. Crea los modelos de datos correspondientes

### Añadir autenticación
Para implementar autenticación básica:

1. Utiliza FastAPI Security con OAuth2PasswordBearer
2. Crea un modelo de Usuario y un sistema de registro/login
3. Protege las rutas sensibles con dependencias de autenticación

## Contribuir

Las contribuciones son bienvenidas. Por favor, siente libre de mejorar esta aplicación y enviar pull requests.