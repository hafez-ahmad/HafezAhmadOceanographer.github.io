path = r'c:\Users\hafez\MSU\Research\HafezAhmadOceanographer.github.io\index.html'
with open(path, encoding='utf-8') as f:
    c = f.read()
checks = [
    ('Hydrological Connectivity card', 'Hydrological Connectivity'),
    ('Methods section id', 'id="methods"'),
    ('Cellular Automata card', 'Cellular Automata'),
    ('Multivariate stats (PERMANOVA)', 'PERMANOVA'),
    ('Time series (Mann-Kendall)', 'Mann-Kendall'),
    ('Hydro numerical (Lagrangian)', 'Lagrangian Tracking'),
    ('RS analysis (CCDC)', 'CCDC / LandTrendr'),
    ('Ecology (Ecopath)', 'Ecopath'),
    ('Methods in nav', 'Analytical Methods'),
    ('Section nav methods link', '#methods'),
    ('Moran spatial', "Moran"),
]
for label, ch in checks:
    print(f"{'PASS' if ch in c else 'FAIL'}: {label}")
print(f"\nFile size: {len(c):,} chars")
