# PLANTILLA CANÓNICA DE BRIEF — IA en la Oficina (Edición 01/26)

> **Para qué sirve este documento.** Es la fuente de verdad para redactar y revisar los 17 briefs por sesión (`D01`–`D17`). Cada brief alimenta dos flujos: (a) se sube a NotebookLM para generar los formatos cara al alumno (audio, vídeo, infografía, flashcards, cuestionario, FAQ, chat); (b) es parseado por `Scripts/generar_deck.py` para producir el deck del formador en PPTX. **No** se sube esta plantilla a NotebookLM; se suben los briefs `DXX`.

---

## ⚠️ Regla de oro del script (innegociable)

**Todo el contenido textual del PPTX del formador viene del brief. El script `generar_deck.py` no inventa pedagogía, ejemplos, prompts, datos, citas, glosario ni notas del orador.** Si el brief no lo tiene, el PPTX no lo lleva. Esto exige que el brief sea la fuente única y completa; un brief escueto produce tanto un pódcast pobre como un deck pobre.

---

## ⚠️ Títulos de sección son anclas del parser (no renombrar)

Los encabezados `## N. NOMBRE` de las 22 secciones son anclas estables que el script usa para parsear el brief. **Cualquier cambio de nombre rompe el parser.** Si necesitas añadir contenido, hazlo dentro de la sección; no cambies el título.

---

## Principios de redacción

1. **Idioma:** español de España, claro, sin tecnicismos. Si aparece un término técnico, se explica en una frase la primera vez.
2. **Frases completas y autoexplicativas.** El texto debe sonar bien **leído en voz alta**: NotebookLM genera un *Audio Overview* (pódcast) y un *Video Overview* a partir de la fuente. Nada de viñetas sueltas sin contexto en el cuerpo teórico.
3. **Documento autocontenido y rico.** Objetivo **≥ 450 líneas**. NotebookLM **fundamenta todos sus formatos en la fuente**: si el brief es escueto, el pódcast, el cuestionario o la infografía salen pobres o con relleno inventado. El script `generar_deck.py` necesita la misma densidad para producir slides con contenido real. Mejor sobra contexto que falta.
4. **Público:** personal administrativo y de oficina, sin experiencia previa en IA, perfiles diversos. Todos los ejemplos son de **tareas administrativas y financieras de oficina** (correos, informes, actas, atención al cliente, control de gastos, documentación de procesos…). No se asume perfil técnico.
5. **Solo herramientas gratuitas** usables con una **cuenta de Gmail personal** (los alumnos no tienen cuentas corporativas). Ver `Herramientas_Gratuitas.md`. **Nunca** mencionar Microsoft Copilot ni herramientas de pago como herramienta del curso (como mucho: "opcional, solo si tu empresa ya te lo proporciona").
6. **Privacidad siempre presente.** Recordar anonimizar datos reales antes de pegarlos en cualquier IA y antes de cualquier pregunta al chat del notebook.
7. **Escenario narrativo.** Cada brief tiene un personaje administrativo recurrente dentro de la sesión (p. ej. "Marta, del departamento de administración") que vive el problema y lo resuelve con IA. Da hilo al pódcast, al vídeo y a las notas del orador del deck.
8. **Tono:** directo, motivador, realista. Se cuantifica el ahorro de tiempo siempre que se pueda.

---

## Mínimos cuantitativos por sección (objetivo ≥ 450 líneas en total)

| # | Sección | Mínimo |
|---|---------|--------|
| A1 | Longitud total | **≥ 450 líneas** |
| A2 | §3 Resumen ejecutivo | 8–10 frases |
| A3 | §6 Conceptos teóricos (`### nombre`) | **≥ 8** conceptos, cada uno con párrafo 80–120 palabras + analogía + escenario "Marta" + bloque `**Puntos clave:**` |
| A4 | §7 Datos y cifras | **≥ 8** bullets con fuente o contexto |
| A5 | §8 Ejemplos resueltos | **≥ 4** casos con Situación / Prompt / Resultado / Iteración |
| A6 | §9 Glosario | **12–15** términos |
| A7 | §10 Errores comunes | **≥ 8** errores/buenas prácticas con corrección y causa |
| A8 | §14 Cuestionario | **15** preguntas mixtas con respuestas razonadas |
| A9 | §15 FAQ | **≥ 10** preguntas con respuesta de 2–4 frases |
| A10 | §20 Ideas para recordar | **7** bullets |
| A11 | §11 Actividades | **3** con modalidad, duración, consigna, entregable, rúbrica corta |

---

## Regla anti-relleno — árbol de decisión ante un déficit

Antes de añadir contenido a un brief corto, recorre estos pasos en orden. Solo si los pasos anteriores están agotados se avanza al siguiente:

1. **Ampliar cobertura del concepto existente.** ¿El concepto tiene ya la analogía cotidiana, el escenario de Marta y la comparativa antes/después? Si no, ampliar el párrafo hasta 80–120 palabras.
2. **Añadir una segunda herramienta gratuita equivalente.** ¿Hay otra herramienta gratuita del catálogo que el alumno podría usar para la misma tarea? Si sí, añadirla como subsección del concepto existente.
3. **Añadir un caso práctico adicional en §8.** ¿La situación propuesta tiene variantes realistas (por ejemplo, el mismo tipo de correo en registro formal e informal)? Si sí, añadir el Caso N+1.
4. **Ampliar datos/cifras en §7.** Buscar una estadística adicional pertinente (ahorro de tiempo, tasa de adopción, comparativa de herramientas).
5. **Ampliar cuestionario/FAQ.** ¿Hay una duda real de alumno administrativo que todavía no está respondida en §14 o §15? Si sí, añadirla.
6. **Si tras los pasos 1–5 el temario se queda corto, detenerse y preguntar** antes de proponer un sub-tema nuevo. No añadir sub-temas sin confirmación.

---

## Nota de uso del notebook (incluir literal cerca del inicio de cada brief)

> *Este documento es la fuente del notebook de hoy. Además de las diapositivas, puedes pedirle a NotebookLM un resumen en **audio** (tipo pódcast), un **vídeo**, una **infografía** o mapa mental, una **guía de estudio**, **fichas** (flashcards), un **cuestionario** para autoevaluarte, o **escribir tus preguntas en el chat**. Usa el formato con el que mejor aprendas. No escribas datos personales reales en el chat.*

---

## Estructura obligatoria — 22 secciones

El símbolo → indica qué formato de NotebookLM o del script alimenta principalmente cada sección.

### 1. Cabecera
```
# BRIEF PARA NOTEBOOKLM — DXX
## Módulo M, Sesión S de N: <título de la sesión>
## Curso: IA en la Oficina – Eficiencia y Productividad
## Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital
```
Más una línea con **Fecha**, **horario 15:00–19:00 h** y **Día X de 17**.

### 2. Contexto del curso
Programa (68 h · 17 sesiones), público, **Metodología: ~40 % teoría+demo · ~50 % práctica guiada · ~10 % puesta en común**, recap **"Sesión anterior (DXX): …"** (qué sabe ya el grupo) y la **nota de uso del notebook** (texto literal de arriba).

### 3. Resumen de la sesión (8–10 frases) → portada del deck · intro del pódcast/vídeo · documento informativo
Párrafo(s) con al menos 8 frases completas: qué se aprende hoy, por qué importa para una oficina, qué herramientas se usan, qué se llevará el alumno y cómo conecta con el día anterior y el siguiente.

### 4. Estructura de la sesión — tabla fija (240 min)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| Apertura | 15 min | Repaso de la sesión anterior + objetivos del día |
| Teórico-demostrativo | 75 min | *(3–4 conceptos clave)* |
| Descanso | 15 min | — |
| Práctica guiada | 95 min | *(práctica individual + trabajo en parejas/grupo)* |
| Puesta en común | 40 min | Revisión de entregables + mini-entregable + cierre |

*(15+75+15+95+40 = 240 min. No alterar las duraciones; solo el contenido de cada bloque.)*

### 5. Objetivos de aprendizaje
3–4 objetivos con verbo de acción, anclados a tareas de oficina.

### 6. Desarrollo teórico en prosa → pódcast · vídeo · guía de estudio · **notas del orador del deck**
**El corazón del brief.** Cada concepto en una subsección `### nombre del concepto` con **párrafos completos de 80–120 palabras**, una analogía cotidiana y el **escenario del personaje "Marta"**. Integrar tablas y comparativas. Al final de cada subsección, añadir el bloque obligatorio `**Puntos clave:**`:

```markdown
### Los tres tipos de resumen según el destinatario
[prosa rica de 80–120 palabras × N párrafos, con analogía y escenario de Marta]

> **Puntos clave:**
> - Ejecutivo: máx 5 puntos, decisiones y riesgos
> - Operativo: lista numerada de acciones con responsable
> - Divulgativo: lenguaje cotidiano sin siglas
```

El bloque `**Puntos clave:**` es **obligatorio** en cada `### concepto`. El script lo lee literal para los bullets de la slide. Sin él, el script aplica un fallback degradado (primera oración de cada párrafo) y emite warning. La prosa sigue alimentando el Audio/Video Overview. Extensión orientativa de §6: 120–200 líneas.

### 7. Datos y cifras clave → infografía · mapa mental
**≥ 8 bullets** de estadísticas, comparativas y "antes/después" con contexto o fuente (p. ej. "automatizar una tarea de 20 min × 3/semana = +50 h/año"). Formato `- texto con cifra [fuente o contexto]`.

### 8. Ejemplos resueltos paso a paso → todos los formatos · base de la práctica
**≥ 4 casos** completos, cada uno en una subsección `### Caso N — título`:
- **Situación:** descripción de la tarea real
- **Prompt:** el texto exacto que se escribe en la IA
- **Resultado:** qué devuelve la IA (resumen/extracto)
- **Cómo iterarlo:** una mejora concreta del prompt o del uso del resultado

Datos siempre ficticios/anonimizados. Usar siempre el escenario de Marta u otro personaje de oficina.

### 9. Glosario → flashcards
**12–15 términos** del día, cada uno con una frase de definición sencilla. Formato `**Término:** definición.`

### 10. Errores comunes y buenas prácticas → guía de estudio
**≥ 8 entradas** (errores + buenas prácticas). Formato `**Error N — título.** texto con causa y corrección.` o `**Buena práctica — título.** texto.` Incluir siempre privacidad/anonimización y verificación de datos (alucinaciones).

### 11. Actividades en aula → **slides de práctica del deck**
**3 actividades** con nombre completo en `### Actividad N — Título [Modalidad · NN min]`. Cada una incluye: descripción de la consigna, objetivo de aprendizaje, material necesario y rúbrica corta de evaluación. La suma de duraciones encaja en los 95 min de práctica.

### 12. 🔁 Trabajo en parejas / grupo → slide propia
Callout **explícito y separado**: qué dinámica colaborativa tiene hoy la sesión, cómo se agrupan (parejas / tríos / grupo) y qué producen juntos. **Nunca vacío.**

### 13. Ejercicios sugeridos
2–4 ejercicios del banco citados por código: `Ver Banco de Ejercicios: EJ-DXX-1 (Individual), EJ-DXX-2 (Pareja), EJ-DXX-3 (Grupo)`. Los códigos deben existir en `Banco_de_Ejercicios.md`.

### 14. Cuestionario de autoevaluación → cuestionario/quiz de NotebookLM
**15 preguntas** (mezcla de opción múltiple 4 opciones con ✓ y preguntas abiertas) **con sus respuestas razonadas** al final de la sección. Formato pregunta: `**N. ¿Pregunta?**` seguida de opciones a)/b)/c)/d) con ✓ en la correcta. Cubren los objetivos del día.

### 15. Preguntas frecuentes (FAQ) → FAQ · mejora el chat
**≥ 10 preguntas** reales que tendría un alumno administrativo, con respuesta de 2–4 frases. Formato: `**¿Pregunta?**` seguida del párrafo de respuesta.

### 16. Herramientas de la sesión
Solo gratuitas, con cuenta de Gmail personal. Enlace a `Herramientas_Gratuitas.md`. Indicar el límite gratuito relevante si aplica.

### 17. Mini-entregable del día
**Nombre · Formato · Contenido**, y una frase de **cómo alimenta el proyecto final**.

### 18. 🎓 Hilo del proyecto final
- **D01:** callout de **siembra** (el mapa de oportunidades es el germen del proyecto final).
- **D09:** callout de **checkpoint** (cada alumno fija su idea de proyecto, mitad de curso).
- **D16:** callout de **construcción**.
- **D17:** callout de **presentación**.
- **Resto de días:** una sola línea: *"Para tu proyecto final: lo de hoy te sirve para…"*.

### 19. Mensaje clave de la sesión
Una frase memorable (cita destacada).

### 20. Ideas para recordar → documento informativo · guía de estudio
**Exactamente 7 viñetas** de cierre con lo esencial. Formato `- texto`. El script emite warning si hay más o menos de 7.

### 21. Conexión con el resto del curso
De dónde viene (sesión anterior/módulo) y a dónde lleva (siguiente sesión), 3–5 líneas.

### 22. Footer
`*Brief para NotebookLM · DXX · Edición 01/26 — IA en la Oficina*`

---

## Lista de verificación antes de dar por bueno un brief

- [ ] Tiene las **22 secciones** en orden con los títulos `## N. NOMBRE` exactos (no renombrar).
- [ ] **≥ 450 líneas** y el cuerpo teórico (§6) es **prosa con párrafos completos**, no viñetas sueltas.
- [ ] Tabla de estructura = 15/75/15/95/40 (suma 240 min).
- [ ] Cero menciones de Copilot / M365 / ChatGPT Plus / herramientas de pago (salvo "opcional si tu empresa lo da").
- [ ] §6 tiene **≥ 8 conceptos** (`### nombre`) cada uno con párrafo de 80–120 palabras + analogía + escenario Marta + bloque `**Puntos clave:**` con ≤ 5 bullets de ≤ 15 palabras.
- [ ] §7 tiene **≥ 8 bullets** con cifras.
- [ ] §8 tiene **≥ 4 casos** con Situación/Prompt/Resultado/Iteración completos.
- [ ] §9 tiene **12–15 términos** de glosario.
- [ ] §10 tiene **≥ 8 entradas** (errores + buenas prácticas).
- [ ] §11 tiene **3 actividades** con modalidad, duración, consigna, entregable y rúbrica.
- [ ] Callout 🔁 no vacío y ≥ 1 actividad etiquetada Pareja o Grupo.
- [ ] Callout 🎓 (siembra/checkpoint/build/presentación en D01/D09/D16/D17; línea breve en el resto).
- [ ] §14 tiene **15 preguntas** de cuestionario con respuestas razonadas.
- [ ] §15 tiene **≥ 10 preguntas** FAQ con respuesta de 2–4 frases.
- [ ] §20 tiene **exactamente 7 bullets** de ideas para recordar.
- [ ] Ejercicios sugeridos citan códigos `EJ-DXX-N` existentes en el banco.
- [ ] Nota de uso del notebook incluida.
- [ ] Privacidad/anonimización mencionada.
- [ ] "Sesión anterior (DXX)" y "Día X de 17" correctos.

---

*Plantilla canónica · Edición 01/26 — IA en la Oficina. Mantener actualizada si cambia el estándar.*
