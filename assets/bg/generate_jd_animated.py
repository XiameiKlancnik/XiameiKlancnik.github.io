import math, sys, pathlib, json
W, H = 2560, 1440

def ridge_y(x, center=0.5, width=0.14, height=220, wiggle=28, seed=0):
    g = math.exp(-((x-center)**2)/(2*width*width))
    y = height*g
    y += wiggle * math.sin(2*math.pi*(3.0*x + 0.1*seed))
    y += 0.5*wiggle * math.sin(2*math.pi*(5.7*x + 0.17*seed + 0.3))
    y += 0.25*wiggle * math.sin(2*math.pi*(11.3*x + 0.37*seed + 1.2))
    return y

def line_path(y_offset, scale=1.0, samples=1100, seed=0):
    parts=[]
    for i in range(samples):
        t = i/(samples-1)
        x = t*W
        y = ridge_y(t, height=260*scale, wiggle=24*scale, seed=seed)
        y += 16*scale*math.sin(2*math.pi*(t*0.6 + seed*0.03))
        parts.append(("%s %.2f,%.2f" % ("M" if i==0 else "L", x, (y_offset - y))))
    return " ".join(parts)

def build_svg_animated(accent, halo, bg, contrast=1.0):
    svg=[]
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    svg.append(f'''
<defs>
  <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="{2.2*contrast:.2f}" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <radialGradient id="vignette" cx="40%" cy="50%" r="80%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="100%" stop-color="#000" stop-opacity="{0.55 if contrast>=1 else 0.45}"/>
  </radialGradient>
</defs>
''')
    svg.append(f'<rect width="{W}" height="{H}" fill="{bg}"/>')
    svg.append(f'<rect width="{W}" height="{H}" fill="url(#vignette)"/>')

    num_lines=56; gap=20
    center_y = H*0.56
    start_y = center_y - (num_lines//2)*gap

    for i in range(num_lines):
        y_off = start_y + i*gap
        scale = 0.98 + (i - num_lines/2)*0.004
        d = line_path(y_off, scale=scale, seed=i)
        dist = abs(i - num_lines/2) / (num_lines/2)
        base_opacity = 0.92*(1 - 0.85*dist) + 0.12
        core_opacity = min(1.0, base_opacity * (0.95 if contrast>=1 else 0.75))
        halo_opacity = base_opacity * (0.22 if contrast>=1 else 0.16)
        stroke_w = 2.0 if i % 2 == 0 else 1.3

        # Add animated wave effect - each line has slightly offset timing
        path_id = f"path{i}"
        duration = 8 + (i % 5) * 0.3  # Vary duration 8-9.5s

        # Halo path with animation
        svg.append(f'<path id="{path_id}_halo" d="{d}" fill="none" stroke="{halo}" stroke-opacity="{halo_opacity:.3f}" stroke-width="{stroke_w*6:.2f}" filter="url(#softGlow)">')
        svg.append(f'  <animateTransform attributeName="transform" type="translate" values="0,0; 0,-8; 0,0; 0,6; 0,0" dur="{duration}s" repeatCount="indefinite"/>')
        svg.append(f'</path>')

        # Core path with animation
        svg.append(f'<path id="{path_id}_core" d="{d}" fill="none" stroke="{accent}" stroke-opacity="{core_opacity:.3f}" stroke-width="{stroke_w:.2f}">')
        svg.append(f'  <animateTransform attributeName="transform" type="translate" values="0,0; 0,-8; 0,0; 0,6; 0,0" dur="{duration}s" repeatCount="indefinite"/>')
        svg.append(f'</path>')

    svg.append('</svg>')
    return "\n".join(svg)

if __name__ == "__main__":
    # Read palette via JSON env on argv[1]
    pal = json.loads(sys.argv[1])
    out_std   = pathlib.Path(pal["out_dir"]) / f'jd_{pal["name"]}.svg'
    out_subtle= pathlib.Path(pal["out_dir"]) / f'jd_{pal["name"]}_subtle.svg'
    out_std.write_text(build_svg_animated(pal["accent"], pal["halo"], pal["bg"], contrast=1.0), encoding="utf-8")
    out_subtle.write_text(build_svg_animated(pal["accent"], pal["halo"], pal["bg"], contrast=0.8), encoding="utf-8")
    print(f"Generated animated: {out_std}")
    print(f"Generated animated: {out_subtle}")
