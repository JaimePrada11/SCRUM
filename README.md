# Tienda Enigma

Tienda Enigma es una aplicación para la gestión de ventas e inventario desarrollada en Python. Permite a los administradores y vendedores gestionar productos, emitir facturas, y generar reportes detallados. Utiliza archivos JSON para almacenar datos de inventario y facturación, ofreciendo una solución eficiente y escalable para la administración de ventas.

## Tabla de contenidos

| Indice | Titulo |
|--|--|
| 1 | [Requisitos](#requisitos)|
| 2 | [Instalación](#instalacion)|
| 3 | [Uso](#uso)|
| 4 | [Tecnologías y Herramientas](#tecnologías-y-herramientas-utilizadas) |
| 5 | [Funcionalidades](#funcionalidades)|
| 6 | [Estructura del Proyecto](#estructura-del-proyecto) |
| 7 | [Estructura JSON](#estructura-json)|
| 8 | [Contribuidores](#contribuidores) |
| 9 | [Contribuir](#contribuir) |
| 10 | [Autor](#autor)|
| 11 | [Licencia](#licencia)|


## Requisitos

### Requisitos de Software

- **Visual Studio Code:** Se recomienda utilizar Visual Studio Code para el desarrollo. Puedes descargarlo desde [aquí](https://code.visualstudio.com/).
  
### Requisitos de Instalación

- **Git:** Para clonar el repositorio, necesitas tener Git instalado. Puedes descargarlo desde [aquí](https://git-scm.com/).

> [!IMPORTANT]
> Asegúrate de tener Git instalado para facilitar la colaboración y la gestión de versiones del proyecto.


## Instalacion
Para instalar y ejecutar la página web localmente:

   1. Clona el repositorio:
   ```bash
   $ git clone https://github.com/JaimePrada11/SCRUM.git
   ```
   2. Navega al directorio del proyecto:
   
   ```bash
   cd SCRUM
   ```

## Uso
Para visualizar y trabajar con esta página web, sigue estos pasos:
1. **Abrir el Proyecto:**
   - Navega a la carpeta del proyecto donde has clonado o descomprimido el repositorio.
     
2. **Abrir el Archivo Principal:**
   - ejecuta el comando `python main.py` y sigue las instrucciones en la consola



## Tecnologías y Herramientas Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-%230078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

- **Python**: Utilizado para el desarrollo de la lógica y funcionalidad del proyecto.
- **Visual Studio Code**: Editor de código.


## Funcionalidades

- **Registro**: Permite ingresar y modificar la información de los usuarios
- **Asignacion de Rutas de Entrenamiento**: Administra diferentes rutas de entrenamiento.
- **Evaluacion**: Permite la evaluacion de los campers.
- **Reportes**: Genera reportes detallados.
- **Base de datos**: Guarda la informacion en un JSON.
  

## Estructura del Proyecto

El proyecto está organizado en dos roles principales que garantizan la correcta administración y gestión del sistema:

- **Administrador**: Se encarga de la administración completa del sistema, incluyendo la creación de nuevos productos, la visualización de reportes detallados, el análisis de ganancias y la revisión de facturas.
    - Este rol tiene acceso total a todas las funcionalidades relacionadas con la gestión y supervisión del proyecto.

- **Vendedor**: Su responsabilidad principal es la emisión de facturas y la revisión del inventario.
    - Este rol se centra en la interacción directa con los clientes a través de la generación de facturas y en la gestión básica del inventario para asegurar que esté actualizado.

## Estructura JSON

A continuación se muestra un ejemplo de cómo está estructurado el archivo JSON en el proyecto:

### Inventario

```json
     "P001": {
        "Descripcion": "PANTALON",
        "Marca": "LEVIS",
        "Talla": "L",
        "Cantidad": 17,
        "Estado": "Activo",
        "Costo": 50,
        "Precio": 75
    },
    "P002": {
        "Descripcion": "PANTALON",
        "Marca": "CALVIN",
        "Talla": "M",
        "Cantidad": 15,
        "Estado": "Activo",
        "Costo": 100,
        "Precio": 150
    }
```

### Facturacion

```json
     "F001": {
        "fecha": "21/07/2024",
        "ID": "123456",
        "nombre": "ANDRES",
        "Email": "J@GMAIL.COM",
        "Telefono": "3011778698",
        "Productos": {
            "P001": {
                "Talla": "L",
                "precio": 75,
                "Costo": 50,
                "Cantidad": 3
            },
            "P002": {
                "Talla": "M",
                "precio": 150,
                "Costo": 100,
                "Cantidad": 4
            }
        },
        "Costo": 550,
        "SubTotal": 825,
        "descuento": 41.25,
        "iva": 148.9125,
        "Total": 932.6625
    }
```

## Contribuidores

Gracias a las siguientes personas por su valiosa ayuda y colaboración en este proyecto:

- **Jhoan Sebastian Diaz Ardila** - *Product Owner*
  - Responsable de definir las características del producto y priorizar el backlog.

- **Alejandro Rincon Perez** - *Scrum Master*
  - Facilitador de las reuniones Scrum, encargado de la gestión del proceso Scrum y apoyo al equipo.

- **Julian David Piñeros Coronado** - *Equipo de Desarrollo*
  - Desarrollador, encargado de implementar las funcionalidades del proyecto y participar en las revisiones de sprint.

- **Maria Camila Diaz Toledo** - *Equipo de Desarrollo*
  - Desarrolladora, responsable de la codificación y las pruebas de las características del producto.

Si deseas contribuir a este proyecto, sigue las instrucciones en la sección [Contribuir](#contribuir) para comenzar.

## Contribuir

¡Gracias por tu interés en contribuir a este proyecto! Aquí tienes algunos pasos para comenzar:

1. **Fork del Repositorio**
   - Realiza un fork del repositorio en GitHub para tener tu propia copia del proyecto. Puedes hacer esto haciendo clic en el botón "Fork" en la parte superior derecha de la página del repositorio.

2. **Clona el Repositorio**
   - Clona el repositorio forked a tu máquina local para que puedas trabajar en él. Usa el siguiente comando:
     ```bash
     git clone https://github.com/TU_USUARIO/NOMBRE_DEL_REPOSITORIO.git
     ```
   - Asegúrate de reemplazar `TU_USUARIO` y `NOMBRE_DEL_REPOSITORIO` con tu nombre de usuario y el nombre del repositorio correspondiente.

3. **Crea una Rama**
   - Crea una nueva rama para tus cambios. Es una buena práctica nombrar la rama de manera descriptiva:
     ```bash
     git checkout -b nombre-de-tu-rama
     ```

4. **Realiza Cambios**
   - Haz los cambios necesarios en el código, la documentación o en los archivos del proyecto. Asegúrate de probar tus cambios localmente antes de proceder.

5. **Commit y Push de tus Cambios**
   - Una vez que hayas realizado y probado tus cambios, realiza un commit y luego haz push a tu repositorio forked:
     ```bash
     git add .
     git commit -m "Descripción de los cambios"
     git push origin nombre-de-tu-rama
     ```

6. **Envía un Pull Request**
   - Ve a la página de tu repositorio en GitHub y verás una opción para enviar un pull request para tu rama. Haz clic en "New Pull Request", selecciona la rama en la que has trabajado y crea el pull request.
   - Asegúrate de proporcionar una descripción clara de los cambios que has realizado y cualquier detalle adicional que pueda ser útil para la revisión.


## Autor
Este proyecto fue desarrollado por Jaime Andres Prada Torres

- **Email**: [jandrespradato.11@gmail.com](mailto:jandrespradato.11@gmail.com)
  
Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través del enlace anterior.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.
