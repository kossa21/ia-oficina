# BRIEF PARA NOTEBOOKLM — D13
## Módulo 6, Sesión 2: Material visual, comunicación interna y accesibilidad
## Curso: IA en la Oficina – Eficiencia y Productividad
## Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital

**Fecha:** Viernes 17 de julio de 2026 · 15:00–19:00 h · Día 13 de 17

---

## 2. CONTEXTO DEL CURSO

**Programa:** IA en la Oficina – Eficiencia y Productividad (68 horas · 17 sesiones de 4 horas)
**Público:** Personal administrativo y de oficina sin experiencia previa en IA generativa
**Metodología:** ~40 % teoría y demostración · ~50 % práctica guiada · ~10 % puesta en común
**Sesión anterior (D12):** El grupo crea presentaciones profesionales con Canva y genera imágenes con IA.

> *Este documento es la fuente del notebook de hoy. Además de las diapositivas, puedes pedirle a NotebookLM un resumen en **audio** (tipo pódcast), un **vídeo**, una **infografía** o mapa mental, una **guía de estudio**, **fichas** (flashcards), un **cuestionario** para autoevaluarte, o **escribir tus preguntas en el chat**. Usa el formato con el que mejor aprendas. No escribas datos personales reales en el chat.*

---

## 3. RESUMEN DE LA SESIÓN

Comunicar bien en la oficina no es solo cuestión de redactar un buen correo: a veces hace falta que el mensaje llegue a través de un cartel en la entrada, un banner en el canal de equipo y un boletín interno, todos coherentes entre sí y con la misma voz. Hoy aprendemos a crear kits de comunicación interna coordinados, en los que la IA escribe los textos y Canva construye las piezas visuales a partir de una misma plantilla. Partimos del trabajo de análisis de datos de D10 para convertir esos números en una infografía útil, y descubrimos cómo la función de redimensionado de Canva permite adaptar una pieza para distintos formatos en segundos. La parte más importante de la sesión —y la que más impacto tendrá en el puesto de trabajo— es la accesibilidad: cómo revisar contraste, texto alternativo y tamaño de fuente para que las comunicaciones lleguen de verdad a todas las personas, incluidas aquellas con distintas capacidades visuales o cognitivas. Al terminar, cada grupo entrega un mini-kit de comunicación visual coherente y accesible sobre un tema de su entorno laboral real.

---

## 4. ESTRUCTURA DE LA SESIÓN (240 min)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| Apertura | 15 min | Repaso D12 + presentación objetivos del día + ¿qué es comunicar con impacto? |
| Teórico-demostrativo | 75 min | Tipos de comunicación visual interna · Infografía desde datos · Kit coordinado · Canva y formatos múltiples · Vídeo simple · Accesibilidad en detalle |
| Descanso | 15 min | — |
| Práctica guiada | 95 min | Demo infografía · Mini-campaña en grupo · Auditoría de accesibilidad individual |
| Puesta en común | 40 min | Presentación de kits + reflexión sobre accesibilidad + cierre |

*(15+75+15+95+40 = 240 min)*

---

## 5. OBJETIVOS DE APRENDIZAJE

1. Crear una infografía a partir de datos tabulares, pasando por la síntesis con IA y la maquetación en Canva.
2. Diseñar un kit de comunicación interna de 3 piezas coordinadas (cartel, correo, banner) usando IA para los textos y Canva para los visuales.
3. Aplicar los criterios básicos de accesibilidad (contraste, texto alternativo, tamaño de fuente, diferenciadores no dependientes del color) en materiales digitales.
4. Utilizar el redimensionado de Canva para generar múltiples formatos desde una única plantilla sin duplicar el trabajo de diseño.

---

## 6. DESARROLLO TEÓRICO EN PROSA

### Cuándo usar cada tipo de comunicación visual interna

Marta trabaja en el departamento de administración de una empresa distribuidora de tamaño medio. Con relativa frecuencia, su equipo necesita comunicar cambios a otras áreas: una nueva política de gestión de pedidos, el traslado temporal de una sala de reuniones, el arranque de una campaña de bienestar. El problema no es que no sepan qué decir: el problema es que siempre usan el correo electrónico para todo, y los correos se pierden entre decenas de mensajes, se reenvían mal y no consiguen que el mensaje cale.

La comunicación visual interna abarca varios formatos con propósitos distintos. El **cartel de anuncio** es ideal cuando el mensaje es puntual, urgente y breve: "El viernes no habrá servicio de comedor" o "Nueva política de accesos desde el lunes". Su fortaleza es que puede colocarse físicamente en espacios de paso o enviarse como imagen en un canal de equipo, y se lee en segundos. La **infografía de datos** convierte números en narrativa visual: permite explicar los resultados de una encuesta de satisfacción, los indicadores de un trimestre o el comparativo de incidencias entre departamentos sin necesidad de que el lector interprete tablas. El **boletín interno** (newsletter) es adecuado para comunicaciones periódicas con más contenido: noticias del mes, logros del equipo, recordatorios de beneficios. Los **materiales de incorporación** (onboarding) —guías visuales, presentaciones de bienvenida, fichas de procedimiento— ayudan a que las personas nuevas en un puesto entiendan los procesos básicos sin depender de que alguien se los explique de palabra.

Conocer cuándo usar cada formato es tan importante como saber crearlo. Una infografía densa no es el vehículo adecuado para un anuncio urgente. Un correo de texto largo no es el mejor canal para explicar un proceso con muchos pasos. La IA puede ayudar a tomar esa decisión: si describes la situación al asistente de IA, este puede sugerirte qué formato y longitud se ajustan mejor al objetivo.

> **Puntos clave:**
> - Cada formato visual sirve a un propósito comunicativo distinto.
> - El cartel es para mensajes urgentes y breves; la infografía, para datos.
> - El boletín y el onboarding son para contenidos periódicos o estructurados.
> - La IA puede sugerir qué formato encaja mejor con cada situación.

### De los datos de D10 a una infografía: el flujo completo

En la sesión D10, el grupo analizó datos de su área con IA y obtuvo hallazgos sobre tendencias, totales o comparativas. Esos hallazgos, que hasta ahora viven en un documento de texto o una hoja de cálculo, pueden convertirse hoy en una infografía visual en pocos pasos.

El flujo tiene cuatro fases. La primera es **seleccionar los datos clave**: de todo el análisis, elegir los 3 o 4 hallazgos más relevantes y fácilmente comprensibles sin contexto técnico. No todo lo que se analizó tiene que aparecer en la infografía; la síntesis es parte del diseño. La segunda fase es **producir el texto de apoyo**: escribirle a la IA un prompt como "Tengo estos tres hallazgos sobre gastos del primer semestre de mi empresa [DATOS ANONIMIZADOS]. Redacta un titular breve para cada uno, máximo 8 palabras, y una frase de contexto de máximo 20 palabras. Tono directo e informativo." La IA devuelve titulares listos para pegar en Canva.

La tercera fase es **seleccionar y adaptar la plantilla en Canva**: buscar en la galería gratuita de Canva una plantilla de infografía (términos de búsqueda útiles: "infografía datos", "infografía estadísticas", "infographic report"). Las plantillas con bloques numerados o iconos son especialmente claras para datos. Sustituir los textos de ejemplo por los titulares generados con IA, ajustar los números o porcentajes y elegir una paleta de colores coherente con los materiales previos del grupo. La cuarta fase es **exportar**: Canva exporta en PNG o PDF de alta calidad desde el plan gratuito.

Marta aplica este flujo con los datos de incidencias de su departamento: los cuatro hallazgos principales se convierten en cuatro bloques visuales con icono, titular y cifra. El resultado es un documento de una página que puede enviarse por correo, imprimir y colgar en el tablón o compartir en el canal de Teams. Lo que antes habría requerido que Marta supiera maquetar en PowerPoint o contratar a alguien de diseño, ahora sale en unos veinte minutos.

> **Puntos clave:**
> - Seleccionar tres o cuatro hallazgos clave antes de empezar.
> - Pedir a la IA titulares cortos y frases de contexto medidas.
> - Adaptar una plantilla gratuita de Canva con iconos y paleta coherente.
> - Exportar en PNG o PDF para múltiples canales.

### El kit de comunicación interna coordinado

Uno de los principios más potentes de la comunicación efectiva es la coherencia: cuando un mismo mensaje llega a través de varios canales con la misma imagen, el mismo tono y los mismos puntos clave, la probabilidad de que se recuerde aumenta considerablemente. A esto se llama comunicación multicanal coordinada.

Un kit mínimo de comunicación interna consta de tres piezas: el **texto del correo electrónico**, el **cartel de anuncio** (para pantallas o tablones) y el **banner para Teams o canal interno**. Las tres hablan del mismo tema, comparten la paleta de colores, el logo del equipo o empresa y los dos o tres mensajes principales, pero cada una tiene el formato y la extensión adecuados a su canal. El correo puede tener tres párrafos; el cartel, solo el titular y una llamada a la acción; el banner, el titular y la fecha.

La IA facilita enormemente la creación de estas tres piezas porque permite adaptar el mismo mensaje de raíz a distintos formatos con un prompt bien construido. Un ejemplo: "Voy a comunicar internamente que la empresa cambia de sistema de gestión de pedidos el 1 de septiembre. Escríbeme: (1) un correo interno de anuncio de unas 150 palabras, tono cercano pero profesional; (2) un titular breve para un cartel de anuncio, máximo 10 palabras; (3) un texto para un banner de Teams de máximo 25 palabras con emoji opcional. Los tres deben transmitir los mismos tres puntos clave: la fecha, el motivo del cambio y que habrá formación de apoyo." En un solo prompt, Marta obtiene los tres textos base listos para revisar y pegar en Canva.

La ventaja de crear el kit completo de una sola vez con IA, en lugar de hacerlo en momentos distintos, es que la coherencia de mensaje y tono está garantizada desde el principio. Después solo hay que asegurarse de que el diseño visual también sea coherente, lo que se logra usando la misma plantilla de Canva o la misma paleta de colores para las tres piezas.

> **Puntos clave:**
> - El kit mínimo son tres piezas: correo, cartel y banner.
> - La coherencia visual y de tono multiplica el impacto del mensaje.
> - Un solo prompt puede generar los tres textos a la vez.
> - Misma plantilla y paleta para todas las piezas garantizan coherencia.

### Canva y la creación de múltiples formatos

Una de las funciones más prácticas de Canva gratuito para equipos de oficina es la posibilidad de **redimensionar un diseño para distintos formatos**. En el plan gratuito, esto se hace manualmente: una vez diseñada la pieza principal (por ejemplo, el cartel en formato A4 horizontal), se crea una nueva página con las dimensiones del banner (por ejemplo, 1200 × 300 px) y se reorganizan los elementos. No es automático como en el plan de pago, pero el proceso es rápido porque los elementos —colores, tipografías, imágenes— ya están elegidos.

La clave es empezar siempre por la pieza más grande o más compleja (normalmente el cartel) y después adaptar los elementos al formato más pequeño. Reducir es más fácil que ampliar porque hay que simplificar el mensaje, no inventar elementos nuevos. Para el banner de Teams, por ejemplo, puede bastar con el titular del cartel y el logo del equipo.

Canva también permite crear **presentaciones vídeo sencillas** desde sus plantillas de vídeo. Un vídeo de 30 a 60 segundos con texto sobre fondo, imágenes o iconos animados y música de biblioteca (gratuita en Canva) puede ser muy útil para anuncios de incorporación, recordatorios de formaciones o bienvenidas al equipo. No requiere edición de vídeo ni locución: basta con las diapositivas animadas y los textos. Este tipo de vídeo corto funciona especialmente bien cuando se comparte en un canal de Teams, ya que se reproduce directamente en el chat y tiene mucho más impacto visual que un PDF adjunto.

> **Puntos clave:**
> - El redimensionado manual en Canva gratuito es rápido y factible.
> - Empezar por la pieza más grande y simplificar al adaptar formatos.
> - Los vídeos cortos con plantillas de Canva no requieren edición.
> - Un vídeo de 30–60 segundos tiene gran impacto en Teams.

### Accesibilidad en el diseño visual: más que un requisito, una oportunidad

Este es uno de los aspectos más importantes de la sesión, y conviene abordarlo desde el principio con la actitud correcta: la accesibilidad no es un trámite burocrático ni un añadido para cumplir una norma. **El diseño accesible es mejor diseño para todos.** Una presentación con buen contraste es más fácil de leer en cualquier pantalla, incluidas las de baja calidad o en condiciones de luz difícil. Un texto con fuente grande y clara se lee mejor en el móvil. El texto alternativo en imágenes ayuda a los buscadores a indexar el contenido y a cualquier persona que tenga las imágenes desactivadas. Los diferenciadores visuales que no dependen solo del color también ayudan a quien ve la pantalla con mucho sol de fondo.

Que este curso esté vinculado a Fundación ONCE añade una dimensión adicional y muy concreta: en muchos equipos de trabajo ya hay, o habrá, personas con distintos niveles de visión, capacidad auditiva o procesamiento cognitivo. Hacer materiales accesibles es, literalmente, hacer materiales que esas personas pueden usar. No hacerlos accesibles es excluirlas silenciosamente de la comunicación del equipo.

**Contraste de color:** El estándar internacional de accesibilidad web WCAG establece que el contraste mínimo entre el texto y el fondo debe ser de **4,5:1** para texto de tamaño normal, y de 3:1 para texto grande (más de 18 pt o 14 pt en negrita). Un texto gris claro sobre fondo blanco puede verse bonito en pantalla de alta resolución, pero falla la prueba de contraste y resulta ilegible para personas con baja visión o en una pantalla proyectada en una sala iluminada. Para comprobar el contraste de los colores elegidos en Canva, se puede usar herramientas gratuitas en línea como **Colour Contrast Checker** (colourcontrast.cc) o **WebAIM Contrast Checker** (webaim.org/resources/contrastchecker). El proceso es simple: anotar el código hexadecimal del color del texto y del fondo (disponible en la paleta de Canva), introducirlos en el verificador y comprobar si pasan el nivel AA. Si no lo pasan, oscurecer el texto o aclarar el fondo hasta que el ratio supere 4,5.

**Texto alternativo (alt text):** Cuando se inserta una imagen en un documento digital, existe un campo de metadatos llamado "texto alternativo" cuya función es describir el contenido de la imagen para las personas que utilizan lectores de pantalla —herramientas que verbalizan el contenido de la pantalla para personas con discapacidad visual. En Canva, se puede añadir texto alternativo a cada imagen haciendo clic sobre ella y accediendo a las opciones de accesibilidad. Un buen texto alternativo no dice "imagen de gráfico" sino "gráfico de barras que muestra el gasto por departamento: Administración 32 %, Logística 28 %, Ventas 25 %, Otros 15 %". Cuando la imagen es puramente decorativa y no aporta información, el texto alternativo puede dejarse vacío, lo que indica al lector de pantalla que debe ignorarla.

**Tamaño de fuente:** Para materiales digitales, el tamaño mínimo recomendado para el cuerpo del texto es de **16 px**. En presentaciones proyectadas, el mínimo es de **24 pt** para el texto principal. Los subtítulos deben estar al menos 4 pt por encima del cuerpo. Un error muy frecuente en carteles y presentaciones es reducir el tamaño de la fuente para encajar más contenido: la solución no es hacer la letra más pequeña, sino reducir el contenido. Menos texto, más grande, siempre comunica mejor.

**El color como único diferenciador:** Un error de accesibilidad muy extendido es usar solo el color rojo/verde para indicar estado (por ejemplo, celdas en rojo = problema, celdas en verde = correcto). Las personas con daltonismo —que afecta aproximadamente al 8 % de los hombres y al 0,5 % de las mujeres— no perciben esa diferencia. La solución es añadir siempre un segundo diferenciador: un icono (✓ / ✗), una etiqueta de texto (OK / Revisar) o un patrón de relleno diferente. Este principio se aplica también a los gráficos de sectores o barras con múltiples categorías: si se distinguen solo por color, añadir también etiquetas directas o tramas.

**Lenguaje claro:** La accesibilidad no es solo visual. Un texto en oraciones largas, con mucha subordinación y vocabulario técnico, excluye a personas con dislexia, baja comprensión lectora o que leen en su segunda lengua. La IA es especialmente útil aquí: se le puede pedir que simplifique un texto, que lo reescriba con frases más cortas o que compruebe si hay términos que podrían sustituirse por sinónimos más comunes. Un prompt eficaz es: "Reescribe este texto para que sea comprensible para alguien sin conocimientos técnicos del tema. Frases de máximo 20 palabras, voz activa, sin siglas sin explicar. [PEGAR TEXTO]"

En resumen: aplicar criterios de accesibilidad no añade trabajo significativo si se integra desde el principio del proceso de diseño. La decisión de los colores, el tamaño de la fuente y la revisión del contraste se toman una sola vez para la plantilla base y luego se replican automáticamente en todas las piezas del kit. El texto alternativo se añade en dos minutos por imagen. Y el resultado es un material que funciona mejor para todos, no solo para quienes tienen alguna discapacidad.

> **Puntos clave:**
> - El diseño accesible es mejor diseño para todas las personas.
> - El contraste mínimo accesible es 4,5:1 según WCAG nivel AA.
> - Añadir alt text a imágenes informativas y dejar vacías las decorativas.
> - Nunca usar solo el color como diferenciador de estado o categoría.

### Prompts para comunicación accesible y clara con IA

La IA puede actuar como una especie de revisor de accesibilidad lingüística. Estos son algunos de los prompts más útiles para este fin:

Para simplificar: "Reescribe este párrafo con frases de máximo 15 palabras, eliminando el lenguaje técnico y usando voz activa. El público es personal administrativo sin formación especializada. [PEGAR TEXTO]"

Para verificar la legibilidad: "¿Este texto es comprensible para alguien con un nivel de lectura básico? ¿Qué palabras o frases cambiarías para hacerlo más accesible? [PEGAR TEXTO]"

Para reescribir con inclusión: "Este texto usa el género masculino por defecto. Reescríbelo con lenguaje inclusivo sin usar la barra (a/o) ni el lenguaje neutro marcado. Usa reestructuración de frases donde sea posible."

> **Puntos clave:**
> - La IA actúa como revisora de accesibilidad lingüística.
> - Pedir frases cortas, voz activa y sin lenguaje técnico.
> - Verificar legibilidad para nivel de lectura básico antes de publicar.
> - Reestructurar frases para lograr lenguaje inclusivo sin marcas visibles.

### La revisión humana imprescindible del kit antes de publicarlo

Por muy bien construido que esté el prompt y por muy coherente que sea el resultado visual en Canva, ningún kit de comunicación interna debería enviarse sin una revisión humana final. La IA conoce el lenguaje general pero no conoce el contexto interno de la empresa: cómo se llaman los equipos realmente, qué fórmulas de cortesía se usan, qué referencias internas pueden malinterpretarse o qué nombres de personas o departamentos aparecen en los mensajes. Marta, antes de enviar el correo sobre el nuevo sistema de pedidos, lee el texto en voz alta y verifica tres cosas: que el tono encaja con la cultura de su empresa, que los nombres y siglas internas son correctos, y que no hay errores factuales en fechas, horarios o nombres de salas. En general, dedicar cinco minutos a esta revisión evita reenvíos correctivos o malentendidos posteriores que cuestan mucho más tiempo.

> **Puntos clave:**
> - La IA escribe; la revisión humana valida el contexto interno.
> - Leer en voz alta ayuda a detectar tono extraño o fórmulas raras.
> - Verificar siempre nombres, fechas y siglas internas antes de enviar.
> - Cinco minutos de revisión evitan reenvíos correctivos posteriores.

### Reutilizar el kit: plantillas propias para futuras campañas

Crear un kit de comunicación interna desde cero requiere tiempo, aunque sea menos del que se invertía antes. La forma de rentabilizar esa inversión es convertir el kit que funciona en una plantilla reutilizable. En Canva, cualquier diseño puede guardarse como plantilla del equipo y duplicarse en futuras campañas: la paleta, las tipografías, la disposición de elementos y el espacio para el logo ya están definidos. Para una nueva campaña, Marta solo necesita cambiar los textos, las cifras y, si procede, una imagen central; el resto se mantiene. Según experiencia del sector, los equipos que estandarizan sus kits reducen drásticamente el tiempo de producción de comunicaciones internas a partir de la tercera o cuarta campaña, porque la plantilla ya está depurada y revisada en accesibilidad. Además, la coherencia visual a lo largo del tiempo refuerza la identidad de la marca interna del equipo.

> **Puntos clave:**
> - Guardar el kit como plantilla propia ahorra tiempo en campañas futuras.
> - La paleta y tipografía ya están elegidas y revisadas en accesibilidad.
> - Solo hay que cambiar textos, cifras e imagen central.
> - La coherencia visual sostenida refuerza la identidad interna del equipo.

---

## 7. DATOS Y CIFRAS CLAVE

- El **contraste mínimo recomendado** para texto normal sobre fondo es de **4,5:1** según el estándar WCAG 2.1, nivel AA (Web Content Accessibility Guidelines).
- Aproximadamente el **8 % de los hombres y el 0,5 % de las mujeres** tienen algún grado de daltonismo; en un equipo de 50 personas, pueden ser 4 o 5 personas que no perciben la diferencia entre rojo y verde.
- El tamaño de fuente mínimo recomendado para materiales digitales es de **16 px** en cuerpo de texto y **24 pt** en presentaciones proyectadas.
- Crear un kit de 3 piezas coordinadas (correo, cartel, banner) con IA + Canva: **20–30 minutos** frente a **2–3 horas** con diseño tradicional desde cero.
- Convertir un análisis de datos en una infografía con IA + Canva: **15–20 minutos** desde que se tienen los hallazgos.
- El **91 % de las organizaciones** afirma que la comunicación interna efectiva mejora el compromiso de los empleados (Gallup, 2023).
- Un vídeo interno de 30–60 segundos creado con Canva puede producirse en **menos de 1 hora** sin conocimientos previos de edición de vídeo.
- Antes / Después: diseñar un cartel de anuncio interno → antes: 45–60 min en PowerPoint desde cero; con IA + Canva: **10–15 min**.

---

## 8. EJEMPLOS RESUELTOS PASO A PASO

### Caso 1 — Infografía a partir de datos de incidencias

**Situación:** Marta tiene los hallazgos del análisis de D10: las incidencias de logística aumentaron un 30 % en mayo, el 60 % se resuelven en menos de 24 horas y el tipo más frecuente es "retraso en recepción". Quiere convertirlos en una infografía para presentar en la reunión mensual.

**Paso 1 — Prompt en ChatGPT para obtener los textos:**
> "Tengo tres hallazgos sobre incidencias de logística del primer semestre. Para cada uno, escríbeme un titular de máximo 8 palabras y una frase de contexto de máximo 18 palabras. Tono directo e informativo. Los hallazgos son: (1) Las incidencias aumentaron un 30 % en mayo; (2) El 60 % se resuelven en menos de 24 horas; (3) El tipo más frecuente es 'retraso en recepción'."

**Paso 2 — Canva:** Buscar plantilla "infografía estadísticas tres datos" en la galería gratuita. Sustituir los textos de ejemplo por los titulares y frases generados. Añadir los tres iconos temáticos (reloj, porcentaje, caja) de la biblioteca gratuita de Canva.

**Resultado:** Una infografía de una página, exportada en PNG, lista para enviar por correo o proyectar en la reunión. Tiempo total: 18 minutos.

---

### Caso 2 — Kit de 3 piezas para anuncio de nuevo software

**Situación:** El equipo de Marta debe comunicar que a partir del 1 de septiembre se usará un nuevo sistema de gestión de pedidos. Necesitan un correo, un cartel y un banner de Teams.

**Prompt exacto:**
> "Necesito comunicar internamente que nuestra empresa adopta un nuevo sistema de gestión de pedidos a partir del 1 de septiembre. Escríbeme tres textos: (1) Un correo interno de anuncio de 130–150 palabras, tono cercano y profesional, con saludo, tres puntos clave y cierre; (2) Un titular para un cartel de anuncio, máximo 10 palabras, con verbo de acción; (3) Un texto para un banner de Teams de máximo 20 palabras. Los tres mensajes clave son: la fecha (1 de septiembre), el motivo (simplificar el proceso y reducir errores) y que habrá sesiones de formación de apoyo."

**Resultado:** La IA entrega los tres textos en un solo bloque. Marta los revisa, corrige el nombre interno del sistema y los pega en las tres piezas de Canva. El kit completo está listo en 25 minutos.

---

### Caso 3 — Auditoría de accesibilidad de un cartel

**Situación:** Un grupo ha creado un cartel con texto gris claro sobre fondo blanco. Quieren verificar si es accesible.

**Paso 1 — Identificar los colores:** En Canva, hacer clic sobre el texto → ver el código hexadecimal del color (por ejemplo, #AAAAAA para gris claro) y del fondo (#FFFFFF para blanco).

**Paso 2 — Verificar contraste:** Introducir ambos códigos en colourcontrast.cc. Resultado: ratio 2,3:1 → No supera el mínimo de 4,5:1.

**Paso 3 — Corrección:** Cambiar el gris del texto a #595959 (gris oscuro). Nuevo ratio: 7:1 → Pasa nivel AAA.

**Prompt de revisión lingüística:**
> "Revisa este texto de cartel interno y dime si hay términos técnicos que podrían sustituirse por palabras más comunes, y si alguna frase supera las 20 palabras. [PEGAR TEXTO]"

---

### Caso 4 — Vídeo de bienvenida para nuevas incorporaciones

**Situación:** Marta quiere preparar un vídeo corto de bienvenida (45 segundos) para personas nuevas en el departamento, con los hitos del primer día y un saludo del equipo. Necesita un guion sencillo y una pieza visual que pueda compartirse por correo o por Teams.

**Prompt exacto:**
> "Escríbeme un guion de vídeo de bienvenida para nuevas incorporaciones a un departamento de administración. Duración objetivo: 45 segundos. Estructura: saludo cálido, tres hitos del primer día (acogida y café con el equipo, recorrido por la oficina, sesión introductoria con la responsable), cierre con invitación a preguntar. Tono cercano y profesional, frases cortas. Devuélvelo como una secuencia de cinco diapositivas con un titular breve y una línea de texto cada una."

**Resultado comentado:** La IA devuelve cinco bloques de texto numerados que Marta pega directamente en una plantilla de vídeo de Canva (sección "Vídeo · Bienvenida"). Añade música de la biblioteca gratuita, ajusta el contraste del texto al fondo y exporta el vídeo en MP4. El resultado es una pieza de 45 segundos lista para compartir en el correo de incorporación.

**Cómo iterarlo:** Si el tono resulta demasiado formal, pedir a la IA "reescribe el mismo guion con un tono más cálido y un toque de humor amable". Si el vídeo se va a compartir en Teams, pedir también una versión con un titular de máximo 10 palabras para acompañar el mensaje del chat. Tras la primera incorporación real, recoger un par de comentarios y ajustar el guion para la próxima persona; así la plantilla mejora con cada uso.

---

## 9. GLOSARIO

**Kit de comunicación:** Conjunto de piezas visuales y textuales coordinadas que transmiten un mismo mensaje a través de distintos canales (correo, cartel, banner), con coherencia visual y de tono.

**Infografía:** Representación visual de información o datos que combina texto breve, iconos y gráficos para facilitar la comprensión rápida de un tema.

**Contraste de color:** Diferencia de luminosidad entre el color del texto y el color del fondo; se mide con un ratio numérico; el mínimo accesible según WCAG es 4,5:1 para texto normal.

**WCAG (Web Content Accessibility Guidelines):** Estándar internacional de accesibilidad digital desarrollado por el W3C; el nivel AA es el de referencia para organismos públicos y muchas organizaciones privadas en España.

**Texto alternativo (alt text):** Descripción textual de una imagen que los lectores de pantalla verbalizan para personas con discapacidad visual; debe describir el contenido informativo de la imagen, no su aspecto estético.

**Lector de pantalla:** Software que convierte el texto y los elementos de la pantalla en voz sintetizada o texto braille; usado por personas con discapacidad visual para navegar y leer contenidos digitales.

**Daltonismo:** Condición visual que dificulta o impide distinguir ciertos colores, especialmente el rojo y el verde; afecta a aproximadamente el 8 % de los hombres.

**Redimensionar (Canva):** Proceso de adaptar un diseño a un nuevo formato o tamaño; en Canva gratuito se hace creando un nuevo lienzo con las dimensiones deseadas y reorganizando los elementos.

**Paleta de colores:** Conjunto de colores elegidos para un proyecto visual que garantizan coherencia estética entre todas las piezas; Canva permite guardar paletas personalizadas.

**Comunicación multicanal:** Estrategia de comunicación que usa varios canales simultáneamente (correo, cartel, chat, intranet) con el mismo mensaje central para aumentar su alcance y retención.

**Vídeo de diapositivas:** Presentación visual exportada como archivo de vídeo, con transiciones y música de fondo; Canva permite crearlo directamente desde plantillas de vídeo sin conocimientos de edición.

**Legibilidad:** Facilidad con la que un texto puede ser leído y comprendido; depende del tamaño de la fuente, el contraste, el interlineado, la longitud de las frases y el vocabulario utilizado.

**Ratio de contraste:** Valor numérico que expresa la diferencia de luminosidad entre dos colores; se calcula con una fórmula estándar y se expresa como X:1 (por ejemplo 4,5:1); cuanto mayor es el ratio, mayor el contraste.

**Código hexadecimal:** Notación de seis caracteres precedida de una almohadilla (por ejemplo #595959) que identifica de forma única un color en pantalla; en Canva aparece al hacer clic sobre cualquier color del diseño.

**Plantilla reutilizable:** Diseño base guardado en Canva que mantiene paleta, tipografía y disposición, y que se duplica para campañas posteriores cambiando solo los textos y datos.

---

## 10. ERRORES COMUNES Y BUENAS PRÁCTICAS

**Error 1 — Usar texto gris claro sobre fondo blanco por razones estéticas.** Es una de las combinaciones más habituales en plantillas de diseño moderno y una de las que más frecuentemente falla la prueba de contraste. Comprobar siempre el ratio antes de dar por bueno el diseño. La corrección es sencilla: oscurecer el texto.

**Error 2 — Usar el color como único indicador de estado.** Celdas en rojo/verde, círculos de colores para semáforos de estado, gráficos con categorías diferenciadas solo por color. Añadir siempre un segundo diferenciador: icono, etiqueta de texto o trama de relleno.

**Error 3 — No añadir texto alternativo a las imágenes informativas.** Si la imagen contiene datos, gráficos o información relevante y no tiene alt text, esa información es invisible para los lectores de pantalla. Añadir el alt text toma menos de dos minutos por imagen.

**Error 4 — Reducir el tamaño de la fuente para encajar más texto.** La solución siempre es reducir el texto, no el tamaño de la letra. Menos contenido, más grande y más claro, siempre comunica mejor.

**Error 5 — Crear las tres piezas del kit en momentos distintos sin plantilla común.** Si el correo se crea el lunes, el cartel el martes y el banner el jueves, es probable que tengan paletas de colores, tipografías o tonos distintos. Crear el kit completo en una misma sesión, con la misma plantilla base, garantiza coherencia.

**Error 6 — Pedir a la IA un texto único y usarlo en todos los canales sin adaptar.** Un correo y un banner de Teams son formatos radicalmente distintos en extensión y estructura. Pedir a la IA los tres formatos en un mismo prompt, especificando la longitud y el propósito de cada uno.

**Buena práctica — Guardar la plantilla del kit como plantilla propia en Canva.** Una vez creado un kit que funciona bien, guardarlo como plantilla del equipo para reutilizarlo en próximas campañas. Solo hay que cambiar los textos y el tema.

**Error 7 — Olvidar la revisión humana del texto generado por la IA antes de enviarlo.** La IA no conoce los nombres internos, las siglas del equipo ni las fórmulas de cortesía propias de la empresa. En general, basta con cinco minutos de revisión final (leer el texto en voz alta, comprobar nombres, fechas y siglas) para evitar reenvíos correctivos.

**Buena práctica — Mantener un repositorio compartido de prompts que funcionan bien.** Cuando un prompt produce un resultado especialmente útil (kit completo, infografía clara, revisión de accesibilidad), guardarlo en un documento compartido del equipo con una breve nota sobre cuándo usarlo. Según experiencia del sector, este repositorio reduce el tiempo de arranque de futuras campañas y eleva la calidad media de las comunicaciones internas.

---

## 11. ACTIVIDADES EN AULA

### Actividad 1 — Demo: infografía desde datos de D10 [Grupo · 15 min]

**Descripción:** El formador, en pantalla compartida, toma el dataset ficticio de incidencias de D10 y construye en directo una infografía completa: prompt en ChatGPT para obtener titulares → selección de plantilla en Canva → sustitución de textos → exportación. Todo en no más de 10 minutos de trabajo real, seguido de 5 minutos de preguntas.

**Objetivo:** Que el grupo vea el flujo completo antes de replicarlo. La demo en tiempo real, sin cortes, es fundamental: demuestra que el proceso es realmente rápido.

**Material:** Dataset ficticio de D10 en pantalla, ChatGPT o Claude en versión gratuita, Canva gratuito.

---

### Actividad 2 — Mini-campaña de comunicación interna [Grupo de 3 · 55 min]

**Descripción:** Cada grupo de tres personas recibe una de las siguientes situaciones ficticias de anuncio interno: (A) traslado de oficina a nueva planta el próximo mes, (B) implantación de nueva política de teletrabajo con solicitud de justificación previa, (C) lanzamiento de programa de bienestar con actividades mensuales voluntarias. Con esa situación, el grupo debe crear un kit de comunicación de tres piezas: un cartel de anuncio (formato A4 o pantalla), el texto de un correo electrónico interno y un banner para el canal de Teams. La IA escribe los textos base; Canva produce las tres piezas con paleta de colores coherente.

**Objetivo:** Aplicar el flujo completo de kit coordinado, con IA para textos y Canva para visuales, en un contexto cercano al trabajo real.

**Material:** Canva gratuito, ChatGPT o Claude gratuito, hoja de especificaciones de cada situación (proporcionada por el formador).

**Distribución de tareas sugerida dentro del grupo:** Una persona construye el prompt y gestiona la IA; la segunda maqueta en Canva; la tercera revisa coherencia y hace la auditoría de accesibilidad.

---

### Actividad 3 — Auditoría de accesibilidad [Individual · 25 min]

**Descripción:** Cada persona realiza una auditoría de accesibilidad de una de las piezas creadas por su grupo en la Actividad 2, usando una checklist de 5 puntos: (1) ¿El contraste de texto/fondo supera 4,5:1? — verificar en colourcontrast.cc; (2) ¿Las imágenes informativas tienen texto alternativo? — revisar en Canva; (3) ¿El texto del cuerpo es de al menos 16 px? — comprobar en Canva; (4) ¿El estado o categoría se diferencia por algo más que el color?; (5) ¿El texto tiene frases de menos de 20 palabras y sin jerga técnica? — verificar con IA si es necesario. Se documentan los hallazgos y se propone al menos una mejora concreta.

**Objetivo:** Interiorizar los criterios de accesibilidad como hábito de revisión propio, no como lista externa de requisitos.

**Material:** Checklist de accesibilidad (proporcionada por el formador), colourcontrast.cc, Canva.

---

## 12. 🔁 TRABAJO EN PAREJAS / GRUPO

En la **Actividad 2**, el grupo trabaja en **tríos** durante 55 minutos. La dinámica de roles dentro del grupo es clave: una persona gestiona la IA y construye los prompts, la segunda maqueta en Canva y la tercera actúa como revisora de coherencia y accesibilidad. Tras 30 minutos de trabajo, los grupos rotan los roles durante los últimos 25 minutos para que cada persona practique al menos dos funciones distintas. En la **puesta en común**, cada grupo presenta su kit en 3 minutos explicando: qué situación eligieron, qué prompt usaron para los textos y qué decisión de diseño o accesibilidad les resultó más significativa. El debate posterior sobre las distintas soluciones a la misma situación produce aprendizaje colectivo sobre las diferencias que genera un prompt más o menos específico.

---

## 13. EJERCICIOS SUGERIDOS

Ver Banco de Ejercicios:
- **EJ-D13-1** (Individual): Crear una infografía de 3–4 datos a partir del análisis de D10 propio, con texto generado por IA y maquetado en Canva gratuito.
- **EJ-D13-2** (Grupo): Mini-campaña con nueva situación ficticia diferente a la de clase: crear kit de 3 piezas coordinadas con IA + Canva y realizar auditoría de accesibilidad cruzada (otro grupo audita tu kit).
- **EJ-D13-3** (Individual): Tomar un material visual que uses habitualmente en tu trabajo (cartel, presentación, plantilla de correo) y pasarlo por la checklist de accesibilidad de 5 puntos. Documentar hallazgos y proponer mejoras.

---

## 14. CUESTIONARIO DE AUTOEVALUACIÓN

**1. ¿Cuál es el contraste mínimo recomendado por WCAG para texto normal sobre fondo?**
a) 2:1
b) 3:1
c) 4,5:1 ✓
d) 7:1

**2. ¿Qué es el texto alternativo (alt text) en una imagen?**
a) El pie de foto visible bajo la imagen
b) Una descripción textual de la imagen que los lectores de pantalla pueden leer en voz alta ✓
c) El título del documento que contiene la imagen
d) Un resumen del documento generado automáticamente

**3. ¿Cuál es el tamaño de fuente mínimo recomendado para el cuerpo de texto en materiales digitales?**
a) 10 px
b) 12 px
c) 14 px
d) 16 px ✓

**4. Un cartel de estado usa solo colores rojo y verde para indicar si una tarea está hecha o no. ¿Qué problema de accesibilidad tiene?**
a) El contraste entre rojo y verde siempre falla el ratio mínimo
b) Las personas con daltonismo no pueden distinguir el rojo del verde, así que el estado es ilegible para ellas ✓
c) No hay problema, los colores rojo y verde siempre tienen suficiente contraste
d) El problema es que el verde tiene connotaciones distintas en distintas culturas

**5. ¿Cuál de estos formatos es más adecuado para un anuncio urgente y puntual en la oficina?**
a) Boletín interno mensual
b) Infografía de datos
c) Cartel de anuncio breve ✓
d) Guía de incorporación

**6. ¿Qué hace el redimensionado de Canva en el plan gratuito?**
a) Crea automáticamente todas las variantes de formato con un clic
b) Permite crear un nuevo lienzo con las dimensiones deseadas y reorganizar los elementos del diseño original ✓
c) Escala automáticamente todos los textos para que no se corten
d) Exporta el diseño en todos los formatos simultáneamente

**7. ¿Cuál es la ventaja principal de crear las tres piezas del kit de comunicación en un solo prompt de IA?**
a) La IA trabaja más rápido con prompts largos
b) Se garantiza la coherencia de mensaje y tono entre las tres piezas ✓
c) El texto generado no necesita revisión porque es más preciso
d) Se obtiene un diseño visual automático en Canva

**8. ¿Cuándo es adecuado dejar el campo de texto alternativo vacío en una imagen?**
a) Cuando la imagen es muy pequeña
b) Cuando la imagen es puramente decorativa y no aporta información relevante ✓
c) Cuando la imagen ya tiene un título visible
d) Nunca, todas las imágenes deben tener texto alternativo descriptivo

**9. Verdadero o falso: el diseño accesible solo beneficia a personas con discapacidad.**
Respuesta: **Falso.** El diseño accesible beneficia a todas las personas: funciona mejor en pantallas de baja calidad, en condiciones de luz difícil, en móviles con pantalla pequeña y para personas que leen en su segunda lengua. La accesibilidad es mejor diseño para todos.

**10. ¿Cuál es el flujo correcto para crear una infografía desde datos?**
a) Diseñar en Canva → pedir textos a la IA → insertar datos
b) Seleccionar datos clave → obtener titulares con IA → elegir plantilla en Canva → sustituir textos → exportar ✓
c) Exportar la hoja de datos → subirla a Canva → añadir iconos
d) Pedir a la IA que diseñe la infografía completa directamente

**11. ¿Cómo verificas en la práctica que el contraste de un cartel supera el ratio mínimo?**
Respuesta abierta: Identificar los códigos hexadecimales del color del texto y del fondo en Canva (haciendo clic en el color elegido), introducirlos en un verificador gratuito como colourcontrast.cc o webaim.org/resources/contrastchecker, y comprobar que el ratio obtenido es igual o superior a 4,5:1.

**12. ¿Qué prompt usarías para pedir a la IA que simplifique un texto para que sea más accesible?**
Respuesta abierta: Un ejemplo válido: "Reescribe este texto con frases de máximo 15 palabras, eliminando el lenguaje técnico y usando voz activa. El público es personal administrativo sin formación especializada. [PEGAR TEXTO]"

**13. ¿Cuál de estas afirmaciones describe mejor el orden correcto al diseñar un kit multicanal?**
a) Diseñar primero el banner, después el correo y por último el cartel
b) Empezar por la pieza más grande o compleja (cartel) y adaptar los elementos a los formatos más pequeños ✓
c) Crear cada pieza por separado, en días distintos, para no influirse entre sí
d) Empezar por el vídeo y derivar el resto a partir del guion

**14. ¿Por qué conviene guardar el kit como plantilla propia en Canva tras la primera campaña?**
Respuesta abierta: Porque la paleta, las tipografías, la disposición y los criterios de accesibilidad ya están elegidos y revisados; en campañas futuras solo hay que cambiar los textos, las cifras y, si procede, una imagen central. Según experiencia del sector, esta reutilización reduce drásticamente el tiempo de producción a partir de la tercera o cuarta campaña y refuerza la coherencia visual a lo largo del tiempo.

**15. ¿Qué información mínima debe contener un buen texto alternativo para un gráfico de barras de gasto por departamento?**
a) Solo la palabra "gráfico"
b) El tipo de gráfico y las cifras o porcentajes principales por categoría, por ejemplo "gráfico de barras del gasto por departamento: Administración 32 %, Logística 28 %, Ventas 25 %, Otros 15 %" ✓
c) Una descripción estética de los colores y el tamaño
d) El nombre del archivo de la imagen

---

## 15. PREGUNTAS FRECUENTES (FAQ)

**¿Necesito tener los datos de D10 para crear la infografía de hoy?**
No es imprescindible. El formador proporciona un conjunto de datos ficticios de ejemplo para quien no los tenga. Si tienes tus propios hallazgos de D10, puedes usarlos directamente: serán más significativos porque son de tu área real (anonimizados).

**¿La función de redimensionado automático de Canva es gratuita?**
La función "Cambiar tamaño mágico" que redimensiona con un clic es exclusiva del plan de pago. En el plan gratuito, el proceso es manual: se crea un nuevo lienzo con las dimensiones deseadas y se reorganizan los elementos. Es algo más lento, pero perfectamente factible para tres piezas de un kit.

**¿El texto alternativo que añado en Canva se conserva cuando exporto el documento?**
El alt text añadido en Canva se conserva cuando se exporta en PDF accesible. Al exportar en PNG o imagen, el texto alternativo no se incluye en el archivo de imagen, pero sí en el PDF. Para documentos que van a compartirse digitalmente y leerse con lectores de pantalla, exportar en PDF es la opción más accesible.

**¿Cómo sé si mi texto supera el nivel de legibilidad adecuado?**
Puedes pegarlo en ChatGPT o Claude y preguntar: "¿Este texto tiene un nivel de lectura adecuado para personal administrativo sin conocimientos especializados? ¿Qué cambiarías para simplificarlo?" También puedes usar la herramienta gratuita Hemingway App (hemingwayapp.com), que indica el nivel de legibilidad de un texto en inglés, o Readable (readable.com) con soporte para español.

**¿La IA puede cometer errores al adaptar el tono de una comunicación interna?**
Sí. La IA puede producir textos demasiado formales, demasiado informales o con fórmulas de cortesía que no se usan en tu empresa. Siempre hay que revisar el texto generado antes de enviarlo o imprimirlo. El estilo interno de tu organización (cómo se llaman los equipos, qué nivel de formalidad se usa) es algo que tú conoces y la IA no.

**¿Puedo usar el kit de comunicación que cree hoy para el proyecto final del curso?**
Sí, absolutamente. Si tu proyecto final involucra comunicar algo a un equipo o a la organización, el kit de comunicación de hoy puede ser directamente el entregable de comunicación de ese proyecto, siempre que esté adaptado a un caso real de tu puesto.

**¿Qué hago si en mi empresa no tenemos Teams sino otro sistema de mensajería interna?**
El banner de Teams es simplemente el ejemplo del curso. Si tu empresa usa Slack, Google Chat, correo con firma gráfica o cualquier otro canal, adapta el formato a las dimensiones de ese sistema. La IA te puede ayudar a especificar el texto para cualquier canal si le dices cuál es y cuántos caracteres o palabras admite.

**¿Por qué es importante el accesibilidad en materiales de comunicación interna si los envío solo a mis compañeros?**
Porque entre tus compañeros puede haber personas con baja visión, daltonismo, dislexia u otras condiciones que afectan a cómo perciben los materiales. Además, los materiales internos a veces se reenvían, se imprimen o se proyectan en condiciones distintas a las que imaginaste al crearlos. Un material accesible funciona bien en todos esos contextos.

**¿Puedo usar la misma plantilla de Canva en sucesivas campañas sin que se note repetitiva?**
Sí, siempre que mantengas la estructura base (paleta, tipografía, disposición) y vayas cambiando los elementos que sí dependen de cada campaña: titular, imagen central, cifras, llamada a la acción y, si procede, un acento de color secundario. La coherencia visual a lo largo del tiempo, en general, refuerza la identidad interna del equipo y ayuda a que las personas reconozcan al primer vistazo que se trata de una comunicación oficial.

**¿Qué hago si la IA me devuelve un correo demasiado formal o demasiado coloquial para el tono de mi empresa?**
Iterar el prompt es la solución más rápida. Puedes pedir "reescríbelo con un tono más cercano, manteniendo el respeto profesional" o "reescríbelo con un tono más formal, sin perder claridad". También funciona dar ejemplos: pegar un correo previo de tu empresa que sí tenga el tono adecuado y pedir a la IA que imite ese registro. Según experiencia del sector, dos o tres iteraciones suelen ser suficientes para encontrar el tono correcto.

---

## 16. HERRAMIENTAS DE LA SESIÓN

- **Canva** (canva.com) — Plan gratuito; plantillas de infografía, cartel, banner y vídeo; biblioteca de iconos y elementos gratuitos; exportación en PNG y PDF.
- **ChatGPT** (chat.openai.com) — Cuenta gratuita; generación de textos para las tres piezas del kit, titulares para infografía, revisión de legibilidad.
- **Claude** (claude.ai) — Alternativa gratuita a ChatGPT; especialmente útil para tareas de revisión y simplificación de textos.
- **Google Gemini** (gemini.google.com) — Alternativa gratuita con cuenta Gmail; integrado con el ecosistema de Google.
- **Colour Contrast Checker** (colourcontrast.cc) — Herramienta gratuita en línea para verificar el ratio de contraste entre dos colores introduciendo sus códigos hexadecimales.
- **WebAIM Contrast Checker** (webaim.org/resources/contrastchecker) — Alternativa gratuita al anterior; ampliamente usada en entornos de accesibilidad web.

Ver el mapa completo en `Recursos/Herramientas_Gratuitas.md`.

---

## 17. MINI-ENTREGABLE DEL DÍA

**Nombre:** Kit de comunicación interna accesible
**Formato:** 2–3 archivos PNG o PDF exportados desde Canva + documento de texto con los prompts usados
**Contenido:** Un cartel de anuncio, el texto de un correo interno y un banner de Teams o canal equivalente, todos coherentes en paleta de colores y tono, creados para un tema real del puesto propio. El documento de texto incluye el prompt principal usado para generar los textos y los resultados de la auditoría de accesibilidad (checklist de 5 puntos con hallazgos y mejoras).
**Cómo alimenta el proyecto final:** Si el proyecto final incluye comunicar un cambio, proceso o resultado a un equipo, el kit de hoy puede incorporarse directamente como el componente de comunicación del proyecto. La experiencia de diseñar con criterios de accesibilidad desde el principio aplica a cualquier material visual que se incluya en el entregable final.

---

## 18. 🎓 HILO DEL PROYECTO FINAL

Para tu proyecto final: si tu solución implica comunicar algo a tu equipo o a la organización —un nuevo proceso, un resultado, una propuesta de mejora— el kit de comunicación de hoy (cartel + correo + banner) puede ser el componente de difusión del proyecto, diseñado ya con criterios de accesibilidad que lo harán más profesional y de mayor alcance real.

---

## 19. MENSAJE CLAVE DE LA SESIÓN

> "Comunicar con impacto no es hacer algo bonito: es hacer algo claro, coherente y que llegue a todas las personas, incluidas las que tienen distintas capacidades."

---

## 20. IDEAS PARA RECORDAR

- El diseño accesible no es un extra: es mejor diseño para todos. Un buen contraste, una fuente legible y texto alternativo en imágenes benefician a cualquier persona, en cualquier pantalla.
- Un kit de comunicación coordinado (cartel + correo + banner) comunica tres veces más que un correo solo, con apenas el doble de tiempo, si usas IA + Canva.
- La IA escribe los textos; Canva crea las piezas visuales; tú revisas la coherencia, el tono y la adecuación al contexto de tu empresa. Los tres son necesarios.
- Verificar el contraste de color lleva menos de dos minutos con herramientas gratuitas en línea. No hay excusa para no hacerlo.
- Antes de reducir el tamaño de la fuente para encajar más texto, pregúntate si el problema es la fuente o el exceso de contenido. Casi siempre es el exceso de contenido.
- Guardar el kit que funciona como plantilla propia de Canva convierte la inversión inicial en una palanca de eficiencia para campañas futuras.
- Nunca uses solo el color para diferenciar estados o categorías: añade siempre un segundo indicador (icono, etiqueta o trama) que funcione también para personas con daltonismo.

---

## 21. CONEXIÓN CON EL RESTO DEL CURSO

D13 es la segunda y última sesión del Módulo 6, dedicado a creatividad y diseño. Recoge las herramientas de presentación de D12 (Canva, imágenes con IA) y les añade la dimensión de la comunicación multicanal coordinada y la accesibilidad. Los datos que nutren la infografía vienen de D10 (análisis de datos), lo que refuerza la conexión entre el módulo de datos y el de diseño. A partir de D14, el curso entra en el Módulo 7 (flujos de trabajo y documentación), donde los materiales visuales creados hoy pueden combinarse con los procedimientos documentados para construir recursos de formación interna completos. La accesibilidad como criterio de calidad se mantendrá como hilo presente en los entregables del proyecto final.

---

## 22. FOOTER

*Brief para NotebookLM · D13 · Edición 01/26 — IA en la Oficina*
