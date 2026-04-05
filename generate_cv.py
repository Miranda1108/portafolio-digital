"""Generate a professional CV PDF for Angel Emiliano Miranda Baeza."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import os

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CV_Angel_Miranda.pdf")

# Colors
NAVY = HexColor("#1a1f2e")
ACCENT = HexColor("#c8ff00")
ACCENT_DARK = HexColor("#8ab300")
DARK_TEXT = HexColor("#1a1a2e")
MID_TEXT = HexColor("#4a4a5a")
LIGHT_TEXT = HexColor("#d0d0d8")
SIDEBAR_TEXT = HexColor("#b0b0c0")
WHITE = white
DIVIDER = HexColor("#e0e0e8")
SIDEBAR_W = 200

W, H = letter  # 612 x 792


def draw_sidebar(c):
    """Draw the dark sidebar with contact, skills, competencies, languages."""
    # Sidebar background
    c.setFillColor(NAVY)
    c.rect(0, 0, SIDEBAR_W, H, fill=1, stroke=0)

    # Accent strip at top
    c.setFillColor(ACCENT)
    c.rect(0, H - 4, SIDEBAR_W, 4, fill=1, stroke=0)

    x = 24
    y = H - 40

    # Name
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(x, y, "ANGEL EMILIANO")
    y -= 20
    c.drawString(x, y, "MIRANDA BAEZA")
    y -= 16
    c.setFont("Helvetica", 8.5)
    c.setFillColor(ACCENT)
    c.drawString(x, y, "Ing. en Sistemas Computacionales")
    y -= 12
    c.drawString(x, y, "Estudiante | 5to Semestre")

    # Divider
    y -= 18
    c.setStrokeColor(HexColor("#2a3040"))
    c.setLineWidth(0.5)
    c.line(x, y, SIDEBAR_W - 24, y)

    # Contact section
    y -= 20
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x, y, "CONTACTO")
    y -= 16

    contacts = [
        ("Email", "angelmc06@outlook.com"),
        ("Tel.", "56 1008 0655"),
        ("LinkedIn", "/in/angel-emiliano-miranda-baeza"),
        ("GitHub", "github.com/Miranda1108"),
        ("Portfolio", "miranda1108.github.io/portafolio-digital"),
        ("Ubicacion", "Ixtapaluca, Edo. de Mexico"),
    ]
    for label, value in contacts:
        c.setFillColor(ACCENT_DARK)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(x, y, label)
        y -= 11
        c.setFillColor(LIGHT_TEXT)
        c.setFont("Helvetica", 7.5)
        # Wrap long values
        if len(value) > 28:
            words = value.split("/")
            if len(words) > 2:
                line1 = "/".join(words[:2]) + "/"
                line2 = "/".join(words[2:])
                c.drawString(x, y, line1)
                y -= 10
                c.drawString(x, y, line2)
            else:
                c.drawString(x, y, value)
        else:
            c.drawString(x, y, value)
        y -= 14

    # Divider
    y -= 4
    c.setStrokeColor(HexColor("#2a3040"))
    c.line(x, y, SIDEBAR_W - 24, y)

    # Technical Skills
    y -= 18
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x, y, "HABILIDADES TECNICAS")
    y -= 16

    skills = [
        ("Lenguajes", ["JavaScript / TypeScript", "Python", "Java", "C#"]),
        ("Frontend", ["React.js", "HTML5 / CSS3", "Tailwind CSS"]),
        ("Backend", ["Node.js / Express", "Django / FastAPI", ".NET Core"]),
        ("Bases de Datos", ["MySQL / PostgreSQL", "MongoDB"]),
        ("DevOps & Tools", ["Git / GitHub", "Docker", "Linux", "REST APIs"]),
    ]
    for category, items in skills:
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(x, y, category)
        y -= 11
        c.setFillColor(SIDEBAR_TEXT)
        c.setFont("Helvetica", 7)
        for item in items:
            c.drawString(x + 6, y, item)
            y -= 10
        y -= 4

    # Divider
    y -= 2
    c.setStrokeColor(HexColor("#2a3040"))
    c.line(x, y, SIDEBAR_W - 24, y)

    # Competencias
    y -= 16
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x, y, "COMPETENCIAS")
    y -= 14

    competencias = [
        "Trabajo en equipo",
        "Resolucion de problemas",
        "Aprendizaje continuo",
        "Comunicacion efectiva",
        "Adaptabilidad",
        "Gestion del tiempo",
    ]
    c.setFillColor(SIDEBAR_TEXT)
    c.setFont("Helvetica", 7.5)
    for comp in competencias:
        c.drawString(x + 6, y, comp)
        y -= 11

    # Divider
    y -= 6
    c.setStrokeColor(HexColor("#2a3040"))
    c.line(x, y, SIDEBAR_W - 24, y)

    # Idiomas
    y -= 16
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x, y, "IDIOMAS")
    y -= 14

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(x + 6, y, "Espanol")
    c.setFillColor(SIDEBAR_TEXT)
    c.setFont("Helvetica", 7)
    c.drawString(x + 50, y, "- Nativo")
    y -= 12
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(x + 6, y, "Ingles")
    c.setFillColor(SIDEBAR_TEXT)
    c.setFont("Helvetica", 7)
    c.drawString(x + 42, y, "- B\u00e1sico")


def draw_main(c):
    """Draw the main content area."""
    x_start = SIDEBAR_W + 28
    x_end = W - 28
    content_w = x_end - x_start
    y = H - 36

    # Accent line at top
    c.setFillColor(ACCENT)
    c.rect(SIDEBAR_W, H - 4, W - SIDEBAR_W, 4, fill=1, stroke=0)

    # ── PERFIL PROFESIONAL ──
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x_start, y, "PERFIL PROFESIONAL")
    y -= 3
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.5)
    c.line(x_start, y, x_start + 80, y)
    y -= 14

    style_body = ParagraphStyle(
        "body",
        fontName="Helvetica",
        fontSize=8,
        leading=12,
        textColor=MID_TEXT,
        alignment=TA_JUSTIFY,
    )

    perfil = (
        "Estudiante de Ingenier\u00eda en Sistemas Computacionales en el TESI con "
        "s\u00f3lida formaci\u00f3n en desarrollo fullstack. Experiencia pr\u00e1ctica en el "
        "dise\u00f1o e implementaci\u00f3n de aplicaciones web con arquitecturas modernas, "
        "integraci\u00f3n de APIs RESTful y bases de datos relacionales y no relacionales. "
        "Orientado a resultados, con capacidad de entregar soluciones funcionales en "
        "entornos de trabajo remoto y metodolog\u00edas \u00e1giles."
    )
    p = Paragraph(perfil, style_body)
    pw, ph = p.wrap(content_w, 200)
    p.drawOn(c, x_start, y - ph)
    y -= ph + 16

    # ── EDUCACION ──
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x_start, y, "EDUCACI\u00d3N")
    y -= 3
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.5)
    c.line(x_start, y, x_start + 50, y)
    y -= 16

    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x_start, y, "Ing. en Sistemas Computacionales")
    y -= 13
    c.setFillColor(MID_TEXT)
    c.setFont("Helvetica", 8)
    c.drawString(x_start, y, "Tecnol\u00f3gico de Estudios Superiores de Ixtapaluca (TESI)")
    y -= 12
    c.setFillColor(ACCENT_DARK)
    c.setFont("Helvetica-Oblique", 7.5)
    c.drawString(x_start, y, "5to Semestre  |  2023 - Presente")
    y -= 22

    # ── EXPERIENCIA & PROYECTOS ──
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x_start, y, "EXPERIENCIA & PROYECTOS")
    y -= 3
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.5)
    c.line(x_start, y, x_start + 100, y)
    y -= 16

    # Project 1
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(x_start, y, "Finanzas con Pam")
    c.setFillColor(MID_TEXT)
    c.setFont("Helvetica", 8)
    c.drawRightString(x_end, y, "Desarrollo Freelance")
    y -= 12
    c.setFillColor(ACCENT_DARK)
    c.setFont("Helvetica-Oblique", 7.5)
    c.drawString(x_start, y, "React.js  |  Node.js  |  Express  |  MongoDB  |  Tailwind CSS")
    y -= 14

    bullets_1 = [
        "Dise\u00f1o y desarrollo de plataforma web de finanzas personales con dashboard interactivo para visualizaci\u00f3n de gastos e ingresos.",
        "Implementaci\u00f3n de sistema de autenticaci\u00f3n y gesti\u00f3n de sesiones con JWT para protecci\u00f3n de datos financieros del usuario.",
        "Desarrollo de API RESTful para operaciones CRUD con validaci\u00f3n de datos y manejo de errores centralizado.",
        "Dise\u00f1o responsive optimizado para dispositivos m\u00f3viles, asegurando accesibilidad y UX consistente.",
    ]

    style_bullet = ParagraphStyle(
        "bullet",
        fontName="Helvetica",
        fontSize=7.5,
        leading=10.5,
        textColor=MID_TEXT,
        alignment=TA_JUSTIFY,
        leftIndent=8,
    )

    for bullet in bullets_1:
        c.setFillColor(ACCENT_DARK)
        c.setFont("Helvetica", 7.5)
        c.drawString(x_start, y + 1, "\u2022")
        p = Paragraph(bullet, style_bullet)
        pw, ph = p.wrap(content_w - 10, 100)
        p.drawOn(c, x_start, y - ph + 3)
        y -= ph + 2

    y -= 10

    # Project 2
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(x_start, y, "Advance")
    c.setFillColor(MID_TEXT)
    c.setFont("Helvetica", 8)
    c.drawRightString(x_end, y, "Desarrollo Freelance")
    y -= 12
    c.setFillColor(ACCENT_DARK)
    c.setFont("Helvetica-Oblique", 7.5)
    c.drawString(x_start, y, "Python / FastAPI  |  React.js  |  PostgreSQL  |  Docker")
    y -= 14

    bullets_2 = [
        "Arquitectura e implementaci\u00f3n de plataforma web fullstack con separaci\u00f3n clara de responsabilidades (frontend/backend/DB).",
        "Desarrollo de backend con FastAPI, incluyendo endpoints documentados con OpenAPI/Swagger para integraci\u00f3n de equipos.",
        "Modelado de base de datos relacional en PostgreSQL con migraciones versionadas y queries optimizadas con \u00edndices.",
        "Contenerizaci\u00f3n del entorno de desarrollo con Docker y Docker Compose para garantizar reproducibilidad del stack.",
    ]

    for bullet in bullets_2:
        c.setFillColor(ACCENT_DARK)
        c.setFont("Helvetica", 7.5)
        c.drawString(x_start, y + 1, "\u2022")
        p = Paragraph(bullet, style_bullet)
        pw, ph = p.wrap(content_w - 10, 100)
        p.drawOn(c, x_start, y - ph + 3)
        y -= ph + 2

    y -= 12

    # ── CERTIFICACIONES ──
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x_start, y, "CERTIFICACIONES")
    y -= 3
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.5)
    c.line(x_start, y, x_start + 70, y)
    y -= 16

    certs = [
        ("JavaScript", "Santander / Becas Santander"),
        ("Data Analyst Essentials", "Cisco Networking Academy"),
        ("Inteligencia Artificial", "Tecnol\u00f3gico Nacional de M\u00e9xico (TecNM)"),
        ("Exploring SAP Analytics Cloud", "SAP"),
    ]

    for name, issuer in certs:
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(x_start, y, name)
        c.setFillColor(MID_TEXT)
        c.setFont("Helvetica", 7.5)
        c.drawString(x_start, y - 11, issuer)
        y -= 26


def main():
    c = canvas.Canvas(OUTPUT, pagesize=letter)
    c.setTitle("CV - Angel Emiliano Miranda Baeza")
    c.setAuthor("Angel Emiliano Miranda Baeza")
    c.setSubject("Curriculum Vitae")

    # White background
    c.setFillColor(WHITE)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    draw_sidebar(c)
    draw_main(c)

    c.save()
    print(f"CV generado: {OUTPUT}")


if __name__ == "__main__":
    main()
