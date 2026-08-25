"""Genera el CV en PDF de Angel Emiliano Miranda Baeza.

Contenido sincronizado con index.html (portafolio) y con el CV maestro en Word.
Paleta alineada al portafolio: tinta profunda + ambar.

Uso:  python generate_cv.py
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import os

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CV_Angel_Miranda.pdf")

# ── Paleta (coherente con el portafolio) ──
INK        = HexColor("#14120f")   # barra lateral
INK_RULE   = HexColor("#2b251c")
AMBER      = HexColor("#e3a75c")
AMBER_DEEP = HexColor("#a8762f")
DARK_TEXT  = HexColor("#17150f")
MID_TEXT   = HexColor("#4c4740")
SIDE_TEXT  = HexColor("#cfc7b8")
SIDE_DIM   = HexColor("#9a9080")
WHITE      = white

W, H = letter          # 612 x 792
SIDEBAR_W = 196
PAD_X     = 22         # margen interno de la barra lateral
MAIN_X    = SIDEBAR_W + 26
MAIN_R    = W - 30
MAIN_W    = MAIN_R - MAIN_X
BOTTOM    = 42         # margen inferior antes de saltar de pagina


# ═══════════════ Estilos de parrafo ═══════════════
def _style(name, size, leading, color, align=TA_LEFT, indent=0, bold=False):
    return ParagraphStyle(
        name,
        fontName="Helvetica-Bold" if bold else "Helvetica",
        fontSize=size, leading=leading, textColor=color,
        alignment=align, leftIndent=indent,
    )


S_BODY   = _style("body",   8.1, 11.8, MID_TEXT, TA_JUSTIFY)
S_BULLET = _style("bullet", 7.5, 10.4, MID_TEXT, TA_JUSTIFY, indent=9)
S_SIDE   = _style("side",   6.9,  9.4, SIDE_TEXT)


# ═══════════════ Utilidades de dibujo ═══════════════
class Doc:
    """Lienzo con control de flujo vertical y salto de pagina."""

    def __init__(self, c):
        self.c = c
        self.y = H - 44
        self.page = 1

    # -- control de pagina --
    def space(self, needed):
        """Asegura `needed` puntos libres; si no, abre pagina nueva."""
        if self.y - needed < BOTTOM:
            self.new_page()

    def new_page(self):
        self.c.showPage()
        self.page += 1
        paint_chrome(self.c)
        self.y = H - 44

    # -- bloques --
    def heading(self, text, rule_w=64):
        self.space(40)
        c = self.c
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(MAIN_X, self.y, text)
        self.y -= 4
        c.setStrokeColor(AMBER)
        c.setLineWidth(1.6)
        c.line(MAIN_X, self.y, MAIN_X + rule_w, self.y)
        self.y -= 15

    def para(self, text, style=S_BODY, gap=9):
        p = Paragraph(text, style)
        _, ph = p.wrap(MAIN_W, 400)
        self.space(ph + 4)
        p.drawOn(self.c, MAIN_X, self.y - ph)
        self.y -= ph + gap

    def entry(self, title, right="", sub="", stack=""):
        """Encabezado de un puesto o proyecto."""
        self.space(46)
        c = self.c
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 9.3)
        c.drawString(MAIN_X, self.y, title)
        if right:
            c.setFillColor(MID_TEXT)
            c.setFont("Helvetica", 7.6)
            c.drawRightString(MAIN_R, self.y, right)
        self.y -= 11
        if sub:
            c.setFillColor(MID_TEXT)
            c.setFont("Helvetica-Oblique", 7.6)
            c.drawString(MAIN_X, self.y, sub)
            self.y -= 10
        if stack:
            c.setFillColor(AMBER_DEEP)
            c.setFont("Helvetica-Oblique", 7.2)
            c.drawString(MAIN_X, self.y, stack)
            self.y -= 11
        else:
            self.y -= 2

    def bullets(self, items, gap_after=9):
        for it in items:
            p = Paragraph(it, S_BULLET)
            _, ph = p.wrap(MAIN_W - 10, 300)
            self.space(ph + 4)
            self.c.setFillColor(AMBER_DEEP)
            self.c.setFont("Helvetica", 7.5)
            self.c.drawString(MAIN_X, self.y - 1, "•")
            p.drawOn(self.c, MAIN_X, self.y - ph + 1)
            self.y -= ph + 2.4
        self.y -= gap_after


def paint_chrome(c):
    """Barra lateral y filete superior (en cada pagina)."""
    c.setFillColor(INK)
    c.rect(0, 0, SIDEBAR_W, H, fill=1, stroke=0)
    c.setFillColor(AMBER)
    c.rect(0, H - 3.5, W, 3.5, fill=1, stroke=0)


# ═══════════════ Barra lateral ═══════════════
def draw_sidebar(c):
    x = PAD_X
    y = H - 46

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(x, y, "ANGEL EMILIANO")
    y -= 17
    c.drawString(x, y, "MIRANDA BAEZA")
    y -= 15
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 7.2)
    c.drawString(x, y, "DESARROLLADOR FULL-STACK")
    y -= 10
    c.drawString(x, y, "SAP CERTIFIED  |  FINTECH")

    def divider(yy):
        c.setStrokeColor(INK_RULE)
        c.setLineWidth(0.6)
        c.line(x, yy, SIDEBAR_W - PAD_X, yy)

    def section(title, yy):
        divider(yy)
        yy -= 15
        c.setFillColor(AMBER)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(x, yy, title)
        return yy - 13

    def items(pairs, yy, label_font=6.4, val_font=7.0, gap=10.4):
        for label, value in pairs:
            if label:
                c.setFillColor(AMBER_DEEP)
                c.setFont("Helvetica-Bold", label_font)
                c.drawString(x, yy, label)
                yy -= 8.4
            c.setFillColor(SIDE_TEXT)
            c.setFont("Helvetica", val_font)
            c.drawString(x, yy, value)
            yy -= gap
        return yy

    # ── Contacto ──
    y = section("CONTACTO", y - 16)
    y = items([
        ("EMAIL", "angelemilianomirandabaeza"),
    ], y, gap=8.2)
    c.setFillColor(SIDE_TEXT)
    c.setFont("Helvetica", 7.0)
    c.drawString(x, y, "@gmail.com")
    y -= 10.5
    y = items([
        ("ALTERNO", "angelmc06@outlook.com"),
        ("TEL", "56 1008 0655"),
        ("LINKEDIN", "/in/angel-miranda-dev"),
        ("GITHUB", "github.com/Miranda1108"),
        ("PORTAFOLIO", "miranda1108.github.io"),
        ("FIANZIFY", "fianzify.com"),
        ("UBICACION", "Ixtapaluca, Edo. de Mexico"),
    ], y)

    # ── Ecosistema SAP ──
    y = section("ECOSISTEMA SAP", y - 3)
    c.setFillColor(SIDE_TEXT)
    c.setFont("Helvetica", 6.8)
    for line in [
        "SAP BTP (Cloud Foundry, Kyma)",
        "SAP AI Core / Generative AI Hub",
        "SAP Fiori Elements / SAPUI5",
        "SAP Build Process Automation",
        "SAP Integration Suite",
        "Identity Services (IAS/IPS)",
        "Cloud Connector",
        "Terraform (SAP BTP provider)",
    ]:
        c.drawString(x, y, line)
        y -= 9.4

    # ── Stack ──
    y = section("STACK DE DESARROLLO", y - 3)
    groups = [
        ("Lenguajes", ["TypeScript / JavaScript", "Python  |  PHP  |  SQL", "Ensamblador x86 (TASM)"]),
        ("Backend", ["FastAPI  |  Node.js / Express", "Laravel  |  Serverless", "PostgreSQL / MySQL / Supabase"]),
        ("Frontend y movil", ["React  |  Next.js 16  |  Vue.js", "Capacitor (iOS + Android)", "Tailwind / Livewire / HTMX"]),
        ("Cloud y DevOps", ["Vercel / Netlify / Cloudflare", "Render / Railway / Codemagic", "GitHub Actions  |  DNS/TLS"]),
        ("Integraciones", ["API de Claude (Anthropic)", "Mercado Pago  |  Resend", "WhatsApp Business API"]),
        ("Infraestructura", ["Cisco Packet Tracer / VLAN", "HAProxy / NGINX / Fedora", "Windows Server (AD)"]),
    ]
    for cat, lines in groups:
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 7.0)
        c.drawString(x, y, cat)
        y -= 9.2
        c.setFillColor(SIDE_DIM)
        c.setFont("Helvetica", 6.6)
        for ln in lines:
            c.drawString(x + 4, y, ln)
            y -= 8.6
        y -= 3.4

    # ── Idiomas ──
    y = section("IDIOMAS", y - 1)
    c.setFillColor(SIDE_TEXT)
    c.setFont("Helvetica", 6.9)
    c.drawString(x, y, "Espanol  -  Nativo")


def draw_sidebar_p2(c):
    """Barra lateral de la segunda pagina: educacion y en preparacion."""
    x = PAD_X
    y = H - 46

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(x, y, "EDUCACION")
    y -= 14

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 7.6)
    c.drawString(x, y, "Ing. en Sistemas")
    y -= 9.4
    c.drawString(x, y, "Computacionales")
    y -= 11
    c.setFillColor(SIDE_TEXT)
    c.setFont("Helvetica", 6.8)
    c.drawString(x, y, "Tecnologico de Estudios")
    y -= 8.6
    c.drawString(x, y, "Superiores de Ixtapaluca")
    y -= 8.6
    c.drawString(x, y, "(TESI)")
    y -= 11
    c.setFillColor(AMBER_DEEP)
    c.setFont("Helvetica-Oblique", 6.8)
    c.drawString(x, y, "7o semestre  |  Grupo 1701")

    # En preparacion
    y -= 26
    c.setStrokeColor(INK_RULE)
    c.setLineWidth(0.6)
    c.line(x, y, SIDEBAR_W - PAD_X, y)
    y -= 15
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(x, y, "EN PREPARACION")
    y -= 13

    for title, detail in [
        ("SAP BTP Administrator", "C_ADBTP_2511"),
        ("CompTIA Security+", "y PenTest+"),
        ("Networking nivel CCNA", "ruteo y conmutacion"),
    ]:
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 6.9)
        c.drawString(x, y, title)
        y -= 8.6
        c.setFillColor(SIDE_DIM)
        c.setFont("Helvetica", 6.5)
        c.drawString(x + 4, y, detail)
        y -= 11.5


# ═══════════════ Contenido principal ═══════════════
def build(doc):
    # ── Perfil ──
    doc.heading("PERFIL PROFESIONAL", 96)
    doc.para(
        "Desarrollador full-stack <b>certificado por SAP</b> que lleva productos de cero a "
        "produccion: aplicaciones moviles publicadas en App Store y Google Play, plataformas web "
        "con cobro en linea y sistemas fintech que hoy operan para empresas reales. Participo en "
        "el desarrollo de <b>Fianzify</b>, plataforma de intermediacion de fianzas para el mercado mexicano. "
        "Experiencia comprobable en backend (FastAPI, Node.js, Laravel), frontend moderno "
        "(React, Next.js, Capacitor), integracion de IA en producto (API de Claude, SAP Generative "
        "AI Hub) y despliegue con CI/CD. Septimo semestre de Ingenieria en Sistemas Computacionales (TESI).",
        gap=13,
    )

    # ── Certificacion SAP ──
    doc.heading("CERTIFICACION SAP", 84)
    doc.entry(
        "SAP Generative AI Developer (C_AIG)",
        right="APROBADA",
        sub="Certificacion oficial SAP  |  SAP Learning Hub, Student Edition - 177 horas",
    )
    doc.para(
        "Desarrollo con IA generativa: prompt engineering sobre SAP AI Launchpad y Generative AI Hub, "
        "con evaluacion practica basada en sistema. Centro Publico de Formacion en Inteligencia "
        "Artificial (INFOTEC / Agencia de Transformacion Digital, Gobierno de Mexico). Primera "
        "generacion, enero-julio 2026.",
        gap=13,
    )

    # ── Experiencia ──
    doc.heading("EXPERIENCIA PROFESIONAL", 112)

    doc.entry(
        "Fianzify - Desarrollador",
        right="2025 - Presente",
        sub="Plataforma de intermediacion de fianzas  |  fianzify.com",
        stack="Next.js 16  |  TypeScript  |  Tailwind  |  Vercel  |  Supabase  |  API de Claude  |  Resend",
    )
    doc.bullets([
        "Desarrolle el sitio en Next.js 16 / TypeScript / Tailwind, desplegado en Vercel con dominio y correo corporativo propios.",
        "Integre un asistente conversacional con la API de Claude que califica prospectos y captura leads, con limite de tasa y persistencia de sesion.",
        "Construi un sistema interno de expedientes (Supabase/PostgreSQL) que extrae datos de contratos con IA, genera checklists dinamicos segun tipo de fianza y da seguimiento hasta la emision.",
        "Automatice la captacion: formulario con carga de documentos, analisis por IA, notificacion y confirmacion automatica al cliente via Resend.",
        "Implemente la estrategia SEO (sitemap, datos estructurados, blog y paginas por ciudad) con indexacion en Google Search Console.",
    ])

    doc.entry(
        "ADVANCE - Desarrollador Full-Stack, CRM y Bot de WhatsApp",
        right="2026 - Presente",
        sub="Promotora y Distribuidora de Instrumentos Financieros ADVANCE S.A.P.I. de C.V.",
        stack="Node.js  |  Express  |  PostgreSQL  |  WhatsApp Cloud API  |  Google Calendar  |  JWT  |  Railway",
    )
    doc.bullets([
        "Disene y desarrolle un bot conversacional en WhatsApp que califica prospectos, agenda citas y asigna asesores automaticamente (flujo de 15 etapas), habilitando atencion 24/7.",
        "Implemente generacion automatica de contratos en PDF y recopilacion segura de documentos (INE, comprobante de domicilio, CSF).",
        "Construi un panel administrativo con metricas en tiempo real (conversion, tasa de cierre, NPS), gestion de citas y contratos.",
        "Reforce el sistema con seguridad (JWT, validacion de webhook), pruebas automatizadas y CI/CD, entregando ~15 despliegues a produccion.",
        "Disene ademas una operacion de liquidacion OTC de stablecoins: estructura legal/fiscal, dashboards en vivo y sistemas de KYC.",
    ])

    # ── Proyectos ──
    doc.heading("PROYECTOS DESTACADOS", 104)

    doc.entry(
        "Gestori - App de finanzas personales (iOS + Android)",
        right="2026",
        sub="Publicada en App Store y Google Play  |  desarrollo full-stack individual",
        stack="React  |  TypeScript  |  FastAPI  |  Python  |  PostgreSQL  |  Capacitor  |  Codemagic  |  Render",
    )
    doc.bullets([
        "Backend en FastAPI con mas de 100 endpoints, PostgreSQL y un motor de movimientos que mantiene la consistencia del saldo mediante listeners de eventos.",
        "Frontend en React + Capacitor: una sola base de codigo compilada para iOS y Android.",
        "CI/CD de iOS en Codemagic - compilacion y firma sin Mac local, resolviendo code signing, perfiles de aprovisionamiento y publicacion automatica a TestFlight.",
        "Escribi ~315 pruebas automatizadas (backend y frontend) integradas al pipeline de compilacion.",
        "Gestione el ciclo completo de publicacion: prueba cerrada con 21 usuarios reales, iteracion sobre bugs y envio a produccion en ambas tiendas.",
    ])

    doc.entry(
        "Finanzas con Pam - Plataforma web con tienda digital",
        right="finanzasconpam.com",
        sub="Venta de productos digitales con entrega protegida",
        stack="JavaScript (ES6+)  |  Node.js  |  Netlify Functions/Blobs  |  Mercado Pago  |  Python (Pillow)",
    )
    doc.bullets([
        "Implemente venta de productos digitales con Mercado Pago (Checkout Pro) y entrega protegida: permisos de un solo uso con caducidad de 24 h y limite de descargas, emitidos tras verificar el pago contra la API del proveedor.",
        "Disene la arquitectura para que el precio resida en el servidor, no en el cliente, impidiendo su manipulacion desde el navegador.",
        "Desarrolle cuatro funciones serverless para cobros, verificacion de pagos, entrega de archivos y webhooks.",
        "Construi un sistema de diseno propio en CSS (~1,400 lineas, sin frameworks), consistente en 12 paginas.",
        "Detecte y corregi un sesgo estadistico en el cuestionario de perfil de inversionista que asignaba el mismo resultado al ~76% de los usuarios; recalibre los cortes a 30/50/20.",
        "Automatice un pipeline de imagenes en Python (Pillow): reduje el peso publicado de 2 MB a 299 KB (-85%).",
    ])

    doc.entry(
        "Ferreselect - Sitio corporativo y catalogo digital",
        right="2026  |  ferreselect.com",
        sub="Generador estatico propio, sin dependencias externas",
        stack="Node.js  |  JavaScript  |  Cloudflare Workers  |  JSON-LD",
    )
    doc.bullets([
        "Desarrolle un generador estatico en Node.js sin dependencias externas (2,000 lineas) que produce 70 paginas HTML a partir de un solo archivo de datos.",
        "Recupere el catalogo desde un PDF sin capa de texto: decodifique la codificacion desplazada de fuentes embebidas y extraje 74 imagenes de los streams comprimidos.",
        "Implemente SEO tecnico: URL limpia por producto, canonicas, sitemap.xml, Open Graph y datos estructurados JSON-LD.",
        "Construi una calculadora de materiales de 6 tipos que envia el resultado como mensaje precargado de WhatsApp, usada para captacion de prospectos.",
    ])

    # ── Credenciales ──
    doc.heading("CREDENCIALES ACREDITADAS", 116)
    tracks = [
        ("Ciberseguridad y Redes", "Cisco Networking Academy",
         "Ethical Hacker &middot; Cyber Threat Management &middot; Introduction to Cybersecurity &middot; "
         "Network Support and Security &middot; Networking Devices and Initial Configuration"),
        ("SAP Business Technology Platform y Build", "SAP",
         "Exploring SAP BTP &middot; Terraform on SAP BTP &middot; Joule Studio in SAP Build &middot; "
         "SAP Build Work Zone &middot; SAP Build Process Automation &middot; Agentic Systems (Human-Centered)"),
        ("SAP Analytics Cloud", "SAP",
         "Exploring &middot; Designing Stories &middot; Extended Stories &middot; Data Connections "
         "(Cloud y On-Premise) &middot; Security and Administration"),
        ("Programas colaborativos", "Santander  |  TecNM  |  Cisco",
         "JavaScript (Becas Santander) &middot; Inteligencia Artificial (TecNM) &middot; "
         "Data Analyst Essentials (Cisco)"),
    ]
    style_track = _style("track", 7.0, 9.4, MID_TEXT, indent=8)
    for title, issuer, items_txt in tracks:
        doc.space(30)
        doc.c.setFillColor(DARK_TEXT)
        doc.c.setFont("Helvetica-Bold", 7.9)
        doc.c.drawString(MAIN_X, doc.y, title)
        doc.c.setFillColor(AMBER_DEEP)
        doc.c.setFont("Helvetica-Oblique", 6.9)
        doc.c.drawRightString(MAIN_R, doc.y, issuer)
        doc.y -= 10
        p = Paragraph(items_txt, style_track)
        _, ph = p.wrap(MAIN_W - 8, 200)
        p.drawOn(doc.c, MAIN_X, doc.y - ph + 2)
        doc.y -= ph + 8


# ═══════════════ Enlaces clicables ═══════════════
def add_links(c):
    """Zonas clicables sobre la barra lateral (pagina 1)."""
    zones = [
        ("mailto:angelemilianomirandabaeza@gmail.com", 640, 668),
        ("mailto:angelmc06@outlook.com",               620, 638),
        ("tel:+525610080655",                          600, 618),
        ("https://linkedin.com/in/angel-miranda-dev",  580, 598),
        ("https://github.com/Miranda1108",             560, 578),
        ("https://miranda1108.github.io/portafolio-digital/", 540, 558),
        ("https://fianzify.com/",                      520, 538),
    ]
    for url, y0, y1 in zones:
        c.linkURL(url, (PAD_X - 4, y0, SIDEBAR_W - 8, y1), relative=0)


def main():
    c = canvas.Canvas(OUTPUT, pagesize=letter)
    c.setTitle("CV - Angel Emiliano Miranda Baeza")
    c.setAuthor("Angel Emiliano Miranda Baeza")
    c.setSubject("Curriculum Vitae - Desarrollador Full-Stack | SAP Certified")

    paint_chrome(c)
    draw_sidebar(c)
    add_links(c)

    doc = Doc(c)
    build(doc)

    # La barra lateral de la pagina 2 se pinta al final,
    # cuando ya sabemos que la pagina existe.
    if doc.page >= 2:
        draw_sidebar_p2(c)

    c.save()
    print("CV generado: {}  ({} pagina(s))".format(OUTPUT, doc.page))


if __name__ == "__main__":
    main()
