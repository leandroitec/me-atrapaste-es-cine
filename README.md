# 🎬 Me Atrapaste, Es Cine - Sistema de Cartelera y Tickets 🍿

Trabajo práctico evaluativo desarrollado en Django para la gestión integral de un complejo de cines. El sistema incluye control de usuarios personalizados, asignación de permisos por grupos, administración de cartelera con imágenes (Pillow), manejo de salas y funciones dinámicas, además de un context processor global.

---

## 🚀 Requisitos de la Consigna Cumplidos

### 📊 1. Base de Datos (6 Modelos Relacionados)
* **UsuarioPersonalizado (`AbstractUser`)**: Registro extendido para los clientes del cine (con campos DNI y Teléfono) desacoplado en su propia app de usuarios.
* **Pelicula**: Contiene título, sinopsis, duración y soporte multimedia para la carga de imágenes (`ImageField` para el póster).
* **Sala**: Configuración física de los espacios (Sala 1, Sala 2, etc.) y su capacidad de asientos.
* **Funcion**: Modelo pivote que conecta una Película con una Sala en una fecha/hora determinada y un formato de proyección específico (2D, 3D, 4D).
* **Ticket**: Registro de las compras asociando al usuario con la función elegida y la cantidad de butacas reservadas.
* **Resena**: Comentarios y puntuaciones de 1 a 5 estrellas que los usuarios otorgan a los films.

### 🔐 2. Autenticación y Permisos por Grupo
* **Lectura libre (Read)**: Cualquier usuario registrado puede iniciar sesión para visualizar el Home con las promociones, la cartelera de películas y los horarios de las funciones.
* **Escritura protegida (CRUD C-U-D)**: El panel de administración cuenta con el grupo **`GestionCine`**. Solo los usuarios asignados a este grupo heredan los permisos correspondientes para crear, editar o eliminar películas y funciones directamente desde los templates de la web. Los usuarios comunes tienen los botones de gestión ocultos y las rutas bloqueadas.

### ⚙️ 3. Otras Características Técnicas
* **Context Processor**: Implementación de `info_cine` que inyecta de manera global y automática datos como el nombre del cine, el año actual dinámico en el footer y el conteo de películas en cartelera sin recargar las vistas.
* **Estilos Profesionales**: Interfaz pulida y responsive armada con el framework **Bootstrap 5**, incluyendo vistas personalizadas con imágenes estáticas para combos comerciales y el icónico banner temático del proyecto.

---

## 🖼️ Capturas del Proyecto en Funcionamiento

### 🏠 Pantalla de Inicio (Home Comercial)
<img width="1919" height="1027" alt="Image" src="https://github.com/user-attachments/assets/975c1e2e-8018-4e50-b3ee-0a1668bdab76" />
<img width="1919" height="1079" alt="Image" src="https://github.com/user-attachments/assets/7840014a-7258-4dd8-b4b7-55ec1a765a4e" />

### Login
<img width="1918" height="1030" alt="Image" src="https://github.com/user-attachments/assets/a5fab1e1-c9f2-4869-b852-cd85a8410d1e" />


### Register
<img width="1919" height="1028" alt="Image" src="https://github.com/user-attachments/assets/cecc89dc-4272-429a-bc0a-bf6f6f8a2f85" />

### Cartelera (admin - user)
<img width="1919" height="1027" alt="Image" src="https://github.com/user-attachments/assets/373753b7-0786-45ea-9ef1-2f955b292c01" />

<img width="1914" height="1029" alt="Image" src="https://github.com/user-attachments/assets/e0878834-88c1-4d03-a4e9-88433ef71f53" />


### Funciones (admin - user)

<img width="1919" height="1029" alt="Image" src="https://github.com/user-attachments/assets/b0e97b2b-0829-4c05-b7f2-2717495046b6" />

<img width="1919" height="1030" alt="Image" src="https://github.com/user-attachments/assets/9a07262f-d217-49e1-b0ad-74a2fffb45e1" />

### Agregar, editar y eliminar Pelicula (admin)
<img width="1919" height="1029" alt="Image" src="https://github.com/user-attachments/assets/87ddbef8-c9b2-4f3a-a0e1-69e46e8c9eb5" />

<img width="1919" height="1029" alt="Image" src="https://github.com/user-attachments/assets/58fd8da4-0e5f-4444-8350-963a6290e806" />

<img width="1919" height="1031" alt="Image" src="https://github.com/user-attachments/assets/a15c39fd-e130-4672-b725-8b9afa281a51" />

### Agregar Funcion (admin)
<img width="1919" height="1025" alt="Image" src="https://github.com/user-attachments/assets/4c9587f2-4155-42a0-ac61-d5bf8be4136a" />

## 🛠️ Instalación y Ejecución Local

1. Clonar el repositorio:
   git clone git@github.com:leandroitec/me-atrapaste-es-cine.git
   cd me-atrapaste-es-cine

2. Crear y activar el entorno virtual:
    python3 -m venv venv
    source venv/bin/activate

3. Instalar las dependencias necesarias:
    npm install
    pip install django Pillow

4. Realizar las migraciones y levantar el servidor:
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

5. Ejecutar: 
    npm run dev
    
