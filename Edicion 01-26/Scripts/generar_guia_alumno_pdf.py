#!/usr/bin/env python3
"""
Genera Guia_Alumno_NotebookLM.pdf a partir de una plantilla HTML embebida.
Uso: python3 Scripts/generar_guia_alumno_pdf.py
Salida: Recursos/Guia_Alumno_NotebookLM.pdf
"""

import base64
import os
from pathlib import Path
from weasyprint import HTML, CSS

# ── Rutas ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
BASE       = SCRIPT_DIR.parent
LOGO_PATH  = BASE / "Logos" / "00_FULL COLOR (1).png"
OUT_PATH   = BASE / "Recursos" / "Guia_Alumno_NotebookLM.pdf"

# ── Logo en base64 ─────────────────────────────────────────────────────────────
with open(LOGO_PATH, "rb") as f:
    LOGO_B64 = base64.b64encode(f.read()).decode()

# ── HTML ───────────────────────────────────────────────────────────────────────
HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  /* ── Variables de color AllWomen ── */
  :root {{
    --blue:   #2B5CE6;
    --orange: #E8601A;
    --cream:  #F5EFE6;
    --cream2: #EDE3D8;
    --dark:   #1A1A2E;
    --mid:    #3D3D5C;
    --light:  #F9F7F4;
    --white:  #FFFFFF;
  }}

  /* ── Reset y base ── */
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 9.5pt;
    color: var(--dark);
    background: var(--white);
    line-height: 1.45;
  }}

  /* ══════════════════════════════════════
     PÁGINA 1
  ══════════════════════════════════════ */
  .page {{
    width: 210mm;
    min-height: 297mm;
    padding: 0;
    page-break-after: always;
    background: var(--white);
  }}

  /* ── Cabecera / portada ── */
  .header {{
    background: var(--blue);
    color: white;
    padding: 22pt 28pt 18pt;
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
  }}
  .header-text {{ flex: 1; }}
  .header-tag {{
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 1.5pt;
    text-transform: uppercase;
    color: rgba(255,255,255,0.7);
    margin-bottom: 6pt;
  }}
  .header h1 {{
    font-size: 22pt;
    font-weight: 900;
    line-height: 1.1;
    letter-spacing: -0.5pt;
  }}
  .header h1 span {{ color: #FFB347; }}
  .header-sub {{
    margin-top: 6pt;
    font-size: 9pt;
    color: rgba(255,255,255,0.85);
  }}
  .header-logo {{
    width: 54pt;
    margin-left: 20pt;
    flex-shrink: 0;
  }}
  .header-logo img {{ width: 100%; }}

  /* ── Franja naranja ── */
  .stripe {{
    background: var(--orange);
    height: 5pt;
  }}

  /* ── Intro ── */
  .intro {{
    background: var(--cream);
    padding: 12pt 28pt;
    border-bottom: 1pt solid var(--cream2);
  }}
  .intro p {{
    font-size: 9.5pt;
    color: var(--mid);
    line-height: 1.5;
  }}
  .intro strong {{ color: var(--dark); }}

  /* ── Paso 1: Cómo abrir ── */
  .section {{
    padding: 14pt 28pt;
  }}
  .section-title {{
    font-size: 11pt;
    font-weight: 800;
    color: var(--blue);
    text-transform: uppercase;
    letter-spacing: 0.8pt;
    margin-bottom: 10pt;
    padding-bottom: 5pt;
    border-bottom: 2pt solid var(--orange);
    display: inline-block;
  }}

  /* Pasos numerados */
  .steps {{
    display: flex;
    gap: 10pt;
    flex-wrap: wrap;
  }}
  .step {{
    flex: 1;
    min-width: 80pt;
    background: var(--light);
    border-radius: 6pt;
    padding: 10pt 11pt;
    position: relative;
    border: 1pt solid var(--cream2);
  }}
  .step-num {{
    width: 20pt;
    height: 20pt;
    background: var(--blue);
    color: white;
    border-radius: 50%;
    font-size: 10pt;
    font-weight: 900;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 6pt;
  }}
  .step p {{
    font-size: 8.5pt;
    color: var(--mid);
    line-height: 1.4;
  }}
  .step strong {{ color: var(--dark); font-size: 9pt; display: block; margin-bottom: 3pt; }}

  /* ── Grid de formatos ── */
  .formats-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 9pt;
    padding: 0 28pt 14pt;
  }}
  .format-card {{
    border-radius: 8pt;
    padding: 10pt 12pt;
    border: 1pt solid var(--cream2);
    background: var(--light);
    position: relative;
    overflow: hidden;
  }}
  .format-card::before {{
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 4pt;
    height: 100%;
  }}
  .fc-audio::before   {{ background: #E8601A; }}
  .fc-video::before   {{ background: #2B5CE6; }}
  .fc-info::before    {{ background: #10B981; }}
  .fc-study::before   {{ background: #8B5CF6; }}
  .fc-brief::before   {{ background: #F59E0B; }}
  .fc-flash::before   {{ background: #EF4444; }}
  .fc-quiz::before    {{ background: #06B6D4; }}
  .fc-faq::before     {{ background: #84CC16; }}
  .fc-chat::before    {{ background: #EC4899; }}

  .format-icon {{
    font-size: 18pt;
    line-height: 1;
    margin-bottom: 5pt;
    display: block;
  }}
  .format-name {{
    font-size: 9.5pt;
    font-weight: 800;
    color: var(--dark);
    margin-bottom: 3pt;
  }}
  .format-desc {{
    font-size: 8pt;
    color: var(--mid);
    line-height: 1.4;
  }}
  .format-use {{
    margin-top: 5pt;
    font-size: 7.5pt;
    color: var(--orange);
    font-weight: 700;
    font-style: italic;
  }}

  /* ── Tabla resumen ── */
  .table-wrap {{
    padding: 0 28pt 14pt;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 8.5pt;
  }}
  thead tr {{
    background: var(--blue);
    color: white;
  }}
  thead th {{
    padding: 7pt 10pt;
    text-align: left;
    font-weight: 700;
    font-size: 8pt;
    letter-spacing: 0.5pt;
    text-transform: uppercase;
  }}
  tbody tr:nth-child(even) {{ background: var(--cream); }}
  tbody tr:nth-child(odd)  {{ background: var(--white); }}
  tbody td {{
    padding: 6pt 10pt;
    border-bottom: 0.5pt solid var(--cream2);
    vertical-align: middle;
  }}
  tbody td:first-child {{ font-size: 11pt; text-align: center; }}
  tbody td:nth-child(2) {{ font-weight: 700; color: var(--dark); }}
  tbody td:last-child {{ color: var(--mid); font-style: italic; }}

  /* ── Tips y privacidad ── */
  .two-col {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12pt;
    padding: 0 28pt 18pt;
  }}
  .tips-box {{
    background: #EFF6FF;
    border-radius: 8pt;
    padding: 12pt 14pt;
    border: 1pt solid #BFDBFE;
  }}
  .tips-box .box-title {{
    font-size: 9pt;
    font-weight: 800;
    color: var(--blue);
    margin-bottom: 8pt;
    display: flex;
    align-items: center;
    gap: 5pt;
  }}
  .tips-box ul {{
    list-style: none;
    padding: 0;
  }}
  .tips-box li {{
    font-size: 8.5pt;
    color: var(--mid);
    padding: 3pt 0;
    padding-left: 12pt;
    position: relative;
    line-height: 1.4;
  }}
  .tips-box li::before {{
    content: '→';
    position: absolute;
    left: 0;
    color: var(--blue);
    font-weight: 700;
  }}

  .privacy-box {{
    background: #FFF7ED;
    border-radius: 8pt;
    padding: 12pt 14pt;
    border: 1pt solid #FED7AA;
  }}
  .privacy-box .box-title {{
    font-size: 9pt;
    font-weight: 800;
    color: var(--orange);
    margin-bottom: 8pt;
    display: flex;
    align-items: center;
    gap: 5pt;
  }}
  .privacy-box p {{
    font-size: 8.5pt;
    color: var(--mid);
    line-height: 1.5;
  }}
  .privacy-box strong {{ color: var(--dark); }}

  /* ── Limit badge ── */
  .limit-badge {{
    display: inline-block;
    background: var(--orange);
    color: white;
    border-radius: 12pt;
    padding: 2pt 8pt;
    font-size: 7.5pt;
    font-weight: 700;
    margin-left: 4pt;
    vertical-align: middle;
  }}

  /* ── Footer ── */
  .footer {{
    background: var(--dark);
    color: rgba(255,255,255,0.6);
    font-size: 7.5pt;
    padding: 9pt 28pt;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .footer strong {{ color: white; }}

  /* ── Separador de sección ── */
  .section-sep {{
    height: 1pt;
    background: var(--cream2);
    margin: 0 28pt;
  }}

  /* ── Prompt hint ── */
  .prompt-hint {{
    background: #F0FDF4;
    border-left: 3pt solid #10B981;
    border-radius: 0 6pt 6pt 0;
    padding: 8pt 12pt;
    margin: 8pt 0 0;
    font-size: 8pt;
    color: #065F46;
    font-style: italic;
  }}
  .prompt-hint strong {{ font-style: normal; }}

</style>
</head>
<body>

<!-- ════════════════════════════════════
     PÁGINA 1
════════════════════════════════════ -->
<div class="page">

  <!-- CABECERA -->
  <div class="header">
    <div class="header-text">
      <div class="header-tag">IA en la Oficina · Edición 01/26</div>
      <h1>Tu notebook<br>del día <span>en acción</span></h1>
      <div class="header-sub">
        Guía del alumno · Google NotebookLM
      </div>
    </div>
    <div class="header-logo">
      <img src="data:image/png;base64,{LOGO_B64}" alt="AllWomen">
    </div>
  </div>
  <div class="stripe"></div>

  <!-- INTRO -->
  <div class="intro">
    <p>Cada día de clase recibirás un <strong>enlace a un notebook</strong> con todo el material de esa sesión. Puedes consumirlo en el formato que más te guste: escucharlo, verlo, estudiar con fichas o simplemente preguntarle lo que no haya quedado claro. No necesitas instalar nada, solo tu cuenta de Gmail.</p>
  </div>

  <!-- CÓMO ABRIR -->
  <div class="section">
    <div class="section-title">1 · Cómo abrir el notebook del día</div>
    <div class="steps">
      <div class="step">
        <div class="step-num">1</div>
        <strong>Recibe el enlace</strong>
        <p>Ananda te lo envía por el canal del curso al inicio de cada sesión.</p>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <strong>Haz clic</strong>
        <p>Se abre Google NotebookLM en tu navegador. Sin descarga.</p>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <strong>Inicia sesión con Gmail</strong>
        <p>Usa tu cuenta personal de Gmail cuando te lo pida.</p>
      </div>
      <div class="step">
        <div class="step-num">4</div>
        <strong>¡Listo!</strong>
        <p>Elige tu formato favorito del panel derecho o escribe en el chat.</p>
      </div>
    </div>
  </div>

  <div class="section-sep"></div>

  <!-- FORMATOS -->
  <div class="section" style="padding-bottom: 8pt;">
    <div class="section-title">2 · Los formatos disponibles</div>
  </div>

  <div class="formats-grid">

    <div class="format-card fc-audio">
      <span class="format-icon">🎙️</span>
      <div class="format-name">Audio Overview · Podcast</div>
      <div class="format-desc">Dos voces de IA debaten el contenido del día. Dura 8–15 minutos. Ideal para el camino de vuelta a casa o con los ojos cerrados.</div>
      <div class="format-use">Genera en: panel derecho → Audio Overview</div>
    </div>

    <div class="format-card fc-video">
      <span class="format-icon">🎬</span>
      <div class="format-name">Video Overview</div>
      <div class="format-desc">Vídeo corto con diapositivas animadas y narración IA. Resumen visual dinámico de 3–8 minutos.</div>
      <div class="format-use">Genera en: panel derecho → Video Overview</div>
    </div>

    <div class="format-card fc-info">
      <span class="format-icon">🗺️</span>
      <div class="format-name">Infografía / Mapa mental</div>
      <div class="format-desc">Esquema visual con conceptos y relaciones. Perfecto para imprimir y tener cerca del ordenador.</div>
      <div class="format-use">Pide en el chat: "Genera una infografía con los conceptos clave"</div>
    </div>

    <div class="format-card fc-study">
      <span class="format-icon">📖</span>
      <div class="format-name">Guía de estudio</div>
      <div class="format-desc">Documento organizado con los puntos más importantes. Para estudiar en profundidad o tener como referencia futura.</div>
      <div class="format-use">Genera en: panel derecho → Study Guide</div>
    </div>

    <div class="format-card fc-brief">
      <span class="format-icon">📄</span>
      <div class="format-name">Documento informativo</div>
      <div class="format-desc">Resumen ejecutivo de lo más importante. Lectura de 3 minutos, útil para compartir con quien no asistió.</div>
      <div class="format-use">Genera en: panel derecho → Briefing Doc</div>
    </div>

    <div class="format-card fc-flash">
      <span class="format-icon">🃏</span>
      <div class="format-name">Flashcards</div>
      <div class="format-desc">Tarjetas de memorización: término en el anverso, definición en el reverso. Para repasar rápido en momentos cortos.</div>
      <div class="format-use">Pide en el chat: "Genera 15 flashcards del glosario de hoy"</div>
    </div>

    <div class="format-card fc-quiz">
      <span class="format-icon">❓</span>
      <div class="format-name">Cuestionario</div>
      <div class="format-desc">Preguntas de opción múltiple y abiertas para comprobar lo que has asimilado. Con respuestas al final.</div>
      <div class="format-use">Genera en: panel derecho → Quiz</div>
    </div>

    <div class="format-card fc-faq">
      <span class="format-icon">💡</span>
      <div class="format-name">Preguntas frecuentes</div>
      <div class="format-desc">Las dudas más comunes sobre el contenido del día, ya resueltas. Empieza por aquí si algo no quedó claro en clase.</div>
      <div class="format-use">Pide en el chat: "Genera una FAQ de esta sesión"</div>
    </div>

    <div class="format-card fc-chat">
      <span class="format-icon">💬</span>
      <div class="format-name">Chat · Pregúntale</div>
      <div class="format-desc">Escribe cualquier duda y el notebook responde basándose solo en el material del día. Tu sesión es privada.
        <span class="limit-badge">~50 preguntas/día</span>
      </div>
      <div class="format-use">Escribe directamente en el cuadro de chat</div>
    </div>

  </div>

</div>


<!-- ════════════════════════════════════
     PÁGINA 2
════════════════════════════════════ -->
<div class="page">

  <!-- CABECERA PEQUEÑA -->
  <div class="header" style="padding: 14pt 28pt;">
    <div class="header-text">
      <div class="header-tag">IA en la Oficina · Edición 01/26 · Guía del alumno</div>
      <h1 style="font-size: 14pt;">¿Qué formato elijo?</h1>
    </div>
    <div class="header-logo">
      <img src="data:image/png;base64,{LOGO_B64}" alt="AllWomen">
    </div>
  </div>
  <div class="stripe"></div>

  <!-- TABLA RESUMEN -->
  <div class="section" style="padding-bottom: 10pt;">
    <div class="section-title">3 · Elige según tu objetivo</div>
  </div>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th></th>
          <th>Si quiero…</th>
          <th>Formato recomendado</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>🎙️</td>
          <td>Escuchar el resumen de camino a casa</td>
          <td>Audio Overview (podcast)</td>
        </tr>
        <tr>
          <td>🎬</td>
          <td>Ver un vídeo resumen rápido</td>
          <td>Video Overview</td>
        </tr>
        <tr>
          <td>🗺️</td>
          <td>Un esquema visual para imprimir</td>
          <td>Infografía / mapa mental</td>
        </tr>
        <tr>
          <td>📖</td>
          <td>Estudiar en profundidad</td>
          <td>Guía de estudio</td>
        </tr>
        <tr>
          <td>📄</td>
          <td>Leer un resumen en 5 minutos</td>
          <td>Documento informativo</td>
        </tr>
        <tr>
          <td>🃏</td>
          <td>Memorizar términos y definiciones</td>
          <td>Flashcards</td>
        </tr>
        <tr>
          <td>❓</td>
          <td>Comprobar si he entendido bien</td>
          <td>Cuestionario</td>
        </tr>
        <tr>
          <td>💡</td>
          <td>Ver las dudas más comunes resueltas</td>
          <td>Preguntas frecuentes (FAQ)</td>
        </tr>
        <tr>
          <td>💬</td>
          <td>Resolver una duda concreta</td>
          <td>Chat (escribe tu pregunta)</td>
        </tr>
      </tbody>
    </table>

    <div class="prompt-hint">
      <strong>Truco para el chat:</strong> las preguntas específicas dan mejores respuestas que las generales. En vez de "explica eso mejor", escribe: <em>"¿Cuál es la diferencia entre el resumen ejecutivo y el operativo del apartado de ejemplos resueltos?"</em>
    </div>
  </div>

  <div class="section-sep"></div>

  <!-- TIPS + PRIVACIDAD -->
  <div class="section" style="padding-bottom: 10pt;">
    <div class="section-title">4 · Consejos y privacidad</div>
  </div>

  <div class="two-col">
    <div class="tips-box">
      <div class="box-title">
        <span>💡</span> Sácale más partido
      </div>
      <ul>
        <li>Empieza por el <strong>Audio Overview</strong> si llegas cansado: te pone en contexto sin esfuerzo.</li>
        <li>Usa el <strong>cuestionario antes de ver las respuestas</strong> para que el repaso sea más efectivo.</li>
        <li>Combina formatos: podcast → flashcards → cuestionario. Tres pasadas = aprendizaje sólido.</li>
        <li>Si el audio sale en inglés, pide en el chat: <em>"Genera un resumen en español de los puntos clave."</em></li>
        <li>El enlace del notebook <strong>sigue activo</strong> durante todo el curso. Úsalo para repasar cuando quieras.</li>
        <li>Puedes usar los notebooks de sesiones anteriores para preparar tu <strong>proyecto final</strong>.</li>
      </ul>
    </div>

    <div class="privacy-box">
      <div class="box-title">
        <span>🔒</span> Tu privacidad importa
      </div>
      <p>
        El chat del notebook es <strong>solo tuyo</strong> — nadie más ve tus conversaciones.<br><br>
        Aun así, recuerda:<br><br>
        <strong>No escribas en el chat datos reales</strong> de tu empresa: nombres de clientes, DNIs, números de cuenta, contraseñas o información confidencial.<br><br>
        Si quieres usar un ejemplo de tu trabajo, usa nombres ficticios: <strong>CLIENTE_A, REF_X, EMPRESA_Y.</strong><br><br>
        El análisis funciona igual con datos anónimos. Siempre.
      </p>
    </div>
  </div>

  <div class="section-sep"></div>

  <!-- PREGUNTAS FRECUENTES RÁPIDAS -->
  <div class="section" style="padding-bottom: 10pt;">
    <div class="section-title">5 · Preguntas frecuentes</div>
  </div>

  <div style="padding: 0 28pt 18pt; display: grid; grid-template-columns: 1fr 1fr; gap: 8pt;">

    <div style="background: var(--light); border-radius: 6pt; padding: 9pt 11pt; border: 1pt solid var(--cream2);">
      <div style="font-weight: 800; font-size: 8.5pt; color: var(--blue); margin-bottom: 4pt;">¿Necesito cuenta de pago?</div>
      <div style="font-size: 8pt; color: var(--mid); line-height: 1.4;">No. Todos los formatos de esta guía son gratuitos con Gmail personal.</div>
    </div>

    <div style="background: var(--light); border-radius: 6pt; padding: 9pt 11pt; border: 1pt solid var(--cream2);">
      <div style="font-weight: 800; font-size: 8.5pt; color: var(--blue); margin-bottom: 4pt;">¿Puedo modificar el material?</div>
      <div style="font-size: 8pt; color: var(--mid); line-height: 1.4;">No. El notebook es de solo lectura para alumnos. Puedes generar formatos y chatear, pero no editar la fuente.</div>
    </div>

    <div style="background: var(--light); border-radius: 6pt; padding: 9pt 11pt; border: 1pt solid var(--cream2);">
      <div style="font-weight: 800; font-size: 8.5pt; color: var(--blue); margin-bottom: 4pt;">¿Mis chats son visibles?</div>
      <div style="font-size: 8pt; color: var(--mid); line-height: 1.4;">No. Cada alumno tiene su sesión de chat independiente y privada.</div>
    </div>

    <div style="background: var(--light); border-radius: 6pt; padding: 9pt 11pt; border: 1pt solid var(--cream2);">
      <div style="font-weight: 800; font-size: 8.5pt; color: var(--blue); margin-bottom: 4pt;">¿Cuántas preguntas puedo hacer?</div>
      <div style="font-size: 8pt; color: var(--mid); line-height: 1.4;">Aproximadamente 50 por día con cuenta gratuita. Más que suficiente para una sesión normal.</div>
    </div>

    <div style="background: var(--light); border-radius: 6pt; padding: 9pt 11pt; border: 1pt solid var(--cream2);">
      <div style="font-weight: 800; font-size: 8.5pt; color: var(--blue); margin-bottom: 4pt;">¿Puedo acceder después de clase?</div>
      <div style="font-size: 8pt; color: var(--mid); line-height: 1.4;">Sí. El enlace sigue activo durante todo el curso. Úsalo para repasar cuando quieras.</div>
    </div>

    <div style="background: var(--light); border-radius: 6pt; padding: 9pt 11pt; border: 1pt solid var(--cream2);">
      <div style="font-weight: 800; font-size: 8.5pt; color: var(--blue); margin-bottom: 4pt;">¿El chat no entiende mi pregunta?</div>
      <div style="font-size: 8pt; color: var(--mid); line-height: 1.4;">Reformúlala con más contexto: añade el nombre de la sección o el apartado al que te refieres.</div>
    </div>

  </div>

  <!-- FOOTER -->
  <div class="footer">
    <span>IA en la Oficina – Eficiencia y Productividad · Edición 01/26 · Fundación ONCE · Inserta Empleo · Talento Digital</span>
    <strong>AllWomen · ananda@allwomen.tech</strong>
  </div>

</div>

</body>
</html>"""

# ── Generar PDF ────────────────────────────────────────────────────────────────
print(f"Generando PDF: {OUT_PATH}")
HTML(string=HTML_CONTENT).write_pdf(
    str(OUT_PATH),
    stylesheets=[CSS(string="@page { size: A4; margin: 0; }")]
)
print(f"✅ Guardado: {OUT_PATH}")
print(f"   Tamaño: {OUT_PATH.stat().st_size / 1024:.0f} KB")
