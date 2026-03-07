import sys

path = r'c:\Users\hafez\MSU\Research\HafezAhmadOceanographer.github.io\index.html'
with open(path, encoding='utf-8') as f:
    content = f.read()

if 'id="methods"' in content:
    print('Methods section already present — nothing to do.')
    sys.exit(0)

# ── 1. Add Hydrological Connectivity card + close research-topics + insert Methods section ──
# Target: end of GIS card → closing of research-topics → about section start

hydrological_card = """\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-project-diagram"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Hydrological Connectivity</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Surface and subsurface hydrological connectivity in coastal-deltaic, floodplain, and wetland systems. Analysis of wetland-estuary exchange, tidal creek networks, and groundwater-surface water interactions using tracer experiments, dye studies, and hydrodynamic models.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">Surface-Subsurface Flow</span><span class="skill-tag">Wetland Connectivity</span><span class="skill-tag">Tracer Analysis</span><span class="skill-tag">Floodplain Hydrology</span></div>
\t\t\t\t\t\t\t\t\t\t</div>"""

methods_section = """
\t\t\t\t\t\t\t\t<!-- ANALYTICAL METHODS -->
\t\t\t\t\t\t\t\t<section id="methods">
\t\t\t\t\t\t\t\t\t<header class="major">
\t\t\t\t\t\t\t\t\t\t<h2><i class="fas fa-cogs" style="color:var(--ocean-teal);margin-right:0.45em;"></i>Analytical Methods</h2>
\t\t\t\t\t\t\t\t\t</header>
\t\t\t\t\t\t\t\t\t<p style="color:var(--text-medium);margin-bottom:1.5em;">Quantitative and computational methods applied across research projects in oceanography, coastal science, remote sensing, and ecology.</p>
\t\t\t\t\t\t\t\t\t<div class="activities-grid">
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-brain"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Machine Learning &amp; Deep Learning</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Supervised and unsupervised ensemble methods (Random Forest, XGBoost, Gradient Boosting, SVM) alongside deep learning architectures (CNN, LSTM, U-Net, Vision Transformers). Transfer learning and foundation model fine-tuning for Earth observation tasks including water quality retrieval, habitat mapping, and plankton classification.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">Random Forest / XGBoost</span><span class="skill-tag">CNN / LSTM</span><span class="skill-tag">U-Net / ViT</span><span class="skill-tag">Transfer Learning</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-chart-pie"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Multivariate Statistics</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>PCA / EOF decomposition for oceanographic field analysis, canonical correspondence analysis (CCA), redundancy analysis (RDA), non-metric multidimensional scaling (nMDS), PERMANOVA, cluster analysis, discriminant function analysis (DFA), and partial least squares (PLS) regression for high-dimensional environmental datasets.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">PCA / EOF</span><span class="skill-tag">CCA / RDA</span><span class="skill-tag">nMDS / PERMANOVA</span><span class="skill-tag">Cluster Analysis</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-map-marked-alt"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Spatial Analysis &amp; Geostatistics</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Ordinary and universal kriging, spatial autocorrelation metrics (Moran's I, Getis-Ord Gi*), hotspot analysis, kernel density estimation, geographically weighted regression (GWR), variogram modeling, and spatial interpolation for environmental monitoring and fisheries survey design.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">Kriging</span><span class="skill-tag">Moran's I / Getis-Ord</span><span class="skill-tag">GWR</span><span class="skill-tag">Hotspot Analysis</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-th"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Cellular Automata &amp; Land Change Modeling</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>CA-Markov, FLUS, and SLEUTH models for land-use / land-cover (LULC) transition prediction and simulation. Applied to urban growth, coastal delta retreat, mangrove loss, and wetland conversion modeling driven by remote sensing time-series inputs and socio-economic drivers.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">CA-Markov</span><span class="skill-tag">FLUS</span><span class="skill-tag">LULC Transition</span><span class="skill-tag">Urban Growth Simulation</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-wave-square"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Time Series &amp; Spectral Analysis</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Fast Fourier Transform (FFT), continuous wavelet transform (CWT), empirical mode decomposition (EMD / HHT), seasonal-trend decomposition (STL), Mann-Kendall trend detection, harmonic regression for phenological studies, and tidal constituent analysis (t_tide, UTide) for water-level records.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">Wavelet / EMD</span><span class="skill-tag">Mann-Kendall</span><span class="skill-tag">FFT</span><span class="skill-tag">Tidal Analysis</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-wind"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Hydrodynamic Numerical Methods</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Finite-volume and finite-element discretization schemes for coastal ocean models. Unstructured mesh generation (SMS, GMSH), open boundary condition specification, model data assimilation (ensemble Kalman filter, optimal interpolation), Lagrangian particle tracking for larval dispersal, and wave-current coupling (FVCOM-SWAVE, ROMS-SWAN).</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">Finite Volume / FEM</span><span class="skill-tag">Data Assimilation (EnKF)</span><span class="skill-tag">Lagrangian Tracking</span><span class="skill-tag">Wave-Current Coupling</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-satellite-dish"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Remote Sensing Image Analysis</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Atmospheric correction (6S, ACOLITE, SeaDAS, iCOR), supervised and unsupervised image classification, spectral mixture analysis, continuous change detection (CCDC, LandTrendr), SAR backscatter processing (Sentinel-1 / SNAP), pan-sharpening, object-based image analysis (OBIA), and ocean color algorithm development and validation.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">Atmospheric Correction</span><span class="skill-tag">OBIA / Classification</span><span class="skill-tag">CCDC / LandTrendr</span><span class="skill-tag">SAR Processing</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-leaf"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Ecological &amp; Community Analysis</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>PRIMER-e multivariate community ecology workflows (nMDS, SIMPER, ANOSIM), diversity indices (Shannon, Simpson, Margalef), MaxEnt and Boosted Regression Tree (BRT) species distribution modeling, Ecopath with Ecosim (EwE) food-web analysis, hierarchical occupancy models, and trait-based community assembly analysis.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">nMDS / SIMPER</span><span class="skill-tag">MaxEnt / BRT</span><span class="skill-tag">Ecopath / EwE</span><span class="skill-tag">Occupancy Modeling</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t</section>
"""

# ── find the exact marker: end of GIS card + close grid + close research-topics section ──
gis_tags_line = '\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">Spatial Analysis</span><span class="skill-tag">Change Detection</span><span class="skill-tag">Geostatistics</span></div>'
close_grid = '\n\t\t\t\t\t\t\t\t\t\t</div>'
close_research = '\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t</section>'

old_gis_end = gis_tags_line + close_grid + close_research

if old_gis_end not in content:
    # Try with slightly different indentation
    import re
    m = re.search(r'<span class="skill-tag">Geostatistics</span></div>\s*\n\s*</div>\s*\n\s*</div>\s*\n\s*</section>', content)
    if m:
        print(f"Found GIS section end at pos {m.start()}")
        print(repr(content[m.start()-20:m.end()+20]))
    else:
        print('ERROR: GIS card end not found')
    sys.exit(1)

new_gis_end = gis_tags_line + close_grid + '\n' + hydrological_card + close_research + methods_section

content = content.replace(old_gis_end, new_gis_end, 1)

print(f'Research Topics + Methods insertion done.')

# ── verify ────────────────────────────────────────────────────────────────────
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

checks = ['id="methods"', 'Hydrological Connectivity', 'CA-Markov', 'Moran\'s I', 'Mann-Kendall',
          'Cellular Automata', 'PERMANOVA', 'Lagrangian Tracking', 'CCDC / LandTrendr']
ok, fail = [], []
for c in checks:
    (ok if c in content else fail).append(c)
print(f'Content checks PASS: {len(ok)}/{len(checks)}')
if fail:
    print('MISSING:', fail)
print(f'File size: {len(content):,} chars')
