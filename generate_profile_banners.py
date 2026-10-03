import os
import shutil
from PIL import Image, ImageEnhance

# 1. Load portrait and generate ASCII overlay
im = Image.open("assets/portrait_processed.jpg").convert("L")
cols = 34
rows = 24
im_small = im.resize((cols, rows), Image.Resampling.LANCZOS)
enhancer = ImageEnhance.Contrast(im_small)
im_contrasted = enhancer.enhance(1.25)

char_ramp = " .,:;!+=*%#@"
ascii_rows = []
for y in range(rows):
    line = []
    for x in range(cols):
        val = im_contrasted.getpixel((x, y))
        if val < 36:
            ch = " "
        elif val < 65:
            ch = "." if (x + y) % 2 == 0 else " "
        else:
            idx = int((val / 255.0) * (len(char_ramp) - 1))
            ch = char_ramp[idx]
        line.append(ch)
    escaped_line = "".join(line).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    ascii_rows.append(escaped_line)

with open("assets/portrait_base64.txt", "r") as f:
    portrait_b64 = f.read().strip()

ascii_lines_dark = ""
ascii_lines_light = ""
start_y = 74
line_height = 9.2

for idx, line in enumerate(ascii_rows):
    curr_y = start_y + (idx * line_height)
    ascii_lines_dark += f'<text x="68" y="{curr_y:.1f}">{line}</text>\n        '
    ascii_lines_light += f'<text x="68" y="{curr_y:.1f}">{line}</text>\n        '

# 2. Build 1200x380 DARK BANNER (dark.svg)
dark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 380" width="100%" height="100%" role="img" aria-label="Babul Kumar — Developer Profile Banner" style="background:#090C11; font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <!-- Ambient Radial Glows -->
    <radialGradient id="radialCyan" cx="22%" cy="36%" r="42%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.08" />
      <stop offset="60%" stop-color="#00E5FF" stop-opacity="0.01" />
      <stop offset="100%" stop-color="#090C11" stop-opacity="0" />
    </radialGradient>
    
    <radialGradient id="radialViolet" cx="84%" cy="65%" r="38%">
      <stop offset="0%" stop-color="#6366F1" stop-opacity="0.06" />
      <stop offset="70%" stop-color="#6366F1" stop-opacity="0.01" />
      <stop offset="100%" stop-color="#090C11" stop-opacity="0" />
    </radialGradient>

    <!-- Portrait Duotone Gradients -->
    <linearGradient id="portraitGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.18" />
      <stop offset="40%" stop-color="#00E5FF" stop-opacity="0.03" />
      <stop offset="85%" stop-color="#090C11" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#090C11" stop-opacity="0.95" />
    </linearGradient>

    <!-- Terminal Background -->
    <linearGradient id="termBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0F141F" stop-opacity="0.94" />
      <stop offset="100%" stop-color="#0A0E17" stop-opacity="0.98" />
    </linearGradient>

    <!-- Name Gradient -->
    <linearGradient id="nameGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="75%" stop-color="#F1F5F9" />
      <stop offset="100%" stop-color="#00E5FF" />
    </linearGradient>

    <!-- Scanline -->
    <linearGradient id="scanlineGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0" />
      <stop offset="50%" stop-color="#00E5FF" stop-opacity="0.03" />
      <stop offset="100%" stop-color="#00E5FF" stop-opacity="0" />
    </linearGradient>

    <!-- Soft Grid Mask -->
    <linearGradient id="gridFade" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#FFF" stop-opacity="0.2" />
      <stop offset="90%" stop-color="#000" stop-opacity="0" />
    </linearGradient>
    <mask id="gridMask">
      <rect width="1200" height="380" fill="url(#gridFade)" />
    </mask>

    <!-- Portrait Clip -->
    <clipPath id="portraitClip">
      <path d="M 64 56 L 312 56 L 312 286 L 298 300 L 64 300 Z" />
    </clipPath>

    <!-- Terminal Clip -->
    <clipPath id="termClip">
      <rect x="360" y="154" width="780" height="174" />
    </clipPath>

    <!-- Animation Choreography -->
    <style><![CDATA[
      .anim-frame {{
        opacity: 0;
        animation: bootFadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.0s forwards;
      }}
      .anim-portrait {{
        opacity: 0;
        animation: bootScaleIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.3s forwards;
      }}
      .anim-name {{
        opacity: 0;
        animation: bootFadeSlide 0.55s cubic-bezier(0.16, 1, 0.3, 1) 0.6s forwards;
      }}
      .anim-headline {{
        opacity: 0;
        animation: bootFadeSlide 0.55s cubic-bezier(0.16, 1, 0.3, 1) 0.9s forwards;
      }}
      .anim-terminal {{
        opacity: 0;
        animation: bootFadeSlide 0.6s cubic-bezier(0.16, 1, 0.3, 1) 1.2s forwards;
      }}
      .line-1 {{ opacity: 0; animation: lineReveal 0.35s ease 1.35s forwards; }}
      .line-2 {{ opacity: 0; animation: lineReveal 0.35s ease 1.50s forwards; }}
      .line-3 {{ opacity: 0; animation: lineReveal 0.35s ease 1.65s forwards; }}
      .line-4 {{ opacity: 0; animation: lineReveal 0.35s ease 1.80s forwards; }}

      .idle-cursor {{
        opacity: 0;
        animation: lineReveal 0.2s ease 1.95s forwards, cursorBlink 0.95s step-end 2.05s infinite;
      }}
      .idle-pulse {{
        animation: pulseDot 2.8s ease-in-out infinite;
      }}
      .idle-glow {{
        animation: glowDrift 5.2s ease-in-out infinite alternate;
      }}
      .idle-scanline {{
        animation: scanlineDrift 5s linear infinite;
      }}
      .idle-shimmer {{
        animation: portraitShimmer 4s ease-in-out infinite alternate;
      }}

      @keyframes bootFadeIn {{
        from {{ opacity: 0; }} to {{ opacity: 1; }}
      }}
      @keyframes bootFadeSlide {{
        from {{ opacity: 0; transform: translateY(6px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes bootScaleIn {{
        from {{ opacity: 0; transform: scale(0.98); }}
        to {{ opacity: 1; transform: scale(1); }}
      }}
      @keyframes lineReveal {{
        from {{ opacity: 0; }} to {{ opacity: 1; }}
      }}
      @keyframes cursorBlink {{
        0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }}
      }}
      @keyframes pulseDot {{
        0%, 100% {{ opacity: 0.95; transform: scale(1); }}
        50% {{ opacity: 0.35; transform: scale(0.85); }}
      }}
      @keyframes glowDrift {{
        0% {{ opacity: 0.7; transform: translate(0, 0); }}
        100% {{ opacity: 1.0; transform: translate(10px, -5px); }}
      }}
      @keyframes scanlineDrift {{
        0% {{ transform: translateY(0px); opacity: 0.02; }}
        50% {{ opacity: 0.04; }}
        100% {{ transform: translateY(140px); opacity: 0.02; }}
      }}
      @keyframes portraitShimmer {{
        0% {{ opacity: 0.25; }}
        100% {{ opacity: 0.42; }}
      }}
    ]]></style>
  </defs>

  <!-- Background -->
  <rect width="1200" height="380" fill="#090C11" />
  <circle class="idle-glow" cx="260" cy="190" r="280" fill="url(#radialCyan)" />
  <circle class="idle-glow" cx="960" cy="260" r="300" fill="url(#radialViolet)" />

  <!-- Grid -->
  <g mask="url(#gridMask)" stroke="#38BDF8" stroke-opacity="0.03" stroke-width="1">
    <line x1="40" y1="46" x2="1140" y2="46" />
    <line x1="40" y1="106" x2="850" y2="106" />
    <line x1="40" y1="166" x2="680" y2="166" />
    <line x1="40" y1="226" x2="580" y2="226" />
    <line x1="40" y1="286" x2="720" y2="286" />
    <line x1="40" y1="334" x2="1140" y2="334" />

    <line x1="50" y1="26" x2="50" y2="354" />
    <line x1="160" y1="26" x2="160" y2="354" />
    <line x1="330" y1="26" x2="330" y2="354" />
    <line x1="500" y1="26" x2="500" y2="240" />
    <line x1="720" y1="26" x2="720" y2="180" />
    <line x1="1148" y1="26" x2="1148" y2="354" />
  </g>

  <!-- Corner Marks -->
  <g stroke="#00E5FF" stroke-opacity="0.18" stroke-width="1">
    <path d="M 47 38 h 6 M 50 35 v 6" />
    <path d="M 1145 38 h 6 M 1148 35 v 6" />
    <path d="M 47 342 h 6 M 50 339 v 6" />
    <path d="M 1145 342 h 6 M 1148 339 v 6" />
  </g>

  <!-- Outer Frame -->
  <g class="anim-frame">
    <rect x="36" y="24" width="1128" height="332" fill="none" stroke="#1E293B" stroke-opacity="0.5" stroke-width="1" />
    <path d="M 32 24 h 10 M 36 20 v 10" stroke="#00E5FF" stroke-opacity="0.4" stroke-width="1.2" />
    <path d="M 1158 24 h 10 M 1164 20 v 10" stroke="#64748B" stroke-opacity="0.3" stroke-width="1" />
    <path d="M 32 356 h 10 M 36 352 v 10" stroke="#64748B" stroke-opacity="0.3" stroke-width="1" />
    <path d="M 1158 356 h 10 M 1164 352 v 10" stroke="#00E5FF" stroke-opacity="0.4" stroke-width="1.2" />
  </g>

  <!-- Left Focal Anchor: Portrait with Tasteful Technical ASCII Texture -->
  <g class="anim-portrait">
    <line x1="54" y1="52" x2="54" y2="328" stroke="#00E5FF" stroke-opacity="0.18" stroke-width="1" stroke-dasharray="110 5 20 4" />
    <rect x="60" y="52" width="256" height="252" fill="#0C1017" stroke="#1E293B" stroke-opacity="0.8" stroke-width="1" />
    <path d="M 56 68 v -18 h 18" fill="none" stroke="#00E5FF" stroke-width="1.5" />
    <path d="M 320 290 v 18 h -18" fill="none" stroke="#00E5FF" stroke-opacity="0.6" stroke-width="1.5" />

    <!-- Clipped Portrait with Photographic Likeness and Subtle ASCII Overlay -->
    <g clip-path="url(#portraitClip)">
      <image href="data:image/jpeg;base64,{portrait_b64}" x="64" y="56" width="248" height="244" preserveAspectRatio="xMidYMid slice" opacity="0.9" />
      <rect x="64" y="56" width="248" height="244" fill="url(#portraitGlow)" />
      
      <!-- Monospaced ASCII Character Texture Overlay -->
      <g class="idle-shimmer" font-family="'JetBrains Mono', monospace" font-size="7.6" fill="#38BDF8" letter-spacing="0.5" pointer-events="none">
        {ascii_lines_dark}
      </g>
    </g>

    <!-- Status Bar Below Portrait -->
    <rect x="60" y="278" width="256" height="28" fill="#090D14" fill-opacity="0.94" stroke="#1E293B" stroke-width="1" />
    <circle class="idle-pulse" cx="74" cy="292" r="3" fill="#10B981" />
    <text x="84" y="295" fill="#E2E8F0" font-size="9" font-weight="500" letter-spacing="0.8" font-family="'JetBrains Mono', monospace">babul@workspace</text>
    <text x="250" y="295" fill="#64748B" font-size="8.5" font-family="'JetBrains Mono', monospace">builder</text>
  </g>

  <!-- Right Section: Identity + Terminal -->
  <g transform="translate(360, 0)">
    
    <!-- Identity -->
    <g class="anim-name">
      <text x="0" y="80" fill="url(#nameGradient)" font-size="38" font-weight="800" letter-spacing="-0.02em">BABUL KUMAR</text>
    </g>
    <g class="anim-headline">
      <text x="2" y="104" fill="#00E5FF" font-size="10.5" font-weight="600" letter-spacing="1.4" font-family="'JetBrains Mono', monospace">Computer Science &amp; Engineering &#8226; AI/ML &#8226; Full-Stack</text>
      <text x="2" y="128" fill="#94A3B8" font-size="12.5" font-weight="400" letter-spacing="0.01em">Building software, experimenting with AI, and turning ideas into working systems.</text>
    </g>

    <!-- Personal Developer Terminal Card -->
    <g class="anim-terminal" transform="translate(0, 146)">
      <rect width="780" height="182" rx="6" fill="url(#termBg)" stroke="#1E293B" stroke-width="1" />
      
      <!-- Titlebar -->
      <rect width="780" height="28" rx="6" fill="#0C1017" />
      <line x1="0" y1="28" x2="780" y2="28" stroke="#1E293B" stroke-width="1" />
      
      <circle cx="16" cy="14" r="3" fill="#EF4444" fill-opacity="0.6" />
      <circle cx="28" cy="14" r="3" fill="#F59E0B" fill-opacity="0.6" />
      <circle cx="40" cy="14" r="3" fill="#10B981" fill-opacity="0.6" />
      
      <text x="56" y="18" fill="#475569" font-size="9" font-family="'JetBrains Mono', monospace">~/babul-kumar &#8226; main</text>

      <g clip-path="url(#termClip)">
        <rect class="idle-scanline" x="1" y="29" width="778" height="20" fill="url(#scanlineGrad)" pointer-events="none" />
      </g>

      <!-- Terminal Lines -->
      <g transform="translate(18, 46)" font-family="'JetBrains Mono', monospace" font-size="11">
        <g class="line-1">
          <text x="0" y="0" fill="#00E5FF">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#A5B4FC">~</text>
          <text x="96" y="0" fill="#F1F5F9">$ whoami</text>
          
          <text x="0" y="16" fill="#E2E8F0" font-weight="500">babul-kumar</text>
        </g>

        <g class="line-2" transform="translate(0, 36)">
          <text x="0" y="0" fill="#00E5FF">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#A5B4FC">~</text>
          <text x="96" y="0" fill="#F1F5F9">$ focus</text>
          
          <text x="0" y="16" fill="#94A3B8">AI / ML &#8226; Full-Stack Development &#8226; Systems</text>
        </g>

        <g class="line-3" transform="translate(0, 72)">
          <text x="0" y="0" fill="#00E5FF">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#A5B4FC">~</text>
          <text x="96" y="0" fill="#F1F5F9">$ status</text>
          
          <text x="0" y="16" fill="#10B981">building software &#8226; 26 active repositories</text>
        </g>

        <g class="line-4" transform="translate(0, 108)">
          <text x="0" y="0" fill="#00E5FF">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#A5B4FC">~</text>
          <text x="96" y="0" fill="#F1F5F9">$</text>
          <rect class="idle-cursor" x="110" y="-10" width="7" height="13" fill="#00E5FF" />
        </g>
      </g>
    </g>
  </g>
</svg>'''

# 3. Build 1200x380 LIGHT BANNER (light.svg)
light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 380" width="100%" height="100%" role="img" aria-label="Babul Kumar — Developer Profile Banner" style="background:#FFFFFF; font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <!-- Ambient Radial Lighting for Light Theme -->
    <radialGradient id="lightRadialCyan" cx="22%" cy="36%" r="42%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.06" />
      <stop offset="60%" stop-color="#0284C7" stop-opacity="0.01" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0" />
    </radialGradient>
    
    <radialGradient id="lightRadialIndigo" cx="84%" cy="65%" r="38%">
      <stop offset="0%" stop-color="#4F46E5" stop-opacity="0.04" />
      <stop offset="70%" stop-color="#4F46E5" stop-opacity="0.01" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0" />
    </radialGradient>

    <!-- Portrait Light Overlay -->
    <linearGradient id="portraitGlowLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.12" />
      <stop offset="40%" stop-color="#0284C7" stop-opacity="0.02" />
      <stop offset="85%" stop-color="#F8FAFC" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.9" />
    </linearGradient>

    <!-- Terminal Background (GitHub Light Canvas) -->
    <linearGradient id="termBgLight" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC" stop-opacity="0.98" />
      <stop offset="100%" stop-color="#F1F5F9" stop-opacity="0.99" />
    </linearGradient>

    <!-- Portrait Clip -->
    <clipPath id="portraitClipLight">
      <path d="M 64 56 L 312 56 L 312 286 L 298 300 L 64 300 Z" />
    </clipPath>

    <!-- Animation Choreography -->
    <style><![CDATA[
      .anim-frame {{
        opacity: 0;
        animation: bootFadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.0s forwards;
      }}
      .anim-portrait {{
        opacity: 0;
        animation: bootScaleIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.3s forwards;
      }}
      .anim-name {{
        opacity: 0;
        animation: bootFadeSlide 0.55s cubic-bezier(0.16, 1, 0.3, 1) 0.6s forwards;
      }}
      .anim-headline {{
        opacity: 0;
        animation: bootFadeSlide 0.55s cubic-bezier(0.16, 1, 0.3, 1) 0.9s forwards;
      }}
      .anim-terminal {{
        opacity: 0;
        animation: bootFadeSlide 0.6s cubic-bezier(0.16, 1, 0.3, 1) 1.2s forwards;
      }}
      .line-1 {{ opacity: 0; animation: lineReveal 0.35s ease 1.35s forwards; }}
      .line-2 {{ opacity: 0; animation: lineReveal 0.35s ease 1.50s forwards; }}
      .line-3 {{ opacity: 0; animation: lineReveal 0.35s ease 1.65s forwards; }}
      .line-4 {{ opacity: 0; animation: lineReveal 0.35s ease 1.80s forwards; }}

      .idle-cursor {{
        opacity: 0;
        animation: lineReveal 0.2s ease 1.95s forwards, cursorBlink 0.95s step-end 2.05s infinite;
      }}
      .idle-pulse {{
        animation: pulseDot 2.8s ease-in-out infinite;
      }}

      @keyframes bootFadeIn {{
        from {{ opacity: 0; }} to {{ opacity: 1; }}
      }}
      @keyframes bootFadeSlide {{
        from {{ opacity: 0; transform: translateY(6px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes bootScaleIn {{
        from {{ opacity: 0; transform: scale(0.98); }}
        to {{ opacity: 1; transform: scale(1); }}
      }}
      @keyframes lineReveal {{
        from {{ opacity: 0; }} to {{ opacity: 1; }}
      }}
      @keyframes cursorBlink {{
        0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }}
      }}
      @keyframes pulseDot {{
        0%, 100% {{ opacity: 0.95; transform: scale(1); }}
        50% {{ opacity: 0.35; transform: scale(0.85); }}
      }}
    ]]></style>
  </defs>

  <!-- Background -->
  <rect width="1200" height="380" fill="#FFFFFF" />
  <circle cx="260" cy="190" r="280" fill="url(#lightRadialCyan)" />
  <circle cx="960" cy="260" r="300" fill="url(#lightRadialIndigo)" />

  <!-- Grid -->
  <g stroke="#0284C7" stroke-opacity="0.05" stroke-width="1">
    <line x1="40" y1="46" x2="1140" y2="46" />
    <line x1="40" y1="106" x2="850" y2="106" />
    <line x1="40" y1="166" x2="680" y2="166" />
    <line x1="40" y1="226" x2="580" y2="226" />
    <line x1="40" y1="286" x2="720" y2="286" />
    <line x1="40" y1="334" x2="1140" y2="334" />

    <line x1="50" y1="26" x2="50" y2="354" />
    <line x1="160" y1="26" x2="160" y2="354" />
    <line x1="330" y1="26" x2="330" y2="354" />
    <line x1="500" y1="26" x2="500" y2="240" />
    <line x1="720" y1="26" x2="720" y2="180" />
    <line x1="1148" y1="26" x2="1148" y2="354" />
  </g>

  <!-- Corner Marks -->
  <g stroke="#0284C7" stroke-opacity="0.3" stroke-width="1">
    <path d="M 47 38 h 6 M 50 35 v 6" />
    <path d="M 1145 38 h 6 M 1148 35 v 6" />
    <path d="M 47 342 h 6 M 50 339 v 6" />
    <path d="M 1145 342 h 6 M 1148 339 v 6" />
  </g>

  <!-- Outer Frame -->
  <g class="anim-frame">
    <rect x="36" y="24" width="1128" height="332" fill="none" stroke="#E2E8F0" stroke-width="1" />
    <path d="M 32 24 h 10 M 36 20 v 10" stroke="#0284C7" stroke-width="1.2" />
    <path d="M 1158 24 h 10 M 1164 20 v 10" stroke="#94A3B8" stroke-width="1" />
    <path d="M 32 356 h 10 M 36 352 v 10" stroke="#94A3B8" stroke-width="1" />
    <path d="M 1158 356 h 10 M 1164 352 v 10" stroke="#0284C7" stroke-width="1.2" />
  </g>

  <!-- Left Focal Anchor: Portrait with Tasteful Technical ASCII Texture -->
  <g class="anim-portrait">
    <line x1="54" y1="52" x2="54" y2="328" stroke="#0284C7" stroke-opacity="0.25" stroke-width="1" stroke-dasharray="110 5 20 4" />
    <rect x="60" y="52" width="256" height="252" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1" />
    <path d="M 56 68 v -18 h 18" fill="none" stroke="#0284C7" stroke-width="1.5" />
    <path d="M 320 290 v 18 h -18" fill="none" stroke="#0284C7" stroke-opacity="0.7" stroke-width="1.5" />

    <!-- Clipped Portrait with Photographic Likeness and Subtle ASCII Overlay -->
    <g clip-path="url(#portraitClipLight)">
      <image href="data:image/jpeg;base64,{portrait_b64}" x="64" y="56" width="248" height="244" preserveAspectRatio="xMidYMid slice" opacity="0.92" />
      <rect x="64" y="56" width="248" height="244" fill="url(#portraitGlowLight)" />
      
      <!-- Monospaced ASCII Character Texture Overlay -->
      <g font-family="'JetBrains Mono', monospace" font-size="7.6" fill="#0369A1" opacity="0.32" letter-spacing="0.5" pointer-events="none">
        {ascii_lines_light}
      </g>
    </g>

    <!-- Status Bar Below Portrait -->
    <rect x="60" y="278" width="256" height="28" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1" />
    <circle class="idle-pulse" cx="74" cy="292" r="3" fill="#059669" />
    <text x="84" y="295" fill="#1E293B" font-size="9" font-weight="500" letter-spacing="0.8" font-family="'JetBrains Mono', monospace">babul@workspace</text>
    <text x="250" y="295" fill="#64748B" font-size="8.5" font-family="'JetBrains Mono', monospace">builder</text>
  </g>

  <!-- Right Section: Identity + Terminal -->
  <g transform="translate(360, 0)">
    
    <!-- Identity -->
    <g class="anim-name">
      <text x="0" y="80" fill="#0F172A" font-size="38" font-weight="800" letter-spacing="-0.02em">BABUL KUMAR</text>
    </g>
    <g class="anim-headline">
      <text x="2" y="104" fill="#0284C7" font-size="10.5" font-weight="600" letter-spacing="1.4" font-family="'JetBrains Mono', monospace">Computer Science &amp; Engineering &#8226; AI/ML &#8226; Full-Stack</text>
      <text x="2" y="128" fill="#475569" font-size="12.5" font-weight="400" letter-spacing="0.01em">Building software, experimenting with AI, and turning ideas into working systems.</text>
    </g>

    <!-- Personal Developer Terminal Card -->
    <g class="anim-terminal" transform="translate(0, 146)">
      <rect width="780" height="182" rx="6" fill="url(#termBgLight)" stroke="#D0D7DE" stroke-width="1" />
      
      <!-- Titlebar -->
      <rect width="780" height="28" rx="6" fill="#E2E8F0" />
      <line x1="0" y1="28" x2="780" y2="28" stroke="#CBD5E1" stroke-width="1" />
      
      <circle cx="16" cy="14" r="3" fill="#EF4444" fill-opacity="0.8" />
      <circle cx="28" cy="14" r="3" fill="#F59E0B" fill-opacity="0.8" />
      <circle cx="40" cy="14" r="3" fill="#10B981" fill-opacity="0.8" />
      
      <text x="56" y="18" fill="#64748B" font-size="9" font-family="'JetBrains Mono', monospace">~/babul-kumar &#8226; main</text>

      <!-- Terminal Lines -->
      <g transform="translate(18, 46)" font-family="'JetBrains Mono', monospace" font-size="11">
        <g class="line-1">
          <text x="0" y="0" fill="#0284C7">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#4F46E5">~</text>
          <text x="96" y="0" fill="#0F172A">$ whoami</text>
          
          <text x="0" y="16" fill="#1E293B" font-weight="500">babul-kumar</text>
        </g>

        <g class="line-2" transform="translate(0, 36)">
          <text x="0" y="0" fill="#0284C7">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#4F46E5">~</text>
          <text x="96" y="0" fill="#0F172A">$ focus</text>
          
          <text x="0" y="16" fill="#475569">AI / ML &#8226; Full-Stack Development &#8226; Systems</text>
        </g>

        <g class="line-3" transform="translate(0, 72)">
          <text x="0" y="0" fill="#0284C7">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#4F46E5">~</text>
          <text x="96" y="0" fill="#0F172A">$ status</text>
          
          <text x="0" y="16" fill="#059669">building software &#8226; 26 active repositories</text>
        </g>

        <g class="line-4" transform="translate(0, 108)">
          <text x="0" y="0" fill="#0284C7">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#4F46E5">~</text>
          <text x="96" y="0" fill="#0F172A">$</text>
          <rect class="idle-cursor" x="110" y="-10" width="7" height="13" fill="#0284C7" />
        </g>
      </g>
    </g>
  </g>
</svg>'''

# 4. Write primary outputs (dark.svg and light.svg at root as specified in Phase 19/22)
with open("dark.svg", "w", encoding="utf-8") as f:
    f.write(dark_svg)

with open("light.svg", "w", encoding="utf-8") as f:
    f.write(light_svg)

# Write backwards-compatible aliases
with open("banner-dark.svg", "w", encoding="utf-8") as f:
    f.write(dark_svg)

with open("banner-light.svg", "w", encoding="utf-8") as f:
    f.write(light_svg)

with open("banner.svg", "w", encoding="utf-8") as f:
    f.write(dark_svg)

# Also write to assets/ for backwards-compatible paths
os.makedirs("assets", exist_ok=True)
shutil.copyfile("dark.svg", "assets/dark.svg")
shutil.copyfile("light.svg", "assets/light.svg")
shutil.copyfile("dark.svg", "assets/banner-dark.svg")
shutil.copyfile("light.svg", "assets/banner-light.svg")

print("Generated dark.svg, light.svg, and aliases successfully!")
