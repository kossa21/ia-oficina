# IA en la Oficina – Eficiencia y Productividad
## Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital

**68 horas · 17 sesiones de 4h · 1–23 julio 2026 · 15:00–19:00h**
**Formadora:** Ananda (Anandamaya Arnó) · AllWomen · ananda@allwomen.tech

---

## Estructura del repositorio

```
Edicion 01-26/
├── README.md                          ← este archivo
├── Briefs/
│   ├── D01_Brief_NotebookLM.md        ← fuente del notebook D01
│   ├── D02_Brief_NotebookLM.md
│   ├── ... (D01–D17)
│   └── Modulos_overview/              ← referencia para el formador (no fuente de notebook)
│       ├── M1_Brief_NotebookLM.md
│       ├── M2_Brief_NotebookLM.md
│       ├── M3_Brief_NotebookLM.md
│       └── M4_Brief_NotebookLM.md
├── Recursos/
│   ├── Plantilla_Brief.md             ← plantilla canónica de 22 secciones
│   ├── Banco_de_Ejercicios.md         ← ejercicios alternativos (EJ-DXX-N) para el formador
│   ├── Herramientas_Gratuitas.md      ← mapa de herramientas aprobadas (todas gratuitas con Gmail)
│   ├── NotebookLM_Prompts_Referencia.md ← prompts por sesión y por formato
│   └── Guia_Alumno_NotebookLM.md     ← guía para el alumno: cómo usar el notebook del día
├── Contexto/
│   ├── CONTEXTO_PROYECTO.md           ← contexto completo para continuar trabajo con Claude
│   └── Course requirements.pdf        ← requisitos del cliente (Fundación ONCE/INSERTA)
├── Decks/                             ← PPTX generados y procesados (no editar directamente)
├── Logos/
│   └── 00_FULL COLOR (1).png          ← logo AllWomen (esquina superior derecha, 1.2")
└── Scripts/
    ├── pipeline_ia_oficina.py         ← pipeline completo: brief → NotebookLM → PPTX
    └── process_decks.py               ← solo fase 2: añade logo + speaker notes a PPTX
```

---

## Workflow de producción (por sesión)

### Paso 1 — Brief
El brief `DXX_Brief_NotebookLM.md` es la **fuente única** de cada notebook. Contiene:
- Teoría en prosa con escenario de oficina (para podcast/vídeo)
- Ejemplos resueltos paso a paso (con prompts exactos)
- Glosario, cuestionario con respuestas, FAQ (para flashcards/quiz)
- Actividades etiquetadas Individual/Pareja/Grupo
- Callouts 🔁 (trabajo colaborativo) y 🎓 (hilo del proyecto final)

### Paso 2 — Notebook en NotebookLM
1. Abre [notebooklm.google.com](https://notebooklm.google.com)
2. Crea un notebook con el nombre estándar: `IA Oficina 01/26 — DXX [Tema]`
3. Sube el brief como **única fuente**
4. Usa los prompts de `Recursos/NotebookLM_Prompts_Referencia.md` para pre-generar formatos
5. Comparte el enlace en modo público (anyone with the link)
6. Envía el enlace a los alumnos al inicio de cada sesión

### Paso 3 — Procesado del deck (en el Mac)
```bash
# Procesar un deck con logo AllWomen + speaker notes:
python3 Scripts/process_decks.py Decks/D05_raw.pptx

# Pipeline completo (crea notebook + genera deck + procesa):
python3 Scripts/pipeline_ia_oficina.py D05 D06 D07
```

---

## Herramientas aprobadas

**Solo herramientas gratuitas con cuenta Gmail personal.** Ver detalles completos en `Recursos/Herramientas_Gratuitas.md`.

| Para... | Herramienta |
|---------|------------|
| Redacción y análisis | ChatGPT (free), Gemini (free), Claude (free) |
| Notebook del alumno | Google NotebookLM (free) |
| Diseño y presentaciones | Canva (plan gratuito) |
| Búsqueda e investigación | Perplexity (free), Google |
| Documentos | Google Docs / Sheets / Slides / Forms / Drive |
| Prompts guardados | Gemini Gems (free) o Google Doc personal |
| Transcripción | Subtítulos Meet, Tactiq (free tier) |

Microsoft Copilot **no se usa** en este curso (requiere licencia M365).

---

## Calendario de sesiones

| Día | Fecha | Módulo | Sesión |
|-----|-------|--------|--------|
| D01 | Mié 1 Jul | M1 | IA generativa, herramientas y privacidad |
| D02 | Jue 2 Jul | M2 | Prompts básicos — R-C-T-F-R |
| D03 | Vie 3 Jul | M2 | Prompts avanzados — encadenamiento |
| D04 | Lun 6 Jul | M3 | Automatización de tareas repetitivas |
| D05 | Mar 7 Jul | M3 | Resúmenes y transformación de formatos |
| D06 | Mié 8 Jul | M3 | Correos profesionales |
| D07 | Jue 9 Jul | M3 | Redacción de informes |
| D08 | Vie 10 Jul | M4 | Planificación semanal y reuniones |
| D09 | Lun 13 Jul | M4 | Actas, seguimiento y delegación ★ checkpoint proyecto |
| D10 | Mar 14 Jul | M5 | Análisis de datos sin Excel |
| D11 | Mié 15 Jul | M5 | Búsqueda e informes de mercado |
| D12 | Jue 16 Jul | M6 | Canva con IA — presentaciones |
| D13 | Vie 17 Jul | M6 | Material visual y accesibilidad |
| D14 | Lun 20 Jul | M7 | Gestión documental y flujos |
| D15 | Mar 21 Jul | M7 | Atención al cliente |
| D16 | Mié 22 Jul | M8 | Taller proyecto personal |
| D17 | Jue 23 Jul | M8 | Presentaciones finales y cierre |

**Hilo del proyecto final:** D01 (siembra) → D09 (checkpoint) → D16 (build) → D17 (presentación)

---

## Para continuar trabajo con Claude

Abre `Contexto/CONTEXTO_PROYECTO.md` — contiene el estado de avance, las decisiones tomadas, y el workflow completo.
