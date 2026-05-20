# BRIEF PARA NOTEBOOKLM — D14
## Módulo 7, Sesión 1: Gestión documental y flujos de trabajo con IA
## Curso: IA en la Oficina – Eficiencia y Productividad
## Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital

**Fecha:** Lunes 20 de julio de 2026 · 15:00–19:00 h · Día 14 de 17

---

## 2. CONTEXTO DEL CURSO

**Programa:** IA en la Oficina – Eficiencia y Productividad (68 horas · 17 sesiones de 4 horas)
**Público:** Personal administrativo y de oficina sin experiencia previa en IA generativa
**Metodología:** ~40 % teoría y demostración · ~50 % práctica guiada · ~10 % puesta en común
**Sesión anterior (D13):** El grupo crea material visual interno accesible y kits de comunicación coordinados.

> *Este documento es la fuente del notebook de hoy. Además de las diapositivas, puedes pedirle a NotebookLM un resumen en **audio** (tipo pódcast), un **vídeo**, una **infografía** o mapa mental, una **guía de estudio**, **fichas** (flashcards), un **cuestionario** para autoevaluarte, o **escribir tus preguntas en el chat**. Usa el formato con el que mejor aprendas. No escribas datos personales reales en el chat.*

---

## 3. RESUMEN DE LA SESIÓN

En casi todas las oficinas existe una categoría de conocimiento que no está en ningún manual: el "saber cómo hacer" que vive en la cabeza de una sola persona y que, cuando esa persona está de vacaciones, enferma o cambia de puesto, hace que el equipo se detenga o cometa errores. Hoy aprendemos a transformar ese conocimiento tácito en documentación útil, concreta y mantenible, con la ayuda de la IA como copiloto de escritura estructurada. Veremos cómo nombrar y organizar carpetas de forma coherente, cómo convertir una descripción caótica de un proceso en un Procedimiento Operativo Estándar (SOP), cómo generar una checklist de uso diario a partir de ese SOP y cómo usar Google Forms y Sheets para crear flujos sencillos de recogida de datos sin necesidad de programar. También exploraremos cómo NotebookLM puede convertirse en una base de conocimiento consultable por cualquier compañero del equipo. Al terminar la sesión, cada persona tendrá documentado al menos un procedimiento propio, en un formato que cualquier colega puede seguir sin preguntar.

---

## 4. ESTRUCTURA DE LA SESIÓN (240 min)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| Apertura | 15 min | Repaso D13 + dinámica de arranque: "¿qué proceso de tu trabajo vive solo en tu cabeza?" |
| Teórico-demostrativo | 75 min | El problema documental · Nombrar y clasificar · SOPs con IA · Checklists · Mapeo de flujos · Google Forms → Sheets · NotebookLM como base de conocimiento · Cuándo NO automatizar |
| Descanso | 15 min | — |
| Práctica guiada | 95 min | Demo en grupo · Mapeo de proceso en parejas · SOP individual |
| Puesta en común | 40 min | Presentación de SOPs + reflexión sobre el conocimiento tácito + cierre |

*(15+75+15+95+40 = 240 min)*

---

## 5. OBJETIVOS DE APRENDIZAJE

1. Crear un Procedimiento Operativo Estándar (SOP) completo a partir de una descripción verbal de un proceso, usando IA como asistente de escritura estructurada.
2. Generar una checklist de uso diario a partir de un SOP existente para facilitar su aplicación en el día a día.
3. Diseñar un formulario de Google Forms conectado a una hoja de Google Sheets para automatizar la recogida de datos sin necesidad de conocimientos técnicos.
4. Identificar los límites de la automatización y las tareas que requieren criterio humano y no deben delegarse en un proceso automático.

---

## 6. DESARROLLO TEÓRICO EN PROSA

### El problema de la documentación en la oficina

Marta lleva cuatro años en el departamento de administración de su empresa y gestiona, entre otras cosas, el proceso de solicitud de material de oficina: quién puede pedirlo, con qué antelación, qué formulario hay que rellenar, quién lo aprueba, con qué proveedor se trabaja y qué pasa cuando el proveedor no tiene existencias. Ese proceso existe y funciona razonablemente bien, pero solo porque Marta lo conoce. Cuando Marta estuvo de baja dos semanas en febrero, el proceso se paralizó o se gestionó de forma distinta según quién interviniera. La empresa tiene carpetas llenas de documentos, pero no tiene ningún documento que explique ese proceso de principio a fin.

Este escenario es más frecuente que la excepción en las organizaciones medianas y pequeñas. La información está dispersa entre correos electrónicos, mensajes de Teams, documentos sin versionar, notas adhesivas y la memoria de las personas. Cuando alguien falta, se va o cambia de puesto, una parte del funcionamiento de la empresa se va con ellas. No es que nadie quiera que esto sea así: es que documentar se percibe como una tarea adicional que "ya haré cuando tenga tiempo", y ese tiempo nunca llega porque la prioridad siempre la tienen las tareas urgentes del día.

La IA cambia esta ecuación de forma significativa porque **elimina la parte más costosa de documentar: la escritura**. Si Marta puede describir oralmente (o por escrito en párrafos informales) cómo funciona el proceso de pedido de material, la IA puede convertir esa descripción en un SOP estructurado, con secciones, pasos numerados y un formato homogéneo, en menos de dos minutos. Lo que antes requería una o dos horas de escritura cuidadosa ahora requiere una revisión de diez minutos. La barrera del tiempo desaparece.

> **Puntos clave:**
> - El conocimiento tácito es frágil cuando depende de una sola persona.
> - La información dispersa en correos y memoria detiene equipos.
> - La IA elimina el coste mayor: redactar desde cero.
> - Revisar diez minutos sustituye a escribir una hora.

### Nombrar y clasificar documentos con criterio

Antes de hablar de cómo crear documentos, hay que hablar de cómo encontrarlos. Una carpeta de empresa sin convención de nombrado es un laberinto: "Informe final v2 DEFINITIVO (1).docx", "Contrato Pedro 2024 nuevo.pdf", "hoja de cálculo marzo.xlsx". Nadie recuerda cómo se llamaba el archivo que busca, y la búsqueda por nombre se convierte en una lotería.

Una **convención de nombrado** es un conjunto de reglas acordadas para nombrar archivos y carpetas de forma coherente. Una convención simple pero efectiva para entornos de oficina incluye cuatro elementos: **área o departamento**, **tipo de documento**, **descripción breve** y **fecha en formato AAAA-MM-DD**. Por ejemplo: `ADM_SOP_PedidoMaterial_2026-07-01` o `RRHH_FORM_SolicitudVacaciones_2026`. Este formato tiene varias ventajas: los archivos se ordenan automáticamente por departamento y fecha en cualquier explorador de carpetas, el tipo de documento permite buscar solo SOPs o solo formularios, y la fecha hace innecesario el sufijo "versión final definitiva".

La IA puede ayudar a diseñar una convención de nombrado personalizada para el equipo. El prompt es: "Soy responsable de administración de una empresa distribuidora de tamaño medio. Nuestra carpeta de documentos está desorganizada. Diseña una convención de nombrado para archivos y carpetas que sea simple, consistente y fácil de aplicar sin formación previa. Incluye ejemplos de los tipos de documentos más frecuentes: contratos, facturas, informes, formularios, procedimientos, plantillas." La IA devuelve una propuesta con ejemplos concretos que el equipo puede adaptar y adoptar en una reunión breve.

La **estructura de carpetas** sigue la misma lógica: unas pocas carpetas de primer nivel claras (Procedimientos, Plantillas, Informes, Proveedores, Clientes, Proyectos) y nunca más de tres niveles de profundidad. Una estructura demasiado profunda es tan difícil de navegar como una sin estructura.

> **Puntos clave:**
> - Una convención coherente convierte la búsqueda en algo predecible.
> - Usar área, tipo, descripción y fecha AAAA-MM-DD.
> - La IA puede proponer la convención adaptada al equipo.
> - Nunca pasar de tres niveles de carpetas de profundidad.

### Escribir SOPs con IA: de la descripción caótica al procedimiento claro

Un **Procedimiento Operativo Estándar** (SOP, por sus siglas en inglés) es un documento que describe cómo se realiza una tarea de principio a fin de forma que cualquier persona competente pueda ejecutarla sin depender de quien la documentó. Un buen SOP tiene seis partes: **título** (qué proceso describe), **objetivo** (para qué sirve y qué resultado produce), **quién y cuándo** (quién es responsable de ejecutarlo y en qué circunstancias), **pasos detallados** (secuencia numerada de acciones), **excepciones** (qué hacer si algo falla o no sigue el camino normal) y **versión y fecha** (cuándo fue creado o revisado por última vez).

El flujo para crear un SOP con IA es el siguiente. Primero, describir el proceso en lenguaje informal, como si se lo estuvieras explicando a alguien nuevo por teléfono: "Cuando alguien pide material de oficina, me manda un correo o me lo dice en persona. Yo compruebo si tenemos existencias en el almacén. Si tenemos, le digo que pase a recogerlo. Si no tenemos, contacto al proveedor habitual, que es Suministros García, y hago el pedido. El pedido tarda entre 3 y 5 días. Cuando llega, aviso al solicitante. Si el proveedor no tiene el material, busco alternativa o lo consulto con mi jefa." Esa descripción informal, con todos sus detalles y matices, es la materia prima del SOP.

El segundo paso es pegarlo en ChatGPT, Claude o Gemini con este prompt:

> "Convierte la siguiente descripción informal de un proceso administrativo en un SOP (Procedimiento Operativo Estándar) con estas secciones: Título, Objetivo, Responsable y cuándo aplica, Pasos (numerados y detallados), Excepciones y casos especiales, Versión y fecha. El tono debe ser formal pero claro, en español. Descripción del proceso: [PEGAR DESCRIPCIÓN]"

La IA devuelve un SOP estructurado que Marta revisa en diez minutos: comprueba que los pasos están completos, añade los nombres internos correctos (el proveedor real, el sistema de correo interno) y corrige cualquier detalle que la IA haya interpretado de forma imprecisa. El resultado es un documento útil, consistente con el formato de los demás SOPs del equipo, y que cualquier compañero puede seguir.

Un caso especialmente útil es cuando ya existe un documento de instrucciones, pero está redactado de forma caótica o incompleta: un correo de "cómo se hace esto" que alguien mandó hace dos años, una lista de pasos a medias, un PDF escaneado. La IA puede tomar ese material y estructurarlo como SOP con el mismo prompt: "Convierte este texto en un SOP con las siguientes secciones... [PEGAR TEXTO ORIGINAL]"

> **Puntos clave:**
> - Un buen SOP tiene seis secciones bien diferenciadas.
> - Describir primero el proceso en lenguaje informal y completo.
> - La IA estructura; tú revisas nombres y matices internos.
> - También sirve para reestructurar documentos antiguos caóticos.

### De SOP a checklist de uso diario

Un SOP es el documento de referencia: explica el proceso completo con todos sus matices. Pero para el uso cotidiano, lo que más se necesita es una **checklist**: una lista de verificación breve que permite confirmar que no se ha saltado ningún paso sin tener que releer el SOP completo cada vez.

La conversión es instantánea con IA: una vez que tienes el SOP, añades un prompt de seguimiento: "Ahora genera una checklist de uso diario a partir de este SOP. Debe ser una lista de verificación concisa con casillas de verificación (☐), máximo 10 ítems, con el verbo en infinitivo. El objetivo es que alguien pueda marcar cada paso mientras lo ejecuta sin necesitar leer el SOP completo."

La IA devuelve una checklist lista para imprimir o compartir en Google Docs. Esta checklist puede convertirse en una plantilla reutilizable: cada vez que alguien ejecuta el proceso, imprime o abre una copia nueva, marca los pasos realizados y la archiva o descarta. En sectores donde hay obligación de trazabilidad o auditoría, la checklist completada y firmada es también evidencia de que el proceso se siguió correctamente.

> **Puntos clave:**
> - El SOP es referencia; la checklist es uso diario.
> - Máximo diez ítems, verbo en infinitivo, casillas marcables.
> - Un prompt de seguimiento convierte el SOP en checklist.
> - Sirve como evidencia de trazabilidad cuando se firma.

### Mapear flujos de trabajo con texto

Antes de documentar un proceso como SOP, a veces es útil entender primero cómo funciona realmente el proceso de principio a fin, identificar si hay pasos redundantes, cuellos de botella o decisiones que nadie ha definido formalmente. Esta es la fase de **mapeo de flujo**.

El mapeo de flujo con IA no requiere ningún software de diagramas. Basta con describir el proceso como una secuencia de acciones y decisiones en texto plano, usando una notación simple: "A → B → si C, entonces D; si no, E → F". Por ejemplo: "Recepción de pedido → Comprobación de existencias → Si hay existencias: confirmar al cliente y preparar envío → Si no hay: contactar proveedor → Si proveedor puede servir en 3 días: hacer pedido → Si no: buscar alternativa o escalar a responsable → Recepción de mercancía → Aviso al cliente → Archivo del albarán."

Una vez descrito el flujo en texto, se puede pedir a la IA que lo analice: "Este es el flujo de un proceso de gestión de pedidos de material. ¿Identificas algún cuello de botella, paso redundante o situación donde no hay responsable definido? ¿Qué mejorarías?" La IA suele identificar puntos donde el proceso depende de una sola persona, pasos donde no hay tiempo máximo definido o situaciones de excepción que no están contempladas. Esa análisis es la base para mejorar el proceso antes de documentarlo definitivamente.

> **Puntos clave:**
> - Antes de documentar, conviene entender el proceso real.
> - Bastan flechas y condicionales en texto plano.
> - La IA detecta cuellos de botella y responsabilidades difusas.
> - Mejorar el flujo antes de fijarlo como SOP definitivo.

### Google Forms → Sheets: automatización sin código

Una de las automatizaciones más útiles y accesibles para cualquier persona de oficina es la combinación de **Google Forms** con **Google Sheets**. El principio es simple: se crea un formulario de Google para recoger datos (solicitudes, registros, encuestas), y cada respuesta se guarda automáticamente en una hoja de cálculo de Google Sheets, sin necesidad de copiar datos a mano.

Los casos de uso son muy variados: registro de incidencias (quién notifica la incidencia, cuándo, de qué tipo, estado de resolución), solicitudes de material (quién pide, qué pide, para cuándo, aprobado o no), encuestas de satisfacción de un servicio interno, registro de asistencia a formaciones o eventos, seguimiento de tareas de un proyecto. En todos estos casos, el formulario es el punto de entrada de datos y la hoja de cálculo es la base de datos que permite después analizar, filtrar y exportar la información.

El proceso de creación es sencillo. En Google Drive, crear un nuevo formulario (Nuevo → Formulario de Google). Añadir las preguntas del formulario: texto corto para nombres y descripciones, desplegable o selección múltiple para categorías, fecha para el registro de cuándo ocurrió algo. Una vez el formulario está listo, en el menú de respuestas → "Ver en Sheets" → Google crea automáticamente una hoja de cálculo vinculada donde cada respuesta nueva aparece como una fila nueva. Desde esa hoja, se pueden aplicar filtros, crear tablas dinámicas o pegar los datos anonimizados en ChatGPT para análisis, exactamente igual que en D10.

Marta aplica esto al registro de incidencias de su departamento: antes, cada incidencia se notificaba por correo y luego ella tenía que copiar los datos en una hoja de Excel manualmente. Ahora, cualquier compañero rellena el formulario de Google en dos minutos, y la hoja de cálculo se actualiza sola. Al final del mes, Marta tiene un dataset limpio y completo para analizar, sin haber transcrito ni un solo dato.

La IA también puede ayudar a diseñar el formulario: "Voy a crear un formulario de Google para registrar incidencias en el departamento de logística. ¿Qué campos debería incluir para que los datos sean útiles para el análisis posterior? Incluye el tipo de campo recomendado para cada uno (texto libre, desplegable, fecha, etc.)."

> **Puntos clave:**
> - Forms recoge datos; Sheets los acumula automáticamente como filas.
> - Cero transcripción manual desde el primer registro.
> - Útil para incidencias, solicitudes, encuestas y registros internos.
> - La IA puede sugerir los campos y sus tipos.

### NotebookLM como base de conocimiento del equipo

Una vez que el equipo tiene varios SOPs documentados, surge una pregunta práctica: ¿cómo consulta un compañero un procedimiento sin tener que buscar el documento correcto entre decenas de archivos? La respuesta puede ser **NotebookLM** usado como base de conocimiento consultable.

El flujo es el siguiente: subir los SOPs del equipo como fuentes a un notebook de NotebookLM (en PDF o Google Doc). A partir de ese momento, cualquier persona que tenga acceso al notebook puede hacerle preguntas en lenguaje natural: "¿Cómo se gestiona una solicitud de material urgente?", "¿Quién aprueba los pedidos superiores a 500 euros?", "¿Qué hago si el proveedor habitual no puede servir el material?". NotebookLM busca la respuesta en los SOPs subidos y la presenta con la referencia al documento de origen.

Esto tiene dos ventajas importantes. La primera es que la consulta es inmediata y no requiere abrir y leer el SOP completo: se pregunta en lenguaje natural y se obtiene el fragmento relevante. La segunda es que las respuestas están fundamentadas en los documentos reales del equipo, no en el conocimiento general de la IA, lo que reduce el riesgo de respuestas incorrectas o inventadas.

Una limitación importante a tener en cuenta: NotebookLM solo puede responder sobre lo que está en los documentos subidos. Si un procedimiento no está documentado, NotebookLM no puede inventarlo. Esta es, en realidad, una ventaja indirecta: incentiva a documentar más, porque cuanto más completa es la base de conocimiento, más útil es la herramienta.

> **Puntos clave:**
> - Subir SOPs convierte un notebook en consulta colectiva.
> - Las respuestas se fundamentan en los documentos reales del equipo.
> - Solo responde sobre lo subido: no inventa procedimientos.
> - Esa limitación incentiva a documentar más y mejor.

### Cuándo NO automatizar

Ninguna herramienta tecnológica es la respuesta correcta a todos los problemas, y la IA no es una excepción. Hay tareas que no deben automatizarse ni delegarse en un proceso mecánico, y es importante que el equipo pueda identificarlas.

Las decisiones que afectan directamente a personas de forma significativa —si se renueva o no el contrato de un proveedor de larga duración, cómo se gestiona una situación de conflicto entre compañeros, si un trabajador tiene o no derecho a una adaptación de su puesto por razones de salud— requieren **criterio humano, contexto, empatía y responsabilidad**. Un SOP puede describir el proceso de recogida de información y la cadena de aprobaciones, pero la decisión en sí no puede delegarse en un automatismo.

Del mismo modo, cualquier tarea donde un error tiene consecuencias graves e irreversibles —el envío de una comunicación oficial a un organismo público, la firma de un contrato, la baja de un proveedor del sistema, la modificación de datos salariales— debe tener siempre una persona responsable que revise y confirme antes de ejecutar. La automatización puede preparar los datos, redactar el borrador y verificar que la información es completa, pero el "enviar" o "confirmar" final debe ser siempre un acto humano consciente.

Una buena regla práctica: si la pregunta "¿qué pasa si esto sale mal?" no tiene una respuesta simple y reversible, no se automatiza sin supervisión humana en el paso final.

> **Puntos clave:**
> - Decisiones con impacto en personas requieren criterio humano siempre.
> - Acciones irreversibles necesitan confirmación humana consciente al final.
> - La IA prepara y revisa; la persona decide y firma.
> - Regla: si el error no es reversible, supervisar manualmente.

### Mantenimiento y revisión periódica de los SOPs

Un SOP útil hoy puede quedar obsoleto en pocos meses si el proceso cambia y la documentación no se actualiza. Marta lo experimentó cuando el proveedor de material cambió de plataforma de pedidos: el SOP seguía describiendo el flujo antiguo y los compañeros que lo consultaron en agosto cometieron errores. Por eso, cada SOP necesita un **responsable de mantenimiento** explícito y un **ritmo de revisión** definido. En general, una revisión anual basta para procesos estables; los procesos en evolución (proveedores nuevos, cambios normativos recientes) conviene revisarlos trimestralmente. La IA puede ayudar a comparar la versión vigente con una descripción actualizada y resaltar diferencias: "Este es el SOP actual. Este es cómo se hace hoy realmente. Resalta los puntos del SOP que necesitan actualizarse." Esa comparación reduce el tiempo de revisión y evita olvidos.

> **Puntos clave:**
> - Sin responsable y sin fecha, todo SOP envejece silenciosamente.
> - Revisión anual basta para procesos estables.
> - Procesos cambiantes piden revisión trimestral.
> - La IA compara versión vigente con descripción actualizada.

### Privacidad y datos sensibles en la documentación

Documentar procesos administrativos implica, a veces, manejar información delicada: nombres de empleados, datos de proveedores, importes salariales, claves de acceso, criterios internos de aprobación. Es importante separar lo que va al SOP de lo que debe permanecer fuera. En general, el SOP describe **el proceso**, no las credenciales ni los datos personales concretos: indica "consultar el listado de proveedores autorizados" en lugar de pegar el listado completo, y "introducir las credenciales del sistema de gestión" en lugar de incluir usuarios y contraseñas. Cuando Marta usa IA para redactar un SOP, también sustituye nombres reales por marcadores ("Proveedor A", "Compañera responsable") antes de pegar la descripción en el chat. Esa higiene básica evita filtraciones y, según experiencia del sector, suele exigirlo cualquier política de protección de datos.

> **Puntos clave:**
> - El SOP describe el proceso, no las credenciales concretas.
> - Sustituir nombres reales por marcadores antes de usar IA.
> - Nunca pegar contraseñas ni datos personales en el chat.
> - La higiene básica protege frente a filtraciones accidentales.

---

## 7. DATOS Y CIFRAS CLAVE

- Los empleados dedican de media **2,5 horas al día a buscar información** que debería estar accesible y organizada (McKinsey Global Institute).
- El **42 % del conocimiento organizativo específico de cada puesto** vive solo en la memoria de la persona que ocupa ese puesto, sin ninguna documentación de respaldo.
- Crear un SOP desde una descripción verbal con IA: **15–20 minutos** frente a **1–2 horas** de escritura tradicional desde cero.
- Un equipo con SOPs actualizados reduce el tiempo de incorporación de personas nuevas a un puesto en un **40–60 %** (SHRM, Society for Human Resource Management).
- Google Forms + Sheets automatiza la recogida de datos sin programación: **0 minutos de transcripción manual** por registro.
- Antes / Después: registro manual de incidencias en Excel (copiar de correo a hoja) → **5–10 min por incidencia**; con Google Forms → **0 min de trabajo manual**.
- El tiempo de respuesta a una pregunta de procedimiento cuando hay SOPs en NotebookLM: **menos de 1 minuto** frente a **10–20 minutos** de búsqueda en carpetas y correos.
- Las organizaciones con procesos documentados tienen un **30 % menos de errores operativos** en tareas repetitivas que aquellas que dependen de la memoria y la tradición oral (estudio Deloitte, 2022).

---

## 8. EJEMPLOS RESUELTOS PASO A PASO

### Caso 1 — De descripción caótica a SOP en tres prompts

**Situación:** Marta describe oralmente cómo gestiona las solicitudes de material de oficina. La descripción es informal, incompleta y con varias bifurcaciones.

**Descripción original de Marta (texto informal):**
"Cuando alguien me pide algo, primero miro si lo tenemos en el almacén. Si sí, le digo que pase. Si no, llamo a Suministros García o les mando un correo, depende. El pedido normalmente tarda 3 días, a veces más. Cuando llega aviso a quien lo pidió. Si el proveedor no tiene, busco en otra parte o se lo comento a mi jefa para que decida."

**Prompt 1 — Crear el SOP:**
> "Convierte esta descripción informal en un SOP (Procedimiento Operativo Estándar) con estas secciones: Título, Objetivo, Responsable y cuándo aplica, Pasos numerados y detallados, Excepciones y casos especiales, Versión y fecha (usar hoy). Tono formal pero claro, en español. Descripción: [TEXTO DE MARTA]"

**Prompt 2 — Revisar y completar:**
> "El SOP está bien, pero falta especificar: (1) el plazo máximo de respuesta al solicitante cuando no hay existencias, (2) qué información exacta debe incluir el correo al proveedor. Añade esos detalles en los pasos correspondientes."

**Prompt 3 — Generar la checklist:**
> "Ahora genera una checklist de uso diario con casillas (☐), máximo 8 ítems, verbo en infinitivo, para que Marta pueda marcar cada paso mientras gestiona una solicitud de material."

**Resultado:** Un SOP de una página más una checklist de 8 puntos. Tiempo total: 18 minutos, incluyendo la revisión de Marta.

---

### Caso 2 — Mapeo y mejora de un flujo de trabajo con IA

**Situación:** El equipo de administración quiere entender por qué el proceso de aprobación de facturas tarda tanto. Describen el flujo actual al asistente de IA.

**Flujo descrito:**
"Llega una factura → La recibe Marta → Marta la registra en el sistema → Marta la envía a su jefa por correo → La jefa la revisa → Si hay alguna duda, la jefa pregunta al proveedor directamente → Si no hay duda, la jefa la aprueba y la reenvía a contabilidad → Contabilidad registra el pago → Pago al proveedor en 30 días."

**Prompt exacto:**
> "Este es el flujo de aprobación de facturas de nuestro departamento. Analízalo e identifica: (1) cuellos de botella o pasos que dependen de una sola persona, (2) pasos donde no hay un tiempo máximo definido, (3) situaciones de excepción que no están contempladas y (4) cualquier mejora que podría reducir el tiempo total del proceso. Sé concreto y práctico."

**Resultado:** La IA identifica que el cuello de botella principal es la revisión de dudas con el proveedor (que no tiene tiempo límite definido) y que el proceso depende completamente de la disponibilidad de la jefa sin delegación posible. Propone: añadir un SLA de respuesta de 48 horas para la jefa y crear un protocolo de escalado si no responde en ese plazo.

---

### Caso 3 — Diseño de formulario de Google con IA

**Situación:** Marta quiere crear un formulario de registro de incidencias logísticas para que cualquier compañero pueda notificar un problema sin tener que mandarle un correo.

**Prompt exacto:**
> "Voy a crear un formulario de Google para que mis compañeros registren incidencias logísticas. El objetivo es recoger datos útiles para el análisis mensual. ¿Qué campos debería incluir? Para cada campo, dime el nombre del campo, el tipo de respuesta recomendado (texto corto, párrafo, desplegable, fecha, escala 1–5, etc.) y por qué es importante incluirlo."

**Resultado:** La IA propone: Nombre del notificador (texto corto), Fecha de la incidencia (fecha), Tipo de incidencia (desplegable con categorías: retraso en entrega, mercancía dañada, error en pedido, otro), Descripción detallada (párrafo), Impacto estimado (desplegable: leve, moderado, grave), Estado actual (desplegable: pendiente, en gestión, resuelto). Marta añade el campo de "número de pedido afectado" que la IA no había incluido y que es fundamental para el seguimiento interno.

---

### Caso 4 — Consulta de procedimientos con NotebookLM en el equipo

**Situación:** El departamento ha documentado cinco SOPs (pedidos de material, gestión de incidencias, aprobación de facturas, alta de proveedores y solicitud de vacaciones). Marta quiere convertirlos en una base de conocimiento consultable para que cualquier compañero pueda preguntar dudas sin interrumpirla.

**Prompt exacto (dentro del notebook de NotebookLM, con los cinco SOPs como fuentes):**
> "Eres el asistente de procedimientos del departamento de administración. Responde solo con la información que aparece en los SOPs subidos. Si la respuesta no está en los documentos, di exactamente: 'Este punto no está documentado todavía; consulta con la persona responsable'. Cita siempre el SOP de origen al final de cada respuesta. Pregunta de prueba: ¿qué hago si un proveedor habitual no puede servir el material en el plazo previsto?"

**Resultado comentado:** NotebookLM responde con los pasos del SOP de pedidos de material (buscar proveedor alternativo, escalar a responsable si el importe supera 500 euros) y cita el documento de origen. Cuando Marta pregunta algo no documentado ("¿qué pasa si el solicitante quiere material no incluido en el catálogo aprobado?"), responde con la frase de fallback acordada, lo que revela un hueco en la documentación que merece un nuevo SOP o un anexo.

**Cómo iterarlo:** Tras dos semanas de uso, Marta pide a NotebookLM: "Lista todas las preguntas que no has podido responder por falta de documentación en las últimas conversaciones." Esa lista se convierte en la agenda de la siguiente sesión de documentación del equipo: cada hueco identificado se transforma en un SOP nuevo o en una sección añadida a un SOP existente. Así, el uso real del notebook guía la mejora continua de la base de conocimiento.

---

## 9. GLOSARIO

**SOP (Standard Operating Procedure / Procedimiento Operativo Estándar):** Documento estructurado que describe cómo ejecutar un proceso de principio a fin de forma que cualquier persona competente pueda realizarlo sin depender de quien lo diseñó; incluye título, objetivo, responsable, pasos, excepciones y versión.

**Checklist:** Lista de verificación con casillas de comprobación que permite confirmar que se han completado todos los pasos de un proceso sin tener que leer el SOP completo; herramienta de control de calidad para tareas repetitivas.

**Flujo de trabajo (workflow):** Secuencia de pasos, decisiones y transferencias de responsabilidad que componen un proceso de trabajo; puede representarse como texto lineal (A → B → si C, D) o como diagrama visual.

**Cuello de botella:** Punto de un flujo de trabajo donde el proceso se ralentiza o se detiene porque depende de una sola persona, un recurso limitado o una decisión que no tiene tiempo límite definido.

**Convención de nombrado:** Conjunto de reglas acordadas para nombrar archivos y carpetas de forma coherente; incluye elementos como área, tipo de documento, descripción y fecha para facilitar la búsqueda y el orden.

**Google Forms:** Herramienta gratuita de Google para crear formularios de recogida de datos; cada respuesta se guarda automáticamente en Google Sheets cuando se activa la vinculación.

**Google Sheets vinculado:** Hoja de cálculo de Google conectada a un formulario de Google Forms que recibe automáticamente cada nueva respuesta como una fila nueva, creando un dataset actualizable sin intervención manual.

**Conocimiento tácito:** Conocimiento que existe en la mente de una persona a partir de su experiencia práctica pero que no está documentado en ningún lugar; cuando esa persona falta o cambia de puesto, el conocimiento se pierde o no es accesible para el equipo.

**Base de conocimiento:** Repositorio organizado de documentos, procedimientos y respuestas a preguntas frecuentes que permite a un equipo consultar información sin depender de una persona específica; NotebookLM puede funcionar como interfaz de consulta de una base de conocimiento.

**SLA (Service Level Agreement / Acuerdo de Nivel de Servicio):** Compromiso de tiempo de respuesta o resolución para una tarea o servicio; en procesos internos, establecer SLAs (por ejemplo, "respuesta en 48 horas") reduce los cuellos de botella y las esperas indefinidas.

**Trazabilidad:** Capacidad de seguir el historial de un proceso o decisión: quién hizo qué, cuándo y con qué resultado; los formularios de Google con respuesta a Sheets proporcionan trazabilidad automática de todos los registros.

**Automatización de bajo código:** Flujos de trabajo que automatizan tareas repetitivas sin necesidad de programar; Google Forms → Sheets es un ejemplo de automatización de bajo código accesible para cualquier usuario de oficina.

---

## 10. ERRORES COMUNES Y BUENAS PRÁCTICAS

**Error 1 — Documentar el proceso como debería ser, no como es realmente.** Un SOP escrito desde el despacho, sin consultar a quien realmente ejecuta el proceso, suele omitir los casos de excepción más frecuentes y las decisiones informales que se toman a diario. Describir primero el proceso real, aunque sea caótico, y luego mejorarlo al documentarlo.

**Error 2 — Crear un SOP demasiado largo que nadie lee.** Si el SOP tiene más de dos páginas, probablemente está documentando un proceso demasiado amplio o con demasiado detalle innecesario. Dividir procesos complejos en sub-procedimientos más cortos, cada uno con su propio SOP de una página.

**Error 3 — No versionar los SOPs.** Un SOP sin fecha ni número de versión es un documento huérfano: nadie sabe si está actualizado o si hay una versión más reciente en alguna carpeta. Añadir siempre la fecha de creación y la de última revisión en el pie de página o en la cabecera.

**Error 4 — Usar Google Forms sin vincular a Sheets.** El formulario sin vinculación a Sheets guarda las respuestas en Google, pero son difíciles de analizar o exportar. Siempre activar "Ver en Sheets" antes de distribuir el formulario, para asegurarse de que los datos son accesibles desde el primer momento.

**Error 5 — Confiar en que la IA ha documentado el proceso correctamente sin revisarlo.** La IA puede inferir pasos razonables a partir de una descripción, pero no conoce los detalles internos específicos de la organización: nombres de proveedores, sistemas propios, tiempos reales. Siempre revisar el SOP generado por la IA con quien ejecuta el proceso.

**Error 6 — Intentar automatizar decisiones que requieren criterio humano.** La automatización es adecuada para tareas repetitivas y predecibles. Las decisiones que tienen un impacto significativo en personas, las situaciones de excepción complejas y cualquier paso con consecuencias irreversibles deben mantenerse bajo supervisión humana.

**Buena práctica — Asignar un responsable de mantenimiento a cada SOP.** Un SOP sin responsable no se actualiza nunca. Asignar explícitamente quién revisa y actualiza cada procedimiento, y con qué frecuencia (por ejemplo, una revisión anual o cuando cambia el proceso).

**Buena práctica — Sustituir datos sensibles por marcadores antes de usar la IA.** Cuando se pega una descripción de proceso en ChatGPT, Claude o Gemini, conviene reemplazar nombres reales de personas, proveedores, importes y credenciales por marcadores genéricos ("Proveedor A", "Compañera responsable", "[IMPORTE]"). El SOP resultante se completa con los datos reales en local, dentro del Google Doc, sin que esa información haya pasado nunca por el chat.

**Buena práctica — Probar el SOP con un compañero antes de publicarlo.** Antes de subir el SOP a la base de conocimiento del equipo, conviene que una persona que no haya intervenido en su redacción lo siga paso a paso para ejecutar el proceso. Los huecos detectados en esa prueba (instrucciones ambiguas, pasos implícitos, decisiones no documentadas) se corrigen antes de la publicación oficial, evitando errores en el uso real.

---

## 11. ACTIVIDADES EN AULA

### Actividad 1 — Demo: de caos a SOP en tres prompts [Grupo · 20 min]

**Descripción:** El formador proporciona al grupo una descripción caótica e incompleta de un proceso administrativo ficticio (gestión de devoluciones de material defectuoso). En pantalla compartida, el grupo construye colectivamente los tres prompts —crear SOP, completar detalles y generar checklist— y observa en tiempo real cómo la IA transforma la descripción informal en un documento estructurado. Se dedican 5 minutos a identificar qué ha capturado bien la IA y qué necesita corrección humana.

**Objetivo:** Que el grupo vea el flujo completo de creación de SOP con IA antes de aplicarlo a sus propios procesos; y que desarrolle el ojo crítico para revisar lo que la IA genera.

**Material:** Descripción ficticia de proceso proporcionada por el formador (impresa o en pantalla), ChatGPT o Claude en versión gratuita.

---

### Actividad 2 — Mapear un proceso real en parejas [Pareja · 45 min]

**Descripción:** Cada pareja elige uno de sus procesos de trabajo reales (no otro del curso): puede ser la gestión de pedidos, el registro de facturas, la coordinación con un proveedor, la preparación de un informe periódico o cualquier otra tarea repetitiva. Describen el proceso actual en texto (15 min), lo comparten con la IA para identificar cuellos de botella y pasos sin responsable definido (20 min) y proponen al menos dos mejoras concretas basadas en el análisis de la IA (10 min). Al final, cada pareja escribe en un Post-it (físico o digital) cuál es el mayor problema que ha identificado en su flujo.

**Objetivo:** Aplicar el mapeo de flujo con IA a un proceso real de cada persona, con el apoyo de un compañero para completar los puntos ciegos.

**Material:** ChatGPT, Claude o Gemini en versión gratuita; papel o documento de Google para describir el flujo.

---

### Actividad 3 — Mi SOP individual [Individual · 30 min]

**Descripción:** Cada persona documenta uno de sus propios procedimientos como SOP completo (título, objetivo, responsable, pasos, excepciones, versión) usando IA como asistente de escritura. Tras crear el SOP, genera también la checklist de uso diario correspondiente. El criterio de calidad es: ¿podría un compañero nuevo ejecutar este proceso correctamente siguiendo solo este documento?

**Objetivo:** Que cada persona salga de la sesión con al menos un procedimiento propio documentado, listo para compartir con su equipo.

**Material:** ChatGPT, Claude o Gemini gratuito; Google Doc para editar y guardar el SOP.

---

## 12. 🔁 TRABAJO EN PAREJAS

En la **Actividad 2**, el grupo trabaja en **parejas** durante 45 minutos. La pareja tiene una dinámica específica: la primera persona describe su proceso mientras la segunda toma notas y hace preguntas de clarificación ("¿quién decide si el pedido se aprueba?", "¿qué pasa si el proveedor no responde en 24 horas?"). Después de 20 minutos, se intercambian los roles y se describe el proceso del segundo miembro. Esta dinámica de escucha activa es fundamental porque el externo siempre detecta huecos y asunciones implícitas que quien ejecuta el proceso no advierte porque las da por descontadas. Al final de la actividad, cada pareja comparte en la puesta en común el cuello de botella más significativo que identificó la IA en sus flujos y qué mejora proponen, generando un debate colectivo sobre patrones comunes de ineficiencia en procesos de oficina.

---

## 13. EJERCICIOS SUGERIDOS

Ver Banco de Ejercicios:
- **EJ-D14-1** (Individual): Documentar dos procedimientos propios como SOP completo + checklist, usando IA como asistente de escritura. Evaluación: ¿un compañero sin conocimiento previo podría seguirlos?
- **EJ-D14-2** (Pareja): Crear un formulario de Google Forms para un proceso de recogida de datos real del equipo (solicitudes, registros, encuestas), vincularlo a Google Sheets y diseñar con IA los campos óptimos para el análisis posterior.
- **EJ-D14-3** (Grupo): Subir tres SOPs del equipo a NotebookLM y probarlo como base de conocimiento: cada miembro del grupo hace cinco preguntas sobre los procedimientos y evalúa la calidad de las respuestas. Identificar qué información faltaba en los SOPs a partir de las preguntas que NotebookLM no pudo responder.

---

## 14. CUESTIONARIO DE AUTOEVALUACIÓN

**1. ¿Qué es un SOP y cuál es su propósito principal?**
a) Un software de gestión de proyectos
b) Un documento estructurado que describe cómo ejecutar un proceso para que cualquier persona competente pueda realizarlo sin depender de quien lo creó ✓
c) Un informe de análisis de datos de fin de trimestre
d) Una plantilla de correo electrónico para comunicaciones internas

**2. ¿Cuál es la ventaja de describir primero el proceso de forma informal antes de pasárselo a la IA para crear el SOP?**
a) La IA necesita texto informal para funcionar correctamente
b) La descripción informal captura los detalles reales, los casos de excepción y las decisiones informales que un SOP teórico omitiría ✓
c) La descripción informal ahorra tiempo en el prompt
d) No hay ventaja: es mejor pedirle a la IA que cree el SOP desde cero sin descripción previa

**3. ¿Cuál de estos elementos NO forma parte de un SOP completo?**
a) Título y objetivo
b) Pasos numerados y detallados
c) Nombre del proveedor del sistema de nóminas ✓
d) Excepciones y casos especiales

**4. ¿Qué prompt de seguimiento convierte un SOP en una checklist de uso diario?**
Respuesta abierta: Un ejemplo válido: "Genera una checklist de uso diario con casillas (☐), máximo 10 ítems, verbo en infinitivo, para que alguien pueda marcar cada paso mientras ejecuta el proceso sin necesitar leer el SOP completo."

**5. ¿Qué ocurre automáticamente cuando alguien rellena un formulario de Google Forms vinculado a Google Sheets?**
a) El formulario envía un correo al responsable
b) La respuesta aparece como una nueva fila en la hoja de cálculo vinculada, sin necesidad de copiar nada manualmente ✓
c) El formulario se cierra y bloquea nuevas respuestas
d) Los datos se guardan en Google Drive como un documento de texto

**6. ¿Cómo puede usarse NotebookLM como base de conocimiento de procedimientos?**
a) NotebookLM crea automáticamente SOPs a partir de conversaciones del equipo
b) Subiendo los SOPs como fuentes, los compañeros pueden hacer preguntas en lenguaje natural y NotebookLM busca la respuesta en los documentos subidos ✓
c) NotebookLM reemplaza a Google Drive como sistema de almacenamiento de documentos
d) NotebookLM envía recordatorios automáticos cuando un SOP necesita actualización

**7. ¿Cuál de estas tareas NO es adecuada para automatizar completamente sin supervisión humana?**
a) Registro de solicitudes de material en un formulario
b) Envío automático de confirmación de recepción de un formulario
c) Decisión de renovar o no el contrato de un trabajador ✓
d) Copia de respuestas de formulario a una hoja de cálculo

**8. ¿Qué es un cuello de botella en un flujo de trabajo?**
a) Un error en la configuración del formulario de Google
b) Un punto del proceso donde el avance se ralentiza o detiene, generalmente por depender de una sola persona o recurso sin tiempo límite definido ✓
c) Un documento SOP que tiene demasiadas páginas
d) Una tarea que no tiene SOP documentado

**9. ¿Cuál es la regla práctica para decidir si algo puede automatizarse sin supervisión humana en el paso final?**
Respuesta abierta: Si la pregunta "¿qué pasa si esto sale mal?" no tiene una respuesta simple y reversible, no se automatiza sin supervisión humana. Las tareas con consecuencias graves o irreversibles en caso de error requieren siempre confirmación humana consciente.

**10. Verdadero o falso: un SOP generado por IA puede usarse directamente sin revisión porque la IA conoce los procesos de la empresa.**
Respuesta: **Falso.** La IA genera la estructura y el formato del SOP a partir de la descripción que le damos, pero no conoce los detalles específicos internos de la organización: nombres de sistemas propios, proveedores, tiempos reales, personas responsables. Siempre hay que revisar el SOP con quien ejecuta el proceso antes de distribuirlo.

**11. ¿Por qué es importante asignar un responsable de mantenimiento a cada SOP?**
Respuesta abierta: Un SOP sin responsable asignado no se actualiza cuando cambia el proceso, lo que hace que quede obsoleto y deje de ser útil —o peor, que induzca a errores al seguir instrucciones desactualizadas. El responsable de mantenimiento revisa el procedimiento periódicamente y lo actualiza cuando el proceso cambia.

**12. ¿Cuál de estas convenciones de nombrado es más recomendable para una carpeta compartida de oficina?**
a) "Informe final v2 DEFINITIVO (1).docx"
b) "ADM_SOP_PedidoMaterial_2026-07-01.docx" ✓
c) "el documento de Marta nuevo.docx"
d) "Documento 7 - copia (3).docx"

**13. ¿Qué ventaja indirecta tiene la limitación de NotebookLM de responder solo sobre lo que está en sus fuentes?**
a) Hace que el equipo use más Google Drive
b) Reduce el coste de la herramienta para el equipo
c) Incentiva a documentar más y mejor, porque cada hueco detectado se convierte en un procedimiento por escribir ✓
d) Permite a la IA inventar respuestas cuando no encuentra información

**14. Marta quiere actualizar un SOP porque ha cambiado el sistema de pedidos. ¿Cuál es la forma correcta de proceder?**
Respuesta abierta: Abrir el SOP vigente en Google Docs, modificar los pasos afectados, actualizar la fecha y el número de versión en el pie de página y comunicar el cambio al responsable de mantenimiento y al resto del equipo. Si se usa IA, el prompt es: "Este SOP necesita actualización. El cambio es: [DESCRIBIR]. Modifica el SOP y actualiza la versión a la fecha de hoy."

**15. Verdadero o falso: para crear un SOP con IA es seguro pegar la descripción del proceso con los nombres reales de proveedores, importes y credenciales.**
Respuesta: **Falso.** En general, conviene sustituir nombres reales, importes concretos y credenciales por marcadores genéricos antes de pegar la descripción en el chat. Los datos reales se completan después, en local, dentro del Google Doc del SOP. Esa práctica evita filtraciones de información interna y suele estar exigida por la política de protección de datos de la organización.

---

## 15. PREGUNTAS FRECUENTES (FAQ)

**¿Tengo que saber redactar bien para crear un SOP con IA?**
No. Precisamente ese es el punto: puedes describir el proceso de forma informal, como si se lo explicaras a alguien por teléfono, con interrupciones y saltos entre ideas. La IA se encarga de estructurarlo, ordenarlo y darle formato. Tú revisas que el contenido sea correcto; la IA se ocupa de la forma.

**¿Qué hago si la IA inventa pasos que no existen en mi proceso real?**
Es habitual. La IA puede inferir pasos razonables a partir de la lógica del proceso, aunque tú no los hayas mencionado. Algunos pueden ser correctos y útiles; otros pueden ser incorrectos para tu contexto específico. Por eso la revisión es imprescindible. Señala al asistente qué pasos son incorrectos: "El paso 3 no es así en nuestra empresa. El proceso real es: [DESCRIPCIÓN CORRECTA]. Corrígelo."

**¿Cómo puedo compartir el SOP con mi equipo sin que se pierda entre carpetas?**
Varias opciones: guardarlo en una carpeta compartida de Google Drive con nombre siguiendo la convención acordada; añadirlo como fuente en el notebook de NotebookLM del equipo; o crear un Google Doc compartido con la lista de todos los SOPs disponibles y los enlaces a cada uno. La clave es que la ubicación sea conocida por todo el equipo y esté acordada de antemano.

**¿Puedo pegar el SOP en NotebookLM y pedirle que lo mejore?**
Sí, es un uso muy válido. NotebookLM puede analizar el SOP y señalar secciones ambiguas, pasos que falta detallar o situaciones de excepción no contempladas. También puede usarse para generar preguntas de comprensión que ayuden a verificar que quien lee el SOP lo ha entendido correctamente.

**¿Google Forms es suficientemente seguro para datos internos de empresa?**
Google Forms almacena los datos en Google Drive de la cuenta que crea el formulario, lo que generalmente cumple los estándares de seguridad para datos internos no especialmente sensibles. Para datos personales de empleados o datos confidenciales protegidos por RGPD, consultar con el responsable de protección de datos de la organización antes de usar Google Forms para recogerlos.

**¿Cuántos SOPs debería tener documentados un departamento de administración?**
No hay un número mínimo universal. Un criterio práctico: documentar primero los procesos que tienen mayor impacto si fallan, los que dependen de una sola persona y los que se repiten con más frecuencia. Empezar con 3–5 SOPs de los procesos más críticos y crecer progresivamente. Demasiados SOPs mal mantenidos son peores que pocos SOPs bien actualizados.

**¿La checklist puede usarse en papel o solo en digital?**
Puede usarse en cualquier formato. Para tareas de verificación rápida en entornos con mucho movimiento físico (almacén, recepción), la versión impresa con casillas para marcar con bolígrafo es perfectamente válida. Google Docs también permite crear listas de verificación interactivas con casillas que se pueden marcar desde el ordenador o el móvil.

**¿Cómo actualizo un SOP cuando cambia el proceso?**
La forma más eficiente es volver al SOP en Google Docs, hacer los cambios necesarios (añadir, eliminar o modificar pasos) y actualizar la fecha de versión en el pie de página. Si usas IA para la actualización, el prompt es: "Este SOP necesita actualización. El cambio es: [DESCRIBIR EL CAMBIO]. Modifica el SOP para reflejar el nuevo procedimiento y actualiza la versión a la fecha de hoy."

**¿Por dónde empiezo si en mi oficina no hay nada documentado todavía?**
Empezar por el proceso que más te cuesta delegar cuando te ausentas, o el que más errores genera en el equipo. Documentar uno solo, con detalle y revisión, y comprobar en uso real que funciona. A partir de ese primer SOP, en general resulta más fácil convencer al equipo de seguir documentando porque ya hay un ejemplo concreto del beneficio. Crear veinte SOPs a la vez suele acabar con veinte documentos a medio terminar.

**¿Puedo usar la IA para escribir el SOP sobre un proceso que aún no domino del todo?**
Es posible, pero no recomendable como flujo principal. La IA solo puede estructurar y ordenar lo que tú le describes; no puede inventar conocimiento que tú no tienes. Si describes un proceso que entiendes a medias, el SOP resultante tendrá huecos o errores que la IA no detectará. Mejor entrevistar primero a quien sí domina el proceso, tomar notas y luego usar la IA para estructurarlas en formato SOP.

---

## 16. HERRAMIENTAS DE LA SESIÓN

- **ChatGPT** (chat.openai.com) — Cuenta gratuita; creación de SOPs, checklists, análisis de flujos, diseño de formularios con IA.
- **Claude** (claude.ai) — Cuenta gratuita; especialmente eficaz para tareas de escritura estructurada y revisión de documentos largos.
- **Google Gemini** (gemini.google.com) — Cuenta gratuita con Gmail; alternativa integrada con el ecosistema de Google.
- **Google Forms** (forms.google.com) — Gratuito con cuenta Gmail; creación de formularios de recogida de datos sin necesidad de programación.
- **Google Sheets** (sheets.google.com) — Gratuito con cuenta Gmail; destino automático de las respuestas de Google Forms; análisis de datos.
- **Google Docs** (docs.google.com) — Gratuito con cuenta Gmail; edición colaborativa de SOPs y checklists.
- **NotebookLM** (notebooklm.google.com) — Gratuito con cuenta Gmail; base de conocimiento consultable a partir de SOPs y procedimientos subidos como fuentes.

Ver el mapa completo en `Recursos/Herramientas_Gratuitas.md`.

---

## 17. MINI-ENTREGABLE DEL DÍA

**Nombre:** Mi SOP y checklist de procedimiento propio
**Formato:** Google Doc compartido o PDF exportado (1–2 páginas)
**Contenido:** Un SOP completo de un procedimiento real del puesto propio (título, objetivo, responsable, pasos numerados, excepciones, versión y fecha) más la checklist de uso diario correspondiente (máximo 10 ítems con casillas de verificación). El documento debe incluir también un campo "Pendiente de revisar" con al menos una mejora identificada durante el mapeo del flujo.
**Cómo alimenta el proyecto final:** Si el proyecto final implica mejorar o describir un proceso de trabajo, el SOP de hoy puede ser el componente de documentación del proyecto. El flujo Forms → Sheets puede ser la infraestructura de recogida de datos del proyecto. Ambos son entregables directamente incorporables al proyecto final de D16.

---

## 18. 🎓 HILO DEL PROYECTO FINAL

Para tu proyecto final: si tu solución implica sistematizar un proceso, el SOP y la checklist de hoy son el núcleo de ese entregable. Si implica recoger datos de forma estructurada, el formulario de Google Forms vinculado a Sheets es la infraestructura que necesitas. Y si quieres que tu equipo pueda consultar los procedimientos de forma autónoma, NotebookLM como base de conocimiento puede ser el componente de difusión de tu proyecto.

---

## 19. MENSAJE CLAVE DE LA SESIÓN

> "El conocimiento que vive solo en la cabeza de una persona es un riesgo para el equipo. Documentar no es burocracia: es la forma más eficiente de que tu criterio profesional escale sin ti."

---

## 20. IDEAS PARA RECORDAR

- El conocimiento tácito no documentado es frágil: cuando la persona que lo posee falta, el equipo se detiene. Documentar es un acto de solidaridad profesional además de eficiencia.
- La IA elimina la parte más costosa de documentar —la escritura— y la convierte en una revisión de diez minutos a partir de una descripción informal.
- Google Forms + Sheets es la automatización de bajo código más accesible para cualquier persona de oficina: sin programación, sin costes, con datos organizados desde el primer registro.
- Un SOP sin fecha ni responsable de mantenimiento se vuelve obsoleto en meses y genera más confusión que su ausencia. Versionar siempre.
- NotebookLM como base de conocimiento convierte los SOPs en una asistencia consultable: cualquier compañero puede preguntar "¿cómo se hace X?" y obtener la respuesta de los documentos del equipo, no de la memoria de nadie.
- Antes de pegar una descripción en la IA, sustituye nombres reales, importes y credenciales por marcadores: el SOP se completa con los datos reales en local, dentro del documento del equipo.
- No se automatizan las decisiones con impacto en personas ni las acciones irreversibles: si la pregunta "¿qué pasa si esto sale mal?" no tiene respuesta simple y reversible, el paso final lo confirma siempre una persona.

---

## 21. CONEXIÓN CON EL RESTO DEL CURSO

D14 abre el Módulo 7, el penúltimo del curso, dedicado a flujos de trabajo y documentación. Es una sesión bisagra: llega cuando el grupo ya tiene sólidos fundamentos de redacción con IA (M2–M3), organización del tiempo (M4), análisis de datos (M5) y diseño visual (M6). Todo ese conocimiento converge aquí: la escritura estructurada de SOPs usa los prompts de M2–M3; los flujos de datos con Forms → Sheets conectan con el análisis de D10; los materiales visuales de D13 pueden incluirse en los SOPs como capturas de pantalla o diagramas. En **D15** (mañana), el módulo continúa con búsqueda de información avanzada y síntesis de mercado, que complementa la documentación interna de hoy con la inteligencia externa. Todo el trabajo de D14 alimenta directamente el proyecto final de D16, donde cada alumno presentará su solución completa con documentación, datos y comunicación.

---

## 22. FOOTER

*Brief para NotebookLM · D14 · Edición 01/26 — IA en la Oficina*
