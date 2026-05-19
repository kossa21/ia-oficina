# BRIEF PARA NOTEBOOKLM — D05
## Módulo 3, Sesión 2: Resúmenes y transformación de formatos
## Curso: IA en la Oficina – Eficiencia y Productividad
## Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital

---

## 2. CONTEXTO DEL CURSO

**Programa:** IA en la Oficina – Eficiencia y productividad (68 horas · 17 sesiones de 4 horas)
**Público:** Personal administrativo y de oficina sin experiencia previa en IA generativa. Todos los alumnos utilizan cuentas personales de Gmail; no hay cuentas corporativas ni licencias de Microsoft 365.
**Metodología:** ~40 % teoría y demo · ~50 % práctica guiada · ~10 % puesta en común
**Sesión anterior (D04):** El grupo ya automatiza tareas repetitivas con IA y tiene plantillas personales con campos variables en [CORCHETES] guardadas y listas para usar.

> *Este documento es la fuente del notebook de hoy. Además de las diapositivas, puedes pedirle a NotebookLM un resumen en **audio** (tipo pódcast), un **vídeo**, una **infografía** o mapa mental, una **guía de estudio**, **fichas** (flashcards), un **cuestionario** para autoevaluarte, o **escribir tus preguntas en el chat**. Usa el formato con el que mejor aprendas. No escribas datos personales reales en el chat.*

---

## 3. RESUMEN DE LA SESIÓN

Un mismo documento puede necesitar ser leído por tres personas distintas: la directora que tiene cinco minutos antes de la reunión, el técnico que necesita saber exactamente qué tiene que hacer el lunes, y el cliente que no entiende la jerga interna de la empresa. Hoy aprenderemos a producir esos tres documentos a partir de uno solo, usando la IA para resumir, adaptar y transformar. Trabajaremos los tres tipos de resumen según el destinatario, los cinco tipos de conversión de formato más útiles en una oficina, y la técnica de extracción de campos para procesar lotes de correos o documentos en minutos. También veremos cómo gestionar documentos largos que no caben en una sola consulta y cuándo conviene usar Claude o NotebookLM en lugar de ChatGPT. Al terminar la sesión cada alumno tendrá el mismo documento en tres versiones listas para usar, y el criterio para saber cuál usar con cada destinatario.

---

## 4. ESTRUCTURA DE LA SESIÓN (240 min)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| Apertura | 15 min | Repaso de plantillas D04 · Objetivos del día |
| Teórico-demostrativo | 75 min | Los 3 tipos de resumen · Conversión de formatos · Extracción de campos · Documentos largos |
| Descanso | 15 min | — |
| Práctica guiada | 95 min | Acta en 3 formatos (grupo) + documento real propio (individual) + mini-debate |
| Puesta en común | 40 min | Comparativa de versiones · Mini-entregable · Cierre |

---

## 5. OBJETIVOS DE APRENDIZAJE

1. Producir tres versiones de un mismo documento adaptadas a tres tipos de destinatario (ejecutivo, operativo, divulgativo).
2. Convertir información entre los cinco formatos más útiles en oficina: texto a tabla, tabla a texto, lista a párrafo, párrafo a checklist, notas a documento formal.
3. Extraer información estructurada de correos, contratos o actas usando un único prompt de extracción de campos.
4. Gestionar documentos que superan el límite de contexto de los modelos de IA sin perder información relevante.

---

## 6. DESARROLLO TEÓRICO EN PROSA

### El problema de escribir para todos con el mismo documento

Marta ha preparado el informe de incidencias del trimestre. Son cuatro páginas densas con tablas, datos de proveedores, análisis de causas y propuestas de mejora. Ahora tiene que enviarlo a tres personas distintas: a la directora general, que tiene dos reuniones seguidas y cinco minutos para leerlo; al jefe de operaciones, que necesita saber exactamente qué hay que hacer la semana que viene; y al proveedor principal, que no tiene acceso a la terminología interna de la empresa y se perdería entre las siglas. Hasta ahora Marta dedicaba entre 45 minutos y una hora a reescribir el informe tres veces, adaptando cada versión al destinatario. Hoy eso cambia.

La IA es especialmente eficaz en tareas de adaptación de contenido, precisamente porque no tiene el problema que tenemos las personas: no le cuesta "olvidar" lo que ya sabe sobre el tema para explicarlo desde cero, ni le supone un esfuerzo extra ser más conciso de lo habitual, ni tarda más en escribir formal que informal. Para la IA, producir tres versiones del mismo contenido es casi la misma tarea que producir una, siempre que las instrucciones sean claras.

### Los tres tipos de resumen según el destinatario

El primer criterio a la hora de resumir no es la longitud del documento original, sino quién lo va a leer y para qué. Hay tres perfiles habituales en una empresa, y cada uno necesita un formato distinto.

El resumen ejecutivo está pensado para quienes toman decisiones: dirección, gerencia, consejos de administración. Estas personas leen el documento para decidir, no para entender todos los detalles. Por eso el resumen ejecutivo tiene como máximo cinco puntos, usa lenguaje no técnico aunque el tema sea técnico, y prioriza decisiones pendientes, riesgos relevantes y próximos pasos concretos. No hay espacio para explicaciones de proceso ni para contexto histórico que ya se conoce. El prompt para generarlo es:

> "Resume el siguiente documento en máximo 5 puntos clave para una reunión de dirección de 5 minutos. Usa lenguaje no técnico. Prioriza decisiones pendientes, riesgos relevantes y próximos pasos concretos. No incluyas detalles de proceso ni información histórica ya conocida. [PEGAR DOCUMENTO]"

El resumen operativo está pensado para el equipo de trabajo: quienes ejecutan, coordinan o dan seguimiento. Estas personas necesitan saber qué tienen que hacer, no solo qué está pasando. Por eso el resumen operativo toma la forma de una lista numerada de acciones, cada una con su responsable y su plazo. No es un resumen narrativo: es un listado accionable. El prompt para generarlo es:

> "Del siguiente documento, extrae todas las acciones que implican hacer algo. Preséntalo como lista numerada con formato: Acción / Responsable / Plazo. Si algún dato no aparece en el documento, indica 'por determinar'. [PEGAR DOCUMENTO]"

El resumen divulgativo está pensado para destinatarios externos o para personas que no conocen el contexto interno de la empresa: clientes, proveedores, colaboradores externos, público general. Estas personas no manejan las siglas internas, no conocen los procesos que se dan por supuesto, y necesitan que la información se les explique como si fuera la primera vez que oyen hablar del tema. El lenguaje es llano, las frases son más cortas, y si hay términos técnicos imprescindibles se explican brevemente. El prompt para generarlo es:

> "Reescribe el siguiente texto para que lo entienda alguien ajeno a la empresa que no conoce la terminología interna. Usa frases cortas y lenguaje cotidiano. Si hay siglas o términos técnicos, explícalos brevemente la primera vez que aparecen. Mantén toda la información relevante pero elimina los detalles de proceso interno. [PEGAR DOCUMENTO]"

Estos tres prompts producen tres versiones del mismo contenido adaptadas al destinatario real, y juntas cubren el 90 % de los casos de comunicación en una empresa mediana.

### Conversión de formatos: los cinco más útiles en oficina

Más allá de resumir, la IA puede transformar la forma en que está presentada la información sin cambiar el contenido. Esto es especialmente útil cuando se recibe información en un formato que no es el que necesitas para trabajar con ella, o cuando hay que preparar el mismo contenido para distintos soportes.

La primera conversión, texto a tabla, es quizá la más usada. Cuando un correo largo o unas notas de reunión contienen información que sería mucho más clara en una tabla (fechas, responsables, plazos, importes), un solo prompt la reorganiza: "Convierte la siguiente información en una tabla con columnas: Fecha / Responsable / Acción / Plazo." En segundos, un bloque de texto difícil de leer se convierte en una tabla manejable que se puede pegar directamente en un informe o en una hoja de cálculo.

La segunda, tabla a texto, funciona en sentido inverso: cuando tienes datos en una tabla y necesitas incorporarlos a un documento narrativo, como un informe o un correo, la IA los convierte en párrafos fluidos y coherentes: "Describe en prosa los datos de esta tabla como si fuera el párrafo de análisis de un informe mensual."

La tercera, lista a párrafo, es muy útil para los correos formales. Las listas de puntos quedan bien en notas internas, pero en comunicaciones externas o más formales un párrafo fluido transmite más credibilidad y cuidado. La instrucción es directa: "Convierte esta lista de puntos en un párrafo fluido para incluir en un correo formal. Usa conectores y mantén toda la información."

La cuarta, párrafo a checklist, va en sentido contrario: tienes un correo o un documento lleno de obligaciones, compromisos o pasos a seguir, y necesitas extraerlos como lista de verificación para no olvidarte de nada. "Extrae de este texto todas las acciones, compromisos y pasos que hay que ejecutar y preséntalos como checklist numerado."

La quinta, notas informales a documento formal, es especialmente valiosa para quienes toman apuntes rápidos en reuniones y luego tienen que convertirlos en actas o informes. "Reescribe estas notas de reunión como acta formal con las secciones: Asistentes / Puntos tratados / Decisiones adoptadas / Acciones acordadas (con responsable y plazo). Mantén toda la información pero corrija el estilo y elimina las abreviaturas y notas personales."

### Extracción de campos: información estructurada en segundos

Una de las tareas más tediosas del trabajo administrativo es procesar un lote de correos, contratos o actas para extraer siempre los mismos datos de cada uno: quién lo firma, qué fecha tiene, qué importe menciona, qué plazos establece. Si hay diez correos, son diez lecturas completas y diez apuntes manuales. Con IA, el mismo trabajo se hace con un prompt que se aplica a cada documento:

> "Del siguiente texto, extrae en formato tabla los siguientes campos: (1) fechas mencionadas y su contexto, (2) importes económicos y su concepto, (3) nombres de personas y su rol en el documento, (4) acciones comprometidas con su responsable y plazo. Si algún campo no aparece en el texto, escribe 'no se menciona'. [PEGAR TEXTO]"

Este tipo de prompt de extracción de campos es especialmente potente porque produce siempre el mismo formato de salida, lo que facilita consolidar los resultados de varios documentos en una sola tabla comparativa. Marta lo usa para procesar las reclamaciones de clientes de cada semana: en vez de leer cada correo completo, lanza el prompt sobre los diez correos uno a uno y en tres minutos tiene una tabla con las diez reclamaciones, los importes afectados y los plazos solicitados. El mismo trabajo le llevaba antes media hora.

La clave de los buenos prompts de extracción es ser muy concreto sobre los campos que necesitas y especificar qué escribir cuando el campo no aparece. Si no se da esta instrucción, la IA puede inventar datos que no están en el texto para no dejar celdas vacías, que es precisamente lo que hay que evitar.

### Documentos largos: cómo procesarlos sin perder información

Los modelos de IA tienen un límite de texto que pueden procesar en una sola consulta, lo que se llama ventana de contexto. Para la mayoría de correos, notas y documentos de una o dos páginas, este límite no es un problema. Pero para contratos extensos, informes de muchas páginas o transcripciones largas de reuniones, hay que usar estrategias específicas.

La estrategia más directa es dividir el documento en secciones lógicas (capítulos, páginas, bloques temáticos), procesar cada sección con el mismo prompt de resumen o extracción, y luego hacer un resumen final de los resúmenes: "Aquí tienes los resúmenes de las cuatro secciones del documento. Genera ahora un resumen global en máximo diez puntos, sin añadir información que no aparezca en los resúmenes." Este proceso de chunking, como se llama técnicamente, mantiene toda la información relevante y produce un resultado coherente.

La alternativa más cómoda para documentos largos es usar directamente Claude o Google NotebookLM, que tienen ventanas de contexto significativamente más grandes que ChatGPT en su versión gratuita. Claude permite pegar documentos de hasta varias decenas de miles de palabras en una sola consulta, y NotebookLM está diseñado específicamente para trabajar con documentos de referencia extensos: se sube el documento entero y se hacen preguntas sobre él de forma natural, como si fuera una conversación. Para contratos, informes largos o documentación técnica extensa, NotebookLM es la herramienta más adecuada del curso.

---

## 7. DATOS Y CIFRAS CLAVE

- Procesar **10 correos de clientes** para extraer reclamación, importe y plazo: **3 minutos con IA** vs 30 minutos sin IA (ahorro: 90 %).
- El mismo documento resumido para tres destinatarios distintos antes costaba entre **45 y 60 minutos** de reescritura; con IA: **5–8 minutos** de prompts y revisión.
- El **47 % de los correos profesionales** no reciben respuesta en 24 horas porque el contenido no deja claro qué se espera del destinatario. Un resumen operativo bien hecho elimina ese problema.
- Conversión de formato texto a tabla: proceso manual **10–15 minutos** por documento; con IA: menos de **1 minuto**.
- Claude (plan gratuito) admite documentos de hasta ~200.000 tokens (equivalente a más de 150 páginas) en una sola consulta, frente a los ~8.000 del ChatGPT gratuito estándar.
- Los tres tipos de resumen (ejecutivo, operativo, divulgativo) cubren el **90 % de los casos** de comunicación habituales en una empresa mediana.
- Usar el formato de resumen equivocado para el destinatario equivocado puede retrasar una decisión **hasta 48–72 horas** (la dirección no actúa sobre listas de 20 ítems; el equipo operativo no actúa sobre resúmenes de cinco puntos sin asignar responsable).

---

## 8. EJEMPLOS RESUELTOS PASO A PASO

### Caso 1: Acta de reunión en tres formatos

**Situación:** Marta tiene que distribuir el acta de la reunión trimestral de coordinación. La asistieron la directora general, el jefe de operaciones y dos proveedores externos. Cada uno necesita una versión diferente del mismo documento.

**Prompt para el resumen ejecutivo:**
> "Resume el siguiente acta de reunión en máximo 5 puntos para la directora general. Prioriza las decisiones adoptadas, los riesgos identificados y los próximos pasos que requieren su aprobación. Usa lenguaje directo y no técnico. Máximo 120 palabras. [PEGAR ACTA]"

**Prompt para el resumen operativo:**
> "Del siguiente acta de reunión, extrae todas las acciones acordadas. Presenta el resultado como lista numerada con el formato exacto: ACCIÓN / RESPONSABLE / PLAZO. Si el responsable o el plazo no quedaron definidos en la reunión, escribe 'por definir'. [PEGAR ACTA]"

**Prompt para el resumen divulgativo (para los proveedores):**
> "Reescribe el siguiente acta de reunión para comunicarla a proveedores externos que no conocen la organización interna. Incluye solo los puntos que les afectan directamente. Usa lenguaje claro y evita siglas o referencias internas. Máximo 150 palabras. [PEGAR ACTA]"

**Resultado comentado:** Los tres prompts producen documentos completamente diferentes en extensión, tono y estructura, aunque parten exactamente del mismo texto de origen. La directora recibe 5 puntos de decisión; el jefe de operaciones, una lista de 8 acciones con responsable y plazo; los proveedores, un párrafo claro sobre lo que les afecta.

**Cómo iterarlo:** Si el resumen ejecutivo resulta demasiado técnico: "El punto 3 usa terminología interna que la directora no necesita. Reescríbelo en lenguaje de negocio general." Si falta una acción en el resumen operativo: "Añade la acción acordada en el punto 4 del acta: revisión de tarifas antes del 15 de julio, responsable: departamento de compras."

---

### Caso 2: Extracción de campos de correos de reclamación

**Situación:** Marta recibe cada lunes entre ocho y doce correos de clientes con reclamaciones de distinto tipo. Antes los leía todos y hacía un resumen manual en un Excel. Ahora usa extracción de campos.

**Prompt exacto:**
> "Del siguiente correo de cliente, extrae en formato tabla los campos: (1) Nombre del cliente o empresa (si se menciona), (2) Tipo de reclamación en tres palabras máximo, (3) Importe económico afectado (si se menciona; si no, escribe 'no especificado'), (4) Plazo solicitado por el cliente (si se menciona; si no, escribe 'no especificado'), (5) Tono del correo (urgente / neutro / molesto). No añadas información que no esté en el correo. [PEGAR CORREO]"

**Resultado comentado:** La IA devuelve una tabla de cinco columnas con la información exacta del correo, sin inventar nada. Marta lanza el mismo prompt sobre los doce correos uno a uno (o puede pegarlos todos numerados en un solo prompt si los documentos son cortos) y consolida las doce filas en un único Excel de seguimiento. El proceso completo tarda menos de cinco minutos.

**Cómo iterarlo:** "El correo número 3 tiene el importe en el cuerpo del mensaje pero la tabla lo marcó como 'no especificado'. Búscalo de nuevo: el importe es 1.240 euros. Actualiza la fila correspondiente."

---

### Caso 3: Convertir notas de reunión en documento formal

**Situación:** Marta tiene estas notas tomadas a mano durante una reunión de proveedores: "Juan dice que el albarán del 12 está mal. Lo revisamos. Marta dice que llama a logística. Precio unitario sube 3% desde agosto. Confirmar antes del viernes. Próxima reunión: 28 julio."

**Prompt exacto:**
> "Convierte las siguientes notas de reunión en un acta formal con estas secciones: Fecha y asistentes (usa los datos disponibles; si faltan, escribe 'por confirmar'), Puntos tratados (descripción breve de cada tema), Decisiones adoptadas (lista numerada), Acciones acordadas (tabla con Acción / Responsable / Plazo). Corrige el estilo y elimina las abreviaturas. Tono: formal y directo. NOTAS: [PEGAR NOTAS]"

**Resultado comentado:** La IA produce un acta estructurada y formal a partir de unas notas de tres líneas. Los campos que no están en las notas (fecha, lista completa de asistentes) quedan marcados como "por confirmar", lo que es correcto: la IA no inventa lo que no sabe.

**Cómo iterarlo:** "Añade al inicio del acta el campo 'Lugar: Sala de reuniones B' y la fecha '15 de julio de 2026'. Completa los asistentes: Marta García (administrativa), Juan Rodríguez (proveedor Suministros Norte)."

---

## 9. GLOSARIO

**Resumen ejecutivo:** Versión reducida de un documento pensada para quienes toman decisiones, con un máximo de 5 puntos que priorizan decisiones, riesgos y próximos pasos, sin detalles de proceso.

**Resumen operativo:** Versión de un documento orientada al equipo de trabajo, en forma de lista numerada de acciones con responsable y plazo asignados.

**Resumen divulgativo:** Versión de un documento para destinatarios externos o no especializados, en lenguaje cotidiano, sin jerga interna ni siglas sin explicar.

**Conversión de formato:** Proceso de transformar la presentación de una información (de texto a tabla, de lista a párrafo, de notas a acta formal) sin cambiar el contenido.

**Extracción de campos:** Técnica que consiste en pedir a la IA que lea un texto y extraiga siempre los mismos datos en forma de tabla estructurada, para procesar varios documentos con el mismo esquema.

**Ventana de contexto:** Cantidad máxima de texto que un modelo de IA puede leer y procesar en una sola consulta. Varía por herramienta y plan; es importante conocerla para saber cuándo dividir un documento.

**Chunking:** Técnica de dividir un documento largo en secciones para procesarlo en partes, y luego hacer un resumen global de los resúmenes parciales.

**Acta formal:** Documento oficial de registro de lo ocurrido en una reunión, con secciones fijas: asistentes, puntos tratados, decisiones y acciones con responsable y plazo.

**Prompt de extracción:** Tipo de prompt diseñado para leer un texto y extraer siempre los mismos campos de información en un formato predefinido, con instrucción explícita de qué escribir si el campo no aparece.

**Destinatario:** La persona o grupo específico para quien se escribe o adapta un documento, cuyas necesidades de información y nivel de conocimiento del tema determinan el tipo de resumen o formato adecuado.

---

## 10. ERRORES COMUNES Y BUENAS PRÁCTICAS

**Error 1 — Usar el mismo resumen para todos los destinatarios.** El resumen operativo con 12 acciones numeradas es perfecto para el equipo pero inútil para la directora, que necesita cinco puntos de decisión. Antes de resumir, pregúntate siempre: ¿quién lo va a leer y qué necesita saber para qué?

**Error 2 — No especificar qué hacer con los campos que faltan.** Si en el prompt de extracción no se indica qué escribir cuando un campo no está en el texto, la IA puede inventar datos para no dejar la celda vacía. Añade siempre al prompt: "Si el campo no aparece en el texto, escribe 'no especificado'" o "no se menciona".

**Error 3 — Confiar en el resumen sin verificar los datos críticos.** Los resúmenes de IA son generalmente muy fieles al documento original, pero en documentos con muchos datos numéricos (fechas, importes, porcentajes) siempre hay que verificar que los números del resumen coinciden con los del original. Los modelos pueden redondear o confundir cifras similares.

**Error 4 — Intentar procesar un documento muy largo de una vez con ChatGPT gratuito.** Si el documento es muy largo y el modelo devuelve solo una parte o un resultado incoherente, es señal de que superó la ventana de contexto. La solución es dividir el documento en secciones o cambiar a Claude o NotebookLM.

**Error 5 — Pegar documentos con datos personales reales sin anonimizar.** Antes de pegar cualquier correo, contrato o acta en una herramienta de IA, sustituye los datos reales: nombres por PERSONA_A, importes por IMPORTE_X, fechas sensibles por FECHA_Y, números de cuenta o referencia por REFERENCIA_Z. Este paso protege a las personas involucradas y cumple con las obligaciones de protección de datos.

**Buena práctica — Guardar los tres prompts de resumen como plantilla.** Los tres prompts (ejecutivo, operativo, divulgativo) son los que más vas a usar en tu día a día. Guárdalos ya en tu Google Doc de biblioteca de prompts con un nombre claro para cada uno. La próxima vez que tengas un documento que resumir, solo tendrás que pegarlos.

**Buena práctica — Hacer siempre una pasada de revisión antes de enviar.** La IA produce textos muy buenos pero no perfectos. En el resumen ejecutivo, verifica que los cinco puntos son los realmente más importantes. En el operativo, comprueba que los responsables y plazos son los que se acordaron. En el divulgativo, lee una vez más para asegurarte de que no hay jerga interna que haya quedado.

---

## 11. ACTIVIDADES EN AULA

**Actividad 1 — Acta en tres formatos [Grupo · 35 min]**

El formador proporciona un acta ficticia de reunión de dos páginas (disponible en el aula virtual). La clase trabaja en grupos de tres o cuatro personas: cada subgrupo produce las tres versiones del acta (resumen ejecutivo, operativo y divulgativo) usando ChatGPT, Gemini o Claude. Cada subgrupo compara sus tres versiones con las de otro subgrupo y debaten las diferencias de resultado entre herramientas. El formador proyecta tres ejemplos en pantalla y señala qué funciona bien y qué se puede mejorar en cada tipo de resumen. Objetivo: internalizar que el mismo contenido requiere tres tratamientos radicalmente distintos.

**Actividad 2 — Mi documento real [Individual · 50 min]**

Cada alumno trae un documento de su trabajo (anonimizado antes de la sesión: nombres reales sustituidos por PERSONA_A, etc.) y lo procesa con IA en tres pasos: primero genera el resumen ejecutivo, luego el operativo, luego aplica una conversión de formato que sea relevante para ese documento (texto a tabla, párrafo a checklist, o extracción de campos). El alumno elige las herramientas que prefiere y documenta los prompts usados en su Google Doc de biblioteca. Los últimos 5 minutos son para escribir una nota de reflexión: ¿cuál de las tres versiones usarías con cada destinatario de tu trabajo real?

**Actividad 3 — Mini-debate: ¿qué resumen para quién? [Grupo · 10 min]**

Ronda rápida donde cada alumno comparte un ejemplo de su trabajo real (anonimizado): "Tengo que enviar [tipo de documento] a [tipo de destinatario]. ¿Qué formato de resumen usarías?" El grupo responde y el formador modera añadiendo el criterio que lo justifica. Objetivo: consolidar el criterio de selección de formato según el destinatario y detectar casos límite donde el criterio no es obvio.

*Total práctica guiada: 35 + 50 + 10 = 95 min.*

---

## 12. 🔁 TRABAJO EN PAREJAS / GRUPO

La Actividad 1 es completamente colaborativa: el aula se organiza en grupos de tres o cuatro personas desde el primer minuto. Cada grupo trabaja conjuntamente sobre el mismo acta ficticia para producir las tres versiones de resumen y las compara con las de otro grupo. Los grupos se forman por proximidad física en el aula (las personas sentadas juntas forman el grupo) para facilitar la dinámica. Lo que producen juntos es un conjunto de tres documentos comparados, con notas sobre qué herramienta dio mejor resultado para cada tipo de resumen y por qué. Estas notas colectivas se comparten en el chat del aula virtual al final de la actividad para que todos puedan verlas. Durante la Actividad 2 el trabajo es individual, pero en los últimos 5 minutos cada persona le muestra a su compañero más cercano el documento que ha procesado y le pide una sugerencia de mejora o un tipo de resumen alternativo que no había considerado.

---

## 13. EJERCICIOS SUGERIDOS

Ver Banco de Ejercicios:
- **EJ-D05-1 (Individual):** Toma un informe o correo largo de tu trabajo (anonimizado) y genera las tres versiones de resumen. Escribe una nota de dos líneas para cada versión explicando a quién se lo enviarías y por qué.
- **EJ-D05-2 (Pareja):** Intercambia con tu compañero el resumen ejecutivo que has generado. Cada uno lo evalúa con un único criterio: ¿está todo lo que necesita saber un director para tomar una decisión? Propón una iteración de mejora.
- **EJ-D05-3 (Grupo):** El grupo elige un tipo de documento común (por ejemplo, un parte de incidencias o unas notas de reunión) y cada subgrupo aplica un tipo de conversión de formato diferente. Se comparan los resultados y se debate cuál es el más útil para el trabajo diario.

---

## 14. CUESTIONARIO DE AUTOEVALUACIÓN

**1. ¿Cuál es la característica principal del resumen ejecutivo?**
a) Es el más largo de los tres tipos
b) Está pensado para el equipo operativo con acciones numeradas
c) Tiene máximo 5 puntos y prioriza decisiones, riesgos y próximos pasos ✓
d) Está escrito en lenguaje cotidiano para clientes externos

**2. ¿Qué tipo de resumen es más adecuado para enviar al equipo que tiene que ejecutar las decisiones de una reunión?**
a) Resumen ejecutivo
b) Resumen operativo ✓
c) Resumen divulgativo
d) Cualquiera de los tres sirve igual

**3. ¿Cuál de estas conversiones de formato es un ejemplo de "texto a tabla"?**
a) Convertir un resumen de 5 puntos en un párrafo fluido
b) Reescribir unas notas informales como acta formal
c) Convertir una lista de notas de reunión en una tabla Acción / Responsable / Plazo ✓
d) Transformar un informe en un resumen ejecutivo

**4. En un prompt de extracción de campos, ¿por qué es importante especificar qué escribir cuando un campo no aparece en el texto?**
a) Para que el resultado sea más largo
b) Para que la IA no invente datos que no están en el documento ✓
c) Para que la tabla tenga siempre el mismo número de filas
d) No es importante especificarlo

**5. Marta necesita procesar 10 correos de clientes para extraer la reclamación, el importe y el plazo de cada uno. ¿Cuánto tiempo tarda con IA vs sin IA?**
a) 15 minutos con IA vs 30 minutos sin IA
b) 3 minutos con IA vs 30 minutos sin IA ✓
c) 10 minutos con IA vs 60 minutos sin IA
d) 5 minutos con IA vs 15 minutos sin IA

**6. ¿Qué herramienta del curso es más adecuada para trabajar con un contrato de 50 páginas en una sola consulta?**
a) ChatGPT gratuito
b) Gemini Gems
c) Claude o NotebookLM ✓
d) Canva

**7. ¿Qué es el "chunking" aplicado a documentos largos?**
a) Resumir el documento en un solo punto
b) Dividir el documento en secciones para procesarlas por partes y luego hacer un resumen global ✓
c) Convertir el documento a formato tabla
d) Extraer solo los datos numéricos del documento

**8. Antes de pegar un correo de un cliente en un prompt de IA, ¿qué pasos de privacidad hay que seguir?**
*Respuesta abierta:* Anonimizar todos los datos personales reales antes de pegar: sustituir nombres por PERSONA_A o CLIENTE_X, importes por IMPORTE_X, fechas sensibles por FECHA_Y, referencias identificables por REFERENCIA_Z. Nunca pegar DNI, números de cuenta, datos de nómina ni información que permita identificar a una persona real.

**9. ¿Cuál es la diferencia entre un resumen operativo y una extracción de campos?**
*Respuesta abierta:* El resumen operativo se aplica a un único documento para extraer las acciones acordadas con su responsable y plazo. La extracción de campos se aplica a uno o varios documentos para extraer siempre los mismos datos predefinidos (cualquier tipo de campo: fechas, importes, nombres, etc.) en forma de tabla estructurada, y está pensada para procesar lotes de documentos con el mismo esquema.

**10. Nombra las cinco conversiones de formato más útiles en oficina que hemos visto hoy.**
*Respuesta abierta:* Texto a tabla, tabla a texto, lista a párrafo, párrafo a checklist, notas informales a documento formal.

**11. ¿Cuál es el riesgo principal de usar el mismo resumen para todos los destinatarios?**
*Respuesta abierta:* Que la información no sea útil para quien la recibe: la directora no puede tomar decisiones a partir de una lista de 12 acciones operativas; el equipo no sabe qué tiene que hacer leyendo solo cinco puntos sin asignar responsable ni plazo; el proveedor no entiende el documento si está lleno de jerga interna. Cada destinatario necesita el formato que le permite actuar sobre la información.

---

## 15. PREGUNTAS FRECUENTES (FAQ)

**¿Puedo resumir documentos muy técnicos aunque yo no sea experta en el tema?**
Sí. La IA puede resumir documentos técnicos incluso cuando quien hace el prompt no tiene conocimientos especializados, siempre que el prompt indique claramente el nivel de lenguaje deseado en el resultado. La clave está en especificar bien el destinatario: "para alguien sin conocimientos técnicos" o "para una reunión de dirección generalista" orienta a la IA hacia el nivel de detalle y el vocabulario adecuados.

**¿Cuántas páginas puede procesar ChatGPT de una sola vez?**
En la versión gratuita, ChatGPT puede procesar textos de unas 6.000–8.000 palabras aproximadamente (unas 12–15 páginas densas). Si el documento es más largo, el resultado puede quedar incompleto o perder coherencia en la segunda mitad. En ese caso, divide el documento en secciones o usa Claude o NotebookLM, que tienen ventanas de contexto mucho más grandes.

**¿El resumen que genera la IA siempre es fiel al documento original?**
En general sí, pero los datos numéricos (fechas, importes, porcentajes) son los más propensos a errores de transcripción o redondeo. Después de generar cualquier resumen, haz siempre una verificación rápida de los números clave: que la fecha del acta sea la correcta, que los importes coincidan con el original, que los plazos estén bien. Es el único tipo de revisión que no se puede saltarse.

**¿Puedo usar NotebookLM para resumir documentos de trabajo?**
Sí, y es especialmente útil para documentos largos o cuando quieres hacer preguntas concretas sobre el contenido. Sube el documento (anonimizado), y en el chat del notebook puedes pedir el resumen ejecutivo, el operativo o hacer preguntas específicas como "¿cuáles son las tres acciones con plazo más urgente?" NotebookLM mantiene el documento como referencia durante toda la sesión, lo que es muy útil cuando hay que volver a él varias veces.

**¿Qué hago si el resumen es demasiado largo o demasiado corto?**
Itera directamente sobre el resultado en la misma conversación. Si es demasiado largo: "Reduce este resumen a la mitad manteniendo los puntos más importantes." Si es demasiado corto y falta información relevante: "Este resumen no menciona el punto sobre los plazos de entrega. Añádelo como punto adicional manteniendo el resto igual." No es necesario repetir el prompt desde cero.

**¿Puedo usar la extracción de campos con contratos o documentos legales?**
Sí, con precaución. La extracción de campos funciona bien para identificar fechas, partes del contrato, importes y cláusulas clave. Pero para documentos con implicaciones legales, el resultado siempre debe ser revisado por alguien con criterio sobre el contenido, y nunca debe usarse como sustituto del análisis jurídico. La IA puede omitir cláusulas importantes o malinterpretar el alcance de una condición. Para documentos críticos, úsala como primer filtro, no como fuente definitiva.

**¿Por qué a veces la IA añade información que no estaba en el documento original?**
Este comportamiento, llamado alucinación, ocurre cuando el modelo no tiene suficiente información en el texto de entrada y "completa" con conocimiento general. Se reduce al mínimo siendo muy específico en el prompt: "Solo usa la información que aparece explícitamente en el texto. Si un campo no está en el documento, escribe 'no se menciona'." Esta instrucción reduce drásticamente las alucinaciones en prompts de extracción y resumen.

---

## 16. HERRAMIENTAS DE LA SESIÓN

Todas las herramientas son gratuitas con cuenta personal de Gmail. Ver detalles en `Recursos/Herramientas_Gratuitas.md`.

| Herramienta | Uso en esta sesión | Acceso |
|---|---|---|
| **ChatGPT** (OpenAI) | Resúmenes, conversión de formatos, extracción de campos | chat.openai.com · cuenta Google |
| **Google Gemini** | Resúmenes, conversión, integración con Docs | gemini.google.com · Gmail |
| **Claude** (Anthropic) | Documentos largos (mayor ventana de contexto) | claude.ai · cuenta Google |
| **Google NotebookLM** | Documentos largos y preguntas sobre el contenido; material del día | notebooklm.google.com · Gmail |
| **Google Docs** | Guardar los tres resúmenes y la biblioteca de prompts | docs.google.com · Gmail |

*Nota: Microsoft Copilot no se usa en este curso. Si tu empresa ya te proporciona Copilot, los conceptos de esta sesión aplican igualmente.*

---

## 17. MINI-ENTREGABLE DEL DÍA

**Nombre:** Tres versiones de resumen
**Formato:** Google Doc con tres secciones claramente diferenciadas
**Contenido:** El mismo documento (anonimizado) resumido en tres formatos: resumen ejecutivo (máximo 5 puntos), resumen operativo (lista de acciones con responsable y plazo) y resumen divulgativo (lenguaje llano para destinatario externo). El documento incluye al inicio una nota del alumno de dos o tres líneas explicando para qué destinatario real de su trabajo usaría cada versión.
**Cómo alimenta el proyecto final:** Las tres versiones de resumen demuestran la capacidad de adaptación de contenido que el proyecto final requiere: en el proyecto habrá que presentar los resultados para al menos dos audiencias distintas (el equipo y la dirección), y la habilidad entrenada hoy es exactamente la que permite hacerlo de forma eficiente.

---

## 18. 🎓 HILO DEL PROYECTO FINAL

Para tu proyecto final: lo de hoy te sirve para dominar la capa de presentación y comunicación del proyecto, que es lo que determina si tu propuesta convence a la dirección, si el equipo sabe cómo implementarla, y si los clientes o colaboradores externos la entienden. Saber producir tres versiones del mismo contenido en minutos es una ventaja directa a la hora de defender tu proyecto ante distintos interlocutores.

---

## 19. MENSAJE CLAVE

> "El mismo contenido, tres lectores distintos, tres documentos distintos. La IA hace ese trabajo de adaptación en 30 segundos. Lo que antes era reescribir el mismo informe tres veces ahora es un solo prompt con tres iteraciones."

---

## 20. IDEAS PARA RECORDAR

- Antes de resumir, pregúntate siempre quién lo va a leer: el tipo de destinatario determina el tipo de resumen, no la longitud del documento original.
- La extracción de campos permite procesar diez correos o contratos en el tiempo que antes costaba leer uno: define bien los campos y especifica qué escribir cuando alguno no aparece.
- La conversión de formato no cambia el contenido; cambia cómo se presenta, y eso puede marcar la diferencia entre que alguien actúe sobre la información o la archive.
- Para documentos largos, usa Claude o NotebookLM; si no tienes opción, divide el documento en secciones y haz un resumen de resúmenes al final.
- Nunca pegues datos personales reales en la IA: anonimiza siempre antes de procesar cualquier documento de trabajo.

---

## 21. CONEXIÓN CON EL RESTO DEL CURSO

Esta sesión continúa directamente desde D04, donde el grupo automatizó tareas de producción de contenido; hoy aprendemos a transformar y adaptar contenido ya existente, que es la otra gran capacidad de la IA para el trabajo de oficina. La combinación de las dos sesiones (crear plantillas + resumir y transformar) cubre el 80 % de los casos de uso más frecuentes en administración. La sesión siguiente, D06, llevará estas habilidades al terreno específico de la comunicación escrita y los correos profesionales: veremos cómo redactar correos en situaciones difíciles, construir bancos de respuestas para clientes y revisar el tono y el estilo antes de enviar. Las habilidades de resumen y transformación de formato aprendidas hoy se aplicarán directamente en D06 para adaptar los mismos correos a distintos destinatarios y tonos.

---

## 22. FOOTER

*Brief para NotebookLM · D05 · Edición 01/26 — IA en la Oficina*
