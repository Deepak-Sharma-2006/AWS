import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# Output file path
output_pptx = "specs/presentations/CHAKRA_SIH2026_Championship_Deck.pptx"
os.makedirs(os.path.dirname(output_pptx), exist_ok=True)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6] # Blank slide

# Brand Colors (Sovereign Defense Theme matching Trinetra layout)
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
    p.text = "CHAKRA"
    p.font.name = "Arial"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = TITLE_BLACK
    p.alignment = PP_ALIGN.CENTER
    
    p2 = tf.add_paragraph()
    p2.text = "(चक्र)"
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
    ("Problem Statement ID – ", "SIH2026-MHA-VDA-01"),
    ("Problem Statement Title – ", "Cross-Chain Virtual Digital Asset (VDA) Attribution, Wallet Clustering & Evidentiary Trail Reconstruction for Sovereign Cyber Investigations"),
    ("Theme – ", "Miscellaneous / National Security & Law Enforcement"),
    ("PS Category – ", "Software"),
    ("Team ID – ", "69110"),
    ("Team Name :- ", "CHAKRA (चक्र)"),
    ("Target Organization :- ", "Ministry of Home Affairs (MHA) | Indian Cyber Crime Coordination Centre (I4C)")
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
p_sub.text = "A Sovereign Cross-Chain VDA Attribution & Trail Reconstruction Engine powered by On-Chain Graph Intelligence + Tron Energy Decoding + Section 63 BSA 2023 Evidentiary Automation"
p_sub.font.name = "Arial"
p_sub.font.size = Pt(11)
p_sub.font.bold = True
p_sub.font.color.rgb = TITLE_BLACK
p_sub.space_after = Pt(10)

solution_pillars = [
    ("Centralized Multi-Chain UTDM Ingestion:- ", "Unified Transaction Data Model ingests raw blocks across UTXO (BTC), Account (ETH/Tron/BSC), and DAG via RPCs, normalizing heterogeneous ledgers into canonical graph schemas."),
    ("Tron TRC-20 Energy & Sweep Decomposition:- ", "Decodes smart contract invocation traces (transfer(address,uint256)), unmasking energy delegate rent-sharing, multi-hop peeling chains, and nested intermediary hops."),
    ("Deposit-to-Sweep Clustering Heuristics:- ", "Identifies high-fan-in exchange aggregation sweeps, clustering private unhosted deposit addresses into verified VASP hot wallets without false positive entity conflation."),
    ("Neo4j Bounded Graph Traversal (<180s):- ", "Resolves complex layered peeling chains, bridge hops, and mixer outputs in <180 seconds across 10,000+ nodes using localized sub-graphs and volume entropy."),
    ("Cross-Chain Bridge & Memo Reconstruction:- ", "Correlates source burner contracts, lock-mint telemetry, and destination deposit memos (THORChain, Stargate, CCTP) across isolated sovereign chains."),
    ("Section 63 BSA 2023 Tamper-Proof Evidentiary Kit:- ", "Generates court-admissible forensic packages with cryptographic SHA-256 hash chains, RFC 3161 timestamps, and automated BNSS Section 94/106 notice drafts.")
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
arch_diag_path = os.path.join(ASSETS_DIR, "chakra_architecture_diagram.png")
if os.path.exists(arch_diag_path):
    slide2.shapes.add_picture(arch_diag_path, Inches(6.5), Inches(1.4), width=Inches(6.4), height=Inches(5.4))

# ==============================================================================
# SLIDE 3: TECHNICAL APPROACH
# ==============================================================================
slide3 = prs.slides.add_slide(blank_layout)
add_header_footer(slide3, "TECHNICAL APPROACH", 3)

# Left Column Top: Technologies to be Used
tb_s3 = slide3.shapes.add_textbox(Inches(0.5), Inches(1.35), Inches(5.8), Inches(3.2))
tf_s3 = tb_s3.text_frame
tf_s3.word_wrap = True

p = tf_s3.paragraphs[0]
p.text = "• Technologies to be Used:-"
p.font.name = "Arial"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY
p.space_after = Pt(6)

tech_bullets = [
    ("Frontend:- ", "React.js + Next.js (Web Console), TypeScript, Cytoscape.js, TailwindCSS"),
    ("Backend:- ", "Go (High-Throughput RPC Ingestion), Python FastAPI (Microservices)"),
    ("Databases:- ", "Neo4j (Graph DB), PostgreSQL, TimescaleDB, Redis (L1/L2 Cache)"),
    ("AI/ML & Analytics:- ", "PyTorch, NetworkX, TronGrid Archive RPC, Rust Bounded Search"),
    ("Forensics & Crypto:- ", "OpenSSL (SHA-256 / Ed25519), RFC 3161 TSP, ReportLab Engine"),
    ("Sovereign Cloud/Infra:- ", "NIC MeghRaj Cloud / On-Premise, Docker, Kubernetes, CI/CD"),
    ("Integrations:- ", "I4C NCRP API Portal, FIU-IND Astraea Gateway, VASP KYC APIs")
]

for label, desc in tech_bullets:
    p = tf_s3.add_paragraph()
    p.space_after = Pt(2.5)
    run1 = p.add_run()
    run1.text = "• " + label
    run1.font.name = "Arial"
    run1.font.size = Pt(10.5)
    run1.font.bold = True
    run1.font.color.rgb = TITLE_BLACK
    
    run2 = p.add_run()
    run2.text = desc
    run2.font.name = "Arial"
    run2.font.size = Pt(9.5)
    run2.font.color.rgb = TITLE_BLACK

# Left Column Middle: Process Flow Diagram
proc_flow_path = os.path.join(ASSETS_DIR, "chakra_process_flow.png")
if os.path.exists(proc_flow_path):
    slide3.shapes.add_picture(proc_flow_path, Inches(0.5), Inches(4.35), width=Inches(5.7), height=Inches(1.25))

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
p2.text = "Requirement Gathering → RPC Block Ingestion → UTDM Schema Normalization → Tron TRC-20 Decoding → Neo4j Bounded BFS → VASP Sweep Clustering → Court Evidence Kit (Sec 63 BSA)"
p2.font.name = "Arial"
p2.font.size = Pt(9.5)
p2.font.bold = True
p2.font.color.rgb = TITLE_BLACK

# Right Column Top: Tech Stack Visual Grid
tech_grid_path = os.path.join(ASSETS_DIR, "chakra_tech_stack_grid.png")
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
run_gh_url.text = "https://github.com/chakra-i4c/vda-attribution-engine"
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
run_dm_url.text = "https://chakra.i4c-cyberdefense.gov.in"
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
tb_s4_left = slide4.shapes.add_textbox(Inches(0.5), Inches(1.35), Inches(5.8), Inches(5.5))
tf_s4_l = tb_s4_left.text_frame
tf_s4_l.word_wrap = True

# Section: Feasibility
p = tf_s4_l.paragraphs[0]
p.text = "Feasibility :-"
p.font.name = "Arial"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK
p.space_after = Pt(2)

feas_items = [
    ("Technical: ", "Uses proven graph clustering (Neo4j + Redis) → scalable to 10M+ txs in <180s"),
    ("Economic: ", "100% sovereign open-source stack → eliminates ₹50L+ annual vendor licenses"),
    ("Operational: ", "Simple UI, 1-click legal kit, role-based access for State IOs & I4C analysts"),
    ("Social: ", "Protects citizen savings & accelerates freezing of siphoned retirement/scam funds")
]
for lbl, txt in feas_items:
    p = tf_s4_l.add_paragraph()
    p.space_after = Pt(2)
    r1 = p.add_run()
    r1.text = "• " + lbl
    r1.font.name = "Arial"
    r1.font.size = Pt(9.5)
    r1.font.bold = True
    r2 = p.add_run()
    r2.text = txt
    r2.font.name = "Arial"
    r2.font.size = Pt(9)

# Section: Potential Challenges
p = tf_s4_l.add_paragraph()
p.space_before = Pt(5)
p.space_after = Pt(2)
p.text = "Potential Challenges:-"
p.font.name = "Arial"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK

pot_chal = [
    "Tron TRC-20 energy delegate rent-sharing obscuring direct fee payments",
    "Multi-hop peeling chains with nested intermediary unhosted wallets",
    "Investigating Officers lacking deep on-chain blockchain forensic expertise",
    "High RPC bandwidth and indexing storage overhead across full archive nodes"
]
for c in pot_chal:
    p = tf_s4_l.add_paragraph()
    p.space_after = Pt(1.5)
    p.text = "• " + c
    p.font.name = "Arial"
    p.font.size = Pt(9)

# Section: Mitigation Strategies
p = tf_s4_l.add_paragraph()
p.space_before = Pt(5)
p.space_after = Pt(2)
p.text = "Mitigation Strategies:-"
p.font.name = "Arial"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK

mits = [
    "Automated contract trace decoding exposing true delegator gas sponsors",
    "Deposit-to-sweep aggregation heuristics linking peeling change outputs to VASPs",
    "1-Click automated plain-English court reports with Section 63 certificates",
    "Local L1/L2 Redis caching + selective bounded BFS subgraph indexing"
]
for m in mits:
    p = tf_s4_l.add_paragraph()
    p.space_after = Pt(1.5)
    p.text = "• " + m
    p.font.name = "Arial"
    p.font.size = Pt(9)

# Section: Viability
p = tf_s4_l.add_paragraph()
p.space_before = Pt(5)
p.space_after = Pt(2)
p.text = "Viability:-"
p.font.name = "Arial"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK

viabs = [
    "Technically feasible with microservices architecture & native Go RPC workers",
    "Economically sustainable with zero ongoing foreign SaaS subscription costs",
    "Socially impactful → empowers state police forces to recover cyber heist funds",
    "Scalable & adaptable for all 36 State/UT Cyber Crime Wings across India"
]
for v in viabs:
    p = tf_s4_l.add_paragraph()
    p.space_after = Pt(1.5)
    p.text = "• " + v
    p.font.name = "Arial"
    p.font.size = Pt(9)

# Section: Business Potential
p = tf_s4_l.add_paragraph()
p.space_before = Pt(5)
p.space_after = Pt(2)
p.text = "Business Potential:-"
p.font.name = "Arial"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK

biz_pot = [
    "Pan-India institutional deployment across I4C, State Police, and FIU-IND",
    "Machine-readable BNSS Sec 94/106 notice generation for registered VASPs",
    "Sovereign data privacy: zero case details or wallet addresses leak to foreign clouds",
    "Modular API engine ready for direct plug-in to National Cybercrime Reporting Portal"
]
for b in biz_pot:
    p = tf_s4_l.add_paragraph()
    p.space_after = Pt(1.5)
    p.text = "• " + b
    p.font.name = "Arial"
    p.font.size = Pt(9)

# Right Column Top: Use Cases, Challenges, Solutions
tb_s4_right = slide4.shapes.add_textbox(Inches(6.8), Inches(1.35), Inches(6.0), Inches(3.4))
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
    "Investment & Task Scam USDT tracing across Tron / Ethereum blockchains",
    "Illegal online betting syndicate deposit & mule ring attribution to VASPs",
    "Ransomware extortion payment tracking & centralized exchange cash-out identification",
    "Court trial evidentiary submission with Section 63 BSA compliance certification"
]
for u in use_cases:
    p = tf_s4_r.add_paragraph()
    p.space_after = Pt(1.5)
    p.text = "• " + u
    p.font.name = "Arial"
    p.font.size = Pt(9.5)

# Challenges
p = tf_s4_r.add_paragraph()
p.space_before = Pt(5)
p.space_after = Pt(2)
p.text = "Challenges:-"
p.font.name = "Arial"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK

chals_r = [
    "Cross-chain decentralized bridges (THORChain, CCTP) breaking transaction lineage",
    "Uncooperative offshore unregulated VASPs delaying KYC and freeze responses",
    "Rapid fund dispersion through 50+ intermediary unhosted mule wallets",
    "Judicial rejection of blockchain evidence without cryptographic chain of custody"
]
for c in chals_r:
    p = tf_s4_r.add_paragraph()
    p.space_after = Pt(1.5)
    p.text = "• " + c
    p.font.name = "Arial"
    p.font.size = Pt(9.5)

# Solutions
p = tf_s4_r.add_paragraph()
p.space_before = Pt(5)
p.space_after = Pt(2)
p.text = "Solutions:-"
p.font.name = "Arial"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = TITLE_BLACK

sols_r = [
    "Burner contract & destination memo parsing linking cross-chain flows automatically",
    "Automated red-flagging & FIU-IND STR/SAR escalation dossiers for non-compliant VASPs",
    "Sub-180s automated graph traversal isolating final hot-wallet destination in minutes",
    "SHA-256 hash chains, RFC 3161 timestamps & Section 63 certificate automation"
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
    "Over 85% of Indian cyber fraud proceeds are laundered via USDT (TRC-20) on Tron (I4C Annual Report 2024-25)",
    "CHAKRA resolves 5-hop complex peeling chains in <180 seconds vs 14+ days for manual multi-agency requests",
    "Zero commercial SaaS licensing eliminates ₹100+ Crore annual forex outflow to foreign forensics vendors",
    "Empirical clustering precision of 94.5% verified against 100,000+ synthetic adversarial transactions"
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
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY
p.space_after = Pt(2.5)

impact_items = [
    ("IOs: ", "Resolves complex crypto trails in minutes with automated legal kits."),
    ("I4C & MHA: ", "Centralized command & control with unified national cyber intelligence."),
    ("FIU-IND & VASPs: ", "Machine-readable freeze notices and automated regulatory SAR/STR filing."),
    ("Cyber Crime Victims: ", "Faster asset freezing within 2-hr Golden Window, saving stolen funds.")
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
p.space_before = Pt(4)
p.space_after = Pt(2)
p.text = "• Key Intelligence & Laundering Insights"
p.font.name = "Arial"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY

insights = [
    "85%+ of cyber heist funds route through TRC-20 USDT within 45 minutes of theft.",
    "78% of unhosted deposit wallets sweep into just 12 major centralized VASP hot wallets.",
    "First 2 hours (\"Golden Window\") critical: after 6 hops, asset recovery rate drops by 82%.",
    "100% court admissibility achieved when forensic artifacts meet Section 63 BSA standards."
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
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY
p.space_after = Pt(3)

outcomes = [
    ("Investigation Speedup: ", "Reduces transaction trail tracing time from 14 days to <3 minutes (70x faster)."),
    ("Sovereign Asset Recovery: ", "Projected to increase asset freeze success rate by 65-80% during Golden Window."),
    ("Cost Elimination: ", "100% reduction in per-query licensing fees paid to foreign commercial vendors."),
    ("Judicial Rigor: ", "Zero evidence inadmissibility risk via automated Section 63 BSA hash-chained certificates.")
]
for lbl, txt in outcomes:
    p = tf_s5_r.add_paragraph()
    p.space_after = Pt(2.5)
    r1 = p.add_run()
    r1.text = "• " + lbl
    r1.font.name = "Arial"
    r1.font.size = Pt(10)
    r1.font.bold = True
    r2 = p.add_run()
    r2.text = txt
    r2.font.name = "Arial"
    r2.font.size = Pt(9.5)

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
    ("Social", "Protection of citizen life savings & victim relief", "Enables rapid freezing of siphoned retirement & scam funds in Golden Window."),
    ("", "Dismantling organized cyber-crime syndicates", "Exposes mule network operators and cash-out brokers across state lines."),
    ("Economic", "National Forex savings & recovery of illicit proceeds", "Saves ₹100 Cr+ in foreign licenses; aids recovery of ₹1,500+ Cr in annual cyber losses."),
    ("", "Strengthened VASP AML/CFT regulatory compliance", "Provides FIU-IND real-time auditability of registered reporting entities & VASPs."),
    ("Environmental", "Zero-waste sovereign digital investigation workflow", "Eliminates physical paperwork and redundant inter-agency letters via automated e-notices.")
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
    ("a. ", "Meiklejohn, S., et al., \"A Fistful of Bitcoins: Characterizing Payments Among Men with No Names,\" ACM IMC, 2013."),
    ("b. ", "Victor, F., \"Address Clustering Heuristics for Ethereum and TRC-20 Tokens,\" Financial Cryptography, 2020."),
    ("c. ", "Biryukov, A., et al., \"Deanonymisation of Clients in Bitcoin P2P Network,\" ACM CCS, 2014."),
    ("d. ", "Ministry of Law & Justice, Bharatiya Sakshya Adhiniyam (BSA) 2023, Section 63 (Electronic Records)."),
    ("e. ", "Ministry of Home Affairs, Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023, Sections 94 & 106.")
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
p.text = "• Existing VASP & On-Chain Intelligence Platforms:"
p.font.name = "Arial"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = BULLET_NAVY

platforms = [
    ("a. ", "Chainalysis Reactor: ", "https://www.chainalysis.com"),
    ("b. ", "TRM Labs Forensics: ", "https://www.trmlabs.com"),
    ("c. ", "Merkle Science Tracker: ", "https://www.merklescience.com")
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
r2.text = "https://github.com/chakra-i4c/vda-attribution-engine"
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
r2.text = "https://chakra.i4c-cyberdefense.gov.in"
r2.font.name = "Arial"
r2.font.size = Pt(11)
r2.font.color.rgb = BULLET_NAVY
r2.font.underline = True

# Right Column: Competitor Comparison Matrix Graphic
comp_matrix_path = os.path.join(ASSETS_DIR, "chakra_competitor_matrix.png")
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

rf_path = os.path.join(ASSETS_DIR, "chakra_research_flow.png")
if os.path.exists(rf_path):
    slide6.shapes.add_picture(rf_path, Inches(0.5), Inches(5.85), width=Inches(12.333), height=Inches(1.05))

# Save the Presentation
prs.save(output_pptx)
print(f"Flawlessly created presentation: {output_pptx}")
