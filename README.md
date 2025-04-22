# exam-simulator
Este proyecto es una aplicación web interactiva que permite a los usuarios practicar para un examen a partir de archivos de entrada con preguntas, respuestas y explicaciones. El sistema genera automáticamente una interfaz web de simulación con retroalimentación inmediata y explicación detallada de cada pregunta.

## 🚀 Características
- Carga dinámica de preguntas desde archivos `.txt`
- Corrección automática de respuestas
- Explicaciones detalladas tras cada intento
- Interfaz amigable e intuitiva
- Ideal para prácticas individuales o entornos educativos

## 📦 Estructura del Proyecto
```text
simulador-examenes/
├── preguntas.txt
├── respuestas.txt
├── explicaciones.txt
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```
## 🌿 Variables de Entorno

El archivo `.env` se utiliza para configurar las variables de entorno necesarias para que la aplicación funcione correctamente. A continuación se detallan las variables que debes incluir en el archivo `.env`:

### Variables Requeridas

- **ARCHIVO_PREGUNTAS**: Define el nombre del archivo que contiene las preguntas para el examen.
  - Ejemplo: `preguntas.txt`

- **ARCHIVO_RESPUESTAS**: Define el nombre del archivo que contiene las respuestas correctas para cada pregunta.
  - Ejemplo: `respuestas.txt`

- **ARCHIVO_EXPLICACIONES**: Define el nombre del archivo que contiene las explicaciones de las respuestas correctas.
  - Ejemplo: `explicaciones.txt`

### Ejemplo de archivo `.env`

```env
ARCHIVO_PREGUNTAS=preguntas.txt
ARCHIVO_RESPUESTAS=respuestas.txt
ARCHIVO_EXPLICACIONES=explicaciones.txt
```

## 📂 Estructura de Archivos de Entrada
El sistema requiere tres archivos de entrada con el siguiente formato:

### 1. `preguntas.txt`
Cada línea representa una pregunta y sus opciones. El separador de preguntas es `---`  
**Formato:**
```text
1. ¿Qué es Python?
A. Un animal
B. Un lenguaje de programación
C. Un videojuego
D. Una ciudad
---
2. Which of the following are the current options for paid support in GCP? (Select three)
A. Standard
B. Enhanced
C. Premium
D. Role
E. Premier
```
### 2. `respuestas.txt`
Cada línea contiene la opción correcta para la pregunta correspondiente en `preguntas.txt`.  
**Formato:**
```text
1:B
2:A,B,C
```
### 3. `explicaciones.txt`
Cada línea contiene la explicación de la respuesta correcta correspondiente. El separador de explicaciones es `---`  
**Formato:**
```text
1:Python es un lenguaje de programación de alto nivel muy usado en desarrollo web, ciencia de datos, automatización, entre otros.
---
2:GCP provides three options for paid support, which are Standard, Enhanced, and Premium. Basic Support is included with your Google Cloud subscription, which only covers case, phone, and chat support for billing issues.
```

## ⚙️ Instalación
1. Clona el repositorio:
```
git clone https://github.com/tuusuario/exam-simulator.git
cd exam-simulator`
```
2. Crea el contenedor
`docker-compose up --build`

3. Abre tu navegador y accede a: http://localhost:8080

