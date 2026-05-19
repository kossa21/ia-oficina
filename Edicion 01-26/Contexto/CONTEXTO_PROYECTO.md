# Contexto del proyecto — IA en la Oficina 01/26
*Documento para continuar el trabajo en cualquier sesión de Claude*

---

## Quién soy

Soy Ananda (Anandamaya Arnó), formadora en **AllWomen** (ananda@allwomen.tech). Estoy desarrollando un curso de formación en IA para **INSERTA Empleo / Fundación ONCE / Talento Digital**. Trabajo en español. Los archivos y nombres de decks pueden estar en inglés porque los genera NotebookLM automáticamente.

---

## El curso

**Nombre:** IA en la Oficina – Eficiencia y Productividad
**Edición:** 01/26
**Duración:** 68 horas · 17 sesiones de 4h
**Fechas:** 1 julio – 23 julio 2026 · Horario: 15:00–19:00h
**Alumnado:** ~10 personas, perfil administrativo/oficina, sin experiencia previa en IA, perfiles muy diversos
**Clientes:** Fundación ONCE · Inserta Empleo · Talento Digital

---

## Estructura de módulos y calendario

| Día | Fecha | Módulo | Sesión |
|-----|-------|--------|--------|
| D01 | Mié 1 Jul | M1 | IA generativa, herramientas y privacidad |
| D02 | Jue 2 Jul | M2 | Prompts básicos — estructura R-C-T-F-R |
| D03 | Vie 3 Jul | M2 | Prompts avanzados — encadenamiento e iteración |
| D04 | Lun 6 Jul | M3 | Automatización de tareas repetitivas |
| D05 | Mar 7 Jul | M3 | Resúmenes y transformación de formatos |
| D06 | Mié 8 Jul | M3 | Correos profesionales y situaciones difíciles |
| D07 | Jue 9 Jul | M3 | Redacción de informes con IA |
| D08 | Vie 10 Jul | M4 | Planificación semanal y gestión de reuniones |
| D09 | Lun 13 Jul | M4 | Actas, seguimiento y delegación |
| D10 | Mar 14 Jul | M5 | Análisis de datos sin ser experto en Excel |
| D11 | Mié 15 Jul | M5 | Búsqueda, síntesis e informes de mercado |
| D12 | Jue 16 Jul | M6 | Canva con IA — presentaciones e imágenes |
| D13 | Vie 17 Jul | M6 | Material visual, social y comunicación interna |
| D14 | Lun 20 Jul | M7 | Gestión documental y flujos de trabajo |
| D15 | Mar 21 Jul | M7 | Atención al cliente y procesos recurrentes |
| D16 | Mié 22 Jul | M8 | Taller integrador — proyecto personal con IA |
| D17 | Jue 23 Jul | M8 | Presentaciones finales y cierre del curso |

**Módulos resumidos:**
- M1 — ¿Qué es la IA? (1 sesión, 4h)
- M2 — Ingeniería de prompts para principiantes (2 sesiones, 8h)
- M3 — Redacción y comunicación con IA (4 sesiones, 16h)
- M4 — Organización del trabajo con IA (2 sesiones, 8h)
- M5 — Análisis fácil de información con IA (2 sesiones, 8h)
- M6 — Creatividad y diseño para no expertos (2 sesiones, 8h)
- M7 — Organizando la oficina con IA (2 sesiones, 8h)
- M8 — Proyecto final y práctica real (2 sesiones, 8h)

---

## Workflow de producción de materiales

El brief alimenta **dos flujos en paralelo** a partir de la Edición 01/26:

**Paso 1 — Brief**
Creo (con Claude) un documento `DXX_Brief_NotebookLM.md` con la estructura completa de 22 secciones y ≥ 450 líneas: teoría en prosa con bloques `**Puntos clave:**`, ≥ 4 ejemplos resueltos, glosario de 12–15 términos, cuestionario de 15 preguntas, ≥ 10 FAQ, 3 actividades, callouts 🔁 y 🎓. El brief es la fuente única y la verdad del material del día.

**Paso 2a — NotebookLM (formatos cara al alumno)**
En [notebooklm.google.com](https://notebooklm.google.com):
- Creo un notebook con el nombre estándar (ver tabla más abajo)
- Subo el brief como única fuente
- Uso los prompts de `Recursos/NotebookLM_Prompts_Referencia.md` para generar Audio Overview (pódcast), Video Overview, infografía, flashcards, cuestionario, FAQ y guía de estudio
- Los alumnos reciben el enlace público del notebook y lo consumen en el formato que prefieran
- **Importante:** NotebookLM no controla la estructura del deck del formador (verificado en producción — ignora cualquier instrucción de estructura vía chat, botón Crear o fuente adicional). Solo se usa para formatos cara al alumno.

**Paso 2b — `generar_deck.py` (deck del formador)**
```
python3 Scripts/generar_deck.py DXX
```
El script parsea el brief y emite `Decks/DXX_procesado.pptx` con:
- Paleta AllWomen, logo full color esquina superior derecha, footer
- Slides de portada, agenda, objetivos, conceptos (bullets desde `**Puntos clave:**`), datos, ejemplos, errores, glosario, práctica y cierre
- Notas del orador extraídas literalmente de la prosa del brief
- **Regla de oro:** el script no inventa ningún contenido. Si el brief no lo tiene, el PPTX no lo lleva.

`Scripts/process_decks.py` — **DEPRECADO** (legacy): solo añadía logo con speaker notes hardcodeadas por día. No usar para nuevos decks.

---

## Estado de avance actual

| Día | Brief | Notebook creado | Deck generado | Deck procesado (logo+notas) |
|-----|-------|----------------|--------------|----------------------------|
| D01 | ✅ revisado | ✅ | ✅ | ✅ `D01_Practical_Office_AI.pptx` |
| D02 | ✅ revisado | ✅ | ✅ | ✅ `D02_The_Prompting_Blueprint.pptx` |
| D03 | ✅ revisado | ✅ | ✅ | ✅ `D03_The_AI_Assembly_Line.pptx` |
| D04 | ✅ revisado | ✅ | ✅ | ✅ `D04_AI_Office_Automation.pptx` |
| D05 | ✅ revisado | ✅ | ⏳ por generar en NLM | — |
| D06 | ✅ revisado | ✅ | ⏳ | — |
| D07 | ✅ revisado | ✅ | ⏳ | — |
| D08 | ✅ revisado | ✅ | ⏳ | — |
| D09 | ✅ revisado | ✅ | ⏳ | — |
| D10 | ✅ nuevo | ⏳ por crear | — | — |
| D11 | ✅ nuevo | ⏳ | — | — |
| D12 | ✅ nuevo | ⏳ | — | — |
| D13 | ✅ nuevo | ⏳ | — | — |
| D14 | ✅ nuevo | ⏳ | — | — |
| D15 | ✅ nuevo | ⏳ | — | — |
| D16 | ✅ nuevo | ⏳ | — | — |
| D17 | ✅ nuevo | ⏳ | — | — |

---

## Notebooks de NotebookLM — nombres estándar

### Notebooks existentes (D01–D09)

| Notebook | Brief | Sesión |
|----------|-------|--------|
| `IA Oficina 01/26 — D01 Qué es la IA` | D01_Brief_NotebookLM.md | M1 |
| `IA Oficina 01/26 — D02 Prompts Básicos` | D02_Brief_NotebookLM.md | M2 S1 |
| `IA Oficina 01/26 — D03 Prompts Avanzados` | D03_Brief_NotebookLM.md | M2 S2 |
| `IA Oficina 01/26 — D04 Tareas Repetitivas` | D04_Brief_NotebookLM.md | M3 S1 |
| `IA Oficina 01/26 — D05 Resúmenes y Formatos` | D05_Brief_NotebookLM.md | M3 S2 |
| `IA Oficina 01/26 — D06 Correos Profesionales` | D06_Brief_NotebookLM.md | M3 S3 |
| `IA Oficina 01/26 — D07 Informes con IA` | D07_Brief_NotebookLM.md | M3 S4 |
| `IA Oficina 01/26 — D08 Planificación Semanal` | D08_Brief_NotebookLM.md | M4 S1 |
| `IA Oficina 01/26 — D09 Actas y Delegación` | D09_Brief_NotebookLM.md | M4 S2 |

### Notebooks por crear (D10–D17)

| Notebook | Brief | Sesión |
|----------|-------|--------|
| `IA Oficina 01/26 — D10 Análisis de Datos` | D10_Brief_NotebookLM.md | M5 S1 |
| `IA Oficina 01/26 — D11 Búsqueda e Informes` | D11_Brief_NotebookLM.md | M5 S2 |
| `IA Oficina 01/26 — D12 Canva con IA` | D12_Brief_NotebookLM.md | M6 S1 |
| `IA Oficina 01/26 — D13 Comunicación Visual` | D13_Brief_NotebookLM.md | M6 S2 |
| `IA Oficina 01/26 — D14 Gestión Documental` | D14_Brief_NotebookLM.md | M7 S1 |
| `IA Oficina 01/26 — D15 Atención al Cliente` | D15_Brief_NotebookLM.md | M7 S2 |
| `IA Oficina 01/26 — D16 Proyecto Personal` | D16_Brief_NotebookLM.md | M8 S1 |
| `IA Oficina 01/26 — D17 Presentaciones Finales` | D17_Brief_NotebookLM.md | M8 S2 |

---

## Decisiones importantes ya tomadas

### Validadas desde el inicio
- **Estética de NotebookLM:** aprobada por Daniela (contacto en INSERTA). No cambiar de herramienta.
- **Un notebook por sesión** (no por módulo): genera resultados más limpios y enfocados.
- **Logo AllWomen:** full color (no negro), esquina superior derecha, 1.2" de ancho. Se añade programáticamente con Python, no manualmente.
- **Speaker notes:** se generan desde el brief y se añaden automáticamente al PPTX. NotebookLM no puede generarlas directamente.
- **Privacidad:** el brief es el único documento que entra a NotebookLM. Nunca datos reales de alumnos ni de clientes.

### Decisiones tomadas en la revisión de mayo 2026 (densidad + script deck)

- **Solo herramientas gratuitas con cuenta Gmail personal.** Microsoft Copilot eliminado de todos los briefs y recursos. Nunca se menciona como herramienta del curso; solo como "opcional si tu empresa ya te lo da". Mapa de sustituciones: Copilot en Word → Gemini en Google Docs / ChatGPT copy-paste; Copilot en Teams → Tactiq free / captions de Meet / audio+IA; GPTs Plus → Gemini Gems / Google Doc biblioteca de prompts.

- **Reparto de sesión: ~40 % teoría+demo / ~50 % práctica / ~10 % puesta en común.** Estructura fija 15+75+15+95+40 = 240 min. El reparto antiguo (25/65/10, tabla 105 min práctica, 30 min puesta en común) queda obsoleto.

- **El brief es la fuente única y multiformato de cara al alumno.** Cada día Ananda comparte el enlace del notebook del día (modo público). Los alumnos lo consumen en el formato que prefieran: Audio Overview (podcast), Video Overview, infografía/mapa mental, guía de estudio, documento informativo, flashcards, cuestionario, o haciendo preguntas al chat. El brief debe nutrir todos esos outputs; no puede ser un esqueleto de viñetas.

- **Los briefs D01–D09 han sido revisados** a la plantilla rica de 22 secciones. Los briefs D10–D17 han sido creados nuevos con la misma plantilla. **Todos pendientes de ampliación a ≥ 450 líneas** con los nuevos mínimos cuantitativos (Fase 3 del plan de trabajo).

- **Nuevo estándar de densidad ≥ 450 líneas** con mínimos cuantitativos por sección: ≥ 8 conceptos en §6, ≥ 8 datos en §7, ≥ 4 ejemplos en §8, 12–15 términos de glosario, ≥ 8 errores/buenas prácticas, 15 preguntas de cuestionario, ≥ 10 FAQ, 7 bullets en §20, 3 actividades completas con rúbrica. Ver tabla completa en `Recursos/Plantilla_Brief.md`.

- **NotebookLM no controla la estructura del deck** (verificado en producción). Cualquier instrucción de formato de diapositiva enviada vía chat, botón Crear o fuente adicional es ignorada. Decisión: el deck del formador se genera con `Scripts/generar_deck.py` a partir del brief. NotebookLM se reserva para los formatos cara al alumno (audio, vídeo, infografía, flashcards, cuestionario, FAQ, chat).

- **Regla de oro del script `generar_deck.py`:** todo el contenido textual del PPTX viene del brief. El script no inventa pedagogía, ejemplos, prompts, datos, citas, glosario ni notas del orador. Si el brief no lo tiene, el PPTX no lo lleva.

- **Marcador `**Puntos clave:**` obligatorio en §6.** Cada subsección `### concepto` del desarrollo teórico debe terminar con un blockquote `> **Puntos clave:** / > - bullet ≤ 15 palabras` (≤ 5 bullets). El script los lee literalmente para los bullets de la slide de ese concepto. Sin el marcador, el script usa la primera oración de cada párrafo como fallback y emite warning.

- **Hilo del proyecto final individual (D16–D17):** sembrado en D01 (callout 🎓 SIEMBRA: mapa de oportunidades), checkpoint en D09 (callout 🎓 CHECKPOINT: el alumno fija su idea), build en D16 (callout 🎓 BUILD: sprint individual con mentoría), presentación en D17 (callout 🎓 PRESENTACIÓN).

- **Trabajo en parejas/grupo explícito:** cada brief tiene un callout 🔁 con la dinámica colaborativa de la sesión y ≥1 actividad etiquetada Pareja o Grupo.

- **No se crean M5–M8 module briefs.** Los M-briefs son material de apoyo redundante; el brief operativo (lo que entra a NotebookLM) es el D-brief por sesión. M1–M4 se conservan en `Briefs/Modulos_overview/` con banner de "documento de consulta (no fuente NotebookLM)" y se parchean para eliminar referencias a Copilot y al reparto 25/65/10.

- **Banco de ejercicios:** `Recursos/Banco_de_Ejercicios.md` cubre los 17 días con 3 ejercicios por día (EJ-DXX-1 Individual, EJ-DXX-2 Pareja, EJ-DXX-3 Grupo). Los briefs referencian estos códigos en la sección "Ejercicios sugeridos".

- **Guía del alumno:** `Recursos/Guia_Alumno_NotebookLM.md` explica a los alumnos cómo abrir el enlace del notebook y generar/consumir cada formato. Límite ~50 preguntas/día en cuenta gratuita.

---

## Estructura del brief (plantilla canónica — 22 secciones)

La fuente de verdad es `Recursos/Plantilla_Brief.md`. Los títulos `## N. NOMBRE` son anclas del parser de `generar_deck.py` — **no renombrar**. Resumen con nuevos mínimos:

1. Cabecera (curso, módulo, día X de 17, fecha, horario)
2. Contexto del curso (recap sesión anterior + nota de uso del notebook)
3. Resumen de la sesión (**8–10 frases**)
4. Estructura de la sesión (tabla 15/75/15/95/40 = 240 min)
5. Objetivos de aprendizaje (3–4, verbos de acción)
6. Desarrollo teórico en prosa (**≥ 8 conceptos** `### nombre`, cada uno con prosa 80–120 palabras + analogía + Marta + bloque `**Puntos clave:**`)
7. Datos y cifras clave (**≥ 8 bullets** con cifras)
8. Ejemplos resueltos paso a paso (**≥ 4 casos** con Situación/Prompt/Resultado/Iteración)
9. Glosario (**12–15 términos**)
10. Errores comunes y buenas prácticas (**≥ 8 entradas**)
11. Actividades en aula (**3 actividades** con modalidad, duración, consigna, entregable, rúbrica)
12. 🔁 Trabajo en parejas/grupo (callout separado, nunca vacío)
13. Ejercicios sugeridos (códigos EJ-DXX-N del banco)
14. Cuestionario de autoevaluación (**15 preguntas** con respuestas razonadas)
15. Preguntas frecuentes / FAQ (**≥ 10** preguntas con respuesta 2–4 frases)
16. Herramientas de la sesión (solo gratuitas)
17. Mini-entregable del día
18. 🎓 Hilo del proyecto final (callout en D01, D09, D16, D17; línea en el resto)
19. Mensaje clave
20. Ideas para recordar (**exactamente 7 bullets**)
21. Conexión con el resto del curso
22. Footer `*Brief para NotebookLM · DXX · Edición 01/26*`

---

## Posibilidades exploradas (para tener en cuenta)

- **NotebookLM compartido con alumnos:** viable. Modo público ("anyone with the link"). Cada alumno tiene su propia sesión de chat independiente. Límite: ~50 preguntas/día por usuario (cuenta gratuita). Los viewers pueden chatear y ver contenido generado por el owner, pero no generar nuevo contenido en Studio.
- **Google Classroom:** explorado como LMS para distribuir materiales y recoger entregables. Gratis con Gmail. Pendiente confirmar si INSERTA tiene plataforma propia o si Ananda puede usar su cuenta allwomen.tech para crear clases.
- **Formatos alternativos desde NotebookLM:** Audio Overview (podcast IA), Video Overview, infografía/mapa mental, guía de estudio, documento informativo, flashcards, cuestionario — todos generables desde el mismo notebook.

---

## Tareas pendientes

1. **[En curso — Fase 3]** Ampliar los 17 briefs a ≥ 450 líneas cumpliendo mínimos A1–A11, añadiendo bloque `**Puntos clave:**` en cada concepto de §6
2. **[En curso — Fase 4]** Crear `Scripts/generar_deck.py` — parser brief → PPTX completo sin contenido inventado
3. **[En curso — Fase 5]** Limpiar `Recursos/NotebookLM_Prompts_Referencia.md` (eliminar instrucciones de estructura del deck) y ajustar `Scripts/pipeline_ia_oficina.py`
4. Crear los notebooks D10–D17 en NotebookLM y subirles sus briefs
5. Confirmar con INSERTA si tienen LMS institucional o si se usa Google Classroom
6. Confirmar con AllWomen si la cuenta allwomen.tech tiene Google Classroom habilitado

---

*Documento actualizado el 19 de mayo de 2026 (Fase 2: doctrina ≥450 líneas + script generar_deck) · Actualizar cuando haya cambios relevantes*
