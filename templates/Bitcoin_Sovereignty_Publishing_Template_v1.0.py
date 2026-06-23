#!/usr/bin/env python3
"""
Bitcoin Sovereignty Publishing Template v1.0
Complete Production-Ready reportlab Template

This template is designed to be used together with 
Bitcoin_Sovereignty_Publishing_Baseline_v1.0.pdf as a matched pair.

- The Baseline v1.0 defines all mandatory rules, visual standards, 
  identity hierarchy, cross-tier integration requirements, and 
  preferred page-break behaviour (e.g. subheadings should not be 
  orphaned at the bottom of a page; certain sections like 3.4 start 
  on a new page).
- This Template provides the working code that implements those standards.

Usage:
1. Update only the variables in the "DOCUMENT SETTINGS" section below.
2. Add your content in the story list (after the title page).
3. Run the script to generate a clean, professional PDF.

All colours, fonts, margins, header/footer logic, and Truth & Clarity 
box styling are pre-configured to comply with Baseline v1.1.
Do not modify the core styling definitions unless the Baseline itself is updated.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, 
    Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.pdfgen import canvas

# =============================================================================
# DOCUMENT SETTINGS (UPDATE THESE)
# =============================================================================
DOCUMENT_TITLE = "YOUR DOCUMENT TITLE HERE"
DOCUMENT_SUBTITLE = "Series Subtitle or Version"
AUTHOR_LINE = "Jacques Strydom, PMP (PMI ID: 3160455) (Project Owner & Creator)"
PUBLISHER = "MoloBTC"
COLLABORATOR = "Grok (built by xAI)"
LICENSE = "BSOL v1.0"
DATE = "June 2026"

# =============================================================================
# COLOURS (Locked - do not change)
# =============================================================================
NAVY = HexColor('#1a365d')
GOLD = HexColor('#c9a227')
LIGHT_BG = HexColor('#f5f5f5')
DARK_TEXT = HexColor('#2d3748')
SUBTLE_GREY = HexColor('#718096')

# =============================================================================
# PAGE SETUP
# =============================================================================
PAGE_WIDTH, PAGE_HEIGHT = A4
LEFT_MARGIN = 0.9 * inch
RIGHT_MARGIN = 0.9 * inch
TOP_MARGIN = 0.7 * inch
BOTTOM_MARGIN = 0.6 * inch

# =============================================================================
# STYLES
# =============================================================================
styles = getSampleStyleSheet()

styles.add(ParagraphStyle(name='MainTitle', fontName='Helvetica-Bold', fontSize=16,
                          textColor=NAVY, alignment=TA_CENTER, spaceAfter=6))
styles.add(ParagraphStyle(name='Subtitle', fontName='Helvetica', fontSize=10,
                          textColor=GOLD, alignment=TA_CENTER, spaceAfter=10))
styles.add(ParagraphStyle(name='SectionHead', fontName='Helvetica-Bold', fontSize=11,
                          textColor=NAVY, spaceBefore=14, spaceAfter=6))
styles.add(ParagraphStyle(name='SubSectionHead', fontName='Helvetica-Bold', fontSize=10,
                          textColor=NAVY, spaceBefore=10, spaceAfter=4))
styles.add(ParagraphStyle(name='JustifiedBody', fontName='Helvetica', fontSize=9.5,
                          textColor=DARK_TEXT, alignment=TA_JUSTIFY, spaceBefore=2,
                          spaceAfter=4, leading=12))
styles.add(ParagraphStyle(name='Author', fontName='Helvetica', fontSize=9.5,
                          textColor=DARK_TEXT, alignment=TA_CENTER, spaceBefore=2, spaceAfter=2))
styles.add(ParagraphStyle(name='BulletText', fontName='Helvetica', fontSize=9.5,
                          textColor=DARK_TEXT, alignment=TA_LEFT, spaceBefore=1,
                          spaceAfter=2, leading=11.5, leftIndent=15))
styles.add(ParagraphStyle(name='SmallNote', fontName='Helvetica-Oblique', fontSize=8,
                          textColor=SUBTLE_GREY, alignment=TA_CENTER, spaceBefore=6))
styles.add(ParagraphStyle(name='TableHeader', fontName='Helvetica-Bold', fontSize=8,
                          textColor=NAVY, alignment=TA_CENTER))
styles.add(ParagraphStyle(name='TableCell', fontName='Helvetica', fontSize=8,
                          textColor=DARK_TEXT, alignment=TA_LEFT, leading=10))

# =============================================================================
# HEADER / FOOTER
# =============================================================================
def add_header_footer(canvas, doc):
    canvas.saveState()
    
    # Gold header rule
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(0.5)
    canvas.line(LEFT_MARGIN, PAGE_HEIGHT - 0.48*inch, 
                PAGE_WIDTH - RIGHT_MARGIN, PAGE_HEIGHT - 0.48*inch)
    
    canvas.setFont('Helvetica', 6)
    canvas.setFillColor(SUBTLE_GREY)
    short_title = DOCUMENT_TITLE[:48] + "..." if len(DOCUMENT_TITLE) > 48 else DOCUMENT_TITLE
    canvas.drawString(LEFT_MARGIN, PAGE_HEIGHT - 0.38*inch, 
                      f"{short_title} | Publishing Baseline v1.1")
    
    # Navy footer rule
    canvas.setStrokeColor(NAVY)
    canvas.line(LEFT_MARGIN, 0.48*inch, PAGE_WIDTH - RIGHT_MARGIN, 0.48*inch)
    
    footer = f"Page {doc.page} • Jacques Strydom, PMP with MoloBTC • {LICENSE} • {DATE}"
    canvas.setFont('Helvetica', 6)
    canvas.setFillColor(SUBTLE_GREY)
    canvas.drawCentredString(PAGE_WIDTH / 2, 0.34*inch, footer)
    
    canvas.restoreState()

# =============================================================================
# TRUTH & CLARITY BOX (Protected from bad page breaks)
# =============================================================================
def create_truth_box(title, content):
    title_para = Paragraph(f"<b>TRUTH & CLARITY — {title}</b>", 
                           ParagraphStyle('t', fontName='Helvetica-Bold', fontSize=8, 
                                          textColor=NAVY, spaceAfter=3))
    content_para = Paragraph(content, 
                             ParagraphStyle('c', fontName='Helvetica', fontSize=8, 
                                            textColor=DARK_TEXT, alignment=TA_JUSTIFY, leading=10))
    
    data = [[title_para], [content_para]]
    t = Table(data, colWidths=[6.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_BG),
        ('BOX', (0, 0), (-1, -1), 0.75, NAVY),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    return KeepTogether([t])

# =============================================================================
# BUILD DOCUMENT
# =============================================================================
doc = SimpleDocTemplate(
    f"{DOCUMENT_TITLE.replace(' ', '_')}_v1.pdf",
    pagesize=A4,
    leftMargin=LEFT_MARGIN,
    rightMargin=RIGHT_MARGIN,
    topMargin=TOP_MARGIN,
    bottomMargin=BOTTOM_MARGIN
)

story = []

# ========== TITLE PAGE ==========
story.append(Spacer(1, 1.1*inch))
story.append(Paragraph(DOCUMENT_TITLE, styles['MainTitle']))
story.append(Paragraph(DOCUMENT_SUBTITLE, styles['Subtitle']))
story.append(Spacer(1, 0.25*inch))
story.append(HRFlowable(width="55%", thickness=1, color=GOLD, spaceBefore=4, spaceAfter=12))
story.append(Paragraph(AUTHOR_LINE, styles['Author']))
story.append(Paragraph("Published by MoloBTC", styles['Author']))
story.append(Paragraph("In collaboration with Grok (built by xAI)", styles['Author']))
story.append(Paragraph("LinkedIn: linkedin.com/in/strydomjacques", styles['Author']))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph(f"{DATE} | {LICENSE}", styles['Author']))
story.append(Spacer(1, 0.35*inch))
story.append(Paragraph(
    "This document follows the Bitcoin Sovereignty Publishing Baseline v1.0 standards "
    "(including preferred handling of subheadings and page breaks).",
    ParagraphStyle('Intro', fontName='Helvetica', fontSize=9.5, textColor=DARK_TEXT, 
                   alignment=TA_CENTER, leading=12)
))
story.append(PageBreak())

# =============================================================================
# YOUR CONTENT GOES HERE
# =============================================================================
# Example structure - replace with your actual content:

story.append(Paragraph("1. SECTION HEADING", styles['SectionHead']))
story.append(Paragraph(
    "Your body text goes here. Use styles['JustifiedBody'] for normal paragraphs. "
    "Keep line spacing and margins consistent with the Baseline standards.",
    styles['JustifiedBody']
))

story.append(create_truth_box("Example Box",
    "This is how a Truth & Clarity box should look. It is protected from bad page breaks."))

story.append(Paragraph("2. ANOTHER SECTION", styles['SectionHead']))
story.append(Paragraph("More content here...", styles['JustifiedBody']))

# Add more sections, tables, bullet points, etc. as needed.
# Use styles['BulletText'] for bullet points.
# Use KeepTogether() around complex elements you don't want to split.

# =============================================================================
# CLOSING / AUTHORSHIP BLOCK
# =============================================================================
story.append(Spacer(1, 12))
story.append(HRFlowable(width="100%", thickness=0.5, color=GOLD, spaceBefore=6, spaceAfter=8))
story.append(Paragraph(
    f"<b>Authorship</b>: Prepared by Jacques Strydom, PMP (PMI ID: 3160455). "
    f"Published by MoloBTC. Research collaboration with Grok (built by xAI). "
    f"License: Released under the Bitcoin Sovereign Open License (BSOL) v1.0.",
    ParagraphStyle('FooterNote', fontName='Helvetica', fontSize=8, textColor=SUBTLE_GREY, alignment=TA_CENTER)
))

# Build the PDF
doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)

print("✅ PDF generated successfully using Bitcoin Sovereignty Publishing Template v1.0")