# BRIEF PARA NOTEBOOKLM — D09
## Módulo 4, Sesión 2: Actas, seguimiento y delegación con IA
## Curso: IA en la Oficina – Eficiencia y Productividad
## Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital

**Fecha:** Lunes 13 de julio de 2026 · 15:00–19:00 h · Día 9 de 17

---

## 2. CONTEXTO DEL CURSO

**Programa:** IA en la Oficina – Eficiencia y Productividad (68 horas · 17 sesiones de 4 horas)
**Público:** Personal administrativo y de oficina sin experiencia previa en IA generativa
**Metodología:** ~40 % teoría y demostración · ~50 % práctica guiada · ~10 % puesta en común
**Sesión anterior (D08):** El grupo planifica su semana con IA, prepara reuniones más eficaces con orden del día y briefing previo, y conoce las opciones gratuitas de transcripción. Comienza la segunda semana del curso.

> *Este documento es la fuente del notebook de hoy. Además de las diapositivas, puedes pedirle a NotebookLM un resumen en **audio** (tipo pódcast), un **vídeo**, una **infografía** o mapa mental, una **guía de estudio**, **fichas** (flashcards), un **cuestionario** para autoevaluarte, o **escribir tus preguntas en el chat**. Usa el formato con el que mejor aprendas. No escribas datos personales reales en el chat.*

---

## 3. RESUMEN DE LA SESIÓN

Las reuniones son el gran consumidor de tiempo en la oficina moderna: sin acta, los acuerdos se olvidan; sin seguimiento, las tareas delegadas vuelven sin haberse hecho; sin instrucciones claras, la delegación se convierte en una fuente de malentendidos y trabajo doble. Hoy cerramos el módulo de organización aprendiendo a convertir notas caóticas de reunión en actas estructuradas en tres prompts, a crear tableros de seguimiento visuales sin herramientas de gestión de proyectos, y a redactar instrucciones de delegación que eliminen la ambigüedad. La segunda mitad de la sesión profundiza en el seguimiento: cómo redactar recordatorios profesionales que mantienen la presión sin deteriorar la relación, cómo escalar cuando una tarea no avanza, y cómo cerrar el ciclo de delegación documentando el resultado cuando la tarea se completa. El conjunto de flujos de hoy —acta → tablero → delegación → seguimiento → cierre— forma un sistema completo y autosuficiente que cualquier perfil administrativo puede aplicar desde el día siguiente sin aprender ninguna herramienta nueva. Estos tres flujos son inmediatamente aplicables al día siguiente de terminar la sesión. Hoy, además, es el punto de inflexión del curso: cada alumno revisará el mapa de oportunidades creado en D01 y elegirá la idea que desarrollará como proyecto final en D16 y D17.

---

## 4. ESTRUCTURA DE LA SESIÓN (240 min)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| Apertura | 15 min | Repaso D08 + checkpoint de proyecto final + objetivos del día |
| Teórico-demostrativo | 75 min | Anatomía del acta · Tableros de seguimiento · Instrucciones de delegación · Recordatorios |
| Descanso | 15 min | — |
| Práctica guiada | 95 min | Acta desde transcripción · Kanban propio · Delegación + revisión en parejas |
| Puesta en común | 40 min | Revisión de entregables + checkpoint proyecto final + mini-entregable |

*(15+75+15+95+40 = 240 min)*

---

## 5. OBJETIVOS DE APRENDIZAJE

1. Generar actas claras y útiles a partir de notas o transcripciones desordenadas en tres prompts o menos.
2. Crear tableros de seguimiento visuales (kanban y sistema RAG) con ayuda de IA, sin herramientas de gestión de proyectos.
3. Redactar instrucciones de delegación que incluyan los cinco elementos esenciales y eliminen los malentendidos más comunes.
4. Automatizar recordatorios y comunicaciones de seguimiento para tareas delegadas.

---

## 6. DESARROLLO TEÓRICO EN PROSA

### Por qué el acta es el documento más infravalorado de la oficina

Marta sale de una reunión de coordinación con cuatro páginas de notas garabateadas, cuatro acuerdos verbales y tres "¿quién se encargaba de eso?". Una semana después, dos de los acuerdos no se han ejecutado porque nadie recuerda exactamente qué se acordó ni quién era el responsable. Esta situación, que el 60 % de las personas reconoce vivir al menos una vez a la semana, tiene una solución directa: un acta bien estructurada redactada en los primeros diez minutos después de la reunión.

Un acta útil no es una transcripción de todo lo que se dijo. Es un documento de acción que contiene exactamente lo que se necesita para que la reunión tenga consecuencias. Su estructura tiene cinco secciones fijas que la IA puede rellenar a partir de notas o de una transcripción en menos de dos minutos.

El **encabezado** incluye el nombre de la reunión, la fecha y hora, los asistentes y quién moderó. El **contexto** es una sola frase que explica por qué se convocó la reunión y qué problema se pretendía resolver. Las **decisiones** son una lista numerada donde cada punto contiene una única decisión tomada, sin ambigüedades: no "se habló de la campaña de verano" sino "se aprueba lanzar la campaña de verano el 15 de julio con un presupuesto de X euros". Las **acciones** van en una tabla con tres columnas: acción concreta, responsable (nombre o cargo) y plazo. La **próxima reunión** cierra el documento con fecha, hora y objetivo, para que no haya que buscarla después.

El prompt para convertir notas en acta es directo y funciona con notas de cualquier nivel de desorden:

> "A partir de las siguientes notas de reunión, genera un acta con cinco secciones: (1) encabezado con fecha, asistentes y moderador, (2) contexto en una frase, (3) decisiones tomadas en lista numerada, (4) acciones acordadas en tabla con columnas Acción / Responsable / Plazo, (5) próxima reunión. Máximo una página. [PEGAR NOTAS]"

Si las notas son muy escuetas, se puede añadir un segundo prompt: *"¿Hay algún punto de las notas del que no quede claro si fue una decisión o solo una conversación? Señálalo para que yo lo confirme."* La IA identifica las ambigüedades que tú podrías haber pasado por alto.

> **Puntos clave:**
> - Un acta útil NO es una transcripción: contiene solo decisiones + tabla de acciones (Acción/Responsable/Plazo)
> - El prompt incluye las 5 secciones fijas: encabezado, contexto, decisiones, acciones, próxima reunión
> - Segundo prompt de ambigüedad: pide a la IA que señale qué notas son decisiones y cuáles conversación sin resolver

### Tableros de seguimiento sin herramientas de gestión de proyectos

Muchos equipos no tienen acceso a herramientas como Jira, Trello o Asana, o simplemente no quieren añadir otra herramienta al día. La IA permite crear tableros de seguimiento funcionales en formato texto dentro de un correo, un Google Doc o un mensaje de Teams, sin necesidad de ninguna aplicación adicional.

El **tablero kanban en texto** organiza las tareas en cuatro estados: Pendiente, En curso, Bloqueado y Completado. El prompt para crearlo es:

> "Crea un tablero kanban en formato tabla para el proyecto [NOMBRE]. Columnas: Pendiente / En curso / Bloqueado / Completado. Tareas: [LISTA]. Estado inicial de cada una: [ESTADOS]."

Para el seguimiento semanal, el sistema de semáforo RAG (Rojo/Ámbar/Verde) es especialmente útil porque hace visible el estado de cada tarea de un vistazo:

> "Genera una tabla de seguimiento semanal con columnas: Tarea / Responsable / Fecha límite / Estado / Notas. Estado: usa 🔴 para 'atrasado, requiere intervención', 🟡 para 'en riesgo leve, requiere atención' y 🟢 para 'en plazo, sin problemas'. Rellena con: [LISTA DE TAREAS]."

Marta usa este formato cada lunes para el correo semanal de su equipo. En lugar de redactar el resumen de estado tarea por tarea, actualiza la tabla de la semana anterior y pide a la IA que redacte el párrafo de seguimiento. Lo que antes le llevaba cuarenta minutos ahora son diez.

> **Puntos clave:**
> - Kanban en texto: 4 columnas (Pendiente/En curso/Bloqueado/Completado), sin necesidad de herramientas externas
> - Sistema RAG: 🔴 intervención urgente, 🟡 atención, 🟢 en plazo; hace el riesgo visible de un vistazo
> - Actualizar el tablero: pegar la tabla anterior en el chat + cambios de estado = nueva tabla en segundos

### Instrucciones de delegación que se entienden a la primera

El 80 % de los malentendidos en delegación no provienen de que la persona delegada sea incompetente, sino de que las instrucciones eran incompletas. Una buena instrucción de delegación tiene cinco elementos que la IA puede ayudarte a estructurar:

El primer elemento es el **qué**, pero no la actividad sino el resultado esperado: no "prepara el informe de ventas" sino "prepara un informe de ventas del Q2 de una página para la reunión del lunes, con los tres indicadores principales y una conclusión". El segundo elemento es el **por qué**: el contexto e importancia de la tarea, para que la persona delegada pueda tomar buenas decisiones si surge un imprevisto. El tercer elemento es el **cuándo**: no solo la fecha de entrega final, sino los hitos intermedios si la tarea lo requiere. El cuarto elemento es el **cómo**: los recursos disponibles, las restricciones (qué no puede hacer), el nivel de autonomía (¿puede decidir sin consultar o debe confirmar cada paso?). El quinto elemento es **cómo informar**: cuándo y de qué forma esperas que te actualice el progreso.

El prompt para generar una instrucción de delegación completa:

> "Redacta una instrucción de delegación clara y completa para la siguiente tarea: [DESCRIPCIÓN]. La persona que la recibirá tiene el siguiente perfil: [PERFIL]. Plazo de entrega: [FECHA]. Recursos disponibles: [LISTA]. Restricciones: [LISTA]. Resultado esperado: [DESCRIPCIÓN DETALLADA]. Incluye un punto sobre cómo y cuándo quiero que me mantenga informado del progreso."

El resultado es un texto que elimina las preguntas de seguimiento y los malentendidos antes de que ocurran. Marta calcula que con instrucciones bien redactadas reduce a la mitad el número de correos de aclaración que recibe después de delegar.

> **Puntos clave:**
> - Los 5 elementos: qué (resultado concreto, no actividad), por qué, cuándo (hitos + entrega final), cómo (recursos + restricciones + autonomía), cómo informar
> - El 80 % de los malentendidos en delegación vienen de instrucciones sin resultado esperado concreto
> - Una instrucción completa elimina las 3 preguntas de seguimiento más probables antes de que ocurran

### Recordatorios automatizados: cómo seguir sin parecer pesado

Delegar sin hacer seguimiento es la forma más rápida de no ver nunca el resultado. Pero hacer seguimiento de forma inadecuada (mensajes diarios, tono de urgencia innecesaria) deteriora la relación profesional. La IA ayuda a redactar recordatorios que son firmes pero cordiales.

Para el primer recordatorio, cuando la fecha de entrega se acerca:

> "Redacta un recordatorio cordial para [NOMBRE/ROL] sobre [TAREA] que vence el [FECHA]. Tono amable pero claro, que quede evidente que necesito el resultado en esa fecha. Máximo 60 palabras."

Para el segundo seguimiento, si no ha habido respuesta:

> "Redacta un segundo mensaje de seguimiento sobre [TEMA] para alguien que no ha respondido al primer recordatorio. Profesional, sin presión excesiva, pero dejando claro que necesito una respuesta o una actualización de estado antes del [FECHA]."

> **Puntos clave:**
> - Primer recordatorio: 60 palabras máximo, cordial, fecha clara
> - Segundo seguimiento si no hubo respuesta: más directo, pide actualización de estado, sin presión excesiva
> - El seguimiento sistemático (no reactivo) preserva la relación y multiplica la tasa de cumplimiento

### El ciclo completo de la reunión: preparación → acta → seguimiento → cierre

Una reunión eficaz no empieza cuando se abre el calendario y no termina cuando se cierra la videollamada. Empieza con la preparación (orden del día + briefing previo, D08) y termina cuando todas las acciones acordadas están completadas y documentadas como completadas. En el medio hay tres momentos que la IA gestiona en minutos: la generación del acta inmediatamente después de la reunión, la actualización del tablero de seguimiento una vez por semana, y el cierre formal del ciclo cuando la última acción se marca como completada. El error más frecuente es tratar cada reunión como un evento aislado en lugar de como un paso de un flujo continuo. Cuando Marta aplica el ciclo completo, descubre que el 70 % de las reuniones de seguimiento que tenía programadas desaparecen porque las acciones ya están visibles en el tablero y los responsables saben exactamente qué se espera de ellos.

> **Puntos clave:**
> - El ciclo completo es: preparación (D08) → acta → tablero de seguimiento → cierre de acciones
> - Tratar la reunión como evento aislado (sin acta ni seguimiento) es lo que genera las reuniones de seguimiento
> - Cuando el ciclo funciona, las reuniones de seguimiento se reducen porque la información ya es visible para todos

### La ambigüedad como causa principal de los malentendidos en delegación

Cuando una tarea delegada vuelve sin haberse hecho o hecha de forma incorrecta, la causa casi siempre es una de tres: el delegado no entendió el resultado esperado, no sabía qué recursos tenía disponibles, o no entendía hasta qué punto podía tomar decisiones solo. Las tres son formas de ambigüedad, y la IA ayuda a eliminarlas con dos técnicas concretas. La primera es el test de lectura desde el punto de vista del receptor: después de generar la instrucción de delegación, se le pide a la IA que la lea como si fuera el receptor y señale qué preguntas le surgirían. "Lee esta instrucción como si fuera la persona que la recibe. ¿Qué preguntas sobre el resultado, los recursos o el nivel de autonomía quedarían sin respuesta?" La IA identifica 2 o 3 gaps casi siempre. La segunda técnica es especificar el nivel de autonomía de forma explícita, que es lo que más raramente se hace: "puedes decidir sobre X sin consultarme; necesitas confirmarme antes de hacer Y; no hagas Z sin aprobación". Sin esta especificación, el delegado suele pecar de exceso de consultas (paraliza) o de exceso de autonomía (hace algo diferente a lo esperado).

> **Puntos clave:**
> - Test del receptor: pide a la IA que lea la instrucción como el destinatario y señale las preguntas que quedarían sin respuesta
> - Especificar el nivel de autonomía explícitamente: qué puede decidir solo, qué debe consultar antes, qué no puede hacer
> - Las 3 causas de malentendido: resultado poco claro, recursos no especificados, autonomía ambigua

### Cómo escalar el seguimiento cuando una tarea no avanza

Hay tareas delegadas que no avanzan por razones legítimas: la persona tiene más prioridades de las que puede gestionar, encontró un bloqueante que no sabía cómo resolver, o la tarea resultó más compleja de lo esperado. Y hay tareas que no avanzan simplemente porque no son prioritarias para quien las tiene asignadas. La diferencia importa porque cada una se gestiona de forma distinta. El primer paso siempre es preguntar, no asumir: un breve mensaje que pida una actualización de estado ("¿hay algún bloqueante en el que pueda ayudarte?") da la información necesaria para decidir cómo actuar. Si la respuesta revela un bloqueante legítimo, la acción es resolver el bloqueante o reasignar la tarea. Si la respuesta revela falta de prioridad, es el momento de una conversación directa sobre prioridades. La IA ayuda a redactar ambos tipos de mensajes sin que suenen ni como reproche ni como indiferencia. La escalada formal (comunicar a dirección o al responsable de área) se hace solo cuando la tarea tiene un impacto significativo y los intentos anteriores no han funcionado: la IA ayuda a redactar ese mensaje también, pero la decisión de escalar es siempre del usuario.

> **Puntos clave:**
> - Primer paso siempre: preguntar si hay bloqueante, no asumir falta de diligencia
> - Bloqueante legítimo → resolver el bloqueante o reasignar; falta de prioridad → conversación directa
> - La escalada formal es el último recurso; la IA redacta el mensaje pero la decisión de escalar es del usuario

### Documentar el cierre: el último paso del ciclo de delegación

Cuando una tarea delegada se completa, hay un paso que casi nadie hace: documentar el resultado. ¿Qué se entregó? ¿Cuándo? ¿Estaba completo o hubo excepciones? Este registro de cierre tiene tres funciones prácticas. La primera es el archivo: si en el futuro surge una duda sobre si esa tarea se hizo y cómo, hay un registro. La segunda es el aprendizaje: si la tarea tardó el doble de lo estimado o hubo imprevistos, esa información mejora la estimación la próxima vez que se delegue algo similar. La tercera es el reconocimiento: una nota explícita de "recibido, está completo, gracias" cierra el ciclo para la persona delegada y refuerza el hábito de cumplimiento. Marta usa un prompt de un solo párrafo para generar estas notas de cierre: "Redacta una nota de confirmación de que la tarea [DESCRIPCIÓN] ha sido completada satisfactoriamente por [PERSONA], entregada el [FECHA]. Tono: agradecido y profesional. Máximo 3 líneas." Es la forma más eficiente de cerrar el ciclo y de construir, con el tiempo, un registro de quién hace qué bien y en qué plazos.

> **Puntos clave:**
> - Documentar el cierre: qué se entregó, cuándo, si estaba completo; crea archivo, aprendizaje y reconocimiento
> - Una nota de cierre de 3 líneas refuerza el hábito de cumplimiento en la persona delegada
> - El registro acumulado muestra quién cumple en qué plazos: información valiosa para futuras delegaciones

---

## 7. DATOS Y CIFRAS CLAVE

- El 60 % de los acuerdos tomados en reuniones sin acta documentada no se ejecutan en el plazo acordado; con acta estructurada, ese porcentaje baja al 25 % (fuente: Harvard Business Review).
- El 80 % de los malentendidos en delegación provienen de instrucciones incompletas.
- Redactar un acta desde notas desordenadas con IA: 2–4 min. Sin IA desde notas: 20–40 min.
- Antes / Después: crear un tablero de seguimiento kanban para 10 tareas → antes: 15–20 min en herramienta externa; con prompt de IA: 2 min.
- El empleado medio pierde 31 horas al mes en reuniones no productivas (University of North Carolina); un acta bien estructurada reduce el tiempo de reuniones de seguimiento hasta un 30 %.
- Instrucción de delegación completa con IA: 3 min. Sin IA: 10–15 min (y suele estar incompleta).
- Equipos que sistematizan el seguimiento con tableros aumentan la tasa de cumplimiento de plazos un 35 %.
- Documentar el cierre de una tarea delegada (nota de confirmación de 3 líneas): crea registro, aprendizaje y refuerza el hábito de cumplimiento en el equipo.

---

## 8. EJEMPLOS RESUELTOS PASO A PASO

### Caso 1 — De notas caóticas a acta en dos prompts

**Situación:** Marta llega de una reunión de coordinación con estas notas: "- hablar de presupuesto Q3 - Carlos: pendiente proveedor logístico - María dijo que informe listo el 15 - hay que llamar a cliente Bravo - próxima reunión en 2 semanas - se aprueba presupuesto".

**Prompt 1 (anonimizado antes de pegar):**
> "A partir de las siguientes notas de reunión, genera un acta con: encabezado (fecha hoy, asistentes EMPLEADO_A y EMPLEADO_B, reunión de coordinación), contexto en una frase, decisiones tomadas en lista numerada, acciones en tabla Acción/Responsable/Plazo, próxima reunión. [PEGAR NOTAS ANONIMIZADAS]"

**Resultado comentado:** La IA genera una acta limpia en 30 segundos. Marta detecta que "llamar a cliente Bravo" no quedó claro si era una acción o una sugerencia.

**Prompt 2 (iteración):**
> "El punto de 'llamar al cliente' no quedó claro en la reunión. Márcalo en el acta con '[POR CONFIRMAR]' al lado del responsable para que sea evidente que necesita verificación."

---

### Caso 2 — Tablero kanban desde lista de tareas pendientes

**Situación:** Marta necesita un tablero de seguimiento para el cierre de fin de mes con 8 tareas asignadas a tres personas.

**Prompt exacto (con nombres anonimizados):**
> "Crea un tablero de seguimiento en formato tabla para el cierre de junio. Columnas: Tarea / Responsable / Plazo / Estado (🔴🟡🟢) / Observaciones. Tareas: (1) Conciliación bancaria — EMPLEADO_A — 28 junio — 🟢; (2) Informe de gastos — EMPLEADO_B — 25 junio — 🟡 (esperando datos de logística); (3) Facturación pendiente — EMPLEADO_A — 30 junio — 🔴 (atrasada 3 días); [continuar con las demás tareas]."

**Resultado comentado:** La IA genera una tabla clara con el semáforo de estado. Marta puede actualizarla cada semana pidiendo: "Actualiza la tabla cambiando el estado de la Tarea 2 a 🟢 y añadiendo en Observaciones 'recibidos datos el 24 junio'."

---

### Caso 3 — Instrucción de delegación para una tarea compleja

**Situación:** Marta va a delegar la preparación de un informe de proveedores a un compañero nuevo en el equipo.

**Prompt exacto:**
> "Redacta una instrucción de delegación para esta tarea: preparar el informe comparativo de proveedores de material de oficina del primer semestre. La persona que lo hará lleva 3 meses en la empresa y conoce el sistema de gestión pero no ha hecho este informe antes. Plazo: viernes de esta semana. Recursos: acceso al sistema de compras (solo lectura), la plantilla de informe del año pasado en Drive. Restricciones: no contactar directamente con los proveedores. Resultado esperado: tabla comparativa con los 5 proveedores principales, columnas Proveedor / Volumen / Precio medio / Incidencias / Valoración. Incluye cómo quiero que me actualice el progreso."

**Resultado comentado:** La IA genera una instrucción completa de 200-250 palabras que cubre los cinco elementos. Marta la revisa en un minuto, ajusta el plazo y la envía por correo. Ha eliminado de antemano las tres preguntas más probables del compañero.

---

### Caso 4 — Escalar el seguimiento de una tarea que no avanza

**Situación:** Marta delegó hace 5 días la preparación de un informe comparativo de proveedores a EMPLEADO_A. El plazo era el miércoles. Es viernes y no ha recibido ninguna actualización ni el informe. Antes de escalar a dirección, quiere enviar un segundo seguimiento que sea firme pero no confrontacional.

**Prompt exacto:**
> "Redacta un segundo mensaje de seguimiento para EMPLEADO_A sobre el informe comparativo de proveedores que tenía que entregar el miércoles. Han pasado 5 días desde la delegación y 2 días desde el plazo sin que haya habido ninguna actualización. El tono debe ser firme pero profesional: necesito saber si hay un bloqueante o si el informe estará listo hoy. No usar un tono de reproche. Máximo 5 líneas."

**Resultado comentado:** El mensaje generado reconoce la posibilidad de que haya un bloqueante antes de pedir explicaciones, pide una actualización de estado concreta para hoy antes de las 15:00 h, y es suficientemente directo para que el destinatario entienda la urgencia sin sentirse atacado.

**Cómo iterarlo:** Si el primer seguimiento tampoco recibe respuesta y Marta necesita escalar al responsable de área: "Redacta un correo de escalada profesional al responsable de área de EMPLEADO_A informando de que el informe comparativo de proveedores, con plazo del miércoles, no ha sido entregado ni actualizado. Incluye el contexto de la delegación (fecha y plazo original) y lo que se necesita ahora (el informe hoy o una nueva fecha comprometida). Tono: informativo, sin valoraciones personales."

---

## 9. GLOSARIO

**Acta:** Documento que registra las decisiones, acciones y compromisos de una reunión; no es una transcripción sino un documento de acción con estructura fija.

**Tablero kanban:** Sistema de seguimiento visual que organiza las tareas en columnas según su estado: Pendiente, En curso, Bloqueado, Completado.

**Sistema RAG:** Sistema de semáforo para seguimiento de estado: 🔴 Rojo (atrasado, intervención urgente), 🟡 Ámbar (en riesgo, atención), 🟢 Verde (en plazo, sin problemas).

**Delegación:** Transferencia de la responsabilidad de una tarea a otra persona, junto con los recursos y la autoridad necesarios para llevarla a cabo.

**Instrucción de delegación:** Documento o mensaje que recoge los cinco elementos de una delegación efectiva: qué (resultado esperado), por qué, cuándo, cómo y cómo informar.

**Acción comprometida:** Tarea específica acordada en una reunión, con responsable y plazo definidos; diferente de una sugerencia o un tema de conversación.

**Seguimiento (follow-up):** Proceso de verificar el progreso de las tareas delegadas o acordadas, idealmente mediante un sistema estructurado y no de manera ad hoc.

**Transcripción:** Texto generado a partir del audio de una reunión; herramienta de partida para generar el acta con IA (requiere consentimiento previo de todos los participantes).

**Cierre de delegación:** Confirmación formal de que una tarea delegada se ha completado satisfactoriamente, con nota de agradecimiento; crea registro, aprendizaje y refuerza el hábito de cumplimiento.

**Escalada:** Comunicación a un nivel jerárquico superior cuando una tarea no avanza y los intentos de seguimiento previos no han producido resultado; es el último recurso, no el primero.

**Test del receptor:** Técnica que consiste en pedir a la IA que lea una instrucción de delegación desde el punto de vista del destinatario para identificar preguntas o ambigüedades no resueltas antes de enviarla.

**Bloqueante:** Impedimento externo a la persona delegada que le impide avanzar en la tarea: falta de información, falta de acceso, dependencia de otra persona. Distinguirlo de la falta de prioridad es el primer paso antes de escalar.

---

## 10. ERRORES COMUNES Y BUENAS PRÁCTICAS

**Error 1 — Acta demasiado larga.** El acta no debe ser una transcripción de todo lo dicho. Si supera una página, probablemente está capturando conversaciones en lugar de decisiones y acciones. El prompt incluye siempre "máximo una página".

**Error 2 — No revisar el acta antes de distribuirla.** La IA puede malinterpretar alguna nota ambigua o asumir un responsable incorrecto. Dedica 2–3 minutos a revisar el acta antes de enviarla, especialmente la tabla de acciones.

**Error 3 — Pegar el acta con nombres reales en la IA.** Las notas de reunión a menudo contienen nombres completos, cargos y datos internos. Anonimiza antes de pegar: EMPLEADO_A, CLIENTE_B, PROYECTO_X.

**Error 4 — Instrucción de delegación sin resultado esperado concreto.** "Haz el informe de ventas" no es suficiente. Especifica siempre el formato, la extensión, la audiencia y qué decisión se tomará a partir del informe.

**Error 5 — Seguimiento sin sistema.** Recordar mentalmente qué tareas has delegado y a quién agota recursos cognitivos. Un tablero kanban o RAG actualizado una vez por semana lo automatiza completamente.

**Buena práctica — Comparte el acta el mismo día de la reunión.** El valor del acta cae rápidamente con el tiempo. Si la compartes el mismo día, los compromisos están frescos y la tasa de ejecución es significativamente más alta.

**Buena práctica — Guarda los prompts de acta y delegación en tu biblioteca.** Los prompts de acta y de instrucción de delegación son de los más reutilizables del curso. Una vez ajustados a tu tipo de reuniones y al perfil de tu equipo, guardarlos en la biblioteca de prompts de D04 garantiza que cada acta y cada delegación tenga el mismo nivel de calidad sin tener que reinventar el prompt.

**Error 6 — Escalar sin haber preguntado primero.** Comunicar a dirección que una tarea no está hecha sin antes haber pedido una actualización de estado es un error que deteriora relaciones profesionales. El primer paso siempre es preguntar si hay un bloqueante: el escalamiento se reserva para cuando ya se ha preguntado, ya se ha dado tiempo razonable y la tarea tiene un impacto significativo.

---

## 11. ACTIVIDADES EN AULA

### Actividad 1 — De transcripción a acta en 3 prompts [Grupo · 35 min]

**Descripción:** El formador proporciona la transcripción desordenada de una reunión de coordinación ficticia (1 página, ~15 intervenciones, con interrupciones y cambios de tema). El grupo trabaja colectivamente para extraer el acta en un máximo de 3 prompts, guiados por el formador. Se compara el resultado del primer prompt con el resultado después de iterar.

**Objetivo:** Que los alumnos vean que incluso con notas imperfectas, el flujo de 2–3 prompts produce un acta profesional.

**Material:** Transcripción ficticia de reunión (Google Doc compartido).

---

### Actividad 2 — Mi kanban y mis delegaciones [Individual · 30 min]

**Descripción:** Cada alumno crea dos entregables: (a) un tablero kanban con semáforo RAG para una iniciativa real o ficticia de su puesto, y (b) una instrucción de delegación completa para una tarea que habitualmente delega o podría delegar.

**Objetivo:** Practicar los dos flujos (tablero y delegación) con contexto propio y producir material reutilizable.

**Material:** ChatGPT o Gemini, Google Doc propio.

---

### Actividad 3 — Revisión cruzada de delegaciones [Pareja · 30 min]

**Descripción:** Por parejas, cada alumno comparte su instrucción de delegación con el compañero. El compañero actúa como la persona que recibe la delegación: ¿entiendo qué tengo que hacer? ¿Qué preguntas me surgirían? ¿Me falta algún elemento? Se anotan los gaps y cada persona mejora su instrucción con la retroalimentación recibida, ayudándose de la IA para reescribirla.

**Objetivo:** Detectar ambigüedades desde el punto de vista del destinatario, que suelen ser invisibles para quien delega.

**Material:** Instrucción de delegación creada en la Actividad 2.

---

## 12. 🔁 TRABAJO EN PAREJAS

En la **Actividad 3**, el grupo trabaja en **parejas** durante 30 minutos. Cada persona adopta el rol del destinatario de la delegación de su compañero y da retroalimentación honesta desde esa perspectiva: "No tengo claro cuál es el formato esperado", "No sé hasta qué punto puedo tomar decisiones solo", "¿Qué pasa si el sistema de compras no tiene el dato que necesito?". Este cambio de perspectiva, difícil de hacer uno mismo, es lo que hace que la instrucción de delegación pase de buena a excelente. La pareja usa después la IA para reescribir la instrucción incorporando el feedback recibido.

---

## 13. EJERCICIOS SUGERIDOS

Ver Banco de Ejercicios:
- **EJ-D09-1** (Individual): Generar acta y tablero RAG a partir de notas propias de una reunión real (anonimizadas)
- **EJ-D09-2** (Pareja): Revisión cruzada de instrucciones de delegación desde el punto de vista del receptor
- **EJ-D09-3** (Grupo): Simulación completa: notas de reunión → acta → tablero kanban → recordatorio a responsables

---

## 14. CUESTIONARIO DE AUTOEVALUACIÓN

**1. ¿Cuál es la diferencia entre un acta y una transcripción de reunión?**
a) El acta es más larga que la transcripción
b) El acta recoge decisiones y acciones; la transcripción recoge todo lo dicho ✓
c) La transcripción es más útil para hacer seguimiento
d) No hay diferencia relevante

**2. ¿Qué columnas debe tener la tabla de acciones en un acta bien estructurada?**
a) Tema / Comentarios / Estado
b) Acción / Responsable / Plazo ✓
c) Tarea / Departamento / Prioridad
d) Punto / Decisión / Fecha

**3. En el sistema RAG, ¿qué significa el estado 🟡 (Ámbar)?**
a) La tarea está completada
b) La tarea no ha empezado
c) La tarea está en riesgo leve y requiere atención ✓
d) La tarea está atrasada y requiere intervención urgente

**4. ¿Cuál de estos elementos NO forma parte de una instrucción de delegación completa?**
a) Qué resultado se espera
b) Por qué es importante la tarea
c) La opinión personal del delegante sobre la persona ✓
d) Cómo y cuándo informar del progreso

**5. Según los datos del curso, ¿qué porcentaje de acuerdos tomados en reuniones sin acta se ejecutan en plazo?**
a) El 80%
b) El 60%
c) El 40 % ✓ (el 60% NO se ejecuta)
d) El 20%

**6. ¿Por qué es importante anonimizar las notas de reunión antes de pegarlas en ChatGPT?**
Respuesta abierta: Porque las notas de reunión suelen contener **nombres completos**, cargos, datos de proyectos internos y a veces cifras económicas que son información confidencial de la organización. Al anonimizarlas (EMPLEADO_A, PROYECTO_X), puedes usar la IA para generar el acta sin comprometer los datos.

**7. ¿Cuál es el momento ideal para distribuir el acta de una reunión?**
a) Al día siguiente, cuando se ha descansado y se puede revisar con calma
b) En la siguiente reunión, para que sirva de punto de partida
c) El mismo día de la reunión, mientras los compromisos están frescos ✓
d) Antes de la próxima reunión, una semana después

**8. ¿Qué diferencia hay entre un kanban y un sistema RAG?**
Respuesta abierta: El **kanban** organiza las tareas por **estado de flujo** (Pendiente / En curso / Bloqueado / Completado) y es útil para visualizar el avance de un proceso. El **sistema RAG** organiza las tareas por **nivel de riesgo** (🔴 atrasada / 🟡 en riesgo / 🟢 en plazo) y es útil para priorizar la atención del equipo. Ambos se pueden combinar.

**9. ¿Qué hace el quinto elemento de una buena instrucción de delegación ("cómo informar")?**
a) Indica a la persona delegada cuándo puede pedir ayuda
b) Especifica cuándo y de qué forma debe reportar el progreso, eliminando la necesidad de hacer seguimiento reactivo ✓
c) Define el nivel de calidad esperado
d) Señala quién revisará el resultado final

**10. Verdadero o falso: si el primer acta que genera la IA a partir de tus notas tiene errores, es mejor empezar de cero con un prompt nuevo.**
Respuesta: **Falso**. Es mejor iterar sobre el resultado ya generado: señala el error específico ("el responsable del punto 3 no es EMPLEADO_A sino EMPLEADO_B") y pide la corrección manteniendo el resto. Esto es más eficiente que regenerar desde cero.

**11. ¿Qué hace el "test del receptor" en el proceso de delegación?**
Respuesta abierta: Consiste en pedir a la IA que lea la instrucción de delegación desde el punto de vista de quien la recibe y señale qué preguntas quedarían sin respuesta (sobre el resultado esperado, los recursos disponibles o el nivel de autonomía). Permite detectar ambigüedades antes de enviar la instrucción, eliminando las preguntas de seguimiento más probables.

**12. ¿Por qué es importante especificar el nivel de autonomía en una instrucción de delegación?**
a) Para que la persona delegada sepa cuánto tiempo puede invertir en la tarea
b) Para que la persona delegada sepa qué puede decidir sola, qué debe consultar y qué no puede hacer ✓
c) Para que la IA pueda redactar la instrucción con el tono correcto
d) No es necesario si la persona delegada tiene experiencia

**13. ¿Cuál es el primer paso cuando una tarea delegada no avanza?**
a) Escalar directamente al responsable de área
b) Reasignar la tarea a otra persona
c) Preguntar si hay un bloqueante antes de asumir falta de diligencia ✓
d) Cancelar la delegación y hacerlo uno mismo

**14. ¿Qué información debe incluir la nota de cierre de una delegación completada?**
a) Solo un agradecimiento genérico
b) Una evaluación del desempeño de la persona delegada
c) Qué se entregó, cuándo y si estaba completo; con tono agradecido y profesional ✓
d) Una lista de mejoras para la próxima delegación similar

**15. Describe el ciclo completo de gestión de una reunión con IA, desde la preparación hasta el cierre de todas las acciones.**
*Respuesta abierta:* (1) Preparación (D08): orden del día con tiempos y objetivos, briefing previo para participantes, preguntas clave para el moderador. (2) Acta (D09): convertir notas o transcripción en acta estructurada en ≤3 prompts, con encabezado, contexto, decisiones, acciones y próxima reunión. (3) Tablero de seguimiento: crear tabla kanban o RAG con las acciones del acta, actualizar una vez por semana. (4) Recordatorios: generar recordatorio cordial antes del plazo de cada acción. (5) Cierre: nota de confirmación cuando cada acción se completa. El ciclo completo elimina las reuniones de seguimiento porque la información siempre es visible.

---

## 15. PREGUNTAS FRECUENTES (FAQ)

**¿Qué hago si las notas de reunión son tan caóticas que no hay forma de entenderlas?**
Eso es exactamente para lo que sirve el primer prompt. Pega las notas tal cual (anonimizadas) y pide a la IA que las estructure antes de generar el acta: "Organiza estas notas de reunión en: puntos discutidos, decisiones mencionadas y tareas que parecen acordadas. Señala qué partes son ambiguas." Luego usa esa versión organizada para generar el acta definitiva.

**¿Puedo usar el acta generada por IA directamente sin revisarla?**
No. Siempre revisa el acta antes de enviarla, especialmente la tabla de acciones: que los responsables sean correctos, que los plazos coincidan con lo acordado y que ninguna "decisión" sea en realidad una conversación sin resolver. La revisión tarda 2–3 minutos y elimina el riesgo de confusiones.

**¿Qué pasa si no recuerdo quién era el responsable de alguna acción?**
Marca ese campo en la tabla con "[POR CONFIRMAR]" y envía el acta indicando que ese punto necesita verificación. Es mejor una acta con un campo pendiente que una acta con un responsable incorrecto.

**¿El kanban en texto funciona igual que Trello o Jira?**
No tiene las funcionalidades avanzadas de esas herramientas (notificaciones automáticas, asignación con correo, integraciones), pero funciona perfectamente para equipos pequeños o para un uso personal. La ventaja es que no requiere que nadie aprenda una herramienta nueva: es solo una tabla en un Google Doc.

**¿Cómo actualizo el tablero RAG cada semana sin tener que reescribirlo?**
Guarda la tabla en un Google Doc. Cada semana, copia la tabla y pégala en el chat con las novedades: "Actualiza la tabla cambiando el estado de X a 🟢 porque se entregó el martes, y añade la tarea nueva Y con responsable EMPLEADO_A y plazo el 20 de julio." La IA devuelve la tabla actualizada.

**¿Es normal que la persona a quien delego me haga muchas preguntas después?**
Si las preguntas son sobre el resultado esperado, el plazo o los recursos disponibles, es señal de que la instrucción de delegación estaba incompleta. Usa el modelo de 5 elementos (qué, por qué, cuándo, cómo, cómo informar) y las preguntas de seguimiento disminuirán drásticamente.

**¿Puedo pedir a la IA que redacte automáticamente los recordatorios de seguimiento?**
Sí, exactamente. Guarda el prompt de recordatorio con los datos de la tarea y úsalo cuando se acerque la fecha de entrega. La IA genera un mensaje cordial y profesional en segundos; tú solo tienes que revisarlo y enviarlo.

**¿Cuándo debo considerar escalar una tarea delegada que no avanza?**
La escalada se justifica cuando se cumplen tres condiciones: ya has enviado al menos un recordatorio directo preguntando por el estado, ha pasado un tiempo razonable desde el plazo acordado sin respuesta, y la tarea tiene un impacto real en otros procesos o personas. Si solo se cumple una de las tres, la escalada es prematura. Comunica la situación con hechos concretos (fecha de delegación, plazo acordado, intentos de seguimiento) y sin valoraciones personales sobre el delegado.

**¿Sirve el ciclo acta → tablero → seguimiento para reuniones de una sola persona (sin equipo)?**
Sí, y para muchos perfiles es donde aporta más valor. Si Marta tiene reuniones individuales con su jefa, clientes o proveedores, el acta estructurada de esas reuniones documenta los compromisos de ambas partes. El tablero de seguimiento puede ser un Google Doc personal. El ciclo completo aplica igual aunque solo haya dos personas en la reunión.

**¿Puedo usar el mismo prompt de acta para reuniones de equipo grandes (10+ personas)?**
Sí, pero con dos ajustes: (1) usa una transcripción de Tactiq o de Meet en lugar de notas manuales, porque con 10+ personas es imposible capturar todo a mano; (2) añade la instrucción "si un punto no tiene un responsable claramente identificado en la transcripción, escríbelo como '[RESPONSABLE POR CONFIRMAR]' en lugar de asignarlo por inferencia". En reuniones grandes la IA tiende a asumir responsables a partir del contexto, lo que puede producir asignaciones incorrectas.

---

## 16. HERRAMIENTAS DE LA SESIÓN

- **ChatGPT** (chat.openai.com) — Para generación de actas, tableros y delegaciones; cuenta gratuita.
- **Google Gemini** (gemini.google.com) — Alternativa directa con cuenta Gmail; puede usarse también dentro de Google Docs para trabajar sobre el documento directamente.
- **Google Docs** — Para guardar y compartir actas, tableros y plantillas de delegación; integrado con Gemini.

Ver el mapa completo en `Recursos/Herramientas_Gratuitas.md`.

---

## 17. MINI-ENTREGABLE DEL DÍA

**Nombre:** Kit de organización personal + idea de proyecto final
**Formato:** Google Doc
**Contenido:** (1) Acta de una reunión real o ficticia generada con IA, (2) tablero kanban/RAG de una iniciativa propia, (3) instrucción de delegación revisada después del feedback en parejas, (4) un párrafo breve describiendo la idea elegida para el proyecto final.
**Cómo alimenta el proyecto final:** El párrafo de descripción del proyecto es el primer artefacto del proyecto final, que se construirá en D16 y se presentará en D17.

---

## 18. 🎓 HILO DEL PROYECTO FINAL — CHECKPOINT (D09)

Hoy es el punto medio del curso: nueve sesiones completadas, ocho por delante. Es el momento de convertir el mapa de oportunidades de D01 en una decisión concreta.

**Tu tarea de hoy:** revisa el mapa que creaste en D01 y elige **una** oportunidad como tu proyecto final. Usa estos tres criterios para elegir: (1) que resuelva un problema real y recurrente de tu trabajo, algo que se repita al menos una vez a la semana; (2) que puedas construir una solución completa usando las herramientas y técnicas de M2–M4 (ya aprendidas) y lo que viene en M5–M7; (3) que puedas presentarla en 5 minutos con una demo o ejemplo concreto.

En D16 (la penúltima sesión) tendrás una sesión completa para construirla de principio a fin con el apoyo del formador. En D17 la presentarás al grupo. Incluye tu idea en el mini-entregable de hoy con una frase que explique el problema que resuelve y cómo la IA ayuda.

---

## 19. MENSAJE CLAVE DE LA SESIÓN

> "Una reunión sin acta es tiempo perdido. Una tarea delegada sin instrucción clara es trabajo que vuelve dos veces. La IA convierte las notas más caóticas en documentos de acción en menos tiempo del que tardas en explicarle a alguien qué tiene que hacer."

---

## 20. IDEAS PARA RECORDAR

- Un acta útil no es una transcripción: contiene solo decisiones y acciones, con responsable y plazo para cada una.
- Anonimiza siempre las notas antes de pegarlas en la IA: nombres → EMPLEADO_A, proyectos → PROYECTO_X.
- El tablero RAG (🔴🟡🟢) hace visible el estado de las tareas de un vistazo sin necesidad de herramientas de gestión de proyectos.
- Una instrucción de delegación sin los 5 elementos (qué, por qué, cuándo, cómo, cómo informar) genera preguntas de seguimiento que podrías haber evitado.
- Hoy es el checkpoint: elige tu idea de proyecto final. La construirás en D16 y la presentarás en D17.
- El ciclo completo (preparación → acta → tablero → seguimiento → cierre) elimina las reuniones de seguimiento innecesarias: la información siempre está visible.
- Antes de escalar una tarea que no avanza, pregunta si hay un bloqueante; la escalada es el último recurso, no el primero.

---

## 21. CONEXIÓN CON EL RESTO DEL CURSO

Esta sesión cierra el Módulo 4 (Organización del Trabajo), que comenzó en D08. El grupo sale de este módulo con un sistema completo para planificar su semana, preparar reuniones eficaces, levantarlas con acta estructurada y dar seguimiento a los compromisos. Es el módulo más directamente aplicable al día a día de cualquier perfil administrativo. Desde **D10** empieza el Módulo 5 (Datos y Búsqueda), que lleva la IA a un terreno nuevo: el análisis de hojas de cálculo y la investigación de mercado. El proyecto final elegido hoy en el checkpoint empezará a tomar forma real a partir de los módulos siguientes, que añaden nuevas herramientas a la caja que ya tienes.

---

## 22. FOOTER

*Brief para NotebookLM · D09 · Edición 01/26 — IA en la Oficina*
