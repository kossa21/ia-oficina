#!/usr/bin/env python3
"""
process_decks.py — IA en la Oficina 01/26
Añade logo AllWomen + speaker notes a los PPTX generados por NotebookLM.

Uso:
    python3 process_decks.py D05_MiDeck.pptx
    python3 process_decks.py D05_MiDeck.pptx D06_Otro.pptx D07_Otro.pptx
    python3 process_decks.py *.pptx   (todos los pptx sin procesar)

El script detecta automáticamente el día (D05, D06...) desde el nombre del archivo
y aplica las speaker notes correspondientes.
El archivo procesado se guarda en el mismo directorio con el nombre original.
"""

import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

# ── CONFIGURACIÓN ────────────────────────────────────────────────────────────

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(SCRIPT_DIR, "00_FULL COLOR (1).png")

# Posición logo AllWomen (aprobada por Daniela, no cambiar)
LOGO_WIDTH  = Inches(1.2)
LOGO_TOP    = Inches(0.20)
SLIDE_W     = Inches(17.78)
LOGO_LEFT   = SLIDE_W - LOGO_WIDTH - Inches(0.30)

# ── SPEAKER NOTES POR SESIÓN ─────────────────────────────────────────────────
# Cada lista tiene una nota por slide, en orden.
# Si el deck tiene más slides que notas, las slides extra quedan sin nota.
# Si tiene menos, solo se usan las primeras.

NOTES = {

    "D05": [
        "Arranca el M3 sesión 2. Conecta con D04: ya automatizan tareas repetitivas. Hoy aprenden a transformar cualquier documento en el formato exacto que necesita cada destinatario.",
        "Lanza la pregunta: '¿Alguna vez habéis tenido que explicar lo mismo tres veces a tres personas distintas?' Ese problema lo resuelve la IA en 30 segundos.",
        "Los tres tipos de resumen son el núcleo de la sesión. Escribe en la pizarra: EJECUTIVO / OPERATIVO / DIVULGATIVO. Pregunta: ¿Para quién escribiría cada uno de vosotros normalmente?",
        "Demuestra en directo: coge el acta ficticia del material, pégala en ChatGPT, y genera los tres resúmenes uno a uno con el prompt exacto de la slide. El grupo ve la diferencia en tiempo real.",
        "Conversión de formatos: el más útil en el día a día es texto→tabla y tabla→texto. Demuestra ambos con el mismo documento que acabas de usar. Pregunta: '¿Cuál usaríais vosotros esta semana?'",
        "Extracción de campos: este es el que más impresiona. Pega un correo largo y extrae: fechas, importes, responsables, acciones. El grupo ve que lo que antes tomaba 10 minutos ahora tarda 20 segundos.",
        "Documentos largos: no entres en tecnicismos sobre límites de tokens. Explica simplemente: 'Si el documento es muy largo, lo partes en trozos y luego pides el resumen global.'",
        "Actividad 1 — Acta en tres formatos (40 min). Proporciona el acta ficticia del material. El grupo trabaja individualmente y comparte resultados. Señala las diferencias de vocabulario entre versiones.",
        "Actividad 2 — Tu documento real (50 min). Cada alumno procesa un documento propio anonimizado. Circula por las mesas, ayuda con los prompts. Es el momento de personalizar el aprendizaje.",
        "Cierre y mini-entregable: tres versiones del mismo documento. Pregunta final: '¿Qué resumen usarías mañana en el trabajo?' Que cada persona nombre su destinatario real.",
    ],

    "D06": [
        "Arranca M3 sesión 3. Conecta con D05: ya saben resumir y transformar documentos. Hoy todo gira alrededor del correo, que es donde la mayoría pasa entre 1 y 2 horas al día.",
        "Estadística de impacto: el 47% de los correos no reciben respuesta en 24h por un asunto o cierre mal redactado. Pregunta: '¿Cuántos de vosotros tenéis correos sin respuesta desde hace más de 48h?'",
        "Los 6 elementos del correo: repásalos uno a uno con ejemplos malos vs buenos. El asunto es clave: demuestra el mismo correo con asunto vago ('Reunión') vs asunto concreto ('Validación del informe Q2 — plazo viernes').",
        "Situaciones difíciles: estas son las que más valor tienen para el grupo. Haz una votación rápida: '¿Cuál de estas situaciones os genera más bloqueo?' Y empieza por la más votada.",
        "Demuestra en directo: coge la situación más votada, escribe el prompt de la slide, y genera el correo en tiempo real. Pide al grupo que sugiera mejoras antes de cerrar.",
        "Respuestas a clientes — el patrón de 3 pasos: RECONOCE / INFORMA / ACTÚA. Escríbelo en la pizarra. Es la estructura que deben memorizar. Úsala en el role-play.",
        "Revisión con IA antes de enviar: demuestra el prompt de auditoría con un correo real (tuyo, anonimizado). El grupo ve cómo la IA señala lo que no está claro.",
        "Actividad 1 — 3 correos difíciles en directo (25 min). El grupo propone las situaciones, tú las resuelves con IA en pantalla. Mantén el ritmo: máximo 8 minutos por correo.",
        "Actividad 2 — Mis 5 correos reales (55 min). Cada alumno reescribe 5 correos propios. Insiste: deben anonimizar nombres y datos. Circula por las mesas y señala mejoras concretas.",
        "Role-play y mini-entregable: el banco de 5 plantillas. Que cada alumno comparta una plantilla antes de cerrar. Recuerda: los [CORCHETES] son los campos variables que deberán personalizar cada vez.",
    ],

    "D07": [
        "Arranca M3 sesión 4 y cierre del módulo de redacción. Conecta con D06: ya tienen su banco de plantillas. Hoy construyen documentos más largos: el informe.",
        "El informe es el mayor bloqueador de productividad en oficina. Pregunta: '¿Cuánto tiempo os lleva redactar un informe de 2 páginas?' Anota las respuestas. Al final de la sesión lo compararán con el tiempo que tardaron hoy.",
        "El flujo de 4 pasos es el contenido más importante de la sesión. Escríbelo en la pizarra: ÍNDICE → SECCIONES → RESUMEN EJECUTIVO → REVISIÓN. Insiste: el resumen ejecutivo siempre al final, nunca al principio.",
        "Demuestra paso a paso: usa el caso ficticio del material, construye el informe en 4 prompts en tiempo real. El grupo ve que el resultado en 15 minutos equivale a lo que normalmente les lleva una tarde.",
        "Adaptación de tono — las 3 versiones: TÉCNICA / EJECUTIVA / CLIENTE. Muestra las diferencias en el mismo párrafo. El vocabulario, la longitud de las frases y los detalles cambian radicalmente.",
        "Alucinaciones en informes: este es el punto de seguridad más crítico de la sesión. La regla de oro: 'Si no lo escribiste tú, verifícalo.' Demuestra el prompt de auditoría: pide a la IA que liste todos los datos que usó.",
        "Actividad 1 — Informe en 4 iteraciones (55 min). Proporciona los datos brutos del caso. El grupo construye el informe colectivamente, tú guías cada prompt. Al final, cronometrad el tiempo total.",
        "Actividad 2 — Adaptar a 3 públicos (40 min). Cada alumno adapta un texto propio. Sugiere que elijan un informe o documento que tengan que entregar próximamente — el entregable será real.",
        "Revisión cruzada y mini-entregable (10 min). Las 3 versiones del informe. Pregunta final: '¿Cuánto habríais tardado en hacer esto sin IA?' Cierra el módulo M3 recordando lo que han aprendido en D04–D07.",
    ],

    "D08": [
        "Arranca el módulo M4 — Organización del trabajo. Conecta: el grupo ya domina la redacción. Ahora IA para pensar, priorizar y organizarse, no solo para escribir.",
        "Dato de impacto: los profesionales que priorizan formalmente completan un 25% más de trabajo de alto impacto. Pregunta: '¿Cómo priorizáis ahora mismo? ¿Por orden de llegada, por urgencia, por intuición?'",
        "Eisenhower con IA: demuestra en directo. Pide al grupo que dicten 8-10 tareas reales. Pégalas en ChatGPT con el prompt de la slide. El grupo ve su propia semana clasificada en tiempo real.",
        "MoSCoW: explica que es más útil para proyectos con plazo fijo. Ejemplo: preparar el curso en sí mismo. ¿Qué es Must? ¿Qué es Won't? El grupo lo reconoce porque están viviendo la planificación del curso.",
        "Planificación semanal — el método de 4 pasos: VUELCA / RESTRICCIONES / PLAN / REFINA. El 'refina' es clave: la IA no es rígida, puedes negociar con ella igual que con un asistente.",
        "Demuestra el prompt de planificación semanal con la semana ficticia del material (15 tareas). El grupo ve cómo la IA propone bloques horarios y agrupa tareas similares.",
        "Reuniones: orden del día, briefing previo, preguntas clave. Muestra cómo preparar una reunión en 5 minutos con IA vs los 20-30 minutos habituales. Pregunta: '¿Cuántas reuniones tenéis esta semana sin orden del día?'",
        "Transcripciones y privacidad: punto crítico. Antes de grabar cualquier reunión, consentimiento. Antes de subir la transcripción a ChatGPT, verificar que no hay datos confidenciales.",
        "Actividad 1 — Semana ficticia (30 min). Proporciona las 15 tareas con estimaciones. Trabajan colectivamente. Circula y ayuda con las restricciones ('tengo reunión fija el martes a las 16h').",
        "Actividad 2 — Mi próxima semana real (50 min). Este es el entregable que se llevan. Insiste en que usen tareas reales. Al final, pide voluntarios que compartan su plan.",
        "Notas → acta (25 min) y mini-entregable: el plan semanal. Que cada alumno comparta una decisión de priorización que les sorprendió hacer con IA.",
    ],

    "D09": [
        "Arranca M4 sesión 2 y cierre del módulo de organización. Conecta con D08: ya planifican y preparan reuniones. Hoy cierran el ciclo: qué pasa después de la reunión.",
        "Dato de impacto: el 60% de los acuerdos tomados en reuniones sin acta no se ejecutan en el plazo acordado. Con acta estructurada, baja al 25%. Pregunta: '¿Cuántas de vuestras reuniones tienen acta?' Normalmente la respuesta es pocas.",
        "Anatomía del acta útil: no es una transcripción, es un documento de acción. Escribe en la pizarra: DECISIONES + ACCIONES (tabla) + PRÓXIMA REUNIÓN. Eso es todo lo que importa.",
        "Demuestra el prompt de acta: pega las notas crudas del material y genera el acta en tiempo real. El grupo ve la diferencia entre el caos de las notas y la claridad del resultado.",
        "Tablero kanban en texto: no necesitan Trello ni Asana. ChatGPT genera una tabla kanban con columnas Pendiente / En curso / Bloqueado / Completado. Demuestra con el proyecto ficticio del material.",
        "Sistema RAG (🔴🟡🟢): explica que es el estándar internacional para semáforos de seguimiento. Muestra cómo la IA rellena el estado inicial y cómo el equipo lo actualiza manualmente.",
        "Instrucciones de delegación — los 5 elementos: QUÉ / POR QUÉ / CUÁNDO / CÓMO / CÓMO INFORMAR. El 'por qué' es el más olvidado y el más importante: sin contexto, la persona delegada no puede tomar buenas decisiones ante imprevistos.",
        "Recordatorios: muestra los dos prompts (primer seguimiento / segundo seguimiento sin respuesta). La diferencia de tono entre ambos es sutil pero importante. Pregunta: '¿Tenéis tareas delegadas que llevan semanas sin respuesta?'",
        "Actividad 1 — Transcripción → acta + plan de acción (40 min). Proporciona la transcripción ficticia. El grupo trabaja en grupos de 2-3. Compara las actas resultantes: ¿coinciden en las decisiones y responsables?",
        "Actividad 2 — Mi kanban (35 min). Cada alumno crea un tablero para una iniciativa real. Circula y ayuda a definir qué va en cada columna.",
        "Actividad 3 — 3 delegaciones reales (30 min) y mini-entregable: el kit de organización (acta + kanban + delegación). Cierra M4: '¿Qué vais a hacer diferente la próxima semana?'",
    ],
}

# ── FUNCIONES ─────────────────────────────────────────────────────────────────

def detect_day(filename):
    """Extrae el código de día (D05, D06...) del nombre del archivo."""
    import re
    basename = os.path.basename(filename).upper()
    match = re.search(r'D(\d{2})', basename)
    if match:
        return f"D{match.group(1)}"
    return None


def logo_already_added(slide):
    """Comprueba si ya hay un logo AllWomen en la slide (posición top-right)."""
    for shape in slide.shapes:
        if shape.shape_type == 13:  # PICTURE
            left_in = shape.left / 914400
            width_in = shape.width / 914400
            # Si hay una imagen pequeña en la esquina derecha, es el logo
            if width_in < 3 and left_in > 14:
                return True
    return False


def add_logo(slide):
    """Añade el logo AllWomen si no está ya."""
    if logo_already_added(slide):
        return
    if not os.path.exists(LOGO_PATH):
        print(f"  ⚠️  Logo no encontrado: {LOGO_PATH}")
        return
    slide.shapes.add_picture(LOGO_PATH, LOGO_LEFT, LOGO_TOP, LOGO_WIDTH)


def add_notes(slide, note_text):
    """Añade o reemplaza las speaker notes de una slide."""
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = note_text


def process_deck(pptx_path):
    day = detect_day(pptx_path)
    if day not in NOTES:
        print(f"⚠️  {os.path.basename(pptx_path)}: no hay notas para '{day}'. "
              f"Días disponibles: {list(NOTES.keys())}")
        print("   Solo se añadirá el logo.")
        day_notes = []
    else:
        day_notes = NOTES[day]

    print(f"\n📂 Procesando {os.path.basename(pptx_path)} → {day}")
    prs = Presentation(pptx_path)
    slides = list(prs.slides)
    print(f"   {len(slides)} slides detectadas")

    for i, slide in enumerate(slides):
        # Logo
        add_logo(slide)
        # Notas
        if i < len(day_notes):
            add_notes(slide, day_notes[i])
            print(f"   Slide {i+1}: logo ✅  notas ✅")
        else:
            print(f"   Slide {i+1}: logo ✅  notas — (sin nota definida para esta slide)")

    prs.save(pptx_path)
    print(f"   💾 Guardado: {pptx_path}")


# ── MAIN ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    for path in sys.argv[1:]:
        if not os.path.exists(path):
            print(f"⚠️  Archivo no encontrado: {path}")
            continue
        if not path.lower().endswith(".pptx"):
            print(f"⚠️  No es un .pptx: {path}")
            continue
        process_deck(path)

    print("\n✅ Procesado completado.")
