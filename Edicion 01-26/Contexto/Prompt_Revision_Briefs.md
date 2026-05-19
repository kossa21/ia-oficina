# Prompt para revisión y enriquecimiento de briefs — IA en la Oficina 01/26

> **Uso:** copiar el bloque entre `===` íntegro y pegarlo como primer mensaje en una nueva sesión de Claude Code conectada al repo `kossa21/ia-oficina`, rama `claude/plan-ai-course-6WxJC`. El prompt está pensado para una sesión de trabajo completa: incluye contexto, problema, criterios cuantitativos y reglas de decisión.

---

================== INICIO DEL PROMPT ==================

# Misión

Eres responsable de revisar y enriquecer los **17 briefs** del curso *IA en la Oficina – Eficiencia y Productividad · Edición 01/26* para que las presentaciones generadas por Google NotebookLM tengan **suficiente densidad de contenido para cubrir con calidad las 4 horas lectivas de cada sesión**. El problema actual es que los decks generados se quedan cortos: faltan slides, los conceptos se atropellan, y no hay material para llenar el bloque teórico-demostrativo de 75 minutos.

Tu trabajo NO es regenerar los decks (eso lo hace Ananda con NotebookLM). Tu trabajo es **trabajar sobre la fuente** — los briefs Markdown — para que, cuando NotebookLM los procese, produzca decks completos.

---

# Contexto del curso

**Producto:** Curso *IA en la Oficina – Eficiencia y Productividad*, edición 01/26.
**Cliente:** Fundación ONCE · Inserta Empleo · Talento Digital.
**Formato:** 17 sesiones presenciales × 4 horas = **68 horas lectivas**.
**Público:** personal administrativo sin experiencia previa en IA. Diversidad funcional contemplada (accesibilidad como criterio transversal).
**Formadora:** Ananda (AllWomen).

**Estructura estándar de cada sesión (240 min):**

| Bloque | Duración | Función |
|---|---|---|
| Apertura | 15 min | Repaso sesión anterior + objetivos del día |
| Teórico-demostrativo | 75 min | Conceptos + demos en vivo |
| Descanso | 15 min | — |
| Práctica guiada | 95 min | Ejercicios individuales / parejas / grupo |
| Puesta en común | 40 min | Revisión de entregables + recap + mañana |

Reparto pedagógico: **~40 % teoría+demo / ~50 % práctica / ~10 % puesta en común**.

**Reglas no negociables:**
- **Todo gratuito con cuenta Google personal.** Nada de Microsoft Copilot, M365 o ChatGPT Plus (los alumnos usan Gmail personal). Las sustituciones aprobadas están en `Edicion 01-26/Recursos/Herramientas_Gratuitas.md`.
- **Foco oficina/administración** (procesos administrativos y financieros). Creatividad y datos solo en sus módulos dedicados (M5 datos, M6 diseño/comunicación visual).
- **Trabajo en parejas/grupo explícito** en cada sesión (callout 🔁).
- **Hilo del proyecto final individual**: callout 🎓 en D01 (siembra), D09 (checkpoint a mitad de curso), D16 (build) y D17 (presentación).
- **Privacidad:** los alumnos nunca pegan datos reales en NotebookLM ni en otras herramientas — siempre anonimización.

**Workflow del material (importante para entender por qué hace falta más densidad):**
1. Ananda redacta/edita el brief `DXX_Brief_NotebookLM.md`.
2. Sube el brief como fuente única en un notebook de Google NotebookLM.
3. NotebookLM genera **todos los formatos** a partir de esa fuente: deck (con un PROMPT específico definido en `Recursos/NotebookLM_Prompts_Referencia.md`), Audio Overview (podcast), Video Overview, infografía/mapa mental, guía de estudio, documento informativo, flashcards, cuestionario, FAQ.
4. Ananda comparte el enlace público del notebook con los alumnos. **Cada alumno consume el formato que quiera y chatea con el notebook.**
5. El script `Scripts/process_decks.py` solo añade el logo de AllWomen al PPTX descargado — **toda la estructura del deck y las notas del formador vienen del PROMPT a NotebookLM, no del script**.

→ Por tanto, **si el brief es escueto, NotebookLM produce un deck escueto, un podcast pobre, flashcards repetitivas, etc.** El brief es el cuello de botella.

---

# Problema concreto a resolver

Los decks que NotebookLM está generando con los briefs actuales son **demasiado cortos** para sostener una sesión de 4 horas. Se nota especialmente en el bloque teórico-demostrativo de 75 min: la formadora se queda sin material a mitad del bloque o tiene que improvisar transiciones porque los conceptos no están desarrollados con suficiente profundidad en el brief.

**No queremos:**
- Quedarnos cortos en clase.
- Que la formadora tenga que rellenar con improvisación.
- Que el podcast/audio overview dure 3 minutos por falta de sustancia.
- Que las flashcards tengan 4 términos.

**Queremos:**
- Decks con la densidad correcta para llenar 75 min de teoría + 15 min de apertura + 40 min de puesta en común (≈130 min de slides activos).
- Suficiente material para que cualquier formato derivado (audio, vídeo, infografía, flashcards, cuestionario, FAQ) tenga sustancia.
- Que el alumno pueda preguntar al chat con resultados ricos.

---

# Criterios cuantitativos mínimos (esto es lo nuevo)

## A) Densidad mínima del BRIEF (fuente Markdown)

Cada brief debe cumplir **TODOS** estos mínimos. Si no llegan, hay que **ampliar contenido** (ver regla de decisión más abajo).

| Sección | Mínimo anterior | **Mínimo nuevo** |
|---|---|---|
| Longitud total | 250 líneas | **≥ 450 líneas** |
| Resumen ejecutivo | 5–6 frases | 8–10 frases |
| Desarrollo teórico en prosa | "varios párrafos" | **≥ 8 conceptos clave, cada uno con párrafo de 80–120 palabras + analogía + escenario de oficina con la protagonista "Marta"** |
| Datos y cifras clave | lista breve | **≥ 8 datos/estadísticas/comparativas con fuente o contexto** |
| Ejemplos resueltos paso a paso | 2–3 | **≥ 4 ejemplos completos** (situación → prompt exacto → resultado comentado → 1 iteración de mejora) |
| Glosario | 6–12 términos | **12–15 términos** con definición de una frase |
| Errores comunes y buenas prácticas | "lista" | **≥ 8 errores frecuentes**, cada uno con su corrección y por qué pasa |
| Cuestionario de autoevaluación | 8–12 preguntas | **15 preguntas** (mezcla opción múltiple + abiertas) con respuestas razonadas |
| Preguntas frecuentes (FAQ) | 6–10 | **≥ 10 preguntas** con respuesta de 2–4 frases |
| Ideas para recordar | 5 bullets | 7 bullets |
| Actividades en aula | 2–3 etiquetadas Ind/Pareja/Grupo | **3 actividades**, con duración, consigna, entregable esperado y rúbrica corta |

## B) Densidad mínima del DECK (lo que NotebookLM debe generar)

El PROMPT a NotebookLM en `Recursos/NotebookLM_Prompts_Referencia.md` ya define la estructura. Hay que **revisar y endurecer las cantidades** para que NotebookLM no se quede corto:

| Bloque de la sesión | Slides mínimos | Slides objetivo |
|---|---|---|
| Portada | 1 | 1 |
| Agenda del día | 1 | 1 |
| Apertura (objetivos + recap sesión anterior) | 3 | 4 |
| **Teórico-demostrativo** | **24** | **30–35** |
| Slides "🛠 AHORA: PRÁCTICA" (señal de ejercicio, una por actividad práctica) | 3 | 3 |
| Práctica — fichas de cada ejercicio (consigna + criterios) | 3 | 4 |
| Puesta en común (estructura + criterios de revisión) | 3 | 4 |
| Cierre — Lo que hicimos hoy | 1 | 1 |
| Cierre — Mañana (qué viene en DXX+1) | 1 | 1 |
| **TOTAL** | **40 slides** | **50–55 slides** |

**Cada slide debe llevar:**
- Título narrativo (no descriptivo): máx. 8 palabras, debe contar algo.
- ≤ 5 bullets, ≤ 15 palabras por bullet.
- **Un elemento visual** (diagrama, icono, comparativa, estadística destacada, mockup, captura anotada).
- **Notas del formador** de 2–3 frases: qué preguntar al grupo, qué demostrar en vivo, cuánto detenerse.

## C) Densidad mínima por formato derivado

Para que NotebookLM produzca formatos derivados ricos, el brief debe contener:

- **Audio Overview / Podcast:** prosa narrativa con la historia de Marta hilando la sesión → objetivo ≥ 12 minutos.
- **Video Overview:** mismo material que el audio, suficiente para 5–8 min de vídeo con slides.
- **Infografía / mapa mental:** ≥ 8 datos/cifras + estructura jerárquica clara (3–4 ramas grandes con 2–3 subramas cada una).
- **Flashcards:** ≥ 12 términos del glosario (mínimo de la sección A).
- **Cuestionario:** ≥ 15 preguntas (mínimo de la sección A).
- **FAQ:** ≥ 10 preguntas (mínimo de la sección A).
- **Guía de estudio:** los 8 conceptos clave en prosa + ejemplos resueltos + errores comunes (todo ya está en el brief si A está cumplido).

---

# Regla de decisión: ampliar contenido si el temario "se queda corto"

Si al revisar un brief detectas que **el temario actual no da para llegar a los mínimos de la sección A**, no rellenes con relleno. **Amplía el temario** siguiendo este árbol de decisión:

1. **¿Hay aspectos colaterales del tema del día que aportan valor real al alumno administrativo y no están cubiertos?**
   → Sí: añádelos como conceptos nuevos en el desarrollo teórico (con su analogía + escenario de Marta).
   *Ejemplos:* en D04 (redacción con IA) se podría profundizar en revisión gramatical, en adaptación de registro formal/informal por canal, en plantillas reutilizables. En D08 (planificación semanal) se podría añadir gestión de interrupciones y método de bloques.

2. **¿Hay herramientas gratuitas equivalentes que aún no se hayan mostrado y refuercen el tema?**
   → Sí: añade una comparativa o demo de una segunda herramienta.

3. **¿Hay un caso práctico realista del entorno administrativo/financiero que añadiría profundidad?**
   → Sí: añade un ejemplo resuelto adicional (caso de éxito, caso de error, caso límite).

4. **¿El tema necesita más datos/cifras/estadísticas que lo aterricen?**
   → Sí: añade evidencia (estudios, cifras de adopción, ahorros típicos de tiempo, benchmarks).

5. **¿El cuestionario y la FAQ están cubriendo todos los matices?**
   → Si no: añade preguntas sobre límites, privacidad, casos reales del puesto, decisiones (cuándo usar vs cuándo no).

6. **Solo como último recurso, si los pasos 1–5 ya están agotados y aún quedan slides por llenar:**
   → Propón al usuario (en un mensaje aparte, no en el brief) **añadir un sub-tema nuevo al temario** del curso. Justifica por qué encaja, qué módulo lo acoge y qué desplaza. **No lo añadas sin confirmación explícita.**

→ **La regla anti-relleno:** si tras agotar 1–5 sigues sin llegar a los mínimos, ese día probablemente **no debería ser una sesión de 4 horas completa** y hay que discutirlo. Mejor avisar que rellenar.

---

# Mapa del repositorio (lo que necesitas conocer)

```
Edicion 01-26/
├── README.md                       Índice del repo + workflow
├── Contexto/
│   ├── CONTEXTO_PROYECTO.md        Estado actual, decisiones, calendario
│   ├── Course requirements.pdf     PDF del cliente (9 contenidos oficiales)
│   └── Prompt_Revision_Briefs.md   ESTE prompt
├── Briefs/
│   ├── D01..D17_Brief_NotebookLM.md  Fuente única que sube a NotebookLM
│   └── Modulos_overview/M1..M4...    Documentos de consulta (deprecados)
├── Recursos/
│   ├── Plantilla_Brief.md             Plantilla canónica de 22 secciones
│   ├── NotebookLM_Prompts_Referencia.md   PROMPTS por sesión/formato
│   ├── Herramientas_Gratuitas.md      Sustituciones aprobadas
│   ├── Banco_de_Ejercicios.md         51 ejercicios EJ-DXX-N
│   ├── Guia_Alumno_NotebookLM.md      Guía PDF (cara al alumno)
│   └── Guia_Alumno_NotebookLM.pdf     PDF distribuido a alumnos
├── Decks/                          Salida de NotebookLM (no se versiona aquí)
├── Scripts/
│   ├── pipeline_ia_oficina.py     PROMPT consolidado para NotebookLM
│   ├── process_decks.py           Solo añade logo al PPTX descargado
│   └── generar_guia_alumno_pdf.py PDF de la guía del alumno
└── Logos/00_FULL COLOR (1).png    Logo AllWomen
```

**Antes de tocar nada, leer:**
1. `Contexto/CONTEXTO_PROYECTO.md` — estado y decisiones.
2. `Recursos/Plantilla_Brief.md` — plantilla canónica.
3. Un brief actual (p. ej. `Briefs/D05_Brief_NotebookLM.md`) para calibrar el nivel actual.
4. `Recursos/NotebookLM_Prompts_Referencia.md` — prompts que se mandan a NotebookLM.

---

# Plan de trabajo sugerido

1. **Calibración inicial (no editar todavía):**
   - Contar líneas, conceptos clave, ejemplos, glosario, cuestionario y FAQ de los 17 briefs.
   - Sacar tabla "brief → cumple A1 / A2 / … / A11" para ver dónde hay déficit.
   - Reportar la tabla al usuario antes de empezar a editar.

2. **Endurecer el PROMPT a NotebookLM** en `Recursos/NotebookLM_Prompts_Referencia.md` y en la constante `PROMPT` de `Scripts/pipeline_ia_oficina.py`:
   - Forzar el mínimo de **40 slides** y los rangos por bloque.
   - Forzar que cada slide del bloque teórico desarrolle **un solo concepto** (en vez de meter 3 conceptos en una slide).
   - Forzar notas del formador en cada slide.

3. **Ampliar los briefs uno a uno**, en orden D01 → D17:
   - Cumplir mínimos de la sección A.
   - Aplicar la regla de decisión cuando el tema "se quede corto".
   - Si necesitas añadir sub-tema nuevo al temario, **detenerse y preguntar** antes de hacerlo.

4. **Verificación** (sin ejecutar NotebookLM, no tenemos esa cuenta aquí):
   - Cada brief ≥ 450 líneas.
   - Cada brief con ≥ 8 conceptos teóricos, ≥ 4 ejemplos resueltos, ≥ 12 glosario, ≥ 15 cuestionario, ≥ 10 FAQ, ≥ 8 errores comunes.
   - Estructura de 22 secciones íntegra.
   - Callouts 🔁 y 🎓 en su sitio.
   - Cero referencias a Copilot/M365/ChatGPT Plus salvo las pedagógicas explícitas (D04 y D08).
   - Códigos `EJ-DXX-N` del brief existen en `Banco_de_Ejercicios.md` (sin huérfanos).

5. **Commit y push a `claude/plan-ai-course-6WxJC`** con mensajes claros por lote (p. ej. "Ampliar D01–D05 a densidad mínima nueva: +N líneas, +N conceptos, +N ejemplos").

---

# Restricciones de proceso

- **No tocar la arquitectura** (mapa de módulos, calendario, asignación de días). Solo profundidad de contenido.
- **No mover archivos** salvo que el usuario lo pida.
- **No regenerar el PDF de la guía del alumno** salvo que se modifique su contenido textual.
- **El script `process_decks.py` se queda como está** (logo-only, simplificado).
- **Idioma español neutro, accesible**, frases completas (debe sonar bien leído en voz alta — Audio Overview).
- **Nada de relleno.** Si llegas al techo del temario, párate y pregunta.
- **Reporte de estado cada 3–4 briefs** revisados (líneas añadidas, conceptos añadidos, decisiones tomadas) para que el usuario pueda redirigir antes de seguir.

---

# Output esperado al final del trabajo

- 17 briefs ampliados cumpliendo todos los mínimos de la sección A.
- `Recursos/NotebookLM_Prompts_Referencia.md` y la constante `PROMPT` de `pipeline_ia_oficina.py` actualizados con los mínimos de la sección B.
- `Contexto/CONTEXTO_PROYECTO.md` con una nota nueva en "Decisiones" describiendo el nuevo estándar de densidad y la regla anti-relleno.
- En caso de haber propuesto sub-temas nuevos al temario: lista clara de cuáles, dónde encajan y qué desplazan — **solo aplicada si el usuario dijo sí**.
- Commits limpios en `claude/plan-ai-course-6WxJC`.

================== FIN DEL PROMPT ==================

---

## Notas de uso

- Este prompt está pensado para una sesión larga. Si lo divides, mantén siempre el bloque "Criterios cuantitativos mínimos" y la "Regla de decisión" en cada subprompt.
- Si quieres que primero te entreguen solo la **tabla de calibración** (sin editar nada), recorta el "Plan de trabajo" a su paso 1 y añade: *"Detente tras la calibración y espera mi visto bueno antes de editar."*
- Si NotebookLM sigue generando decks cortos pese a brief enriquecido, el cuello de botella es el PROMPT — endurecerlo más en `NotebookLM_Prompts_Referencia.md` y `pipeline_ia_oficina.py`.
