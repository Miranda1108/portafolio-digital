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
    c.drawString(x, y, "Estudiante | 6to Semestre")

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
        ("Email", "angelmc06@outlook.com", "mailto:angelmc06@outlook.com"),
        ("Tel.", "56 1008 0655", "tel:+525610080655"),
        ("LinkedIn", "/in/angel-miranda-dev",
         "https://linkedin.com/in/angel-miranda-dev"),
        ("GitHub", "github.com/Miranda1108", "https://github.com/Miranda1108"),
        ("Portfolio", "miranda1108.github.io/portafolio-digital",
         "https://miranda1108.github.io/portafolio-digital/"),
        ("Ubicacion", "Ixtapaluca, Edo. de Mexico", None),
    ]
    for label, value, url in contacts:
        c.setFillColor(ACCENT_DARK)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(x, y, label)
        y -= 11
        c.setFillColor(LIGHT_TEXT)
        c.setFont("Helvetica", 7.5)
        # Track the clickable region for this value
        link_top = y + 8
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
        # Register clickable hyperlink over the value text
        if url:
            c.linkURL(url, (x, y - 2, SIDEBAR_W - 16, link_top), relative=0)
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
        ("Frontend", ["React.js / Next.js", "HTML5 / CSS3", "Tailwind CSS"]),
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
        "Arquitectura de soluciones",
        "Integraci\u00f3n de APIs",
        "Trabajo en equipo",
        "Resoluci\u00f3n de problemas",
        "Aprendizaje continuo",
        "Comunicaci\u00f3n efectiva",
        "Adaptabilidad",
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
        "Desarrollador Fullstack y estudiante de Ingenier\u00eda en Sistemas Computacionales "
        "(TESI) con experiencia construyendo y desplegando aplicaciones web de extremo a "
        "extremo. Llev\u00e9 a producci\u00f3n un CRM con automatizaci\u00f3n de WhatsApp e integraciones "
        "de terceros (Meta Cloud API, Google Calendar), adem\u00e1s de plataformas con "
        "autenticaci\u00f3n segura mediante JWT y APIs RESTful. Combino interfaces intuitivas con "
        "backends s\u00f3lidos y escalables, trabajando bajo metodolog\u00edas \u00e1giles y en entornos remotos."
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
    c.drawString(x_start, y, "6to Semestre  |  2023 - Presente")
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

    style_bullet = ParagraphStyle(
        "bullet",
        fontName="Helvetica",
        fontSize=7.5,
        leading=10.5,
        textColor=MID_TEXT,
        alignment=TA_JUSTIFY,
        leftIndent=8,
    )

    projects = [
        {
            "name": "Fianzify \u2014 Sitio Corporativo",
            "tag": "Desarrollo Freelance",
            "stack": "Next.js 14  |  React  |  TypeScript  |  Resend  |  SEO Local",
            "bullets": [
                "Sitio web corporativo para empresa de fianzas con Next.js 14 (App Router) y TypeScript, desplegado con cobertura nacional.",
                "9 p\u00e1ginas SEO geolocalizadas por ciudad y p\u00e1ginas por tipo de fianza, con blog din\u00e1mico y calculadora de prima en vivo.",
                "Formulario de captaci\u00f3n de leads con API route e integraci\u00f3n de correo v\u00eda Resend, m\u00e1s CTA directo a WhatsApp.",
            ],
        },
        {
            "name": "Finanzas con Pam",
            "tag": "Desarrollo Freelance",
            "stack": "React.js  |  Node.js  |  Express  |  MongoDB  |  Tailwind CSS",
            "bullets": [
                "Plataforma web de finanzas personales con dashboard interactivo para visualizaci\u00f3n de gastos e ingresos.",
                "Autenticaci\u00f3n y gesti\u00f3n de sesiones con JWT, y API RESTful para operaciones CRUD con validaci\u00f3n y manejo de errores.",
                "Dise\u00f1o responsive optimizado para dispositivos m\u00f3viles, con UX consistente y accesible.",
            ],
        },
        {
            "name": "ADVANCE \u2014 CRM & Bot WhatsApp",
            "tag": "Desarrollo Freelance",
            "stack": "Node.js  |  Express  |  PostgreSQL  |  Meta WhatsApp API  |  Google Calendar  |  JWT",
            "bullets": [
                "Sistema CRM con bot de WhatsApp (Meta Cloud API) que automatiza la captaci\u00f3n de prospectos en un flujo conversacional de 13 etapas.",
                "Dashboard administrativo con autenticaci\u00f3n JWT, roles (admin/asesor), gr\u00e1ficas con Chart.js y exportaci\u00f3n CSV.",
                "Integraci\u00f3n con Google Calendar (OAuth2) y automatizaci\u00f3n de reportes y recordatorios con node-cron.",
            ],
        },
    ]

    for i, proj in enumerate(projects):
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(x_start, y, proj["name"])
        c.setFillColor(MID_TEXT)
        c.setFont("Helvetica", 8)
        c.drawRightString(x_end, y, proj["tag"])
        y -= 12
        c.setFillColor(ACCENT_DARK)
        c.setFont("Helvetica-Oblique", 7.5)
        c.drawString(x_start, y, proj["stack"])
        y -= 14

        for bullet in proj["bullets"]:
            c.setFillColor(ACCENT_DARK)
            c.setFont("Helvetica", 7.5)
            c.drawString(x_start, y + 1, "\u2022")
            p = Paragraph(bullet, style_bullet)
            pw, ph = p.wrap(content_w - 10, 100)
            p.drawOn(c, x_start, y - ph + 3)
            y -= ph + 2

        y -= 10 if i < len(projects) - 1 else 12

    # ── CERTIFICACIONES ──
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x_start, y, "CERTIFICACIONES")
    y -= 3
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.5)
    c.line(x_start, y, x_start + 70, y)
    y -= 16

    cert_tracks = [
        ("Ciberseguridad & Redes", "Cisco Networking Academy",
         "Ethical Hacker \u00b7 Cyber Threat Management \u00b7 Introduction to Cybersecurity \u00b7 "
         "Network Support and Security \u00b7 Networking Devices and Initial Configuration"),
        ("SAP Business Technology Platform & Build", "SAP",
         "Exploring SAP BTP \u00b7 Terraform on SAP BTP \u00b7 Joule Studio in SAP Build \u00b7 "
         "SAP Build Work Zone \u00b7 SAP Build Process Automation \u00b7 Agentic Systems (Human-Centered)"),
        ("SAP Analytics Cloud", "SAP",
         "Exploring \u00b7 Designing Stories \u00b7 Extended Stories \u00b7 Data Connections (Cloud y On-Premise) \u00b7 "
         "Security & Administration"),
        ("Desarrollo & Datos", "Santander \u00b7 TecNM \u00b7 Cisco",
         "JavaScript \u00b7 Inteligencia Artificial \u00b7 Data Analyst Essentials"),
    ]

    style_certlist = ParagraphStyle(
        "certlist", fontName="Helvetica", fontSize=7, leading=9.5,
        textColor=MID_TEXT, alignment=TA_LEFT, leftIndent=8,
    )

    for title, issuer, items in cert_tracks:
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(x_start, y, title)
        c.setFillColor(ACCENT_DARK)
        c.setFont("Helvetica-Oblique", 7)
        c.drawRightString(x_end, y, issuer)
        y -= 11
        p = Paragraph(items, style_certlist)
        pw, ph = p.wrap(content_w - 8, 100)
        p.drawOn(c, x_start, y - ph + 2)
        y -= ph + 9


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
