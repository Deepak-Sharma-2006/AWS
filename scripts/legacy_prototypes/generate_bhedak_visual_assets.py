import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs('specs/presentations/assets', exist_ok=True)
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(14, 12), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')
    
    # Title
    ax.text(0.5, 0.97, 'BHEDAK – Autonomous Dark Web Threat Actor De-Anonymization Architecture', 
            ha='center', va='center', fontsize=17, fontweight='bold', color='#0F172A')
    
    # 4 User Roles at top
    users = [
        ('NTRO Cyber Intel Analysts', '#0284C7'),
        ('IB / Central LEAs', '#1E40AF'),
        ('CERT-In Responders', '#0D9488'),
        ('State Cyber Crime Wings', '#334155')
    ]
    u_xs = [0.12, 0.37, 0.63, 0.88]
    for (name, col), x in zip(users, u_xs):
        box = patches.FancyBboxPatch((x - 0.11, 0.88), 0.22, 0.05,
                                     boxstyle="round,pad=0.015,rounding_size=0.02",
                                     fc=col, ec='none')
        ax.add_patch(box)
        ax.text(x, 0.905, name, ha='center', va='center', color='white', fontsize=11, fontweight='bold')
    
    # Connector from users to Central Users Pill
    for x in u_xs:
        ax.plot([x, x, 0.5], [0.88, 0.85, 0.85], color='#94A3B8', lw=1.5)
    ax.plot([0.5, 0.5], [0.85, 0.82], color='#94A3B8', lw=1.5)
    
    # STAKEHOLDERS Pill
    box_stakeholders = patches.FancyBboxPatch((0.33, 0.77), 0.34, 0.05,
                                              boxstyle="round,pad=0.015,rounding_size=0.025",
                                              fc='#3B82F6', ec='none')
    ax.add_patch(box_stakeholders)
    ax.text(0.5, 0.795, 'THREAT INTEL ANALYSTS & INVESTIGATORS', ha='center', va='center', color='white', fontsize=11.5, fontweight='bold')
    
    # Split from Stakeholders to UI Layer and Backend Services
    ax.plot([0.5, 0.28, 0.28], [0.77, 0.74, 0.71], color='#94A3B8', lw=1.5)
    ax.plot([0.5, 0.72, 0.72], [0.77, 0.74, 0.71], color='#94A3B8', lw=1.5)
    
    # UI Layer Pill (Left)
    box_ui = patches.FancyBboxPatch((0.13, 0.66), 0.30, 0.05,
                                    boxstyle="round,pad=0.015,rounding_size=0.025",
                                    fc='#EA580C', ec='none')
    ax.add_patch(box_ui)
    ax.text(0.28, 0.685, 'Forensic UI Layer (React Flow + Cytoscape)', ha='center', va='center', color='white', fontsize=11.5, fontweight='bold')
    
    # Backend Services Pill (Right)
    box_be = patches.FancyBboxPatch((0.57, 0.66), 0.30, 0.05,
                                    boxstyle="round,pad=0.015,rounding_size=0.025",
                                    fc='#DC2626', ec='none')
    ax.add_patch(box_be)
    ax.text(0.72, 0.685, 'Core Microservices (Go + Python Celery)', ha='center', va='center', color='white', fontsize=11.5, fontweight='bold')
    
    # Sub-headers under UI Layer
    box_web = patches.FancyBboxPatch((0.02, 0.59), 0.24, 0.04,
                                     boxstyle="round,pad=0.01,rounding_size=0.015",
                                     fc='#334155', ec='none')
    ax.add_patch(box_web)
    ax.text(0.14, 0.61, 'Investigator Visual Canvas', ha='center', va='center', color='white', fontsize=10, fontweight='bold')
    
    box_term = patches.FancyBboxPatch((0.28, 0.59), 0.24, 0.04,
                                      boxstyle="round,pad=0.01,rounding_size=0.015",
                                      fc='#0D9488', ec='none')
    ax.add_patch(box_term)
    ax.text(0.40, 0.61, 'Legal & Export Terminal', ha='center', va='center', color='white', fontsize=10, fontweight='bold')
    
    web_feats = [
        'Multi-Market Entity Graph',
        'Cross-Platform Persona Pivot',
        'JARM & Favicon Correlation',
        'Diurnal Sleep Cycle Visualizer',
        'Stylometric Similarity Matrix',
        '1-Click Section 63 BSA Dossier'
    ]
    term_feats = [
        'Automated BNSS Sec 94 Notice',
        'I4C Samanvaya MIS Sync',
        'CERT-In STIX 2.1 Exporter',
        'RFC 3161 Court Hash Chain',
        'FIU-IND FINGate STR Bridge',
        'Deconfliction Vault & Audit Log'
    ]
    
    y_start = 0.52
    for i, (wf, tf) in enumerate(zip(web_feats, term_feats)):
        y = y_start - i * 0.075
        w_box = patches.FancyBboxPatch((0.02, y), 0.24, 0.055,
                                       boxstyle="round,pad=0.01,rounding_size=0.015",
                                       fc='#0F4C81', ec='none')
        ax.add_patch(w_box)
        ax.text(0.14, y + 0.0275, wf, ha='center', va='center', color='white', fontsize=9.2, fontweight='bold')
        
        t_box = patches.FancyBboxPatch((0.28, y), 0.24, 0.055,
                                       boxstyle="round,pad=0.01,rounding_size=0.015",
                                       fc='#1E3A8A', ec='none')
        ax.add_patch(t_box)
        ax.text(0.40, y + 0.0275, tf, ha='center', va='center', color='white', fontsize=9.2, fontweight='bold')
    
    be_services = [
        'Tor Crawl Pool (8 SOCKS5h)',
        'Engine 0: OSINT & Handle Miner',
        'Engine 1: Tor Misconfig Prober',
        'Engine 2: Crypto & PGP Graph',
        'Engine 3: Siamese RoBERTa NLP'
    ]
    y_be_start = 0.58
    for i, bs in enumerate(be_services):
        y = y_be_start - i * 0.065
        b_box = patches.FancyBboxPatch((0.57, y), 0.38, 0.048,
                                       boxstyle="round,pad=0.01,rounding_size=0.015",
                                       fc='#0284C7', ec='none')
        ax.add_patch(b_box)
        ax.text(0.76, y + 0.024, bs, ha='center', va='center', color='white', fontsize=10, fontweight='bold')
        ax.plot([0.55, 0.57], [y + 0.024, y + 0.024], color='#CBD5E1', lw=1.2)
    
    box_ai = patches.FancyBboxPatch((0.57, 0.21), 0.38, 0.05,
                                    boxstyle="round,pad=0.015,rounding_size=0.025",
                                    fc='#D97706', ec='none')
    ax.add_patch(box_ai)
    ax.text(0.76, 0.235, 'Engine 4: Asymmetric Confidence Scorer', ha='center', va='center', color='white', fontsize=11, fontweight='bold')
    ax.plot([0.72, 0.72], [0.66, 0.26], color='#F59E0B', lw=2, linestyle=':')
    
    ai_sub = [
        'Deterministic PGP / Wallet Linkage (1.0)',
        'Server mod_status Origin Bind (0.90)',
        'AI Stylometry Hard Cap (0.65 Maximum)',
        'Section 63 BSA Dual-Signature Certification'
    ]
    y_ai_start = 0.14
    for i, ais in enumerate(ai_sub):
        y = y_ai_start - i * 0.05
        ai_box = patches.FancyBboxPatch((0.57, y), 0.38, 0.04,
                                        boxstyle="round,pad=0.01,rounding_size=0.012",
                                        fc='#0F172A', ec='none')
        ax.add_patch(ai_box)
        ax.text(0.76, y + 0.02, ais, ha='center', va='center', color='white', fontsize=9.2, fontweight='bold')
        ax.plot([0.55, 0.57], [y + 0.02, y + 0.02], color='#CBD5E1', lw=1.2)
        
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.08, 1.0)
    plt.tight_layout()
    out_path = 'specs/presentations/assets/bhedak_architecture_diagram.png'
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated {out_path}")

def create_process_flow():
    fig, ax = plt.subplots(figsize=(12, 3.0), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')
    
    stages = [
        ('1. Tor Ingestion\n(Markets/Forums)', '#2563EB', 'TOR POOL'),
        ('2. Infra & OSINT\nProbing (JARM/EXIF)', '#0D9488', 'PROBING'),
        ('3. Neo4j Entity\nLinking (PGP/Crypto)', '#7C3AED', 'GRAPH DB'),
        ('4. AI Stylometry &\nDiurnal Profiling', '#D97706', 'AI NLP'),
        ('5. Court Evidence Kit\n(Section 63 BSA)', '#059669', 'LEGAL')
    ]
    
    n = len(stages)
    w = 0.14
    h = 0.50
    y_box = 0.38
    xs = [0.08 + i * 0.195 for i in range(n)]
    
    for i, ((title, col, sym), x) in enumerate(zip(stages, xs)):
        box = patches.FancyBboxPatch((x - w/2, y_box), w, h,
                                     boxstyle="round,pad=0.015,rounding_size=0.025",
                                     fc=col, ec='none')
        ax.add_patch(box)
        
        # White badge inside
        tag_w, tag_h = 0.10, 0.12
        tag = patches.FancyBboxPatch((x - tag_w/2, y_box + h/2 - tag_h/2 + 0.02), tag_w, tag_h,
                                     boxstyle="round,pad=0.005,rounding_size=0.02",
                                     fc='white', ec='none')
        ax.add_patch(tag)
        
        ax.text(x, y_box + h/2 + 0.02, sym, ha='center', va='center', 
                color=col, fontsize=8.8, fontweight='bold')
        
        ax.text(x, y_box - 0.10, title, ha='center', va='top', 
                color='#0F172A', fontsize=10, fontweight='bold', multialignment='center')
        
        if i < n - 1:
            next_x = xs[i+1]
            ax.annotate('', xy=(next_x - w/2 - 0.015, y_box + h/2), 
                        xytext=(x + w/2 + 0.015, y_box + h/2),
                        arrowprops=dict(arrowstyle="-|>", color='#64748B', lw=2.5, mutation_scale=16))
            
    ax.set_xlim(0, 0.98)
    ax.set_ylim(0.02, 0.96)
    plt.tight_layout()
    out_path = 'specs/presentations/assets/bhedak_process_flow.png'
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated {out_path}")

def create_tech_stack_grid():
    fig, ax = plt.subplots(figsize=(14, 9), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')
    
    ax.text(0.5, 0.96, 'TECHNOLOGIES TO BE USED:', ha='center', va='center', 
            fontsize=18, fontweight='bold', color='#1E3A8A')
    
    columns = [
        ('INGESTION', '#1E40AF', [
            ('tor Daemon Pool', '#38BDF8'),
            ('Stem Python API', '#0F172A'),
            ('Playwright Stealth', '#3B82F6'),
            ('Telethon Scraper', '#0D9488')
        ]),
        ('BACKEND', '#059669', [
            ('Go (Golang)', '#00ADD8'),
            ('Python Celery', '#3776AB'),
            ('FastAPI Service', '#059669'),
            ('Redis Streams', '#DC2626')
        ]),
        ('DATABASES', '#D97706', [
            ('Neo4j 5 Graph DB', '#008CC1'),
            ('Elasticsearch 8', '#336791'),
            ('TimescaleDB', '#FDB515'),
            ('PostgreSQL 16', '#336791')
        ]),
        ('AI & STYLOMETRY', '#7C3AED', [
            ('RoBERTa Triplet', '#EE4C2C'),
            ('Writeprints NLP', '#C23631'),
            ('BERTopic HDBSCAN', '#4F46E5'),
            ('DistilGPT Perplexity', '#0F172A')
        ]),
        ('SECURITY & LEGAL', '#334155', [
            ('OpenSSL SHA-256', '#FF9900'),
            ('RFC 3161 TSP', '#059669'),
            ('ReportLab Engine', '#2496ED'),
            ('Air-Gapped Linux', '#E95420')
        ]),
        ('INTEGRATIONS', '#0F766E', [
            ('I4C Samanvaya', '#1E3A8A'),
            ('CERT-In STIX 2.1', '#0D9488'),
            ('FIU-IND FINGate', '#4338CA'),
            ('BNSS Sec 94 Notice', '#B45309')
        ])
    ]
    
    num_cols = len(columns)
    col_width = 0.145
    col_spacing = 0.162
    left_margin = 0.025
    
    for c_idx, (col_name, header_col, items) in enumerate(columns):
        cx = left_margin + c_idx * col_spacing
        
        hdr_box = patches.FancyBboxPatch((cx, 0.85), col_width, 0.055,
                                         boxstyle="round,pad=0.01,rounding_size=0.015",
                                         fc=header_col, ec='none')
        ax.add_patch(hdr_box)
        ax.text(cx + col_width/2, 0.877, col_name, ha='center', va='center', 
                color='white', fontsize=10, fontweight='bold')
        
        if c_idx < num_cols - 1:
            div_x = cx + col_width + 0.008
            ax.plot([div_x, div_x], [0.15, 0.90], color='#E2E8F0', lw=1.2)
            
        y_item = 0.76
        for it_name, it_col in items:
            it_box = patches.FancyBboxPatch((cx, y_item), col_width, 0.095,
                                            boxstyle="round,pad=0.01,rounding_size=0.015",
                                            fc='#F8FAFC', ec='#CBD5E1', lw=1.2)
            ax.add_patch(it_box)
            
            tag_badge = patches.FancyBboxPatch((cx + 0.01, y_item + 0.052), col_width - 0.02, 0.028,
                                              boxstyle="round,pad=0.005,rounding_size=0.008",
                                              fc=it_col, ec='none')
            ax.add_patch(tag_badge)
            
            ax.text(cx + col_width/2, y_item + 0.066, it_name.split(' ')[0], 
                    ha='center', va='center', color='white', fontsize=8.5, fontweight='bold')
            
            ax.text(cx + col_width/2, y_item + 0.025, it_name, 
                    ha='center', va='center', color='#0F172A', fontsize=9.5, fontweight='bold')
            
            y_item -= 0.155
            
    ax.set_xlim(0, 1.0)
    ax.set_ylim(0.08, 1.0)
    plt.tight_layout()
    out_path = 'specs/presentations/assets/bhedak_tech_stack_grid.png'
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated {out_path}")

def create_research_flow():
    fig, ax = plt.subplots(figsize=(16, 2.2), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')
    
    stages = [
        '1. Darknet Threat\nLandscape & NTRO PS',
        '2. Tor v3 Protocol\n& OPSEC Audit',
        '3. 5-Engine Pipeline\n& Schema Design',
        '4. AI Stylometry\n& RoBERTa Tuning',
        '5. Adversarial Red/\nBlue Fuzzing Loop',
        '6. Core System TDD\n& Neo4j Linking',
        '7. BSA Section 63\nCourt Benchmarking',
        '8. BHEDAK Sovereign\nNTRO Deployment'
    ]
    
    cols = ['#2563EB', '#3B82F6', '#6366F1', '#4F46E5', '#0284C7', '#0D9488', '#059669', '#16A34A']
    
    n = len(stages)
    w = 0.096
    h = 0.58
    y_box = 0.22
    xs = [0.048 + i * 0.121 for i in range(n)]
    
    for i, (title, col, x) in enumerate(zip(stages, cols, xs)):
        box = patches.FancyBboxPatch((x - w/2, y_box), w, h,
                                     boxstyle="round,pad=0.008,rounding_size=0.018",
                                     fc=col, ec='none')
        ax.add_patch(box)
        
        ax.text(x, y_box + h/2, title, ha='center', va='center', 
                color='white', fontsize=8.2, fontweight='bold', multialignment='center')
        
        if i < n - 1:
            next_x = xs[i+1]
            ax.annotate('', xy=(next_x - w/2 - 0.008, y_box + h/2), 
                        xytext=(x + w/2 + 0.008, y_box + h/2),
                        arrowprops=dict(arrowstyle="-|>", color='#EA580C', lw=2.2, mutation_scale=13))
            
    ax.set_xlim(0, 0.98)
    ax.set_ylim(0.05, 0.95)
    plt.tight_layout()
    out_path = 'specs/presentations/assets/bhedak_research_flow.png'
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated {out_path}")

def create_competitor_matrix_graphic():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')
    
    headers = ['De-Anonymization Capability / Feature', 'BHEDAK (NTRO)', 'Palantir Gotham', 'DarkOwl Vision', 'Chainalysis']
    cols_x = [0.03, 0.46, 0.63, 0.77, 0.91]
    
    ax.text(cols_x[0], 0.93, headers[0], ha='left', va='center', fontsize=12, fontweight='bold', color='#0F172A')
    for h, x in zip(headers[1:], cols_x[1:]):
        ax.text(x, 0.93, h, ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')
    
    ax.plot([0.02, 0.98], [0.89, 0.89], color='#CBD5E1', lw=1.5)
    
    rows = [
        ('1. Tor Misconfig & JARM Favicon Fingerprinting', True, False, False, False),
        ('2. AI Stylometry Profiling (Writeprints + RoBERTa)', True, False, False, False),
        ('3. Multi-Market PGP & BTC Common-Input Graph', True, True, False, True),
        ('4. Asymmetric Scoring (0.65 AI Cap - No False Match)', True, False, False, False),
        ('5. Section 63 BSA 2023 Evidentiary Dual-Cert', True, False, False, False),
        ('6. Automated BNSS Sec 94 Notice Generation', True, False, False, False),
        ('7. 100% Sovereign On-Premise (Zero Forex Outflow)', True, False, False, False),
    ]
    
    y_start = 0.82
    for r_idx, (feat, c1, c2, c3, c4) in enumerate(rows):
        y = y_start - r_idx * 0.115
        
        if r_idx % 2 == 1:
            row_bg = patches.Rectangle((0.02, y - 0.045), 0.96, 0.09, fc='#F8FAFC', ec='none')
            ax.add_patch(row_bg)
            
        ax.text(cols_x[0], y, feat, ha='left', va='center', fontsize=10.5, fontweight='bold', color='#1E293B')
        
        for val, x in zip([c1, c2, c3, c4], cols_x[1:]):
            bw, bh = 0.042, 0.054
            if val:
                # Green Check Badge
                box = patches.FancyBboxPatch((x - bw/2, y - bh/2), bw, bh,
                                             boxstyle="round,pad=0.005,rounding_size=0.01",
                                             fc='#10B981', ec='none')
                ax.add_patch(box)
                chk_x = [x - 0.012, x - 0.003, x + 0.012]
                chk_y = [y, y - 0.012, y + 0.013]
                ax.plot(chk_x, chk_y, color='white', lw=3.0, solid_capstyle='round', solid_joinstyle='round')
            else:
                # Red Cross Badge
                box = patches.FancyBboxPatch((x - bw/2, y - bh/2), bw, bh,
                                             boxstyle="round,pad=0.005,rounding_size=0.01",
                                             fc='#EF4444', ec='none')
                ax.add_patch(box)
                d = 0.010
                ax.plot([x - d, x + d], [y - d, y + d], color='white', lw=3.0, solid_capstyle='round')
                ax.plot([x - d, x + d], [y + d, y - d], color='white', lw=3.0, solid_capstyle='round')
                
        ax.plot([0.02, 0.98], [y - 0.05, y - 0.05], color='#F1F5F9', lw=1.0)
        
    ax.set_xlim(0, 1.0)
    ax.set_ylim(0.02, 1.0)
    plt.tight_layout()
    out_path = 'specs/presentations/assets/bhedak_competitor_matrix.png'
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated {out_path}")

if __name__ == '__main__':
    create_architecture_diagram()
    create_process_flow()
    create_tech_stack_grid()
    create_research_flow()
    create_competitor_matrix_graphic()
