# BRIEF PARA NOTEBOOKLM — D10
## Módulo 5, Sesión 1: Análisis de datos sin ser experto en Excel
## Curso: IA en la Oficina – Eficiencia y Productividad
## Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital

**Fecha:** Martes 14 de julio de 2026 · 15:00–19:00 h · Día 10 de 17

---

## 2. CONTEXTO DEL CURSO

**Programa:** IA en la Oficina – Eficiencia y Productividad (68 horas · 17 sesiones de 4 horas)
**Público:** Personal administrativo y de oficina sin experiencia previa en IA generativa
**Metodología:** ~40 % teoría y demostración · ~50 % práctica guiada · ~10 % puesta en común
**Sesión anterior (D09):** El grupo ya planifica su semana, prepara reuniones eficaces, genera actas estructuradas y redacta instrucciones de delegación. Muchos han elegido ya su idea de proyecto final.

> *Este documento es la fuente del notebook de hoy. Además de las diapositivas, puedes pedirle a NotebookLM un resumen en **audio** (tipo pódcast), un **vídeo**, una **infografía** o mapa mental, una **guía de estudio**, **fichas** (flashcards), un **cuestionario** para autoevaluarte, o **escribir tus preguntas en el chat**. Usa el formato con el que mejor aprendas. No escribas datos personales reales en el chat.*

---

## 3. RESUMEN DE LA SESIÓN

Los datos están en todas partes en la oficina: hojas de gastos, registros de incidencias, presupuestos trimestrales, listas de proveedores. El problema no es la falta de datos, sino que analizarlos sin ser experto en Excel o estadística siempre ha requerido mucho tiempo o conocimientos que no todo el mundo tiene. Hoy descubrimos que la IA cambia esa ecuación por completo: con Google Sheets y Gemini, o con ChatGPT y una tabla pegada, cualquier persona puede obtener fórmulas, detectar tendencias, generar gráficos y extraer conclusiones accionables en minutos, no en horas. El único requisito previo es saber anonimizar los datos antes de subirlos. Al final de la sesión, cada alumno tendrá un mini-análisis real de su área con hallazgos concretos y una recomendación para su equipo.

---

## 4. ESTRUCTURA DE LA SESIÓN (240 min)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| Apertura | 15 min | Repaso D09 + checkpoint del proyecto final + objetivos del día |
| Teórico-demostrativo | 75 min | Google Sheets + Gemini · ChatGPT con tabla · Fórmulas en lenguaje natural · Gráficos · Interpretación |
| Descanso | 15 min | — |
| Práctica guiada | 95 min | Demo con dataset ficticio · Análisis en parejas · Hoja propia anonimizada |
| Puesta en común | 40 min | Presentación de hallazgos + mini-entregable + cierre |

*(15+75+15+95+40 = 240 min)*

---

## 5. OBJETIVOS DE APRENDIZAJE

1. Usar Google Sheets con Gemini para limpiar datos, generar fórmulas y obtener tablas dinámicas con instrucciones en lenguaje natural.
2. Pegar una tabla anonimizada en ChatGPT o Claude y obtener análisis, tendencias y recomendaciones.
3. Solicitar a la IA la creación o interpretación de un gráfico adecuado para los datos.
4. Identificar y corregir errores habituales al analizar datos con IA (alucinaciones numéricas, datos no anonimizados).

---

## 6. DESARROLLO TEÓRICO EN PROSA

### El problema de los datos en la oficina

Marta tiene en su escritorio una hoja de Excel con los gastos del primer semestre: más de 400 filas con fecha, proveedor, concepto, importe y departamento. Su jefa le ha pedido que prepare un análisis para la reunión del lunes: cuánto se ha gastado por departamento, si hay alguna anomalía y cuál es el proveedor con mayor volumen. Antes, Marta habría necesitado media tarde para hacer filtros, tablas dinámicas y un gráfico. Hoy, con IA, lo hace en veinte minutos.

El análisis de datos ha sido históricamente el dominio exclusivo de personas con formación en estadística o en herramientas avanzadas de hoja de cálculo. La IA rompe esa barrera de dos formas distintas, y las dos son accesibles con herramientas gratuitas y una cuenta de Gmail.

La primera opción es **Google Sheets con Gemini**. Desde 2024, Google ha integrado Gemini directamente en Google Sheets. Esto significa que puedes seleccionar un rango de datos, abrir el panel lateral de Gemini y escribirle en lenguaje normal lo que necesitas: "Genera una fórmula para calcular el total por departamento", "Crea una tabla dinámica con el gasto mensual por categoría", "¿Hay valores atípicos en la columna de importes?". Gemini genera la fórmula o la tabla directamente en la hoja, sin que tengas que saber la sintaxis. Esta opción es ideal cuando los datos están ya en Google Sheets y no quieres sacarlos de ahí, lo que también garantiza mayor control sobre la privacidad.

La segunda opción es **copiar la tabla y pegarla en ChatGPT o Claude**. Si tienes una hoja en Excel o Sheets, puedes seleccionar el rango, copiarlo y pegarlo directamente en el chat de cualquier IA como texto. La IA leerá la estructura de la tabla y podrá responder preguntas, calcular totales, identificar tendencias o sugerir visualizaciones. Esta opción es más flexible porque funciona con cualquier formato de tabla, y el modelo puede hacer razonamientos más complejos sobre los datos. La limitación es que la tabla tiene que ser de tamaño moderado (no miles de filas) y, sobre todo, hay que **anonimizar antes de pegar**: ningún nombre de cliente, empleado o proveedor real debe salir de tu sistema.

> **Puntos clave:**
> - Dos caminos accesibles: Gemini en Sheets o tabla pegada en ChatGPT/Claude
> - Gemini en Sheets mantiene los datos dentro de tu cuenta Google
> - Pegar en chat externo exige anonimizar previamente
> - La IA elimina la barrera de Excel para perfiles no técnicos

### Fórmulas en lenguaje natural: el fin de la sintaxis imposible

Uno de los mayores miedos de las personas no técnicas ante Excel o Sheets es la sintaxis de las fórmulas. ¿Cómo se escribe un BUSCARV? ¿Cómo se anidan condiciones en una fórmula SI? La IA elimina completamente esa barrera.

El flujo es simple: describes en palabras lo que quieres calcular, y la IA te da la fórmula lista para pegar. Por ejemplo:

- "Quiero calcular la suma de todos los importes donde la columna Departamento sea igual a 'Administración'. Los datos están en las columnas B (departamento) y D (importe), desde la fila 2 hasta la fila 400."
- La IA devuelve: `=SUMIF(B2:B400,"Administración",D2:D400)`

Y si no entiendes la fórmula que te ha dado, puedes pedirle: "Explícame qué hace cada parte de esta fórmula en lenguaje sencillo." Esto es aprendizaje y productividad a la vez.

> **Puntos clave:**
> - Describes el cálculo en palabras, la IA devuelve la fórmula lista
> - Indica rango exacto (columnas y filas) para que la fórmula compile
> - Pídele que explique la fórmula resultante para aprender la sintaxis
> - Sirve para SUMIF, BUSCARV, condicionales anidadas y fórmulas complejas

### Cómo interpretar los resultados: de números a conclusiones

Obtener números es solo el primer paso. Lo valioso es saber qué significan esos números para tu organización. La IA también ayuda aquí:

Una vez que tienes los datos calculados, puedes pegar el resumen (ya anonimizado o con datos ficticios equivalentes) en el chat y preguntar: "Estos son los totales de gasto por departamento del primer semestre. ¿Qué patrones observas? ¿Hay algo que llame la atención?" La IA identificará variaciones, proporciones inusuales y posibles áreas de análisis adicional.

El paso siguiente es convertir ese análisis en una recomendación accionable para tu equipo. El prompt para eso es: "Basándote en este análisis, redacta un párrafo de conclusiones y una recomendación concreta para el equipo de gestión. Tono ejecutivo, máximo 150 palabras."

> **Puntos clave:**
> - Calcular es el primer paso; interpretar es lo que aporta valor real
> - Pídele patrones, anomalías y posibles causas, no solo cifras
> - Cierra con párrafo ejecutivo: conclusión + recomendación accionable
> - Tu criterio profesional revisa y adapta el análisis a tu audiencia

### La regla de oro: anonimiza antes de analizar

Este punto no puede repetirse suficiente: **antes de pegar cualquier tabla en ChatGPT, Claude o cualquier herramienta de IA externa, debes anonimizar los datos**. Sustituye los nombres de clientes por CLIENTE_A, CLIENTE_B; los nombres de proveedores por PROVEEDOR_X; los nombres de empleados por EMPLEADO_1; los importes exactos puedes mantenerlos si son públicos o redondearlos a aproximaciones si son confidenciales.

Si los datos son muy sensibles y no puedes anonimizarlos suficientemente, la opción segura es trabajar únicamente con Gemini dentro de Google Sheets (los datos no salen de tu cuenta de Google) o consultar con el responsable de protección de datos de tu organización antes de proceder.

Además del riesgo de privacidad, hay un riesgo técnico específico para el análisis de datos: las **alucinaciones numéricas**. A diferencia de los textos, donde una alucinación es difícil de detectar, en los números es más frecuente y grave que la IA "calcule" un total incorrecto con total confianza. La regla es siempre verificar los cálculos de la IA con una muestra: comprueba manualmente 2 o 3 de los resultados que te ha dado para confirmar que la fórmula o el análisis es correcto.

> **Puntos clave:**
> - Sustituye nombres reales por etiquetas (CLIENTE_A, PROVEEDOR_X) antes de pegar
> - Datos muy sensibles → trabaja solo en Gemini dentro de Sheets
> - Las alucinaciones numéricas son más frecuentes que las de texto
> - Verifica manualmente 2–3 cálculos antes de presentar el análisis

### Limpiar los datos sucios: el paso previo invisible

En la oficina real, las hojas de datos rara vez llegan limpias. Marta abre el extracto de gastos y se encuentra con tres versiones del mismo proveedor (con espacios, con mayúsculas, con guiones), fechas en cuatro formatos distintos (dd/mm, mes en texto, fecha completa) y celdas vacías mezcladas con ceros literales. Un análisis hecho sobre datos sucios genera totales falsos. La limpieza es el paso previo invisible que distingue el análisis útil del análisis equivocado.

La IA simplifica drásticamente esa limpieza. Pegas una muestra de las 20 primeras filas en el chat y le pides: "Esta es una muestra de los datos. Detecta inconsistencias en los nombres de proveedor, en los formatos de fecha y en los importes. Sugiere reglas de normalización para unificarlos." La IA identifica las duplicaciones por mayúsculas, los formatos heterogéneos y las celdas problemáticas. Después, con Gemini en Sheets, puedes pedir directamente: "Crea una columna nueva que normalice los valores de la columna B convirtiéndolos todos a minúsculas y eliminando espacios al principio y al final." Lo que antes era una tarde con buscar-reemplazar, hoy son tres prompts.

La regla de oro aquí es **limpiar antes de calcular**, no después. Si Marta hace el análisis con los datos sucios y luego intenta corregirlo, los totales por departamento estarán mezclados entre "Administración" y "administración " (con espacio) como si fueran dos departamentos diferentes. Limpiar lleva 10 minutos; recalcular después de detectar el problema lleva una hora.

> **Puntos clave:**
> - Datos sucios producen totales falsos con apariencia de precisión
> - Pide a la IA detectar inconsistencias en una muestra de 20 filas
> - Normaliza con Gemini en Sheets: minúsculas, sin espacios, formato único
> - Limpia primero, calcula después — al revés cuesta seis veces más

### Comparar dos tablas: cruces, diferencias y duplicados

Una de las tareas más recurrentes para perfiles administrativos es cruzar dos listas: pedidos cobrados frente a pedidos pendientes, asistentes registrados frente a asistentes reales, facturas emitidas frente a facturas pagadas. Antes, esto requería un BUSCARV bien construido o una macro. Con IA, es una instrucción en lenguaje natural que casi cualquiera puede formular.

El planteamiento es siempre el mismo: dos tablas, una columna común que sirve de identificador (número de pedido, código de cliente anonimizado, referencia de factura) y una pregunta concreta. Por ejemplo, Marta tiene una hoja con todas las facturas emitidas en mayo y otra con los pagos recibidos. Pega ambas tablas en ChatGPT y le pide: "Cruza estas dos tablas por el campo 'referencia'. Dime qué facturas emitidas no tienen pago registrado (impagos), qué pagos no se corresponden con ninguna factura (pagos huérfanos) y si hay alguna referencia duplicada en cualquiera de las dos tablas." La IA produce tres listas separadas y un resumen breve.

Si las tablas son grandes, el mismo cruce se puede hacer con Gemini en Sheets pidiendo una fórmula de tipo BUSCARV o COINCIDIR. La IA construye la fórmula y la pega en la columna que indiques. Lo importante es nombrar bien lo que buscas (impagos, duplicados, faltantes) para que la IA estructure la respuesta de forma útil.

> **Puntos clave:**
> - Cruce de tablas con una columna común: pega las dos y pide los desajustes
> - Nombra explícitamente los tres resultados: faltantes, huérfanos, duplicados
> - Para tablas grandes, pide la fórmula y aplícala en Sheets
> - Útil para conciliación de pagos, control de asistentes y revisión de listas

### Detectar tendencias y estacionalidad en series temporales

Cuando los datos tienen una columna de fecha, aparece un análisis adicional que es enormemente valioso para la oficina: las **series temporales**. Las series temporales son simplemente datos ordenados por momento (mes, semana, día) que permiten detectar tres cosas: si el dato crece o decrece de forma sostenida (tendencia), si se repite con un patrón periódico (estacionalidad) y si hay momentos puntuales fuera de la curva (picos o caídas).

Marta tiene los gastos de los últimos doce meses agrupados por mes. Pega la tabla en el chat y le pregunta: "Analiza esta serie temporal de doce meses de gasto. ¿Hay una tendencia general (al alza, a la baja, plana)? ¿Se observa estacionalidad (algún mes que se repita con valores altos cada año)? ¿Hay picos o caídas puntuales que merezca la pena investigar?" La IA identifica el patrón estacional (los gastos suben en julio y diciembre), señala el pico de mayo como anomalía y describe la tendencia general como ligeramente creciente.

Esta capacidad transforma reuniones operativas. En vez de presentar números aislados de un mes, Marta presenta el contexto: "Mayo es un 40 % superior a la media, pero esto coincide con dos meses anteriores de subida. Hay que comprobar si es estacional o si responde a una causa específica." La interpretación es la diferencia entre un informe que se lee y un informe sobre el que se decide.

> **Puntos clave:**
> - Una columna de fecha permite analizar tendencia, estacionalidad y picos
> - Pide los tres patrones en una sola instrucción para no fragmentar
> - La estacionalidad explica anomalías aparentes y evita falsos positivos
> - Una tendencia contextualiza un número aislado y orienta la decisión

### El gráfico correcto para cada tipo de pregunta

Un error frecuente es elegir el tipo de gráfico antes de tener clara la pregunta que se quiere responder. La IA puede ayudar también aquí. La regla básica es: **barras** para comparar categorías (qué departamento gasta más), **líneas** para mostrar evolución en el tiempo (cómo varía el gasto mes a mes), **sectores** (tartas) para mostrar proporción sobre un total (qué porcentaje representa cada categoría sobre el gasto total) y **dispersión** para mostrar relación entre dos variables (ingresos frente a horas trabajadas, por ejemplo).

Cuando Marta no está segura, pega los datos en el chat y le pregunta: "Estos son los datos. La pregunta que quiero responder es: ¿qué departamento gasta más por mes? ¿Qué tipo de gráfico es el más adecuado y por qué?" La IA elige (en este caso, gráfico de barras agrupadas por mes) y explica el razonamiento. Después puede pedir a Gemini en Sheets que cree el gráfico directamente, o seguir los pasos manuales que la IA le ha indicado.

El otro consejo importante es **no sobrecargar el gráfico**. Si la tabla tiene cinco años de datos y veinte categorías, un gráfico que incluya todo es ilegible. La IA puede ayudar a filtrar: "Quédate con los últimos doce meses y con las cinco categorías de mayor volumen; las demás agrúpalas en 'Otras'." Un gráfico legible vale más que un gráfico exhaustivo.

> **Puntos clave:**
> - Barras comparan; líneas muestran evolución; tartas reparten; dispersión relaciona
> - Define primero la pregunta, después elige el tipo de gráfico
> - Pídele a la IA que justifique la elección antes de generar el gráfico
> - Un gráfico legible filtra y agrupa; no busca mostrar todos los datos

---

## 7. DATOS Y CIFRAS CLAVE

- Un perfil administrativo puede dedicar entre 2 y 4 horas a preparar un análisis de datos básico que con IA se reduce a 20–30 minutos.
- Generar una tabla dinámica en Google Sheets con Gemini mediante lenguaje natural: menos de 2 minutos (vs. 15–20 minutos aprendiendo la función manualmente).
- El 68 % de los errores en informes de datos de oficina provienen de fórmulas introducidas manualmente sin verificación posterior (estudio McKinsey 2023).
- Antes / Después: identificar el top 5 proveedores por volumen de gasto en una hoja de 300 filas → antes: 25–40 min; con IA: 3–5 min.
- Antes / Después: explicar una tendencia de ventas con un párrafo ejecutivo → antes: 30 min; con IA: 5 min.
- Las empresas que usan análisis de datos para tomar decisiones operativas tienen un 23 % más de eficiencia en sus procesos administrativos.
- Un gráfico de barras generado en Google Sheets con instrucción en lenguaje natural: 1–2 minutos.

---

## 8. EJEMPLOS RESUELTOS PASO A PASO

### Caso 1 — Análisis de gastos por departamento

**Situación:** Marta tiene una hoja con 400 registros de gastos del semestre (fecha, departamento, proveedor, concepto, importe). Necesita un resumen por departamento para la reunión del lunes.

**Paso 1 — Anonimizar:** Marta sustituye los nombres de proveedores reales por PROVEEDOR_A, PROVEEDOR_B, etc. Los departamentos puede dejarlos genéricos (Administración, Ventas, Logística) ya que son categorías internas, no datos personales.

**Paso 2 — Prompt exacto en ChatGPT (con tabla pegada):**
> "Te pego a continuación una tabla de gastos del primer semestre. Analízala y dime: (1) total gastado por departamento, (2) mes con mayor gasto total, (3) los 3 proveedores con mayor volumen acumulado, (4) si hay algún importe que parezca anómalo respecto al resto. [PEGAR TABLA ANONIMIZADA]"

**Resultado comentado:** La IA devuelve un análisis estructurado con los cuatro puntos. Marta verifica manualmente el total por departamento de administración (que es el suyo) para confirmar que el cálculo es correcto. Detecta que los totales son precisos.

**Cómo iterarlo:** "Ahora redacta un párrafo de conclusiones de máximo 100 palabras para presentar en la reunión de dirección del lunes. Tono directo y ejecutivo."

---

### Caso 2 — Fórmula en lenguaje natural con Gemini en Google Sheets

**Situación:** Marta quiere calcular, en una nueva columna, el porcentaje que representa cada gasto sobre el total de su departamento.

**Prompt exacto en Gemini (dentro de Google Sheets):**
> "En la columna F, calcula el porcentaje que representa cada importe (columna D) sobre el total de la columna D donde el departamento (columna B) sea igual al valor de la celda B de esa misma fila. Los datos van de la fila 2 a la 400."

**Resultado comentado:** Gemini genera la fórmula con referencias absolutas correctas. Marta la aplica a toda la columna. Ha aprendido una fórmula compleja sin necesitar un manual.

**Cómo iterarlo:** "¿Cómo ordenaría esta hoja de mayor a menor porcentaje dentro de cada departamento? Dame los pasos."

---

### Caso 3 — Interpretación de tendencia y recomendación

**Situación:** Marta ya tiene los totales por mes. Los gastos de mayo son un 40 % superiores a la media. Quiere entender qué significa esto antes de presentarlo.

**Prompt exacto:**
> "El gasto total de mayo fue de 18.500 € cuando la media mensual es de 13.200 €. Es un 40 % por encima. Las categorías que más contribuyeron a ese exceso fueron 'Material de oficina' (3.100 € extra) y 'Servicios externos' (2.200 € extra). ¿Qué explicaciones posibles habría para este pico? ¿Qué preguntas debería hacerle a los responsables de esas áreas antes de concluir que es un problema?"

**Resultado comentado:** La IA proporciona un listado de causas posibles (campaña especial, compra anticipada, imprevistos) y preguntas concretas para verificar. Marta llega a la reunión preparada, no solo con datos sino con las preguntas correctas.

---

## 9. GLOSARIO

**Tabla dinámica:** Herramienta de hoja de cálculo que resume grandes volúmenes de datos agrupándolos por categorías; con IA, se puede crear con una instrucción en lenguaje natural.

**Alucinación numérica:** Error específico de la IA al analizar datos: calcular un resultado incorrecto con total confianza; siempre verificar manualmente los cálculos clave.

**Fórmula SUMIF / SUMAR.SI:** Fórmula de hoja de cálculo que suma solo los valores que cumplen una condición específica; puede pedirse a Gemini o ChatGPT en lenguaje natural.

**Anonimización de datos:** Proceso de sustituir datos identificativos (nombres, cuentas, DNI) por etiquetas genéricas antes de procesarlos con una IA externa; obligatorio antes de pegar cualquier tabla.

**Valor atípico (outlier):** Dato que se aleja significativamente del resto; la IA puede identificarlos automáticamente y sugerir si son errores o eventos reales.

**Lenguaje natural:** Forma de comunicarse con la IA usando frases normales en lugar de comandos técnicos o sintaxis de programación.

**Gemini en Sheets:** Funcionalidad de Google que integra el modelo de IA Gemini directamente dentro de Google Sheets, permitiendo generar fórmulas, tablas dinámicas y análisis sin salir de la hoja.

**Visualización de datos:** Representación gráfica de datos (barras, líneas, sectores) que facilita detectar patrones; se puede solicitar a la IA con instrucciones en lenguaje natural.

**Tendencia:** Dirección general que siguen los datos a lo largo del tiempo (crecimiento, descenso, estacionalidad); uno de los análisis más valiosos que la IA puede extraer automáticamente.

---

## 10. ERRORES COMUNES Y BUENAS PRÁCTICAS

**Error 1 — Pegar datos sin anonimizar.** El error más grave y más fácil de evitar: sustituir nombres reales por etiquetas genéricas antes de pegar cualquier tabla. Si los datos son de clientes, empleados o proveedores, anonimizar es obligatorio.

**Error 2 — Confiar en los cálculos de la IA sin verificar.** A diferencia del texto, donde las alucinaciones son difíciles de detectar, en los números son más frecuentes. Comprueba siempre al menos 2–3 resultados manualmente antes de presentar el análisis.

**Error 3 — Pegar tablas demasiado grandes.** Los modelos de IA tienen límites de contexto. Una tabla de miles de filas puede truncarse o analizarse de forma incompleta. Si la hoja es muy grande, trabaja con una muestra representativa o usa Gemini directamente en Google Sheets.

**Error 4 — Pedir análisis sin dar contexto del negocio.** "¿Qué te parece esta tabla?" es un prompt pobre. La IA no sabe si un gasto de 5.000 € es normal o anómalo para tu empresa. Da siempre el contexto: sector, tamaño de la empresa, qué representa cada columna.

**Error 5 — Presentar el análisis de la IA directamente.** El análisis es un punto de partida, no el producto final. Revisa las conclusiones, añade tu criterio profesional y adapta el lenguaje a tu audiencia.

**Buena práctica — Guarda los prompts de análisis que funcionan.** Un buen prompt de análisis puede reutilizarse cada mes con los nuevos datos. Guárdalo en tu Google Doc de biblioteca de prompts.

---

## 11. ACTIVIDADES EN AULA

### Actividad 1 — Demo: dataset de gastos ficticios [Grupo · 20 min]

**Descripción:** El formador proporciona un dataset ficticio de 50 filas (gastos trimestrales de una empresa inventada). En pantalla, el grupo trabaja colectivamente para extraer 3 hallazgos clave y sugerir un gráfico, usando tanto ChatGPT con tabla pegada como Gemini en Sheets.

**Objetivo:** Que los alumnos vean el flujo completo (tabla → prompt → análisis → gráfico) antes de hacerlo solos.

**Material:** Dataset ficticio en Google Sheets (enlace compartido por el formador).

---

### Actividad 2 — Análisis en parejas con dataset del curso [Pareja · 45 min]

**Descripción:** Por parejas, los alumnos reciben un dataset ficticio diferente al de la demo (registro de incidencias de un departamento de atención al cliente). Deben responder 5 preguntas de análisis usando IA: totales por categoría, tendencia mensual, incidencia más frecuente, mes con más casos, y propuesta de mejora basada en los datos.

**Objetivo:** Aplicar el flujo completo de análisis con IA en un caso más complejo que la demo, con apoyo mutuo.

**Material:** Dataset de incidencias (Google Sheets compartido).

---

### Actividad 3 — Mi hoja real anonimizada [Individual · 30 min]

**Descripción:** Cada alumno trae o construye una versión anonimizada de una hoja de datos real de su trabajo (puede ser una tabla de gastos, un registro de tareas, un listado de pedidos). Obtiene al menos 3 hallazgos usando IA y redacta un párrafo de conclusiones.

**Objetivo:** Conectar lo aprendido con la realidad inmediata del puesto.

**Material:** Hoja de datos del alumno (anonimizada previamente), ChatGPT o Gemini en Sheets.

---

## 12. 🔁 TRABAJO EN PAREJAS

En la **Actividad 2**, el grupo trabaja en **parejas** durante 45 minutos. Cada pareja recibe el mismo dataset de incidencias y colabora para responder las 5 preguntas de análisis. La dinámica permite que una persona formule los prompts mientras la otra revisa los resultados y plantea preguntas de seguimiento; después se intercambian los roles. Al final, cada pareja presenta su hallazgo más sorprendente al grupo. La presentación breve al grupo en la puesta en común refuerza la consolidación del aprendizaje y genera debate sobre las distintas interpretaciones que puede producir la misma tabla analizada con prompts diferentes.

---

## 13. EJERCICIOS SUGERIDOS

Ver Banco de Ejercicios:
- **EJ-D10-1** (Individual): Análisis de hoja de datos propia con 3 preguntas de negocio
- **EJ-D10-2** (Pareja): Dataset compartido con 5 preguntas de análisis y presentación de hallazgos
- **EJ-D10-3** (Grupo): Comparativa de análisis del mismo dataset con ChatGPT vs Gemini en Sheets

---

## 14. CUESTIONARIO DE AUTOEVALUACIÓN

**1. ¿Qué ventaja tiene usar Gemini dentro de Google Sheets frente a pegar la tabla en ChatGPT?**
a) Gemini es más inteligente
b) Los datos no salen de tu cuenta de Google, lo que mejora la privacidad ✓
c) ChatGPT no puede analizar tablas
d) Gemini es más rápido

**2. ¿Qué debes hacer ANTES de pegar una tabla con datos de clientes o empleados en ChatGPT?**
a) Convertirla a PDF
b) Reducirla a menos de 10 filas
c) Anonimizar los datos identificativos ✓
d) Pedirle a ChatGPT que borre los datos al terminar

**3. ¿Cómo se llama el error de la IA que consiste en calcular un número incorrecto con total confianza?**
a) Error de sintaxis
b) Alucinación numérica ✓
c) Desbordamiento de contexto
d) Error de formato

**4. Si tienes una hoja de 5.000 filas que quieres analizar con ChatGPT, ¿cuál es la estrategia recomendada?**
a) Pegar todas las filas de golpe
b) Trabajar con una muestra representativa o usar Gemini en Sheets ✓
c) Exportar a PDF y subirlo
d) Dividir la hoja en hojas de 100 filas cada una y pegar todas

**5. ¿Para qué sirve la fórmula SUMIF (SUMAR.SI)?**
Respuesta abierta: Para sumar solo los valores de un rango que cumplan una condición específica. Por ejemplo, sumar todos los importes donde el departamento sea "Administración".

**6. ¿Por qué es importante dar contexto del negocio al pedir un análisis a la IA?**
a) Para que la IA genere gráficos más bonitos
b) Porque sin contexto la IA no puede distinguir si un valor es normal o anómalo para tu organización ✓
c) Para que la respuesta sea más larga
d) El contexto no importa en análisis numérico

**7. ¿Cuál es el flujo correcto para analizar datos con IA?**
a) Pegar datos → publicar resultado directamente
b) Anonimizar → pegar con contexto → analizar → verificar manualmente → conclusión propia ✓
c) Generar gráfico → buscar tendencia → publicar
d) Pedir a la IA que limpie los datos primero sin revisarlos

**8. ¿Qué es un valor atípico (outlier) en un conjunto de datos?**
Respuesta abierta: Un dato que se aleja significativamente del resto del conjunto. Puede ser un error de entrada de datos o un evento real inusual. La IA puede identificarlos automáticamente al analizar una tabla.

**9. Verdadero o falso: la IA siempre calcula correctamente los totales de una tabla numérica.**
Respuesta: **Falso**. La IA puede cometer errores de cálculo (alucinaciones numéricas). Siempre hay que verificar manualmente al menos una muestra de los resultados antes de usar el análisis.

**10. ¿Cómo pides a la IA una fórmula para calcular el promedio de ventas por mes cuando los datos están en las columnas A (mes) y B (ventas)?**
Respuesta abierta: Un buen prompt sería: "Genera la fórmula de Google Sheets para calcular el promedio de los valores de la columna B (ventas) agrupados por el valor de la columna A (mes). Los datos van de la fila 2 a la fila 100."

---

## 15. PREGUNTAS FRECUENTES (FAQ)

**¿Necesito saber Excel o Sheets para beneficiarme de esta sesión?**
No. Precisamente ese es el punto: la IA elimina la necesidad de conocer la sintaxis de las fórmulas o la mecánica de las tablas dinámicas. Describes en palabras lo que quieres y la IA te da el resultado.

**¿Puedo analizar datos confidenciales de mi empresa con ChatGPT?**
Solo si los anonimizas previamente: sustituye nombres, IDs, datos de clientes y empleados por etiquetas genéricas. Si no puedes anonimizarlos suficientemente, usa Gemini dentro de Google Sheets, donde los datos no salen de tu cuenta de Google.

**¿Qué pasa si la tabla es muy grande y no cabe en el chat?**
Trabaja con una muestra representativa (50–100 filas) o usa Gemini directamente en Google Sheets, que puede procesar la hoja completa sin necesidad de copiarla.

**¿Cómo sé si el cálculo que me ha dado la IA es correcto?**
Verifica manualmente 2–3 resultados. Si los totales coinciden con lo que calculas a mano, es probable que el resto también sea correcto. Nunca presentes un análisis sin haber comprobado al menos una muestra.

**¿Gemini en Google Sheets está disponible en las cuentas gratuitas?**
La disponibilidad de Gemini en Sheets para cuentas gratuitas puede variar según la región. Si no está disponible, el flujo alternativo (pegar tabla en ChatGPT) da resultados igualmente buenos para las prácticas del curso.

**¿Puedo pedirle a la IA que genere el gráfico por mí?**
La IA puede indicarte qué tipo de gráfico es más adecuado y darte los pasos para crearlo en Sheets, pero no puede "clicar" por ti para generarlo. Gemini en Sheets puede sugerir y crear visualizaciones básicas directamente si tienes esa funcionalidad activa.

**¿Qué hago si la IA me da una fórmula que no funciona?**
Copia el mensaje de error de Sheets y pégalo en el chat: "Esta fórmula da el siguiente error: [PEGAR ERROR]. ¿Cómo la corrijo?" La IA suele resolver el problema en el segundo intento.

---

## 16. HERRAMIENTAS DE LA SESIÓN

- **Google Sheets** con **Gemini** (google.com/sheets) — Accesible con cuenta Gmail; Gemini integrado puede no estar disponible en todas las regiones o cuentas gratuitas.
- **ChatGPT** (chat.openai.com) — Para análisis por copy-paste de tabla anonimizada; cuenta gratuita.
- **Claude** (claude.ai) — Alternativa a ChatGPT para análisis de tablas; especialmente bueno con textos y datos de cierta complejidad; cuenta gratuita.

Ver el mapa completo en `Recursos/Herramientas_Gratuitas.md`.

---

## 17. MINI-ENTREGABLE DEL DÍA

**Nombre:** Mi mini-análisis de datos
**Formato:** Google Doc o texto en el cuaderno digital
**Contenido:** Análisis de una hoja de datos real (anonimizada) o del dataset del curso: 5 hallazgos clave (en bullets), 1 gráfico o tabla resumen, 1 recomendación para el equipo.
**Cómo alimenta el proyecto final:** Si el proyecto final del alumno involucra datos (gastos, registros, seguimiento de indicadores), los prompts y el flujo de hoy son directamente reutilizables en la fase de construcción de D16.

---

## 18. 🎓 HILO DEL PROYECTO FINAL

Para tu proyecto final: si tu solución implica analizar datos o generar informes a partir de hojas de cálculo, los prompts de análisis, las fórmulas en lenguaje natural y el flujo de interpretación que aprendiste hoy son parte de tu caja de herramientas para construirlo en D16.

---

## 19. MENSAJE CLAVE DE LA SESIÓN

> "Los datos sin análisis son solo ruido. Los datos con IA son decisiones. No necesitas ser analista ni dominar Excel: necesitas saber qué pregunta hacerle a la hoja de cálculo. Hoy aprendemos a hacer las preguntas correctas."

---

## 20. IDEAS PARA RECORDAR

- Anonimiza siempre antes de pegar cualquier tabla en una IA externa: nombres → CLIENTE_A, importes sensibles → aproximaciones.
- Gemini en Sheets mantiene los datos dentro de tu cuenta Google; ChatGPT requiere anonimización pero es más flexible.
- Las alucinaciones numéricas existen: verifica siempre 2–3 cálculos manualmente antes de presentar el análisis.
- No es suficiente con tener los números: usa la IA también para interpretar qué significan y qué recomienda hacer.
- Los prompts de análisis que funcionan se reutilizan cada mes con nuevos datos; guárdalos en tu biblioteca de prompts.

---

## 21. CONEXIÓN CON EL RESTO DEL CURSO

Esta sesión abre el Módulo 5, dedicado a datos y búsqueda de información. Llega justo en la segunda mitad del curso (D10 de 17), cuando el grupo ya tiene base sólida de prompts y redacción (M2–M3) y organización (M4). El análisis de datos con IA es la extensión natural de los resúmenes y transformaciones de formato aprendidos en D05: la diferencia es que ahora el material no es texto, sino números en una tabla. En **D11** (mañana) el módulo continúa con búsqueda, síntesis e informes de mercado, donde la capacidad de interpretar datos es igualmente necesaria. Los hallazgos de hoy pueden nutrir directamente el mini-análisis que sirva de base para el proyecto final en D16.

---

## 22. FOOTER

*Brief para NotebookLM · D10 · Edición 01/26 — IA en la Oficina*
