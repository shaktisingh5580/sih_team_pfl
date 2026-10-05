"""
Generate HTML pages from ORCA markdown documents.
Converts markdown to HTML with proper code block, table, and heading rendering.
"""
import re
import html
import os

BASE_DIR = r"c:\Users\shakt\Downloads\Smart_india_hackathon_2026"
OUT_DIR = os.path.join(BASE_DIR, "orca-research-doc")

# Document definitions: (output_file, source_md, title, nav_active, prev, next)
DOCS = [
    ("doc1.html",
     "ORCA Architecture Document 1 — Complete User Flow Architecture.md",
     "Doc 1 — Complete User Flow Architecture",
     "User Flows",
     ("index.html", "Home"),
     ("doc2.html", "Doc 2: Agentic System")),

    ("doc2.html",
     "ORCA Architecture Document 2 — Core Agentic System Architecture.md",
     "Doc 2 — Core Agentic System Architecture",
     "Agentic System",
     ("doc1.html", "Doc 1: User Flows"),
     ("doc3.html", "Doc 3: Data Pipeline")),

    ("doc3.html",
     "ORCA Architecture Document 3 — Data Processing Pipeline & Scientific Intelligence.md",
     "Doc 3 — Data Processing Pipeline & Scientific Intelligence",
     "Data Pipeline",
     ("doc2.html", "Doc 2: Agentic System"),
     ("doc4.html", "Doc 4: Database")),

    ("doc4.html",
     "ORCA Architecture Document 4 — Database Design.md",
     "Doc 4 — Database Design",
     "Database",
     ("doc3.html", "Doc 3: Data Pipeline"),
     ("doc5.html", "Doc 5: Implementation")),

    ("doc5.html",
     "ORCA Architecture Document 5 — Implementation Plan & PS Reminder.md",
     "Doc 5 — Implementation Plan & PS Reminder",
     "Implementation",
     ("doc4.html", "Doc 4: Database"),
     ("doc6.html", "Doc 6: Memory & Context")),

    ("doc6.html",
     "ORCA Archetecture Document 6_Memory_and_Context_Architecture_Deep_Research_and_Implementation.md",
     "Doc 6 — Memory & Context Architecture",
     "Memory & Context",
     ("doc5.html", "Doc 5: Implementation"),
     ("fisher.html", "Fisher Research")),

    ("fisher.html",
     "ORCA_Fisher_Research_and_Product_Reference (1).md",
     "Fisher-Facing Product Research & Field Validation",
     "Fisher Research",
     ("doc6.html", "Doc 6: Memory & Context"),
     ("data-sources.html", "Data Sources")),

    ("data-sources.html",
     "ORCA_Data_Acquisition_Matrix_and_Engineering_Specification.md",
     "Data Acquisition Matrix & Engineering Specification",
     "Data Sources",
     ("fisher.html", "Fisher Research"),
     ("agentic-spec.html", "Agentic Spec")),

    ("agentic-spec.html",
     "ORCA_System_3_Agentic_and_Orchestration_Engineering_Specification_v2_Security_Evals_Reliability.md",
     "Agentic & Orchestration Engineering Specification",
     "Agentic Spec",
     ("data-sources.html", "Data Sources"),
     ("scientific.html", "Scientific System")),

    ("scientific.html",
     "ORCA_System_7_Scientific_and_Marine_Intelligence_System.md",
     "Scientific & Marine Intelligence System",
     "Scientific System",
     ("agentic-spec.html", "Agentic Spec"),
     ("core-agentic-technical.html", "Core Agentic Tech")),

    ("core-agentic-technical.html",
     "ORCA_Core_Agentic_Technical_Architecture.md",
     "Core Agentic Technical Architecture",
     "Core Agentic Tech",
     ("scientific.html", "Scientific System"),
     ("master-arch.html", "Master Architecture")),

    ("master-arch.html",
     "ORCA_MASTER_ARCHITECTURE.md",
     "ORCA Master Architecture",
     "Master Architecture",
     ("core-agentic-technical.html", "Core Agentic Tech"),
     ("index.html", "Home")),
]

NAV_ITEMS = [
    ("index.html", "Home"),
    ("architecture.html", "Architecture Diagram"),
    ("doc1.html", "User Flows"),
    ("doc2.html", "Agentic System"),
    ("doc3.html", "Data Pipeline"),
    ("doc4.html", "Database"),
    ("doc5.html", "Implementation"),
    ("doc6.html", "Memory & Context"),
    ("fisher.html", "Fisher Research"),
    ("data-sources.html", "Data Sources"),
]


def md_to_html(md_text, page_prefix='doc'):
    """Simple but effective markdown to HTML converter for code blocks, tables, headings, etc."""
    lines = md_text.split('\n')
    result = []
    in_code = False
    code_lang = ''
    code_lines = []
    diag_count = 0
    in_table = False
    table_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Code blocks
        if line.strip().startswith('```'):
            if in_code:
                # End code block
                if code_lang.lower() == 'mermaid':
                    diag_count += 1
                    diag_id = f"{page_prefix}-mermaid-{diag_count}"
                    raw_code = '\n'.join(code_lines).strip()
                    escaped_code = html.escape(raw_code)
                    result.append(f'''<div class="mermaid-container" id="{diag_id}">
  <div class="mermaid-toolbar">
    <div class="mermaid-title"><span class="mermaid-icon">&#9881;</span> Architecture Diagram</div>
    <div class="mermaid-controls">
      <button type="button" class="mm-btn" onclick="mermaidZoom('{diag_id}', 1.25)" title="Zoom In">&#65291; Zoom</button>
      <button type="button" class="mm-btn" onclick="mermaidZoom('{diag_id}', 0.8)" title="Zoom Out">&#65293;</button>
      <button type="button" class="mm-btn" onclick="mermaidReset('{diag_id}')" title="Fit to Screen">&#x26F6; Fit</button>
      <button type="button" class="mm-btn" onclick="mermaidFullscreen('{diag_id}')" title="Expand Fullscreen">&#x2922; Expand</button>
      <button type="button" class="mm-btn mm-btn-copy" onclick="mermaidCopy('{diag_id}')" title="Copy Mermaid Syntax">Copy Code</button>
      <button type="button" class="mm-btn" onclick="mermaidToggleCode('{diag_id}')" title="Toggle Source Code">&lt;/&gt; Code</button>
    </div>
  </div>
  <div class="mermaid-viewport" id="{diag_id}-viewport">
    <div class="mermaid-stage" id="{diag_id}-stage">
      <div style="color: #64748b; font-size: 13px; padding: 20px;">Rendering diagram...</div>
    </div>
    <pre class="mermaid-source" style="display:none;">{escaped_code}</pre>
  </div>
  <div class="mermaid-code" id="{diag_id}-code" style="display:none;">
    <pre><code>{escaped_code}</code></pre>
  </div>
</div>''')
                else:
                    code_content = html.escape('\n'.join(code_lines))
                    lang_class = f' class="language-{code_lang}"' if code_lang else ''
                    result.append(f'<pre><code{lang_class}>{code_content}</code></pre>')
                code_lines = []
                in_code = False
            else:
                # Start code block
                in_code = True
                code_lang = line.strip()[3:].strip()
                code_lines = []
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        # Tables
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(line)
            i += 1
            continue
        elif in_table:
            # End of table
            result.append(render_table(table_lines))
            in_table = False

        stripped = line.strip()

        # Empty line
        if not stripped:
            result.append('')
            i += 1
            continue

        # Headings
        if stripped.startswith('# '):
            result.append(f'<h1>{inline_md(stripped[2:])}</h1>')
        elif stripped.startswith('## '):
            result.append(f'<h2>{inline_md(stripped[3:])}</h2>')
        elif stripped.startswith('### '):
            result.append(f'<h3>{inline_md(stripped[4:])}</h3>')
        elif stripped.startswith('#### '):
            result.append(f'<h4>{inline_md(stripped[5:])}</h4>')

        # Horizontal rule
        elif stripped == '---' or stripped == '***':
            result.append('<hr>')

        # Blockquote with admonitions
        elif stripped.startswith('> [!'):
            # GitHub-style admonitions
            admonition_match = re.match(r'>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]', stripped)
            if admonition_match:
                adm_type = admonition_match.group(1).lower()
                css_class = {'note': 'note', 'tip': 'tip', 'important': 'important',
                             'warning': 'warning', 'caution': 'warning'}[adm_type]
                # Collect all blockquote lines
                adm_lines = []
                i += 1
                while i < len(lines) and lines[i].strip().startswith('>'):
                    content = lines[i].strip()
                    if content.startswith('> '):
                        adm_lines.append(content[2:])
                    elif content == '>':
                        adm_lines.append('')
                    else:
                        adm_lines.append(content[1:])
                    i += 1
                adm_content = inline_md(' '.join(adm_lines))
                result.append(f'<div class="{css_class}"><strong>{adm_type.upper()}:</strong> {adm_content}</div>')
                continue

        # Regular blockquote
        elif stripped.startswith('>'):
            bq_lines = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                content = lines[i].strip()
                if content.startswith('> '):
                    bq_lines.append(content[2:])
                elif content == '>':
                    bq_lines.append('')
                else:
                    bq_lines.append(content[1:])
                i += 1
            bq_content = inline_md('<br>'.join(bq_lines))
            result.append(f'<blockquote>{bq_content}</blockquote>')
            continue

        # Unordered list
        elif stripped.startswith('- ') or stripped.startswith('* '):
            list_items = []
            while i < len(lines):
                l = lines[i].strip()
                if l.startswith('- ') or l.startswith('* '):
                    list_items.append(inline_md(l[2:]))
                elif l.startswith('  ') and list_items:
                    list_items[-1] += ' ' + inline_md(l.strip())
                elif not l:
                    break
                else:
                    break
                i += 1
            ul = '<ul>\n' + '\n'.join(f'<li>{item}</li>' for item in list_items) + '\n</ul>'
            result.append(ul)
            continue

        # Ordered list
        elif re.match(r'^\d+\.\s', stripped):
            list_items = []
            while i < len(lines):
                l = lines[i].strip()
                m = re.match(r'^\d+\.\s(.*)', l)
                if m:
                    list_items.append(inline_md(m.group(1)))
                elif l.startswith('  ') and list_items:
                    list_items[-1] += ' ' + inline_md(l.strip())
                elif not l:
                    break
                else:
                    break
                i += 1
            ol = '<ol>\n' + '\n'.join(f'<li>{item}</li>' for item in list_items) + '\n</ol>'
            result.append(ol)
            continue

        # Paragraph
        else:
            result.append(f'<p>{inline_md(stripped)}</p>')

        i += 1

    # Close any remaining code block
    if in_code:
        code_content = html.escape('\n'.join(code_lines))
        result.append(f'<pre><code>{code_content}</code></pre>')

    # Close any remaining table
    if in_table:
        result.append(render_table(table_lines))

    return '\n'.join(result)


def render_table(lines):
    """Render markdown table lines to HTML."""
    if len(lines) < 2:
        return ''

    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        rows.append(cells)

    # Skip separator row (row[1] with dashes)
    header = rows[0]
    data_rows = []
    for r in rows[1:]:
        if all(re.match(r'^[-:]+$', c) for c in r if c):
            continue
        data_rows.append(r)

    html_out = '<div style="overflow-x:auto;"><table>\n<thead><tr>'
    for h in header:
        html_out += f'<th>{inline_md(h)}</th>'
    html_out += '</tr></thead>\n<tbody>'
    for row in data_rows:
        html_out += '<tr>'
        for j, cell in enumerate(row):
            html_out += f'<td>{inline_md(cell)}</td>'
        html_out += '</tr>\n'
    html_out += '</tbody></table></div>'
    return html_out


def inline_md(text):
    """Convert inline markdown: bold, italic, code, links."""
    # Escape HTML first (but preserve already-safe content)
    # Bold + italic
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', text)
    return text


def extract_toc(content_html):
    """Extract headings from rendered HTML and return (toc_html, updated_content_html).
    Adds id attributes to headings and builds a TOC list."""
    import re as _re
    headings = []
    counter = [0]

    def add_id(match):
        tag = match.group(1)  # h1, h2, h3, h4
        inner = match.group(2)
        counter[0] += 1
        slug = f"section-{counter[0]}"
        # Strip HTML tags for TOC text
        text = _re.sub(r'<[^>]+>', '', inner).strip()
        if len(text) > 80:
            text = text[:77] + '...'
        headings.append((tag, slug, text))
        return f'<{tag} id="{slug}">{inner}</{tag}>'

    updated = _re.sub(r'<(h[1-4])>(.*?)</\1>', add_id, content_html)

    # Build TOC HTML
    toc_items = []
    for tag, slug, text in headings:
        css_class = ''
        if tag == 'h3':
            css_class = ' class="toc-h3"'
        elif tag == 'h4':
            css_class = ' class="toc-h4"'
        toc_items.append(f'<li><a href="#{slug}"{css_class} data-target="{slug}">{text}</a></li>')

    toc_html = '\n'.join(toc_items)
    return toc_html, updated


def generate_page(out_file, title, nav_active, content_html, prev_link, next_link):
    """Generate a full HTML page with the Karpathy-style template + sidebar TOC."""
    nav_html = ''
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if label == nav_active else ''
        nav_html += f'<a href="{href}"{cls}>{label}</a>\n'

    prev_html = ''
    if prev_link:
        prev_html = f'''<a href="{prev_link[0]}">
      <span class="page-nav-label">&#8592; Previous</span>
      <span class="page-nav-title">{prev_link[1]}</span>
    </a>'''

    next_html = ''
    if next_link:
        next_html = f'''<a href="{next_link[0]}" class="next">
      <span class="page-nav-label">Next &#8594;</span>
      <span class="page-nav-title">{next_link[1]}</span>
    </a>'''

    # Extract TOC from content
    toc_html, content_with_ids = extract_toc(content_html)

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>{title} | ORCA Research Dossier</title>
<meta name="description" content="ORCA &#8212; {title}. Complete research and architecture documentation.">
<link rel="stylesheet" type="text/css" href="style.css">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="mermaid.min.js"></script>
<script>
if (typeof mermaid === 'undefined') {{
  document.write('<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"><\\/script>');
}}
</script>
</head>
<body>

<header id="dhead" class="container">
  <div class="row">
    <div id="dpic">
      <img src="ORCA_architecture.svg" class="ppic" alt="ORCA" onerror="this.style.background='#f0f0f0'" />
    </div>
    <div id="ddesc">
      <h1>ORCA</h1>
      <h2>{title}</h2>
      <nav class="doc-nav">
        {nav_html}
      </nav>
    </div>
  </div>
</header>

<hr>

<div class="page-with-toc">
  <!-- Sidebar TOC -->
  <aside class="toc-sidebar">
    <div class="toc-sticky">
      <div class="toc-header">
        <span class="toc-label">&#9679; Table of Contents</span>
        <a class="toc-top-link" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">&#8593; TOP</a>
      </div>
      <ul class="toc-list" id="tocList">
        {toc_html}
      </ul>
    </div>
  </aside>

  <!-- Main content -->
  <div class="toc-content">
    <div class="breadcrumb"><a href="index.html">Home</a> / {title}</div>

    <div class="md-content">
{content_with_ids}
    </div>

    <div class="page-nav">
      {prev_html}
      {next_html}
    </div>
  </div>
</div>

<footer class="container">
  <strong>ORCA</strong> &#183; Marine EcOsystem Reasoning with Collaborative Agents &#183; SIH 2026 &#183; PS 26176
</footer>

<button class="back-to-top" id="backToTop" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">&#8593;</button>

<script>
// Back to top button
window.addEventListener('scroll', function() {{
  var btn = document.getElementById('backToTop');
  if (window.scrollY > 300) {{ btn.classList.add('visible'); }}
  else {{ btn.classList.remove('visible'); }}
}});

// Scroll-spy: highlight active TOC link
(function() {{
  var tocLinks = document.querySelectorAll('#tocList a');
  if (!tocLinks.length) return;

  var headingEls = [];
  tocLinks.forEach(function(link) {{
    var target = link.getAttribute('data-target');
    var el = document.getElementById(target);
    if (el) headingEls.push({{ el: el, link: link }});
  }});

  function updateActive() {{
    var scrollY = window.scrollY + 80;
    var current = null;

    for (var i = 0; i < headingEls.length; i++) {{
      if (headingEls[i].el.offsetTop <= scrollY) {{
        current = headingEls[i];
      }}
    }}

    tocLinks.forEach(function(l) {{ l.classList.remove('active'); }});
    if (current) {{
      current.link.classList.add('active');
      // Scroll TOC to keep active item visible
      var tocSticky = current.link.closest('.toc-sticky');
      if (tocSticky) {{
        var linkTop = current.link.offsetTop - tocSticky.offsetTop;
        var stickyHeight = tocSticky.clientHeight;
        if (linkTop < tocSticky.scrollTop || linkTop > tocSticky.scrollTop + stickyHeight - 40) {{
          tocSticky.scrollTop = linkTop - stickyHeight / 3;
        }}
      }}
    }}
  }}

  window.addEventListener('scroll', updateActive);
  updateActive();
}})();

// --- Mermaid Diagram Compiler & Interactive Viewer ---
(function() {{
  if (typeof mermaid === 'undefined') return;

  try {{
    mermaid.initialize({{
      startOnLoad: false,
      theme: 'neutral',
      securityLevel: 'loose',
      fontFamily: 'Inter, system-ui, -apple-system, sans-serif',
      maxTextSize: 100000,
      flowchart: {{
        htmlLabels: true,
        curve: 'basis',
        useMaxWidth: true
      }},
      er: {{
        useMaxWidth: true
      }}
    }});
  }} catch (e) {{
    console.error('Mermaid init error:', e);
  }}

  window.mmZoomState = window.mmZoomState || {{}};

  async function compileMermaidDiagrams() {{
    var containers = document.querySelectorAll('.mermaid-container');
    if (!containers.length) return;

    for (var i = 0; i < containers.length; i++) {{
      var container = containers[i];
      var id = container.id;
      var preEl = container.querySelector('pre.mermaid-source');
      var stageEl = document.getElementById(id + '-stage');
      if (!preEl || !stageEl) continue;

      var code = preEl.textContent.trim();
      mmZoomState[id] = 1.0;

      try {{
        var renderId = 'mm-svg-' + id.replace(/[^a-zA-Z0-9_-]/g, '_') + '-' + i;
        var res = await mermaid.render(renderId, code);
        stageEl.innerHTML = res.svg;
        var svgEl = stageEl.querySelector('svg');
        if (svgEl) {{
          svgEl.style.maxWidth = '100%';
          svgEl.style.height = 'auto';
          svgEl.style.display = 'block';
          svgEl.style.margin = '0 auto';
          svgEl.setAttribute('preserveAspectRatio', 'xMidYMid meet');
        }}
      }} catch (err) {{
        console.error('Mermaid render error for ' + id + ':', err);
        stageEl.innerHTML = '<div class="mermaid-error">' +
          '<div class="mermaid-error-title">&#9888; Diagram Compilation Notice</div>' +
          '<p>' + (err.message || String(err)) + '</p>' +
          '</div>';
      }}
    }}
  }}

  window.mermaidZoom = function(id, factor) {{
    var stage = document.getElementById(id + '-stage');
    if (!stage) return;
    var svg = stage.querySelector('svg');
    if (!svg) return;
    mmZoomState[id] = (mmZoomState[id] || 1.0) * factor;
    if (mmZoomState[id] < 0.25) mmZoomState[id] = 0.25;
    if (mmZoomState[id] > 4.0) mmZoomState[id] = 4.0;
    stage.style.transform = 'scale(' + mmZoomState[id] + ')';
    if (mmZoomState[id] > 1.0) {{
      svg.style.maxWidth = 'none';
    }} else {{
      svg.style.maxWidth = '100%';
    }}
  }};

  window.mermaidReset = function(id) {{
    var stage = document.getElementById(id + '-stage');
    if (!stage) return;
    var svg = stage.querySelector('svg');
    if (!svg) return;
    mmZoomState[id] = 1.0;
    stage.style.transform = 'scale(1)';
    svg.style.maxWidth = '100%';
  }};

  window.mermaidToggleCode = function(id) {{
    var codeDiv = document.getElementById(id + '-code');
    if (!codeDiv) return;
    codeDiv.style.display = (codeDiv.style.display === 'none') ? 'block' : 'none';
  }};

  window.mermaidCopy = function(id) {{
    var container = document.getElementById(id);
    if (!container) return;
    var codePre = container.querySelector('.mermaid-code pre code') || container.querySelector('pre.mermaid-source');
    if (!codePre) return;
    navigator.clipboard.writeText(codePre.textContent).then(function() {{
      var btn = container.querySelector('.mm-btn-copy');
      if (btn) {{
        var orig = btn.innerHTML;
        btn.innerHTML = '&#10003; Copied!';
        btn.style.color = '#137333';
        setTimeout(function() {{ btn.innerHTML = orig; btn.style.color = ''; }}, 2000);
      }}
    }});
  }};

  window.mermaidFullscreen = function(id) {{
    var container = document.getElementById(id);
    if (!container) return;
    if (!document.fullscreenElement) {{
      if (container.requestFullscreen) {{
        container.requestFullscreen().catch(function() {{ container.classList.toggle('is-fullscreen'); }});
      }} else {{
        container.classList.toggle('is-fullscreen');
      }}
    }} else {{
      if (document.exitFullscreen) {{
        document.exitFullscreen();
      }}
    }}
  }};

  document.addEventListener('fullscreenchange', function() {{
    var containers = document.querySelectorAll('.mermaid-container');
    containers.forEach(function(c) {{
      if (c === document.fullscreenElement) {{
        c.classList.add('is-fullscreen');
      }} else {{
        c.classList.remove('is-fullscreen');
      }}
    }});
  }});

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', compileMermaidDiagrams);
  }} else {{
    compileMermaidDiagrams();
  }}
}})();
</script>

</body>
</html>'''
    return page


def main():
    count = 0
    for out_file, src_md, title, nav_active, prev_link, next_link in DOCS:
        src_path = os.path.join(BASE_DIR, src_md)
        out_path = os.path.join(OUT_DIR, out_file)

        if not os.path.exists(src_path):
            print(f"SKIP: {src_md} not found")
            continue

        print(f"Processing: {src_md} -> {out_file}")

        with open(src_path, 'r', encoding='utf-8') as f:
            md_text = f.read()

        page_slug = out_file.replace('.html', '')
        content_html = md_to_html(md_text, page_prefix=page_slug)
        page_html = generate_page(out_file, title, nav_active, content_html, prev_link, next_link)

        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(page_html)

        count += 1
        print(f"  OK Written {out_file} ({len(page_html)} bytes)")

    print(f"\nDone! Generated {count} pages in {OUT_DIR}")


if __name__ == '__main__':
    main()

