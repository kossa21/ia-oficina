# BRIEF PARA NOTEBOOKLM — D03
## Módulo 2, Sesión 2: Prompts avanzados — Encadenamiento e iteración
## Curso: IA en la Oficina – Eficiencia y Productividad
## Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital

**Fecha:** Viernes 4 de julio de 2026 · 15:00–19:00 h · Día 3 de 17

---

## 2. CONTEXTO DEL CURSO

**Programa:** IA en la Oficina – Eficiencia y Productividad (68 horas · 17 sesiones de 4 horas)
**Público:** Personal administrativo y de oficina sin experiencia previa en IA generativa. Perfiles muy diversos: administración, atención al cliente, contabilidad, logística, recursos humanos.
**Metodología:** ~40 % teoría y demostración · ~50 % práctica guiada · ~10 % puesta en común
**Evaluación:** Mini-entregable al final de cada sesión + Proyecto Final individual (D16–D17)
**Sesión anterior (D02):** El grupo ya domina la estructura R-C-T-F-R, tiene 5 prompts personales escritos y probados, y ha visto la diferencia entre un prompt vago y uno estructurado.

> *Este documento es la fuente del notebook de hoy. Además de las diapositivas, puedes pedirle a NotebookLM un resumen en **audio** (tipo pódcast), un **vídeo**, una **infografía** o mapa mental, una **guía de estudio**, **fichas** (flashcards), un **cuestionario** para autoevaluarte, o **escribir tus preguntas en el chat**. Usa el formato con el que mejor aprendas. No escribas datos personales reales en el chat.*

---

## 3. RESUMEN DE LA SESIÓN

Hoy damos el salto del prompt suelto al flujo de trabajo: la técnica de encadenar varios prompts para resolver tareas complejas que no caben en una sola instrucción. Aprenderemos también a pegar contexto real dentro del prompt de forma efectiva y segura, y a refinar resultados mediante iteración en lugar de empezar desde cero cada vez que algo no sale perfecto. El cierre de la sesión aborda una pregunta que todo el mundo se hace pero pocos se atreven a formular: ¿cuándo la IA no es la herramienta adecuada? Al terminar el día, cada alumno tendrá un flujo documentado de al menos tres prompts encadenados que resuelven una tarea real de su puesto, completando así el Módulo 2 del curso y disponiendo de las dos herramientas fundamentales del trabajo con IA: el prompt estructurado y el flujo encadenado.

---

## 4. ESTRUCTURA DE LA SESIÓN (240 min)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| Apertura | 15 min | Repaso R-C-T-F-R + preguntas del día anterior + warm-up con un prompt real del grupo |
| Teórico-demostrativo | 75 min | Pensar en flujos: divide antes de pedir · Pegar contexto correctamente · Iteración: mejorar sin empezar de cero · Cuándo NO usar IA |
| Descanso | 15 min | — |
| Práctica guiada | 95 min | Caso práctico grupal: informe en 4 prompts (40 min) · Mi flujo de 3 prompts (45 min) · Revisión en pareja (10 min) |
| Puesta en común | 40 min | 3-4 flujos compartidos en pantalla + reflexión colectiva + mini-entregable |

*(15+75+15+95+40 = 240 min)*

---

## 5. OBJETIVOS DE APRENDIZAJE

1. Dividir una tarea compleja de oficina en pasos intermedios y resolverla con varios prompts encadenados, usando el resultado de cada paso como contexto del siguiente.
2. Pegar contexto real (correos, datos, documentos) en el prompt de forma efectiva y anonimizada.
3. Mejorar un resultado mediante prompts de iteración sin empezar desde cero, ahorrando tiempo y preservando lo que ya funcionaba.
4. Identificar con criterio cuándo la IA no es la herramienta adecuada para una tarea concreta.

---

## 6. DESARROLLO TEÓRICO

### Pensar la tarea como un flujo: divide antes de pedir

En D02, Marta aprendió a construir prompts R-C-T-F-R para tareas concretas: redactar un correo, resumir un texto, generar respuestas tipo. Hoy se enfrenta a algo más exigente: el informe mensual de incidencias. Es un documento de dos páginas que incluye un resumen por categorías, un análisis de las incidencias más graves y un apartado de recomendaciones. Marta lo hace cada mes y le lleva casi cuatro horas. Cuando abre ChatGPT y escribe "redacta el informe de incidencias de este mes", el resultado es una estructura vacía sin ningún contenido real, porque la IA no tiene las notas ni los datos de los que partir. El problema no es la IA. El problema es que Marta está intentando resolver un trabajo de cuatro pasos en un único prompt.

La clave de las tareas complejas de oficina es **dividir antes de pedir**. Casi ningún documento profesional real se resuelve en un solo prompt: hay información que hay que procesar primero, hay secciones que dependen del análisis de otras, hay un orden lógico que respetar. El flujo de prompts es exactamente esto: una cadena en la que la respuesta de cada prompt se convierte en el contexto del siguiente, construyendo el resultado final paso a paso.

El proceso tiene tres etapas. Primero, define el objetivo final: ¿qué documento necesitas al terminar, qué tiene que contener, a quién va dirigido? Segundo, identifica los pasos intermedios: ¿qué información hay que generar o procesar primero para que el siguiente paso tenga sentido? Tercero, escribe un prompt por paso usando el resultado anterior como material de partida.

Volvamos con Marta. En lugar de un único prompt, construye el siguiente flujo de cuatro pasos para el informe de incidencias:

> **Prompt 1:** "Actúa como asistente administrativo. Te paso las notas de incidencias del mes anonimizadas. Organízalas en categorías: logística, atención al cliente, proveedores y otras. Usa formato de lista con subtítulos por categoría. [PEGAR NOTAS ANONIMIZADAS]"

> **Prompt 2:** "A partir de la lista por categorías que acabas de hacer, identifica las 3 incidencias más graves. Para cada una: describe brevemente qué ocurrió, qué impacto tuvo y si se resolvió. Sin añadir información que no esté en la lista."

> **Prompt 3:** "Con las 3 incidencias graves que acabas de describir, redacta la sección 'Análisis de incidencias' del informe mensual. Tono formal, máximo 200 palabras. Estructura: una frase de contexto general, luego un párrafo por cada incidencia."

> **Prompt 4:** "Basándote en el análisis anterior, redacta la sección 'Recomendaciones' del informe. Propón 3 acciones concretas para reducir incidencias similares el mes siguiente. Formato: lista numerada, una acción por punto, máximo dos líneas por acción."

El resultado de este flujo es un informe de dos páginas, coherente, verificable en cada paso y sin alucinaciones, porque Marta ha controlado la información que la IA recibe en cada fase. En lugar de cuatro horas, el proceso completo —incluyendo revisión— le lleva menos de cuarenta minutos.

La diferencia respecto a un prompt único no es solo de calidad. Es también de **verificabilidad**: en un flujo de cuatro pasos, si algo sale mal en el paso 2, Marta puede corregirlo antes de que ese error se propague a los pasos 3 y 4. Con un prompt único, el error aparece en el documento final y hay que rehacer todo.

---

### Cómo pegar contexto correctamente: información real, resultados reales

La IA no conoce tu empresa, ni a tus clientes, ni el historial de incidencias de este mes. Lo que sabe es lo que le das en el prompt. Pegar contexto real —correos, extractos de documentos, tablas de datos, notas de reuniones— es lo que transforma una respuesta genérica en una respuesta específica y directamente usable.

Hay cuatro tipos de contexto que los perfiles administrativos suelen pegar con frecuencia: correos recibidos (para redactar respuestas), notas de reunión o de incidencias (para generar informes), tablas o listados de datos (para resumir o analizar), y ejemplos del estilo o formato que usa la empresa (para que la respuesta se parezca a los documentos reales).

La técnica más eficaz para introducir contexto es usar **etiquetas de delimitación**: una marca de inicio y una de fin que indican a la IA dónde empieza y dónde termina el material que le estás pasando. Esto evita que la IA confunda el texto que le das con las instrucciones del prompt.

> Ejemplo de estructura con etiqueta:
> "Actúa como administrativa de RRHH. A continuación te paso el correo que ha enviado un empleado solicitando permisos. Redacta una respuesta formal confirmando la recepción y pidiendo la documentación justificativa. Correo original: [INICIO] Buenos días, me gustaría solicitar dos días de permiso para [MOTIVO_X] los días [FECHA_1] y [FECHA_2]. Gracias. EMPLEADO_A [FIN] Máximo 60 palabras."

Las etiquetas [INICIO] y [FIN] —o cualquier marcador claro que elijas— hacen que el prompt sea más legible para ti y más interpretable para la IA.

Cuando el documento que necesitas pegar es muy largo —más de cinco o seis páginas—, ChatGPT en su versión gratuita puede tener dificultades para procesar todo el texto sin perder información de las partes más alejadas del inicio. En esos casos, la alternativa más eficaz son **Claude** (que gestiona documentos más largos con mayor fidelidad) o **Google NotebookLM** (que permite subir el documento entero y hacer preguntas sobre él). Ambas herramientas son gratuitas con cuenta Gmail.

Y la regla que nunca cambia, independientemente de la herramienta: **anonimiza siempre antes de pegar**. Los nombres reales, los datos bancarios, los expedientes internos, los datos de RRHH o las referencias de clientes no deben salir de la organización sin autorización explícita. La solución práctica es sencilla y tarda menos de dos minutos: sustituye NOMBRE_REAL por EMPLEADO_A, CLIENTE_B, PROVEEDOR_C; sustituye importes concretos por IMPORTE_X; sustituye fechas específicas de expedientes por FECHA_Y. El resultado es igualmente útil para la IA y tú cumples con el RGPD.

---

### Iteración: mejorar sin empezar de cero

La iteración es la técnica más poderosa del trabajo con IA y, paradójicamente, la que menos usan los principiantes. Cuando el primer resultado no es exactamente lo que necesitaban, la mayoría de personas borra la conversación y escribe un prompt nuevo desde cero. Esto desperdicia todo el trabajo que ya hizo la IA y obliga a repetir el proceso desde el principio.

La iteración funciona de otra forma: en lugar de empezar de nuevo, le pides a la IA que ajuste, mejore o corrija la respuesta que ya tiene delante. La IA recuerda el contexto de la conversación activa y puede modificar el resultado anterior con una instrucción muy breve.

La siguiente tabla recoge los tipos de refinado más útiles en el trabajo de oficina, con el prompt exacto para cada uno:

| Tipo de refinado | Prompt de iteración |
|-----------------|---------------------|
| Acortar | "Reduce esta respuesta a la mitad manteniendo todos los puntos clave." |
| Cambiar tono | "Reescribe con un tono más empático y menos formal." |
| Añadir sección | "Añade al final un párrafo con los próximos pasos concretos." |
| Cambiar formato | "Convierte este texto en una lista de 5 puntos numerados." |
| Corregir un dato | "El tercer punto no es correcto: [EXPLICACIÓN]. Corrígelo manteniendo el resto." |
| Adaptar destinatario | "Adapta este texto para que lo entienda alguien sin conocimientos técnicos del sector." |
| Simplificar vocabulario | "Reescribe usando un vocabulario más sencillo. Sin tecnicismos." |
| Añadir formalidad | "Reescribe con un registro más formal. El documento va a dirección." |

Marta prueba esto con el correo de respuesta a una reclamación que generó en D02. El primer resultado es correcto pero algo frío. En lugar de reescribir el prompt entero, escribe: "Reescribe con un tono más cálido. El cliente es habitual y queremos retenerle." La IA ajusta el registro en segundos, manteniendo el contenido correcto del primer resultado. En total, dos prompts han producido un correo que habría tardado veinte minutos en escribir a mano.

La **regla práctica de la iteración** es esta: antes de regenerar desde cero, siempre intenta una iteración. Si el resultado tiene el contenido correcto pero algo falla (tono, extensión, formato, un dato concreto), la iteración lo arregla en un prompt breve. Si el resultado tiene el contenido completamente equivocado, entonces sí tiene sentido empezar de nuevo con un prompt más detallado.

Un matiz importante: la IA solo "recuerda" el contexto dentro de la misma conversación activa. Si cierras la ventana y abres una nueva, la IA no recuerda nada de lo anterior. Por eso, cuando trabajas en un flujo de varios prompts, hazlo siempre dentro de la misma conversación, sin cerrarla entre un paso y el siguiente.

---

### Cuándo NO usar IA

Dominar los prompts no significa usarlos en todo. Una parte del criterio profesional con IA es saber cuándo la herramienta no es la adecuada, y no ceder a la tentación de automatizar lo que no debería automatizarse.

Hay cinco situaciones claras en las que la IA no es la herramienta correcta. La primera: cuando la tarea **requiere información confidencial que no puedes anonimizar** de forma razonable. Hay documentos cuya confidencialidad es tan crítica (expedientes disciplinarios, datos financieros sensibles, información médica) que el esfuerzo de anonimizar destruye la utilidad de la tarea. En esos casos, no uses la IA.

La segunda: cuando **un error tendría consecuencias graves sin revisión humana posterior**. Si el documento va a ser publicado, enviado de forma masiva o tiene consecuencias legales, la revisión humana no es opcional. La IA es un punto de partida, no una firma.

La tercera: cuando **la tarea es más rápida de hacer directamente que de escribir el prompt**. Si enviar un correo de dos líneas te cuesta cuarenta segundos, escribir el prompt, lanzarlo, revisar el resultado y ajustarlo puede costar el triple. La IA ahorra tiempo en tareas con un volumen o complejidad suficiente para justificar el proceso.

La cuarta: cuando **necesitas información verificada y de última hora**. La IA genera texto a partir de sus datos de entrenamiento, que tienen una fecha de corte. Para noticias recientes, normativas actualizadas, precios actuales o cualquier información que cambia con frecuencia, usa Perplexity (que cita fuentes) o comprueba directamente en la fuente oficial.

La quinta: cuando **la tarea requiere juicio ético genuino o decisión humana**. Decidir si un expediente merece una sanción, evaluar el rendimiento de un empleado o gestionar un conflicto entre personas son tareas que requieren criterio humano, contexto relacional y responsabilidad. La IA puede ayudarte a preparar la información, pero la decisión debe ser tuya.

---

## 7. DATOS Y CIFRAS CLAVE

- Construir un informe mensual en un flujo de 4 prompts encadenados puede reducir el tiempo de redacción de 3-4 horas a 30-45 minutos (ahorro del 80 %).
- Los usuarios que aprenden iteración producen resultados satisfactorios en una media de 1-2 prompts adicionales; quienes no la usan generan el resultado en 4-6 intentos desde cero.
- Antes / Después — informe de incidencias mensual (2 páginas): antes 3,5 horas; con flujo de 4 prompts 35-40 min.
- Antes / Después — responder y refinar un correo complejo: antes 20-30 min; con prompt inicial + 1-2 iteraciones 3-5 min.
- Antes / Después — resumir y estructurar notas de reunión (1 hora de reunión): antes 45-60 min; con flujo de prompts 8-12 min.
- El 73 % del tiempo que los principiantes dedican a trabajar con IA se pierde regenerando respuestas desde cero cuando la iteración habría sido suficiente (estimación basada en observación de aula).
- Claude gestiona documentos de hasta ~200 000 tokens de contexto en su versión gratuita, frente a los ~8 000 tokens por conversación del nivel gratuito de ChatGPT — para documentos largos, Claude o NotebookLM son la elección correcta.

---

## 8. EJEMPLOS RESUELTOS PASO A PASO

### Caso 1 — Flujo de 4 prompts: informe de incidencias mensual

**Situación:** Marta tiene que entregar cada primer lunes del mes el informe de incidencias a dirección. Dispone de un documento de notas desordenadas que ha ido acumulando durante el mes. El informe debe tener tres secciones: resumen por categorías, análisis de las tres más graves y recomendaciones.

**Prompt 1 — Clasificar las notas:**
> "Actúa como asistente administrativo. Te paso las notas de incidencias del mes en bruto. Organízalas en cuatro categorías: logística, atención al cliente, proveedores y otras. Formato: lista con subtítulos en negrita por categoría y puntos bajo cada uno. Solo usa la información que te proporciono; no añadas nada. [INICIO] NOTA 1: PROVEEDOR_A entregó el pedido PEDIDO_001 con 2 días de retraso sin avisar. NOTA 2: CLIENTE_B llamó dos veces sin respuesta el día FECHA_1. NOTA 3: error en la factura REF_002: importe incorrecto. [FIN]"

**Prompt 2 — Identificar las más graves:**
> "De la lista que acabas de hacer, identifica las 3 incidencias más graves. Para cada una: una línea con qué ocurrió, una línea con el impacto estimado y una línea indicando si está resuelta o pendiente. Sin añadir información externa."

**Prompt 3 — Redactar el análisis:**
> "Con las 3 incidencias graves que has descrito, redacta la sección 'Análisis de incidencias' del informe mensual. Tono formal. Máximo 200 palabras. Estructura: frase introductoria general + un párrafo por incidencia."

**Prompt 4 — Redactar las recomendaciones:**
> "Basándote en el análisis anterior, redacta la sección 'Recomendaciones' del informe. Propón 3 acciones concretas para reducir incidencias similares el mes siguiente. Formato: lista numerada, máximo 2 líneas por punto. Lenguaje directo y orientado a la acción."

**Resultado comentado:** Cada prompt produce una sección del informe que Marta revisa antes de pasar al siguiente. Si en el Prompt 2 la IA selecciona una incidencia que Marta considera menos grave que otra, puede corregirla antes de que ese dato incorrecto llegue al Prompt 3. El informe final es coherente, verificado paso a paso y directamente usable con ajustes menores.

**Cómo iterarlo:** Si el tono del análisis resulta demasiado impersonal para el estilo habitual de la empresa: *"Reescribe la sección de análisis manteniendo el contenido pero con un registro algo menos formal, más directo."*

---

### Caso 2 — Iteración práctica: mejorar el tono sin perder el contenido

**Situación:** Marta ha generado un correo de respuesta a una reclamación de un cliente habitual. El contenido es correcto pero el tono le parece demasiado frío para alguien con quien la empresa lleva años trabajando.

**Prompt inicial:**
> "Actúa como responsable de atención al cliente de una empresa de distribución. CLIENTE_C nos ha enviado una reclamación porque el pedido PEDIDO_002 llegó con el embalaje dañado. Redacta un correo formal reconociendo el problema, confirmando que gestionaremos el reemplazo y pidiendo disculpas. Máximo 100 palabras."

**La IA genera una respuesta correcta pero fría.** En lugar de reescribir el prompt entero, Marta añade:

**Iteración 1:**
> "El tono está bien en contenido pero es demasiado frío para un cliente con el que llevamos 5 años trabajando. Reescribe manteniendo el mismo contenido pero con un tono más cálido y cercano."

**Iteración 2 (opcional si todavía hay ajuste):**
> "Está mejor. Ahora añade una frase al inicio que reconozca específicamente que entendemos lo incómodo que es recibir un pedido dañado, antes de ofrecer la solución."

**Resultado comentado:** Dos iteraciones breves han producido un correo que Marta no podría haber generado fácilmente con un único prompt, porque el equilibrio entre formalidad y calidez es difícil de especificar de antemano. La iteración permite ir ajustando el resultado como si estuvieras hablando con alguien que ya tiene el borrador delante.

---

### Caso 3 — Pegar contexto: responder a un correo complejo de proveedor

**Situación:** Marta recibe un correo de un proveedor que tiene varios puntos: pregunta por el estado de dos facturas, solicita cambiar los datos bancarios y avisa de un cambio de representante comercial. Quiere responder a los tres puntos con el tono adecuado.

**Prompt exacto:**
> "Actúa como administrativa de una empresa de distribución. Te paso un correo de un proveedor con tres temas distintos. Redacta una respuesta que: (1) confirme que revisaremos las dos facturas en 48 horas, (2) indique que el cambio de datos bancarios debe tramitarse por formulario oficial (no por correo), y (3) agradezca la información sobre el nuevo representante y pida su contacto directo. Formato: correo formal, un párrafo por punto, máximo 150 palabras en total. Correo original: [INICIO] Buenos días, les escribo para preguntar el estado de las facturas REF_A y REF_B. También necesito actualizar los datos bancarios para futuros pagos. Por último, informarles de que a partir de FECHA_Y su nuevo representante será PERSONA_X. Gracias. PROVEEDOR_D [FIN]"

**Resultado comentado:** Al usar etiquetas [INICIO] y [FIN] para delimitar el correo original, la IA entiende con claridad qué es instrucción y qué es material de referencia. La respuesta generada aborda los tres puntos en el orden del original, con el tono apropiado para cada uno. Marta solo necesita revisar que los plazos mencionados sean los correctos según la política de la empresa.

---

## 9. GLOSARIO

**Flujo de prompts:** Secuencia de dos o más prompts encadenados en los que el resultado de cada uno se usa como contexto del siguiente, para resolver tareas que son demasiado complejas para un único prompt.

**Encadenamiento:** Técnica de diseñar los prompts de un flujo de forma que cada respuesta alimenta la siguiente, construyendo el resultado final de manera progresiva y verificable.

**Iteración:** Prompt adicional que pide a la IA que ajuste, mejore o corrija la respuesta anterior dentro de la misma conversación, sin empezar desde cero.

**Ventana de contexto:** Límite de texto que una IA puede "leer y recordar" dentro de una misma conversación; cuando se supera, la IA puede olvidar información de los primeros mensajes. Los modelos gratuitos tienen ventanas de contexto menores que los de pago.

**Etiqueta de delimitación:** Marcador textual ([INICIO] / [FIN], o similares) que indica a la IA dónde empieza y dónde termina el material de contexto que se le está pasando, diferenciándolo de las instrucciones.

**Anonimización:** Sustitución de datos personales o confidenciales por etiquetas genéricas (CLIENTE_A, IMPORTE_X, FECHA_Y) antes de pegarlos en cualquier herramienta de IA externa; imprescindible para cumplir con el RGPD.

**Refinado:** Cada iteración que mejora un aspecto específico del resultado (tono, extensión, formato, corrección de un dato), sin modificar lo que ya estaba bien.

**Alucinación:** Dato incorrecto que la IA afirma con total confianza, como si fuera cierto; especialmente frecuente con cifras, fechas, nombres propios y referencias normativas. Siempre verificar.

**Claude:** Herramienta de IA de Anthropic, gratuita con cuenta Google, especialmente útil para documentos muy largos que superan la ventana de contexto de ChatGPT en su versión gratuita.

**NotebookLM:** Herramienta de Google que permite subir documentos completos y hacer preguntas sobre ellos; ideal para documentos extensos que no caben en el contexto de un chat de IA convencional.

---

## 10. ERRORES COMUNES Y BUENAS PRÁCTICAS

**Error 1 — Intentar resolver en un solo prompt lo que necesita un flujo.** "Redacta el informe mensual completo" sin proporcionar datos no puede producir un resultado real. Si la tarea tiene más de una sección o requiere procesar información antes de redactar, divídela en pasos.

**Error 2 — No verificar los resultados intermedios antes de avanzar.** En un flujo de cuatro prompts, si el resultado del Prompt 2 contiene un error y no lo detectas, ese error se propaga a los Prompts 3 y 4. Revisa cada paso antes de usar ese resultado como contexto del siguiente.

**Error 3 — Cerrar la conversación entre pasos del flujo.** La IA no recuerda conversaciones anteriores. Si cierras la ventana y abres una nueva, tienes que volver a proporcionar todo el contexto desde el principio. Trabaja siempre un flujo completo dentro de la misma conversación activa.

**Error 4 — Pegar texto confidencial sin anonimizar.** Correos con nombres reales de empleados, datos bancarios, importes de nóminas o información de expedientes no deben pegarse en ninguna herramienta de IA externa sin anonimizar. La norma aplica a ChatGPT, Gemini, Claude y cualquier otra herramienta.

**Error 5 — Regenerar desde cero cuando la iteración es suficiente.** Si el contenido del resultado es correcto pero el tono, el formato o la extensión no es exactamente lo que necesitas, usa una iteración. Es más rápido, más eficiente y preserva lo que ya funcionaba.

**Buena práctica — Documenta los flujos que funcionan.** Cuando construyas un flujo de prompts que produce un buen resultado, guárdalo completo: los cuatro prompts en orden, con sus instrucciones y etiquetas. La próxima vez que necesites hacer el mismo informe, el flujo ya está diseñado.

**Buena práctica — Usa Claude para documentos largos.** Si necesitas pegar un documento de más de 5-6 páginas, cambia a Claude o NotebookLM. No es una limitación de tu capacidad: es usar la herramienta adecuada para cada escala de tarea.

---

## 11. ACTIVIDADES EN AULA

### Actividad 1 — Caso práctico grupal: informe en 4 prompts [Grupo · 40 min]

**Descripción:** El formador proporciona un conjunto de notas desordenadas de incidencias ficticias (una página, datos ya anonimizados). El grupo, guiado por el formador, construye juntos en pantalla el flujo de 4 prompts del Caso 1 del apartado de ejemplos. Cada prompt se lanza en ChatGPT con el proyector visible; el grupo debate si el resultado es adecuado o si conviene iterar antes de pasar al siguiente paso. Al final, el grupo dispone de un informe completo de dos páginas generado en directo.

**Objetivo:** Que todos los alumnos experimenten el flujo de principio a fin antes de intentarlo individualmente; que el formador pueda corregir en tiempo real los errores más comunes (avanzar sin revisar, no usar etiquetas, etc.).

**Material:** Proyector, ChatGPT abierto en pantalla, documento de notas ficticias de incidencias (proporcionado por el formador).

---

### Actividad 2 — Mi flujo de 3 prompts [Individual · 45 min]

**Descripción:** Cada alumno elige una tarea real de su puesto que requiera más de un paso (un informe, un resumen a partir de notas, una respuesta a una consulta compleja, una comunicación que necesita información previa). Construye un flujo de mínimo 3 prompts encadenados, documenta cada prompt y el resultado obtenido en cada paso, y produce el resultado final. En los últimos 5 minutos de la actividad, el alumno elige qué parte del flujo le resultó más útil para comentarlo en la revisión.

**Objetivo:** Aplicar el encadenamiento a una tarea real y propia; producir el mini-entregable del día.

**Material:** Ordenador con ChatGPT y/o Claude, plantilla "Mi flujo de prompts" (Google Doc o papel).

---

### Actividad 3 — Revisión cruzada de flujos [Pareja · 10 min]

**Descripción:** Cada alumno comparte brevemente su flujo con un/a compañero/a. El revisor hace dos preguntas concretas: (a) ¿hay algún paso del flujo que podría fusionarse con el anterior sin perder calidad? y (b) ¿hay algún paso que esté haciendo demasiado y convendría dividir en dos? La revisión es rápida y orientada a detectar los extremos (flujos demasiado fragmentados o prompts que intentan hacer demasiado).

**Objetivo:** Practicar la evaluación de la granularidad del flujo: ni demasiado dividido ni demasiado comprimido; preparar los flujos para la puesta en común.

**Material:** Los flujos producidos en la Actividad 2.

---

## 12. 🔁 TRABAJO EN PAREJAS

La **Actividad 3** es la dinámica colaborativa central de la sesión. Las parejas se forman preferiblemente entre personas con puestos distintos (por ejemplo, una persona de logística con una de RRHH), de modo que el revisor mire el flujo desde fuera sin la inercia de "así es como yo lo haría". Cada persona actúa como revisora del flujo del otro durante cinco minutos y luego se intercambian los roles. Lo que produce la pareja —la lista de sugerencias de ajuste— es lo que cada alumno puede aplicar en el mini-entregable antes de entregarlo. En la puesta en común, el formador pide a 3-4 parejas que compartan qué sugerencia de ajuste fue más útil y por qué; esto genera una reflexión colectiva sobre la granularidad óptima de los flujos que beneficia a todo el grupo.

---

## 13. EJERCICIOS SUGERIDOS

Ver Banco de Ejercicios:
- **EJ-D03-1** (Individual): Construir un flujo de 3 prompts encadenados para una de las tareas del mapa de oportunidades de D01
- **EJ-D03-2** (Pareja): Intercambiar flujos y aplicar la revisión cruzada de granularidad; documentar las mejoras aplicadas
- **EJ-D03-3** (Grupo): Comparativa de flujos: tres voluntarios comparten su flujo en pantalla; el grupo debate qué decisión de diseño (dividir vs. fusionar pasos) produce mejor resultado

---

## 14. CUESTIONARIO DE AUTOEVALUACIÓN

**1. ¿Qué es un flujo de prompts?**
a) Un único prompt muy largo con muchas instrucciones
b) Una secuencia de prompts encadenados donde cada resultado alimenta el siguiente ✓
c) Un prompt que se repite varias veces hasta dar un buen resultado
d) Un archivo donde se guardan los prompts favoritos

**2. ¿Cuál es la principal ventaja de resolver una tarea compleja en varios prompts encadenados en lugar de un único prompt?**
a) Los prompts cortos son más rápidos de escribir
b) La IA entiende mejor las instrucciones cortas
c) Permite verificar y corregir cada paso antes de que los errores se propaguen al resultado final ✓
d) Los flujos de prompts solo funcionan en Claude, no en ChatGPT

**3. ¿Para qué sirven las etiquetas de delimitación como [INICIO] y [FIN] en un prompt?**
a) Para indicar el principio y el fin del prompt entero
b) Para separar claramente el material de contexto (texto que pegas) de las instrucciones ✓
c) Son un formato obligatorio en ChatGPT para que funcione correctamente
d) Para que la IA sepa qué parte del texto debe traducir

**4. Marta ha generado un correo que tiene el contenido correcto pero el tono es demasiado formal. ¿Qué debe hacer?**
a) Borrar la conversación y escribir un prompt completamente nuevo
b) Escribir un prompt de iteración: "Reescribe con un tono más cercano, manteniendo el mismo contenido" ✓
c) Copiar el correo y editarlo manualmente
d) Lanzar el mismo prompt original en otra herramienta

**5. ¿En qué situación es mejor usar Claude en lugar de ChatGPT para pegar contexto?**
a) Cuando quieres que el resultado sea más creativo
b) Cuando el documento a pegar tiene más de 5-6 páginas y supera la ventana de contexto del nivel gratuito de ChatGPT ✓
c) Cuando el prompt está en español, porque Claude es mejor en este idioma
d) Claude y ChatGPT son intercambiables en todos los casos

**6. ¿Por qué hay que anonimizar los datos antes de pegarlos en la IA, incluso cuando el resultado es solo para uso interno?**
a) Para que la IA procese el texto más rápido
b) Porque la IA no entiende los nombres propios
c) Para proteger datos personales, evitar infracciones del RGPD y no revelar información confidencial de la organización a servicios externos ✓
d) Solo es necesario anonimizar si el resultado se va a publicar

**7. ¿Cuál de las siguientes NO es una situación en la que la IA es la herramienta adecuada?**
a) Generar 5 respuestas tipo para consultas frecuentes de proveedores
b) Resumir las notas de una reunión en 5 puntos clave
c) Decidir si un empleado merece una sanción disciplinaria ✓
d) Redactar el primer borrador de un comunicado interno

**8. Si cierras la ventana de ChatGPT y abres una nueva conversación, ¿qué pasa con el flujo de prompts que estabas construyendo?**
a) La IA recuerda el contexto automáticamente
b) Puedes recuperarlo desde el historial de conversaciones con un clic
c) La IA no recuerda nada: tendrías que volver a proporcionar todo el contexto desde el principio ✓
d) Solo se pierde si han pasado más de 24 horas

**9. ¿Cuándo conviene empezar desde cero con un prompt nuevo en lugar de iterar?**
Respuesta: Cuando el contenido de la respuesta es completamente equivocado o la IA ha interpretado mal el objetivo de la tarea desde el principio. Si solo hay problemas de tono, formato, extensión o un dato concreto, la iteración es más eficiente que empezar de cero.

**10. Marta tiene un documento de notas de reunión de 8 páginas que quiere resumir. ¿Qué herramienta es más adecuada y por qué?**
a) ChatGPT gratuito, porque es la herramienta principal del curso
b) Claude o NotebookLM, porque gestionan documentos largos con mayor fidelidad dentro de su nivel gratuito ✓
c) Gemini, porque está integrado con Google Docs
d) Canva, porque permite visualizar el resumen como infografía

**11. Describe el flujo mínimo para convertir notas de reunión desordenadas en un acta formal usando prompts encadenados.**
Respuesta: Un flujo mínimo de 3 pasos sería: Prompt 1: organizar las notas por temas o puntos del orden del día. Prompt 2: identificar los acuerdos y compromisos concretos de la reunión. Prompt 3: redactar el acta formal con fecha, asistentes (anonimizados), puntos tratados y acuerdos alcanzados. Cada prompt usa el resultado del anterior como contexto.

**12. ¿Qué ventaja tiene guardar un flujo de prompts completo (no solo los prompts sueltos)?**
Respuesta: Un flujo completo con los prompts en orden, las etiquetas de delimitación y las instrucciones de cada paso es directamente reutilizable la próxima vez que se necesita la misma tarea. No hay que rediseñar el proceso, solo sustituir el contenido (las notas, el correo, los datos del mes) y lanzar los pasos en orden.

---

## 15. PREGUNTAS FRECUENTES (FAQ)

**¿Cuántos prompts debe tener un flujo? ¿Hay un número ideal?**
No hay un número ideal fijo. La regla práctica es: tantos como pasos distintos y verificables tenga la tarea. Tareas sencillas pueden resolverse en 2-3 prompts; documentos complejos pueden necesitar 5-6. Lo importante es que cada prompt haga una cosa clara y que el resultado sea verificable antes de pasar al siguiente.

**¿Puedo usar el flujo de un compañero para una tarea similar a la mía?**
Sí, y es una de las formas más eficientes de aprender. Si un compañero ha construido un flujo para generar un informe de incidencias y tú tienes una tarea similar, puedes tomar su flujo, ajustar el contexto y las instrucciones a tu situación y lanzarlo. Las plantillas de flujo son tan reutilizables como las plantillas de prompts individuales.

**¿La IA recuerda lo que le dije ayer en otra conversación?**
No. Cada conversación nueva empieza completamente desde cero, sin memoria de sesiones anteriores. La única forma de que la IA "recuerde" tus instrucciones habituales es incluirlas de nuevo al principio del prompt, o usar herramientas como los Gemini Gems (que guardan instrucciones permanentes) o la función de instrucciones personalizadas de ChatGPT.

**¿Cuándo uso Claude en lugar de ChatGPT?**
Claude es especialmente útil cuando el documento o texto que necesitas procesar es muy largo (más de 5-6 páginas), cuando necesitas un análisis muy preciso sin perder información de las partes más largas del texto, o cuando el resultado requiere una redacción especialmente cuidada. Para tareas de extensión normal, ChatGPT y Claude son intercambiables.

**¿Qué pasa si la IA inventa datos en uno de los pasos del flujo?**
Es una de las razones por las que verificar cada paso del flujo antes de avanzar es tan importante. Si en el Prompt 2 la IA añade un dato que no estaba en las notas originales (por ejemplo, un plazo que tú no mencionaste), debes corregirlo antes de usar ese resultado en el Prompt 3. La iteración de corrección es: "El dato X no es correcto. Corrígelo con [DATO CORRECTO] y mantén el resto."

**¿Puedo pedirle a la IA que diseñe el flujo por mí?**
Sí, es una técnica útil cuando no sabes cómo dividir la tarea. Puedes escribir: "Necesito construir un flujo de prompts para [DESCRIBIR LA TAREA]. Propón los pasos en los que dividirías esta tarea y qué pediría en cada prompt." La IA te dará un esquema de flujo que tú puedes revisar, ajustar y lanzar.

**¿Tengo que usar etiquetas [INICIO] y [FIN] siempre que pego texto?**
No son obligatorias, pero sí muy recomendables cuando el texto que pegas es largo o cuando el prompt mezcla instrucciones y material de referencia. Sin etiquetas, la IA puede interpretar el texto pegado como parte de las instrucciones y producir resultados confusos. Si el texto es corto y el contexto está claro, puedes omitirlas.

**¿Existe alguna forma de guardar un flujo de prompts para reutilizarlo?**
La forma más sencilla es guardar los prompts en orden en un Google Doc personal, con el nombre de la tarea como título. También puedes crear un Gemini Gem (asistente personalizado) con las instrucciones fijas del flujo, de modo que solo tengas que pegar el contenido variable en cada uso. En D04 aprenderás más formas de organizar y reutilizar tus prompts.

---

## 16. HERRAMIENTAS DE LA SESIÓN

- **ChatGPT** (chatgpt.com) — Herramienta principal para construir flujos de prompts. Cuenta gratuita creada en D01. Nota: la ventana de contexto del nivel gratuito es limitada; para documentos largos, usa Claude.
- **Claude** (claude.ai) — Herramienta gratuita con cuenta Google, ideal para documentos largos que superan la ventana de contexto de ChatGPT. Se activa cuando el texto a procesar supera 5-6 páginas.
- **Google Gemini** (gemini.google.com) — Alternativa directamente accesible con la cuenta Gmail del alumno. Admite pegar contexto de forma similar a ChatGPT.
- **Google NotebookLM** (notebooklm.google.com) — Para documentos muy extensos: permite subir el documento completo y hacer preguntas sobre él en el chat. El formador comparte el enlace del notebook del día.

Ver el mapa completo de herramientas en `Recursos/Herramientas_Gratuitas.md`.

---

## 17. MINI-ENTREGABLE DEL DÍA

**Nombre:** Mi flujo de prompts
**Formato:** Documento Google Docs o plantilla en papel
**Contenido:** Flujo documentado de mínimo 3 prompts encadenados que resuelven una tarea real del puesto del alumno. Incluye: (1) descripción de la tarea y el objetivo final, (2) los 3 prompts con estructura R-C-T-F-R, con las etiquetas de delimitación si se usa contexto pegado, y (3) el resultado final obtenido en cada paso y el resultado final del flujo completo.
**Cómo alimenta el proyecto final:** Este flujo es la segunda capa del proyecto final, después de los 5 prompts de D02. En D09, el alumno elegirá uno de sus flujos como base del proyecto y lo ampliará con las herramientas aprendidas en los módulos siguientes. Un flujo bien documentado hoy ahorra horas de trabajo en D16.

---

## 18. 🎓 HILO DEL PROYECTO FINAL

Para tu proyecto final: lo de hoy te sirve para pasar de prompts sueltos a flujos de trabajo completos. El flujo que construyes hoy es el esqueleto de tu proyecto: en sesiones posteriores añadirás herramientas específicas, automatización y presentación, pero la estructura de "dividir la tarea en pasos y encadenarlos" es la que sostendrá todo lo demás.

---

## 19. MENSAJE CLAVE DE LA SESIÓN

> "Un prompt no es una orden, es el inicio de una conversación. Las tareas más complejas no se resuelven de golpe: se dividen, se encadenan y se refinan. Quien aprende a iterar con la IA trabaja tres veces más rápido que quien intenta acertarlo todo en el primer intento."

---

## 20. IDEAS PARA RECORDAR

- Divide antes de pedir: una tarea compleja resuelta en 4 prompts verificables es más fiable que el mismo trabajo pedido en un único prompt gigante.
- Anonimiza siempre antes de pegar: nombre, DNI, datos bancarios y expedientes nunca deben llegar a la IA sin sustituir por etiquetas genéricas.
- Itera antes de regenerar: si el contenido es correcto pero algo falla en tono, formato o extensión, un prompt breve de iteración es más rápido que empezar desde cero.
- Verifica cada paso del flujo antes de avanzar: los errores en los pasos intermedios se propagan al resultado final si no los detectas a tiempo.
- Saber cuándo NO usar IA es tan importante como saber cómo usarla: hay tareas que requieren juicio humano y otras que son más rápidas sin IA.

---

## 21. CONEXIÓN CON EL RESTO DEL CURSO

Esta sesión cierra el Módulo 2 y sienta la base técnica del resto del curso. Los flujos de prompts aprendidos hoy son la arquitectura sobre la que se construyen todas las prácticas de los módulos siguientes: en **D04-D07** (Módulo 3) se aplicará el encadenamiento a tareas concretas de redacción, comunicación y documentación; en **D08-D09** (Módulo 4) se combinará con herramientas específicas de análisis y organización. La iteración, en particular, es la habilidad que más diferencia a los usuarios avanzados de los principiantes a lo largo de todo el curso. Y los flujos documentados de hoy son la materia prima del proyecto final de D16-D17: en D09 el alumno revisará sus flujos y elegirá el que quiere desarrollar como proyecto personal.

---

## 22. FOOTER

*Brief para NotebookLM · D03 · Edición 01/26 — IA en la Oficina*
