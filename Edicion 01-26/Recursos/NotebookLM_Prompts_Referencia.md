# PROMPTS DE REFERENCIA — NotebookLM
## Curso: IA en la Oficina · Edición 01/26
## Para el formador: copia el prompt correspondiente en el chat de cada notebook.

---

## Cómo usar este documento

Cada sesión tiene un **menú de prompts por formato**. Antes de cada clase, Ananda pre-genera en el notebook del día los formatos que quiera tener listos (el deck siempre; el podcast cuando quiera ofrecer audio; el cuestionario antes del cierre, etc.). Los alumnos pueden generar los demás ellos mismos desde el enlace público del notebook.

**Consejo:** si un resultado no convence, añade al final del prompt:
> *"Prioriza datos numéricos, comparativas visuales y analogías concretas sobre listas de texto."*

---

## ⭐ ESTRUCTURA OBLIGATORIA DEL DECK (léeme primero)

Sí: **el formato y la estructura de las diapositivas se controlan desde el prompt**, no desde el script. Si pides explícitamente la agenda, las señales de ejercicio y el cierre, NotebookLM las genera. El script Python (`process_decks.py`) **solo** añade después el logo de AllWomen y las notas del formador — el contenido y el orden de las slides ya vienen del prompt.

**Pega este bloque al final de CUALQUIER prompt de deck** (o usa el prompt estándar de abajo, que ya lo incluye):

> Estructura obligatoria del deck, en este orden exacto:
> 1. **PORTADA** — título de la sesión, "Día X de 17", módulo y nombre del curso.
> 2. **AGENDA DEL DÍA** — una diapositiva con los bloques de la sesión y su duración: Apertura (15 min), Teórico-demostrativo (75 min), Descanso (15 min), Práctica guiada (95 min), Puesta en común (40 min). Junto a cada bloque, en una línea, los temas o actividades que se verán.
> 3. **SLIDES DE CONTENIDO** — máximo 5 puntos cortos por slide, cada una con un elemento visual (diagrama, dato, comparativa o iconos).
> 4. **SEÑAL DE EJERCICIO** — justo antes de cada actividad práctica de la sesión, inserta una diapositiva de transición con fondo distinto y el título "🛠 AHORA: PRÁCTICA". Debe indicar: el nombre de la actividad, su código de ejercicio (formato EJ-DXX-N si aparece en el documento), la modalidad (Individual / En parejas / En grupo), la duración en minutos y el objetivo en una sola frase. Esta diapositiva sirve a la formadora para saber con claridad cuándo parar la teoría y empezar la práctica.
> 5. **CIERRE** — una diapositiva de recap titulada "Lo que hicimos hoy" con 3-4 puntos de lo trabajado en la sesión, seguida de "Mañana" con 2-3 puntos de lo que se verá en la sesión siguiente. (En D17, en lugar de "Mañana", usa "Tu plan de 30 días" y el cierre del curso.)
>
> Tono: directo, accesible, sin tecnicismos. Público: personal administrativo sin experiencia previa en IA.

---

## Prompts reutilizables por formato

### Deck / presentación (PROMPT ESTÁNDAR — usa este para cualquier sesión)
> Genera una presentación visualmente rica sobre **[TEMA DEL DÍA]**. Usa títulos provocadores y narrativos, no descriptivos. Cada slide incluye un elemento visual (diagrama, estadística, comparativa o iconos).
>
> Estructura obligatoria del deck, en este orden exacto:
> 1. **PORTADA** — título de la sesión, "Día X de 17", módulo y nombre del curso.
> 2. **AGENDA DEL DÍA** — una diapositiva con los bloques de la sesión y su duración: Apertura (15 min), Teórico-demostrativo (75 min), Descanso (15 min), Práctica guiada (95 min), Puesta en común (40 min). Junto a cada bloque, los temas o actividades que se verán.
> 3. **SLIDES DE CONTENIDO** — máximo 5 puntos cortos por slide, cada una con un elemento visual.
> 4. **SEÑAL DE EJERCICIO** — justo antes de cada actividad práctica, una diapositiva de transición "🛠 AHORA: PRÁCTICA" que indique: nombre de la actividad, código (EJ-DXX-N si aparece en el documento), modalidad (Individual / En parejas / En grupo), duración en minutos y objetivo en una frase. Sirve a la formadora para saber cuándo parar la teoría y hacer la práctica.
> 5. **CIERRE** — diapositiva "Lo que hicimos hoy" (3-4 puntos de recap) seguida de "Mañana" (2-3 puntos de la sesión siguiente).
>
> Tono: directo, accesible, sin tecnicismos. Público: personal administrativo sin experiencia previa en IA.

*Las descripciones por sesión de más abajo son la línea **[TEMA DEL DÍA]** que se inserta en este prompt estándar; ya no hace falta repetir la estructura, basta con combinar el tema con el bloque de estructura.*

### Audio Overview / podcast
> Genera un Audio Overview en español sobre los conceptos clave de esta sesión. Tono conversacional, con ejemplos concretos del entorno de oficina. Empieza con el problema que resuelve la sesión y termina con el mensaje más importante que debe recordar el oyente.

### Video Overview
> Genera un Video Overview en español que resuma visualmente los puntos principales de esta sesión. Estructura: introducción al problema (30 seg) → conceptos clave (2-3 min) → ejemplos prácticos (1-2 min) → mensaje final (30 seg).

### Infografía / mapa mental
> Genera una infografía o mapa mental con los conceptos clave de esta sesión. Organiza los conceptos en jerarquía: concepto central → categorías principales → detalles y ejemplos. Incluye datos numéricos del documento donde estén disponibles.

### Guía de estudio
> Genera una guía de estudio completa de esta sesión para un alumno que quiere repasar el material antes de aplicarlo en el trabajo. Incluye: resumen de conceptos, tabla comparativa de herramientas o enfoques, ejemplos de prompts y pasos a seguir, y errores comunes a evitar.

### Documento informativo (Briefing Doc)
> Genera un documento informativo de máximo una página que resuma los puntos más importantes de esta sesión. Debe poder leerse en 3 minutos y ser útil para alguien que no asistió a la clase.

### Flashcards
> Genera un conjunto de flashcards de repaso basadas en el glosario y los conceptos clave de esta sesión. Formato: pregunta en el anverso / respuesta concisa en el reverso. Mínimo 10 tarjetas.

### Cuestionario de autoevaluación
> Genera un cuestionario de autoevaluación de 10 preguntas sobre esta sesión. Incluye preguntas de opción múltiple, verdadero/falso y una pregunta abierta de reflexión. Proporciona las respuestas correctas al final.

### FAQ
> Genera una lista de preguntas frecuentes (FAQ) que podría tener un alumno sobre el contenido de esta sesión. Para cada pregunta, proporciona una respuesta clara y concisa. Incluye al menos 8 preguntas.

---

## PROMPTS POR SESIÓN

> **Cómo usar esta sección:** el prompt **Deck** de cada sesión es la versión rápida (tema concreto). Para obtener la **agenda del día**, las **señales de ejercicio** y el **cierre con recap + mañana**, añade el bloque ⭐ ESTRUCTURA OBLIGATORIA DEL DECK (arriba) al final del prompt Deck, o usa directamente el PROMPT ESTÁNDAR sustituyendo `[TEMA DEL DÍA]` por el tema de la sesión. Los demás formatos (podcast, cuestionario, etc.) se usan tal cual.

---

### D01 — M1 — Qué es la IA generativa
**Brief:** `D01_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación visualmente rica para la Sesión 1 del curso "IA en la Oficina": qué es la IA generativa, panorama de herramientas gratuitas y reglas de privacidad. Usa títulos provocadores y narrativos. Cada slide incluye un elemento visual. Slide de portada + contenido (máx. 5 puntos) + cierre con misión para D02. Tono accesible, sin tecnicismos. Público: administrativos sin experiencia en IA.

**Podcast:**
> Genera un Audio Overview en español sobre qué es la IA generativa y por qué es relevante para el trabajo de oficina. Desmonta los 4 mitos principales sobre la IA con ejemplos cotidianos. Cierra con el mensaje: qué puede y qué no puede hacer la IA.

**Cuestionario:**
> Genera un cuestionario de 10 preguntas sobre los conceptos de esta sesión: definición de IA generativa, diferencia entre herramientas, reglas de privacidad y cómo identificar tareas donde la IA puede ayudar. Incluye respuestas.

**Flashcards:**
> Genera flashcards con los términos del glosario de esta sesión: IA generativa, LLM, alucinación, prompt, modelo de lenguaje, dato sensible. Definición de una frase en el reverso.

---

### D02 — M2 — Prompts básicos: estructura R-C-T-F-R
**Brief:** `D02_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación para la sesión de prompts básicos: la estructura R-C-T-F-R (Rol, Contexto, Tarea, Formato, Restricciones) y cómo pasar de un prompt vago a uno profesional. Ejemplos reales de prompts mejorados. Slide de portada + contenido + cierre con misión D03.

**Podcast:**
> Genera un Audio Overview en español sobre la estructura R-C-T-F-R. Explica cada componente con un ejemplo de oficina y muestra el antes/después de un prompt real.

**Guía de estudio:**
> Genera una guía de estudio con: definición de cada componente R-C-T-F-R, tabla comparativa de prompt vago vs prompt con estructura, 5 ejemplos de prompts completos para tareas de oficina, y los 3 errores más comunes al escribir prompts.

**Cuestionario:**
> Genera un cuestionario de 10 preguntas sobre la estructura R-C-T-F-R: identifica qué componente falta en cada prompt, cuál es el resultado esperado de añadir el Rol, etc. Incluye respuestas.

---

### D03 — M2 — Prompts avanzados: encadenamiento e iteración
**Brief:** `D03_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación sobre prompts avanzados: encadenamiento de prompts, cómo pegar contexto correctamente e iteración para mejorar resultados. Muestra el flujo de 3 prompts encadenados con un caso de oficina real. Slide de portada + contenido + cierre con misión D04.

**Podcast:**
> Genera un Audio Overview en español sobre por qué un solo prompt rara vez da el mejor resultado y cómo el encadenamiento iterativo transforma un borrador mediocre en un documento profesional.

**Infografía:**
> Genera un mapa mental con el flujo de encadenamiento de prompts: prompt 1 (borrador) → feedback → prompt 2 (mejora) → prompt 3 (refinado). Incluye qué tipo de instrucción va en cada eslabón.

**Cuestionario:**
> Genera un cuestionario de 10 preguntas sobre encadenamiento e iteración: qué prompt sigue en la cadena, cómo mejorar un resultado insatisfactorio, cuándo parar de iterar. Incluye respuestas.

---

### D04 — M3 — Automatización de tareas repetitivas
**Brief:** `D04_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación sobre automatización de tareas repetitivas con IA: cómo identificar qué automatizar, generación en lote, Gemini en Google Docs y cómo guardar prompts favoritos con Gemini Gems o una biblioteca en Google Docs. Slide de portada + contenido + cierre con misión D05.

**Podcast:**
> Genera un Audio Overview en español sobre qué tareas repetitivas de oficina son candidatas a automatizarse con IA y cómo configurar un flujo de generación en lote que ahorre horas cada semana.

**Guía de estudio:**
> Genera una guía de estudio con: los 3 criterios para identificar tareas automatizables, el flujo de generación en lote paso a paso, cómo usar Gemini en Google Docs, y cómo organizar una biblioteca de prompts reutilizables.

**Cuestionario:**
> Genera un cuestionario de 10 preguntas sobre automatización: cuáles son candidatos a generación en lote, cómo usar Gemini en Google Docs, qué es un Gemini Gem y para qué sirve. Incluye respuestas.

---

### D05 — M3 — Resúmenes y transformación de formatos
**Brief:** `D05_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación sobre resúmenes y transformación de formatos: los 3 tipos de resumen según el destinatario (ejecutivo, operativo, divulgativo), conversión entre formatos y extracción de campos clave. Slide de portada + contenido + cierre con misión D06.

**Podcast:**
> Genera un Audio Overview en español sobre la diferencia entre un resumen ejecutivo, uno operativo y uno divulgativo, con ejemplos de cuándo usar cada uno en el trabajo de oficina.

**Infografía:**
> Genera un mapa mental con los 3 tipos de resumen (destinatario → características → ejemplo de uso) y los 4 tipos de transformación de formato (texto→tabla, tabla→texto, largo→breve, informal→formal).

**Cuestionario:**
> Genera un cuestionario de 10 preguntas: identifica qué tipo de resumen corresponde a cada destinatario, cuál es el prompt para extraer campos clave, qué hacer cuando el documento es demasiado largo. Incluye respuestas.

---

### D06 — M3 — Correos profesionales y situaciones difíciles
**Brief:** `D06_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación sobre comunicación escrita con IA: estructura del correo eficaz, cómo gestionar situaciones difíciles (reclamaciones, negativas, urgencias) y el patrón RIA (Reconoce/Informa/Actúa) para respuestas a clientes. Slide de portada + contenido + cierre con misión D07.

**Podcast:**
> Genera un Audio Overview en español sobre los correos difíciles: reclamaciones, mensajes de rechazo, urgencias. Explica el patrón RIA con un ejemplo real y cómo la IA ayuda a mantener el tono profesional bajo presión.

**Guía de estudio:**
> Genera una guía de estudio con: los 6 elementos del correo eficaz, la tabla de situaciones difíciles y cómo manejarlas, el patrón RIA con ejemplo y el prompt de auditoría de correos antes de enviar.

**Cuestionario:**
> Genera un cuestionario de 10 preguntas sobre correos profesionales: identifica qué elemento del correo falta, qué paso del patrón RIA se saltó, cuál es el prompt para reescribir en tono más empático. Incluye respuestas.

---

### D07 — M3 — Redacción de informes con IA
**Brief:** `D07_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación sobre redacción de informes con IA: el flujo de 4 pasos (índice → secciones → resumen ejecutivo → revisión), adaptación a 3 públicos distintos y cómo evitar alucinaciones en informes. Slide de portada + contenido + cierre con misión D08.

**Podcast:**
> Genera un Audio Overview en español sobre por qué el resumen ejecutivo se escribe al final, cuál es la diferencia entre adaptar para un público técnico, ejecutivo y cliente, y cómo verificar que los datos del informe son correctos.

**Infografía:**
> Genera un mapa mental con el flujo de 4 pasos del informe, las 3 versiones de tono (técnica/ejecutiva/cliente) y los 4 tipos de alucinación que hay que verificar en informes.

**Cuestionario:**
> Genera un cuestionario de 10 preguntas sobre informes: cuál es el orden correcto de los 4 pasos, qué cambia entre la versión técnica y la ejecutiva, cómo detectar alucinaciones en cifras. Incluye respuestas.

---

### D08 — M4 — Planificación semanal y gestión de reuniones
**Brief:** `D08_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación sobre organización y planificación con IA: matrices de priorización (Eisenhower, MoSCoW), planificación semanal asistida y preparación de reuniones eficaces. Slide de portada + contenido + cierre con misión D09.

**Podcast:**
> Genera un Audio Overview en español sobre cómo usar la IA para priorizar la semana: la diferencia entre urgente e importante, el método de los 4 pasos para el plan semanal, y cómo preparar una reunión en 5 minutos con IA.

**Infografía:**
> Genera un mapa mental con la matriz de Eisenhower (4 cuadrantes con ejemplos), el método MoSCoW (4 categorías), y el flujo de planificación semanal de 4 pasos.

**Cuestionario:**
> Genera un cuestionario de 10 preguntas sobre planificación y reuniones: clasifica tareas en Eisenhower, identifica el cuadrante MoSCoW correcto, qué incluye el orden del día generado con IA. Incluye respuestas.

---

### D09 — M4 — Actas, seguimiento y delegación
**Brief:** `D09_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación sobre actas, seguimiento y delegación: cómo generar actas útiles desde notas de reunión, tableros kanban en texto con IA y cómo redactar instrucciones de delegación que eliminen malentendidos. Slide de portada + contenido + cierre con misión D10.

**Podcast:**
> Genera un Audio Overview en español sobre qué diferencia un acta útil de una transcripción, cómo usar un kanban de texto sin herramientas especiales, y los 5 elementos que no pueden faltar en una instrucción de delegación.

**Guía de estudio:**
> Genera una guía de estudio con: anatomía del acta útil (decisiones + tabla de acciones + próxima reunión), el prompt de kanban en texto, los 5 elementos de la delegación y los prompts de seguimiento (1er aviso / 2do aviso sin respuesta).

**Cuestionario:**
> Genera un cuestionario de 10 preguntas: qué no debe incluir un acta útil, cuáles son los 5 elementos de la delegación, qué hace el sistema de semáforo de seguimiento. Incluye respuestas.

---

### D10 — M5 — Análisis de datos sin ser experto en Excel
**Brief:** `D10_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación sobre análisis de datos con IA para no expertos: anonimización previa, uso de lenguaje natural para fórmulas y tablas dinámicas en Google Sheets, interpretación de resultados y detección de alucinaciones numéricas. Slide de portada + contenido + cierre con misión D11.

**Podcast:**
> Genera un Audio Overview en español sobre por qué la anonimización es el primer paso de cualquier análisis con IA, cómo pedir fórmulas en lenguaje natural, y la regla de verificación: nunca publicar un dato sin comprobar la fuente.

**Infografía:**
> Genera un mapa mental con el flujo de análisis (anonimizar → formular en lenguaje natural → interpretar → verificar), los 4 tipos de hallazgo (tendencia, anomalía, comparativa, correlación) y las señales de alucinación numérica.

**Cuestionario:**
> Genera un cuestionario de 10 preguntas: cuál es el primer paso antes de subir datos a la IA, cómo pedir una fórmula en lenguaje natural, qué hacer cuando un hallazgo parece sospechoso. Incluye respuestas.

**Flashcards:**
> Genera flashcards con los términos del glosario de esta sesión: anonimización, tabla dinámica, hallazgo, alucinación numérica, verificación de fuente, lenguaje natural, dataset. Definición de una frase en el reverso.

---

### D11 — M5 — Búsqueda, síntesis e informes de mercado
**Brief:** `D11_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación sobre búsqueda e investigación con IA: diferencia entre Google y Perplexity, verificación de fuentes, síntesis comparativa de proveedores/opciones y estructura del informe de mercado. Slide de portada + contenido + cierre con misión D12.

**Podcast:**
> Genera un Audio Overview en español sobre cuándo usar Perplexity en vez de Google, cómo pedir citas a la IA para verificar datos antes de incluirlos en un informe, y la estructura de un informe de mercado de 2 páginas con fuentes.

**Guía de estudio:**
> Genera una guía de estudio con: tabla de herramientas de búsqueda (Google vs Perplexity vs NotebookLM), el flujo de investigación en 5 pasos, la tabla de criterios para comparativa de proveedores, y la estructura del informe de mercado.

**Cuestionario:**
> Genera un cuestionario de 10 preguntas: cuándo usar Perplexity vs Google, cómo verificar que un dato no es una alucinación, qué secciones tiene el informe de mercado estándar. Incluye respuestas.

---

### D12 — M6 — Canva con IA: presentaciones e imágenes
**Brief:** `D12_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación sobre Canva con IA para no diseñadores: los 4 principios básicos de diseño (contraste, alineación, repetición, proximidad), uso de Magic Design y Magic Write, generación de imágenes con IA y gestión de cuotas gratuitas. Slide de portada + contenido + cierre con misión D13.

**Podcast:**
> Genera un Audio Overview en español sobre los 4 principios de diseño que todo el mundo puede aplicar sin ser diseñador, cómo Canva Magic Design automatiza el 80% del trabajo visual, y qué hacer cuando se acaba la cuota de imágenes IA.

**Guía de estudio:**
> Genera una guía de estudio con: los 4 principios de diseño con ejemplos descritos, el flujo de Magic Design paso a paso, el flujo de Magic Write, los límites del plan gratuito de Canva y las alternativas cuando se agotan.

**Cuestionario:**
> Genera un cuestionario de 10 preguntas: identifica qué principio de diseño se viola en cada ejemplo, cuál es el límite de imágenes IA en Canva free, cómo activar Magic Write. Incluye respuestas.

---

### D13 — M6 — Material visual, comunicación interna y accesibilidad
**Brief:** `D13_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación sobre comunicación visual accesible: piezas de comunicación interna (cartel, infografía, post), kit de marca coherente, accesibilidad en diseño (contraste 4.5:1, alt text, tipografía mínima 16px) e intro a vídeo simple en Canva. Slide de portada + contenido + cierre con misión D14.

**Podcast:**
> Genera un Audio Overview en español sobre por qué el diseño accesible es mejor diseño para todos, las 4 reglas de accesibilidad visual que cualquiera puede aplicar, y cómo crear un kit de 3 piezas coherentes de comunicación interna en menos de una hora.

**Guía de estudio:**
> Genera una guía de estudio con: las 4 reglas de accesibilidad con explicación y herramienta de verificación, el paso a paso para añadir alt text en Canva, la guía de kit de marca coherente (colores, fuentes, plantilla), y cómo grabar un vídeo simple desde Canva.

**Cuestionario:**
> Genera un cuestionario de 10 preguntas: cuál es el ratio mínimo de contraste accesible, cómo se añade alt text en Canva, qué es el kit de marca, cuándo NO usar el color como único diferenciador. Incluye respuestas.

---

### D14 — M7 — Gestión documental y flujos de trabajo
**Brief:** `D14_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación sobre gestión documental con IA: naming convention, SOP en 3 prompts, checklist desde SOP, mapeo de flujos de trabajo, automatización ligera con Google Forms→Sheets y NotebookLM como base de conocimiento del equipo. Slide de portada + contenido + cierre con misión D15.

**Podcast:**
> Genera un Audio Overview en español sobre cómo tres prompts son suficientes para generar un SOP completo, cuándo NO automatizar un proceso, y cómo NotebookLM puede convertirse en la memoria del equipo.

**Guía de estudio:**
> Genera una guía de estudio con: la naming convention estándar con ejemplos, los 3 prompts del SOP (contexto → pasos → validación), el flujo Google Forms→Sheets→IA, y cómo configurar NotebookLM como base de conocimiento.

**Cuestionario:**
> Genera un cuestionario de 10 preguntas: cuál es el formato de naming convention, cuántos prompts necesita un SOP completo, qué incluye la validación de un proceso, cuándo NO automatizar. Incluye respuestas.

---

### D15 — M7 — Atención al cliente y procesos recurrentes
**Brief:** `D15_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación sobre atención al cliente con IA: banco de FAQ en lote, patrón RIA para respuestas difíciles, guiones multicanal (email/Teams/teléfono), escalado y privacidad (nunca datos reales de clientes en la IA). Slide de portada + contenido + cierre con misión D16.

**Podcast:**
> Genera un Audio Overview en español sobre cómo construir un banco de FAQ en minutos desde consultas reales anonimizadas, el patrón RIA para situaciones difíciles, y las 3 situaciones en las que siempre hay que escalar a un humano.

**Guía de estudio:**
> Genera una guía de estudio con: el flujo de construcción del banco FAQ, el patrón RIA con ejemplo completo, la tabla de guiones multicanal (email/Teams/teléfono), las 3 situaciones de escalado y la regla de privacidad para datos de clientes.

**Cuestionario:**
> Genera un cuestionario de 10 preguntas: cuál es el primer paso antes de subir consultas de clientes a la IA, qué significa cada letra del patrón RIA, en qué situaciones no se debe responder con IA. Incluye respuestas.

---

### D16 — M8 — Taller integrador: proyecto personal con IA
**Brief:** `D16_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación para el taller de proyecto final individual: la rúbrica de evaluación (4 criterios: utilidad, dominio, calidad, presentación), el lienzo de proyecto (4 bloques), la estructura de presentación de 5 minutos y el feedback entre pares 2+1+1. Slide de portada + contenido. Sin slide de misión próxima sesión.

**Guía de estudio:**
> Genera una guía de estudio con: la rúbrica de evaluación con indicadores para cada nivel, el lienzo de proyecto con preguntas guía para cada bloque, la estructura de presentación de 5 minutos y los criterios del feedback 2+1+1.

**Cuestionario:**
> Genera 10 preguntas de reflexión para el proyecto final: qué problema resuelve, qué herramienta usa y por qué, cómo mediría el impacto en tiempo ahorrado, qué haría diferente con más tiempo. Preguntas abiertas sin respuesta única correcta.

---

### D17 — M8 — Presentaciones finales y cierre del curso
**Brief:** `D17_Brief_NotebookLM.md`

**Deck:**
> Genera una presentación para el cierre del curso: estructura de presentación de 5 minutos para el alumno, criterios de feedback entre pares 2+1+1, diseño del plan personal de 30 días y reflexión grupal de cierre. Slide de portada + contenido. Sin slide de misión próxima sesión.

**Podcast:**
> Genera un Audio Overview en español de cierre del curso: qué han aprendido los alumnos en 17 sesiones, por qué las habilidades de prompting duran aunque cambien las herramientas, y cómo diseñar un plan de 30 días para mantener el hábito.

**Documento informativo:**
> Genera un documento informativo de cierre del curso: resumen de las herramientas gratuitas disponibles, los 5 hábitos de IA que vale la pena mantener, y 3 recursos para seguir aprendiendo (todos gratuitos).

**Cuestionario:**
> Genera un cuestionario de autoevaluación final del curso completo: 12 preguntas que recorren los módulos M1–M7, con énfasis en los conceptos más aplicados en el proyecto final. Incluye respuestas y explica por qué cada respuesta es correcta.

---

## NOTA GENERAL

Si el resultado no te convence en alguna sesión, prueba añadir al final del prompt:
> *"Prioriza datos numéricos, comparativas visuales y analogías concretas sobre listas de texto."*

Para el Audio Overview en español, si sale en inglés:
> *"Genera el Audio Overview íntegramente en español castellano, con vocabulario accesible para alguien sin experiencia técnica."*
