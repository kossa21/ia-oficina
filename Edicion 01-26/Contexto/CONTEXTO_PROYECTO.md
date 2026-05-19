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

El proceso para cada sesión es siempre el mismo:

**Paso 1 — Brief**
Creo (con Claude) un documento `DXX_Brief_NotebookLM.md` con la estructura del contenido de la sesión: objetivos, teoría, actividades, mini-entregable, mensaje clave.

**Paso 2 — NotebookLM**
En [notebooklm.google.com](https://notebooklm.google.com):
- Creo un notebook con el nombre estándar (ver tabla más abajo)
- Subo el brief como única fuente
- Uso el prompt de referencia en el chat para pedir la presentación
- Descargo el PPTX generado

**Paso 3 — Procesado (en el Mac con Claude/Cowork)**
Claude ejecuta un script Python (`process_decks.py`) que:
- Añade el logo de AllWomen (full color, esquina superior derecha) a cada slide
- Añade speaker notes en cada slide basadas en el contenido del brief
- Guarda el PPTX final en la carpeta compartida

---

## Estado de avance actual

| Día | Brief | Notebook creado | Deck generado | Deck procesado (logo+notas) |
|-----|-------|----------------|--------------|----------------------------|
| D01 | ✅ | ✅ | ✅ | ✅ `D01_Practical_Office_AI.pptx` |
| D02 | ✅ | ✅ | ✅ | ✅ `D02_The_Prompting_Blueprint.pptx` |
| D03 | ✅ | ✅ | ✅ | ✅ `D03_The_AI_Assembly_Line.pptx` |
| D04 | ✅ | ✅ | ✅ | ✅ `D04_AI_Office_Automation.pptx` |
| D05 | ✅ | ✅ | ⏳ por generar en NLM | — |
| D06 | ✅ | ✅ | ⏳ | — |
| D07 | ✅ | ✅ | ⏳ | — |
| D08 | ✅ | ✅ | ⏳ | — |
| D09 | ✅ | ✅ | ⏳ | — |
| D10 | ❌ por crear | — | — | — |
| D11 | ❌ | — | — | — |
| D12 | ❌ | — | — | — |
| D13 | ❌ | — | — | — |
| D14 | ❌ | — | — | — |
| D15 | ❌ | — | — | — |
| D16 | ❌ | — | — | — |
| D17 | ❌ | — | — | — |

---

## Notebooks de NotebookLM — nombres y prompts

### Notebooks creados (D01–D09)

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

### Prompt estándar para generar la presentación en NotebookLM

Ajusta el tema según la sesión:

> Genera una presentación visualmente rica para [TEMA DE LA SESIÓN]. Usa títulos provocadores y narrativos, no descriptivos. Cada slide debe tener un elemento visual (diagrama, estadística, comparativa o iconos). Incluye una slide de portada, slides de contenido (máx. 5 puntos cortos por slide), y una slide final de cierre con la misión para la próxima sesión. Tono: directo, accesible, sin tecnicismos. Público: personal administrativo sin experiencia previa en IA.

Si el resultado no convence, añadir:
> *"Prioriza datos numéricos, comparativas visuales y analogías concretas sobre listas de texto."*

---

## Decisiones importantes ya tomadas

- **Estética de NotebookLM:** aprobada por Daniela (contacto en INSERTA). No cambiar de herramienta.
- **Un notebook por sesión** (no por módulo): genera resultados más limpios y enfocados.
- **Logo AllWomen:** full color (no negro), esquina superior derecha, 1.2" de ancho. Se añade programáticamente con Python, no manualmente.
- **Speaker notes:** se generan desde el brief y se añaden automáticamente al PPTX. NotebookLM no puede generarlas directamente.
- **Privacidad:** el brief es el único documento que entra a NotebookLM. Nunca datos reales de alumnos.

---

## Estructura del brief (para crear D10–D17)

Cada brief tiene estas secciones:

1. **Contexto del curso** (datos generales, qué sabe ya el grupo en ese punto)
2. **Estructura de la sesión** (tabla con bloques: apertura 15min, teórico 75min, descanso 15min, práctica 105min, puesta en común 30min)
3. **Objetivos de aprendizaje** (3–4 objetivos concretos)
4. **Contenidos teóricos** (con tablas, estadísticas, analogías, prompts de ejemplo)
5. **Actividades en aula** (2–3 actividades con duración, descripción y objetivo)
6. **Mini-entregable del día** (nombre, formato, contenido)
7. **Mensaje clave de la sesión** (frase memorable)
8. **Conexión con el resto del curso**

---

## Posibilidades exploradas (para tener en cuenta)

- **NotebookLM compartido con alumnos:** viable. Modo público ("anyone with the link"). Cada alumno tiene su propia sesión de chat independiente. Límite: 50 preguntas/día por usuario (cuenta gratuita). Los viewers pueden chatear y ver contenido generado por el owner, pero no generar nuevo contenido en Studio.
- **Google Classroom:** explorado como LMS para distribuir materiales y recoger entregables. Gratis con Gmail. Pendiente confirmar si INSERTA tiene plataforma propia o si Ananda puede usar su cuenta allwomen.tech para crear clases.
- **Formatos alternativos desde NotebookLM:** audio overview (podcast IA), flashcards, study guide, briefing doc — todos generables desde el mismo notebook para que los alumnos elijan su formato de repaso preferido.

---

## Tareas pendientes

1. Generar los decks D05–D09 en NotebookLM y subirlos a Claude (Cowork en Mac) para procesar logo+notas
2. Crear los briefs D10–D17 (M5, M6, M7, M8)
3. Confirmar con INSERTA si tienen LMS institucional o si se usa Google Classroom
4. Confirmar con AllWomen si la cuenta allwomen.tech tiene Google Classroom habilitado para crear clases

---

*Documento generado el 19 de mayo de 2026 · Actualizar cuando haya cambios relevantes*
