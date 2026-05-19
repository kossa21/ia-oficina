# BRIEF PARA NOTEBOOKLM — D04
## Módulo 3, Sesión 1: Simplificando tareas repetitivas con IA
## Curso: IA en la Oficina – Eficiencia y Productividad
## Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital

---

## 2. CONTEXTO DEL CURSO

**Programa:** IA en la Oficina – Eficiencia y productividad (68 horas · 17 sesiones de 4 horas)
**Público:** Personal administrativo y de oficina sin experiencia previa en IA generativa. Todos los alumnos utilizan cuentas personales de Gmail; no hay cuentas corporativas ni licencias de Microsoft 365.
**Metodología:** ~40 % teoría y demo · ~50 % práctica guiada · ~10 % puesta en común
**Sesión anterior (D03):** El grupo ya domina el encadenamiento de prompts y la iteración. Tiene flujos de tareas propias documentados en al menos 3 prompts encadenados.

> *Este documento es la fuente del notebook de hoy. Además de las diapositivas, puedes pedirle a NotebookLM un resumen en **audio** (tipo pódcast), un **vídeo**, una **infografía** o mapa mental, una **guía de estudio**, **fichas** (flashcards), un **cuestionario** para autoevaluarte, o **escribir tus preguntas en el chat**. Usa el formato con el que mejor aprendas. No escribas datos personales reales en el chat.*

---

## 3. RESUMEN DE LA SESIÓN

Entre el 60 y el 70 % del tiempo de un perfil administrativo se invierte en tareas que siguen siempre el mismo patrón: respuestas tipo, confirmaciones, informes periódicos, convocatorias. Hoy aprenderemos a identificar cuáles de esas tareas merece la pena automatizar con IA y a construir plantillas reutilizables que acortan de horas a minutos el trabajo más recurrente. Trabajaremos con la técnica de generación en lote, que permite obtener varias respuestas o documentos en una sola consulta, y descubriremos cómo Gemini en Google Docs puede redactar, reescribir y reformatear directamente en el documento que ya tenemos abierto. Al final de la sesión cada alumno se llevará al menos una plantilla personal lista para usar la semana siguiente y un método para guardar sus mejores prompts sin tener que reescribirlos cada vez.

---

## 4. ESTRUCTURA DE LA SESIÓN (240 min)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| Apertura | 15 min | Repaso de D03: flujos encadenados · Objetivos del día |
| Teórico-demostrativo | 75 min | Qué tareas repetitivas automatizar · Generación en lote · Gemini en Google Docs · Guardar prompts |
| Descanso | 15 min | — |
| Práctica guiada | 95 min | Demo Gemini en Docs + automatizar tarea propia + comparativa de herramientas |
| Puesta en común | 40 min | Plantillas creadas · Mini-entregable · Cierre |

---

## 5. OBJETIVOS DE APRENDIZAJE

1. Identificar qué tareas repetitivas de escritura merece la pena automatizar con IA y cuáles no.
2. Usar ChatGPT, Gemini o Claude para generar contenido en lote (varias respuestas a la vez en una sola consulta).
3. Aplicar las funciones de Gemini en Google Docs para redactar, reescribir y reformatear sin salir del documento.
4. Guardar los mejores prompts en un sistema personal reutilizable para no reescribirlos cada vez.

---

## 6. DESARROLLO TEÓRICO EN PROSA

### Las tareas repetitivas de oficina: cuáles son y cuánto tiempo cuestan

Hay una pregunta que conviene hacerse al empezar cualquier semana laboral: ¿qué voy a hacer esta semana que ya hice exactamente igual la semana pasada? Para la mayoría de los perfiles administrativos la respuesta incluye una lista bastante larga. Marta, administrativa en una empresa de distribución mediana, lleva ocho años en el mismo puesto y tiene bien identificadas las suyas: todos los lunes por la mañana responde entre seis y ocho consultas de clientes que preguntan por el estado de sus pedidos, redacta las convocatorias de reunión interna para el martes, y rellena el parte de incidencias semanal con el mismo formato de siempre. El miércoles cierra las facturas pendientes y el viernes revisa que todos los albaranes del mes estén cotejados. Cada una de esas tareas parece pequeña, pero sumadas representan más de la mitad de su jornada.

Los estudios sobre trabajo administrativo estiman que entre el 60 y el 70 % del tiempo de estos perfiles se dedica a tareas que siguen un patrón fijo: misma estructura, distintos datos. Las categorías más habituales son las respuestas estándar a consultas frecuentes, donde la pregunta cambia pero la respuesta es siempre la misma con variaciones menores; las confirmaciones y acuses de recibo; la adaptación del mismo comunicado a distintos destinatarios con pequeños ajustes de nombre, referencia o fecha; el rellenado de formularios tipo a partir de datos variables; las convocatorias de reunión generadas a partir de una agenda fija; los informes periódicos con estructura ya definida (semanales, mensuales, trimestrales); y los resúmenes de reuniones recurrentes que siguen siempre el mismo esquema.

El criterio para decidir si vale la pena automatizar una tarea es sencillo: si la tarea tarda más de diez minutos y se repite al menos dos veces por semana, es candidata. Si además sigue siempre la misma estructura, pasa a ser prioritaria. La cuenta es fácil: una tarea de 20 minutos que se hace tres veces por semana supone una hora al día, cinco horas a la semana, y más de 50 horas al año. Si esa tarea se puede delegar a la IA en dos minutos dejando solo el tiempo de revisión y ajuste, el ahorro es enorme. Por otro lado, no toda tarea repetitiva merece automatizarse: si requiere un criterio personal genuino que cambia con cada caso, si tiene consecuencias graves en caso de error sin revisión, o si el tiempo de escribir el prompt supera el de hacerla directamente, entonces se hace a mano.

> **Puntos clave:**
> - Criterio de automatización: tarea >10 min + se repite ≥2 veces/semana + estructura fija = candidata prioritaria
> - Cálculo rápido: 20 min × 3/semana = más de 50 horas anuales; con IA: 2 min de prompt + 3 de revisión
> - No automatizar: si requiere criterio cambiante por caso, consecuencias graves sin revisión o es más rápido hacerlo a mano

### Generación en lote: cinco respuestas de un golpe

La forma más habitual de usar la IA es pedir una cosa cada vez. Pero cuando se trata de tareas repetitivas, hay una técnica mucho más eficiente: pedir todas las variaciones de una vez. A esto se le llama generación en lote, y funciona igual que cuando en una panadería se decide hacer cien panes en vez de uno: el horno consume casi el mismo tiempo pero el resultado se multiplica.

Imagina que Marta necesita construir un banco de respuestas tipo para las incidencias más frecuentes de su empresa. En vez de pedir cada respuesta por separado, puede pedir las cinco de golpe en un único prompt:

> "Actúa como responsable de atención al cliente en una empresa de distribución. Genera 5 respuestas tipo para las siguientes situaciones: (1) cliente que pregunta por el estado de su expediente, (2) cliente que reclama un retraso en la entrega, (3) cliente que solicita cambio de datos de facturación, (4) cliente que pide una factura duplicada, (5) cliente que desea cancelar un servicio. Cada respuesta debe tener tono formal y empático, un máximo de 80 palabras, e incluir un hueco para [NOMBRE_CLIENTE] y otro para [REFERENCIA]. No hagas promesas de fechas concretas ni ofrezcas compensaciones económicas."

El resultado es un banco de cinco respuestas que Marta puede guardar en un documento de Google Docs, ajustar una vez y reutilizar durante meses. En lugar de invertir 30 minutos redactando las cinco respuestas una a una, ha invertido 2 minutos en el prompt y otros 5 en revisar y ajustar el resultado. El ahorro es de más del 80 % del tiempo.

La generación en lote funciona igual para otros tipos de contenido: cinco versiones de un mismo correo para distintos destinatarios, diez asuntos de correo para elegir el mejor, cuatro formatos distintos del mismo informe, o tres variaciones de tono para una misma comunicación. La clave está en describir bien las variantes dentro del mismo prompt y dar todas las instrucciones de formato y restricciones de una sola vez.

> **Puntos clave:**
> - Un solo prompt puede generar 5 variaciones distintas en menos de 2 minutos
> - Incluir todas las instrucciones de formato y restricciones en el mismo prompt es esencial
> - Aplica a correos, asuntos, informes y variaciones de tono; no es solo para respuestas de clientes

### Gemini en Google Docs: las cinco funciones más útiles para tareas repetitivas

Cuando se trabaja directamente en Google Docs, no hace falta salir al navegador para usar la IA. Gemini está integrado en Google Docs y permite trabajar dentro del propio documento sin copiar ni pegar. Esto cambia el flujo de trabajo de forma importante: en vez de ir de la herramienta al documento y volver, la asistencia ocurre donde ya se está trabajando. Para alguien como Marta, que tiene abiertos varios documentos a la vez, esto supone no perder el hilo entre pestaña y pestaña.

Las cinco funciones más útiles para tareas repetitivas son las siguientes. La primera es redactar desde cero: describes en el panel de Gemini qué documento necesitas, con qué estructura y para quién, y Gemini genera el borrador directamente en el documento. La segunda es reescribir: seleccionas un párrafo que ya tienes, abres Gemini y le pides que lo reescriba con tono más formal, más breve o adaptado a otro destinatario. La tercera es reformatear: si tienes una lista de puntos y necesitas un párrafo fluido (o al revés), Gemini hace la conversión en segundos sin que tengas que reescribir nada. La cuarta es completar: escribes el inicio de un documento, el encabezado o los primeros párrafos, y le pides a Gemini que lo complete siguiendo la misma línea y estructura. La quinta es resumir: en un documento largo, Gemini puede generar el resumen ejecutivo al instante, listo para pegarse en el encabezado o enviarse por separado.

Es importante saber que la disponibilidad de Gemini dentro de Google Docs puede variar según la región y la versión de la cuenta. Si en el aula no estuviera disponible para algún alumno, el mismo flujo funciona perfectamente con ChatGPT o Claude usando la técnica del copiar y pegar: se copia el texto del documento, se pega en el chat con las instrucciones, y el resultado mejorado se vuelve a pegar en el documento. Es un paso más, pero el resultado es equivalente. Lo importante es no quedarse sin herramienta por dependencia de una sola opción.

> **Puntos clave:**
> - 5 funciones clave: redactar, reescribir, reformatear, completar y resumir, sin salir del documento
> - Elimina el tiempo perdido entre pestaña y pestaña en flujos de trabajo intensivos
> - Si Gemini no está disponible, ChatGPT o Claude con copiar/pegar dan el mismo resultado

### Guardar prompts favoritos: cuatro estrategias para no reescribir nunca lo que ya funciona

Uno de los errores más frecuentes entre personas que empiezan a usar IA en su trabajo es escribir un prompt excelente, obtener un resultado muy bueno, y no guardarlo. Al día siguiente, cuando necesitan hacer lo mismo, tienen que volver a pensar cómo escribirlo y el resultado no es igual. Es como encontrar el punto exacto de sal en una receta y no anotarlo.

Hay cuatro estrategias para evitar esto. La primera son las conversaciones guardadas en ChatGPT: cuando terminas una conversación que ha dado buenos resultados, puedes renombrarla con un nombre descriptivo como "Respuesta queja cliente" o "Convocatoria reunión mensual". Así las tienes organizadas y accesibles la próxima vez que las necesitas. La segunda es crear un Google Doc personal llamado "Mi biblioteca de prompts", organizado por categoría de tarea (correos, informes, resúmenes, convocatorias) y con una breve nota del contexto en que funciona mejor cada prompt. Este documento se convierte en la herramienta de trabajo diaria y puede compartirse con el equipo si se quiere. La tercera es guardar los prompts más usados como borradores en el correo electrónico: una carpeta de borradores con los tres o cuatro prompts más recurrentes, listos para copiar en cualquier momento desde el móvil o el ordenador sin tener que abrir otra aplicación. La cuarta son los Gemini Gems: los Gems son asistentes personalizados gratuitos dentro de Google Gemini que se configuran con instrucciones fijas. Se puede crear un Gem llamado "Atención al cliente distribución" que ya tenga incorporado el rol, el contexto de la empresa y las restricciones habituales, de modo que solo hay que escribir la tarea concreta sin repetir el marco cada vez. Los Gems son la alternativa gratuita a los GPTs personalizados de ChatGPT Plus, y funcionan con una cuenta de Gmail normal sin coste adicional. Si por alguna razón los Gems no estuvieran disponibles en la cuenta del alumno, el Google Doc de biblioteca de prompts cumple la misma función perfectamente.

> **Puntos clave:**
> - 4 estrategias: conversaciones guardadas (ChatGPT), Google Doc biblioteca, borradores de correo, Gemini Gems
> - Los Gems son la alternativa gratuita a GPTs personalizados; funcionan con Gmail sin coste adicional
> - Un prompt guardado hoy evita reescribirlo mañana; cada prompt guardado es tiempo recuperado

### La revisión como paso no negociable

Automatizar una tarea con IA no significa quitarse esa tarea de encima. Significa transformar el tiempo que se invertía en redactar en tiempo que se invierte en revisar. La revisión siempre existe; lo que cambia es su naturaleza: en vez de escribir desde cero, se lee lo que la herramienta ha generado, se ajusta lo que no encaja y se verifica que todos los campos variables están rellenados correctamente. Marta lo describía así: "Antes tardaba 10 minutos en escribir el correo. Ahora tardo 2 en revisarlo. Pero sigo leyendo cada correo antes de enviarlo, porque si hay un error es mío, no de la IA." Esa responsabilidad nunca desaparece. El modelo de confianza es siempre: la IA genera el borrador, la persona lo valida. Este paso de revisión es también el momento en que el criterio humano añade valor: si el tono no encaja con la situación concreta, si hay una variable que falta, si la respuesta es correcta pero no suficiente para ese caso particular.

> **Puntos clave:**
> - Automatizar no elimina la revisión; transforma redactar (10 min) en revisar (2 min)
> - La responsabilidad del resultado es siempre del usuario; la IA genera borradores
> - La revisión es el momento de añadir criterio propio: tono, contexto específico, ajustes

### Adaptar el mismo mensaje a distintos destinatarios en un solo prompt

Una variante especialmente útil de la generación en lote es pedir versiones del mismo mensaje para destinatarios o canales distintos. Esto va más allá de cambiar el nombre: implica adaptar el nivel de detalle, el tono y incluso la extensión según quién lee. Marta, por ejemplo, debe comunicar el mismo retraso en una entrega a tres personas distintas: al director general le bastará con tres líneas que mencionen el impacto y la solución; al gestor de logística le interesa el detalle operativo completo; y al cliente afectado le conviene un mensaje empático que priorice la disculpa. Las tres comunicaciones transmiten la misma información esencial pero cada una habla el idioma del destinatario. Con un único prompt bien construido, que describa los tres perfiles y pida el texto adaptado para cada uno, Marta obtiene los tres borradores en menos de dos minutos y solo tiene que rellenar los datos reales de cada caso.

> **Puntos clave:**
> - Un solo prompt puede generar versiones distintas para director, gestor operativo y cliente
> - La adaptación no es solo de tono; incluye nivel de detalle, extensión y énfasis
> - Describe cada perfil destinatario dentro del prompt para obtener resultados diferenciados

### Construir el mapa personal de tareas automatizables

Antes de empezar a automatizar, vale la pena dedicar 20 minutos a hacer un inventario. No un inventario de todas las tareas del puesto, sino solo de las que cumplen el criterio de automatización: más de 10 minutos, al menos dos veces por semana, estructura fija. Marta lo hizo al volver de la sesión anterior y encontró siete candidatas claras. Las ordenó por volumen de tiempo semanal y empezó por la que más tardaba. Este mapa es también el punto de partida del mini-entregable de hoy y del proyecto final: las mejores plantillas nacen de tareas reales y cuantificadas, no de ejemplos genéricos. Para construirlo, basta con una tabla de cuatro columnas: nombre de la tarea, tiempo promedio por ejecución, frecuencia semanal, total semanal estimado. Las filas con mayor tiempo total son las primeras candidatas. Las que además siguen siempre exactamente la misma estructura son las prioritarias.

> **Puntos clave:**
> - Tabla de 4 columnas: nombre de la tarea, tiempo/ejecución, frecuencia/semana, total/semana estimado
> - Mayor tiempo total × estructura fija = candidata prioritaria para automatizar con IA
> - El mapa se hace una vez y se revisa cada trimestre; es el punto de partida del proyecto final

### Variables condicionales: plantillas que cubren más de una situación

Una plantilla con corchetes simples cubre una situación fija con datos variables. Pero hay una variante más potente: la plantilla condicional, que con un pequeño cambio en el prompt de instrucción produce respuestas distintas según el estado del caso. Imagina que Marta tiene tres posibles estados para una incidencia: en curso, resuelta y escalada. En vez de tener tres plantillas separadas, puede tener una sola con una variable de estado que guía el tono y el contenido: si el estado es "en curso", el correo es informativo y promete seguimiento; si es "resuelta", es positivo y ofrece confirmación; si es "escalada", es más formal e incluye nombre del responsable nuevo. Para implementarlo no hace falta código: basta con añadir una instrucción al principio del prompt que diga "Si [ESTADO] es 'en curso', el tono es informativo; si es 'resuelta', el tono es positivo; si es 'escalada', el tono es formal y menciona [RESPONSABLE_NUEVO]". La IA procesa la condición y genera el texto adecuado cada vez.

> **Puntos clave:**
> - Una plantilla condicional cubre múltiples estados con un solo prompt bien estructurado
> - La condición se describe en lenguaje natural dentro del prompt, sin necesidad de código
> - Reduce el número de plantillas que hay que mantener actualizadas de tres a una sola

---

## 7. DATOS Y CIFRAS CLAVE

- **60–70 %** del tiempo de trabajo administrativo corresponde a tareas con estructura repetitiva.
- Una tarea de **20 min × 3 veces/semana = más de 50 horas al año**. Con IA, el mismo resultado en 2–4 min de prompt + revisión.
- Generación en lote: un solo prompt produce **5 respuestas tipo** en menos de 2 minutos, frente a 25–30 minutos redactándolas una a una.
- Empresas que han implantado plantillas de IA para respuestas de atención al cliente reportan **reducciones del 40–60 %** en tiempo de gestión de incidencias frecuentes.
- Un banco de prompts guardados reduce el tiempo de configuración de cada tarea repetitiva a **menos del 10 %** del tiempo original.
- **Gemini en Google Docs:** ahorra el tiempo de copiar/pegar entre herramientas, lo que en un flujo de trabajo intensivo puede suponer **15–20 minutos diarios**.
- Tener una plantilla con [CORCHETES] para variables reduce los errores de personalización (olvidar cambiar el nombre del destinatario, la referencia, la fecha) a prácticamente cero.
- Las **plantillas condicionales** (con instrucción "si estado X, tono Y") permiten cubrir 3 situaciones distintas con una sola plantilla, reduciendo el mantenimiento a la tercera parte.

---

## 8. EJEMPLOS RESUELTOS PASO A PASO

### Caso 1: Banco de respuestas para incidencias de expediente

**Situación:** Marta recibe entre 6 y 10 correos semanales preguntando por el estado de expedientes. Cada respuesta tarda entre 5 y 8 minutos. Quiere un banco de respuestas tipo que pueda personalizar en 30 segundos.

**Prompt exacto:**
> "Actúa como responsable de atención al cliente en una empresa de distribución logística. Genera 5 respuestas tipo para correo electrónico, cubriendo estas situaciones: (1) el expediente está en proceso normal y en plazo, (2) hay un retraso por causa del proveedor, (3) el expediente está resuelto y ya se ha enviado la documentación, (4) falta documentación del cliente para continuar, (5) el expediente fue escalado a otro departamento. Cada respuesta: tono formal-empático, entre 60 y 90 palabras, con [NOMBRE_CLIENTE] y [REFERENCIA_EXPEDIENTE] como campos variables. No hagas promesas de fechas exactas."

**Resultado comentado:** La IA genera cinco correos bien estructurados con saludo, cuerpo informativo y cierre, todos con los corchetes en las posiciones correctas. El tono es homogéneo y profesional.

**Cómo iterarlo:** Si algún correo resulta demasiado formal o demasiado genérico: "La respuesta 2 suena demasiado fría. Reescríbela añadiendo una frase de disculpa genuina al inicio, manteniendo el resto igual." O para añadir firma: "Añade a todas las respuestas un hueco de firma con [NOMBRE_AGENTE] y [TELÉFONO_DIRECTO]."

---

### Caso 2: Convocatoria de reunión semanal con Gemini en Google Docs

**Situación:** Todos los lunes Marta envía la convocatoria de reunión de coordinación del martes. El formato es siempre el mismo: asunto, lista de asistentes, orden del día y logística. Lo hace a mano y tarda 10–12 minutos.

**Prompt exacto (en el panel de Gemini dentro de Google Docs):**
> "Redacta una convocatoria de reunión de coordinación semanal. Asistentes: [LISTA_ASISTENTES]. Fecha: [FECHA], hora: [HORA], sala: [SALA]. Orden del día: (1) revisión de incidencias de la semana anterior, (2) actualización de pedidos pendientes, (3) asignación de prioridades para la semana. Formato: correo formal con asunto, párrafo de contexto de una frase, lista del orden del día numerada, y logística (sala, duración estimada 45 minutos, confirmación antes del lunes a las 14:00 h). Tono: directo y profesional."

**Resultado comentado:** Gemini genera la convocatoria directamente en el documento, formateada y lista. Marta solo rellena los corchetes con los datos reales de esa semana y la envía.

**Cómo iterarlo:** "Añade una línea al inicio que mencione que en esta semana hay cierre de trimestre, para que los asistentes vengan con sus datos actualizados." O si es demasiado largo: "Reduce la convocatoria a un máximo de 120 palabras, manteniendo el orden del día completo."

---

### Caso 3: Plantilla de informe de incidencias mensual

**Situación:** A final de cada mes Marta elabora el informe de incidencias para dirección. La estructura es siempre la misma pero tarda entre 45 y 60 minutos en juntar los datos y darles formato.

**Prompt exacto:**
> "Actúa como asistente administrativo en una empresa de distribución. Crea una plantilla de informe mensual de incidencias con las siguientes secciones: (1) Resumen ejecutivo (máximo 5 líneas), (2) Tabla de incidencias con columnas Fecha / Tipo / Cliente / Descripción breve / Estado / Responsable, (3) Análisis por categorías (entregas, facturación, documentación, otros), (4) Comparativa con mes anterior (formato: este mes X incidencias vs mes anterior Y), (5) Acciones correctivas propuestas. Deja todos los campos variables en [CORCHETES]. Tono formal."

**Resultado comentado:** La plantilla queda lista con toda la estructura. Marta solo tiene que rellenar los datos reales cada mes, lo que reduce el tiempo de elaboración de 45–60 minutos a unos 15–20 minutos.

**Cómo iterarlo:** "Añade al inicio una portada con campos [MES], [AÑO], [PREPARADO_POR] y [FECHA_ENVÍO]. Añade también una sección final de 'Conclusiones y recomendaciones' con hueco para texto libre."

---

### Caso 4: Adaptar el mismo comunicado a tres destinatarios distintos

**Situación:** Marta necesita comunicar un retraso en la entrega de un pedido importante. Tiene que enviar tres mensajes: uno al director general, uno al responsable de logística y uno al cliente afectado. Cada perfil necesita información distinta y un tono diferente. Hacerlos uno a uno le llevaría 20–25 minutos.

**Prompt exacto:**
> "Actúa como responsable de comunicación en una empresa de distribución. Ha ocurrido un retraso de [DÍAS] días en la entrega del pedido [REFERENCIA] del cliente [CLIENTE]. La causa es [CAUSA]. La nueva fecha estimada es [NUEVA_FECHA]. Redacta tres mensajes distintos para: (1) Director general: máximo 5 líneas, enfoque en impacto y solución; (2) Responsable de logística: detalle operativo completo, acciones correctivas y seguimiento; (3) Cliente afectado: tono empático, disculpa genuina, nueva fecha confirmada, sin tecnicismos. No hagas promesas adicionales más allá de la fecha indicada."

**Resultado comentado:** Los tres mensajes adaptan la misma información esencial al idioma de cada destinatario. El director ve el impacto y la solución. El logístico ve el detalle y las acciones. El cliente recibe la disculpa y la certeza de la fecha.

**Cómo iterarlo:** Si el tono del mensaje al cliente resulta demasiado formal: "Reescribe el mensaje al cliente con un tono más cercano, como si lo enviara directamente la persona que gestiona su pedido, no el departamento corporativo." O para añadir un cuarto destinatario: "Añade un cuarto mensaje para el equipo interno de atención al cliente: instrucciones claras de qué responder si el cliente llama esta semana."

---

## 9. GLOSARIO

**Tarea repetitiva:** Tarea que sigue siempre la misma estructura con variaciones solo en los datos, y que por tanto es candidata a automatizarse con IA.

**Generación en lote:** Técnica que consiste en pedir a la IA varias respuestas, versiones o documentos distintos dentro de un mismo prompt, en vez de hacer una petición por separado para cada uno.

**Plantilla con corchetes:** Documento o respuesta con campos variables marcados entre [CORCHETES] que se rellenan manualmente con los datos reales de cada caso, ahorrando tiempo de redacción y evitando errores de personalización.

**Gemini en Google Docs:** Asistente de IA de Google integrado directamente en el editor de documentos, que permite redactar, reescribir, reformatear y resumir sin salir del documento.

**Gemini Gems:** Asistentes personalizados gratuitos dentro de Google Gemini, configurados con instrucciones fijas de rol, contexto y restricciones, que evitan tener que repetirlas en cada consulta.

**Biblioteca de prompts:** Documento personal (por ejemplo, un Google Doc) donde se guardan los mejores prompts organizados por tipo de tarea, para reutilizarlos sin reescribirlos.

**Automatización de escritura:** Uso de IA para generar, completar o transformar texto de forma semi-automática, con supervisión y ajuste humano en el resultado final.

**Campo variable:** Elemento de una plantilla que cambia en cada uso (nombre del cliente, fecha, referencia de expediente) y se marca con un indicador visible como [NOMBRE_CLIENTE] para identificarlo rápidamente.

**Criterio de automatización:** Regla práctica para decidir si una tarea merece automatizarse: tarda más de 10 minutos y se repite al menos 2 veces por semana, y sigue una estructura fija.

**Plantilla condicional:** Plantilla que incluye una instrucción del tipo "si [VARIABLE] es X, el tono es Y" para generar respuestas distintas según el estado del caso, con un único prompt en lugar de múltiples plantillas separadas.

**Mapa de tareas automatizables:** Inventario personal de las tareas de un puesto que cumplen el criterio de automatización, organizado por tiempo total semanal estimado, que sirve de punto de partida para priorizar qué automatizar primero.

**Anonimización de datos:** Proceso de sustituir datos reales identificables (nombres, DNI, importes, referencias) por variables genéricas (CLIENTE_A, IMPORTE_X) antes de usarlos en un prompt de IA, para proteger la privacidad de las personas.

---

## 10. ERRORES COMUNES Y BUENAS PRÁCTICAS

**Error 1 — Intentar automatizar tareas que requieren criterio personal genuino.** No toda tarea repetitiva es automatizable. Si la decisión cambia radicalmente según el contexto emocional o relacional de cada caso, la IA genera texto pero el criterio sigue siendo tuyo. Úsala para el borrador y aplica tu criterio en la revisión.

**Error 2 — No revisar el resultado antes de enviar.** La generación en lote produce resultados muy buenos, pero siempre pueden quedar frases genéricas, datos inventados o un tono que no encaja exactamente. La regla es: la IA redacta, tú supervisas y ajustas antes de enviar o usar.

**Error 3 — Olvidar rellenar los corchetes.** El mayor riesgo de las plantillas con variables es enviar un documento con [NOMBRE_CLIENTE] sin rellenar. Antes de enviar, busca siempre el símbolo "[" en el documento para verificar que todos los campos variables están completados.

**Error 4 — Pegar datos personales reales en el prompt.** Nunca incluyas en un prompt nombres reales de clientes, DNI, números de cuenta, importes de nómina o datos de expedientes identificables. Sustituye siempre por variables genéricas: CLIENTE_A, IMPORTE_X, REFERENCIA_Y. Esto protege tanto a las personas como a la empresa, y es especialmente importante si el documento trata sobre situaciones sensibles.

**Error 5 — No guardar los prompts que funcionan.** Escribir un prompt excelente y no guardarlo es uno de los errores más costosos. Cada prompt guardado es tiempo recuperado en el futuro. Aunque sea con una nota en el móvil, guarda siempre lo que ha dado buen resultado.

**Buena práctica — Nombrar las conversaciones guardadas con claridad.** En ChatGPT, en vez de dejar el nombre automático, renombra cada conversación útil con el tipo de tarea: "Respuesta retraso entrega", "Convocatoria reunión coordinación", "Informe incidencias mensual". Localizar el prompt en segundos vale mucho cuando el tiempo aprieta.

**Error 6 — Usar plantillas sin adaptarlas al contexto real.** Una plantilla generada en el aula con datos ficticios es un punto de partida, no un documento definitivo. Antes de usarla en el trabajo real hay que revisar que el tono encaja con la cultura de la empresa, que las restricciones reflejan las políticas internas y que el formato es el que se espera. Tratar la plantilla como si ya estuviera lista es uno de los errores que más confianza hace perder en la herramienta.

**Buena práctica — Actualizar la biblioteca de prompts.** Los prompts evolucionan. Cuando encuentres una versión mejor de un prompt que ya tenías guardado, actualiza el Google Doc. Marca con fecha la última versión para saber cuál es la más reciente.

---

## 11. ACTIVIDADES EN AULA

**Actividad 1 — Demo: Gemini en Google Docs en directo [Grupo · 20 min]**

El formador abre en pantalla un Google Doc con cinco puntos desordenados (datos de una reunión ficticia) y, usando Gemini dentro del documento, genera primero una convocatoria formal, luego la reescribe con tono más informal, y finalmente la convierte en una lista de tareas asignadas. Los alumnos observan el flujo completo y replican el último paso en sus propios equipos. Objetivo: interiorizar que la IA trabaja dentro del documento, no fuera de él.

**Actividad 2 — Automatiza tu tarea repetitiva [Individual · 55 min]**

Cada alumno elige la tarea repetitiva que más tiempo le consume de su puesto real (o de su mapa de oportunidades de D01) y la automatiza con la herramienta de su elección (ChatGPT, Gemini o Claude). Debe producir al menos una plantilla reutilizable con campos variables en [CORCHETES], lista para usar la semana siguiente. El formador circula por el aula resolviendo dudas individuales. Durante los últimos 10 minutos, cada alumno escribe una frase describiendo cuánto tiempo le ahorrará esta plantilla a la semana.

**Actividad 3 — Comparativa ChatGPT vs Gemini vs Claude [Grupo · 20 min]**

El mismo prompt de generación en lote (las 5 respuestas tipo de Marta) se lanza simultáneamente en ChatGPT, Gemini y Claude. El grupo compara los resultados en pantalla: ¿cuál es más conciso?, ¿cuál tiene mejor tono?, ¿cuál sigue mejor las instrucciones de formato?, ¿cuál añade cosas que no se pidieron? El formador modera el debate y extrae conclusiones sobre cuándo usar cada herramienta para tareas de este tipo.

*Total práctica guiada: 20 + 55 + 20 = 95 min.*

---

## 12. 🔁 TRABAJO EN PAREJAS / GRUPO

Durante los últimos 10 minutos de la Actividad 2, antes de pasar a la Actividad 3, los alumnos se agrupan por parejas (o tríos si el número es impar). Cada persona le muestra a su compañero la plantilla que ha creado, explica para qué tarea sirve y cuánto tiempo estima que le ahorrará. El compañero sugiere al menos una mejora: un campo variable que falta, una restricción que añadir, una iteración que podría mejorar el resultado. Esta revisión cruzada en pareja dura 10 minutos y el objetivo es que cada alumno salga con una versión mejorada de su plantilla, no solo la primera que generó. Durante la Actividad 3 todo el grupo trabaja conjuntamente comparando las tres herramientas: cada subgrupo de 3–4 personas toma una herramienta diferente, lanza el prompt y presenta el resultado al resto.

---

## 13. EJERCICIOS SUGERIDOS

Ver Banco de Ejercicios:
- **EJ-D04-1 (Individual):** Construye un banco de 3 respuestas tipo para las incidencias más frecuentes de tu puesto usando generación en lote.
- **EJ-D04-2 (Pareja):** Intercambia tu plantilla con un compañero. Cada uno la prueba con datos ficticios, apunta qué falla o falta, y propone una iteración de mejora.
- **EJ-D04-3 (Grupo):** El grupo elige una tarea repetitiva común (convocatoria de reunión, informe de incidencias) y cada subgrupo la automatiza con una herramienta diferente. Se comparan los resultados y se vota la mejor plantilla.

---

## 14. CUESTIONARIO DE AUTOEVALUACIÓN

**1. ¿Qué porcentaje del tiempo administrativo corresponde, según los estudios, a tareas repetitivas?**
a) Entre el 20 y el 30 %
b) Entre el 40 y el 50 %
c) Entre el 60 y el 70 % ✓
d) Entre el 80 y el 90 %

**2. Una tarea de 20 minutos que se repite 3 veces por semana supone, al año:**
a) Unas 20 horas anuales
b) Más de 50 horas anuales ✓
c) Unas 10 horas anuales
d) Más de 100 horas anuales

**3. ¿Qué es la generación en lote?**
a) Generar el mismo texto en varios idiomas a la vez
b) Pedir varias versiones o respuestas distintas dentro de un mismo prompt ✓
c) Usar varias herramientas de IA al mismo tiempo
d) Guardar múltiples prompts en un solo documento

**4. ¿Cuál de estas tareas NO es una buena candidata para automatizar con IA?**
a) Convocatorias de reunión semanales con la misma estructura
b) Respuestas tipo a consultas frecuentes de clientes
c) Una decisión estratégica que depende de criterio personal y contexto emocional ✓
d) Informes mensuales con estructura fija

**5. ¿Qué significa poner [NOMBRE_CLIENTE] en una plantilla?**
a) Que ese campo se rellena automáticamente con IA
b) Que ese campo es un campo variable que hay que rellenar manualmente en cada uso ✓
c) Que ese campo es opcional y puede eliminarse
d) Que la IA buscará el nombre en internet

**6. ¿Cuál es la alternativa gratuita a los GPTs personalizados de ChatGPT Plus para usuarios con Gmail?**
a) Claude Pro
b) Perplexity Premium
c) Gemini Gems ✓
d) NotebookLM

**7. ¿Cuál es el mayor riesgo a la hora de usar plantillas con corchetes?**
a) Que la IA cambie el formato del documento
b) Enviar el documento sin rellenar todos los campos variables ✓
c) Que los corchetes no se muestren bien en todos los dispositivos
d) Que la plantilla sea demasiado larga para la IA

**8. Si no tienes acceso a Gemini dentro de Google Docs, ¿cómo puedes hacer el mismo trabajo?**
a) No es posible, Gemini es imprescindible
b) Usando Microsoft Word con Copilot
c) Usando ChatGPT o Claude con copiar y pegar el texto del documento ✓
d) Solo con NotebookLM

**9. ¿Qué debes hacer ANTES de pegar el texto de un documento de trabajo real en un prompt de IA?**
*Respuesta abierta:* Anonimizar los datos personales reales: sustituir nombres de personas por CLIENTE_A o PERSONA_X, importes reales por IMPORTE_X, referencias identificables por REFERENCIA_Y. Nunca pegar datos como DNI, números de cuenta, salarios o información sensible de personas reales.

**10. Nombra dos estrategias para guardar prompts favoritos y no tener que reescribirlos cada vez.**
*Respuesta abierta:* Cualquiera de las cuatro: conversaciones guardadas en ChatGPT con nombre descriptivo; Google Doc "Mi biblioteca de prompts" organizado por tipo de tarea; borradores en el correo electrónico con los prompts más usados; Gemini Gems configurados con instrucciones fijas.

**11. ¿Qué diferencia hay entre redactar desde cero con Gemini en Google Docs y reescribir un texto existente?**
*Respuesta abierta:* Redactar desde cero parte de una descripción en el panel de Gemini y genera el documento completo; reescribir parte de texto ya escrito que se selecciona y sobre el que Gemini aplica cambios de tono, extensión o formato indicados por el usuario.

**12. ¿Qué es una plantilla condicional y en qué se diferencia de una plantilla con corchetes?**
a) Una plantilla que detecta automáticamente los datos del destinatario
b) Una plantilla que solo funciona con Gemini Gems
c) Una plantilla con instrucciones del tipo "si el estado es X, el tono es Y", que genera respuestas distintas según el caso con un único prompt ✓
d) Una plantilla que usa variables entre llaves {} en lugar de corchetes []

**13. ¿Cuáles son las cuatro columnas del mapa personal de tareas automatizables?**
a) Nombre, herramienta, dificultad y prioridad
b) Nombre de la tarea, tiempo por ejecución, frecuencia semanal y total semanal estimado ✓
c) Nombre, coste, beneficio y riesgo
d) Nombre, tipo, canal y destinatario

**14. Un mismo comunicado de retraso en una entrega se adapta para tres destinatarios distintos en un solo prompt. ¿Cuál de estas adaptaciones es correcta?**
a) Director general: detalle operativo completo; cliente: 5 líneas con impacto; logístico: tono empático
b) Director general: 5 líneas con impacto y solución; logístico: detalle operativo; cliente: disculpa empática y fecha ✓
c) Los tres mensajes deben ser idénticos para no generar confusión
d) Director general: el más largo; los otros dos: versión resumida del primero

**15. Describe el flujo completo de Marta al usar una plantilla de respuesta tipo el lunes por la mañana.**
*Respuesta abierta:* Marta abre su biblioteca de prompts, localiza el prompt correspondiente al tipo de incidencia, lo pega en la herramienta de IA con los datos del caso real (anonimizados si es necesario), revisa el resultado generado, rellena todos los [CORCHETES] con los datos reales del caso específico, verifica que no queda ningún campo sin rellenar y envía. El tiempo total es de 2–3 minutos frente a los 8–10 minutos originales.

---

## 15. PREGUNTAS FRECUENTES (FAQ)

**¿Puedo usar estas plantillas directamente en mi trabajo sin adaptarlas?**
Las plantillas generadas en el aula son puntos de partida, no productos finales. Siempre hay que ajustar el tono al de tu empresa, verificar que el formato encaja con los estándares internos, y asegurarte de que el contenido refleja correctamente tu situación real. Considera la plantilla de la IA como un borrador del 80 %, no como un documento definitivo.

**¿Qué pasa si Gemini no está disponible en mi cuenta de Google Docs?**
No hay problema: el mismo resultado se obtiene con ChatGPT o Claude usando copiar y pegar. Copias el texto que quieres procesar, lo pegas en el chat junto con las instrucciones, obtienes el resultado mejorado y lo pegas de vuelta en el documento. Es un paso más pero el resultado es equivalente. Muchos alumnos acaban prefiriendo este flujo por la flexibilidad que ofrece.

**¿Los Gemini Gems son gratuitos para siempre?**
Los Gems están incluidos en el plan gratuito de Google Gemini, pero las condiciones de los planes gratuitos pueden cambiar. Por eso siempre se recomienda tener también una biblioteca de prompts en Google Doc como alternativa que no depende de ningún plan concreto. Verifica las condiciones actuales en gemini.google.com antes de confiar completamente en esta herramienta para tu trabajo diario.

**¿Cuántos prompts debo guardar en mi biblioteca?**
No hay un número mínimo ni máximo. El criterio es: si has usado un prompt más de dos veces o si el resultado fue especialmente bueno, guárdalo. Una biblioteca de 10–15 prompts bien organizados y actualizados vale más que una de 100 prompts que no recuerdas cómo funcionan.

**¿Puedo compartir mi biblioteca de prompts con el equipo?**
Sí, y es una de las mejores prácticas de productividad colectiva. Un Google Doc compartido con el equipo, donde cada persona aporta los prompts que mejor le han funcionado, crea rápidamente un recurso valioso para todos. Asegúrate de que los prompts del documento no contengan datos reales de clientes o de la empresa: deben ser solo la estructura, con los campos variables en corchetes.

**¿La IA puede "aprender" mis preferencias con el tiempo?**
En las versiones gratuitas, cada conversación nueva empieza desde cero sin memoria de las anteriores. Por eso los Gems y la biblioteca de prompts son tan útiles: compensan esa falta de memoria proporcionando el contexto necesario al inicio de cada consulta. Algunas herramientas ofrecen función de memoria en sus planes de pago, pero para el trabajo diario la biblioteca de prompts funciona perfectamente.

**¿Cuánto tiempo tarda en verse el ahorro real?**
La mayoría de alumnos que han implementado sus primeras plantillas empiezan a notar el ahorro en la primera o segunda semana de uso. El mayor salto se produce cuando se completa el banco de 5–10 respuestas tipo para las incidencias más frecuentes: a partir de ese momento, responder a una consulta recurrente pasa de 8–10 minutos a 1–2 minutos de personalización y envío.

**¿Puedo usar la generación en lote para mensajes en distintos idiomas?**
Sí. El mismo principio de lote aplica a traducciones: describes el mensaje en español y pides también la versión en inglés, francés u otro idioma en el mismo prompt. La clave es indicar claramente las restricciones de tono y vocabulario para cada idioma. Si necesitas consistencia terminológica con documentos internos, incluye un glosario de términos clave en el prompt para que la IA los respete.

**¿Las plantillas de un puesto sirven para otros puestos de la empresa?**
Parcialmente. La estructura y la lógica de una plantilla (criterio de automatización, campos variables, instrucciones de tono) suele ser transferible. El contenido específico (terminología interna, nombres de departamentos, flujos de aprobación) hay que adaptarlo. Lo más eficiente es compartir la estructura del prompt y que cada persona complete el contexto propio de su puesto. Un Google Doc compartido con el equipo, donde cada uno aporta sus plantillas más útiles, crea rápidamente una biblioteca colectiva.

**¿Qué hago si la IA genera un campo variable que no esperaba en el resultado?**
Pídele que lo elimine en la iteración: "Elimina el campo [FIRMA_EMPRESA] de todas las respuestas; los alumnos añadirán la firma desde su cliente de correo." O mejor aún: anticipa en el prompt qué campos variables quieres exactamente, para no tener que corregir después. Especificar "usa solo los campos variables [NOMBRE_CLIENTE] y [REFERENCIA]" en el prompt evita que la IA introduzca campos que no necesitas.

---

## 16. HERRAMIENTAS DE LA SESIÓN

Todas las herramientas son gratuitas con cuenta personal de Gmail. Ver detalles en `Recursos/Herramientas_Gratuitas.md`.

| Herramienta | Uso en esta sesión | Acceso |
|---|---|---|
| **ChatGPT** (OpenAI) | Generación en lote, plantillas, comparativa | chat.openai.com · cuenta Google |
| **Google Gemini** | Comparativa, Gems personalizados | gemini.google.com · Gmail |
| **Gemini en Google Docs** | Redactar, reescribir, reformatear dentro del doc | docs.google.com · Gmail (disponibilidad puede variar) |
| **Claude** (Anthropic) | Comparativa, documentos más largos | claude.ai · cuenta Google |
| **Google Docs** | Crear y guardar plantillas, biblioteca de prompts | docs.google.com · Gmail |
| **Google NotebookLM** | Material del día: audio, guía, cuestionario | notebooklm.google.com · Gmail |

*Nota: Microsoft Copilot no se usa en este curso. Si tu empresa ya te proporciona Copilot, los conceptos de esta sesión aplican igualmente.*

---

## 17. MINI-ENTREGABLE DEL DÍA

**Nombre:** Mi plantilla automatizada
**Formato:** Google Doc o archivo de texto guardado en Google Drive
**Contenido:** Una plantilla de documento o respuesta (correo tipo, informe periódico, convocatoria, comunicado) creada con IA, con todos los campos variables marcados en [CORCHETES], lista para reutilizar en el puesto real del alumno. El documento debe incluir una nota breve indicando para qué situación sirve y cuánto tiempo estima el alumno que le ahorrará por semana.
**Cómo alimenta el proyecto final:** Las plantillas creadas hoy son el primer activo reutilizable del proyecto final. En el proyecto se incluirá un banco de al menos 3 plantillas de este tipo, documentadas y organizadas para ser usadas de forma inmediata en el puesto de trabajo.

---

## 18. 🎓 HILO DEL PROYECTO FINAL

Para tu proyecto final: lo de hoy te sirve para construir el banco de plantillas reutilizables que formará el núcleo del proyecto, demostrando que sabes automatizar las tareas más recurrentes de tu puesto y cuantificar el ahorro de tiempo que aporta cada una.

---

## 19. MENSAJE CLAVE

> "La tarea que haces igual cada semana es la primera candidata a desaparecer de tu lista. No para que no se haga, sino para que se haga sola. Automatizar lo repetitivo no es trabajar menos: es liberar tiempo para lo que realmente requiere tu criterio."

---

## 20. IDEAS PARA RECORDAR

- Si una tarea tarda más de 10 minutos y se repite al menos 2 veces por semana, es candidata a automatizarse con IA.
- La generación en lote permite obtener 5 respuestas tipo en el tiempo que antes costaba hacer una sola.
- Gemini en Google Docs trabaja dentro del documento, sin necesidad de copiar y pegar entre aplicaciones; si no está disponible, ChatGPT con copiar y pegar da el mismo resultado.
- Un prompt guardado hoy es tiempo recuperado la semana que viene: la biblioteca de prompts es tan valiosa como la propia herramienta.
- Nunca envíes una plantilla sin verificar que todos los [CORCHETES] han sido rellenados con los datos reales.
- La revisión nunca desaparece: automatizar significa transformar 10 minutos redactando en 2 minutos revisando, con toda la responsabilidad puesta en esos 2 minutos.
- Un mensaje para tres destinatarios distintos no es trabajo triple: un solo prompt bien construido genera el director, el técnico y el cliente en una sola consulta.

---

## 21. CONEXIÓN CON EL RESTO DEL CURSO

Esta sesión cierra el aprendizaje técnico de los módulos 1 y 2 (qué es la IA, cómo se le habla) y lo convierte en productividad concreta. Lo de hoy parte directamente de los flujos encadenados que el grupo documentó en D03: ahora esos flujos se convierten en plantillas permanentes y reutilizables. La sesión siguiente, D05, llevará más lejos la transformación de documentos: aprenderemos a resumir para distintos destinatarios y a convertir información entre formatos (texto a tabla, párrafo a checklist, notas informales a informe formal), que son las otras grandes capacidades de la IA para el trabajo diario de oficina. Las plantillas creadas hoy se usarán como punto de partida en varias actividades del resto del módulo 3.

---

## 22. FOOTER

*Brief para NotebookLM · D04 · Edición 01/26 — IA en la Oficina*
