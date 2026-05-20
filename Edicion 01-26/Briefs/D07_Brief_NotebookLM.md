# BRIEF PARA NOTEBOOKLM — D07
## Módulo 3, Sesión 4 de 4: Redacción de informes con IA
## Curso: IA en la Oficina – Eficiencia y Productividad
## Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital

**Fecha:** Jueves 9 de julio de 2026 · 15:00–19:00 h · Día 7 de 17

---

## 2. CONTEXTO DEL CURSO

**Programa:** IA en la Oficina – Eficiencia y Productividad (68 horas · 17 sesiones de 4 horas)
**Público:** Personal administrativo y de oficina sin experiencia previa en IA generativa. Perfiles muy diversos: administración, atención al cliente, contabilidad, logística, recursos humanos.
**Metodología:** ~40 % teoría y demostración · ~50 % práctica guiada · ~10 % puesta en común
**Sesión anterior (D06):** El grupo tiene su banco de plantillas de correo y domina la adaptación de tono para situaciones difíciles. Cierra el Módulo 3 con esta sesión dedicada a informes.

> *Este documento es la fuente del notebook de hoy. Además de las diapositivas, puedes pedirle a NotebookLM un resumen en **audio** (tipo pódcast), un **vídeo**, una **infografía** o mapa mental, una **guía de estudio**, **fichas** (flashcards), un **cuestionario** para autoevaluarte, o **escribir tus preguntas en el chat**. Usa el formato con el que mejor aprendas. No escribas datos personales reales en el chat.*

---

## 3. RESUMEN DE LA SESIÓN

Hoy el grupo aprende a construir un informe completo con IA usando un flujo de cuatro pasos que evita los errores más frecuentes: empezar a escribir sin índice, redactar el resumen ejecutivo antes de tener el cuerpo, y mezclar tonos de distintas secciones sin darse cuenta. La sesión aborda también la adaptación del mismo informe a tres audiencias diferentes —equipo técnico, dirección y cliente externo— que es una de las tareas que más tiempo consume y donde la IA aporta más valor. Por último, se trabajan las tres reglas para evitar que el informe contenga datos inventados, lo que en un documento que se entrega a externos puede tener consecuencias serias. Al finalizar, cada alumno tiene un informe corto real en tres versiones, listo para ser entregado a quien corresponda.

---

## 4. ESTRUCTURA DE LA SESIÓN (240 min)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| Apertura | 15 min | Repaso D06 + objetivos del día |
| Teórico-demostrativo | 75 min | Flujo de 4 pasos · Adaptación a 3 audiencias · Consistencia de estilo · Alucinaciones en informes |
| Descanso | 15 min | — |
| Práctica guiada | 95 min | Informe en 4 iteraciones · Adaptar a 3 públicos · Revisión cruzada en parejas |
| Puesta en común | 40 min | Comparativa de versiones + mini-entregable + cierre del módulo |

*(15+75+15+95+40 = 240 min)*

---

## 5. OBJETIVOS DE APRENDIZAJE

1. Construir un informe completo con IA usando el flujo de cuatro pasos: índice → secciones → resumen ejecutivo → revisión de coherencia.
2. Adaptar el mismo contenido a tres audiencias distintas: técnica, directiva y cliente externo.
3. Mantener coherencia de estilo a lo largo de un documento extenso mediante instrucciones explícitas en cada prompt.
4. Detectar y eliminar alucinaciones antes de publicar o entregar cualquier informe.

---

## 6. DESARROLLO TEÓRICO EN PROSA

### El informe como herramienta de decisión

Marta tiene que preparar el informe mensual de incidencias logísticas para la reunión del comité de dirección del viernes. Normalmente empieza a escribir directamente, sección por sección, hasta que llega al resumen ejecutivo y se da cuenta de que no encaja bien con el cuerpo. Relee todo, ajusta, cambia el orden de dos párrafos y al final dedica a ese informe entre tres y cuatro horas. Esta semana ha decidido probarlo de otra manera.

Un informe no es solo un documento: es una decisión esperando ser tomada. El informe de incidencias logísticas no existe para informar, existe para que dirección decida si el proveedor actual sigue siendo viable, si hay que ampliar el almacén intermedio o si la ruta de distribución norte necesita una revisión. Si el informe no lleva al lector a esa decisión de forma clara, está mal escrito aunque sea impecable gramaticalmente. La IA puede ayudar a construir el andamiaje del informe —estructura, tono, coherencia— pero el criterio sobre qué decisiones hay que facilitar sigue siendo de Marta.

> **Puntos clave:**
> - Un informe no informa: facilita una decisión concreta; si el lector no sabe qué decidir, el informe está mal enfocado
> - La IA construye el andamiaje (estructura, tono, coherencia); el criterio sobre qué decisiones facilitar es del autor
> - Marta pasa de 3-4 horas a 45-60 min con el flujo de 4 pasos + verificación manual

### El flujo de cuatro pasos para construir un informe con IA

El error más común al escribir informes con IA es empezar por "escríbeme un informe sobre X". El resultado es un texto genérico, desordenado y sin el nivel de detalle que requiere la situación real. El flujo de cuatro pasos evita ese error.

**Paso 1: genera el índice primero.** Antes de escribir una sola línea del informe, se le pide a la IA que proponga la estructura. Este paso obliga a pensar en qué debe contener el informe antes de empezar a redactarlo, y el índice generado por la IA suele hacer aflorar secciones que no se habían considerado.

El prompt para el índice:
> "Propón un índice para un informe de [tipo] sobre [tema]. Público: [destinatario]. Extensión: [X páginas]. Entre 4 y 6 secciones. Incluye una frase de descripción del contenido de cada sección."

Marta lo usa así para el informe de incidencias: "Propón un índice para un informe mensual de incidencias logísticas. Público: comité de dirección. Extensión: 2 páginas. Entre 4 y 6 secciones." La IA le devuelve un índice con introducción, análisis de incidencias por categoría, tendencias detectadas, conclusiones y recomendaciones. Marta ajusta un par de nombres de sección y ya tiene el esqueleto.

**Paso 2: desarrolla cada sección por separado.** Una vez aprobado el índice, se trabaja sección por sección en conversaciones separadas o en el mismo hilo. La clave es dar a la IA toda la información relevante para cada sección, sin mezclar contenidos de otras secciones en el mismo prompt.

El prompt para cada sección:
> "Redacta la sección '[nombre de la sección]' para un informe de incidencias logísticas. Contexto: [datos de la sección]. Tono: formal y directo. Extensión: [X palabras]. No repitas información de las otras secciones del informe."

La instrucción "no repitas información de otras secciones" es importante: la IA tiende a recapitular lo dicho anteriormente, lo que alarga el informe sin añadir valor.

**Paso 3: genera el resumen ejecutivo al final, nunca al principio.** Este es el error conceptual más frecuente en la redacción de informes: escribir el resumen antes de tener el cuerpo. Un resumen ejecutivo solo puede resumir lo que ya existe. Si se escribe antes, resume lo que uno imagina que va a escribir, y esa disonancia entre el resumen y el cuerpo es la que hace que los informes parezcan inconsistentes.

El prompt para el resumen ejecutivo:
> "Usando el contenido de todas las secciones del informe que hemos redactado, genera un resumen ejecutivo de máximo 150 palabras para un lector con 2 minutos disponibles. Debe incluir: el objetivo del informe en una frase, los tres hallazgos principales y la recomendación prioritaria."

Marta genera este resumen en el cuarto paso, no en el primero. El resultado es un párrafo que realmente refleja lo que dice el informe, no lo que Marta pensaba que iba a decir cuando empezó a escribirlo.

**Paso 4: revisión de coherencia.** Después de ensamblar todas las secciones y el resumen ejecutivo, el informe pasa por una revisión de coherencia. La IA detecta contradicciones entre secciones, cambios de tono no intencionales y referencias cruzadas que no encajan.

El prompt de revisión:
> "Revisa el siguiente informe completo para asegurar coherencia de tono y contenido. Señala: (1) contradicciones entre secciones, (2) cambios de registro o tono no intencionales, (3) datos o afirmaciones que no estén respaldados por la información proporcionada. [PEGAR INFORME ANONIMIZADO]"

> **Puntos clave:**
> - Paso 1: índice primero (nunca empezar a escribir sin estructura aprobada)
> - Paso 2: secciones por separado, cada una con sus datos específicos en el prompt
> - Paso 3: resumen ejecutivo al final, nunca al principio; Paso 4: revisión de coherencia

### Adaptación a tres audiencias: el mismo informe, tres versiones

Una de las tareas que más tiempo consume en un perfil administrativo es adaptar el mismo informe a diferentes destinatarios. El informe técnico de incidencias logísticas que necesita el equipo de operaciones no es el mismo que necesita ver la dirección, y ninguno de los dos es adecuado para enviar al cliente externo que pregunta por sus pedidos afectados.

Sin IA, adaptar un informe técnico a versión ejecutiva y versión para cliente puede llevar entre 45 minutos y hora y media, dependiendo de la extensión y la complejidad. Con IA, el mismo proceso toma entre 8 y 12 minutos.

Las tres versiones tienen características bien diferenciadas:

La **versión técnica** está dirigida al equipo técnico, a auditoría o a quien tiene que ejecutar o revisar los procesos. Su tono es preciso y detallado, usa la terminología específica del sector sin explicaciones, incluye datos numéricos con contexto y señala los pasos técnicos necesarios con claridad. No simplifica ni suaviza: quien la lee tiene la formación para entender los detalles.

La **versión ejecutiva** está dirigida a dirección o gerencia. Solo incluye conclusiones, decisiones necesarias y próximos pasos. No explica el proceso, no detalla la metodología y elimina cualquier dato que no sea relevante para tomar una decisión. La regla de oro de la versión ejecutiva es que cualquier persona que la lea en dos minutos debe poder contestar a la pregunta: "¿qué hay que decidir y por qué?".

La **versión para cliente** está pensada para el cliente final, el socio externo o cualquier destinatario no experto en los procesos internos de la empresa. Usa lenguaje accesible, sin jerga, orientado a los beneficios y al impacto que tiene para esa persona específica. Puede omitir información técnica que no es relevante para el cliente, y debe responder a la pregunta que el cliente en realidad se hace: "¿qué significa esto para mí?".

El prompt de adaptación:
> "Adapta el siguiente informe a una versión [técnica / ejecutiva / para cliente]. El destinatario es [descripción]. Ajusta el tono, el nivel de detalle y el vocabulario para ese público. Mantén todos los datos relevantes para ese destinatario y elimina los que no lo sean. [PEGAR TEXTO ANONIMIZADO]"

Se trabaja cada versión en un prompt separado, no todas en el mismo. Pedir las tres versiones a la vez tiende a generar resultados menos precisos porque la IA no puede ajustar el foco a las tres audiencias simultáneamente.

> **Puntos clave:**
> - Versión técnica: terminología precisa, detalles metodológicos, datos completos
> - Versión ejecutiva: solo conclusiones + decisiones + próximos pasos (test: ¿se puede decidir en 2 min?)
> - Versión para cliente: lenguaje accesible, cero jerga, orientado al "¿qué significa esto para mí?"

### Cómo evitar alucinaciones en informes que se entregan a externos

Un informe interno con una fecha incorrecta puede causar confusión. Un informe que se entrega a un cliente con una estadística inventada, una normativa que no existe o un dato financiero equivocado puede tener consecuencias mucho más serias: pérdida de confianza, reclamaciones, problemas legales.

Las alucinaciones son el mayor riesgo cuando se usa IA para redactar documentos formales, y más cuando esos documentos salen de la empresa. La IA no distingue entre datos que tú le has dado y datos que está generando por su cuenta: los presenta todos con el mismo nivel de confianza.

Hay tres reglas que eliminan casi completamente ese riesgo.

La **primera regla** es una instrucción fija que Marta incluye en todos los prompts de redacción de informes: "Usa únicamente la información que te proporciono a continuación. No añadas datos, estadísticas, normativas ni ejemplos externos que no estén en el material que te doy." Esta instrucción no elimina al cien por cien las alucinaciones, pero las reduce drásticamente.

La **segunda regla** es la verificación manual de todos los datos concretos antes de entregar el informe: fechas, cifras, nombres de personas y organizaciones, referencias normativas, porcentajes. Estos datos no se confían a la IA: se comprueba cada uno en la fuente original.

La **tercera regla** se aplica especialmente cuando el informe cita normativas, estadísticas del sector o datos de contexto general: el **prompt de auditoría de datos**.

El prompt de auditoría:
> "Lista todos los datos concretos que has incluido en el informe (cifras, fechas, normativas, estadísticas, nombres de organizaciones). Para cada uno, indica: (1) si viene de la información que te proporcioné o (2) si lo has añadido por tu cuenta a partir de tu entrenamiento. Señala cuáles necesitan verificación externa."

Si la IA responde que ha añadido por su cuenta una estadística, una ley o un dato de contexto que no estaba en el material de partida, ese dato se verifica antes de incluirlo. Si no se puede verificar, no se incluye.

La señal de alarma más importante es cuando la IA cita una ley, un reglamento o una estadística con gran precisión (número de ley, porcentaje exacto, año) que Marta no recuerda haber incluido en su material. Esa precisión no es garantía de exactitud: al contrario, cuanto más específico suene el dato no verificado, más sospechoso debe resultar.

> **Puntos clave:**
> - Instrucción fija: "Usa únicamente la información que te proporciono; no añadas datos externos"
> - Verificación manual de todos los datos concretos antes de entregar a externos
> - Señal de alarma: cifra muy precisa (decimales, número de ley, fecha exacta) no incluida en el material de partida

### La consistencia de estilo entre secciones redactadas en distintos momentos

Uno de los problemas menos visibles de los informes construidos sección por sección es la inconsistencia de estilo: la introducción tiene un tono formal y académico, la sección de análisis es más coloquial, y las conclusiones vuelven a ser formales. Esto ocurre porque cada sección se redactó en un prompt distinto, a veces con días de diferencia, y sin instrucciones explícitas de tono en cada uno. El resultado es un informe que parece escrito por varias personas, o que da la sensación de que algunas partes se copió y pegó de otra fuente. La solución es doble: incluir siempre la instrucción de tono y registro en cada prompt de sección ("Tono: formal, directo, sin metáforas. Registro: técnico-administrativo"), y usar el prompt de revisión de coherencia del paso 4 para detectar y corregir las inconsistencias que hayan escapado. Marta añadió a su plantilla de índice reutilizable una nota al inicio: "Estilo unificado para todas las secciones: tono formal, frases cortas, vocabulario de administración y logística, sin tecnicismos de otros sectores." Esa nota la pega al inicio de cada prompt de sección y el informe queda homogéneo desde el primer borrador.

> **Puntos clave:**
> - Incluir la instrucción de tono en cada prompt de sección, no solo en el primero
> - El paso 4 (revisión de coherencia) detecta los cambios de registro no intencionales entre secciones
> - Una nota de estilo al inicio del índice reutilizable garantiza homogeneidad sin esfuerzo adicional

### El criterio profesional como capa irremplazable sobre el borrador de IA

La IA genera borradores de informes de alta calidad formal, pero hay una dimensión que no puede aportar: el criterio profesional de quien conoce el contexto real. Marta sabe que el proveedor logístico del norte lleva tres meses con problemas de capacidad porque contrató a un nuevo cliente grande, y que eso afecta directamente a los plazos del primer trimestre del año que viene. Ese contexto no está en ningún prompt y no lo puede saber la IA. Un informe generado sin ese contexto puede ser formalmente correcto pero estratégicamente incompleto. La regla práctica es la siguiente: después de generar cada sección con IA, releer con la pregunta "¿qué sé yo sobre esta situación que la IA no puede saber?" y añadir manualmente los matices relevantes. Esos añadidos son el valor diferenciador del informe: la experiencia, el contexto histórico y las señales débiles que ninguna herramienta de IA puede detectar porque no estuvieron en ninguna reunión, en ningún pasillo ni en ningún correo anterior.

> **Puntos clave:**
> - La IA aporta estructura y forma; el autor aporta el contexto que no está en ningún prompt
> - Preguntar tras cada sección: "¿qué sé yo que la IA no puede saber?" y añadirlo manualmente
> - Los matices estratégicos, las señales débiles y el historial relacional son irremplazables por IA

### Informes recurrentes: plantillas de índice como activo reutilizable

Muchos informes en una empresa son recurrentes: el informe mensual de incidencias, el informe trimestral de actividad, el informe de cierre de proyecto, el informe de seguimiento presupuestario. Cada uno sigue siempre la misma estructura, con variaciones solo en los datos. Una vez que se ha construido y validado el índice de un tipo de informe, ese índice se convierte en una plantilla reutilizable que elimina el paso 1 del flujo en todos los informes siguientes del mismo tipo. Marta tiene ya tres plantillas de índice guardadas en su Google Doc de biblioteca de prompts: la del informe mensual de incidencias, la del informe trimestral de actividad y la del resumen ejecutivo de reunión de proveedores. Cada vez que tiene que preparar uno de esos informes, abre la plantilla correspondiente, rellena los datos del mes actual en los prompts de sección, y el paso 1 ya está hecho. Con el tiempo, las plantillas de índice se convierten en el activo más valioso de su flujo de trabajo con IA: garantizan consistencia entre informes del mismo tipo, reducen el tiempo de inicio y producen documentos que los destinatarios reconocen y saben leer de un mes para otro.

> **Puntos clave:**
> - Cada tipo de informe recurrente debe tener su plantilla de índice guardada en la biblioteca de prompts
> - La plantilla elimina el paso 1 del flujo en todos los informes siguientes del mismo tipo
> - Informes con índice consistente mes a mes son más fáciles de leer: el destinatario ya sabe dónde buscar

### Cómo integrar datos de tablas y hojas de cálculo en el informe

Una fuente habitual de información para los informes administrativos son las hojas de cálculo: ventas por zona, incidencias por tipo, evolución de costes. Integrar esos datos en el texto narrativo del informe es una de las tareas más tediosas: pasar de una tabla de números a un párrafo que los explica e interpreta puede llevar tanto tiempo como redactar el resto del informe. La IA hace esta traducción en segundos. El flujo es el siguiente: se copian los datos clave de la hoja de cálculo (solo los relevantes para esa sección, no toda la tabla), se pegan en el prompt junto con las instrucciones de redacción, y la IA genera el párrafo narrativo que los integra. El prompt es: "Describe en prosa los siguientes datos de tabla como si fueran el párrafo de análisis de un informe mensual. Destaca la tendencia principal, la variación más significativa y el dato más relevante para la decisión. No inventes datos adicionales. [DATOS DE LA TABLA]." La clave, como siempre, es verificar que los números del párrafo generado coinciden exactamente con los de la tabla original antes de incluirlo en el informe final.

> **Puntos clave:**
> - Pegar solo los datos relevantes de la tabla, no toda la hoja: la IA trabaja mejor con foco limitado
> - El prompt pide destacar tendencia principal, variación más significativa y dato más relevante para decidir
> - Verificar siempre que los números del párrafo generado coinciden con los de la tabla original

---

## 7. DATOS Y CIFRAS CLAVE

- Adaptar un informe técnico a versión ejecutiva y versión para cliente con IA: 8–12 minutos. Sin IA: entre 45 y 90 minutos.
- El flujo de 4 pasos (índice → secciones → resumen → coherencia) reduce a la mitad el tiempo de redacción de informes de más de 2 páginas respecto a escribir de manera lineal.
- Escribir el resumen ejecutivo al principio en lugar de al final es el error más frecuente en informes con IA: genera disonancia entre el resumen y el cuerpo que luego cuesta hasta 30 minutos corregir.
- Antes / Después: informe mensual de 2 páginas → antes: 3–4 horas; con flujo de 4 pasos + IA: 45–60 minutos (incluyendo revisión manual de datos).
- Antes / Después: adaptar informe técnico a 3 versiones → antes: 45–90 min; con IA: 8–12 min.
- El 100 % de los datos concretos de un informe externo (fechas, cifras, normativas) deben verificarse manualmente independientemente de que los haya generado la IA.
- Un informe que llega al destinatario con un dato incorrecto requiere en promedio 2 correcciones y 1 reunión de aclaración adicional para recuperar la confianza.
- Informes recurrentes con plantilla de índice reutilizable: el paso 1 del flujo ya está hecho; tiempo de inicio reducido a cero en el segundo informe del mismo tipo.

---

## 8. EJEMPLOS RESUELTOS PASO A PASO

### Caso 1 — Construir el índice de un informe de cierre mensual

**Situación:** Marta tiene que preparar el informe de cierre de gastos del mes de junio para el departamento de administración. Normalmente empieza a escribir sin estructura y el informe le queda desequilibrado: una sección muy larga, otra con cuatro líneas.

**Prompt exacto:**
> "Propón un índice para un informe mensual de cierre de gastos. Público: responsable de administración y dirección financiera. Extensión: 2 páginas. Entre 4 y 6 secciones. Incluye una frase de descripción del contenido de cada sección. El informe debe permitir tomar decisiones sobre desviaciones respecto al presupuesto."

**Resultado comentado:** La IA propone un índice con resumen ejecutivo, análisis de gastos por categoría, comparativa con presupuesto, desviaciones y causas, y recomendaciones. Marta elimina una sección que no aplica a su empresa y ajusta el nombre de otra. Tiene el esqueleto del informe en dos minutos.

**Cómo iterarlo:** *"La sección de 'Desviaciones y causas' es demasiado genérica. Subdivídela en desviaciones por encima del 10 % y desviaciones menores, con columnas distintas en la tabla."*

---

### Caso 2 — Adaptar el mismo informe a dirección y a un proveedor externo

**Situación:** Marta tiene un informe técnico de tres páginas sobre problemas de entrega con un proveedor logístico. Necesita una versión corta para presentar a dirección y una versión distinta para enviar al propio proveedor como parte de la reclamación formal.

**Prompt para la versión ejecutiva:**
> "Adapta el siguiente informe a una versión ejecutiva de máximo media página. El destinatario es la dirección general de la empresa, que tiene 3 minutos para leerlo y necesita saber: qué ha pasado, cuál es el impacto económico y qué decisión se propone. Elimina los detalles técnicos del proceso logístico. [TEXTO ANONIMIZADO]"

**Prompt para la versión al proveedor:**
> "Adapta el mismo informe a una comunicación formal dirigida al proveedor logístico. El objetivo es documentar los incumplimientos del contrato y solicitar un plan de acción. Tono: firme y profesional, basado en hechos, sin expresiones emocionales. Incluye una tabla con las incidencias, fechas y impacto. [TEXTO ANONIMIZADO]"

**Resultado comentado:** Las dos versiones parten del mismo contenido pero tienen extensión, estructura y tono completamente distintos. La versión ejecutiva es un párrafo y una propuesta de decisión. La versión al proveedor es un documento estructurado con evidencias. Marta habría tardado entre una y dos horas en escribir ambas desde cero; con IA las tiene en diez minutos.

**Cómo iterarlo:** Para la versión ejecutiva: *"Añade un párrafo de riesgo: qué pasa si no se toma la decisión esta semana."* Para la versión al proveedor: *"La tabla de incidencias está bien pero falta una columna con el coste estimado de cada incidencia para la empresa."*

---

### Caso 3 — Auditar un informe para detectar datos no verificados

**Situación:** La IA ha generado la sección de contexto de mercado para un informe que Marta va a enviar a un cliente. El texto cita un porcentaje de crecimiento del sector y una normativa comunitaria que Marta no recuerda haber incluido en su material de partida.

**Prompt exacto:**
> "Lista todos los datos concretos que aparecen en la siguiente sección del informe: cifras, porcentajes, fechas, nombres de normativas o leyes, estadísticas de mercado. Para cada dato, dime si viene de la información que yo te proporcioné al principio o si lo añadiste por tu cuenta desde tu entrenamiento. Marca con ⚠️ los que necesitan verificación externa antes de publicar. [TEXTO DE LA SECCIÓN]"

**Resultado comentado:** La IA identifica que el porcentaje de crecimiento y la referencia normativa los añadió por su cuenta. Marta elimina el porcentaje porque no puede verificarlo a tiempo, y busca la normativa citada en el BOE antes de incluirla. El informe sale sin datos no verificados.

**Cómo iterarlo:** Si la IA no señala claramente el origen de cada dato: *"Respóndeme en formato tabla: columna 1 el dato, columna 2 si viene de mi material (SÍ/NO), columna 3 si necesita verificación (SÍ/NO)."*

---

### Caso 4 — Integrar datos de una hoja de cálculo en el texto del informe

**Situación:** Marta tiene una tabla con las incidencias de entrega del mes de junio: 23 incidencias por zona norte, 8 por zona sur, 14 por zona centro. La variación respecto a mayo es del +47 % en la zona norte. Tiene que convertir estos datos en el párrafo de análisis de la sección "Distribución de incidencias por zona" del informe mensual.

**Prompt exacto:**
> "Describe en prosa los siguientes datos de tabla como si fueran el párrafo de análisis de la sección 'Distribución de incidencias por zona' de un informe mensual para el comité de dirección. Destaca la tendencia principal (zona norte), la variación más significativa respecto al mes anterior (+47 %) y lo que eso puede implicar para la gestión del mes siguiente. Tono: formal, directo. Máximo 80 palabras. No añadas datos que no estén en los que te proporciono. DATOS: Zona norte: 23 incidencias (mayo: 14, variación: +47 %); zona sur: 8 incidencias (mayo: 9, variación: -11 %); zona centro: 14 incidencias (mayo: 15, variación: -7 %)."

**Resultado comentado:** La IA genera un párrafo que integra los datos, destaca que la zona norte concentra el 51 % de las incidencias del mes y que su variación del +47 % es la más significativa, y señala que merece atención prioritaria en el mes siguiente. Marta verifica que los números del párrafo coinciden exactamente con su tabla y lo incluye en el informe.

**Cómo iterarlo:** Si Marta quiere añadir una hipótesis sobre la causa del incremento en la zona norte: "Añade una frase que mencione que el incremento puede estar relacionado con el cambio de proveedor de transporte en esa zona durante el mes de junio, sin presentarlo como certeza sino como hipótesis a verificar."

---

## 9. GLOSARIO

**Informe ejecutivo (resumen ejecutivo):** Sección inicial del informe que resume en máximo 150 palabras los hallazgos principales y la recomendación prioritaria, pensada para lectores con poco tiempo disponible. Se redacta siempre al final, cuando el cuerpo del informe ya está completo.

**Índice de informe:** Estructura jerárquica de secciones que define el andamiaje del informe antes de redactar ninguna. Generarlo primero con IA evita desequilibrios de contenido y olvidos de secciones importantes.

**Versión técnica:** Variante del informe dirigida a lectores expertos en el tema; usa terminología específica, incluye detalles metodológicos y no simplifica los datos.

**Versión ejecutiva:** Variante del informe dirigida a dirección o gerencia; solo incluye conclusiones, decisiones requeridas y próximos pasos; elimina cualquier detalle que no sea relevante para decidir.

**Versión para cliente:** Variante del informe dirigida al cliente externo o socio no experto; usa lenguaje accesible, sin jerga, orientado al impacto que tiene para esa persona específica.

**Alucinación en informes:** Error específico en el que la IA incluye datos concretos (estadísticas, normativas, cifras, fechas) que no estaban en el material de partida y que pueden ser incorrectos; el riesgo es mayor cuando el informe se entrega a externos.

**Prompt de auditoría:** Instrucción específica para que la IA identifique qué datos concretos del documento provienen del material proporcionado y cuáles generó por su cuenta, facilitando la verificación manual antes de publicar.

**Coherencia de tono:** Consistencia en el registro formal, el nivel de detalle y el estilo de escritura a lo largo de todas las secciones del informe. La IA puede detectar inconsistencias entre secciones redactadas en momentos distintos.

**Sección por sección:** Metodología de construcción de informes con IA en la que se redacta cada sección en un prompt separado, con los datos específicos de esa sección, para maximizar la precisión y evitar resultados genéricos.

**Revisión cruzada:** Proceso por el que un compañero lee el informe con ojos frescos para detectar lo que el autor ya no ve: incoherencias, frases que suenan inventadas, datos que no encajan.

**Plantilla de índice:** Estructura de secciones de un tipo de informe recurrente guardada en la biblioteca de prompts, que elimina el paso 1 del flujo en todos los informes posteriores del mismo tipo.

**Datos de tabla integrados en prosa:** Proceso de convertir datos numéricos de hojas de cálculo en párrafos narrativos de análisis usando IA, con verificación posterior de que los números del párrafo coinciden con los de la tabla original.

---

## 10. ERRORES COMUNES Y BUENAS PRÁCTICAS

**Error 1 — Pedir a la IA "escríbeme un informe sobre X" sin dar estructura ni datos.** Este prompt genera un texto genérico que no sirve de nada porque la IA no conoce el contexto real. El flujo correcto siempre empieza por el índice, luego los datos de cada sección, luego la redacción.

**Error 2 — Redactar el resumen ejecutivo antes de tener el cuerpo.** Es el error conceptual más frecuente. El resumen ejecutivo resume lo que existe, no lo que se imagina que se va a escribir. Si se genera primero, queda desconectado del cuerpo y hay que reescribirlo entero al final de todas formas.

**Error 3 — No dar instrucciones de tono y audiencia en cada prompt de sección.** Si no se especifica el destinatario y el registro esperado, la IA mezcla tonos y niveles de formalidad entre secciones. La instrucción "Tono: formal y directo. Destinatario: [descripción]" debe estar en cada prompt de sección.

**Error 4 — Pegar el informe con datos reales de la empresa para que la IA lo revise.** Antes de pegar cualquier informe en ChatGPT, Gemini o Claude, sustituir todos los datos que puedan identificar a personas, clientes o proveedores por etiquetas genéricas. CLIENTE_A, PROVEEDOR_X, IMPORTE_Y son etiquetas suficientes para que la IA haga su trabajo y la empresa proteja su información.

**Error 5 — Confiar en los datos que la IA añade por su cuenta.** Si la IA cita una estadística, un porcentaje o una normativa que no estaba en el material de partida, ese dato necesita verificación antes de incluirlo. La señal de alarma es la precisión inesperada: un porcentaje exacto con decimales, un número de ley o una fecha concreta que nadie le dio.

**Buena práctica — Guardar el índice como plantilla reutilizable.** Si el tipo de informe se repite (mensual, trimestral, de incidencias, de seguimiento de proyecto), guardar el índice validado como plantilla. La próxima vez, el paso 1 del flujo ya está hecho.

**Buena práctica — Hacer la revisión cruzada siempre.** Un informe que se ha redactado sección por sección y luego se ha ensamblado siempre tiene al menos una incoherencia que el autor no ve porque está demasiado cerca del texto. Que un compañero lo lea en cinco minutos antes de enviarlo puede evitar un error embarazoso.

**Error 6 — No incluir la instrucción de tono en cada prompt de sección.** Si el tono se especifica solo en el primer prompt y no en los siguientes, el informe queda inconsistente: secciones en distintos registros que parecen escritas por personas distintas. La instrucción "Tono: [formal/directo/técnico]. Registro: [administrativo/ejecutivo]" debe repetirse en cada prompt de sección.

---

## 11. ACTIVIDADES EN AULA

### Actividad 1 — Informe en cuatro iteraciones [Grupo · 50 min]

**Descripción:** El formador proporciona un conjunto de datos brutos de un caso ficticio: los resultados del mes de junio de una empresa de distribución, con datos de ventas por zona, incidencias de entrega, evolución de costes de transporte y una anomalía en la zona norte. La clase construye colectivamente un informe de dos páginas usando exactamente el flujo de cuatro pasos: índice en el primer prompt, dos secciones en los prompts siguientes, resumen ejecutivo en el último y revisión de coherencia al final. El formador proyecta cada paso en pantalla y el grupo debate qué añadir, qué eliminar y cómo iterar cada resultado.

**Objetivo:** Que el grupo experimente en directo la diferencia entre escribir de manera lineal y usar el flujo de cuatro pasos. Que se normalice la iteración como parte natural del proceso, no como señal de que algo ha fallado.

**Material:** Pantalla del formador. Datos del caso ficticio (ficha impresa o Google Doc compartido). ChatGPT o Google Gemini (cuenta del formador para la demo grupal).

---

### Actividad 2 — Adaptar a tres audiencias [Individual · 35 min]

**Descripción:** Cada alumno elige un texto propio de su puesto: puede ser un informe, un resumen de reunión, una comunicación de resultado o cualquier documento que habitualmente adapte a distintos destinatarios. Si no tiene un texto real disponible, usa el informe construido en la Actividad 1. A continuación, genera con IA las tres versiones: técnica, ejecutiva y para cliente externo, en tres prompts separados. Compara las tres versiones y anota en qué cambió el tono, el nivel de detalle y el vocabulario.

**Objetivo:** Comprobar en primera persona que la adaptación a tres audiencias que antes costaba entre 45 y 90 minutos puede hacerse en 10–15 minutos con IA. Que el alumno tome conciencia de que es una tarea que podrá hacer desde mañana mismo.

**Material:** Ordenador con acceso a ChatGPT, Gemini o Claude. Texto propio anonimizado (o el informe del caso ficticio).

---

### Actividad 3 — Revisión cruzada en parejas [Pareja · 10 min]

**Descripción:** Cada alumno intercambia con su pareja una de las versiones del informe generadas en la Actividad 2. La pareja lee el informe con una pregunta en mente: ¿hay algo que no quede claro? ¿Hay algún dato o afirmación que suene inventado o que no esté respaldado por lo que se explica? Cada persona da un feedback verbal de dos minutos sobre lo que ha encontrado.

**Objetivo:** Practicar la revisión cruzada como hábito de calidad antes de entregar un informe. Descubrir que un lector externo detecta en dos minutos lo que el autor no ve tras horas frente al texto.

**Material:** Ordenador o documento impreso con el informe generado en la Actividad 2.

*(Suma de actividades: 50 + 35 + 10 = 95 min)*

---

## 12. 🔁 TRABAJO EN PAREJAS

La **Actividad 3** es una dinámica íntegramente en **parejas**. Durante diez minutos, cada alumno intercambia su informe con el compañero y actúa como lector externo: alguien que no ha participado en la redacción y que lee el documento por primera vez con dos preguntas concretas en mente. La primera: ¿hay algo que no quede claro o que necesite más explicación? La segunda: ¿hay algún dato, estadística o afirmación que suene demasiado genérico o que no esté respaldado por el contenido del informe? Cada persona da un feedback verbal de dos minutos, sin editar el informe del compañero sino señalando los puntos que llaman la atención. Esta revisión cruzada replica el rol de control de calidad que en muchas organizaciones se hace antes de publicar cualquier documento externo: un par de ojos frescos que detectan lo que el autor ya no ve. La reflexión final: ¿qué encontró tu pareja que tú no habías visto? ¿Qué te dice eso sobre el valor de la revisión antes de enviar?

---

## 13. EJERCICIOS SUGERIDOS

Ver Banco de Ejercicios:
- **EJ-D07-1** (Individual): Construir con IA el índice y dos secciones de un informe real del propio puesto usando el flujo de 4 pasos
- **EJ-D07-2** (Pareja): Revisión cruzada de informes: cada alumno lee el informe del compañero y señala incoherencias o datos que suenan inventados
- **EJ-D07-3** (Grupo): Debate sobre la versión más difícil de adaptar (¿técnica, ejecutiva o para cliente?) y construcción colectiva de una guía de buenas prácticas para cada versión

---

## 14. CUESTIONARIO DE AUTOEVALUACIÓN

**1. ¿Por qué el resumen ejecutivo debe redactarse en el último paso del flujo, no en el primero?**
a) Porque la IA tarda más en generar resúmenes que secciones completas
b) Porque el resumen resume lo que ya existe, y si se escribe antes no refleja el contenido real del informe ✓
c) Porque los destinatarios ejecutivos prefieren leer el resumen al final
d) Porque el procesador de texto no permite insertar el resumen al principio

**2. ¿Cuánto tiempo puede ahorrarse al adaptar un informe técnico a tres versiones con IA respecto a hacerlo sin IA?**
a) Entre 5 y 10 minutos
b) Entre 15 y 20 minutos
c) Entre 35 y 80 minutos ✓
d) Más de 2 horas en todos los casos

**3. ¿Cuál es la característica principal de la versión ejecutiva de un informe?**
a) Incluye todos los detalles técnicos con precisión
b) Usa lenguaje accesible sin jerga para clientes externos
c) Solo incluye conclusiones, decisiones requeridas y próximos pasos ✓
d) Es una versión resumida de la versión técnica con el mismo vocabulario

**4. ¿Qué instrucción de seguridad debe incluirse en los prompts de redacción de informes para reducir las alucinaciones?**
a) "Escribe en tercera persona"
b) "Usa únicamente la información que te proporciono. No añadas datos externos." ✓
c) "Incluye solo datos de los últimos tres años"
d) "Cita siempre las fuentes al final del párrafo"

**5. ¿Qué hace el prompt de auditoría de datos?**
a) Corrige los errores ortográficos del informe
b) Adapta el informe a un nuevo público
c) Lista los datos concretos del informe e indica cuáles provienen del material dado y cuáles la IA añadió por su cuenta ✓
d) Genera una nueva versión del informe sin datos

**6. ¿Cuál es la señal de alarma que indica que un dato puede ser una alucinación?**
a) Que el dato aparezca en la primera sección del informe
b) Que el dato sea un porcentaje con decimales o una referencia normativa precisa que no estaba en el material de partida ✓
c) Que el dato esté en una tabla en lugar de en el texto
d) Que la IA lo haya generado muy rápidamente

**7. ¿Por qué se recomienda pedir las tres versiones (técnica, ejecutiva, para cliente) en prompts separados?**
Respuesta abierta: Porque pedir las tres versiones en el mismo prompt tiende a generar resultados menos precisos: la IA no puede ajustar el foco completamente a tres audiencias distintas al mismo tiempo. Con prompts separados, cada versión recibe toda la atención y el ajuste específico que necesita su audiencia.

**8. ¿Cuándo es imprescindible anonimizar un informe antes de pasarlo por la IA?**
a) Solo cuando el informe es muy largo
b) Solo cuando el informe contiene datos financieros
c) Siempre que el informe contenga datos que identifiquen a personas, clientes, proveedores o información interna de la empresa ✓
d) Solo cuando se usa ChatGPT, no cuando se usa Gemini

**9. ¿Cuál es el objetivo de la revisión cruzada en parejas?**
Respuesta abierta: Que una persona que no ha participado en la redacción lea el informe con ojos frescos y detecte incoherencias, datos que suenan inventados o frases que no quedan claras. El autor está demasiado cerca del texto para ver estos problemas; un lector externo los detecta en pocos minutos.

**10. ¿Qué ventaja tiene guardar el índice de un informe como plantilla reutilizable?**
a) La IA genera el informe automáticamente sin necesidad de prompts adicionales
b) Se elimina la necesidad de verificar los datos del informe
c) El paso 1 del flujo ya está hecho en los informes recurrentes del mismo tipo ✓
d) El informe se publica directamente sin revisión

**11. ¿Qué diferencia hay entre la versión técnica y la versión para cliente del mismo informe?**
Respuesta abierta: La versión técnica usa terminología específica, incluye detalles metodológicos y está dirigida a expertos que necesitan la información completa para ejecutar o revisar procesos. La versión para cliente usa lenguaje accesible sin jerga, elimina los detalles técnicos irrelevantes para el destinatario y orienta el contenido hacia el impacto que tiene para esa persona concreta.

**12. ¿Cuál es el primer paso del flujo de construcción de un informe con IA?**
a) Redactar el resumen ejecutivo
b) Escribir la sección más importante del informe
c) Generar el índice completo antes de redactar ninguna sección ✓
d) Definir el tono y el registro del documento

---

## 15. PREGUNTAS FRECUENTES (FAQ)

**¿Puedo usar este flujo de cuatro pasos para informes muy cortos, de una página o menos?**
Para informes muy cortos (menos de una página), el flujo puede simplificarse a dos pasos: índice y redacción completa en un solo prompt. El flujo de cuatro pasos está especialmente diseñado para documentos de dos páginas o más, donde la estructura y la coherencia entre secciones son más difíciles de mantener.

**¿Qué hago si la IA genera secciones muy largas que superan la extensión que pedí?**
Itera con instrucciones precisas: "La sección es demasiado larga. Reduce a [N] palabras manteniendo los puntos 1, 2 y 3. Elimina los ejemplos del párrafo central." La IA ajusta la extensión con facilidad cuando se le da una instrucción específica sobre qué conservar y qué recortar.

**¿Hay diferencia entre usar ChatGPT, Gemini o Claude para redactar informes?**
Las tres herramientas funcionan bien para este propósito. Claude es especialmente preciso en análisis de coherencia y detección de inconsistencias. Gemini tiene la ventaja de integrarse con Google Docs, lo que facilita pegar y editar el resultado directamente en el documento final. ChatGPT es muy versátil y el modelo gratuito es suficiente para todos los pasos del flujo.

**¿La IA puede generar tablas y gráficos para el informe?**
La IA puede generar tablas en formato texto (markdown) que se pueden pegar directamente en Google Docs o Word. Para gráficos visuales, las herramientas de texto como ChatGPT o Claude no generan imágenes, pero sí pueden generar los datos en formato tabla que luego se convierten en gráfico en Sheets o Excel. Canva, en cambio, puede generar elementos visuales a partir de datos.

**¿Cómo sé si la versión ejecutiva que ha generado la IA es realmente ejecutiva?**
La prueba es simple: ¿puede alguien leer el documento en dos minutos y saber qué decisión hay que tomar y por qué? Si la respuesta es sí, es ejecutiva. Si hay párrafos que explican el proceso o detalles que no afectan a la decisión, aún hay trabajo de edición. Pide a la IA: "Revisa esta versión ejecutiva. ¿Hay algún párrafo que un director podría eliminar sin perder la capacidad de tomar la decisión?"

**¿Qué ocurre si el informe que necesito adaptar es muy técnico y yo no domino el vocabulario específico?**
La IA puede ayudarte a identificar qué términos técnicos necesitan explicación para audiencias no expertas. Usa el prompt: "Identifica los términos técnicos de este informe que un lector no experto no entenderá y propón cómo explicarlos en la versión para cliente sin que el texto resulte condescendiente."

**¿Puedo hacer la revisión de coherencia con una IA diferente a la que usé para redactar el informe?**
Sí, y a veces es útil hacerlo así. Cada modelo tiene sus propios patrones de generación, y una IA diferente puede detectar inconsistencias que la que redactó el texto no señalaría. Si usas Claude para redactar y Gemini para revisar, los dos ofrecen perspectivas ligeramente distintas.

**¿El banco de plantillas de correo de ayer y los informes de hoy se pueden conectar en el proyecto final?**
Completamente. El proyecto final puede incluir ambos como evidencias de mejora en comunicación escrita: las plantillas de correo para la comunicación cotidiana y los informes adaptados a tres audiencias para la comunicación formal. Juntos demuestran un dominio completo de la comunicación profesional escrita con IA.

---

## 16. HERRAMIENTAS DE LA SESIÓN

- **ChatGPT** (chatgpt.com) — Cuenta gratuita. Muy versátil para redacción sección por sección y adaptación de tono. El modelo gratuito es suficiente para el flujo de cuatro pasos.
- **Google Gemini** (gemini.google.com) — Cuenta Gmail personal. Ventaja adicional: integración con Google Docs para editar el resultado directamente sin copiar y pegar.
- **Claude** (claude.ai) — Cuenta gratuita. Especialmente recomendado para la revisión de coherencia y el prompt de auditoría de datos, dado su precisión en análisis de texto.
- **Google NotebookLM** (notebooklm.google.com) — El formador comparte el enlace del notebook del día. Los alumnos pueden interrogar los contenidos de la sesión en formato pódcast, vídeo, fichas o cuestionario.

Ver el mapa completo de herramientas en `Recursos/Herramientas_Gratuitas.md`.

---

## 17. MINI-ENTREGABLE DEL DÍA

**Nombre:** Informe en tres versiones
**Formato:** Documento Google Docs (o Word) con tres secciones claramente diferenciadas y encabezadas
**Contenido:** Un informe corto de aproximadamente dos páginas en versión técnica, versión ejecutiva y versión para cliente externo, más una nota del alumno de tres a cinco líneas explicando qué cambió entre versiones y por qué se tomaron esas decisiones de adaptación.
**Cómo alimenta el proyecto final:** El informe en tres versiones es una evidencia directa de la capacidad del alumno para comunicar el mismo contenido a audiencias distintas, que es una competencia clave en cualquier puesto administrativo. En el proyecto final, este entregable puede presentarse como demostración de ahorro de tiempo y mejora de calidad en la comunicación formal con distintos stakeholders.

---

## 18. 🎓 HILO DEL PROYECTO FINAL

Para tu proyecto final: lo de hoy te sirve para demostrar cómo puedes construir documentos formales de calidad profesional con IA en una fracción del tiempo habitual. Si tu proyecto final tiene un componente de documentación o reporting (informe de seguimiento, memoria de actividad, comunicación de resultados), el flujo de cuatro pasos de hoy es directamente aplicable. Guarda los tres borradores del informe de hoy, junto con la nota explicando las decisiones de adaptación: es material concreto y diferenciador para la presentación en D16–D17.

---

## 19. MENSAJE CLAVE DE LA SESIÓN

> "Un informe no es un documento: es una decisión esperando ser tomada. La IA no te quita el criterio profesional, te libera del tiempo de redacción para que puedas dedicarlo al análisis. Lo que antes llevaba una tarde ahora lleva una hora."

---

## 20. IDEAS PARA RECORDAR

- El flujo correcto para informes con IA es siempre: índice primero → secciones por separado → resumen ejecutivo al final → revisión de coherencia.
- El resumen ejecutivo se escribe al final porque resume lo que ya existe; si se escribe antes, queda desconectado del cuerpo real del informe.
- Adaptar un informe a tres audiencias (técnica, ejecutiva, cliente) con IA tarda 8–12 minutos; hacerlo sin IA puede llevar entre 45 minutos y hora y media.
- Antes de entregar cualquier informe a externos, verificar manualmente todos los datos concretos: fechas, cifras, normativas y referencias que la IA haya podido añadir por su cuenta.
- La revisión cruzada con un compañero antes de enviar detecta en cinco minutos lo que el autor ya no ve tras horas frente al texto.

---

## 21. CONEXIÓN CON EL RESTO DEL CURSO

Esta sesión cierra el Módulo 3 de Redacción y Comunicación. En D04 se automatizaron las tareas de escritura repetitiva, en D05 se dominó el resumen y la transformación de formatos, en D06 se perfeccionó la comunicación por correo, y hoy se completa el ciclo con la documentación formal. A partir de mañana, el curso arranca el **Módulo 4 — Organización del Trabajo** con D08, donde todo lo aprendido sobre escritura con IA se traslada a la planificación y la gestión de tareas. Los informes de hoy son los mismos documentos que en D08 se convertirán en punto de partida para planificar proyectos y generar actas de reunión. El Módulo 3 ha construido la base de comunicación escrita; el Módulo 4 construirá sobre ella la base de organización y gestión del tiempo.

---

## 22. FOOTER

*Brief para NotebookLM · D07 · Edición 01/26 — IA en la Oficina*
