# BRIEF PARA NOTEBOOKLM — D02
## Módulo 2, Sesión 1: Prompts básicos — La estructura que lo cambia todo
## Curso: IA en la Oficina – Eficiencia y Productividad
## Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital

**Fecha:** Jueves 2 de julio de 2026 · 15:00–19:00 h · Día 2 de 17

---

## 2. CONTEXTO DEL CURSO

**Programa:** IA en la Oficina – Eficiencia y Productividad (68 horas · 17 sesiones de 4 horas)
**Público:** Personal administrativo y de oficina sin experiencia previa en IA generativa. Perfiles muy diversos: administración, atención al cliente, contabilidad, logística, recursos humanos.
**Metodología:** ~40 % teoría y demostración · ~50 % práctica guiada · ~10 % puesta en común
**Evaluación:** Mini-entregable al final de cada sesión + Proyecto Final individual (D16–D17)
**Sesión anterior (D01):** El grupo ya conoce qué es la IA generativa, tiene cuenta en ChatGPT y ha creado su mapa personal de 5 tareas candidatas a automatizar.

> *Este documento es la fuente del notebook de hoy. Además de las diapositivas, puedes pedirle a NotebookLM un resumen en **audio** (tipo pódcast), un **vídeo**, una **infografía** o mapa mental, una **guía de estudio**, **fichas** (flashcards), un **cuestionario** para autoevaluarte, o **escribir tus preguntas en el chat**. Usa el formato con el que mejor aprendas. No escribas datos personales reales en el chat.*

---

## 3. RESUMEN DE LA SESIÓN

Ayer descubrimos qué es la IA y para qué sirve; hoy aprendemos a hablar con ella de forma que nos dé resultados realmente útiles. La mayoría de las personas que prueban la IA por primera vez se frustran porque los resultados son genéricos o inservibles, y la razón casi siempre es la misma: el prompt era demasiado vago. Esta sesión enseña a diagnosticar por qué fallan los prompts y a corregirlos aplicando la estructura R-C-T-F-R (Rol, Contexto, Tarea, Formato, Restricciones), que convierte cualquier instrucción imprecisa en una orden profesional y reproducible. Los alumnos saldrán del día con cinco prompts propios, escritos con estructura, probados en ChatGPT y ajustados al trabajo real de su puesto, formando la primera pieza del proyecto final del curso.

---

## 4. ESTRUCTURA DE LA SESIÓN (240 min)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| Apertura | 15 min | Repaso D01 + preguntas del grupo + objetivos del día |
| Teórico-demostrativo | 75 min | Por qué fallan los prompts · Estructura R-C-T-F-R · Comparativa bueno/malo · Plantillas reutilizables |
| Descanso | 15 min | — |
| Práctica guiada | 95 min | Taller individual: mis 5 prompts (55 min) + revisión cruzada en parejas (30 min) + puesta en común mini-concurso (10 min) |
| Puesta en común | 40 min | Presentación del mejor prompt de cada pareja + reflexión colectiva + mini-entregable |

*(15+75+15+95+40 = 240 min)*

---

## 5. OBJETIVOS DE APRENDIZAJE

1. Reconocer por qué un prompt vago da resultados pobres y uno estructurado da resultados profesionales y reproducibles.
2. Aplicar la estructura R-C-T-F-R (Rol, Contexto, Tarea, Formato, Restricciones) a cualquier tarea de oficina.
3. Reescribir un prompt malo convirtiéndolo en uno eficaz usando los cinco componentes.
4. Construir una colección personal de plantillas de prompt reutilizables para las tareas más habituales del propio puesto.

---

## 6. DESARROLLO TEÓRICO

### Por qué fallan los prompts: los cinco errores del principiante

Marta lleva ocho años gestionando la administración de una empresa de distribución mediana. Ayer, en D01, probó su primer prompt y comprobó que la IA podía borrar un correo en cuestión de segundos. Esta mañana llega al aula con energía, abre ChatGPT y escribe: "Redacta un correo para mi proveedor". El resultado le decepciona: genérico, sin contexto, lleno de frases vacías como "esperamos su respuesta". "¿Para esto sirve esto?", piensa. El problema no es la herramienta. El problema es el prompt.

Este es el error más universal de las personas que empiezan con la IA: escriben como si la herramienta les conociera, supieran lo que necesitan y fueran capaces de adivinarlo. La realidad es la contraria. La IA no sabe quién eres, dónde trabajas, a quién le escribes ni qué resultado esperas. Es como contratar a alguien nuevo en la empresa y, el primer día, decirle "haz un informe" sin explicarle nada más. El empleado haría algo, pero casi con certeza no sería lo que necesitabas.

Los cinco errores más frecuentes que observamos en principiantes son los siguientes. El primero es el **prompt demasiado vago**: "Redacta un correo", "Haz un resumen", "Ayúdame con esto". La IA no tiene información suficiente para producir algo útil y genera una respuesta que podría ser de cualquier empresa del mundo, sin que sea útil para la tuya. El segundo error es la **falta de contexto**: la IA no conoce tu sector, tu empresa, tu cliente ni el historial de esa conversación concreta. Sin esa información, el resultado es genérico por definición. El tercer error es **pedir todo a la vez**: un prompt que incluye cinco tareas distintas rara vez resuelve bien ninguna de ellas; la IA intenta satisfacer todas las peticiones y termina haciendo un ejercicio de compromiso que no sirve para nada en concreto. El cuarto error es **no indicar el formato**: si no dices si quieres una lista, un correo, una tabla o un párrafo, la IA elegirá el formato más probable según el contexto, que puede no coincidir con lo que necesitas. El quinto error es **no incluir restricciones**: sin decirle qué no debe hacer, la IA puede divagar, añadir información inventada, extenderse más de lo necesario o asumir cosas que tú no quieres que asuma.

La solución a los cinco errores no es saber más de tecnología. Es aplicar una estructura. Y esa estructura tiene nombre: R-C-T-F-R.

---

### La estructura R-C-T-F-R: los cinco componentes de un prompt eficaz

La estructura R-C-T-F-R es un marco de cinco componentes que, cuando se aplican juntos, transforman cualquier instrucción vaga en una orden precisa y reproducible. No hace falta usar los cinco en todo momento —en prompts sencillos bastará con dos o tres—, pero conocerlos todos permite construir prompts profesionales para cualquier situación.

| Letra | Componente | Qué indica a la IA | Ejemplo práctico |
|-------|------------|--------------------|-----------------|
| **R** | Rol | Qué papel o perspectiva debe adoptar | "Actúa como redactora de comunicaciones corporativas" |
| **C** | Contexto | La situación, información de fondo o datos relevantes | "Somos una empresa de logística; un cliente reclama un retraso de 3 días en su pedido" |
| **T** | Tarea | Qué tiene que hacer exactamente, de forma concreta | "Redacta un correo de respuesta que reconozca el problema y ofrezca disculpas" |
| **F** | Formato | Cómo quieres que sea la respuesta | "Correo con asunto, saludo, cuerpo y despedida; máximo 120 palabras" |
| **R** | Restricciones | Qué debe evitar o qué límites debe respetar | "No prometas fechas concretas ni ofrezcas compensaciones económicas" |

Volvamos a Marta. En lugar de "redacta un correo para mi proveedor", ahora escribe:

> "Actúa como administrativa de una empresa de distribución. Nuestro proveedor PROVEEDOR_X nos ha enviado hoy un correo preguntando en qué estado está la factura REF_001 que emitió hace quince días. Redacta una respuesta cordial y formal que le confirme que hemos recibido la factura y que el plazo de pago habitual es de 30 días desde la recepción. Formato: correo con asunto, saludo, cuerpo y despedida, máximo 80 palabras. No incluyas plazos de pago distintos a 30 días ni ofrezcas adelantar el pago."

El resultado esta vez es diferente: un correo con asunto propio, saludo personalizable, cuerpo concreto y despedida apropiada. Marta solo tiene que revisar que los datos de la plantilla sean correctos, ajustar el nombre del proveedor y enviarlo. Ha pasado de 15 minutos a 90 segundos.

El componente más olvidado por los principiantes es el **Rol**. Darle a la IA un papel concreto ajusta automáticamente el tono, el vocabulario y el enfoque de la respuesta. Una misma tarea —redactar un correo sobre una reclamación— dará resultados muy distintos si el rol es "responsable de atención al cliente", "abogado corporativo" o "jefa de administración". El rol no necesita ser largo: basta con una frase breve que sitúe a la IA en el contexto adecuado.

El componente más subestimado es el **Contexto**. La IA trabaja con lo que le das. Si pegas el correo original del cliente en el prompt (siempre anonimizado), la respuesta estará anclada a esa situación concreta. Si no pegas nada, la IA construye una situación imaginaria que puede parecerse o no a la tuya. El contexto es lo que convierte una respuesta genérica en una respuesta que parece escrita por alguien que conoce el caso.

El componente más práctico son las **Restricciones**. La IA tiende a ser educada, a dar más información de la que pediste y a añadir matices. Las restricciones son el modo de podarla: "no más de 80 palabras", "no menciones el precio", "no uses lenguaje técnico", "no empieces con 'Estimado cliente'". Unos segundos dedicados a pensar qué no quieres en la respuesta ahorran varias iteraciones posteriores.

---

### El "cinco de cinco": de prompts vagos a prompts con R-C-T-F-R

La siguiente tabla muestra cinco situaciones habituales de oficina y cómo cambia la calidad del resultado al pasar de un prompt vago a uno estructurado. Estos son exactamente los tipos de prompts que los alumnos van a construir en la práctica de hoy.

| Prompt vago ❌ | Prompt R-C-T-F-R ✅ |
|---------------|---------------------|
| "Escribe un correo" | "Actúa como administrativa de RRHH. Un empleado lleva 3 días sin justificar su ausencia. Redacta un correo formal recordándole que debe entregar el justificante antes del viernes. Máximo 80 palabras. Sin amenazas ni tono agresivo." |
| "Resume esto" | "Actúa como asistente administrativo. Resume el siguiente informe en 5 puntos clave para presentarlo en reunión de dirección de 5 minutos. Usa lenguaje no técnico. [PEGAR TEXTO ANONIMIZADO]" |
| "Haz una lista de tareas" | "Crea 8 tareas prioritarias para el cierre contable de fin de mes de una empresa de distribución mediana. Ordénalas por urgencia. Lista numerada, una línea por tarea, verbo al inicio de cada línea." |
| "Responde a esta queja" | "Actúa como responsable de atención al cliente. El cliente CLIENTE_A dice que le cobramos dos veces el mismo servicio. Redacta una respuesta empática que confirme que investigaremos el caso en 48 horas. Máximo 100 palabras. No reconozcas el error hasta confirmar los datos." |
| "Traduce esto al inglés" | "Traduce al inglés formal (registro empresarial). Mantén exactamente el mismo tono y extensión del original. No añadas ni quites información. [PEGAR TEXTO]" |

---

### Plantillas reutilizables para las tareas más frecuentes

Una vez que dominas R-C-T-F-R, el siguiente paso es convertir los prompts que funcionan en plantillas que puedas reusar sin pensar. La idea es sencilla: donde el prompt tiene información variable, pones un placeholder entre corchetes. Cuando necesites usar la plantilla, solo tienes que rellenar los huecos.

**Plantilla para correo profesional:**
> "Actúa como [ROL]. [CONTEXTO]. Redacta un correo [formal/informal] para [DESTINATARIO] sobre [TEMA]. Máximo [X] palabras. Tono: [directo/empático/formal]. No incluyas [RESTRICCIÓN]."

**Plantilla para resumen ejecutivo:**
> "Actúa como asistente administrativo. Resume el siguiente texto en [X] puntos clave, usando lenguaje claro y directo para [TIPO DE DESTINATARIO]. Incluye solo información del texto; no añadas datos externos. [PEGAR TEXTO ANONIMIZADO]"

**Plantilla para borrador rápido:**
> "Actúa como [ROL]. Necesito un borrador de [TIPO DE DOCUMENTO] sobre [TEMA]. Estructura: [SECCIONES]. Tono: [formal/divulgativo]. Extensión aproximada: [X palabras]. No incluyas [RESTRICCIÓN]."

**Plantilla para adaptar comunicado a distintos destinatarios:**
> "Tienes este comunicado: [PEGAR TEXTO]. Adapta la versión para [NUEVO DESTINATARIO], manteniendo el contenido esencial pero ajustando el tono y el vocabulario. Máximo [X] palabras."

Marta guarda estas cuatro plantillas en un documento de Google Docs llamado "Mis prompts de trabajo". Cada vez que necesita redactar un correo, no empieza desde cero: abre el documento, elige la plantilla, rellena los corchetes y en treinta segundos tiene el prompt listo para lanzar.

---

## 7. DATOS Y CIFRAS CLAVE

- Redactar un correo estándar desde cero suele costar entre 10 y 20 minutos a un perfil administrativo; con un prompt bien estructurado, el borrador se genera en menos de 2 minutos (ahorro del 85-90 %).
- El 60-70 % del tiempo de un perfil administrativo se dedica a tareas que siguen un patrón repetitivo: correos tipo, informes periódicos, actas, resúmenes.
- Antes / Después — redactar una respuesta estándar a consulta de proveedor: antes 15 min; con R-C-T-F-R 1-2 min.
- Antes / Después — generar el primer borrador de un comunicado interno: antes 30 min; con R-C-T-F-R 3-5 min.
- Antes / Después — crear 5 respuestas tipo para preguntas frecuentes: antes 90 min; con un único prompt en lote 5-8 min.
- Los usuarios principiantes necesitan una media de 3-5 iteraciones para obtener un resultado satisfactorio con un prompt vago; con R-C-T-F-R, el primer resultado es usable en el 70-80 % de los casos.
- En un estudio de McKinsey (2023), los trabajadores del conocimiento que usaban herramientas de IA generativa completaban tareas de escritura hasta un 40 % más rápido que quienes no las usaban.

---

## 8. EJEMPLOS RESUELTOS PASO A PASO

### Caso 1 — De prompt vago a prompt eficaz: correo de reclamación

**Situación:** Marta necesita responder a un cliente que ha recibido un pedido incompleto. Su primer intento de prompt fue: "Responde a la queja de un cliente por un pedido incompleto." El resultado fue un texto genérico y algo frío.

**Prompt mejorado con R-C-T-F-R:**
> "Actúa como responsable de atención al cliente de una empresa de distribución. El cliente CLIENTE_B ha recibido el pedido REF_002 pero faltan 2 de los 10 artículos solicitados. Redacta un correo de respuesta que: (1) reconozca el error, (2) confirme que los artículos faltantes se enviarán en 48 horas, (3) ofrezca disculpas. Formato: correo formal con asunto, saludo, cuerpo (máximo 120 palabras) y despedida. No ofrezcas descuentos ni compensaciones económicas."

**Resultado comentado:** La IA genera un correo con asunto descriptivo, reconocimiento concreto del error y compromiso de entrega en 48 horas, sin añadir promesas que Marta no puede cumplir. El resultado es directamente usable: basta con sustituir CLIENTE_B por el nombre real y ajustar la referencia.

**Cómo iterarlo:** Si el tono resulta demasiado frío, Marta añade: *"Reescribe con un tono algo más cálido. El cliente es habitual y queremos retenerle."* Si le parece demasiado larga la respuesta: *"Reduce a 80 palabras manteniendo los tres puntos clave."*

---

### Caso 2 — Generar un banco de respuestas tipo en un solo prompt

**Situación:** El departamento recibe cada mes las mismas cinco preguntas de proveedores distintos. En lugar de escribir cada respuesta por separado, Marta quiere generar las cinco de golpe.

**Prompt exacto:**
> "Actúa como administrativa de una empresa de distribución. Genera 5 respuestas tipo para las siguientes situaciones frecuentes: (1) proveedor que pregunta el estado de su factura; (2) proveedor que solicita cambiar los datos bancarios; (3) proveedor que avisa de un retraso en su entrega; (4) proveedor que solicita una reunión para revisar condiciones; (5) proveedor que reclama un pago no recibido. Cada respuesta: tono formal y cordial, máximo 80 palabras, con huecos [NOMBRE_PROVEEDOR] y [REFERENCIA] donde sea necesario. Sin promesas de pago ni plazos concretos salvo el estándar de 30 días."

**Resultado comentado:** En menos de dos minutos, Marta tiene un banco de cinco respuestas listo para guardar como plantillas. Cada una tiene la estructura correcta y los huecos marcados. A partir de este momento, responder a un proveedor le llevará menos de un minuto.

**Cómo iterarlo:** Si alguna de las respuestas no tiene exactamente el tono deseado: *"La respuesta número 3 está bien, pero la empresa tiene una política de comunicar los retrasos de proveedor solo a logística, no al cliente. Reformúlala para que sea una respuesta interna, no al cliente."*

---

### Caso 3 — Reescribir un correo recibido en tono más profesional

**Situación:** Un compañero de Marta ha redactado un correo a un cliente nuevo que tiene un tono demasiado informal para la imagen de la empresa. Marta quiere mejorar el tono sin reescribirlo desde cero.

**Prompt exacto:**
> "Actúa como correctora de estilo corporativo. Te paso un correo que un compañero ha redactado. Tu tarea es reescribirlo con un tono más formal y profesional, manteniendo exactamente el mismo contenido e información. No añadas ni elimines información. Formato: correo formal con asunto, saludo, cuerpo y despedida. Máximo la misma extensión que el original. Correo original: [INICIO] Hola CLIENTE_C, te mando los datos que me pediste. Ya sabes que si necesitas algo más me dices. Hasta luego. [FIN]"

**Resultado comentado:** La IA mantiene la información (envío de datos, ofrecimiento de ayuda) pero transforma el tono: saludo formal, verbo en tercera persona, despedida apropiada. Marta revisa que no haya añadido compromisos que no estaban en el original y lo pasa al compañero.

**Cómo iterarlo:** *"Mantén el mismo tono formal pero añade una frase al inicio que agradezca al cliente haberse puesto en contacto."*

---

## 9. GLOSARIO

**Prompt:** Instrucción o pregunta que escribes a la IA para que genere un resultado; la calidad del prompt determina directamente la calidad de la respuesta.

**Estructura R-C-T-F-R:** Marco de cinco componentes (Rol, Contexto, Tarea, Formato, Restricciones) que convierte un prompt vago en una instrucción precisa y reproducible.

**Rol:** Primer componente de R-C-T-F-R; indica a la IA qué papel o perspectiva debe adoptar para generar la respuesta (p. ej., "actúa como responsable de atención al cliente").

**Contexto:** Segundo componente; la información de fondo que la IA necesita para que la respuesta sea específica a tu situación real, no genérica.

**Restricciones:** Quinto componente; las instrucciones sobre qué no debe hacer la IA, qué límites debe respetar o qué información no debe incluir.

**Placeholder:** Marcador de posición en una plantilla de prompt, escrito entre corchetes (p. ej., [NOMBRE_PROVEEDOR]), que se sustituye por el dato real en cada uso.

**Plantilla de prompt:** Prompt con los elementos fijos ya redactados y los elementos variables marcados como placeholders, diseñado para reutilizarse en situaciones similares.

**Iteración:** Prompt adicional que pide a la IA que mejore, ajuste o corrija la respuesta anterior sin empezar desde cero; es la técnica clave para afinar resultados rápidamente.

**Alucinación:** Error específico de la IA: afirmar datos incorrectos con total confianza; siempre hay que verificar nombres, cifras y referencias normativas antes de usar el resultado.

**Anonimización:** Sustitución de datos personales o confidenciales por etiquetas genéricas (CLIENTE_A, IMPORTE_X) antes de pegarlos en cualquier herramienta de IA externa.

---

## 10. ERRORES COMUNES Y BUENAS PRÁCTICAS

**Error 1 — Prompt de una sola línea sin contexto.** "Escribe un correo de queja" puede generar algo, pero nunca algo usable directamente en tu empresa. La solución: antes de escribir el prompt, dedica 20 segundos a responder internamente: ¿quién soy yo en este contexto? ¿qué situación ha ocurrido? ¿a quién va dirigido? ¿qué quiero conseguir?

**Error 2 — Omitir el Formato y llevarse sorpresas.** Sin indicar formato, la IA puede dar una respuesta como ensayo, lista o tabla según le parezca. Si necesitas un correo con asunto y despedida, pídelo explícitamente. Si necesitas una lista numerada, dilo. Treinta segundos extra en el prompt ahorran varias iteraciones.

**Error 3 — Pegar datos personales reales.** Aunque resulta tentador copiar y pegar el correo del cliente tal cual, los nombres reales, números de expediente, datos bancarios o de RRHH no deben salir de la organización sin anonimizar. Practica la sustitución por etiquetas desde hoy: CLIENTE_A, IMPORTE_X, REF_001.

**Error 4 — Aceptar el primer resultado sin revisar.** La IA puede afirmar cosas incorrectas con total confianza. Cualquier dato concreto —plazo de pago, referencia legal, cifra— debe verificarse antes de enviar el resultado. El flujo correcto siempre es: generar → revisar → usar (o iterar si es necesario).

**Error 5 — Pedir cinco cosas distintas en un solo prompt.** Un prompt que pide redactar un correo, resumir un informe, hacer una lista de tareas y traducirlo todo al inglés rara vez hace bien ninguna de las cuatro. Divide las tareas y usa un prompt para cada una.

**Buena práctica — Guarda los prompts que funcionan.** Cuando obtengas un resultado que te guste, guarda el prompt en un documento personal. Esa colección es tu biblioteca privada de prompts y se convierte en una de las herramientas más valiosas de tu día a día.

**Buena práctica — Etiqueta tus restricciones de privacidad.** Cada vez que uses un prompt con datos de la empresa, añade mentalmente la pregunta: ¿hay algún dato aquí que no debería salir de la organización? Si la respuesta es sí, anonimiza antes de pegar.

---

## 11. ACTIVIDADES EN AULA

### Actividad 1 — Demostración en vivo: de prompt vago a R-C-T-F-R [Grupo · 15 min]

**Descripción:** El formador recoge 3 prompts vagos reales del grupo —a partir del mapa de tareas construido en D01— y los convierte en prompts R-C-T-F-R en directo, mostrando en pantalla la diferencia de resultados en ChatGPT. El grupo debate qué componente marca más la diferencia en cada caso.

**Objetivo:** Que el alumno vea en tiempo real cómo cambia el resultado al añadir cada componente; anclar la teoría a situaciones reconocibles antes de la práctica individual.

**Material:** Proyector, ChatGPT abierto en pantalla. Prompts vagos recogidos de los mapas de oportunidades de D01.

---

### Actividad 2 — Taller individual: mis 5 prompts profesionales [Individual · 55 min]

**Descripción:** Cada alumno elige 5 tareas de su mapa de oportunidades (creado en D01) y escribe un prompt R-C-T-F-R completo para cada una. Los prueba en ChatGPT y anota en su hoja de trabajo: el prompt escrito, el resultado obtenido y una valoración breve (¿es directamente usable? ¿qué cambiarías?). Si algún resultado no es satisfactorio, el alumno practica la iteración antes de pasar al siguiente.

**Objetivo:** Pasar de la teoría a la práctica real en el contexto del propio puesto; producir el mini-entregable del día.

**Material:** Ordenador con ChatGPT, plantilla "Mis 5 prompts profesionales" (Google Doc o papel).

---

### Actividad 3 — Revisión cruzada en parejas [Pareja · 25 min]

**Descripción:** Cada persona intercambia su hoja de los 5 prompts con un/a compañero/a. El revisor lee los prompts del otro e indica para cada uno: (a) qué componente R-C-T-F-R falta o es débil, y (b) una sugerencia concreta de mejora. Después se devuelven las hojas y cada alumno aplica al menos una mejora de las sugeridas. Los últimos 5 minutos de la actividad: cada pareja elige su "mejor prompt del día" para compartir en la puesta en común.

**Objetivo:** Practicar la mirada crítica sobre prompts ajenos (que luego se aplica a los propios); mejorar los prompts con perspectiva externa.

**Material:** Las mismas hojas de trabajo de la Actividad 2.

---

## 12. 🔁 TRABAJO EN PAREJAS

La **Actividad 3** es el núcleo colaborativo de la sesión. Las parejas se forman por afinidad de puesto o de sector cuando es posible (dos personas de logística, dos de atención al cliente, etc.), lo que enriquece el intercambio porque los contextos son similares y el revisor puede juzgar mejor si el prompt es realista para ese tipo de tarea. Cada persona actúa alternativamente como autora y como revisora, practicando así dos habilidades complementarias: construir prompts propios y detectar qué falla en los de otro. Lo que produce la pareja —el "mejor prompt del día"— es la pieza que llevan a la puesta en común final, donde el grupo compara los distintos enfoques y el formador destaca qué hace especialmente bueno a cada uno.

---

## 13. EJERCICIOS SUGERIDOS

Ver Banco de Ejercicios:
- **EJ-D02-1** (Individual): Reescribir 3 prompts vagos del banco de ejercicios aplicando R-C-T-F-R completo
- **EJ-D02-2** (Pareja): Intercambiar los 5 prompts profesionales y aplicar la revisión cruzada con rúbrica R-C-T-F-R
- **EJ-D02-3** (Grupo): Mini-concurso del mejor prompt: cada persona propone su mejor resultado del día y el grupo vota el más útil; el formador explica los criterios de calidad

---

## 14. CUESTIONARIO DE AUTOEVALUACIÓN

**1. ¿Qué significa la "R" de Rol en la estructura R-C-T-F-R?**
a) La respuesta que esperas de la IA
b) El papel o perspectiva que le pides a la IA que adopte ✓
c) La restricción principal del prompt
d) El resultado final del prompt

**2. ¿Por qué un prompt vago da resultados poco útiles?**
a) Porque la IA gratuita tiene menos capacidad
b) Porque la IA no tiene información suficiente sobre tu situación específica ✓
c) Porque la IA no entiende el español bien
d) Porque los prompts cortos no funcionan en ChatGPT

**3. Tienes el siguiente prompt: "Redacta un correo para un proveedor." ¿Qué componente R-C-T-F-R falta principalmente?**
a) Tarea
b) Rol, Contexto, Formato y Restricciones ✓
c) Solo el Formato
d) Solo las Restricciones

**4. ¿Qué es un placeholder en una plantilla de prompt?**
a) Un error en el prompt
b) La respuesta que genera la IA
c) Un marcador de posición entre corchetes que se sustituye por datos reales al usar la plantilla ✓
d) El título del documento donde guardas los prompts

**5. Marta quiere pegar el correo de un cliente en ChatGPT para que la IA le ayude a responder. ¿Qué debe hacer antes de pegar el texto?**
a) Traducirlo al inglés
b) Anonimizar los datos personales del cliente ✓
c) Copiar el correo completo sin cambios para que la IA tenga toda la información
d) Acortar el texto a menos de 50 palabras

**6. ¿Qué componente de R-C-T-F-R le dice a la IA qué NO debe incluir en su respuesta?**
a) Contexto
b) Formato
c) Restricciones ✓
d) Rol

**7. Después de lanzar un prompt y recibir una respuesta demasiado larga, ¿cuál es la forma más eficiente de acortarla?**
a) Empezar desde cero con un prompt completamente nuevo
b) Pedir a la IA: "Reduce esta respuesta a la mitad manteniendo los puntos clave" ✓
c) Cortar el texto manualmente
d) Usar otra herramienta de IA

**8. ¿Cuál de los siguientes es un prompt completo con estructura R-C-T-F-R?**
a) "Escribe un correo a un cliente"
b) "Actúa como responsable de atención al cliente de una empresa de logística. Un cliente reclama que su pedido llegó roto. Redacta una respuesta empática que confirme que investigamos el caso. Formato: correo formal, máximo 100 palabras. Sin ofrecer reembolso." ✓
c) "ChatGPT, necesito tu ayuda con un correo importante"
d) "Resume este informe y también tradúcelo al inglés y hazlo más formal"

**9. ¿Por qué conviene guardar los prompts que funcionan bien?**
Respuesta: Porque se convierten en plantillas reutilizables. Un prompt que ha dado un buen resultado en una situación puede usarse de nuevo en situaciones similares, simplemente cambiando los placeholders. Con el tiempo, esa colección de prompts es uno de los recursos más valiosos del puesto de trabajo.

**10. ¿Cuál de los siguientes prompts es más eficaz para generar respuestas a preguntas frecuentes?**
a) "Responde a estas preguntas una por una"
b) "Actúa como administrativa de una empresa de distribución. Genera 5 respuestas tipo para estas consultas frecuentes de proveedores: [LISTA]. Cada respuesta: tono formal, máximo 80 palabras, con [NOMBRE_PROVEEDOR] donde sea necesario." ✓
c) "Haz un banco de respuestas"
d) "Escribe respuestas para proveedores"

**11. ¿Qué error comete alguien que escribe el siguiente prompt: "Haz un resumen, una lista de tareas, un borrador de correo y una traducción al inglés"?**
Respuesta: Está pidiendo cuatro tareas distintas en un solo prompt. Esto rara vez produce buenos resultados en ninguna de las cuatro. La solución es dividir las tareas y usar un prompt separado para cada una, o al menos agrupar las que tienen el mismo propósito.

**12. ¿Es suficiente con revisar solo la primera frase del resultado de la IA antes de enviarlo?**
a) Sí, si el principio está bien el resto también lo estará
b) No; siempre hay que leer el resultado completo, verificar los datos concretos y asegurarse de que no hay información incorrecta antes de usarlo ✓
c) Solo hay que revisar si el documento es muy largo
d) No hace falta revisar si la IA es de pago

---

## 15. PREGUNTAS FRECUENTES (FAQ)

**¿Tengo que usar los cinco componentes de R-C-T-F-R en todos los prompts?**
No siempre. En tareas sencillas pueden bastar dos o tres componentes. La regla práctica: si el resultado que obtienes no es lo suficientemente específico para tu situación, añade el componente que falta. Cuantos más componentes incluyas, más controlado y predecible será el resultado. Para tareas importantes o recurrentes, usa los cinco.

**¿Puedo mezclar idiomas en el prompt (escribir parte en español y parte en inglés)?**
Escribe siempre en el idioma en que quieres la respuesta. Si quieres la respuesta en español, escribe el prompt en español. La IA entiende perfectamente el español y no produce mejores resultados por escribirle en inglés. Eso es un mito habitual que no tiene base real.

**¿Qué pasa si no sé exactamente qué rol ponerle a la IA?**
Puedes omitirlo o usar un rol genérico como "actúa como asistente administrativo profesional". La IA adaptará su respuesta. El rol importa más cuando necesitas un registro muy específico: legal, médico, comercial formal. Para tareas de oficina habituales, un rol genérico ya mejora mucho el resultado.

**¿Cuánto contexto debo dar? ¿Es peligroso dar demasiado?**
Más contexto suele dar mejores resultados, pero siempre anonimizado. No existe un límite de "demasiado contexto" en términos de calidad, aunque sí existe un límite técnico de longitud en cada herramienta (la ventana de contexto). Regla práctica: incluye toda la información relevante, pero nunca datos personales reales.

**¿Puedo usar estas plantillas en Gemini o Claude, o solo funcionan en ChatGPT?**
Las plantillas basadas en R-C-T-F-R funcionan en cualquier herramienta de IA generativa: ChatGPT, Gemini, Claude o cualquier otra. La estructura es independiente de la herramienta. Lo que puede variar es el estilo o la extensión de la respuesta, pero el prompt es directamente portable.

**¿La IA recuerda los prompts que le he dado en sesiones anteriores?**
No automáticamente. Cada conversación nueva empieza desde cero. Por eso es tan importante guardar los prompts que funcionan en tu propio documento. Si abres una nueva conversación, tendrás que volver a proporcionar el contexto y las instrucciones desde el principio.

**El resultado tiene información que no pedí y que no necesito. ¿Cómo lo evito?**
Añade restricciones más específicas: "no incluyas introducción", "responde solo con la lista, sin explicaciones adicionales", "no añadas más información de la que está en el texto que te he dado". Las restricciones son el componente más eficaz para eliminar el ruido de las respuestas.

**¿Puedo pedir a la IA que me ayude a construir el prompt en sí?**
Sí, es una técnica muy útil cuando no sabes por dónde empezar. Puedes escribir: "Necesito construir un prompt para [DESCRIBIR LA TAREA]. Ayúdame a formularlo con estructura R-C-T-F-R." La IA te propondrá un borrador de prompt que tú puedes ajustar. Es una forma excelente de aprender la estructura practicándola.

---

## 16. HERRAMIENTAS DE LA SESIÓN

- **ChatGPT** (chatgpt.com) — La herramienta principal del día. Cuenta gratuita con email o cuenta Google, creada en D01. Suficiente para todas las actividades del día.
- **Google Gemini** (gemini.google.com) — Alternativa inmediata accesible con la cuenta Gmail del alumno. Todas las plantillas y prompts de hoy funcionan igual en Gemini.
- **Google NotebookLM** (notebooklm.google.com) — El formador comparte el enlace del notebook del día; los alumnos pueden usarlo para repasar la teoría, generar fichas o cuestionarios sobre R-C-T-F-R, o hacer preguntas al chat.
- **Google Docs** — Para guardar la plantilla "Mis 5 prompts profesionales" y la biblioteca personal de prompts.

Ver el mapa completo de herramientas en `Recursos/Herramientas_Gratuitas.md`.

---

## 17. MINI-ENTREGABLE DEL DÍA

**Nombre:** Mis 5 prompts profesionales
**Formato:** Documento Google Docs o plantilla en papel
**Contenido:** 5 prompts escritos con estructura R-C-T-F-R, cada uno referido a una tarea real del puesto del alumno, con el resultado obtenido en ChatGPT anotado junto al prompt y una valoración breve de si el resultado fue directamente usable o requirió iteración.
**Cómo alimenta el proyecto final:** Estos 5 prompts son la primera capa del proyecto final. En sesiones posteriores el alumno los refinará, los organizará en flujos encadenados (D03) y los vinculará a herramientas específicas (D04-D09), hasta que en D16-D17 presente un flujo de trabajo completo automatizado con IA.

---

## 18. 🎓 HILO DEL PROYECTO FINAL

Para tu proyecto final: los 5 prompts que construyes hoy son la materia prima del proyecto. En D03 aprenderás a encadenarlos en flujos; en D04-D09 los enriquecerás con herramientas especializadas. Guarda el documento de hoy: lo necesitarás en D09 para elegir tu caso de proyecto.

---

## 19. MENSAJE CLAVE DE LA SESIÓN

> "Un buen prompt no es talento, es técnica. Con la estructura R-C-T-F-R cualquier persona obtiene resultados profesionales desde el primer día. La diferencia entre un resultado mediocre y uno excelente no está en la herramienta: está en la instrucción."

---

## 20. IDEAS PARA RECORDAR

- R-C-T-F-R (Rol, Contexto, Tarea, Formato, Restricciones) es la estructura que convierte un prompt vago en una instrucción profesional y reproducible.
- Más contexto siempre es mejor que menos, siempre que los datos estén anonimizados antes de pegarlos.
- Las restricciones ("no hagas X") son el componente más olvidado y uno de los más eficaces para eliminar el ruido de las respuestas.
- Guarda los prompts que funcionan: esa colección personal es una de las herramientas más valiosas de tu puesto de trabajo.
- Antes de enviar cualquier resultado de la IA, léelo completo y verifica los datos concretos: la IA puede equivocarse con total confianza.

---

## 21. CONEXIÓN CON EL RESTO DEL CURSO

Esta sesión es el punto de inflexión entre "probar la IA" (D01) y "usar la IA con criterio" (todo lo demás). La estructura R-C-T-F-R aprendida hoy es la base sobre la que se construyen todos los módulos posteriores: en **D03** se encadenan varios prompts R-C-T-F-R para resolver tareas complejas mediante iteración; en **D04-D07** (Módulo 3) cada ejercicio de redacción, resumen, traducción o generación de documentos parte de un prompt estructurado. Los 5 prompts del mini-entregable de hoy son la semilla que crece a lo largo del curso hasta convertirse en el flujo de trabajo del proyecto final de D16-D17.

---

## 22. FOOTER

*Brief para NotebookLM · D02 · Edición 01/26 — IA en la Oficina*
