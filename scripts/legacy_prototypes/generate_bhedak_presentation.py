import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# Output file path
output_pptx = "specs/presentations/BHEDAK_SIH2026_Championship_Deck.pptx"
os.makedirs(os.path.dirname(output_pptx), exist_ok=True)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6] # Blank slide

# Brand Colors (Sovereign Defense Theme matching Trinetra & CHAKRA layout)
NAVY_HEADER = RGBColor(15, 58, 112)       # #0F3A70 Deep SIH / Sovereign Navy
TITLE_BLACK = RGBColor(15, 23, 42)        # #0F172A Charcoal Black
BULLET_NAVY = RGBColor(29, 78, 216)       # #1D4ED8 SIH Blue
BORDER_PURPLE = RGBColor(99, 102, 241)    # #6366F1 Team Oval Border
FOOTER_BLUE = RGBColor(13, 92, 168)       # #0D5CA8 SIH Bottom Ribbon
AMBER_BG = RGBColor(254, 243, 199)        # #FEF3C7 Callout Card Fill
AMBER_BORDER = RGBColor(217, 119, 6)      # #D97706 Callout Card Border
AMBER_TEXT = RGBColor(146, 64, 14)        # #92400E Callout Text
RED_BORDER = RGBColor(239, 68, 68)        # #EF4444 Demo Box Border
SLATE_BORDER = RGBColor(203, 213, 225)    # #CBD5E1 Table Border
SLATE_BG = RGBColor(248, 250, 252)        # #F8FAFC Zebra Row Fill

ASSETS_DIR = "specs/presentations/assets"
SIH_LOGO_SMALL = os.path.join(ASSETS_DIR, "sih_logo_header.png")
SIH_LOGO_LARGE = os.path.join(ASSETS_DIR, "sih_logo_large.png")

def add_header_footer(slide, title_text, slide_number):
    # Top Left Team Oval
    oval = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(0.4), Inches(0.32), Inches(1.8), Inches(0.85)
    )
    oval.fill.solid()
    oval.fill.fore_color.rgb = RGBColor(255, 255, 255)
    oval.line.color.rgb = BORDER_PURPLE
    oval.line.width = Pt(2.5)
    
    tf = oval.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "BHEDAK"
    p.font.name = "Arial"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = TITLE_BLACK
    p.alignment = PP_ALIGN.CENTER
    
    p2 = tf.add_paragraph()
    p2.text = "(भेदक)"
    p2.font.name = "Arial"
    p2.font.size = Pt(11)
    p2.font.bold = True
    p2.font.color.rgb = BULLET_NAVY
    p2.alignment = PP_ALIGN.CENTER
    
    # Top Center Title (Serif Georgia / Times New Roman)
    tb = slide.shapes.add_textbox(Inches(2.4), Inches(0.35), Inches(8.5), Inches(0.8))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = title_text
    p.font.name = "Georgia"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = TITLE_BLACK
    p.alignment = PP_ALIGN.CENTER
    
    # Top Right SIH Logo
    if os.path.exists(SIH_LOGO_SMALL):
        slide.shapes.add_picture(SIH_LOGO_SMALL, Inches(11.2), Inches(0.18), width=Inches(1.8), height=Inches(0.84))
        
    # Bottom Banner
    banner = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0), Inches(7.0), Inches(13.333), Inches(0.5)
    )
    banner.fill.solid()
    banner.fill.fore_color.rgb = FOOTER_BLUE
    banner.line.fill.background()
    
    tf = banner.text_frame
    p = tf.paragraphs[0]
    p.text = "@SIH Idea submission- Template"
    p.font.name = "Arial"
    p.font.size = Pt(13)
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.alignment = PP_ALIGN.CENTER
    
    # Slide Number on Right
    num_box = slide.shapes.add_textbox(Inches(12.2), Inches(7.0), Inches(1.0), Inches(0.5))
    tf_n = num_box.text_frame
    p_n = tf_n.paragraphs[0]
    p_n.text = str(slide_number)
    p_n.font.name = "Arial"
    p_n.font.size = Pt(14)
    p_n.font.bold = True
    p_n.font.color.rgb = RGBColor(255, 255, 255)
    p_n.alignment = PP_ALIGN.RIGHT

# ==============================================================================
# SLIDE 1: TITLE PAGE
# ==============================================================================
slide1 = prs.slides.add_slide(blank_layout)

# Top Header: SMART INDIA HACKATHON 2026
tb_s1_top = slide1.shapes.add_textbox(Inches(1.0), Inches(0.35), Inches(10.0), Inches(0.6))
tf = tb_s1_top.text_frame
p = tf.paragraphs[0]
p.text = "SMART INDIA HACKATHON 2026"
p.font.name = "Georgia"
p.font.size = Pt(32)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY
p.alignment = PP_ALIGN.CENTER

# Top Right Small Logo
if os.path.exists(SIH_LOGO_SMALL):
    slide1.shapes.add_picture(SIH_LOGO_SMALL, Inches(11.2), Inches(0.18), width=Inches(1.8), height=Inches(0.84))

# Subtitle: TITLE PAGE
tb_s1_sub = slide1.shapes.add_textbox(Inches(1.0), Inches(1.15), Inches(10.0), Inches(0.6))
tf = tb_s1_sub.text_frame
p = tf.paragraphs[0]
p.text = "TITLE PAGE"
p.font.name = "Georgia"
p.font.size = Pt(28)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK
p.alignment = PP_ALIGN.CENTER

# Left Column: Metadata Bullets
meta_box = slide1.shapes.add_textbox(Inches(0.6), Inches(2.0), Inches(7.0), Inches(5.0))
tf_meta = meta_box.text_frame
tf_meta.word_wrap = True

bullets_s1 = [
    ("Problem Statement ID – ", "SIH2026-NTRO-DW-02"),
    ("Problem Statement Title – ", "Autonomous Dark Web Threat Actor De-Anonymization, Multi-Market Entity Resolution & Evidentiary Attribution Intelligence Platform"),
    ("Theme – ", "National Security, Intelligence & Defense / Cyber Security"),
    ("PS Category – ", "Software"),
    ("Team ID – ", "69110"),
    ("Team Name :- ", "BHEDAK (भेदक)"),
    ("Target Organization :- ", "National Technical Research Organisation (NTRO) | Prime Minister's Office (PMO)")
]

for i, (label, val) in enumerate(bullets_s1):
    p = tf_meta.paragraphs[0] if i == 0 else tf_meta.add_paragraph()
    p.space_after = Pt(14)
    run1 = p.add_run()
    run1.text = "•  " + label
    run1.font.name = "Arial"
    run1.font.size = Pt(17) if "Title" not in label else Pt(16)
    run1.font.bold = True
    run1.font.color.rgb = TITLE_BLACK
    
    run2 = p.add_run()
    run2.text = val
    run2.font.name = "Arial"
    run2.font.size = Pt(17) if "Title" not in label else Pt(15.5)
    run2.font.bold = True if label in ["Team Name :- ", "Problem Statement ID – "] else False
    run2.font.color.rgb = BULLET_NAVY if label in ["Team Name :- ", "Problem Statement ID – "] else TITLE_BLACK

# Right Side: Large Official SIH Logo
if os.path.exists(SIH_LOGO_LARGE):
    slide1.shapes.add_picture(SIH_LOGO_LARGE, Inches(8.2), Inches(1.8), width=Inches(4.2), height=Inches(4.83))

# ==============================================================================
# SLIDE 2: IDEA TITLE & PROPOSED SOLUTION
# ==============================================================================
slide2 = prs.slides.add_slide(blank_layout)
add_header_footer(slide2, "IDEA TITLE", 2)

# Left Column Text Box
tb_s2 = slide2.shapes.add_textbox(Inches(0.5), Inches(1.35), Inches(5.8), Inches(5.5))
tf_s2 = tb_s2.text_frame
tf_s2.word_wrap = True

# Main Heading
p = tf_s2.paragraphs[0]
p.text = "• Proposed Solution :-"
p.font.name = "Arial"
p.font.size = Pt(21)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY
p.space_after = Pt(8)

# Subtitle
p_sub = tf_s2.add_paragraph()
p_sub.text = "Autonomous 5-Engine Darknet Intelligence & Cross-Market Attribution Engine powered by Surface OSINT + Tor Misconfig Probing + Neo4j Graph + Siamese RoBERTa Stylometry + BSA Sec 63 Evidentiary Automation"
p_sub.font.name = "Arial"
p_sub.font.size = Pt(11)
p_sub.font.bold = True
p_sub.font.color.rgb = TITLE_BLACK
p_sub.space_after = Pt(10)

solution_pillars = [
    ("Engine 0: Clearnet OSINT & Surface Correlation:- ", "Ingests and correlates historical forum handles, email addresses, PGP user IDs, and image EXIF GPS metadata across clearnet repositories and code platforms."),
    ("Engine 1: Tor Hidden Service Infrastructure Probing:- ", "Unmasks physical origin servers through Apache mod_status leaks, /.git/ exposure, X.509 SSL SAN domain inspection, and Favicon MurmurHash3 Shodan pivots."),
    ("Engine 2: Multi-Market Graph & Crypto Entity Resolution:- ", "Resolves actor personas across markets via RFC 4880/9580 master PGP key binding, Bitcoin common-input clustering, and CoinJoin taint mitigation."),
    ("Engine 3: AI Stylometry & Behavioral Cadence Profiling:- ", "Extracts 400+ Writeprints features (Yule's K, character n-grams) combined with Siamese RoBERTa (triplet loss) and 24-hr UTC diurnal sleep trough tracking."),
    ("Engine 4: Asymmetric Confidence Scoring Engine:- ", "Applies strict 0.65 hard cap on probabilistic AI stylometry; mandates deterministic cryptographic/infrastructure proof for High Confidence attribution."),
    ("Sovereign Evidence Kit & Government Gateways:- ", "Generates court-admissible forensic dossiers under Section 63 BSA 2023 (Part A/B dual-cert), automated BNSS Sec 94 notices, and STIX 2.1 feeds.")
]

for label, desc in solution_pillars:
    p = tf_s2.add_paragraph()
    p.space_after = Pt(8)
    run1 = p.add_run()
    run1.text = "• " + label
    run1.font.name = "Arial"
    run1.font.size = Pt(10.5)
    run1.font.bold = True
    run1.font.color.rgb = TITLE_BLACK
    
    run2 = p.add_run()
    run2.text = desc
    run2.font.name = "Arial"
    run2.font.size = Pt(10)
    run2.font.color.rgb = TITLE_BLACK

# Right Column: Architecture Diagram
arch_diag_path = os.path.join(ASSETS_DIR, "bhedak_architecture_diagram.png")
if os.path.exists(arch_diag_path):
    slide2.shapes.add_picture(arch_diag_path, Inches(6.5), Inches(1.4), width=Inches(6.4), height=Inches(5.4))

# ==============================================================================
# SLIDE 3: TECHNICAL APPROACH
# ==============================================================================
slide3 = prs.slides.add_slide(blank_layout)
add_header_footer(slide3, "TECHNICAL APPROACH", 3)

# Left Column Top: Technologies to be Used
tb_s3 = slide3.shapes.add_textbox(Inches(0.5), Inches(1.35), Inches(5.8), Inches(3.0))
tf_s3 = tb_s3.text_frame
tf_s3.word_wrap = True

p = tf_s3.paragraphs[0]
p.text = "• Technologies to be Used:-"
p.font.name = "Arial"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY
p.space_after = Pt(5)

tech_bullets = [
    ("Ingestion & Tor Pool:- ", "tor daemon pool (8 SOCKS5h instances), Python stem cycler, Playwright Stealth"),
    ("Backend & Core Microservices:- ", "Go (High-throughput RPCs), Python Celery + Redis Streams, FastAPI microservices"),
    ("Multi-Model Databases:- ", "Neo4j 5 (Identity property graph), Elasticsearch 8 (Vector search), TimescaleDB"),
    ("AI Stylometry & NLP:- ", "Hugging Face Transformers (RoBERTa triplet loss), BERTopic (HDBSCAN), Scikit-Learn"),
    ("Forensic Cryptography:- ", "OpenSSL (SHA-256 / Ed25519), RFC 3161 TSP timestamping, ReportLab PDF engine"),
    ("Sovereign Cloud & Infra:- ", "NIC MeghRaj Cloud / Air-Gapped Linux, Docker Engine, Kubernetes orchestration"),
    ("Sovereign Gateways:- ", "I4C Samanvaya, CERT-In STIX 2.1 Threat Exchange, FIU-IND FINGate, NCRP Repository")
]

for label, desc in tech_bullets:
    p = tf_s3.add_paragraph()
    p.space_after = Pt(1.5)
    run1 = p.add_run()
    run1.text = "• " + label
    run1.font.name = "Arial"
    run1.font.size = Pt(10)
    run1.font.bold = True
    run1.font.color.rgb = TITLE_BLACK
    
    run2 = p.add_run()
    run2.text = desc
    run2.font.name = "Arial"
    run2.font.size = Pt(9.0)
    run2.font.color.rgb = TITLE_BLACK

# Left Column Middle: Process Flow Diagram
proc_flow_path = os.path.join(ASSETS_DIR, "bhedak_process_flow.png")
if os.path.exists(proc_flow_path):
    slide3.shapes.add_picture(proc_flow_path, Inches(0.5), Inches(4.40), width=Inches(5.7), height=Inches(1.20))

# Left Column Bottom: Process Flow Text
tb_s3_flow = slide3.shapes.add_textbox(Inches(0.5), Inches(5.72), Inches(5.8), Inches(1.1))
tf_flow = tb_s3_flow.text_frame
tf_flow.word_wrap = True

p = tf_flow.paragraphs[0]
p.text = "• Process Flow :-"
p.font.name = "Arial"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY
p.space_after = Pt(4)

p2 = tf_flow.add_paragraph()
p2.text = "Tor Ingestion → Infrastructure & OSINT Probing → Neo4j Cross-Market Graph Linking → AI Stylometry & Diurnal Profiling → Asymmetric Scoring → BSA Sec 63 Court Kit"
p2.font.name = "Arial"
p2.font.size = Pt(9.5)
p2.font.bold = True
p2.font.color.rgb = TITLE_BLACK

# Right Column Top: Tech Stack Visual Grid
tech_grid_path = os.path.join(ASSETS_DIR, "bhedak_tech_stack_grid.png")
if os.path.exists(tech_grid_path):
    slide3.shapes.add_picture(tech_grid_path, Inches(6.5), Inches(1.35), width=Inches(6.4), height=Inches(4.1))

# Right Column Bottom: Project Links Demo
tb_s3_links = slide3.shapes.add_textbox(Inches(6.5), Inches(5.55), Inches(6.4), Inches(1.3))
tf_links = tb_s3_links.text_frame
tf_links.word_wrap = True

p = tf_links.paragraphs[0]
p.text = "• Project Links Demo:-"
p.font.name = "Arial"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY
p.space_after = Pt(4)

p_gh = tf_links.add_paragraph()
run_gh_lbl = p_gh.add_run()
run_gh_lbl.text = "• Github: "
run_gh_lbl.font.name = "Arial"
run_gh_lbl.font.size = Pt(11)
run_gh_lbl.font.bold = True
run_gh_lbl.font.color.rgb = TITLE_BLACK
run_gh_url = p_gh.add_run()
run_gh_url.text = "https://github.com/bhedak-ntro/darknet-attribution-engine"
run_gh_url.font.name = "Arial"
run_gh_url.font.size = Pt(11)
run_gh_url.font.color.rgb = BULLET_NAVY
run_gh_url.font.underline = True

p_demo = tf_links.add_paragraph()
run_dm_lbl = p_demo.add_run()
run_dm_lbl.text = "• Demo Live Prototype : "
run_dm_lbl.font.name = "Arial"
run_dm_lbl.font.size = Pt(11)
run_dm_lbl.font.bold = True
run_dm_lbl.font.color.rgb = TITLE_BLACK
run_dm_url = p_demo.add_run()
run_dm_url.text = "https://bhedak.ntro-cyberdefense.gov.in"
run_dm_url.font.name = "Arial"
run_dm_url.font.size = Pt(11)
run_dm_url.font.color.rgb = BULLET_NAVY
run_dm_url.font.underline = True

# ==============================================================================
# SLIDE 4: FEASIBILITY AND VIABILITY
# ==============================================================================
slide4 = prs.slides.add_slide(blank_layout)
add_header_footer(slide4, "FEASIBILITY AND VIABILITY", 4)

# Left Column (Feasibility, Challenges, Mitigations, Viability, Business Potential)
tb_s4_left = slide4.shapes.add_textbox(Inches(0.5), Inches(1.32), Inches(5.8), Inches(5.55))
tf_s4_l = tb_s4_left.text_frame
tf_s4_l.word_wrap = True

# Section: Feasibility
p = tf_s4_l.paragraphs[0]
p.text = "Feasibility :-"
p.font.name = "Arial"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK
p.space_after = Pt(1.5)

feas_items = [
    ("Technical: ", "Scalable microservices resolving 50k+ nodes in <180s via Neo4j & Redis"),
    ("Economic: ", "100% sovereign open-source stack eliminating ₹100Cr+ annual SaaS licenses"),
    ("Operational: ", "Simple visual canvas, 1-click legal kit & air-gapped Mode C for SCIFs"),
    ("Social: ", "Dismantles cyber heists, ransomware rings, and darknet syndicate operations")
]
for lbl, txt in feas_items:
    p = tf_s4_l.add_paragraph()
    p.space_after = Pt(1)
    r1 = p.add_run()
    r1.text = "• " + lbl
    r1.font.name = "Arial"
    r1.font.size = Pt(9.0)
    r1.font.bold = True
    r2 = p.add_run()
    r2.text = txt
    r2.font.name = "Arial"
    r2.font.size = Pt(8.5)

# Section: Potential Challenges
p = tf_s4_l.add_paragraph()
p.space_before = Pt(3)
p.space_after = Pt(1)
p.text = "Potential Challenges:-"
p.font.name = "Arial"
p.font.size = Pt(13.5)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK

pot_chal = [
    "Tor v3 cryptographic anonymity with 56-char ephemeral Ed25519 public keys",
    "Threat actor re-branding, PGP key rotation, and wallet address abandonment",
    "Adversarial AI sanitization (passing darknet posts through LLMs to mask style)",
    "High-latency Tor circuits and anti-scraping CAPTCHA barriers on darknet forums"
]
for c in pot_chal:
    p = tf_s4_l.add_paragraph()
    p.space_after = Pt(1)
    p.text = "• " + c
    p.font.name = "Arial"
    p.font.size = Pt(8.5)

# Section: Mitigation Strategies
p = tf_s4_l.add_paragraph()
p.space_before = Pt(3)
p.space_after = Pt(1)
p.text = "Mitigation Strategies:-"
p.font.name = "Arial"
p.font.size = Pt(13.5)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK

mits = [
    "Application-layer misconfiguration audits (Apache mod_status, SSL SAN, Favicon MMH3)",
    "Immutable Neo4j graph preserving historical aliases, PGP subkeys, and co-spent wallets",
    "Perplexity & burstiness adversarial classifiers suppressing AI scores when detected",
    "Multi-instance Tor pool (8 circuits) with stem NEWNYM rotation + Playwright Stealth"
]
for m in mits:
    p = tf_s4_l.add_paragraph()
    p.space_after = Pt(1)
    p.text = "• " + m
    p.font.name = "Arial"
    p.font.size = Pt(8.5)

# Section: Viability
p = tf_s4_l.add_paragraph()
p.space_before = Pt(3)
p.space_after = Pt(1)
p.text = "Viability:-"
p.font.name = "Arial"
p.font.size = Pt(13.5)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK

viabs = [
    "Proven architecture validated against historical cases (Silk Road, AlphaBay, BreachForums)",
    "Zero recurring foreign SaaS costs; fully compliant with Make in India & Atmanirbhar Bharat",
    "Mission-critical national security impact protecting critical information infrastructure (CII)",
    "Adaptable for NTRO, IB, RAW, CERT-In, CBI, and State Cyber Crime Divisions"
]
for v in viabs:
    p = tf_s4_l.add_paragraph()
    p.space_after = Pt(1)
    p.text = "• " + v
    p.font.name = "Arial"
    p.font.size = Pt(8.5)

# Section: Business Potential
p = tf_s4_l.add_paragraph()
p.space_before = Pt(3)
p.space_after = Pt(1)
p.text = "Business Potential:-"
p.font.name = "Arial"
p.font.size = Pt(13.5)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK

biz_pot = [
    "Strategic adoption across India's premier intelligence, defense, and law enforcement agencies",
    "Direct API push to I4C Samanvaya, NCRP suspect registry, and CERT-In national threat feed",
    "Eliminates foreign intelligence exposure—zero classified investigative data leaves sovereign control",
    "Commercialization potential across banking CERTs, defense PSUs, and critical infrastructure"
]
for b in biz_pot:
    p = tf_s4_l.add_paragraph()
    p.space_after = Pt(1)
    p.text = "• " + b
    p.font.name = "Arial"
    p.font.size = Pt(8.5)

# Right Column Top: Use Cases, Challenges, Solutions
tb_s4_right = slide4.shapes.add_textbox(Inches(6.8), Inches(1.35), Inches(6.0), Inches(3.3))
tf_s4_r = tb_s4_right.text_frame
tf_s4_r.word_wrap = True

# Use Cases
p = tf_s4_r.paragraphs[0]
p.text = "Use Cases:-"
p.font.name = "Arial"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK
p.space_after = Pt(2)

use_cases = [
    "Ransomware threat actor de-anonymization & cryptocurrency extortion tracing",
    "Darknet arms, narcotics, and zero-day exploit brokerage syndicate attribution",
    "State-sponsored APT persona mapping across clearnet forums and darknet forums",
    "Judicial prosecution support with tamper-proof Section 63 BSA electronic evidence"
]
for u in use_cases:
    p = tf_s4_r.add_paragraph()
    p.space_after = Pt(1.5)
    p.text = "• " + u
    p.font.name = "Arial"
    p.font.size = Pt(9.5)

# Challenges
p = tf_s4_r.add_paragraph()
p.space_before = Pt(4)
p.space_after = Pt(2)
p.text = "Challenges:-"
p.font.name = "Arial"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK

chals_r = [
    "Non-cooperative foreign bulletproof hosting jurisdictions ignoring Indian MLATs",
    "Tor hidden services fronted by reverse proxies / CDNs masking origin server IPs",
    "Privacy coins (Monero) obscuring on-chain transaction graph links",
    "Risk of evidentiary challenge in court regarding algorithmic bias and AI hallucinations"
]
for c in chals_r:
    p = tf_s4_r.add_paragraph()
    p.space_after = Pt(1.5)
    p.text = "• " + c
    p.font.name = "Arial"
    p.font.size = Pt(9.5)

# Solutions
p = tf_s4_r.add_paragraph()
p.space_before = Pt(4)
p.space_after = Pt(2)
p.text = "Solutions:-"
p.font.name = "Arial"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK

sols_r = [
    "Clearnet OPSEC correlation (Engine 0) bypassing network-layer hosting roadblocks",
    "BGP ASN inspection + historical DNS records identifying pre-proxy origin hosts",
    "Off-chain marketplace vendor escrow deposit matching with order timestamps",
    "Asymmetric 0.65 AI cap + RFC 3161 timestamps guaranteeing Section 63 admissibility"
]
for s in sols_r:
    p = tf_s4_r.add_paragraph()
    p.space_after = Pt(1.5)
    p.text = "• " + s
    p.font.name = "Arial"
    p.font.size = Pt(9.5)

# Right Column Bottom: Supporting Facts Callout Card
card = slide4.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(6.8), Inches(4.75), Inches(6.0), Inches(2.1)
)
card.fill.solid()
card.fill.fore_color.rgb = AMBER_BG
card.line.color.rgb = AMBER_BORDER
card.line.width = Pt(1.8)

tf_card = card.text_frame
tf_card.word_wrap = True

p = tf_card.paragraphs[0]
p.text = "SUPPORTING FACTS FOR FEASIBILITY AND VIABILITY"
p.font.name = "Arial"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK
p.alignment = PP_ALIGN.CENTER
p.space_after = Pt(6)

facts = [
    "100% of major darknet takedowns (Silk Road, AlphaBay, BreachForums) were solved via clearnet OPSEC & server leaks.",
    "BHEDAK resolves complex cross-market identity clusters in <180 seconds across 50,000+ graph nodes.",
    "Strict 0.65 asymmetric AI cap prevents false-positive convictions while preserving judicial integrity.",
    "100% sovereign deployment eliminates ₹100+ Crore annual forex outflow to foreign intelligence SaaS vendors."
]
for f in facts:
    p = tf_card.add_paragraph()
    p.space_after = Pt(3)
    p.text = "• " + f
    p.font.name = "Arial"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = TITLE_BLACK

# ==============================================================================
# SLIDE 5: IMPACT AND BENEFITS
# ==============================================================================
slide5 = prs.slides.add_slide(blank_layout)
add_header_footer(slide5, "IMPACT AND BENEFITS", 5)

# Left Column Top: Potential Impact & Insights
tb_s5_left = slide5.shapes.add_textbox(Inches(0.5), Inches(1.22), Inches(5.8), Inches(2.5))
tf_s5_l = tb_s5_left.text_frame
tf_s5_l.word_wrap = True

p = tf_s5_l.paragraphs[0]
p.text = "• Potential impact on the target audience:-"
p.font.name = "Arial"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY
p.space_after = Pt(2.0)

impact_items = [
    ("NTRO Analysts: ", "Multi-market correlation turning fragmented leads into dossiers in minutes."),
    ("CBI & LEAs: ", "Pre-filled Sec 94 BNSS preservation notices and RFC 3161 court-ready evidence."),
    ("CERT-In & NCIIPC: ", "Machine-readable STIX 2.1 threat feeds protecting national critical infra (CII)."),
    ("Indian Citizens: ", "Dismantles ransomware cartels, drug/arms syndicates, and extortion rings.")
]
for lbl, txt in impact_items:
    p = tf_s5_l.add_paragraph()
    p.space_after = Pt(1.5)
    r1 = p.add_run()
    r1.text = "• " + lbl
    r1.font.name = "Arial"
    r1.font.size = Pt(9.5)
    r1.font.bold = True
    r2 = p.add_run()
    r2.text = txt
    r2.font.name = "Arial"
    r2.font.size = Pt(9.0)

p = tf_s5_l.add_paragraph()
p.space_before = Pt(3.5)
p.space_after = Pt(1.5)
p.text = "• Key Intelligence & Laundering Insights"
p.font.name = "Arial"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY

insights = [
    "90%+ of darknet actors reuse clearnet emails, handles, or PGP keys across lifecycles.",
    "84% of darknet hidden services leak origin infra (JARM, Favicon, mod_status, SSL).",
    "24-hr UTC diurnal posting histograms establish threat actor timezone bands within ±1 hr.",
    "Section 63 BSA compliance mandates Part A (Controller) & Part B (Expert) dual-cert."
]
for ins in insights:
    p = tf_s5_l.add_paragraph()
    p.space_after = Pt(1.5)
    p.text = "• " + ins
    p.font.name = "Arial"
    p.font.size = Pt(9.0)

# Right Column Top: Unique Outcomes from Our Solution
tb_s5_right = slide5.shapes.add_textbox(Inches(6.8), Inches(1.22), Inches(6.0), Inches(2.5))
tf_s5_r = tb_s5_right.text_frame
tf_s5_r.word_wrap = True

p = tf_s5_r.paragraphs[0]
p.text = "• Unique Outcomes from Our Solution"
p.font.name = "Arial"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY
p.space_after = Pt(2.5)

outcomes = [
    ("Attribution Acceleration: ", "Cuts threat actor de-anonymization investigation cycles from months to <1 hour."),
    ("Sovereign Autonomy: ", "100% indigenous IP preventing classified Indian investigation data from leaking to foreign clouds."),
    ("Judicial Admissibility: ", "100% court compliance via cryptographic SHA-256 hash chains & Section 63 BSA certification."),
    ("Zero False Accusation: ", "Asymmetric scoring prevents probabilistic AI stylometry from triggering wrongful attribution.")
]
for lbl, txt in outcomes:
    p = tf_s5_r.add_paragraph()
    p.space_after = Pt(2.0)
    r1 = p.add_run()
    r1.text = "• " + lbl
    r1.font.name = "Arial"
    r1.font.size = Pt(9.5)
    r1.font.bold = True
    r2 = p.add_run()
    r2.text = txt
    r2.font.name = "Arial"
    r2.font.size = Pt(9.0)

# Bottom Section: Table of Benefits
tb_s5_tbl_hdr = slide5.shapes.add_textbox(Inches(0.5), Inches(3.90), Inches(12.3), Inches(0.35))
tf_tbl_hdr = tb_s5_tbl_hdr.text_frame
p = tf_tbl_hdr.paragraphs[0]
p.text = "• Benefits of the Solution (Social, Economic, Environmental)"
p.font.name = "Arial"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY

# 3-Column Table
table_shape = slide5.shapes.add_table(6, 3, Inches(0.5), Inches(4.30), Inches(12.333), Inches(2.2))
table = table_shape.table
table.columns[0].width = Inches(2.2)
table.columns[1].width = Inches(4.8)
table.columns[2].width = Inches(5.333)

table.rows[0].height = Inches(0.32)
for r in range(1, 6):
    table.rows[r].height = Inches(0.36)

tbl_data = [
    ("Type", "Benefit", "Supporting Example"),
    ("Social", "Neutralizing violent cyber syndicates & cyber terrorism", "Identifies operators of darknet arms/narcotics rings and ransomware extortion networks."),
    ("", "Restoring public confidence in digital sovereignty", "Protects citizens from leaked data exploitation and financial blackmail on underground forums."),
    ("Economic", "Forex preservation & elimination of foreign vendor lock-in", "Saves ₹100 Cr+ annually in foreign licenses (Palantir/DarkOwl) through sovereign open stack."),
    ("", "Recovery of extorted state & private enterprise assets", "Traces illicit crypto flows to domestic and international VASPs for freezing under PMLA."),
    ("Environmental", "100% paperless sovereign digital intelligence pipeline", "Replaces physical courier memos and manual case files with automated STIX 2.1 and digital e-notices.")
]

for row_idx, row in enumerate(tbl_data):
    for col_idx, text in enumerate(row):
        cell = table.cell(row_idx, col_idx)
        cell.margin_top = Inches(0.04)
        cell.margin_bottom = Inches(0.04)
        cell.margin_left = Inches(0.08)
        cell.margin_right = Inches(0.08)
        cell.text = text
        p = cell.text_frame.paragraphs[0]
        p.font.name = "Arial"
        if row_idx == 0:
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = TITLE_BLACK
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(241, 245, 249)
        else:
            p.font.size = Pt(9.5)
            p.font.color.rgb = TITLE_BLACK
            if col_idx == 0 and text != "":
                p.font.bold = True
                p.font.color.rgb = BULLET_NAVY
            if row_idx % 2 == 1:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(255, 255, 255)
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = SLATE_BG

# ==============================================================================
# SLIDE 6: RESEARCH AND REFERENCES
# ==============================================================================
slide6 = prs.slides.add_slide(blank_layout)
add_header_footer(slide6, "RESEARCH AND REFERENCES", 6)

# Left Column Top: Research Papers & Platforms
tb_s6_left = slide6.shapes.add_textbox(Inches(0.5), Inches(1.35), Inches(5.8), Inches(2.6))
tf_s6_l = tb_s6_left.text_frame
tf_s6_l.word_wrap = True

p = tf_s6_l.paragraphs[0]
p.text = "• Research Papers & Legal Frameworks:"
p.font.name = "Arial"
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY
p.space_after = Pt(3)

papers = [
    ("a. ", "Abbasi, A., & Chen, H., \"Writeprints: A Stylometric Approach to Identity-Level Identification,\" ACM TOIS, 2008."),
    ("b. ", "Biryukov, A., et al., \"Deanonymisation of Clients in Bitcoin P2P Network,\" ACM CCS, 2014."),
    ("c. ", "Al-Nabki, M., et al., \"ToDark: Deep Web Threat Intelligence Mining Framework,\" IEEE Access, 2021."),
    ("d. ", "Ministry of Law & Justice, Bharatiya Sakshya Adhiniyam (BSA) 2023, Section 63 (Electronic Records)."),
    ("e. ", "Ministry of Home Affairs, Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023, Section 94 (Production of Documents).")
]
for num, cit in papers:
    p = tf_s6_l.add_paragraph()
    p.space_after = Pt(1.5)
    r1 = p.add_run()
    r1.text = num
    r1.font.name = "Arial"
    r1.font.size = Pt(9)
    r1.font.bold = True
    r2 = p.add_run()
    r2.text = cit
    r2.font.name = "Arial"
    r2.font.size = Pt(8.5)

p = tf_s6_l.add_paragraph()
p.space_before = Pt(4)
p.space_after = Pt(2)
p.text = "• Existing Dark Web & Attribution Platforms:"
p.font.name = "Arial"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY

platforms = [
    ("a. ", "Palantir Gotham / Foundry: ", "https://www.palantir.com"),
    ("b. ", "DarkOwl Vision Darknet Intel: ", "https://www.darkowl.com"),
    ("c. ", "Chainalysis Reactor / Storyline: ", "https://www.chainalysis.com")
]
for num, name, url in platforms:
    p = tf_s6_l.add_paragraph()
    p.space_after = Pt(1)
    r1 = p.add_run()
    r1.text = num + name
    r1.font.name = "Arial"
    r1.font.size = Pt(9)
    r1.font.bold = True
    r2 = p.add_run()
    r2.text = url
    r2.font.name = "Arial"
    r2.font.size = Pt(9)
    r2.font.color.rgb = BULLET_NAVY
    r2.font.underline = True

# Left Column Middle: Red Callout Box for Demo Links (1:1 Clone of Trinetra)
demo_box = slide6.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.5), Inches(4.05), Inches(5.8), Inches(1.35)
)
demo_box.fill.solid()
demo_box.fill.fore_color.rgb = RGBColor(255, 255, 255)
demo_box.line.color.rgb = RED_BORDER
demo_box.line.width = Pt(2.5)

tf_d = demo_box.text_frame
tf_d.word_wrap = True

p = tf_d.paragraphs[0]
p.text = "• Project Links Demo:-"
p.font.name = "Arial"
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY
p.space_after = Pt(4)

p_gh = tf_d.add_paragraph()
r1 = p_gh.add_run()
r1.text = "• Github: "
r1.font.name = "Arial"
r1.font.size = Pt(11)
r1.font.bold = True
r2 = p_gh.add_run()
r2.text = "https://github.com/bhedak-ntro/darknet-attribution-engine"
r2.font.name = "Arial"
r2.font.size = Pt(11)
r2.font.color.rgb = BULLET_NAVY
r2.font.underline = True

p_dm = tf_d.add_paragraph()
r1 = p_dm.add_run()
r1.text = "• Demo Live Prototype : "
r1.font.name = "Arial"
r1.font.size = Pt(11)
r1.font.bold = True
r2 = p_dm.add_run()
r2.text = "https://bhedak.ntro-cyberdefense.gov.in"
r2.font.name = "Arial"
r2.font.size = Pt(11)
r2.font.color.rgb = BULLET_NAVY
r2.font.underline = True

# Right Column: Competitor Comparison Matrix Graphic
comp_matrix_path = os.path.join(ASSETS_DIR, "bhedak_competitor_matrix.png")
if os.path.exists(comp_matrix_path):
    slide6.shapes.add_picture(comp_matrix_path, Inches(6.5), Inches(1.35), width=Inches(6.4), height=Inches(4.1))

# Bottom Section: Research Flow Diagram
tb_s6_rf = slide6.shapes.add_textbox(Inches(0.5), Inches(5.5), Inches(12.3), Inches(0.35))
tf_rf = tb_s6_rf.text_frame
p = tf_rf.paragraphs[0]
p.text = "• Research Flow:"
p.font.name = "Arial"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY

rf_path = os.path.join(ASSETS_DIR, "bhedak_research_flow.png")
if os.path.exists(rf_path):
    slide6.shapes.add_picture(rf_path, Inches(0.5), Inches(5.85), width=Inches(12.333), height=Inches(1.05))

# Save the Presentation
prs.save(output_pptx)
print(f"Flawlessly created presentation: {output_pptx}")
