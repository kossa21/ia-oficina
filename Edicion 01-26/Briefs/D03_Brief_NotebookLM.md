# BRIEF PARA NOTEBOOKLM — D03
## Módulo 2, Sesión 2: Prompts avanzados — Encadenamiento e iteración
## Curso: IA en la Oficina – Eficiencia y Productividad
## Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital

---

## CONTEXTO DEL CURSO

**Programa:** IA en la Oficina – Eficiencia y productividad (68 horas · 17 sesiones)
**Público:** Personal administrativo y de oficina sin experiencia previa en IA generativa
**Sesión anterior (D02):** El grupo ya domina la estructura R-C-T-F-R y tiene 5 prompts personales escritos y probados.

---

## SESIÓN D03 — Viernes 3 de julio de 2026 · 15:00–19:00 h

**Módulo:** 2 de 8 — Ingeniería de Prompts para Principiantes
**Sesión:** 2 de 2 del módulo · Día 3 de 17 del curso

---

## ESTRUCTURA DE LA SESIÓN (4 horas)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| Apertura | 15 min | Repaso R-C-T-F-R + preguntas del día anterior |
| Teórico-demostrativo | 75 min | Pensar en flujos · Pegar contexto · Iteración y refinado · Cuándo NO usar IA |
| Descanso | 15 min | — |
| Práctica guiada | 105 min | Caso práctico de informe en 4 prompts + flujo propio de 3 prompts |
| Puesta en común | 30 min | Revisión de flujos + mini-entregable |

---

## OBJETIVOS DE APRENDIZAJE

1. Dividir una tarea compleja en pasos y resolverla con varios prompts encadenados.
2. Pegar contexto real (textos, datos, ejemplos) dentro del prompt de forma efectiva.
3. Mejorar un resultado mediante prompts de refinado sin empezar de cero.
4. Identificar cuándo la IA no es la herramienta adecuada.

---

## CONTENIDOS

### Pensar la tarea como un flujo: divide antes de pedir

Las tareas complejas de oficina rara vez se resuelven en un solo prompt. La clave es dividir antes de pedir:

1. Define el objetivo final (¿qué documento necesitas al final?).
2. Identifica los pasos intermedios (¿qué información hay que generar primero?).
3. Escribe un prompt por paso, usando el resultado del anterior como contexto del siguiente.

**Ejemplo real — informe de incidencias mensual en 4 prompts:**
- Prompt 1: "Resume estas notas de incidencias del mes en una lista por categorías." → [pegar notas]
- Prompt 2: "Identifica las 3 incidencias más graves y su impacto estimado."
- Prompt 3: "Redacta la sección 'Análisis de incidencias' del informe mensual. Tono formal, máximo 200 palabras."
- Prompt 4: "Redacta la sección 'Recomendaciones' proponiendo 3 acciones concretas para el mes siguiente."

**El resultado:** un informe profesional construido en 4 pasos, cada uno verificable, sin alucinaciones porque tú controlas la información en cada fase.

---

### Cómo pegar contexto correctamente

La IA no conoce tu empresa ni tu situación. Tienes que dársela tú:

- **Qué puedes pegar:** correos, extractos de documentos, tablas de datos, ejemplos de cómo lo haces normalmente.
- **Cómo introducirlo:** con una etiqueta clara → "Aquí tienes el correo original: [INICIO] … [FIN]"
- **Cuándo cambiar de herramienta:** si el documento supera 5-6 páginas, usa Claude o NotebookLM, que gestionan textos más largos sin perder información.
- **Regla de privacidad:** anonimiza siempre antes de pegar. Sustituye nombres por CLIENTE_A, importes por IMPORTE_X.

---

### Iteración: mejorar sin empezar de cero

La técnica más poderosa y menos usada por principiantes. En lugar de regenerar desde cero, pides a la IA que mejore la respuesta anterior:

| Tipo de refinado | Prompt de iteración |
|-----------------|-------------------|
| Acortar | "Reduce esta respuesta a la mitad manteniendo los puntos clave." |
| Cambiar tono | "Reescribe con un tono más empático y menos formal." |
| Añadir sección | "Añade al final un párrafo con los próximos pasos concretos." |
| Cambiar formato | "Convierte este texto en una lista de 5 puntos numerados." |
| Corregir un error | "El tercer punto no es correcto: [explicación]. Corrígelo manteniendo el resto." |
| Adaptar destinatario | "Adapta este texto para que lo entienda alguien sin conocimientos técnicos." |

**Regla práctica:** antes de regenerar, siempre intenta primero con iteración. Ahorra tiempo y mantiene lo que ya funcionaba.

---

### Cuándo NO usar IA

La IA no siempre es la mejor herramienta. Descártala cuando:
- La tarea requiere información confidencial que no puedes anonimizar.
- Un error tendría consecuencias graves sin revisión humana posterior.
- La tarea es tan sencilla que el tiempo de escribir el prompt supera el de hacerla directamente.
- El resultado será publicado o enviado de forma masiva sin revisión individual.
- Necesitas juicio ético genuino o información de última hora verificada.

---

## ACTIVIDADES EN AULA

**Actividad 1 — Caso práctico: informe en 4 prompts (60 min)**
El formador proporciona notas desordenadas de una reunión ficticia. La clase construye un informe de 2 páginas en exactamente 4 prompts encadenados. El formador modera en pantalla.

**Actividad 2 — Mi flujo de 3 prompts (50 min)**
Cada alumno elige una tarea real de su puesto que requiera más de un paso y construye un flujo de mínimo 3 prompts encadenados. Documenta el proceso y el resultado final.

**Actividad 3 — Revisión guiada de flujos (20 min)**
3-4 voluntarios comparten su flujo en pantalla. El grupo sugiere mejoras y el formador destaca lo que funciona.

---

## HERRAMIENTAS

- ChatGPT (con opción de subir archivos si la versión lo permite)
- Claude (para documentos más largos)
- Plantilla "flujo de prompts" (entregada en aula virtual)

---

## MINI-ENTREGABLE

**Nombre:** Mi flujo de prompts
**Contenido:** Flujo documentado de mínimo 3 prompts encadenados que resuelven una tarea real del puesto. Incluye: descripción de la tarea, los 3 prompts con estructura R-C-T-F-R, y el resultado final obtenido.

---

## MENSAJE CLAVE

> "Un prompt no es una orden, es el inicio de una conversación. Las tareas más complejas no se resuelven de golpe: se dividen, se encadenan y se refinan. Quien aprende a iterar con la IA trabaja tres veces más rápido que quien intenta acertarlo todo en el primer intento."

---

*Brief para NotebookLM · D03 · Edición 01/26 — IA en la Oficina*
