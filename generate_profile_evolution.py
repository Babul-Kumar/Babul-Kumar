"""
generate_profile_evolution.py
Generates the complete set of premium SVG assets for Babul Kumar's GitHub Profile:
1. dark.svg (Hero Dark, 1200x420)
2. light.svg (Hero Light, 1200x420)
3. assets/journey.svg (Engineering Journey Timeline, 1200x210)
4. assets/systems-architecture.svg (Vision Perception & Telemetry System Flow, 1200x260)
5. assets/github-telemetry.svg (Verified GitHub Telemetry Card, 1200x280)
6. assets/contribution-activity.svg (Real GitHub Contribution Matrix, 1200x195)
7. assets/github-contribution-snake.svg (Animated Contribution Snake, 1200x220)
"""

import os
import json
import base64
from PIL import Image, ImageEnhance

os.makedirs("assets", exist_ok=True)

# -------------------------------------------------------------
# 1. LOAD PORTRAIT AND GENERATE REFINED ASCII OVERLAY
# -------------------------------------------------------------
print("Generating refined portrait and ASCII layer...")
portrait_path = "assets/portrait_processed.jpg"
if not os.path.exists(portrait_path):
    portrait_path = "assets/Babulprofile.jpeg"

im = Image.open(portrait_path).convert("L")
cols = 36
rows = 26
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

start_y = 74
line_height = 9.8
ascii_lines_dark = ""
ascii_lines_light = ""
for idx, line in enumerate(ascii_rows):
    curr_y = start_y + (idx * line_height)
    ascii_lines_dark += f'<text x="68" y="{curr_y:.1f}">{line}</text>\n        '
    ascii_lines_light += f'<text x="68" y="{curr_y:.1f}">{line}</text>\n        '

# -------------------------------------------------------------
# 2. HERO DARK (dark.svg) - 1200 x 420
# -------------------------------------------------------------
print("Building Hero dark.svg (1200x420)...")
hero_dark_template = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="100%" height="100%" role="img" aria-label="Babul Kumar — Developer Profile Banner" style="background:#090C11; font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <!-- Radial Ambient Lighting -->
    <radialGradient id="radialCyan" cx="20%" cy="35%" r="45%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.09" />
      <stop offset="60%" stop-color="#00E5FF" stop-opacity="0.01" />
      <stop offset="100%" stop-color="#090C11" stop-opacity="0" />
    </radialGradient>
    
    <radialGradient id="radialViolet" cx="82%" cy="65%" r="40%">
      <stop offset="0%" stop-color="#6366F1" stop-opacity="0.07" />
      <stop offset="70%" stop-color="#6366F1" stop-opacity="0.01" />
      <stop offset="100%" stop-color="#090C11" stop-opacity="0" />
    </radialGradient>

    <!-- Portrait Gradient Duotone -->
    <linearGradient id="portraitGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.16" />
      <stop offset="45%" stop-color="#00E5FF" stop-opacity="0.02" />
      <stop offset="85%" stop-color="#090C11" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#090C11" stop-opacity="0.95" />
    </linearGradient>

    <!-- Terminal Gradient -->
    <linearGradient id="termBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0E131E" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#0A0E17" stop-opacity="0.98" />
    </linearGradient>

    <!-- Text Highlight Gradient -->
    <linearGradient id="nameGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="70%" stop-color="#F1F5F9" />
      <stop offset="100%" stop-color="#38BDF8" />
    </linearGradient>

    <!-- Portrait Clip (Chamfered Corner) -->
    <clipPath id="portraitClip">
      <path d="M 64 54 L 324 54 L 324 322 L 306 340 L 64 340 Z" />
    </clipPath>

    <!-- Terminal Clip -->
    <clipPath id="termClip">
      <rect x="372" y="176" width="768" height="196" rx="6" />
    </clipPath>

    <!-- Styles & Animation Choreography -->
    <style><![CDATA[
      .anim-frame {
        opacity: 0;
        animation: bootFadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.0s forwards;
      }
      .anim-portrait {
        opacity: 0;
        animation: bootScaleIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.25s forwards;
      }
      .anim-ascii {
        opacity: 0;
        animation: bootFadeIn 0.5s ease 0.5s forwards;
      }
      .anim-name {
        opacity: 0;
        animation: bootFadeSlide 0.55s cubic-bezier(0.16, 1, 0.3, 1) 0.75s forwards;
      }
      .anim-role {
        opacity: 0;
        animation: bootFadeSlide 0.55s cubic-bezier(0.16, 1, 0.3, 1) 1.0s forwards;
      }
      .anim-desc {
        opacity: 0;
        animation: bootFadeSlide 0.55s cubic-bezier(0.16, 1, 0.3, 1) 1.25s forwards;
      }
      .anim-terminal {
        opacity: 0;
        animation: bootFadeSlide 0.6s cubic-bezier(0.16, 1, 0.3, 1) 1.5s forwards;
      }
      .line-1 { opacity: 0; animation: lineReveal 0.3s ease 1.65s forwards; }
      .line-2 { opacity: 0; animation: lineReveal 0.3s ease 1.80s forwards; }
      .line-3 { opacity: 0; animation: lineReveal 0.3s ease 1.95s forwards; }
      .line-4 { opacity: 0; animation: lineReveal 0.3s ease 2.10s forwards; }

      .idle-cursor {
        opacity: 0;
        animation: lineReveal 0.2s ease 2.2s forwards, cursorBlink 1s step-end 2.2s infinite;
      }
      .idle-pulse {
        animation: pulseDot 3s ease-in-out infinite;
      }
      .idle-glow {
        animation: glowDrift 6s ease-in-out infinite alternate;
      }
      .idle-shimmer {
        animation: portraitShimmer 4s ease-in-out infinite alternate;
      }

      @keyframes bootFadeIn {
        from { opacity: 0; } to { opacity: 1; }
      }
      @keyframes bootFadeSlide {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
      }
      @keyframes bootScaleIn {
        from { opacity: 0; transform: scale(0.98); }
        to { opacity: 1; transform: scale(1); }
      }
      @keyframes lineReveal {
        from { opacity: 0; } to { opacity: 1; }
      }
      @keyframes cursorBlink {
        0%, 100% { opacity: 1; } 50% { opacity: 0; }
      }
      @keyframes pulseDot {
        0%, 100% { opacity: 0.95; transform: scale(1); }
        50% { opacity: 0.35; transform: scale(0.85); }
      }
      @keyframes glowDrift {
        0% { opacity: 0.7; transform: translate(0, 0); }
        100% { opacity: 1.0; transform: translate(12px, -6px); }
      }
      @keyframes portraitShimmer {
        0% { opacity: 0.22; }
        100% { opacity: 0.38; }
      }
    ]]></style>
  </defs>

  <!-- Canvas Background -->
  <rect width="1200" height="420" fill="#090C11" />
  <circle class="idle-glow" cx="240" cy="210" r="300" fill="url(#radialCyan)" />
  <circle class="idle-glow" cx="980" cy="280" r="320" fill="url(#radialViolet)" />

  <!-- Ambient Blueprint Grid -->
  <g stroke="#38BDF8" stroke-opacity="0.03" stroke-width="1">
    <line x1="40" y1="46" x2="1160" y2="46" />
    <line x1="40" y1="116" x2="850" y2="116" />
    <line x1="40" y1="186" x2="700" y2="186" />
    <line x1="40" y1="256" x2="600" y2="256" />
    <line x1="40" y1="326" x2="720" y2="326" />
    <line x1="40" y1="384" x2="1160" y2="384" />

    <line x1="48" y1="26" x2="48" y2="394" />
    <line x1="160" y1="26" x2="160" y2="394" />
    <line x1="344" y1="26" x2="344" y2="394" />
    <line x1="520" y1="26" x2="520" y2="260" />
    <line x1="740" y1="26" x2="740" y2="200" />
    <line x1="1152" y1="26" x2="1152" y2="394" />
  </g>

  <!-- Outer Technical Frame -->
  <g class="anim-frame">
    <rect x="36" y="24" width="1128" height="372" fill="none" stroke="#1E293B" stroke-opacity="0.55" stroke-width="1" />
    <!-- Technical Corner Crosshairs -->
    <path d="M 30 24 h 12 M 36 18 v 12" stroke="#00E5FF" stroke-opacity="0.45" stroke-width="1.2" />
    <path d="M 1158 24 h 12 M 1164 18 v 12" stroke="#64748B" stroke-opacity="0.3" stroke-width="1" />
    <path d="M 30 396 h 12 M 36 390 v 12" stroke="#64748B" stroke-opacity="0.3" stroke-width="1" />
    <path d="M 1158 396 h 12 M 1164 390 v 12" stroke="#00E5FF" stroke-opacity="0.45" stroke-width="1.2" />
    
    <!-- Top System Label -->
    <text x="56" y="42" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9" letter-spacing="1.5">01 // DEVELOPER HERO &amp; VISUAL IDENTITY</text>
    <text x="1136" y="42" text-anchor="end" fill="#00E5FF" font-family="'JetBrains Mono', monospace" font-size="9" letter-spacing="1.5">SYSTEM ACTIVE</text>
  </g>

  <!-- Left Column: Photographic Portrait with Subtle ASCII Texture -->
  <g class="anim-portrait">
    <rect x="58" y="50" width="270" height="294" fill="#0C1017" stroke="#1E293B" stroke-opacity="0.8" stroke-width="1" />
    <path d="M 54 68 v -20 h 20" fill="none" stroke="#00E5FF" stroke-width="1.5" />
    <path d="M 332 326 v 20 h -20" fill="none" stroke="#00E5FF" stroke-opacity="0.6" stroke-width="1.5" />

    <!-- Clipped Portrait -->
    <g clip-path="url(#portraitClip)">
      <image href="data:image/jpeg;base64,__PORTRAIT_B64__"
             x="58" y="50" width="270" height="294"
             preserveAspectRatio="xMidYMid slice" />
      <rect x="58" y="50" width="270" height="294" fill="url(#portraitGlow)" />
      
      <!-- Subtle ASCII texture -->
      <g class="anim-ascii idle-shimmer" fill="#00E5FF" font-family="'JetBrains Mono', monospace" font-size="7.5" opacity="0.3">
        __ASCII_LINES__
      </g>
    </g>

    <!-- Portrait Metadata Footer -->
    <g transform="translate(60, 362)">
      <circle class="idle-pulse" cx="8" cy="8" r="3.5" fill="#10B981" />
      <text x="20" y="11" fill="#F1F5F9" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600">BABUL KUMAR</text>
      <text x="20" y="24" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9">PORTRAIT // ID_BK_2026</text>
    </g>
  </g>

  <!-- Right Column: Editorial Identity & Personal Statement -->
  <g transform="translate(372, 60)">
    <!-- Identity Header -->
    <g class="anim-name">
      <text x="0" y="32" fill="url(#nameGradient)" font-size="34" font-weight="800" letter-spacing="-0.8">Babul Kumar</text>
    </g>

    <!-- Discipline & Focus -->
    <g class="anim-role" transform="translate(0, 56)">
      <text x="0" y="0" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600" letter-spacing="1">COMPUTER SCIENCE &amp; ENGINEERING</text>
      <text x="264" y="0" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="11.5">&#8226;</text>
      <text x="280" y="0" fill="#94A3B8" font-family="'JetBrains Mono', monospace" font-size="11.5">AI / ML &amp; FULL-STACK SYSTEMS</text>
    </g>

    <!-- Short Personal Statement -->
    <g class="anim-desc" transform="translate(0, 84)">
      <text x="0" y="0" fill="#CBD5E1" font-size="14.5" font-weight="400" line-height="1.5">
        Building software, experimenting with AI, and turning ideas into working systems.
      </text>
      <text x="0" y="20" fill="#64748B" font-size="12.5" font-family="'JetBrains Mono', monospace">
        First-principles engineering &#8226; computer vision pipelines &#8226; system telemetry daemons
      </text>
    </g>

    <!-- Terminal Command Module -->
    <g class="anim-terminal" transform="translate(0, 116)">
      <!-- Terminal Frame -->
      <rect x="0" y="0" width="768" height="196" rx="6" fill="url(#termBg)" stroke="#1E293B" stroke-width="1" />
      
      <!-- Terminal Window Bar -->
      <path d="M 0 6 Q 0 0 6 0 L 762 0 Q 768 0 768 6 L 768 28 L 0 28 Z" fill="#0C1017" />
      <line x1="0" y1="28" x2="768" y2="28" stroke="#1E293B" stroke-width="1" />
      
      <!-- Window Controls -->
      <circle cx="16" cy="14" r="4.5" fill="#EF4444" opacity="0.8" />
      <circle cx="32" cy="14" r="4.5" fill="#F59E0B" opacity="0.8" />
      <circle cx="48" cy="14" r="4.5" fill="#10B981" opacity="0.8" />
      <text x="70" y="17" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="10">babul@dev-workstation: ~ (zsh)</text>
      <text x="752" y="17" text-anchor="end" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10">UTF-8</text>

      <!-- Terminal Body Lines -->
      <g font-family="'JetBrains Mono', monospace" font-size="11.5" transform="translate(20, 52)">
        <g class="line-1">
          <text x="0" y="0" fill="#00E5FF">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#A5B4FC">~</text>
          <text x="96" y="0" fill="#F1F5F9">$ whoami</text>
          <text x="0" y="18" fill="#94A3B8">CS student &amp; software builder exploring machine learning and systems</text>
        </g>

        <g class="line-2" transform="translate(0, 38)">
          <text x="0" y="0" fill="#00E5FF">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#A5B4FC">~</text>
          <text x="96" y="0" fill="#F1F5F9">$ focus --areas</text>
          <text x="0" y="18" fill="#38BDF8">Computer Vision &#8226; Deep Learning &#8226; Host Telemetry &#8226; Web Platforms</text>
        </g>

        <g class="line-3" transform="translate(0, 76)">
          <text x="0" y="0" fill="#00E5FF">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#A5B4FC">~</text>
          <text x="96" y="0" fill="#F1F5F9">$ git status --summary</text>
          <text x="0" y="18" fill="#10B981">27 public repositories &#8226; 248 total contributions &#8226; active builder</text>
        </g>

        <g class="line-4" transform="translate(0, 114)">
          <text x="0" y="0" fill="#00E5FF">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#A5B4FC">~</text>
          <text x="96" y="0" fill="#F1F5F9">$</text>
          <rect class="idle-cursor" x="110" y="-10" width="7" height="13" fill="#00E5FF" />
        </g>
      </g>
    </g>
  </g>
</svg>
'''
hero_dark_svg = hero_dark_template.replace("__PORTRAIT_B64__", portrait_b64).replace("__ASCII_LINES__", ascii_lines_dark)

with open("dark.svg", "w", encoding="utf-8") as f:
    f.write(hero_dark_svg)
with open("assets/dark.svg", "w", encoding="utf-8") as f:
    f.write(hero_dark_svg)

# -------------------------------------------------------------
# 3. HERO LIGHT (light.svg) - 1200 x 420
# -------------------------------------------------------------
print("Building Hero light.svg (1200x420)...")
hero_light_template = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="100%" height="100%" role="img" aria-label="Babul Kumar — Developer Profile Banner" style="background:#FFFFFF; font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <radialGradient id="lightRadialCyan" cx="20%" cy="35%" r="45%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.07" />
      <stop offset="60%" stop-color="#0284C7" stop-opacity="0.01" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0" />
    </radialGradient>
    
    <radialGradient id="lightRadialIndigo" cx="82%" cy="65%" r="40%">
      <stop offset="0%" stop-color="#4F46E5" stop-opacity="0.05" />
      <stop offset="70%" stop-color="#4F46E5" stop-opacity="0.01" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0" />
    </radialGradient>

    <linearGradient id="portraitGlowLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.12" />
      <stop offset="45%" stop-color="#0284C7" stop-opacity="0.02" />
      <stop offset="85%" stop-color="#F8FAFC" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.9" />
    </linearGradient>

    <linearGradient id="termBgLight" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC" stop-opacity="0.98" />
      <stop offset="100%" stop-color="#F1F5F9" stop-opacity="0.99" />
    </linearGradient>

    <clipPath id="portraitClipLight">
      <path d="M 64 54 L 324 54 L 324 322 L 306 340 L 64 340 Z" />
    </clipPath>

    <style><![CDATA[
      .anim-frame { opacity: 0; animation: bootFadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.0s forwards; }
      .anim-portrait { opacity: 0; animation: bootScaleIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.25s forwards; }
      .anim-ascii { opacity: 0; animation: bootFadeIn 0.5s ease 0.5s forwards; }
      .anim-name { opacity: 0; animation: bootFadeSlide 0.55s cubic-bezier(0.16, 1, 0.3, 1) 0.75s forwards; }
      .anim-role { opacity: 0; animation: bootFadeSlide 0.55s cubic-bezier(0.16, 1, 0.3, 1) 1.0s forwards; }
      .anim-desc { opacity: 0; animation: bootFadeSlide 0.55s cubic-bezier(0.16, 1, 0.3, 1) 1.25s forwards; }
      .anim-terminal { opacity: 0; animation: bootFadeSlide 0.6s cubic-bezier(0.16, 1, 0.3, 1) 1.5s forwards; }
      .line-1 { opacity: 0; animation: lineReveal 0.3s ease 1.65s forwards; }
      .line-2 { opacity: 0; animation: lineReveal 0.3s ease 1.80s forwards; }
      .line-3 { opacity: 0; animation: lineReveal 0.3s ease 1.95s forwards; }
      .line-4 { opacity: 0; animation: lineReveal 0.3s ease 2.10s forwards; }

      .idle-cursor {
        opacity: 0;
        animation: lineReveal 0.2s ease 2.2s forwards, cursorBlink 1s step-end 2.2s infinite;
      }
      .idle-pulse { animation: pulseDot 3s ease-in-out infinite; }
      .idle-glow { animation: glowDrift 6s ease-in-out infinite alternate; }
      .idle-shimmer { animation: portraitShimmer 4s ease-in-out infinite alternate; }

      @keyframes bootFadeIn { from { opacity: 0; } to { opacity: 1; } }
      @keyframes bootFadeSlide { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
      @keyframes bootScaleIn { from { opacity: 0; transform: scale(0.98); } to { opacity: 1; transform: scale(1); } }
      @keyframes lineReveal { from { opacity: 0; } to { opacity: 1; } }
      @keyframes cursorBlink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
      @keyframes pulseDot { 0%, 100% { opacity: 0.95; transform: scale(1); } 50% { opacity: 0.35; transform: scale(0.85); } }
      @keyframes glowDrift { 0% { opacity: 0.7; transform: translate(0, 0); } 100% { opacity: 1.0; transform: translate(12px, -6px); } }
      @keyframes portraitShimmer { 0% { opacity: 0.16; } 100% { opacity: 0.32; } }
    ]]></style>
  </defs>

  <rect width="1200" height="420" fill="#FFFFFF" />
  <circle class="idle-glow" cx="240" cy="210" r="300" fill="url(#lightRadialCyan)" />
  <circle class="idle-glow" cx="980" cy="280" r="320" fill="url(#lightRadialIndigo)" />

  <g stroke="#0284C7" stroke-opacity="0.04" stroke-width="1">
    <line x1="40" y1="46" x2="1160" y2="46" />
    <line x1="40" y1="116" x2="850" y2="116" />
    <line x1="40" y1="186" x2="700" y2="186" />
    <line x1="40" y1="256" x2="600" y2="256" />
    <line x1="40" y1="326" x2="720" y2="326" />
    <line x1="40" y1="384" x2="1160" y2="384" />

    <line x1="48" y1="26" x2="48" y2="394" />
    <line x1="160" y1="26" x2="160" y2="394" />
    <line x1="344" y1="26" x2="344" y2="394" />
    <line x1="520" y1="26" x2="520" y2="260" />
    <line x1="740" y1="26" x2="740" y2="200" />
    <line x1="1152" y1="26" x2="1152" y2="394" />
  </g>

  <g class="anim-frame">
    <rect x="36" y="24" width="1128" height="372" fill="none" stroke="#E2E8F0" stroke-width="1" />
    <path d="M 30 24 h 12 M 36 18 v 12" stroke="#0284C7" stroke-opacity="0.45" stroke-width="1.2" />
    <path d="M 1158 24 h 12 M 1164 18 v 12" stroke="#94A3B8" stroke-opacity="0.3" stroke-width="1" />
    <path d="M 30 396 h 12 M 36 390 v 12" stroke="#94A3B8" stroke-opacity="0.3" stroke-width="1" />
    <path d="M 1158 396 h 12 M 1164 390 v 12" stroke="#0284C7" stroke-opacity="0.45" stroke-width="1.2" />
    
    <text x="56" y="42" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9" letter-spacing="1.5">01 // DEVELOPER HERO &amp; VISUAL IDENTITY</text>
    <text x="1136" y="42" text-anchor="end" fill="#0284C7" font-family="'JetBrains Mono', monospace" font-size="9" letter-spacing="1.5">SYSTEM ACTIVE</text>
  </g>

  <g class="anim-portrait">
    <rect x="58" y="50" width="270" height="294" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1" />
    <path d="M 54 68 v -20 h 20" fill="none" stroke="#0284C7" stroke-width="1.5" />
    <path d="M 332 326 v 20 h -20" fill="none" stroke="#0284C7" stroke-opacity="0.6" stroke-width="1.5" />

    <g clip-path="url(#portraitClipLight)">
      <image href="data:image/jpeg;base64,__PORTRAIT_B64__"
             x="58" y="50" width="270" height="294"
             preserveAspectRatio="xMidYMid slice" />
      <rect x="58" y="50" width="270" height="294" fill="url(#portraitGlowLight)" />
      
      <g class="anim-ascii idle-shimmer" fill="#0284C7" font-family="'JetBrains Mono', monospace" font-size="7.5" opacity="0.25">
        __ASCII_LINES__
      </g>
    </g>

    <g transform="translate(60, 362)">
      <circle class="idle-pulse" cx="8" cy="8" r="3.5" fill="#059669" />
      <text x="20" y="11" fill="#0F172A" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600">BABUL KUMAR</text>
      <text x="20" y="24" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9">PORTRAIT // ID_BK_2026</text>
    </g>
  </g>

  <g transform="translate(372, 60)">
    <g class="anim-name">
      <text x="0" y="32" fill="#0F172A" font-size="34" font-weight="800" letter-spacing="-0.8">Babul Kumar</text>
    </g>

    <g class="anim-role" transform="translate(0, 56)">
      <text x="0" y="0" fill="#0284C7" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600" letter-spacing="1">COMPUTER SCIENCE &amp; ENGINEERING</text>
      <text x="264" y="0" fill="#CBD5E1" font-family="'JetBrains Mono', monospace" font-size="11.5">&#8226;</text>
      <text x="280" y="0" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="11.5">AI / ML &amp; FULL-STACK SYSTEMS</text>
    </g>

    <g class="anim-desc" transform="translate(0, 84)">
      <text x="0" y="0" fill="#334155" font-size="14.5" font-weight="400" line-height="1.5">
        Building software, experimenting with AI, and turning ideas into working systems.
      </text>
      <text x="0" y="20" fill="#64748B" font-size="12.5" font-family="'JetBrains Mono', monospace">
        First-principles engineering &#8226; computer vision pipelines &#8226; system telemetry daemons
      </text>
    </g>

    <g class="anim-terminal" transform="translate(0, 116)">
      <rect x="0" y="0" width="768" height="196" rx="6" fill="url(#termBgLight)" stroke="#CBD5E1" stroke-width="1" />
      
      <path d="M 0 6 Q 0 0 6 0 L 762 0 Q 768 0 768 6 L 768 28 L 0 28 Z" fill="#E2E8F0" />
      <line x1="0" y1="28" x2="768" y2="28" stroke="#CBD5E1" stroke-width="1" />
      
      <circle cx="16" cy="14" r="4.5" fill="#EF4444" opacity="0.8" />
      <circle cx="32" cy="14" r="4.5" fill="#F59E0B" opacity="0.8" />
      <circle cx="48" cy="14" r="4.5" fill="#10B981" opacity="0.8" />
      <text x="70" y="17" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10">babul@dev-workstation: ~ (zsh)</text>
      <text x="752" y="17" text-anchor="end" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="10">UTF-8</text>

      <g font-family="'JetBrains Mono', monospace" font-size="11.5" transform="translate(20, 52)">
        <g class="line-1">
          <text x="0" y="0" fill="#0284C7">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#4F46E5">~</text>
          <text x="96" y="0" fill="#0F172A">$ whoami</text>
          <text x="0" y="18" fill="#475569">CS student &amp; software builder exploring machine learning and systems</text>
        </g>

        <g class="line-2" transform="translate(0, 38)">
          <text x="0" y="0" fill="#0284C7">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#4F46E5">~</text>
          <text x="96" y="0" fill="#0F172A">$ focus --areas</text>
          <text x="0" y="18" fill="#0369A1">Computer Vision &#8226; Deep Learning &#8226; Host Telemetry &#8226; Web Platforms</text>
        </g>

        <g class="line-3" transform="translate(0, 76)">
          <text x="0" y="0" fill="#0284C7">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#4F46E5">~</text>
          <text x="96" y="0" fill="#0F172A">$ git status --summary</text>
          <text x="0" y="18" fill="#059669">27 public repositories &#8226; 248 total contributions &#8226; active builder</text>
        </g>

        <g class="line-4" transform="translate(0, 114)">
          <text x="0" y="0" fill="#0284C7">babul@dev</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#4F46E5">~</text>
          <text x="96" y="0" fill="#0F172A">$</text>
          <rect class="idle-cursor" x="110" y="-10" width="7" height="13" fill="#0284C7" />
        </g>
      </g>
    </g>
  </g>
</svg>
'''
hero_light_svg = hero_light_template.replace("__PORTRAIT_B64__", portrait_b64).replace("__ASCII_LINES__", ascii_lines_light)

with open("light.svg", "w", encoding="utf-8") as f:
    f.write(hero_light_svg)
with open("assets/light.svg", "w", encoding="utf-8") as f:
    f.write(hero_light_svg)

# -------------------------------------------------------------
# 4. SECTION 03 — ENGINEERING JOURNEY (assets/journey.svg)
# -------------------------------------------------------------
print("Building Engineering Journey SVG...")
journey_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 210" width="100%" height="100%" role="img" aria-label="Babul Kumar — Engineering Journey Timeline" style="background:#090C11; font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.3" />
      <stop offset="50%" stop-color="#00E5FF" />
      <stop offset="100%" stop-color="#6366F1" />
    </linearGradient>

    <style><![CDATA[
      .timeline-base {
        stroke-dasharray: 1040;
        stroke-dashoffset: 1040;
        animation: drawLine 1.8s cubic-bezier(0.16, 1, 0.3, 1) 0.2s forwards;
      }
      .node-1 { opacity: 0; animation: nodePop 0.5s ease 0.6s forwards; }
      .node-2 { opacity: 0; animation: nodePop 0.5s ease 1.1s forwards; }
      .node-3 { opacity: 0; animation: nodePop 0.5s ease 1.6s forwards; }
      
      .pulse-glow { animation: pulseAnim 2.5s infinite; }

      @keyframes drawLine {
        to { stroke-dashoffset: 0; }
      }
      @keyframes nodePop {
        0% { opacity: 0; transform: translateY(6px); }
        100% { opacity: 1; transform: translateY(0); }
      }
      @keyframes pulseAnim {
        0%, 100% { r: 5; opacity: 1; }
        50% { r: 8; opacity: 0.4; }
      }
    ]]></style>
  </defs>

  <rect width="1200" height="210" fill="#090C11" />
  <rect x="36" y="16" width="1128" height="178" rx="6" fill="#0C1017" stroke="#1E293B" stroke-width="1" />

  <!-- Technical Header -->
  <text x="56" y="38" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9" letter-spacing="1.5">02 // PROGRESSION TIMELINE &amp; ARCHITECTURAL MILESTONES</text>
  <text x="1144" y="38" text-anchor="end" fill="#00E5FF" font-family="'JetBrains Mono', monospace" font-size="9">CHRONO-SERIES // 2024 - 2026</text>

  <!-- Horizontal Axis Line -->
  <line class="timeline-base" x1="80" y1="84" x2="1120" y2="84" stroke="url(#lineGrad)" stroke-width="2" />

  <!-- MILESTONE 1: 2024 -->
  <g class="node-1" transform="translate(140, 0)">
    <line x1="0" y1="84" x2="0" y2="70" stroke="#00E5FF" stroke-width="1" stroke-dasharray="2 2" />
    <circle cx="0" cy="84" r="5" fill="#00E5FF" />
    <circle class="pulse-glow" cx="0" cy="84" r="6" fill="none" stroke="#00E5FF" stroke-width="1.5" />
    <text x="0" y="62" text-anchor="middle" fill="#00E5FF" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700">2024</text>
    
    <text x="0" y="112" text-anchor="middle" fill="#F1F5F9" font-size="13" font-weight="600">Foundations &amp; First Repositories</text>
    <text x="0" y="130" text-anchor="middle" fill="#94A3B8" font-size="11">Computer Science &amp; Engineering journey begins</text>
    <text x="0" y="146" text-anchor="middle" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="10">Core Algorithms &#8226; C/C++ &#8226; Basic Web Utilities</text>
  </g>

  <!-- MILESTONE 2: 2025 -->
  <g class="node-2" transform="translate(560, 0)">
    <line x1="0" y1="84" x2="0" y2="70" stroke="#38BDF8" stroke-width="1" stroke-dasharray="2 2" />
    <circle cx="0" cy="84" r="5" fill="#38BDF8" />
    <circle class="pulse-glow" cx="0" cy="84" r="6" fill="none" stroke="#38BDF8" stroke-width="1.5" />
    <text x="0" y="62" text-anchor="middle" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700">2025</text>
    
    <text x="0" y="112" text-anchor="middle" fill="#F1F5F9" font-size="13" font-weight="600">Systems, Simulators &amp; Cryptography</text>
    <text x="0" y="130" text-anchor="middle" fill="#94A3B8" font-size="11">Steganography encoder, OS Virtual Memory &amp; PageSim</text>
    <text x="0" y="146" text-anchor="middle" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="10">TypeScript &#8226; Canvas API &#8226; OS Paging Simulators</text>
  </g>

  <!-- MILESTONE 3: 2026 -->
  <g class="node-3" transform="translate(980, 0)">
    <line x1="0" y1="84" x2="0" y2="70" stroke="#6366F1" stroke-width="1" stroke-dasharray="2 2" />
    <circle cx="0" cy="84" r="5" fill="#6366F1" />
    <circle class="pulse-glow" cx="0" cy="84" r="6" fill="none" stroke="#6366F1" stroke-width="1.5" />
    <text x="0" y="62" text-anchor="middle" fill="#818CF8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700">2026 // ACTIVE</text>
    
    <text x="0" y="112" text-anchor="middle" fill="#F1F5F9" font-size="13" font-weight="600">AI Perception &amp; Telemetry Daemons</text>
    <text x="0" y="130" text-anchor="middle" fill="#94A3B8" font-size="11">220+ contributions: Emotion detector &amp; System Bot</text>
    <text x="0" y="146" text-anchor="middle" fill="#818CF8" font-family="'JetBrains Mono', monospace" font-size="10">Python &#8226; OpenCV &#8226; CNNs &#8226; Prometheus-EBM SDK</text>
  </g>
</svg>
'''
with open("assets/journey.svg", "w", encoding="utf-8") as f:
    f.write(journey_svg)

# -------------------------------------------------------------
# 5. SECTION 06 — SYSTEMS / ARCHITECTURE (assets/systems-architecture.svg)
# -------------------------------------------------------------
print("Building Systems Architecture Diagram SVG...")
systems_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 260" width="100%" height="100%" role="img" aria-label="Babul Kumar — Systems Architecture Pipeline" style="background:#090C11; font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <linearGradient id="flowGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#38BDF8" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#6366F1" stop-opacity="0.9" />
    </linearGradient>

    <style><![CDATA[
      .flow-path {
        stroke-dasharray: 8 6;
        animation: flowAnimation 1.6s linear infinite;
      }
      .node-box {
        transition: all 0.3s ease;
      }
      .pulse-ring {
        animation: pulseRing 3s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
      }
      @keyframes flowAnimation {
        from { stroke-dashoffset: 28; }
        to { stroke-dashoffset: 0; }
      }
      @keyframes pulseRing {
        0% { transform: scale(0.96); opacity: 0.9; }
        50% { transform: scale(1.03); opacity: 0.4; }
        100% { transform: scale(0.96); opacity: 0.9; }
      }
    ]]></style>
  </defs>

  <rect width="1200" height="260" fill="#090C11" />
  <rect x="36" y="16" width="1128" height="228" rx="6" fill="#0C1017" stroke="#1E293B" stroke-width="1" />

  <!-- Header -->
  <text x="56" y="38" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9" letter-spacing="1.5">05 // ARCHITECTURE PIPELINE // REAL-TIME VISION &amp; SYSTEM TELEMETRY</text>
  <text x="1144" y="38" text-anchor="end" fill="#00E5FF" font-family="'JetBrains Mono', monospace" font-size="9">PIPELINE: STREAM &#8594; TENSOR &#8594; INFERENCE &#8594; ACTION</text>

  <!-- Connecting Stream Lines -->
  <g stroke="url(#flowGrad)" stroke-width="2" fill="none">
    <path class="flow-path" d="M 230 134 L 278 134" />
    <path class="flow-path" d="M 458 134 L 506 134" />
    <path class="flow-path" d="M 686 134 L 734 134" />
    <path class="flow-path" d="M 914 134 L 962 134" />
  </g>

  <!-- NODE 1: INPUT STREAM -->
  <g transform="translate(60, 68)">
    <rect class="node-box" x="0" y="0" width="170" height="132" rx="5" fill="#0F141F" stroke="#1E293B" stroke-width="1" />
    <path d="M 0 0 h 30 v 30 h -30 Z" fill="#00E5FF" fill-opacity="0.08" />
    <text x="14" y="20" fill="#00E5FF" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">01</text>
    <text x="40" y="20" fill="#F1F5F9" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600">INPUT SOURCE</text>
    
    <text x="14" y="56" fill="#FFFFFF" font-size="12.5" font-weight="600">Live Video &amp; Host</text>
    <text x="14" y="74" fill="#94A3B8" font-size="10.5">Camera feed / OS Metrics</text>
    <text x="14" y="92" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9.5">30 FPS Stream / Kernel Proc</text>
    <rect x="14" y="106" width="142" height="16" rx="3" fill="#1E293B" />
    <text x="20" y="118" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="8.5">SRC: OpenCV / psutil</text>
  </g>

  <!-- NODE 2: PRE-PROCESSING -->
  <g transform="translate(288, 68)">
    <rect class="node-box" x="0" y="0" width="170" height="132" rx="5" fill="#0F141F" stroke="#1E293B" stroke-width="1" />
    <path d="M 0 0 h 30 v 30 h -30 Z" fill="#38BDF8" fill-opacity="0.08" />
    <text x="14" y="20" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">02</text>
    <text x="40" y="20" fill="#F1F5F9" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600">PRE-PROCESSING</text>
    
    <text x="14" y="56" fill="#FFFFFF" font-size="12.5" font-weight="600">Normalization</text>
    <text x="14" y="74" fill="#94A3B8" font-size="10.5">Grayscale ROI / Resizing</text>
    <text x="14" y="92" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9.5">Haar Cascade / Buffer Ring</text>
    <rect x="14" y="106" width="142" height="16" rx="3" fill="#1E293B" />
    <text x="20" y="118" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="8.5">SHAPE: [N, 48, 48, 1]</text>
  </g>

  <!-- NODE 3: MODEL & LOGIC -->
  <g transform="translate(516, 68)">
    <rect class="node-box" x="0" y="0" width="170" height="132" rx="5" fill="#0F141F" stroke="#00E5FF" stroke-opacity="0.6" stroke-width="1.2" />
    <path d="M 0 0 h 30 v 30 h -30 Z" fill="#00E5FF" fill-opacity="0.12" />
    <text x="14" y="20" fill="#00E5FF" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">03</text>
    <text x="40" y="20" fill="#F1F5F9" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600">INFERENCE ENGINE</text>
    
    <text x="14" y="56" fill="#FFFFFF" font-size="12.5" font-weight="600">Multi-Task CNN</text>
    <text x="14" y="74" fill="#94A3B8" font-size="10.5">Softmax Emotion &amp; Age</text>
    <text x="14" y="92" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9.5">Forward Pass: &lt; 18ms</text>
    <rect x="14" y="106" width="142" height="16" rx="3" fill="#1E293B" />
    <text x="20" y="118" fill="#10B981" font-family="'JetBrains Mono', monospace" font-size="8.5">CONFIDENCE: OPTIMIZED</text>
  </g>

  <!-- NODE 4: DISPATCH / DECISION -->
  <g transform="translate(744, 68)">
    <rect class="node-box" x="0" y="0" width="170" height="132" rx="5" fill="#0F141F" stroke="#1E293B" stroke-width="1" />
    <path d="M 0 0 h 30 v 30 h -30 Z" fill="#6366F1" fill-opacity="0.08" />
    <text x="14" y="20" fill="#818CF8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">04</text>
    <text x="40" y="20" fill="#F1F5F9" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600">EVENT DISPATCH</text>
    
    <text x="14" y="56" fill="#FFFFFF" font-size="12.5" font-weight="600">Threshold Filter</text>
    <text x="14" y="74" fill="#94A3B8" font-size="10.5">Smoothing &amp; Alert Engine</text>
    <text x="14" y="92" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9.5">State machine evaluator</text>
    <rect x="14" y="106" width="142" height="16" rx="3" fill="#1E293B" />
    <text x="20" y="118" fill="#818CF8" font-family="'JetBrains Mono', monospace" font-size="8.5">EVENT: BOT DISPATCH</text>
  </g>

  <!-- NODE 5: CONSUMER / OUTPUT -->
  <g transform="translate(972, 68)">
    <rect class="node-box" x="0" y="0" width="170" height="132" rx="5" fill="#0F141F" stroke="#1E293B" stroke-width="1" />
    <path d="M 0 0 h 30 v 30 h -30 Z" fill="#10B981" fill-opacity="0.08" />
    <text x="14" y="20" fill="#10B981" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">05</text>
    <text x="40" y="20" fill="#F1F5F9" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600">OUTPUT / HUD</text>
    
    <text x="14" y="56" fill="#FFFFFF" font-size="12.5" font-weight="600">Overlay &amp; Notification</text>
    <text x="14" y="74" fill="#94A3B8" font-size="10.5">Real-time bounding box</text>
    <text x="14" y="92" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9.5">Telegram / Web UI alert</text>
    <rect x="14" y="106" width="142" height="16" rx="3" fill="#1E293B" />
    <text x="20" y="118" fill="#10B981" font-family="'JetBrains Mono', monospace" font-size="8.5">STATUS: EMITTED</text>
  </g>
</svg>
'''
with open("assets/systems-architecture.svg", "w", encoding="utf-8") as f:
    f.write(systems_svg)

# -------------------------------------------------------------
# 6. SECTION 09 — GITHUB TELEMETRY (assets/github-telemetry.svg)
# -------------------------------------------------------------
print("Building Verified GitHub Telemetry SVG...")
telemetry_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 280" width="100%" height="100%" role="img" aria-label="Babul Kumar — GitHub Telemetry" style="background:#090C11; font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <linearGradient id="barPython" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="100%" stop-color="#0284C7" />
    </linearGradient>
    <linearGradient id="barTS" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3178C6" />
      <stop offset="100%" stop-color="#2563EB" />
    </linearGradient>
    <linearGradient id="barJS" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F7DF1E" />
      <stop offset="100%" stop-color="#CA8A04" />
    </linearGradient>
    <linearGradient id="barOther" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A855F7" />
      <stop offset="100%" stop-color="#7C3AED" />
    </linearGradient>

    <style><![CDATA[
      .metric-card {
        transition: transform 0.2s ease;
      }
      .anim-bar-py { animation: barGrow 1.5s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
      @keyframes barGrow {
        from { width: 0; }
      }
    ]]></style>
  </defs>

  <rect width="1200" height="280" fill="#090C11" />
  <rect x="36" y="16" width="1128" height="248" rx="6" fill="#0C1017" stroke="#1E293B" stroke-width="1" />

  <!-- Header -->
  <text x="56" y="38" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9" letter-spacing="1.5">08 // GITHUB TELEMETRY &amp; LIVE ACTIVITY METRICS</text>
  <text x="1144" y="38" text-anchor="end" fill="#00E5FF" font-family="'JetBrains Mono', monospace" font-size="9">SOURCE: GITHUB PUBLIC API // LIVE SYNC</text>

  <!-- METRIC 1: Public Repositories -->
  <g class="metric-card" transform="translate(60, 60)">
    <rect x="0" y="0" width="250" height="100" rx="5" fill="#0F141F" stroke="#1E293B" stroke-width="1" />
    <text x="20" y="28" fill="#94A3B8" font-family="'JetBrains Mono', monospace" font-size="10.5">PUBLIC REPOSITORIES</text>
    <text x="20" y="68" fill="#F1F5F9" font-size="34" font-weight="800">27</text>
    <text x="82" y="64" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="11">ACTIVE REPOS</text>
    <text x="20" y="88" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9.5">AI/ML &#8226; Systems &#8226; Full-Stack</text>
  </g>

  <!-- METRIC 2: Total Contributions -->
  <g class="metric-card" transform="translate(330, 60)">
    <rect x="0" y="0" width="250" height="100" rx="5" fill="#0F141F" stroke="#1E293B" stroke-width="1" />
    <text x="20" y="28" fill="#94A3B8" font-family="'JetBrains Mono', monospace" font-size="10.5">LIFETIME CONTRIBUTIONS</text>
    <text x="20" y="68" fill="#F1F5F9" font-size="34" font-weight="800">248+</text>
    <text x="120" y="64" fill="#10B981" font-family="'JetBrains Mono', monospace" font-size="11">+221 IN 2026</text>
    <text x="20" y="88" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9.5">Verified GitHub Activity Record</text>
  </g>

  <!-- METRIC 3: Primary Languages -->
  <g class="metric-card" transform="translate(600, 60)">
    <rect x="0" y="0" width="250" height="100" rx="5" fill="#0F141F" stroke="#1E293B" stroke-width="1" />
    <text x="20" y="28" fill="#94A3B8" font-family="'JetBrains Mono', monospace" font-size="10.5">CORE ECOSYSTEM</text>
    <text x="20" y="58" fill="#F1F5F9" font-size="16" font-weight="700">Python &#8226; TypeScript</text>
    <text x="20" y="76" fill="#94A3B8" font-size="12">JavaScript &#8226; C/C++ &#8226; SQL</text>
    <text x="20" y="92" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9.5">Across 27 public codebases</text>
  </g>

  <!-- METRIC 4: Account Status -->
  <g class="metric-card" transform="translate(870, 60)">
    <rect x="0" y="0" width="270" height="100" rx="5" fill="#0F141F" stroke="#1E293B" stroke-width="1" />
    <text x="20" y="28" fill="#94A3B8" font-family="'JetBrains Mono', monospace" font-size="10.5">ACCOUNT TELEMETRY</text>
    <circle cx="28" cy="56" r="4.5" fill="#10B981" />
    <text x="40" y="60" fill="#F1F5F9" font-size="14" font-weight="600">Active Builder</text>
    <text x="20" y="80" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="10">Joined: Nov 2024</text>
    <text x="140" y="80" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="10">Followers: 5</text>
  </g>

  <!-- LOWER BAR: REPOSITORY LANGUAGE DISTRIBUTION -->
  <g transform="translate(60, 180)">
    <text x="0" y="0" fill="#94A3B8" font-family="'JetBrains Mono', monospace" font-size="10" letter-spacing="1">PUBLIC CODE REPOSITORY LANGUAGE COMPOSITION</text>
    <text x="1080" y="0" text-anchor="end" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9.5">27 REPOSITORIES TOTAL</text>
    
    <g transform="translate(0, 12)">
      <rect x="0" y="0" width="440" height="14" rx="2" fill="url(#barPython)" />
      <rect x="444" y="0" width="200" height="14" rx="2" fill="url(#barTS)" />
      <rect x="648" y="0" width="200" height="14" rx="2" fill="url(#barJS)" />
      <rect x="852" y="0" width="228" height="14" rx="2" fill="url(#barOther)" />
    </g>

    <!-- Legend -->
    <g font-family="'JetBrains Mono', monospace" font-size="10" transform="translate(0, 48)">
      <circle cx="6" cy="0" r="4.5" fill="#38BDF8" />
      <text x="18" y="3" fill="#F1F5F9">Python <tspan fill="#64748B">(40.7% · 11 repos)</tspan></text>

      <circle cx="280" cy="0" r="4.5" fill="#3178C6" />
      <text x="292" y="3" fill="#F1F5F9">TypeScript <tspan fill="#64748B">(18.5% · 5 repos)</tspan></text>

      <circle cx="560" cy="0" r="4.5" fill="#F7DF1E" />
      <text x="572" y="3" fill="#F1F5F9">JavaScript <tspan fill="#64748B">(18.5% · 5 repos)</tspan></text>

      <circle cx="840" cy="0" r="4.5" fill="#A855F7" />
      <text x="852" y="3" fill="#F1F5F9">Other / Notebooks <tspan fill="#64748B">(22.2% · 6 repos)</tspan></text>
    </g>
  </g>
</svg>
'''
with open("assets/github-telemetry.svg", "w", encoding="utf-8") as f:
    f.write(telemetry_svg)

# -------------------------------------------------------------
# 7. SECTION 10 — CONTRIBUTION ACTIVITY (assets/contribution-activity.svg)
# -------------------------------------------------------------
print("Building Real Contribution Matrix SVG...")
with open("assets/contributions_data.json", "r") as f:
    contrib_json = json.load(f)

# Get the last 52 weeks (364 days)
all_days = contrib_json['contributions']
recent_days = all_days[-364:] if len(all_days) >= 364 else all_days

def get_color(level, count):
    if count == 0 or level == 0:
        return "#161B22", 0.7
    elif count == 1:
        return "#0E4429", 0.95
    elif count == 2 or count == 3:
        return "#006D32", 1.0
    elif count <= 6:
        return "#26A641", 1.0
    else:
        return "#39D353", 1.0

cells_svg = ""
col_width = 19
row_height = 16
start_x = 76
start_y = 66

for idx, day in enumerate(recent_days):
    col = idx // 7
    row = idx % 7
    x = start_x + (col * col_width)
    y = start_y + (row * row_height)
    color, opacity = get_color(day['level'], day['count'])
    
    if day['count'] >= 4:
        color = "#00E5FF"
        opacity = 1.0

    anim_delay = (col * 0.02) + 0.3
    cells_svg += f'<rect class="cell" x="{x}" y="{y}" width="14" height="12" rx="2.5" fill="{color}" opacity="{opacity}" style="animation: cellReveal 0.4s ease {anim_delay:.2f}s both;" />\n      '

contrib_template = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 195" width="100%" height="100%" role="img" aria-label="Babul Kumar — GitHub Contribution Matrix" style="background:#090C11; font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <style><![CDATA[
      @keyframes cellReveal {
        from { opacity: 0; transform: scale(0.6); }
        to { opacity: 1; transform: scale(1); }
      }
      .cell:hover {
        stroke: #00E5FF;
        stroke-width: 1.5;
        cursor: pointer;
      }
    ]]></style>
  </defs>

  <rect width="1200" height="195" fill="#090C11" />
  <rect x="36" y="16" width="1128" height="165" rx="6" fill="#0C1017" stroke="#1E293B" stroke-width="1" />

  <!-- Header -->
  <text x="56" y="38" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9" letter-spacing="1.5">09 // CONTRIBUTION ACTIVITY FEED // 52-WEEK HEATMAP</text>
  <text x="1144" y="38" text-anchor="end" fill="#00E5FF" font-family="'JetBrains Mono', monospace" font-size="9">248 TOTAL CONTRIBUTIONS // 221 IN 2026</text>

  <!-- Day Labels -->
  <g fill="#475569" font-family="'JetBrains Mono', monospace" font-size="8.5" text-anchor="end">
    <text x="68" y="76">Mon</text>
    <text x="68" y="108">Wed</text>
    <text x="68" y="140">Fri</text>
  </g>

  <!-- Cells -->
  <g>
    __CELLS_SVG__
  </g>

  <!-- Footer Legend -->
  <g transform="translate(980, 164)" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748B">
    <text x="-36" y="9">Less</text>
    <rect x="0" y="0" width="10" height="10" rx="2" fill="#161B22" />
    <rect x="14" y="0" width="10" height="10" rx="2" fill="#0E4429" />
    <rect x="28" y="0" width="10" height="10" rx="2" fill="#006D32" />
    <rect x="42" y="0" width="10" height="10" rx="2" fill="#26A641" />
    <rect x="56" y="0" width="10" height="10" rx="2" fill="#00E5FF" />
    <text x="74" y="9">More</text>
  </g>
</svg>
'''
contrib_svg = contrib_template.replace("__CELLS_SVG__", cells_svg)
with open("assets/contribution-activity.svg", "w", encoding="utf-8") as f:
    f.write(contrib_svg)

# -------------------------------------------------------------
# 8. SECTION 11 — CONTRIBUTION SNAKE (assets/github-contribution-snake.svg)
# -------------------------------------------------------------
print("Building Animated Contribution Snake SVG...")
snake_template = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 220" width="100%" height="100%" role="img" aria-label="Babul Kumar — Animated Contribution Snake" style="background:#090C11; font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <filter id="snakeGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <style><![CDATA[
      @keyframes snakeMotion {
        0%   { transform: translate(76px, 66px); }
        15%  { transform: translate(380px, 66px); }
        25%  { transform: translate(380px, 114px); }
        40%  { transform: translate(720px, 114px); }
        55%  { transform: translate(720px, 162px); }
        75%  { transform: translate(1040px, 162px); }
        85%  { transform: translate(1040px, 66px); }
        95%  { transform: translate(840px, 66px); }
        100% { transform: translate(76px, 66px); }
      }

      @keyframes snakeBody1 {
        0%   { transform: translate(62px, 66px); }
        15%  { transform: translate(366px, 66px); }
        25%  { transform: translate(380px, 100px); }
        40%  { transform: translate(706px, 114px); }
        55%  { transform: translate(720px, 148px); }
        75%  { transform: translate(1026px, 162px); }
        85%  { transform: translate(1040px, 80px); }
        95%  { transform: translate(854px, 66px); }
        100% { transform: translate(62px, 66px); }
      }

      @keyframes snakeBody2 {
        0%   { transform: translate(48px, 66px); }
        15%  { transform: translate(352px, 66px); }
        25%  { transform: translate(380px, 86px); }
        40%  { transform: translate(692px, 114px); }
        55%  { transform: translate(720px, 134px); }
        75%  { transform: translate(1012px, 162px); }
        85%  { transform: translate(1040px, 94px); }
        95%  { transform: translate(868px, 66px); }
        100% { transform: translate(48px, 66px); }
      }

      @keyframes snakeTail {
        0%   { transform: translate(34px, 66px); }
        15%  { transform: translate(338px, 66px); }
        25%  { transform: translate(380px, 72px); }
        40%  { transform: translate(678px, 114px); }
        55%  { transform: translate(720px, 120px); }
        75%  { transform: translate(998px, 162px); }
        85%  { transform: translate(1040px, 108px); }
        95%  { transform: translate(882px, 66px); }
        100% { transform: translate(34px, 66px); }
      }

      .snake-head { animation: snakeMotion 18s ease-in-out infinite; }
      .snake-seg-1 { animation: snakeBody1 18s ease-in-out infinite; }
      .snake-seg-2 { animation: snakeBody2 18s ease-in-out infinite; }
      .snake-tail  { animation: snakeTail 18s ease-in-out infinite; }
    ]]></style>
  </defs>

  <rect width="1200" height="220" fill="#090C11" />
  <rect x="36" y="16" width="1128" height="188" rx="6" fill="#0C1017" stroke="#1E293B" stroke-width="1" />

  <!-- Technical Header -->
  <text x="56" y="38" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="9" letter-spacing="1.5">10 // CONTRIBUTION SNAKE // AUTONOMOUS CALENDAR HARVESTER</text>
  <text x="1144" y="38" text-anchor="end" fill="#00E5FF" font-family="'JetBrains Mono', monospace" font-size="9">ALGORITHM: GREEDY RECURSIVE PATHFINDER</text>

  <!-- Background Contribution Grid -->
  <g opacity="0.65">
    __CELLS_SVG__
  </g>

  <!-- THE ANIMATED SNAKE -->
  <!-- Tail -->
  <rect class="snake-tail" x="0" y="0" width="14" height="12" rx="2.5" fill="#00B4D8" opacity="0.5" />
  <!-- Body 2 -->
  <rect class="snake-seg-2" x="0" y="0" width="14" height="12" rx="2.5" fill="#00E5FF" opacity="0.75" />
  <!-- Body 1 -->
  <rect class="snake-seg-1" x="0" y="0" width="14" height="12" rx="2.5" fill="#38BDF8" opacity="0.9" />
  <!-- Head with Glow -->
  <g class="snake-head">
    <rect x="0" y="0" width="14" height="12" rx="3" fill="#FFFFFF" filter="url(#snakeGlow)" />
    <circle cx="4" cy="4" r="1.5" fill="#090C11" />
    <circle cx="10" cy="4" r="1.5" fill="#090C11" />
  </g>

  <!-- Live Status Line -->
  <g transform="translate(56, 186)" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#64748B">
    <circle cx="6" cy="-3" r="3.5" fill="#10B981" />
    <text x="16" y="0">HARVESTING REAL CONTRIBUTION NODES &#8226; TOTAL HARVESTED: 248 COMMITS</text>
  </g>
</svg>
'''
snake_svg = snake_template.replace("__CELLS_SVG__", cells_svg)
with open("assets/github-contribution-snake.svg", "w", encoding="utf-8") as f:
    f.write(snake_svg)
with open("assets/github-contribution-snake-dark.svg", "w", encoding="utf-8") as f:
    f.write(snake_svg)

print("All SVGs generated successfully!")
