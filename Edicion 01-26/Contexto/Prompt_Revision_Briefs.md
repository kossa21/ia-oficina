# Prompt para revisión y enriquecimiento de briefs — IA en la Oficina 01/26

> **Uso:** copiar el bloque entre `===` íntegro y pegarlo como primer mensaje en una nueva sesión de Claude Code conectada al repo `kossa21/ia-oficina`, rama `claude/plan-ai-course-6WxJC`. El prompt está pensado para una sesión de trabajo completa: incluye contexto, problema, criterios cuantitativos y reglas de decisión.

---

================== INICIO DEL PROMPT ==================

# Misión

Tienes dos tareas acopladas en este proyecto:

1. **Revisar y enriquecer los 17 briefs** del curso *IA en la Oficina – Eficiencia y Productividad · Edición 01/26* para que sean fuente densa y autocontenida — alimentan tanto los formatos de NotebookLM para el alumno (audio, vídeo, flashcards, cuestionario, FAQ, chat) como el deck del formador.
2. **Construir/renovar el script Python que genera el PPTX del deck del formador a partir del brief**, porque NotebookLM **no permite controlar la estructura del deck** (ver "Cambio de arquitectura del deck" más abajo). Toda la información que el script ponga en el PPTX debe **provenir del brief** — nada inventado.

El problema actual es doble: (a) los briefs se quedan cortos en densidad, así que cualquier formato derivado sale pobre; (b) NotebookLM ignora cualquier instrucción de estructura para el deck, así que el deck del formador hay que generarlo nosotros.

Tu trabajo NO es regenerar manualmente los decks en NotebookLM. Es **trabajar sobre el brief** (fuente única) y **dejar el script en condiciones de emitir el PPTX completo y estructurado** desde ese brief.

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

**Workflow del material:**
1. Ananda redacta/edita el brief `DXX_Brief_NotebookLM.md` — la **fuente única de verdad** del día.
2. **Camino alumno (NotebookLM):** sube el brief como fuente única a un notebook, genera y comparte el enlace público. NotebookLM genera Audio Overview (podcast), Video Overview, infografía/mapa mental, guía de estudio, documento informativo, flashcards, cuestionario, FAQ; el alumno consume el formato que prefiere y pregunta al chat.
3. **Camino formador (script Python):** un script parsea el mismo brief y emite el `Decks/DXX_procesado.pptx` con estructura, logo y notas del formador listas para la sesión. Sin pasar por NotebookLM.

→ El brief es el cuello de botella **doble**: si es escueto, ni los formatos de NotebookLM tienen sustancia ni el script tiene material que poner en las slides.

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

# Cambio de arquitectura del deck (descubrimiento verificado en producción)

**NotebookLM no acepta instrucciones de estructura para el slide deck.** Lo verificamos por las tres vías posibles:

- Pegar el prompt en el chat → NotebookLM responde con texto, no con un deck.
- Hacer clic en el botón "Crear" del panel de outputs → NotebookLM ignora cualquier prompt previo y aplica su lógica interna.
- Subir el prompt como fuente adicional → NotebookLM no lo procesa como instrucción.

**Consecuencia:** el deck del formador **no puede salir de NotebookLM con estructura controlada** (portada, agenda, slides "🛠 AHORA: PRÁCTICA" en su sitio, recap + mañana, notas del orador). NotebookLM se queda exclusivamente para los **formatos de cara al alumno** (Audio Overview, Video Overview, flashcards, cuestionario, FAQ, chat).

**Arquitectura nueva del deck:**

```
Brief.md  ──(NotebookLM, sin prompt)──→  audio, vídeo, flashcards, quiz, FAQ, chat para alumno
Brief.md  ──(script Python, parser)──→  PPTX del formador (estructurado, logo, notas)
```

Esto significa que el repo necesita un **script generador de deck que parsea el brief y emite el PPTX**, sustituyendo o ampliando el actual `Scripts/process_decks.py` (que hoy solo añade logo). La especificación del script va más abajo en "Tarea complementaria".

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

## B) Densidad mínima del DECK (lo que el script debe emitir desde el brief)

El script Python (ver "Tarea complementaria" más abajo) emite el PPTX a partir del brief. Estos son los mínimos por bloque, y son a la vez **la especificación de slides obligatorias del script** y **el contrato de qué secciones del brief deben tener contenido suficiente**:

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

**Cada slide del PPTX debe llevar:**
- Título narrativo (no descriptivo): máx. 8 palabras, debe contar algo. **Sale del brief**, no lo inventa el script.
- ≤ 5 bullets, ≤ 15 palabras por bullet. **Bullets resumidos del brief** por el script (truncado controlado, no inventado).
- **Un elemento visual** (icono semántico del catálogo del script, o referencia visual sugerida en el brief si la hay).
- **Notas del orador** (speaker notes) — **párrafo completo de prosa del brief** correspondiente a ese concepto, incluyendo el escenario de Marta y la analogía. Esto es lo que la formadora lee en el monitor del portátil.

## C) Densidad mínima por formato derivado (camino NotebookLM, cara al alumno)

Para que NotebookLM produzca formatos derivados ricos para el alumno, el brief debe contener:

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

# Tarea complementaria: script generador de deck desde el brief

Construir un script Python que **parsea un brief `DXX_Brief_NotebookLM.md` y emite el PPTX completo** del deck del formador para esa sesión. Idealmente:

```bash
python3 Scripts/generar_deck.py D05
# → Decks/D05_procesado.pptx
```

Y modo lote: `python3 Scripts/generar_deck.py D01 D02 D03 ...` o `--all`.

## Regla de oro (la más importante de toda esta tarea)

**TODO el contenido textual del PPTX debe provenir del brief.** El script:

- **No inventa** ejemplos, conceptos, prompts, datos, citas, glosario, errores comunes ni notas del orador.
- **No rellena** con texto genérico cuando una sección del brief queda corta.
- **No reescribe** ni "mejora" el texto del brief — lo extrae, lo resume con criterios mecánicos (recortar a N palabras, partir en bullets por puntos/líneas) y lo coloca.

Si una slide queda con poco texto, es señal de que **el brief necesita más contenido en esa sección** — y eso lo arregla el revisor humano o tu tarea (1) del proyecto, no el script.

## Excepciones explícitas (lo único que el script "sabe" por sí mismo)

Como es estructura común a todos los 17 días, el script puede incluir sin necesidad de leerlo del brief:

- Plantilla visual: paleta AllWomen (azul `#2B5CE6`, naranja `#E8601A`, crema `#F5EFE6`, oscuro `#1A1A2E`), tipografías y layouts.
- Etiquetas estándar fijas: `"Día X de 17"`, `"Apertura · 15 min"`, `"Teórico-demostrativo · 75 min"`, `"Descanso · 15 min"`, `"Práctica guiada · 95 min"`, `"Puesta en común · 40 min"`, `"🛠 AHORA: PRÁCTICA"`, `"Lo que hicimos hoy"`, `"Mañana"`.
- Logo AllWomen (PNG en `Logos/00_FULL COLOR (1).png`).
- Número de slide, footer (curso/edición/cliente: *IA en la Oficina · Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital*).
- Iconos semánticos del catálogo del script para los elementos visuales (un set acotado: 💡, 📊, 🔍, ⚠️, ✅, 🛠, 🎓, 🔁, 🧩, 📝).

Cualquier otro texto sale del brief. Si no está en el brief, no se mete.

## Mapeo brief → slides

| Slide | Sección del brief de origen | Cómo se construye |
|---|---|---|
| **Portada** | Sección 1 "Cabecera" | Título sesión + módulo + "Día X de 17" + edición |
| **Agenda del día** | Sección 4 "Estructura de la sesión" | Tabla de bloques + temas/actividades por bloque |
| **Apertura — Recap sesión anterior** | Sección 2 "Contexto del curso" → "Sesión anterior (DXX)" | 3–5 bullets de lo visto ayer |
| **Apertura — Objetivos del día** | Sección 5 "Objetivos de aprendizaje" | 3–4 bullets en infinitivo |
| **Teórico — 1 slide por concepto** (≥ 8) | Sección 6 "Desarrollo teórico en prosa" | Una slide por concepto. Título narrativo = subtítulo del concepto en el brief. Bullets = puntos resumidos del párrafo. Notas del orador = **párrafo completo + analogía + escenario de Marta** |
| **Teórico — Datos clave** (1–2 slides) | Sección 7 "Datos y cifras clave" | Cifra grande + frase contexto, ≤ 4 datos por slide |
| **Teórico — Ejemplo resuelto** (1 slide por ejemplo, ≥ 4) | Sección 8 "Ejemplos resueltos paso a paso" | Una slide por ejemplo. Estructura fija: Situación / Prompt / Resultado / Iteración. Notas con la prosa explicativa del brief |
| **Teórico — Errores comunes** (1–2 slides) | Sección 10 "Errores comunes y buenas prácticas" | Tabla 2 col: "Error frecuente" / "Cómo evitarlo" |
| **Glosario** (1–2 slides) | Sección 9 "Glosario" | Término + definición; máx. 6–8 términos por slide |
| **🛠 AHORA: PRÁCTICA** (1 por actividad, ≥ 3) | Sección 11 "Actividades en aula" | Slide de transición con código `EJ-DXX-N`, modalidad (Individual/Pareja/Grupo), duración y objetivo en una frase |
| **Práctica — ficha de cada ejercicio** | Sección 11 ampliada + `Recursos/Banco_de_Ejercicios.md` | Consigna paso a paso + entregable + rúbrica corta |
| **Trabajo en parejas/grupo 🔁** | Sección 12 (callout) | Una slide propia con la dinámica colaborativa del día |
| **Puesta en común — Estructura** | Sección 4 + Sección 17 "Mini-entregable del día" | Cómo se va a hacer la revisión: tiempo, criterios, qué se comparte |
| **Cierre — Lo que hicimos hoy** | Sección 20 "Ideas para recordar" | 5–7 bullets de recap |
| **Cierre — Mañana (DXX+1)** | Sección 21 "Conexión con el resto del curso" | 2–3 bullets de qué viene |
| **Hilo proyecto final 🎓** (solo en D01/D09/D16/D17) | Sección 18 (callout) | Una slide específica del hito de proyecto que toque ese día |

→ Total mínimo: **40 slides**, objetivo **50–55** (coincide con sección B).

## Robustez del parser

- **Sección obligatoria ausente** en el brief (las que están en la tabla de mapeo) → el script falla con un error claro indicando qué sección falta y en qué brief. **No genera deck a medias.**
- **Sección por debajo del mínimo** (p. ej. solo 3 conceptos teóricos cuando se piden ≥ 8) → el script emite el deck igualmente pero al final imprime un **informe de déficit**: qué slides salieron flojas, cuántos conceptos/ejemplos/términos faltan.
- **Códigos `EJ-DXX-N` huérfanos**: el script valida que cada código citado en el brief exista en `Banco_de_Ejercicios.md`. Si no, warning.
- **Slides "🛠 AHORA: PRÁCTICA"** deben aparecer **antes** de cada práctica, no después. El parser respeta el orden del brief.

## Estilo visual

- Paleta AllWomen (igual que `Recursos/Guia_Alumno_NotebookLM.pdf`).
- Alto contraste, tipografía limpia ≥ 24pt en cuerpo (criterio Fundación ONCE).
- Logo AllWomen en esquina superior derecha de cada slide (igual que hoy en `process_decks.py`).
- Sin animaciones complejas; transiciones simples.
- Footer en cada slide: número + curso/edición.

## Decisión sobre cómo encajarlo en el repo

- **Opción A:** ampliar `Scripts/process_decks.py` (hoy solo logo) a "brief → PPTX completo + logo". Mantiene un único script.
- **Opción B (recomendada):** crear `Scripts/generar_deck.py` nuevo, dejar `process_decks.py` como utilidad logo-only deprecada o borrarlo. Más limpio conceptualmente, alcance muy distinto.

→ Coordinar con el usuario antes de borrar `process_decks.py`.

## Verificación del script (sin necesidad de cuenta Google)

1. `python3 Scripts/generar_deck.py D05` produce `Decks/D05_procesado.pptx` sin errores.
2. El PPTX abre limpio en LibreOffice / PowerPoint / Google Slides.
3. Conteo: cada deck tiene ≥ 40 slides; portada y cierre presentes; las slides "🛠 AHORA: PRÁCTICA" están en su posición correcta.
4. Cada slide tiene logo, número y footer estándar.
5. Las notas del orador contienen el texto literal del brief (verificable con `grep` en el XML del .pptx tras `unzip`).
6. Generar los 17 decks en una pasada y confirmar que ninguno falla por brief incompleto — si alguno falla, esa es la lista de briefs que aún necesitan trabajo.
7. Diff de "déficit por brief" del script ↔ tabla de calibración del paso 1 del plan: deben coincidir.

## Restricción explícita (recordatorio)

**Bajo ninguna circunstancia el script puede inventar contenido pedagógico, ejemplos, prompts, datos o pasos.** Si el brief no lo tiene, el script no lo pone. Esto fuerza que el brief siga siendo la fuente única de verdad y que cualquier déficit se vea en el output del script, no se camufle.

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
│   ├── pipeline_ia_oficina.py     Wrapper para NotebookLM (camino alumno)
│   ├── process_decks.py           Logo-only sobre PPTX (en proceso de deprecación)
│   ├── generar_deck.py            ← NUEVO: brief → PPTX completo (camino formador)
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

2. **Endurecer la plantilla del brief** en `Recursos/Plantilla_Brief.md` con los nuevos mínimos (sección A) y con una **regla de nombres de subsección estables** (importante: el script va a parsear las secciones por su título, así que cada brief debe usar exactamente los mismos encabezados — "## 6. Desarrollo teórico", "## 11. Actividades en aula", etc.).

3. **Ampliar los briefs uno a uno**, en orden D01 → D17:
   - Cumplir mínimos de la sección A.
   - Respetar los nombres de subsección estables.
   - Aplicar la regla de decisión cuando el tema "se quede corto".
   - Si necesitas añadir sub-tema nuevo al temario, **detenerse y preguntar** antes de hacerlo.

4. **Construir el script `Scripts/generar_deck.py`** (ver "Tarea complementaria"):
   - Parser de brief Markdown → estructura intermedia (lista de slides).
   - Emisor PPTX con `python-pptx`, plantilla AllWomen, logo, notas del orador.
   - Validación de secciones obligatorias y reporte de déficit.
   - Tests rápidos con D01 y D05 (los más estables) antes de pasar el resto.

5. **Ajustar el PROMPT a NotebookLM** en `Recursos/NotebookLM_Prompts_Referencia.md` y en la constante `PROMPT` de `Scripts/pipeline_ia_oficina.py`:
   - **Quitar** todas las instrucciones de estructura del deck (NotebookLM las ignora — confirmado en producción).
   - **Conservar y endurecer** instrucciones para Audio Overview, Video Overview, infografía, flashcards, cuestionario, FAQ (formatos cara al alumno, que sí responden a prompts ricos en la fuente).
   - Eliminar la mención al deck del flujo NotebookLM en este archivo y en `pipeline_ia_oficina.py` — el deck ya no pasa por NotebookLM.

6. **Verificación end-to-end:**
   - Cada brief ≥ 450 líneas.
   - Cada brief con ≥ 8 conceptos teóricos, ≥ 4 ejemplos resueltos, ≥ 12 glosario, ≥ 15 cuestionario, ≥ 10 FAQ, ≥ 8 errores comunes.
   - Estructura de 22 secciones íntegra y nombres de subsección estables.
   - Callouts 🔁 y 🎓 en su sitio.
   - Cero referencias a Copilot/M365/ChatGPT Plus salvo las pedagógicas explícitas (D04 y D08).
   - Códigos `EJ-DXX-N` del brief existen en `Banco_de_Ejercicios.md` (sin huérfanos).
   - **`python3 Scripts/generar_deck.py D01..D17` genera los 17 PPTX sin errores fatales**; los warnings de déficit, si existen, se reportan al usuario.

7. **Commit y push a `claude/plan-ai-course-6WxJC`** con mensajes claros por lote (p. ej. "Ampliar D01–D05 a densidad mínima nueva: +N líneas", "Añadir generar_deck.py: parser brief→PPTX", "Quitar instrucciones de deck del prompt NotebookLM").

---

# Restricciones de proceso

- **No tocar la arquitectura del temario** (mapa de módulos, calendario, asignación de días). Solo profundidad de contenido y herramientas de generación.
- **No mover archivos** salvo que el usuario lo pida.
- **No regenerar el PDF de la guía del alumno** salvo que se modifique su contenido textual.
- **El script nuevo solo lee el brief.** No tiene tablas hardcoded de conceptos, ejemplos o speaker notes por sesión. Si necesitas saber algo del día, ese algo está en el brief o no está.
- **Si decides borrar/deprecar `process_decks.py`**, confírmalo antes de hacerlo.
- **Idioma español neutro, accesible**, frases completas (debe sonar bien leído en voz alta — Audio Overview).
- **Nada de relleno** en los briefs. Si llegas al techo del temario, párate y pregunta.
- **Reporte de estado cada 3–4 briefs** revisados (líneas añadidas, conceptos añadidos, decisiones tomadas) para que el usuario pueda redirigir antes de seguir. Reporte específico al terminar el script con el resumen de validación de los 17 PPTX.

---

# Output esperado al final del trabajo

- **17 briefs ampliados** cumpliendo todos los mínimos de la sección A, con nombres de subsección estables compatibles con el parser del script.
- **`Scripts/generar_deck.py` funcional**: genera los 17 PPTX desde los briefs, con la estructura de la sección B, logo, notas del orador y validación de secciones. Sin contenido inventado ni hardcoded por sesión.
- **`Recursos/NotebookLM_Prompts_Referencia.md` y `pipeline_ia_oficina.py`** limpios de instrucciones de deck (NotebookLM ya no genera el deck); reforzados para los formatos cara al alumno.
- **`Contexto/CONTEXTO_PROYECTO.md`** con una nota nueva en "Decisiones": (a) NotebookLM no controla el deck → script propio; (b) nuevo estándar de densidad y regla anti-relleno; (c) regla de oro del script: solo contenido del brief.
- **`Recursos/Plantilla_Brief.md`** actualizada con los nuevos mínimos y los nombres de subsección estables.
- En caso de haber propuesto sub-temas nuevos al temario: lista clara de cuáles, dónde encajan y qué desplazan — **solo aplicada si el usuario dijo sí**.
- Commits limpios en `claude/plan-ai-course-6WxJC`.

================== FIN DEL PROMPT ==================

---

## Notas de uso

- Este prompt está pensado para una sesión larga. Si lo divides, mantén siempre el bloque "Criterios cuantitativos mínimos", la "Regla de decisión" y la "Regla de oro" del script en cada subprompt.
- Si quieres que primero te entreguen solo la **tabla de calibración** (sin editar nada), recorta el "Plan de trabajo" a su paso 1 y añade: *"Detente tras la calibración y espera mi visto bueno antes de editar."*
- Si quieres dividir el trabajo en dos sesiones, una opción razonable: **Sesión 1** = pasos 1–3 (calibración + plantilla + ampliar briefs); **Sesión 2** = pasos 4–7 (script + ajuste de prompts NotebookLM + verificación end-to-end). El paso 3 debe estar terminado antes de empezar el paso 4: el script depende de que los briefs tengan los nombres de subsección estables.
