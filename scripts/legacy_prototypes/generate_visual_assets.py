import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import numpy as np

os.makedirs('specs/presentations/assets', exist_ok=True)
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(14, 12), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')
    
    # Title
    ax.text(0.5, 0.97, 'CHAKRA – Sovereign VDA Attribution & Forensics Architecture', 
            ha='center', va='center', fontsize=18, fontweight='bold', color='#0F172A')
    
    # 4 User Roles at top
    users = [
        ('I4C Central Analysts', '#0284C7'),
        ('State Police IOs', '#1E40AF'),
        ('FIU-IND Investigators', '#0D9488'),
        ('Cyber Crime Cells', '#334155')
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
    box_stakeholders = patches.FancyBboxPatch((0.35, 0.77), 0.3, 0.05,
                                              boxstyle="round,pad=0.015,rounding_size=0.025",
                                              fc='#3B82F6', ec='none')
    ax.add_patch(box_stakeholders)
    ax.text(0.5, 0.795, 'INVESTIGATING OFFICERS & ANALYSTS', ha='center', va='center', color='white', fontsize=12, fontweight='bold')
    
    # Split from Stakeholders to UI Layer and Backend Services
    ax.plot([0.5, 0.28, 0.28], [0.77, 0.74, 0.71], color='#94A3B8', lw=1.5)
    ax.plot([0.5, 0.72, 0.72], [0.77, 0.74, 0.71], color='#94A3B8', lw=1.5)
    
    # UI Layer Pill (Left)
    box_ui = patches.FancyBboxPatch((0.13, 0.66), 0.30, 0.05,
                                    boxstyle="round,pad=0.015,rounding_size=0.025",
                                    fc='#EA580C', ec='none')
    ax.add_patch(box_ui)
    ax.text(0.28, 0.685, 'Forensic UI Layer (React + WebGL)', ha='center', va='center', color='white', fontsize=12, fontweight='bold')
    
    # Backend Services Pill (Right)
    box_be = patches.FancyBboxPatch((0.57, 0.66), 0.30, 0.05,
                                    boxstyle="round,pad=0.015,rounding_size=0.025",
                                    fc='#DC2626', ec='none')
    ax.add_patch(box_be)
    ax.text(0.72, 0.685, 'Core Forensic Microservices (Go + Python)', ha='center', va='center', color='white', fontsize=12, fontweight='bold')
    
    # Sub-headers under UI Layer
    box_web = patches.FancyBboxPatch((0.02, 0.59), 0.24, 0.04,
                                     boxstyle="round,pad=0.01,rounding_size=0.015",
                                     fc='#334155', ec='none')
    ax.add_patch(box_web)
    ax.text(0.14, 0.61, 'Investigator Web Portal', ha='center', va='center', color='white', fontsize=10, fontweight='bold')
    
    box_term = patches.FancyBboxPatch((0.28, 0.59), 0.24, 0.04,
                                      boxstyle="round,pad=0.01,rounding_size=0.015",
                                      fc='#0D9488', ec='none')
    ax.add_patch(box_term)
    ax.text(0.40, 0.61, 'Tactical Field Terminal', ha='center', va='center', color='white', fontsize=10, fontweight='bold')
    
    web_feats = [
        'Multi-Chain Search Portal',
        'Interactive Peeling Visualizer',
        'Hot-Wallet Cluster Graph',
        'Tron Energy Fee Analyzer',
        'Bridge Hop Correlator',
        '1-Click BSA 2023 Dossier'
    ]
    term_feats = [
        'Automated Freeze Notice Gen',
        'NCRP Live Complaint Ingest',
        'FIU-IND STR/SAR Exporter',
        'Court Hash Chain Auditor',
        'VASP Entity Directory',
        'Audit Log & Chain of Custody'
    ]
    
    y_start = 0.52
    for i, (wf, tf) in enumerate(zip(web_feats, term_feats)):
        y = y_start - i * 0.075
        w_box = patches.FancyBboxPatch((0.02, y), 0.24, 0.055,
                                       boxstyle="round,pad=0.01,rounding_size=0.015",
                                       fc='#0F4C81', ec='none')
        ax.add_patch(w_box)
        ax.text(0.14, y + 0.0275, wf, ha='center', va='center', color='white', fontsize=9.5, fontweight='bold')
        
        t_box = patches.FancyBboxPatch((0.28, y), 0.24, 0.055,
                                       boxstyle="round,pad=0.01,rounding_size=0.015",
                                       fc='#1E3A8A', ec='none')
        ax.add_patch(t_box)
        ax.text(0.40, y + 0.0275, tf, ha='center', va='center', color='white', fontsize=9.5, fontweight='bold')
    
    be_services = [
        'RPC Multi-Chain Ingestion',
        'UTDM Schema Normalizer',
        'Tron TRC-20 Energy Decoder',
        'Deposit-Sweep Cluster Engine',
        'Cross-Chain Memo Parser'
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
    ax.text(0.76, 0.235, 'AI & Graph Analytics Service (Neo4j + PyTorch)', ha='center', va='center', color='white', fontsize=11, fontweight='bold')
    ax.plot([0.72, 0.72], [0.66, 0.26], color='#F59E0B', lw=2, linestyle=':')
    
    ai_sub = [
        'Neo4j Bounded Graph Traversal (<180s)',
        'Peeling Chain Pattern Matcher (Volume Entropy)',
        'VASP Hot-Wallet Classifier (Shared Deposit Sweep)',
        'Section 63 BSA 2023 Evidentiary Hash Anchor'
    ]
    y_ai_start = 0.14
    for i, ais in enumerate(ai_sub):
        y = y_ai_start - i * 0.05
        ai_box = patches.FancyBboxPatch((0.57, y), 0.38, 0.04,
                                        boxstyle="round,pad=0.01,rounding_size=0.012",
                                        fc='#0F172A', ec='none')
        ax.add_patch(ai_box)
        ax.text(0.76, y + 0.02, ais, ha='center', va='center', color='white', fontsize=9.5, fontweight='bold')
        ax.plot([0.55, 0.57], [y + 0.02, y + 0.02], color='#CBD5E1', lw=1.2)
        
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.08, 1.0)
    plt.tight_layout()
    out_path = 'specs/presentations/assets/chakra_architecture_diagram.png'
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated {out_path}")

def create_process_flow():
    # Crisp, well-proportioned 5-box process flow
    fig, ax = plt.subplots(figsize=(12, 3.0), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')
    
    stages = [
        ('1. Data Ingestion\n(RPCs & NCRP)', '#2563EB', 'INGEST'),
        ('2. UTDM Schema\nNormalization', '#0D9488', 'UTDM'),
        ('3. Tron Decoding &\nNeo4j Bounded BFS', '#7C3AED', 'GRAPH'),
        ('4. VASP Attribution &\nSweep Clustering', '#D97706', 'VASP'),
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
        tag_w, tag_h = 0.09, 0.12
        tag = patches.FancyBboxPatch((x - tag_w/2, y_box + h/2 - tag_h/2 + 0.02), tag_w, tag_h,
                                     boxstyle="round,pad=0.005,rounding_size=0.02",
                                     fc='white', ec='none')
        ax.add_patch(tag)
        
        ax.text(x, y_box + h/2 + 0.02, sym, ha='center', va='center', 
                color=col, fontsize=9.5, fontweight='bold')
        
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
    out_path = 'specs/presentations/assets/chakra_process_flow.png'
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
        ('FRONTEND', '#1E40AF', [
            ('React.js', '#38BDF8'),
            ('Next.js', '#0F172A'),
            ('TypeScript', '#3B82F6'),
            ('Cytoscape.js', '#0D9488')
        ]),
        ('BACKEND', '#059669', [
            ('Go (Golang)', '#00ADD8'),
            ('Python', '#3776AB'),
            ('FastAPI', '#059669'),
            ('gRPC Services', '#244c5a')
        ]),
        ('DATABASES', '#D97706', [
            ('Neo4j Graph DB', '#008CC1'),
            ('PostgreSQL', '#336791'),
            ('TimescaleDB', '#FDB515'),
            ('Redis Cache', '#DC2626')
        ]),
        ('ANALYTICS & LEGAL', '#7C3AED', [
            ('TronGrid Nodes', '#C23631'),
            ('PyTorch / ML', '#EE4C2C'),
            ('SHA-256 Hash', '#0F172A'),
            ('RFC 3161 TSP', '#059669')
        ]),
        ('SOVEREIGN INFRA', '#334155', [
            ('NIC MeghRaj', '#FF9900'),
            ('Docker Engine', '#2496ED'),
            ('Kubernetes', '#326CE5'),
            ('Air-Gapped Linux', '#E95420')
        ]),
        ('INTEGRATIONS', '#0F766E', [
            ('I4C NCRP Portal', '#1E3A8A'),
            ('FIU-IND Astraea', '#0D9488'),
            ('VASP KYC API', '#4338CA'),
            ('BNSS Sec 94/106', '#B45309')
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
    out_path = 'specs/presentations/assets/chakra_tech_stack_grid.png'
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated {out_path}")

def create_research_flow():
    fig, ax = plt.subplots(figsize=(16, 2.2), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')
    
    stages = [
        '1. Threat Landscape\n& Problem ID',
        '2. On-Chain Ledger\n& Literature Audit',
        '3. Gap Analysis\n(Tron & BSA 2023)',
        '4. Architectural\nFormulation (UTDM)',
        '5. Adversarial Red/\nBlue Validation',
        '6. System Core\nImplementation',
        '7. Evidentiary\nBenchmarking',
        '8. CHAKRA Sovereign\nDeployment'
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
    out_path = 'specs/presentations/assets/chakra_research_flow.png'
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated {out_path}")

def create_competitor_matrix_graphic():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')
    
    headers = ['Forensic Capability / Feature', 'CHAKRA (I4C)', 'Chainalysis', 'TRM Labs', 'Merkle Science']
    cols_x = [0.03, 0.46, 0.63, 0.77, 0.91]
    
    ax.text(cols_x[0], 0.93, headers[0], ha='left', va='center', fontsize=12, fontweight='bold', color='#0F172A')
    for h, x in zip(headers[1:], cols_x[1:]):
        ax.text(x, 0.93, h, ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')
    
    ax.plot([0.02, 0.98], [0.89, 0.89], color='#CBD5E1', lw=1.5)
    
    rows = [
        ('1. Tron TRC-20 Energy Model Decoding', True, False, False, False),
        ('2. Deposit-to-Sweep Clustering Heuristics', True, True, True, True),
        ('3. Section 63 BSA 2023 Evidentiary Hash Chain', True, False, False, False),
        ('4. Sub-180s Bounded Graph Traversal (<3 min)', True, True, False, False),
        ('5. Sovereign Air-Gapped On-Premise (No Data Leak)', True, False, False, False),
        ('6. Automated BNSS Sec 94/106 Notice Engine', True, False, False, False),
        ('7. Zero Forex License Cost (100% Sovereign Open)', True, False, False, False),
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
                # Draw vector checkmark
                chk_x = [x - 0.012, x - 0.003, x + 0.012]
                chk_y = [y, y - 0.012, y + 0.013]
                ax.plot(chk_x, chk_y, color='white', lw=3.0, solid_capstyle='round', solid_joinstyle='round')
            else:
                # Red Cross Badge
                box = patches.FancyBboxPatch((x - bw/2, y - bh/2), bw, bh,
                                             boxstyle="round,pad=0.005,rounding_size=0.01",
                                             fc='#EF4444', ec='none')
                ax.add_patch(box)
                # Draw vector cross
                d = 0.010
                ax.plot([x - d, x + d], [y - d, y + d], color='white', lw=3.0, solid_capstyle='round')
                ax.plot([x - d, x + d], [y + d, y - d], color='white', lw=3.0, solid_capstyle='round')
                
        ax.plot([0.02, 0.98], [y - 0.05, y - 0.05], color='#F1F5F9', lw=1.0)
        
    ax.set_xlim(0, 1.0)
    ax.set_ylim(0.02, 1.0)
    plt.tight_layout()
    out_path = 'specs/presentations/assets/chakra_competitor_matrix.png'
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated {out_path}")

if __name__ == '__main__':
    create_architecture_diagram()
    create_process_flow()
    create_tech_stack_grid()
    create_research_flow()
    create_competitor_matrix_graphic()
