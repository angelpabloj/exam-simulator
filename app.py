from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv

load_dotenv()

PREGUNTAS_FILE = os.getenv("ARCHIVO_PREGUNTAS", "preguntas_GCDL.txt")
RESPUESTAS_FILE = os.getenv("ARCHIVO_RESPUESTAS", "respuestas_GCDL.txt")
EXPLICACIONES_FILE = os.getenv("ARCHIVO_EXPLICACIONES", "explicaciones_GCDL.txt")

app = Flask(__name__)


def cargar_preguntas(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read().strip()
    bloques = contenido.strip().split('---')
    preguntas = {}
    for bloque in bloques:
        lineas = bloque.strip().split('\n')
        numero_pregunta = int(lineas[0].split('.')[0])
        enunciado = lineas[0]
        opciones = {linea[0]: linea[3:] for linea in lineas[1:]}
        preguntas[numero_pregunta] = {'enunciado': enunciado, 'opciones': opciones}
    return preguntas


def cargar_respuestas(nombre_archivo):
    respuestas = {}
    tipos_pregunta = {}
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            if linea.strip():
                num, resp = linea.strip().split(':')
                opciones = set(r.strip().upper() for r in resp.split(','))
                respuestas[int(num)] = opciones
                tipos_pregunta[int(num)] = 'multiple' if len(opciones) > 1 else 'single'
    return respuestas, tipos_pregunta


def cargar_explicaciones(nombre_archivo):
    explicaciones = {}
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()

    bloques = contenido.strip().split('---')

    for bloque in bloques:
        lineas = bloque.strip().split('\n')
        if not lineas:
            continue

        encabezado = lineas[0]
        if ':' not in encabezado:
            continue

        num_str, primera_linea = encabezado.split(':', 1)
        try:
            num = int(num_str.strip())
        except ValueError:
            continue

        cuerpo = [primera_linea.strip()] + [linea.strip() for linea in lineas[1:]]
        explicaciones[num] = ' '.join(cuerpo).strip()

    return explicaciones

@app.route("/", methods=["GET", "POST"], endpoint='examen')
def examen():
    preguntas = cargar_preguntas(PREGUNTAS_FILE)
    respuestas_correctas, tipos_pregunta = cargar_respuestas(RESPUESTAS_FILE)

    if request.method == "POST":
        respuestas_usuario = {}
        for key, value in request.form.items():
            if key.startswith("respuesta_"):
                num_str = key.replace("respuesta_", "").replace("[]", "")
                num = int(num_str)
                respuestas_usuario.setdefault(num, set()).add(value.strip().upper())
        return redirect(url_for("resultado", **{
            f"respuesta_{k}": ','.join(v) for k, v in respuestas_usuario.items()
        }))

    return render_template("examen.html", preguntas=preguntas, tipos_pregunta=tipos_pregunta)



@app.route('/resultado', methods=['POST'])
def resultado():
    preguntas = cargar_preguntas("preguntas_GCDL.txt")
    respuestas_correctas, tipos_pregunta  = cargar_respuestas(RESPUESTAS_FILE)
    explicaciones = cargar_explicaciones(EXPLICACIONES_FILE)

    respuestas_form = request.form.to_dict(flat=False)
    
    respuestas_usuario = {}
    for clave, valores in respuestas_form.items():
        if clave.startswith("respuesta_"):
            num_str = clave.replace("respuesta_", "").replace("[]", "")
            try:
                num = int(num_str)
                respuestas_usuario[num] = set(v.strip().upper() for v in valores)
            except ValueError:
                continue

    correctas = 0
    resultados = []

    for num, pregunta in preguntas.items():
        seleccion = respuestas_usuario.get(num, set())
        correcta = respuestas_correctas.get(num, set())
        es_correcta = seleccion == correcta
        if es_correcta:
            correctas += 1
        resultados.append({
            'num': num,
            'enunciado': pregunta['enunciado'],
            'opciones': pregunta['opciones'],
            'seleccion': ', '.join(sorted(seleccion)),
            'correcta': ', '.join(sorted(correcta)),
            'es_correcta': es_correcta,
            'explicacion': explicaciones.get(num, "Sin explicación disponible.")
        })

    porcentaje = (correctas / len(preguntas)) * 100
    return render_template("resultado.html", resultados=resultados, porcentaje=porcentaje, correctas=correctas, total=len(preguntas))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)