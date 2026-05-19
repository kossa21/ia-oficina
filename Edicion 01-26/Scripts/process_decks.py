#!/usr/bin/env python3
"""
process_decks.py — IA en la Oficina 01/26
Añade el logo de AllWomen a cada slide de un PPTX generado por NotebookLM.

La estructura del deck (portada, agenda, señales de ejercicio, cierre con
recap + mañana) y el guion del formador ya vienen del prompt de NotebookLM
(ver Recursos/NotebookLM_Prompts_Referencia.md). Este script solo hace lo
único que NotebookLM no puede hacer: estampar el logo corporativo.

Uso:
    python3 process_decks.py D05_MiDeck.pptx
    python3 process_decks.py D05_MiDeck.pptx D06_Otro.pptx
    python3 process_decks.py *.pptx

El archivo procesado se guarda en el mismo directorio con el nombre original.
"""

import sys
import os
from pptx import Presentation
from pptx.util import Inches

# ── CONFIGURACIÓN ────────────────────────────────────────────────────────────

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(SCRIPT_DIR, "..", "Logos", "00_FULL COLOR (1).png")

# Posición logo AllWomen (aprobada por Daniela, no cambiar)
LOGO_WIDTH  = Inches(1.2)
LOGO_TOP    = Inches(0.20)
SLIDE_W     = Inches(17.78)
LOGO_LEFT   = SLIDE_W - LOGO_WIDTH - Inches(0.30)

# ── FUNCIONES ─────────────────────────────────────────────────────────────────

def logo_already_added(slide):
    """Comprueba si ya hay un logo AllWomen en la slide (esquina superior derecha)."""
    for shape in slide.shapes:
        if shape.shape_type == 13:  # PICTURE
            left_in = shape.left / 914400
            width_in = shape.width / 914400
            if width_in < 3 and left_in > 14:
                return True
    return False


def add_logo(slide):
    """Añade el logo AllWomen si no está ya."""
    if logo_already_added(slide):
        return False
    if not os.path.exists(LOGO_PATH):
        print(f"  ⚠️  Logo no encontrado: {LOGO_PATH}")
        return False
    slide.shapes.add_picture(LOGO_PATH, LOGO_LEFT, LOGO_TOP, LOGO_WIDTH)
    return True


def process_deck(pptx_path):
    print(f"\n📂 Procesando {os.path.basename(pptx_path)}")
    prs = Presentation(pptx_path)
    slides = list(prs.slides)
    print(f"   {len(slides)} slides detectadas")

    added = 0
    for i, slide in enumerate(slides):
        if add_logo(slide):
            added += 1
            print(f"   Slide {i+1}: logo ✅")
        else:
            print(f"   Slide {i+1}: logo ya presente, se omite")

    prs.save(pptx_path)
    print(f"   💾 Guardado: {pptx_path}  ({added} logos añadidos)")


# ── MAIN ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    for path in sys.argv[1:]:
        if not os.path.exists(path):
            print(f"⚠️  Archivo no encontrado: {path}")
            continue
        if not path.lower().endswith(".pptx"):
            print(f"⚠️  No es un .pptx: {path}")
            continue
        process_deck(path)

    print("\n✅ Procesado completado.")
