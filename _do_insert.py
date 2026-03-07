import sys, os

path = r'c:\Users\hafez\MSU\Research\HafezAhmadOceanographer.github.io\index.html'

# ── read the file ────────────────────────────────────────────────────────────
with open(path, encoding='utf-8') as f:
    content = f.read()

# ── verify we haven't already inserted ───────────────────────────────────────
if 'id="skills"' in content:
    print('Sections already present — nothing to do.')
    sys.exit(0)

# ── exact marker (confirmed from diagnostic) ─────────────────────────────────
old_marker = (
    '\t\t\t\t\t\t\t\t</section>\n\n'
    '\t\t\t\t\t\t\t<!-- Section -->\n'
    '\t\t\t\t\t\t\t\t\t<section id="about">'
)

if old_marker not in content:
    print('ERROR: marker not found'); sys.exit(1)

# ── 4 new sections ────────────────────────────────────────────────────────────
new_sections = """\n
\t\t\t\t\t\t\t\t<!-- TECHNICAL SKILLS -->
\t\t\t\t\t\t\t\t<section id="skills">
\t\t\t\t\t\t\t\t\t<header class="major">
\t\t\t\t\t\t\t\t\t\t<h2><i class="fas fa-laptop-code" style="color:var(--ocean-teal);margin-right:0.45em;"></i>Technical Skills</h2>
\t\t\t\t\t\t\t\t\t</header>

\t\t\t\t\t\t\t\t\t<h3 style="color:var(--ocean-teal);border-bottom:1px solid rgba(0,206,209,0.2);padding-bottom:0.4rem;margin-bottom:1rem;"><i class="fas fa-code" style="margin-right:0.4em;"></i>Programming &amp; Scripting</h3>
\t\t\t\t\t\t\t\t\t<div class="activities-grid">
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fab fa-python"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Python</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Primary language for data science, ML, ocean modeling post-processing, and automation. Expert-level proficiency across scientific computing and visualization workflows.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.7rem;">
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">NumPy / SciPy</span><span class="skill-tag">Pandas / xarray</span><span class="skill-tag">Matplotlib / Cartopy</span>
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">scikit-learn</span><span class="skill-tag">TensorFlow / PyTorch</span><span class="skill-tag">netCDF4 / h5py</span>
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">Dask / multiprocessing</span><span class="skill-tag">gsw (TEOS-10)</span><span class="skill-tag">cmocean</span>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-chart-bar"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>R</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Statistical analysis, ecological modeling, and marine data visualization. Used for community ecology (PRIMER-equivalent), species distribution modeling, and publication-quality graphics.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.7rem;">
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">ggplot2 / ggOceanMaps</span><span class="skill-tag">vegan / oce / marmap</span>
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">tidyverse</span><span class="skill-tag">ncdf4</span><span class="skill-tag">randomForest / caret</span>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-bolt"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Julia &amp; MATLAB</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>High-performance numerical ocean simulations in Julia (Oceananigans.jl, OceanBioME.jl). MATLAB for legacy oceanographic analysis, ADCP processing, and spectral methods.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.7rem;">
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">Oceananigans.jl</span><span class="skill-tag">OceanBioME.jl</span>
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">m_map toolbox</span><span class="skill-tag">SeaWater toolbox</span>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-cloud"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Google Earth Engine &amp; Cloud</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Large-scale satellite time-series analysis on GEE. Cloud-based scientific workflows using GEE JavaScript/Python API, AWS S3, and HPC cluster job submission (SLURM/PBS).</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.7rem;">
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">GEE JavaScript API</span><span class="skill-tag">geemap</span>
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">HPC / SLURM</span><span class="skill-tag">AWS / Cloud Storage</span>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t</div>

\t\t\t\t\t\t\t\t\t<h3 style="color:var(--ocean-teal);border-bottom:1px solid rgba(0,206,209,0.2);padding-bottom:0.4rem;margin:1.8rem 0 1rem;"><i class="fas fa-map-marked-alt" style="margin-right:0.4em;"></i>GIS, Remote Sensing &amp; Modeling Tools</h3>
\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.45rem;margin-bottom:1.5rem;">
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> ArcGIS Pro / ArcMap</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> QGIS</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> ERDAS Imagine</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> ENVI</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> SNAP (Sentinel Toolbox)</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> SeaDAS</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> ROMS</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> FVCOM</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> ADCIRC</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> SWAT</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> HEC-RAS</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> EFDC</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> Echoview</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> PRIMER-e / R vegan</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> Adobe Illustrator</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> ODV (Ocean Data View)</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> Generic Mapping Tools (GMT)</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> WaveWatch III / SWAN</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> Git / GitHub</span>
\t\t\t\t\t\t\t\t\t\t<span class="skill-tag"><i class="fas fa-check-circle" style="color:var(--ocean-teal);"></i> LaTeX / Quarto / Markdown</span>
\t\t\t\t\t\t\t\t\t</div>

\t\t\t\t\t\t\t\t\t<h3 style="color:var(--ocean-teal);border-bottom:1px solid rgba(0,206,209,0.2);padding-bottom:0.4rem;margin:1.8rem 0 1rem;"><i class="fas fa-tachometer-alt" style="margin-right:0.4em;"></i>Proficiency Levels</h3>
\t\t\t\t\t\t\t\t\t<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:0.9rem;">
\t\t\t\t\t\t\t\t\t\t<div>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;justify-content:space-between;font-size:0.85rem;color:#c0d4d8;margin-bottom:0.22rem;"><span>Python</span><span>95%</span></div>
\t\t\t\t\t\t\t\t\t\t\t<div style="background:rgba(255,255,255,0.08);border-radius:20px;height:8px;"><div style="width:95%;background:linear-gradient(90deg,var(--ocean-teal),#0077b6);border-radius:20px;height:8px;"></div></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;justify-content:space-between;font-size:0.85rem;color:#c0d4d8;margin-bottom:0.22rem;"><span>R</span><span>88%</span></div>
\t\t\t\t\t\t\t\t\t\t\t<div style="background:rgba(255,255,255,0.08);border-radius:20px;height:8px;"><div style="width:88%;background:linear-gradient(90deg,var(--ocean-teal),#0077b6);border-radius:20px;height:8px;"></div></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;justify-content:space-between;font-size:0.85rem;color:#c0d4d8;margin-bottom:0.22rem;"><span>Google Earth Engine</span><span>90%</span></div>
\t\t\t\t\t\t\t\t\t\t\t<div style="background:rgba(255,255,255,0.08);border-radius:20px;height:8px;"><div style="width:90%;background:linear-gradient(90deg,var(--ocean-teal),#0077b6);border-radius:20px;height:8px;"></div></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;justify-content:space-between;font-size:0.85rem;color:#c0d4d8;margin-bottom:0.22rem;"><span>ArcGIS Pro / QGIS</span><span>92%</span></div>
\t\t\t\t\t\t\t\t\t\t\t<div style="background:rgba(255,255,255,0.08);border-radius:20px;height:8px;"><div style="width:92%;background:linear-gradient(90deg,var(--ocean-teal),#0077b6);border-radius:20px;height:8px;"></div></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;justify-content:space-between;font-size:0.85rem;color:#c0d4d8;margin-bottom:0.22rem;"><span>MATLAB / Julia</span><span>78%</span></div>
\t\t\t\t\t\t\t\t\t\t\t<div style="background:rgba(255,255,255,0.08);border-radius:20px;height:8px;"><div style="width:78%;background:linear-gradient(90deg,var(--ocean-teal),#0077b6);border-radius:20px;height:8px;"></div></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;justify-content:space-between;font-size:0.85rem;color:#c0d4d8;margin-bottom:0.22rem;"><span>Ocean Models (ROMS / FVCOM)</span><span>80%</span></div>
\t\t\t\t\t\t\t\t\t\t\t<div style="background:rgba(255,255,255,0.08);border-radius:20px;height:8px;"><div style="width:80%;background:linear-gradient(90deg,var(--ocean-teal),#0077b6);border-radius:20px;height:8px;"></div></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;justify-content:space-between;font-size:0.85rem;color:#c0d4d8;margin-bottom:0.22rem;"><span>Machine Learning / Deep Learning</span><span>85%</span></div>
\t\t\t\t\t\t\t\t\t\t\t<div style="background:rgba(255,255,255,0.08);border-radius:20px;height:8px;"><div style="width:85%;background:linear-gradient(90deg,var(--ocean-teal),#0077b6);border-radius:20px;height:8px;"></div></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;justify-content:space-between;font-size:0.85rem;color:#c0d4d8;margin-bottom:0.22rem;"><span>Remote Sensing / Image Analysis</span><span>90%</span></div>
\t\t\t\t\t\t\t\t\t\t\t<div style="background:rgba(255,255,255,0.08);border-radius:20px;height:8px;"><div style="width:90%;background:linear-gradient(90deg,var(--ocean-teal),#0077b6);border-radius:20px;height:8px;"></div></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t</section>

\t\t\t\t\t\t\t\t<!-- INSTRUMENTS -->
\t\t\t\t\t\t\t\t<section id="instruments">
\t\t\t\t\t\t\t\t\t<header class="major">
\t\t\t\t\t\t\t\t\t\t<h2><i class="fas fa-tools" style="color:var(--ocean-teal);margin-right:0.45em;"></i>Experience with Oceanographic Instruments</h2>
\t\t\t\t\t\t\t\t\t</header>
\t\t\t\t\t\t\t\t\t<p style="color:var(--text-medium);margin-bottom:1.5em;">Hands-on experience with field and laboratory instruments for physical, chemical, biological, and acoustic oceanographic measurements.</p>
\t\t\t\t\t\t\t\t\t<div class="activities-grid">
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-thermometer-three-quarters"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>CTD / Profilers</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Sea-Bird SBE 19plus and SBE 911 CTD systems for measuring conductivity, temperature, and pressure profiles. Water sample collection via Niskin bottle rosette. Post-processing in SBEDataProcessing and Python.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;">
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">Sea-Bird SBE 19plus</span><span class="skill-tag">SBE 911</span><span class="skill-tag">Niskin Bottles</span><span class="skill-tag">T/S Profiling</span>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-wind"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>ADCP &amp; Current Meters</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>RD Instruments Workhorse and Sentinel ADCPs for current velocity profiling, tidal analysis, and vessel-mounted surveys. WinRiver II and MATLAB processing for discharge and current shear analysis.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;">
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">RDI Workhorse ADCP</span><span class="skill-tag">WinRiver II</span><span class="skill-tag">Current Profiling</span><span class="skill-tag">Tidal Analysis</span>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-broadcast-tower"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Echosounders &amp; Acoustic Systems</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Simrad EK60/EK80 scientific echosounders and DIDSON imaging sonar for fish biomass estimation and school detection. Echoview software for data analysis and echo integration.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;">
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">Simrad EK60/EK80</span><span class="skill-tag">DIDSON Sonar</span><span class="skill-tag">Echoview</span><span class="skill-tag">Echo Integration</span>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-satellite-dish"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Optical Sensors &amp; Radiometers</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Hyperspectral and multispectral underwater radiometers (Satlantic, TriOS) for water-leaving radiance and ocean color validation. YSI EXO2 multi-parameter sonde for water quality monitoring.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;">
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">Satlantic / TriOS</span><span class="skill-tag">YSI EXO2</span><span class="skill-tag">Ocean Color Validation</span><span class="skill-tag">Hyperspectral</span>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-binoculars"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Plankton Samplers &amp; Imaging</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Bongo net, Tucker trawl, and Imaging FlowCytobot (IFCB) for phyto- and zooplankton community surveys. CNN-based automated classification pipeline developed for IFCB imagery at MSU.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;">
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">Bongo Net</span><span class="skill-tag">Imaging FlowCytobot (IFCB)</span><span class="skill-tag">Tucker Trawl</span><span class="skill-tag">Plankton Imaging</span>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-map-pin"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>GPS, Drones &amp; Survey Equipment</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Trimble differential GPS for coastal survey and ground-truth data collection. DJI Phantom and Mavic series UAVs for aerial mapping of intertidal zones, seagrass meadows, and habitat classification.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;">
\t\t\t\t\t\t\t\t\t\t\t\t<span class="skill-tag">Trimble DGPS</span><span class="skill-tag">DJI UAV</span><span class="skill-tag">Coastal Survey</span><span class="skill-tag">Ground Truthing</span>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t</section>

\t\t\t\t\t\t\t\t<!-- TEACHING -->
\t\t\t\t\t\t\t\t<section id="teaching">
\t\t\t\t\t\t\t\t\t<header class="major">
\t\t\t\t\t\t\t\t\t\t<h2><i class="fas fa-chalkboard-teacher" style="color:var(--ocean-teal);margin-right:0.45em;"></i>Teaching</h2>
\t\t\t\t\t\t\t\t\t</header>
\t\t\t\t\t\t\t\t\t<p style="color:var(--text-medium);margin-bottom:1.5em;">Courses taught, co-taught, or developed as Graduate Teaching Assistant and Instructor of Record. Syllabi available for download below.</p>
\t\t\t\t\t\t\t\t\t<div class="timeline">
\t\t\t\t\t\t\t\t\t\t<div class="timeline-item">
\t\t\t\t\t\t\t\t\t\t\t<div class="timeline-marker"><i class="fas fa-university"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<div class="timeline-content">
\t\t\t\t\t\t\t\t\t\t\t\t<div class="timeline-date">MSU &mdash; GTA</div>
\t\t\t\t\t\t\t\t\t\t\t\t<h3>Graduate Teaching Assistant &mdash; Mississippi State University</h3>
\t\t\t\t\t\t\t\t\t\t\t\t<p>Supported instruction for remote sensing and GIS courses with combined enrollment of 98+ students. Developed lab exercises, graded assignments, and delivered guest lectures.</p>
\t\t\t\t\t\t\t\t\t\t\t\t<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:0.8rem;margin-top:0.8rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t<div style="background:var(--bg-card);border:1px solid rgba(0,206,209,0.15);border-radius:8px;padding:0.85rem 1rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<strong style="color:#e8f4f8;"><i class="fas fa-map" style="color:var(--ocean-teal);margin-right:0.35em;"></i>GR 2313 &mdash; Maps and Remote Sensing</strong>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p style="font-size:0.84rem;color:#8aabb0;margin:0.3rem 0 0.5rem;">Undergraduate introductory course covering map projections, coordinate systems, aerial photography, and satellite image interpretation.</p>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="teaching/GR 2313 Maps and Remote Sensing_Hafez_Fall_2025.pdf" target="_blank" class="button small" style="font-size:0.76rem;padding:0.35rem 0.8rem;"><i class="fas fa-file-pdf"></i> Syllabus (PDF)</a>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div style="background:var(--bg-card);border:1px solid rgba(0,206,209,0.15);border-radius:8px;padding:0.85rem 1rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<strong style="color:#e8f4f8;"><i class="fas fa-satellite" style="color:var(--ocean-teal);margin-right:0.35em;"></i>GR 6333 &mdash; Remote Sensing of the Environment</strong>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p style="font-size:0.84rem;color:#8aabb0;margin:0.3rem 0 0.5rem;">Graduate-level course on electromagnetic spectrum theory, multi/hyperspectral sensor systems, image classification, and environmental applications.</p>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="teaching/GR 6333 RS_of_the_Envt_Syllabus_pdash.pdf" target="_blank" class="button small" style="font-size:0.76rem;padding:0.35rem 0.8rem;"><i class="fas fa-file-pdf"></i> Syllabus (PDF)</a>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="timeline-item">
\t\t\t\t\t\t\t\t\t\t\t<div class="timeline-marker"><i class="fas fa-book"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<div class="timeline-content">
\t\t\t\t\t\t\t\t\t\t\t\t<div class="timeline-date">Developed</div>
\t\t\t\t\t\t\t\t\t\t\t\t<h3>Courses Developed &amp; Designed</h3>
\t\t\t\t\t\t\t\t\t\t\t\t<p>Original syllabi and instructional resources developed for prospective or current teaching. Each course reflects research-integrated pedagogy with applied data science and field components.</p>
\t\t\t\t\t\t\t\t\t\t\t\t<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:0.8rem;margin-top:0.8rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t<div style="background:var(--bg-card);border:1px solid rgba(0,206,209,0.15);border-radius:8px;padding:0.85rem 1rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<strong style="color:#e8f4f8;"><i class="fas fa-water" style="color:var(--ocean-teal);margin-right:0.35em;"></i>Introduction to Oceanography</strong>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p style="font-size:0.84rem;color:#8aabb0;margin:0.3rem 0 0.5rem;">Survey course covering ocean basins, physical &amp; chemical oceanography, biological productivity, and human impacts on the ocean.</p>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="teaching/syllabus-intro-oceanography.pdf" target="_blank" class="button small" style="font-size:0.76rem;padding:0.35rem 0.8rem;"><i class="fas fa-file-pdf"></i> Syllabus</a>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div style="background:var(--bg-card);border:1px solid rgba(0,206,209,0.15);border-radius:8px;padding:0.85rem 1rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<strong style="color:#e8f4f8;"><i class="fas fa-globe" style="color:var(--ocean-teal);margin-right:0.35em;"></i>Introduction to GIS</strong>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p style="font-size:0.84rem;color:#8aabb0;margin:0.3rem 0 0.5rem;">Foundational GIS course covering vector/raster data models, coordinate reference systems, spatial analysis, and QGIS/ArcGIS applications.</p>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="teaching/introduction_to_gis_syllabus.docx" target="_blank" class="button small" style="font-size:0.76rem;padding:0.35rem 0.8rem;"><i class="fas fa-file-word"></i> Syllabus</a>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div style="background:var(--bg-card);border:1px solid rgba(0,206,209,0.15);border-radius:8px;padding:0.85rem 1rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<strong style="color:#e8f4f8;"><i class="fas fa-satellite" style="color:var(--ocean-teal);margin-right:0.35em;"></i>Applications of Remote Sensing in Marine &amp; Coastal Systems</strong>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p style="font-size:0.84rem;color:#8aabb0;margin:0.3rem 0 0.5rem;">Advanced course on marine remote sensing: ocean color algorithms, SAR, habitat mapping, and GEE workflows for coastal monitoring.</p>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="teaching/Applications of Remote Sensing in Marine and Coastal Systems.pdf" target="_blank" class="button small" style="font-size:0.76rem;padding:0.35rem 0.8rem;"><i class="fas fa-file-pdf"></i> Syllabus</a>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div style="background:var(--bg-card);border:1px solid rgba(0,206,209,0.15);border-radius:8px;padding:0.85rem 1rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<strong style="color:#e8f4f8;"><i class="fas fa-tint" style="color:var(--ocean-teal);margin-right:0.35em;"></i>Hydrological and Coastal Modeling</strong>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p style="font-size:0.84rem;color:#8aabb0;margin:0.3rem 0 0.5rem;">Graduate course on hydrodynamic and watershed modeling: SWAT, HEC-RAS, FVCOM basics, storm surge, and flood inundation with GIS integration.</p>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="teaching/Hydrological and Coastal Modeling.pdf" target="_blank" class="button small" style="font-size:0.76rem;padding:0.35rem 0.8rem;"><i class="fas fa-file-pdf"></i> Syllabus</a>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div style="background:var(--bg-card);border:1px solid rgba(0,206,209,0.15);border-radius:8px;padding:0.85rem 1rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<strong style="color:#e8f4f8;"><i class="fas fa-robot" style="color:var(--ocean-teal);margin-right:0.35em;"></i>AI &amp; Deep Learning in Earth Observation</strong>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p style="font-size:0.84rem;color:#8aabb0;margin:0.3rem 0 0.5rem;">Advanced course on deep learning for satellite imagery: CNNs, U-Net segmentation, transformer-based models, and foundation models for geospatial applications.</p>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="teaching/Artificial Intelligence and Deep Learning in Earth Observation.pdf" target="_blank" class="button small" style="font-size:0.76rem;padding:0.35rem 0.8rem;"><i class="fas fa-file-pdf"></i> Syllabus</a>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div style="background:var(--bg-card);border:1px solid rgba(0,206,209,0.15);border-radius:8px;padding:0.85rem 1rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<strong style="color:#e8f4f8;"><i class="fas fa-code" style="color:var(--ocean-teal);margin-right:0.35em;"></i>Machine Learning with Python</strong>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p style="font-size:0.84rem;color:#8aabb0;margin:0.3rem 0 0.5rem;">Hands-on course covering classical ML, model evaluation, and scikit-learn applications to oceanographic and environmental datasets.</p>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="teaching/machine_learning_with_python_syllabus.docx" target="_blank" class="button small" style="font-size:0.76rem;padding:0.35rem 0.8rem;"><i class="fas fa-file-word"></i> Syllabus</a>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div style="background:var(--bg-card);border:1px solid rgba(0,206,209,0.15);border-radius:8px;padding:0.85rem 1rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<strong style="color:#e8f4f8;"><i class="fas fa-database" style="color:var(--ocean-teal);margin-right:0.35em;"></i>Geospatial Data Science</strong>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p style="font-size:0.84rem;color:#8aabb0;margin:0.3rem 0 0.5rem;">Integrates GIS, Python, and statistical analysis for solving spatial environmental problems; covers geostatistics, spatial regression, and interactive dashboards.</p>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="teaching/geospatial_data_science_syllabus.docx" target="_blank" class="button small" style="font-size:0.76rem;padding:0.35rem 0.8rem;"><i class="fas fa-file-word"></i> Syllabus</a>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div style="background:var(--bg-card);border:1px solid rgba(0,206,209,0.15);border-radius:8px;padding:0.85rem 1rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<strong style="color:#e8f4f8;"><i class="fas fa-cloud" style="color:var(--ocean-teal);margin-right:0.35em;"></i>Geospatial Big Data Analytics &amp; Cloud Computing</strong>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p style="font-size:0.84rem;color:#8aabb0;margin:0.3rem 0 0.5rem;">Covers distributed computing, GEE at scale, AWS/cloud storage, large-scale raster analytics, and parallel Python (Dask, Ray) for petabyte-scale datasets.</p>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="teaching/Geospatial Big Data Analytics and Cloud Computing.pdf" target="_blank" class="button small" style="font-size:0.76rem;padding:0.35rem 0.8rem;"><i class="fas fa-file-pdf"></i> Syllabus</a>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div style="background:var(--bg-card);border:1px solid rgba(0,206,209,0.15);border-radius:8px;padding:0.85rem 1rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<strong style="color:#e8f4f8;"><i class="fas fa-flask" style="color:var(--ocean-teal);margin-right:0.35em;"></i>Oceanographic &amp; Atmospheric Data Analysis</strong>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p style="font-size:0.84rem;color:#8aabb0;margin:0.3rem 0 0.5rem;">Graduate course on analysis of observational data: time series, spectral analysis, EOF/PCA, empirical mode decomposition, and reanalysis products.</p>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="teaching/Oceanographic and Atmospheric Data Analysis.pdf" target="_blank" class="button small" style="font-size:0.76rem;padding:0.35rem 0.8rem;"><i class="fas fa-file-pdf"></i> Syllabus</a>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div style="background:var(--bg-card);border:1px solid rgba(0,206,209,0.15);border-radius:8px;padding:0.85rem 1rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<strong style="color:#e8f4f8;"><i class="fas fa-leaf" style="color:var(--ocean-teal);margin-right:0.35em;"></i>Ecological Modeling</strong>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p style="font-size:0.84rem;color:#8aabb0;margin:0.3rem 0 0.5rem;">NPZ, EwE, species distribution, and Ecopath/Ecosim approaches. Quantitative methods for population dynamics, habitat suitability, and food-web structure with R and Python.</p>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="teaching/syllabus-ecological-modeling.pdf" target="_blank" class="button small" style="font-size:0.76rem;padding:0.35rem 0.8rem;"><i class="fas fa-file-pdf"></i> Syllabus</a>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div style="background:var(--bg-card);border:1px solid rgba(0,206,209,0.15);border-radius:8px;padding:0.85rem 1rem;">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<strong style="color:#e8f4f8;"><i class="fas fa-atom" style="color:var(--ocean-teal);margin-right:0.35em;"></i>Applied AI &amp; Agentic Systems for Environmental Sciences</strong>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p style="font-size:0.84rem;color:#8aabb0;margin:0.3rem 0 0.5rem;">Emerging course on LLM-based agentic workflows, retrieval-augmented generation (RAG), AI copilots for data analysis, and autonomous environmental monitoring pipelines.</p>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="teaching/Applied AI and Agentic Systems for Environmental Sciences.pdf" target="_blank" class="button small" style="font-size:0.76rem;padding:0.35rem 0.8rem;"><i class="fas fa-file-pdf"></i> Syllabus</a>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t</section>

\t\t\t\t\t\t\t\t<!-- RESEARCH TOPICS -->
\t\t\t\t\t\t\t\t<section id="research-topics">
\t\t\t\t\t\t\t\t\t<header class="major">
\t\t\t\t\t\t\t\t\t\t<h2><i class="fas fa-microscope" style="color:var(--ocean-teal);margin-right:0.45em;"></i>Research Topics</h2>
\t\t\t\t\t\t\t\t\t</header>
\t\t\t\t\t\t\t\t\t<p style="color:var(--text-medium);margin-bottom:1.5em;">Core thematic areas driving my research programme, spanning observational, computational, and applied dimensions of ocean and coastal science.</p>
\t\t\t\t\t\t\t\t\t<div class="activities-grid">
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-water"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Coastal &amp; Estuarine Hydrodynamics</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Tidal circulation, freshwater discharge dynamics, storm surge, and wind-driven mixing in estuaries and shallow coastal zones. Numerical modeling with FVCOM and ROMS validated against tide gauge and ADCP observations.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">FVCOM / ROMS</span><span class="skill-tag">Storm Surge</span><span class="skill-tag">Estuarine Circulation</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-vial"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Coastal Water Quality &amp; Hypoxia</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Machine learning and satellite remote sensing for chlorophyll-a, turbidity, CDOM, and dissolved oxygen estimation. Hypoxia dynamics in the northern Gulf of Mexico and Mississippi Sound.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">Water Quality RS</span><span class="skill-tag">Hypoxia</span><span class="skill-tag">Gulf of Mexico</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-satellite"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Ocean Color &amp; Marine Remote Sensing</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Satellite-derived primary productivity, particulate organic carbon, mesoscale eddies, and phytoplankton functional types from MODIS, Sentinel-2/3, and Landsat archives using GEE-based processing pipelines.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">Ocean Color</span><span class="skill-tag">POC / Chl-a</span><span class="skill-tag">Sentinel / Landsat</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-brain"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Machine Learning in Ocean Science</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Ensemble ML, deep learning (CNN, LSTM, Transformers), and foundation model fine-tuning for water quality retrieval, plankton classification, habitat mapping, and eddy detection.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">CNN / LSTM</span><span class="skill-tag">Foundation Models</span><span class="skill-tag">XGBoost / RF</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-leaf"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Marine Ecology &amp; Biodiversity</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Phytoplankton community structure, seagrass mapping, habitat connectivity, and species distribution modeling. Integration of acoustic telemetry, eDNA, and remote sensing for ecosystem-level assessments.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">SDM</span><span class="skill-tag">Seagrass Mapping</span><span class="skill-tag">Acoustic Telemetry</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-exclamation-triangle"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Coastal Hazards &amp; Climate Change</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Sea-level rise impacts, coastal erosion, compound flooding risk, and land-use change detection using time-series remote sensing and delta change modeling (Sundarbans, Irrawaddy, Gulf Coast).</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">Sea-Level Rise</span><span class="skill-tag">Delta Change</span><span class="skill-tag">LULC Dynamics</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-fish"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>Fisheries Acoustics &amp; Biomass Estimation</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Quantitative echo integration, target strength analysis, and kriging-based spatial biomass estimation from scientific echosounder surveys. Applied to Gulf of Mexico and freshwater reservoir fisheries.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">Echo Integration</span><span class="skill-tag">Target Strength</span><span class="skill-tag">Echoview</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t<div class="activity-card">
\t\t\t\t\t\t\t\t\t\t\t<div class="card-icon"><i class="fas fa-map-marked-alt"></i></div>
\t\t\t\t\t\t\t\t\t\t\t<h3>GIS &amp; Geospatial Data Science</h3>
\t\t\t\t\t\t\t\t\t\t\t<p>Advanced spatial analysis, land cover change detection, spatial statistics, and geostatistical interpolation for environmental management. GEE-based cloud workflows for large-area coastal monitoring.</p>
\t\t\t\t\t\t\t\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-top:0.6rem;"><span class="skill-tag">Spatial Analysis</span><span class="skill-tag">Change Detection</span><span class="skill-tag">Geostatistics</span></div>
\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t</section>

"""

# ── perform the replacement ──────────────────────────────────────────────────
replacement = (
    '\t\t\t\t\t\t\t\t</section>\n'
    + new_sections
    + '\n\t\t\t\t\t\t\t<!-- Section -->\n'
    '\t\t\t\t\t\t\t\t\t<section id="about">'
)

new_content = content.replace(old_marker, replacement, 1)

if len(new_content) <= len(content) + 5000:
    print(f'ERROR: not enough content added. Diff = {len(new_content)-len(content)}')
    sys.exit(1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'SUCCESS! {len(content):,} -> {len(new_content):,} chars  (+{len(new_content)-len(content):,})')

# ── quick verification ────────────────────────────────────────────────────────
checks = [
    'id="skills"', 'id="instruments"', 'id="teaching"', 'id="research-topics"',
    'width:95%', 'Sea-Bird SBE 19plus', 'Simrad EK60', 'YSI EXO2', 'DJI UAV',
    'GR 2313', 'GR 6333', 'syllabus-intro-oceanography.pdf',
    'Applied AI and Agentic Systems', 'Hydrological and Coastal Modeling.pdf',
]
ok, fail = [], []
for c in checks:
    (ok if c in new_content else fail).append(c)
print(f'PASS: {len(ok)}/{len(checks)}')
if fail:
    print('MISSING:', fail)
