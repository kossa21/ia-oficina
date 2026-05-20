# BRIEF PARA NOTEBOOKLM — D15
## Módulo 7, Sesión 2: Atención al cliente y gestión de situaciones difíciles con IA
## Curso: IA en la Oficina – Eficiencia y Productividad
## Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital

**Fecha:** Martes 21 de julio de 2026 · 15:00–19:00 h · Día 15 de 17

---

## 2. CONTEXTO DEL CURSO

**Programa:** IA en la Oficina – Eficiencia y Productividad (68 horas · 17 sesiones de 4 horas)
**Público:** Personal administrativo y de oficina sin experiencia previa en IA generativa
**Metodología:** ~40 % teoría y demostración · ~50 % práctica guiada · ~10 % puesta en común
**Sesión anterior (D14):** El grupo documenta procedimientos en SOPs, crea checklists y mapea flujos de trabajo con IA. Saben cómo estructurar y compartir el conocimiento operativo.

> *Este documento es la fuente del notebook de hoy. Además de las diapositivas, puedes pedirle a NotebookLM un resumen en **audio** (tipo pódcast), un **vídeo**, una **infografía** o mapa mental, una **guía de estudio**, **fichas** (flashcards), un **cuestionario** para autoevaluarte, o **escribir tus preguntas en el chat**. Usa el formato con el que mejor aprendas. No escribas datos personales reales en el chat.*

---

## 3. RESUMEN DE LA SESIÓN

La atención al cliente es una de las áreas donde la IA ofrece el mayor retorno inmediato, pero también donde sus límites son más visibles: hay situaciones en las que el cliente necesita sentir que hay una persona real al otro lado, y ningún texto generado por IA puede sustituir eso. Hoy aprendemos a usar la IA para lo que hace bien —construir bancos de respuestas, adaptar el tono a múltiples canales, estructurar escalados, gestionar el tiempo en situaciones frecuentes— y a reconocer cuándo no es la herramienta adecuada. La sesión incluye una de las dinámicas más prácticas del curso: el role-play en parejas, donde uno hace de cliente difícil y el otro usa la IA para elaborar la respuesta en tiempo real. Al final del día, cada alumno tiene un banco de respuestas FAQ listo para usar mañana mismo.

---

## 4. ESTRUCTURA DE LA SESIÓN (240 min)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| Apertura | 15 min | Repaso D14 + objetivos del día |
| Teórico-demostrativo | 75 min | El coste de la mala atención · Banco FAQ desde casos reales · Patrón RIA · Multicanal · Escalados · Privacidad |
| Descanso | 15 min | — |
| Práctica guiada | 95 min | Demo banco FAQ · Role-play en parejas · Banco personal |
| Puesta en común | 40 min | Revisión de bancos + mini-entregable + cierre |

*(15+75+15+95+40 = 240 min)*

---

## 5. OBJETIVOS DE APRENDIZAJE

1. Construir un banco de respuestas FAQ a partir de consultas reales (anonimizadas) con un único prompt en lote.
2. Aplicar el patrón Reconoce / Informa / Actúa (RIA) a situaciones de queja o reclamación con ayuda de IA.
3. Adaptar el mismo mensaje a tres canales (correo formal, respuesta rápida en Teams/WhatsApp, guion telefónico) en minutos.
4. Identificar cuándo la IA no es suficiente y la intervención humana directa es imprescindible.

---

## 6. DESARROLLO TEÓRICO EN PROSA

### El coste real de una respuesta mal gestionada

Marta gestiona, entre otras cosas, las consultas y reclamaciones que llegan al departamento de administración de su empresa de distribución. Cada semana llegan entre 20 y 30 correos de clientes: algunos preguntan por el estado de sus pedidos, otros reclaman un error en la factura, otros están frustrados porque llevan tres semanas esperando una resolución. Antes de este curso, Marta redactaba cada respuesta desde cero, buscando el tono correcto, revisando qué había pasado con ese expediente y asegurándose de no hacer promesas que no podía cumplir. Cada correo le llevaba entre 8 y 15 minutos. Con un banco de respuestas tipo bien construido y los prompts adecuados, ese tiempo se reduce a 2–3 minutos por caso, y la calidad de la respuesta es consistentemente alta.

El coste de una mala gestión de atención al cliente va más allá del tiempo del trabajador: una respuesta tarde, ambigua o con un tono inadecuado puede escalar una consulta menor a una reclamación formal, dañar la relación con un cliente fiel o generar trabajo adicional para otros departamentos. La IA no garantiza respuestas perfectas, pero sí respuestas consistentes, bien estructuradas y adaptadas al tono que la organización quiere proyectar, siempre que los prompts estén bien construidos y la persona que los usa mantenga el criterio profesional sobre el resultado final.

> **Puntos clave:**
> - Cada correo tipo se reduce de 8–15 min a 2–3 min con IA
> - Una mala respuesta escala consultas menores a reclamaciones formales
> - La IA aporta consistencia de tono y estructura, no perfección
> - El criterio profesional sigue siendo del trabajador, no del modelo

### Construir un banco FAQ desde casos reales

El primer paso para sistematizar la atención con IA es construir un banco de respuestas a partir de las consultas más frecuentes. El proceso tiene tres fases. La primera es **identificar las categorías**: revisar la bandeja de entrada de los últimos tres meses (anonimizando nombres y referencias) e identificar los cinco o seis tipos de consulta que se repiten. No hace falta analizarlas todas: las más frecuentes representan el 80 % del volumen.

La segunda fase es **generar las respuestas en lote** con un único prompt:

> "Actúa como responsable de atención al cliente de una empresa de distribución. Genera 5 respuestas tipo para las siguientes consultas frecuentes, todas en tono formal y empático, máximo 100 palabras cada una, con campos variables en [CORCHETES]: (1) cliente que pregunta por el estado de su pedido, (2) cliente que reclama un error en su factura, (3) cliente que solicita cambiar su dirección de envío, (4) cliente que lleva 3 semanas esperando una resolución y está frustrado, (5) cliente que cancela un pedido y pide confirmación. Para la opción (4), usa el patrón Reconoce / Informa / Actúa."

La tercera fase es **organizar el banco** en un Google Doc con secciones por categoría, los campos variables claramente marcados y una nota de cuándo usar cada plantilla. Este banco se convierte en el recurso de trabajo diario: antes de redactar una respuesta desde cero, se comprueba si hay una plantilla aplicable.

> **Puntos clave:**
> - Identifica las 5–6 categorías que cubren el 80 % del volumen
> - Genera las plantillas en un único prompt en lote
> - Marca campos variables en [CORCHETES] para personalizar al usar
> - Organiza el banco en Google Doc por categoría con nota de uso

### El patrón Reconoce / Informa / Actúa (RIA) en profundidad

El patrón RIA, introducido en D06 para correos de clientes, cobra especial importancia en situaciones donde el cliente está frustrado, lleva tiempo esperando o percibe que no se le ha dado la atención que merece. Aplicado correctamente, este patrón transforma una respuesta defensiva en una respuesta que mantiene la relación.

El **Reconoce** es la parte más difícil de escribir sin IA y la más importante para el cliente. No es una disculpa vacía ("lamentamos las molestias"), sino un reconocimiento específico de la situación: "Entiendo que llevas tres semanas esperando una respuesta sobre tu expediente y que eso es frustrante, especialmente cuando afecta a tu planificación." La IA ayuda a formular este reconocimiento de forma genuina y sin frases hechas.

El **Informa** explica con claridad y sin excusas lo que ha ocurrido, lo que está ocurriendo ahora mismo y lo que impide una resolución más rápida, si aplica. La clave es ser honesto sin descargar responsabilidades en el cliente. La IA puede formular esta parte de forma objetiva y sin defensividad si el prompt incluye los hechos reales.

El **Actúa** es el compromiso concreto: qué va a pasar, quién es el responsable y cuándo se tendrá una respuesta. "Voy a escalar este caso a [RESPONSABLE] hoy antes de las 17:00 h y recibirás una respuesta con el estado actualizado antes del [FECHA]. Si no la recibes, puedes contactarme directamente en [CONTACTO]." La acción concreta con plazo real es lo que convierte una respuesta de atención en una solución.

> **Puntos clave:**
> - Reconoce específico, sin frases hechas ("lamentamos las molestias")
> - Informa con honestidad: hechos, no excusas ni descargos
> - Actúa con compromiso concreto: acción, responsable y plazo real
> - El Actúa convierte una respuesta de atención en una solución

### Adaptación multicanal: el mismo mensaje en tres formatos

Los clientes y las consultas internas llegan por múltiples canales: correo electrónico, Teams, WhatsApp corporativo, teléfono. El mismo mensaje necesita formatos completamente distintos según el canal, y la IA puede generar los tres en segundos a partir de la respuesta base:

> "A partir de esta respuesta de correo formal [PEGAR RESPUESTA], genera: (a) una versión corta para Teams o WhatsApp de máximo 3 líneas, manteniendo la información esencial; (b) un guion de 5 puntos para una llamada telefónica que cubra la misma información en conversación hablada."

El correo formal puede tener 200 palabras con saludo, cuerpo estructurado y despedida. El mensaje de Teams necesita ser directo, sin saludo y en no más de 3 líneas. El guion de teléfono es una serie de puntos que el trabajador usa como referencia durante la llamada, no un texto que lee literalmente.

> **Puntos clave:**
> - Mismo contenido, tres formatos según canal (correo, Teams, teléfono)
> - Correo formal: 200 palabras con saludo y despedida
> - Teams/WhatsApp: 3 líneas, directo, sin saludo formal
> - Guion telefónico: lista de puntos, no texto para leer literalmente

### Escalados que funcionan: pasar el caso sin perder información

Uno de los mayores problemas en la gestión de reclamaciones es el escalado: cuando un caso supera las competencias de quien lo recibe y tiene que pasarse a otro departamento o a un superior, con frecuencia se pierde información o el cliente tiene que repetir todo desde el principio. La IA ayuda a estructurar el escalado para que quien lo recibe tenga todo lo que necesita sin hacer preguntas adicionales:

> "Redacta un mensaje de escalado interno para [RESPONSABLE_DEL_ESCALADO] sobre el caso de [CLIENTE_ANONIMIZADO]. Incluye: (1) resumen del problema en 3 líneas, (2) historial de contactos (qué se ha dicho y qué se ha prometido), (3) qué necesita el cliente y cuándo, (4) qué tengo yo competencia para resolver y qué no, (5) qué necesito de ti para cerrar el caso."

> **Puntos clave:**
> - Un escalado mal estructurado obliga a llamar al cliente otra vez
> - Cinco bloques: problema, historial, necesidad, competencia, petición concreta
> - Incluye siempre lo que ya se ha prometido al cliente
> - El receptor del escalado debe poder actuar sin pedirte aclaraciones

### Privacidad en atención al cliente: la regla más importante de hoy

La atención al cliente trabaja por definición con datos personales: nombre del cliente, número de contrato, expediente, importe, dirección. Estos datos no pueden pegarse en ninguna herramienta de IA externa sin anonimizar. La regla es simple y no admite excepciones:

Antes de pegar cualquier correo de cliente en ChatGPT, Gemini o Claude, sustituye: nombre del cliente → CLIENTE_A, número de expediente → REF_EXPEDIENTE_X, importe → IMPORTE_X, dirección → DIRECCIÓN_Y. El nombre del trabajador que responde puede dejarse si es el propio, pero los datos identificativos del cliente siempre se protegen.

Si el caso es tan específico que la anonimización hace la consulta inútil, la alternativa es trabajar con una descripción genérica del problema y el patrón de respuesta, y luego personalizar manualmente con los datos reales. En ningún caso se suben expedientes, contratos o datos de clientes a herramientas de IA externas sin verificar su política de privacidad.

> **Puntos clave:**
> - Nombre → CLIENTE_A, expediente → REF_X, importe → IMPORTE_X
> - Si la anonimización hace la consulta inútil, usa descripción genérica
> - Nunca subir expedientes o contratos a IA externa sin verificar política
> - La privacidad no admite excepciones, incluso bajo presión de tiempo

### Cuándo no usar IA en atención al cliente

La IA no reemplaza el juicio humano ni la empatía real. Hay situaciones donde lo correcto es dejar de lado el banco de respuestas y escribir o hablar directamente:

- Cliente en una situación de grave angustia emocional (pérdida, enfermedad, urgencia vital)
- Casos con implicaciones legales o contractuales que requieren validación jurídica
- Situaciones donde el error fue de la organización y el cliente merece una disculpa genuina y personalizada
- Clientes con los que hay una relación de mucho tiempo y que esperan un trato personal

La IA es una herramienta de productividad, no un sustituto de la relación humana. Saber cuándo no usarla es tan importante como saber cómo usarla bien.

> **Puntos clave:**
> - Angustia grave del cliente requiere respuesta humana genuina
> - Casos legales o contractuales necesitan validación jurídica previa
> - Errores graves de la organización merecen disculpa personal, no plantilla
> - Saber cuándo no usar IA es tan importante como saber cómo usarla

### Aprender de cada caso: el ciclo de mejora del banco FAQ

Un banco FAQ no es un documento estático: es un sistema vivo que mejora cada semana con la experiencia real de su uso. Marta descubre, después de tres semanas usando su banco, que algunas plantillas necesitan ajustes: la respuesta a "cambio de dirección" omitía un dato que el cliente siempre pregunta después, la respuesta al cliente frustrado se sentía demasiado formal cuando el cliente había escrito con tono coloquial, y faltaba una categoría completamente nueva (clientes que preguntan por el plazo de devolución).

El ciclo de mejora tiene cuatro pasos. Primero, **etiquetar** cada respuesta que se envía indicando qué plantilla del banco se usó como base (puede ser una nota al final del correo en la carpeta de enviados). Segundo, **revisar semanalmente** qué respuestas generaron una segunda consulta del cliente: si el cliente vuelve a preguntar algo que la plantilla ya cubría, la plantilla no estaba siendo clara. Tercero, **actualizar la plantilla** con la información que faltaba o el tono que conectaba mejor. Cuarto, **documentar el cambio** con una breve nota en el Google Doc del banco para que el equipo entienda por qué se modificó.

Este ciclo de mejora convierte el banco FAQ de una herramienta inicial en un activo del equipo que mejora con el tiempo. La diferencia entre un banco mantenido y un banco abandonado es lo que separa una herramienta útil durante seis meses de una herramienta útil durante años.

> **Puntos clave:**
> - Etiqueta cada envío con la plantilla base usada para trazabilidad
> - Revisa semanalmente qué respuestas generaron una segunda consulta
> - Actualiza plantillas según la experiencia real de uso
> - Documenta el cambio en el Doc compartido para todo el equipo

---

## 7. DATOS Y CIFRAS CLAVE

- El 67 % de los clientes que abandonan una empresa citan una mala experiencia de atención como razón principal (Salesforce, 2023).
- El tiempo medio de respuesta a consultas de cliente sin sistema de respuestas tipo: 8–15 min por caso. Con banco FAQ: 2–3 min.
- Usando el patrón RIA, la tasa de escalado de reclamaciones baja un 40 % en las primeras semanas de implementación.
- Un banco de 5 respuestas tipo bien construido cubre el 70–80 % de las consultas frecuentes de la mayoría de roles administrativos.
- Antes / Después: generar 5 respuestas tipo para las consultas más frecuentes → antes: 60–90 min; con un prompt en lote: 5 min.
- El 45 % de los clientes espera una respuesta en menos de 24 horas; el 12 % la espera en menos de 1 hora.
- Adaptar una respuesta formal a formato Teams y a guion de teléfono con IA: 30 segundos. Sin IA: 10–15 min.

---

## 8. EJEMPLOS RESUELTOS PASO A PASO

### Caso 1 — Banco de respuestas FAQ en lote

**Situación:** Marta quiere crear un banco de respuestas para las consultas más frecuentes que recibe de clientes sobre pedidos y facturación.

**Prompt exacto:**
> "Actúa como responsable de administración de una empresa de distribución. Genera 5 respuestas tipo para estas consultas frecuentes de clientes. Tono: formal y empático. Máximo 100 palabras por respuesta. Incluye campos variables en [CORCHETES] donde sea necesario. (1) Cliente pregunta por el estado de su pedido REF: ¿cuándo llega? (2) Cliente reclama que le han cobrado un importe incorrecto en su factura. (3) Cliente quiere cambiar su dirección de entrega para el próximo pedido. (4) Cliente lleva 3 semanas esperando la resolución de una incidencia y está frustrado. (5) Cliente solicita la cancelación de un pedido pendiente de envío."

**Resultado comentado:** La IA genera 5 plantillas en 20 segundos. Marta revisa la de la situación 4 (cliente frustrado) para verificar que el tono del "Reconoce" sea genuino y no una frase hecha. Añade el campo [FECHA_RESOLUCIÓN] al Actúa porque la IA lo había dejado genérico.

**Cómo iterarlo:** "Para la respuesta 4, reescribe el primer párrafo con un tono más cálido. La situación es que el cliente lleva 3 semanas esperando y nosotros tuvimos un problema interno que retrasó la resolución, aunque no lo explicamos en su momento."

---

### Caso 2 — Adaptación multicanal de una respuesta

**Situación:** Marta tiene una respuesta formal de 180 palabras a un cliente que pregunta por el estado de su expediente. Necesita enviar también un mensaje rápido por Teams al contacto interno que lleva el caso.

**Prompt exacto:**
> "A partir de este correo formal a un cliente [PEGAR CORREO ANONIMIZADO], genera: (a) una versión interna para Teams de máximo 3 líneas, con el mismo contenido esencial pero tono directo y sin saludo formal — es para mi compañero/a de logística; (b) un guion de 5 puntos para llamar por teléfono al cliente si no responde al correo en 24 horas."

**Resultado comentado:** La IA genera los dos formatos en 10 segundos. El mensaje de Teams es directo y concreto. El guion telefónico cubre los puntos clave sin ser un texto para leer literalmente.

---

### Caso 3 — Escalado estructurado a otro departamento

**Situación:** Una reclamación de cliente supera las competencias de Marta y necesita pasarla al departamento de logística con toda la información necesaria para que no tengan que llamar al cliente de nuevo.

**Prompt exacto:**
> "Redacta un mensaje interno de escalado al departamento de logística sobre la siguiente situación (datos anonimizados): CLIENTE_A solicitó el 10 de junio cambiar la dirección de entrega de su pedido REF_X. Se confirmó el cambio por correo. El pedido llegó a la dirección original el 15 de junio. El cliente reclamó el 16 y espera resolución antes del 20. Yo no tengo acceso al sistema de logística para verificar qué pasó. Incluye: resumen del problema, historial de contactos, qué necesita el cliente y cuándo, y qué necesito de logística para cerrar el caso."

**Resultado comentado:** El escalado tiene toda la información necesaria para que logística actúe sin hacer preguntas adicionales. Marta solo tiene que personalizar los nombres reales antes de enviarlo.

**Cómo iterarlo:** "Adapta el mismo mensaje a una versión más corta para Teams (máximo 3 líneas) que sirva como aviso inmediato a logística antes del correo oficial."

---

### Caso 4 — Respuesta al cliente frustrado con patrón RIA

**Situación:** Marta recibe un correo de un cliente que lleva 3 semanas esperando la resolución de una incidencia de facturación. El cliente está visiblemente molesto y dice que va a cancelar su contrato si no recibe respuesta hoy. Marta tiene que responder en menos de 1 hora.

**Paso 1 — Anonimizar antes de pegar el correo en la IA:** Marta sustituye el nombre del cliente por CLIENTE_A, el número de expediente por REF_X y el importe disputado por IMPORTE_X. El nombre de su propia empresa también lo sustituye por EMPRESA si va a aparecer en el prompt.

**Prompt exacto:**
> "Responde a este correo de cliente frustrado usando el patrón Reconoce / Informa / Actúa. Tono: empático pero profesional. Máximo 150 palabras. El cliente CLIENTE_A lleva 3 semanas esperando respuesta sobre el expediente REF_X. La realidad es que el caso se quedó atascado por un cambio interno de departamento que no le comunicamos. Hoy hemos verificado que su reclamación es válida y procede el ajuste por IMPORTE_X. Mi compromiso: confirmación oficial del ajuste antes del viernes a las 17h, con justificante por email. Si no recibe nada, mi contacto directo es ext. 234."

**Resultado comentado:** La IA genera una respuesta de 140 palabras. El Reconoce evita la frase hecha y nombra específicamente las tres semanas y el silencio. El Informa explica el cambio interno sin descargar responsabilidad en el cliente. El Actúa incluye fecha concreta, formato del justificante y vía de contacto directo. Marta solo personaliza con el nombre real, revisa que el tono sea coherente con la cultura de la empresa, y envía en menos de 15 minutos.

**Cómo iterarlo:** "Ahora reescribe el primer párrafo con un tono más cálido — el cliente lleva 4 años con nosotros y es importante que sienta que valoramos esa relación, no solo que resolvemos su incidencia."

---

## 9. GLOSARIO

**Banco FAQ:** Colección organizada de respuestas tipo para las consultas más frecuentes, con campos variables en [CORCHETES]; reduce el tiempo de respuesta y garantiza consistencia de tono.

**Patrón RIA (Reconoce / Informa / Actúa):** Estructura de respuesta a quejas y reclamaciones: primero reconocer específicamente la situación del cliente, luego informar con claridad y honestidad, finalmente comprometerse a una acción concreta con plazo.

**Escalado:** Transferencia de un caso a otra persona o departamento con más competencia o autoridad para resolverlo; efectivo cuando incluye toda la información relevante sin que el cliente tenga que repetirla.

**Anonimización en atención al cliente:** Sustituir nombre, número de expediente, importes y datos identificativos del cliente por etiquetas genéricas (CLIENTE_A, REF_EXPEDIENTE_X) antes de usar la IA para procesar el caso.

**Adaptación multicanal:** Transformar el mismo mensaje a los diferentes formatos y tonos que exige cada canal: correo formal (extenso, con saludo/despedida), Teams/WhatsApp (3 líneas, directo), teléfono (guion de puntos, conversacional).

**Guion de llamada:** Lista de puntos clave que el trabajador usa como referencia durante una llamada telefónica; no es un texto para leer sino un recordatorio de los temas que hay que cubrir.

**Tasa de escalado:** Porcentaje de consultas que necesitan ser transferidas a un nivel superior; un buen banco FAQ y el patrón RIA la reducen significativamente.

**Empatía en la respuesta:** Reconocimiento genuino y específico de la situación y las emociones del cliente; diferente de las frases hechas ("lamentamos las molestias") y difícil de conseguir sin pensar en el caso concreto.

**Campo variable:** Marca tipo [NOMBRE_CLIENTE] o [FECHA] dentro de una plantilla, que se sustituye por el valor real antes de enviar el mensaje; permite reutilizar la misma plantilla con personalización mínima.

**Ciclo de mejora del banco:** Proceso continuo de etiquetar, revisar, actualizar y documentar las plantillas a partir de la experiencia real de uso; convierte el banco FAQ en un activo del equipo que mejora con el tiempo.

**Cliente frustrado:** Cliente que ha experimentado un retraso, error o silencio prolongado por parte de la organización y cuya prioridad emocional es sentirse escuchado antes que recibir la solución técnica.

**Tono institucional:** Estilo de comunicación adoptado por una organización (formal, cercano, técnico, accesible); definirlo y pegarlo como ejemplo en el prompt es la mejor forma de que la IA respete el tono de la empresa.

---

## 10. ERRORES COMUNES Y BUENAS PRÁCTICAS

**Error 1 — Pegar datos del cliente directamente en la IA.** El error de privacidad más grave en esta sesión. Siempre anonimizar antes: nombre → CLIENTE_A, expediente → REF_X, importe → IMPORTE_X. No hay excepciones.

**Error 2 — Usar el banco FAQ sin personalizar.** Una plantilla sin personalizar suena a plantilla. Los campos variables ([NOMBRE_CLIENTE], [REFERENCIA], [FECHA]) deben completarse siempre antes de enviar. Además, a veces el caso tiene algún elemento específico que merece una línea personalizada.

**Error 3 — Usar IA para situaciones que requieren empatía humana real.** Un cliente en angustia grave, un error importante de la organización o una relación de largo recorrido requieren una respuesta genuinamente humana. La IA puede ayudar a structurarla, pero no debe ser el único autor.

**Error 4 — El "Reconoce" como frase hecha.** "Lamentamos las molestias ocasionadas" no es reconocer: es un cliché que los clientes perciben como desinterés. El Reconoce efectivo es específico: "Entiendo que llevas 3 semanas sin una resolución, y eso es inaceptable."

**Error 5 — Escalado sin toda la información.** Un escalado incompleto obliga a quien lo recibe a llamar al cliente para pedir datos que ya tenías. El prompt de escalado debe incluir siempre el historial de contactos y lo que se ha prometido.

**Buena práctica — Revisa el banco FAQ cada trimestre.** Las consultas más frecuentes cambian con las temporadas, los productos o los procesos. Dedica 15 minutos al trimestre a añadir las nuevas categorías y actualizar las plantillas obsoletas.

**Error 6 — No coincidir el tono de la respuesta con el del cliente.** Si el cliente escribe con tono cercano y coloquial y la IA produce una respuesta extremadamente formal, el cliente percibe distancia. Pide explícitamente: "Adapta el registro al tono del correo del cliente, manteniendo la profesionalidad pero sin sonar institucional."

**Buena práctica — Etiqueta tus envíos con la plantilla utilizada.** Una breve nota mental ("usé plantilla 2 con cambio en el Actúa") permite revisar después qué funcionó y qué no. Esa información alimenta el ciclo de mejora del banco FAQ semana a semana.

---

## 11. ACTIVIDADES EN AULA

### Actividad 1 — Demo: banco FAQ desde tickets ficticios [Grupo · 20 min]

**Descripción:** El formador proyecta 10 correos ficticios de clientes (variados: consultas, quejas, solicitudes, urgencias). En directo, construye el banco FAQ con un único prompt en lote, mostrando cómo la IA agrupa y responde. El grupo evalúa la calidad del Reconoce en la respuesta a la queja y propone mejoras.

**Objetivo:** Ver el flujo completo de construcción del banco FAQ antes de hacerlo individualmente.

**Material:** 10 correos ficticios de clientes (Google Doc compartido).

---

### Actividad 2 — Role-play: cliente difícil con IA en tiempo real [Pareja · 45 min]

**Descripción:** Por parejas. Persona A recibe una tarjeta de escenario con el perfil del cliente difícil (elige entre: cliente frustrado por retraso de 3 semanas, cliente que acusa de error de facturación que no existió, cliente agresivo que amenaza con cancelar todo). Persona B tiene 90 segundos para usar la IA y elaborar una respuesta con el patrón RIA. Después se intercambian los roles con un escenario diferente. Debrief: ¿qué funcionó? ¿qué añadió la persona que la IA no capturó? ¿cuándo hubieras respondido sin IA?

**Objetivo:** Practicar el uso de la IA bajo presión de tiempo, en situaciones difíciles, y reconocer cuándo el criterio humano supera al texto generado.

**Material:** Tarjetas de escenario (3 opciones diferentes para cada pareja).

---

### Actividad 3 — Mi banco de respuestas personal [Individual · 30 min]

**Descripción:** Cada alumno construye su propio banco de 5 respuestas tipo para las situaciones más frecuentes de su área (consultas internas, proveedores, clientes, según su puesto). Puede usar el prompt en lote de la demo o adaptarlo a su contexto.

**Objetivo:** Salir del curso con un banco de respuestas real y listo para usar en el trabajo.

**Material:** Google Doc propio, ChatGPT o Gemini.

---

## 12. 🔁 TRABAJO EN PAREJAS

La **Actividad 2** es el momento más intenso y valioso del día: el **role-play en parejas**. Persona A adopta el perfil del cliente difícil indicado en la tarjeta de escenario (no improvisa: lee el contexto y lo interpreta con autenticidad). Persona B tiene 90 segundos para elaborar una respuesta con la IA usando el patrón RIA. La restricción de tiempo es deliberada: simula la presión real de la atención al cliente. Después del intercambio de roles, la pareja dedica 5 minutos a reflexionar: ¿la IA capturó el tono correcto? ¿Había algo en la situación que requería un elemento que la IA no añadió? ¿Cuándo habrías preferido responder sin IA? Esta reflexión es tan valiosa como el propio ejercicio.

---

## 13. EJERCICIOS SUGERIDOS

Ver Banco de Ejercicios:
- **EJ-D15-1** (Individual): Construir banco FAQ de 5 respuestas para las consultas más frecuentes del puesto propio
- **EJ-D15-2** (Pareja): Role-play cliente difícil con 3 escenarios diferentes y debrief
- **EJ-D15-3** (Grupo): Comparar bancos FAQ de 3 puestos distintos e identificar respuestas transferibles entre áreas

---

## 14. CUESTIONARIO DE AUTOEVALUACIÓN

**1. ¿Qué significa el patrón RIA?**
a) Responde, Informa, Actúa
b) Reconoce, Informa, Actúa ✓
c) Recibe, Investiga, Actúa
d) Resuelve, Informa, Avanza

**2. ¿Cuál es el error más grave al usar IA para atención al cliente?**
a) Usar plantillas en lugar de textos originales
b) Pegar datos personales del cliente sin anonimizar ✓
c) Adaptar el tono a múltiples canales
d) Usar el banco FAQ para más de una categoría de consulta

**3. ¿Qué hace que el "Reconoce" del patrón RIA sea efectivo?**
a) Que sea corto y directo
b) Que incluya una disculpa formal
c) Que sea específico sobre la situación del cliente, no una frase hecha ✓
d) Que vaya al principio y al final de la respuesta

**4. ¿Por qué los escalados son más efectivos cuando se estructuran con IA?**
Respuesta abierta: Porque la IA ayuda a incluir de forma organizada toda la información necesaria: **resumen del problema, historial de contactos, qué promesas se han hecho, qué necesita el cliente y cuándo, y qué necesita la persona que escala del departamento receptor**. Esto evita que quien recibe el escalado tenga que llamar al cliente para obtener información que ya estaba disponible.

**5. ¿En qué situaciones NO es adecuado usar IA para la respuesta al cliente?**
a) Cuando la consulta es muy frecuente y ya tienes plantilla
b) Cuando el cliente lleva tiempo esperando y está frustrado
c) Cuando el cliente está en una situación de angustia grave o el error fue importante y merece una respuesta genuinamente humana ✓
d) Cuando hay que adaptar el mensaje a múltiples canales

**6. ¿Cuántas respuestas tipo necesita una persona para cubrir el 70-80 % de sus consultas frecuentes?**
a) 15-20
b) 10-12
c) 5-6 ✓
d) 30 o más

**7. ¿Cuál es la diferencia entre un correo formal de atención y un mensaje de Teams para el mismo caso?**
Respuesta abierta: El correo formal es **extenso** (100-200 palabras), con saludo, cuerpo estructurado, despedida y tono institucional. El mensaje de Teams es **directo** (máximo 3 líneas), sin saludo formal y orientado a la acción concreta. La IA genera ambos en segundos a partir del texto base.

**8. ¿Qué debe incluir siempre el "Actúa" del patrón RIA?**
a) Una disculpa por el problema
b) El nombre del responsable de la organización
c) Una acción concreta con un responsable y un plazo específico ✓
d) Una oferta de compensación económica

**9. ¿Cómo se anonimiza un expediente de cliente antes de usarlo con IA?**
a) Borrando las páginas con datos sensibles
b) Sustituyendo nombre → CLIENTE_A, número de expediente → REF_X, importe → IMPORTE_X ✓
c) Poniendo el archivo en modo "privado" en Drive
d) Usando solo el resumen del caso, no el expediente completo

**10. Verdadero o falso: un banco FAQ bien construido elimina la necesidad de personalizar las respuestas antes de enviarlas.**
Respuesta: **Falso**. Las plantillas tienen campos variables en [CORCHETES] que siempre deben completarse. Además, algunos casos tienen elementos específicos que merecen una línea personalizada. Enviar una plantilla sin personalizar suena a plantilla y el cliente lo percibe.

**11. ¿Cuáles son los cuatro pasos del ciclo de mejora del banco FAQ?**
a) Crear, enviar, archivar, olvidar
b) Etiquetar el envío, revisar las respuestas que generaron segunda consulta, actualizar la plantilla, documentar el cambio ✓
c) Imprimir, distribuir, firmar, archivar
d) Aprobar, traducir, publicar, mantener

**12. ¿Cómo se le indica a la IA que adapte el tono al cliente sin perder profesionalidad?**
Respuesta abierta: Se le pide explícitamente: "Adapta el registro al tono del correo del cliente, manteniendo la profesionalidad pero sin sonar institucional." Si se quiere reforzar, se puede pegar un ejemplo del tono deseado en el prompt: "Aquí tienes una respuesta nuestra previa que nos parece bien: [PEGAR EJEMPLO]." La IA ajusta su estilo al ejemplo.

**13. ¿Qué es un "pago huérfano" en la atención al cliente? (concepto del flujo de cruce de tablas)**
a) Un pago duplicado del mismo cliente
b) Un pago recibido sin factura emitida que se le corresponda ✓
c) Una factura emitida sin pago
d) Un pago aprobado pero sin cobro efectivo

**14. ¿Cuál es la principal ventaja de etiquetar cada envío con la plantilla usada?**
a) Permite cobrar comisiones internas por uso de plantillas
b) Sirve para reportar al cliente qué plantilla se le envió
c) Permite revisar después qué plantillas funcionan mejor y mejorar el banco ✓
d) Es un requisito legal de protección de datos

**15. Verdadero o falso: si el cliente lleva 4 años con la empresa, conviene mencionarlo explícitamente en el Reconoce de una respuesta a una queja.**
Respuesta: **Verdadero**. Mencionar la relación de largo plazo en el Reconoce ("Después de cuatro años con nosotros, entiendo que esta situación te afecta especialmente") refuerza el sentido de continuidad de la relación y diferencia la respuesta de una plantilla genérica. La IA puede incorporarlo cuando se incluye en el prompt como dato del contexto.

---

## 15. PREGUNTAS FRECUENTES (FAQ)

**¿Puedo usar estas plantillas para responder internamente a compañeros de otros departamentos?**
Sí, adaptando el tono. Las consultas internas suelen tener un registro menos formal y más directo. El mismo banco FAQ puede tener una sección para comunicaciones externas (clientes, proveedores) y otra para comunicaciones internas, con el mismo contenido pero diferente formato.

**¿El banco FAQ sirve si mis consultas nunca son iguales?**
Aunque parezca que cada caso es único, suele haber patrones: el tipo de problema, el estado emocional del cliente, el nivel de urgencia. Las plantillas cubren esos patrones con campos variables que permiten personalizarlas. Si de verdad cada caso es tan único que ninguna plantilla aplica, probablemente necesitas un set de plantillas más específico para tu área.

**¿Qué hago si el cliente escribe en un idioma que no domino?**
La IA puede traducir el correo al español, analizarlo y generar la respuesta, y luego traducir la respuesta al idioma del cliente. ChatGPT y Gemini manejan bien la mayoría de idiomas europeos. Verifica siempre la traducción antes de enviar, especialmente en términos técnicos o frases de doble sentido.

**¿Puedo compartir el banco FAQ con mi equipo para que lo use toda la oficina?**
Sí, y es la recomendación. Un banco compartido en Google Drive garantiza que todos dan el mismo nivel de respuesta y el mismo tono. Si alguien del equipo añade una plantilla nueva, todos se benefician. La IA también puede ayudarte a generar la documentación de uso del banco para que sea fácil de incorporar para personas nuevas.

**¿Cómo sé si el tono de la respuesta generada es adecuado para mi organización?**
Ajusta el prompt inicial con ejemplos del tono que usa tu empresa: "El tono que usamos en nuestra empresa es profesional pero cercano, sin tecnicismos, con frases cortas. Aquí tienes un ejemplo de una respuesta que nos parece bien: [PEGAR EJEMPLO]." La IA ajusta su estilo al ejemplo proporcionado.

**¿Qué pasa si el cliente responde a la plantilla con algo que no cubre ninguna de mis respuestas tipo?**
Las plantillas cubren los casos frecuentes, no todos los casos. Para los casos atípicos, usa el flujo normal de prompt con contexto: describe la situación específica del cliente y pide a la IA una respuesta a medida. No intentes forzar una plantilla donde no encaja.

**¿Cómo enseño a un compañero a usar el banco FAQ que he construido?**
Documenta junto al banco una breve guía de uso: cuándo aplica cada plantilla, qué campos variables hay que completar siempre y qué tipo de casos requieren respuesta a medida en lugar de plantilla. La propia IA puede generar esa guía a partir del banco con un prompt: "Genera una guía de uso de 1 página para este banco de respuestas, dirigida a una persona nueva en el equipo."

**¿Qué hago si percibo que la respuesta generada suena demasiado fría o demasiado formal?**
Pide a la IA un ajuste de tono explícito: "Reescribe esta respuesta con un tono más cálido, manteniendo el contenido pero haciendo que el cliente sienta que hay una persona detrás del mensaje, no una plantilla." Si el problema persiste, pega un ejemplo del tono que usa tu empresa en otras comunicaciones para que la IA lo replique.

**¿El patrón RIA sirve también para situaciones internas (compañeros, jefes) y no solo para clientes externos?**
Sí, y de hecho funciona excepcionalmente bien internamente. Reconoce ("entiendo que necesitas el dato para hoy"), Informa ("estoy esperando confirmación de logística para validarlo") y Actúa ("te lo envío antes de las 14:00 con la confirmación o, si no llega, con la mejor estimación que tenga"). Es el mismo patrón con el mismo efecto: convierte una respuesta en una solución.

---

## 16. HERRAMIENTAS DE LA SESIÓN

- **ChatGPT** (chat.openai.com) — Generación de bancos FAQ en lote, adaptación multicanal, escalados; cuenta gratuita.
- **Google Gemini** (gemini.google.com) — Alternativa directa con cuenta Gmail; funciona igual para todos los prompts de la sesión.
- **Google Docs** (docs.google.com) — Para organizar y compartir el banco FAQ del equipo; gratis con Gmail.
- **Google NotebookLM** — Si se carga el banco FAQ como fuente, los compañeros pueden preguntarle "¿qué respondemos cuando un cliente pregunta X?" y obtener la respuesta del banco sin buscar en el documento.

Ver `Recursos/Herramientas_Gratuitas.md` para referencia completa.

---

## 17. MINI-ENTREGABLE DEL DÍA

**Nombre:** Banco de respuestas FAQ + guiones de situaciones difíciles
**Formato:** Google Doc
**Contenido:** 5 plantillas de respuesta para las consultas más frecuentes del puesto propio (con campos en [CORCHETES]) + 3 guiones para situaciones difíciles (queja, urgencia, escalado), incluyendo la versión de correo, Teams y teléfono de al menos una de ellas.
**Cómo alimenta el proyecto final:** Si el proyecto final del alumno está relacionado con atención al cliente, el banco de hoy puede ser el entregable principal del proyecto de D16–D17.

---

## 18. 🎓 HILO DEL PROYECTO FINAL

Para tu proyecto final: si tu solución implica atención a consultas (de clientes, proveedores, compañeros o ciudadanos), el banco de respuestas y los guiones de hoy son exactamente el tipo de entregable que puedes construir, documentar y presentar en D16–D17.

---

## 19. MENSAJE CLAVE DE LA SESIÓN

> "La atención al cliente no es solo resolver problemas: es hacerlo de forma que la persona sienta que hay alguien que le escucha. La IA puede ayudarte con las palabras correctas; tú aportas el criterio para saber cuándo las palabras no son suficientes."

---

## 20. IDEAS PARA RECORDAR

- Anonimiza siempre los datos del cliente antes de usar cualquier IA: nombre → CLIENTE_A, expediente → REF_X.
- Un banco de 5 respuestas tipo bien construido cubre el 70-80 % de tus consultas frecuentes.
- El patrón RIA (Reconoce específicamente / Informa con claridad / Actúa con plazo concreto) transforma una respuesta defensiva en una que mantiene la relación.
- La misma respuesta necesita tres formatos distintos: correo formal, Teams/WhatsApp en 3 líneas, guion de teléfono.
- Saber cuándo NO usar IA es tan importante como saber usarla: hay situaciones que requieren respuesta humana genuina.
- El banco FAQ es un sistema vivo: etiqueta cada envío, revisa semanalmente y actualiza las plantillas según la experiencia real de uso.
- El patrón RIA funciona también con compañeros y jefes, no solo con clientes externos: convierte cualquier respuesta en una solución con plazo.

---

## 21. CONEXIÓN CON EL RESTO DEL CURSO

Esta sesión cierra el Módulo 7 (Flujos de trabajo y documentación) y es la penúltima antes del proyecto final. El patrón RIA profundiza lo aprendido en D06 (correos profesionales) con situaciones más complejas. El banco FAQ complementa los SOPs de D14: los SOPs documentan los procesos internos; el banco FAQ documenta las respuestas externas. En **D16** (mañana), cada alumno construye su proyecto final integrando todo lo aprendido en M2–M7; quienes tienen roles de atención al cliente encontrarán en el banco FAQ de hoy el punto de partida natural de su proyecto.

---

## 22. FOOTER

*Brief para NotebookLM · D15 · Edición 01/26 — IA en la Oficina*
