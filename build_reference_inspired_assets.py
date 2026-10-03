import os
import xml.etree.ElementTree as ET

os.makedirs('assets/cards', exist_ok=True)

# -------------------------------------------------------------
# 1. card-mailmind.svg (AI Email Priority & Classification)
# -------------------------------------------------------------
card_mailmind = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 110" width="100%" height="110" fill="none">
  <defs>
    <linearGradient id="mmBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B10"/>
      <stop offset="50%" stop-color="#0A1017"/>
      <stop offset="100%" stop-color="#0D1622"/>
    </linearGradient>
    <linearGradient id="mmAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00D2FF"/>
      <stop offset="100%" stop-color="#0077FF"/>
    </linearGradient>
    <filter id="mmGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    @keyframes pulseNode {
      0%, 100% { r: 3.5px; opacity: 0.6; }
      50% { r: 5px; opacity: 1; filter: drop-shadow(0 0 5px #00D2FF); }
    }
    @keyframes sweepLine {
      0% { stroke-dashoffset: 120; opacity: 0.2; }
      50% { opacity: 0.9; }
      100% { stroke-dashoffset: 0; opacity: 0.2; }
    }
    @keyframes orbitNode {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    .orbit-ring {
      transform-origin: 350px 55px;
      animation: orbitNode 9s linear infinite;
    }
    .flow-dash {
      stroke-dasharray: 20 40;
      animation: sweepLine 4s linear infinite;
    }
    .nlp-core {
      animation: pulseNode 2.2s ease-in-out infinite;
    }
  </style>

  <rect x="1" y="1" width="418" height="108" rx="10" fill="url(#mmBg)" stroke="#21262D" stroke-width="1.2"/>
  <line x1="1" y1="1" x2="419" y2="1" stroke="url(#mmAccent)" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Left Content -->
  <g transform="translate(22, 0)">
    <text x="0" y="32" font-family="'SF Mono', 'Segoe UI Mono', Consolas, monospace" font-size="11" font-weight="700" fill="#00D2FF" letter-spacing="1.5px">01 // INTELLIGENCE</text>
    <text x="0" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" fill="#F0F6FC" letter-spacing="1.5px">MailMind</text>
    <text x="0" y="78" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500" fill="#8B949E" letter-spacing="0.2px">AI Email Priority Scoring &amp; Classification Engine</text>
    <g transform="translate(0, 92)">
      <text font-family="'SF Mono', Consolas, monospace" font-size="9" font-weight="600" fill="#00D2FF">PYTHON</text>
      <text x="44" font-family="sans-serif" font-size="9" fill="#484F58">•</text>
      <text x="56" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#8B949E">NLP PIPELINE</text>
      <text x="130" font-family="sans-serif" font-size="9" fill="#484F58">•</text>
      <text x="142" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#8B949E">DEEP LEARNING</text>
    </g>
  </g>

  <!-- Right Graphic: NLP Neural Classification Node & Orbit -->
  <g>
    <circle cx="350" cy="55" r="38" fill="#00D2FF" fill-opacity="0.03"/>
    <circle cx="350" cy="55" r="34" stroke="#1D2633" stroke-width="1.2" fill="none"/>
    <circle cx="350" cy="55" r="22" stroke="#25354A" stroke-width="1" stroke-dasharray="4 8" fill="none" class="orbit-ring"/>
    <circle cx="350" cy="55" r="10" stroke="#00D2FF" stroke-width="1.5" fill="#0E1622"/>
    <circle cx="350" cy="55" r="4" fill="#00D2FF" class="nlp-core"/>

    <!-- Neural connection lines -->
    <line x1="324" y1="36" x2="350" y2="55" stroke="#00D2FF" stroke-width="1" stroke-opacity="0.6"/>
    <line x1="376" y1="36" x2="350" y2="55" stroke="#00D2FF" stroke-width="1" stroke-opacity="0.6"/>
    <line x1="324" y1="74" x2="350" y2="55" stroke="#00D2FF" stroke-width="1" stroke-opacity="0.6"/>
    <line x1="376" y1="74" x2="350" y2="55" stroke="#00D2FF" stroke-width="1" stroke-opacity="0.6"/>

    <!-- Orbiting Classification Points -->
    <circle cx="324" cy="36" r="3" fill="#38EF7D"/>
    <circle cx="376" cy="36" r="3" fill="#00D2FF"/>
    <circle cx="324" cy="74" r="3" fill="#79C0FF"/>
    <circle cx="376" cy="74" r="3" fill="#4FACFE"/>
  </g>
</svg>"""

with open('assets/cards/card-mailmind.svg', 'w', encoding='utf-8') as f:
    f.write(card_mailmind)

# -------------------------------------------------------------
# 2. card-emotion.svg (Emotion & Age Detector)
# -------------------------------------------------------------
card_emotion = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 110" width="100%" height="110" fill="none">
  <defs>
    <linearGradient id="emBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B10"/>
      <stop offset="50%" stop-color="#0A1218"/>
      <stop offset="100%" stop-color="#0E1722"/>
    </linearGradient>
    <linearGradient id="emAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38EF7D"/>
      <stop offset="100%" stop-color="#00D2FF"/>
    </linearGradient>
    <filter id="emGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    @keyframes reticleScan {
      0% { transform: translateY(-16px); opacity: 0.2; }
      50% { opacity: 0.9; }
      100% { transform: translateY(16px); opacity: 0.2; }
    }
    @keyframes boxBlink {
      0%, 100% { stroke-opacity: 0.4; }
      50% { stroke-opacity: 1; }
    }
    .reticle-line {
      animation: reticleScan 2.8s ease-in-out infinite alternate;
    }
    .reticle-box {
      animation: boxBlink 2s ease-in-out infinite;
    }
  </style>

  <rect x="1" y="1" width="418" height="108" rx="10" fill="url(#emBg)" stroke="#21262D" stroke-width="1.2"/>
  <line x1="1" y1="1" x2="419" y2="1" stroke="url(#emAccent)" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Left Content -->
  <g transform="translate(22, 0)">
    <text x="0" y="32" font-family="'SF Mono', 'Segoe UI Mono', Consolas, monospace" font-size="11" font-weight="700" fill="#38EF7D" letter-spacing="1.5px">02 // COMPUTER VISION</text>
    <text x="0" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" fill="#F0F6FC" letter-spacing="1px">Emotion-Age Detector</text>
    <text x="0" y="78" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500" fill="#8B949E" letter-spacing="0.2px">Real-Time Facial Landmark &amp; Emotion Inference</text>
    <g transform="translate(0, 92)">
      <text font-family="'SF Mono', Consolas, monospace" font-size="9" font-weight="600" fill="#38EF7D">OPENCV</text>
      <text x="44" font-family="sans-serif" font-size="9" fill="#484F58">•</text>
      <text x="56" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#8B949E">CNN INFERENCE</text>
      <text x="144" font-family="sans-serif" font-size="9" fill="#484F58">•</text>
      <text x="156" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#8B949E">PYTHON</text>
    </g>
  </g>

  <!-- Right Graphic: Computer Vision Facial Reticle -->
  <g transform="translate(350, 55)">
    <circle cx="0" cy="0" r="38" fill="#38EF7D" fill-opacity="0.03"/>
    <!-- Bounding Corner Brackets -->
    <path d="M -22 -14 L -22 -22 L -14 -22" stroke="#38EF7D" stroke-width="1.8" fill="none" class="reticle-box"/>
    <path d="M 14 -22 L 22 -22 L 22 -14" stroke="#38EF7D" stroke-width="1.8" fill="none" class="reticle-box"/>
    <path d="M -22 14 L -22 22 L -14 22" stroke="#38EF7D" stroke-width="1.8" fill="none" class="reticle-box"/>
    <path d="M 14 22 L 22 22 L 22 14" stroke="#38EF7D" stroke-width="1.8" fill="none" class="reticle-box"/>

    <!-- Facial Keypoints -->
    <circle cx="-8" cy="-6" r="2" fill="#00D2FF"/>
    <circle cx="8" cy="-6" r="2" fill="#00D2FF"/>
    <circle cx="0" cy="2" r="1.5" fill="#38EF7D"/>
    <path d="M -7 10 Q 0 14 7 10" stroke="#00D2FF" stroke-width="1.2" fill="none"/>

    <!-- Scanning Reticle Line -->
    <line x1="-20" y1="0" x2="20" y2="0" stroke="#38EF7D" stroke-width="1.2" class="reticle-line"/>
    <text x="0" y="32" text-anchor="middle" font-family="'SF Mono', Consolas, monospace" font-size="8" fill="#38EF7D">CONF: 98.4%</text>
  </g>
</svg>"""

with open('assets/cards/card-emotion.svg', 'w', encoding='utf-8') as f:
    f.write(card_emotion)

# -------------------------------------------------------------
# 3. card-monitor.svg (smart-system-monitor)
# -------------------------------------------------------------
card_monitor = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 110" width="100%" height="110" fill="none">
  <defs>
    <linearGradient id="monBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B10"/>
      <stop offset="50%" stop-color="#0C121A"/>
      <stop offset="100%" stop-color="#0E1624"/>
    </linearGradient>
    <linearGradient id="monAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00D2FF"/>
      <stop offset="100%" stop-color="#38EF7D"/>
    </linearGradient>
  </defs>

  <style>
    @keyframes pulseWave {
      0% { stroke-dashoffset: 160; }
      100% { stroke-dashoffset: 0; }
    }
    @keyframes heartbeat {
      0%, 100% { r: 3px; opacity: 0.6; }
      20% { r: 5px; opacity: 1; filter: drop-shadow(0 0 4px #00D2FF); }
      40% { r: 3.5px; opacity: 0.7; }
      60% { r: 4.5px; opacity: 0.9; filter: drop-shadow(0 0 3px #00D2FF); }
    }
    .pulse-line {
      stroke-dasharray: 40 120;
      animation: pulseWave 3s linear infinite;
    }
    .heart-node {
      animation: heartbeat 2s ease-in-out infinite;
    }
  </style>

  <rect x="1" y="1" width="418" height="108" rx="10" fill="url(#monBg)" stroke="#21262D" stroke-width="1.2"/>
  <line x1="1" y1="1" x2="419" y2="1" stroke="url(#monAccent)" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Left Content -->
  <g transform="translate(22, 0)">
    <text x="0" y="32" font-family="'SF Mono', 'Segoe UI Mono', Consolas, monospace" font-size="11" font-weight="700" fill="#00D2FF" letter-spacing="1.5px">03 // TELEMETRY &amp; DAEMONS</text>
    <text x="0" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="19" font-weight="800" fill="#F0F6FC" letter-spacing="1.2px">smart-system-monitor</text>
    <text x="0" y="78" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500" fill="#8B949E" letter-spacing="0.2px">Cross-Platform Hardware Diagnostics &amp; Daemon Bot</text>
    <g transform="translate(0, 92)">
      <text font-family="'SF Mono', Consolas, monospace" font-size="9" font-weight="600" fill="#00D2FF">PYTHON</text>
      <text x="44" font-family="sans-serif" font-size="9" fill="#484F58">•</text>
      <text x="56" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#8B949E">PSUTIL</text>
      <text x="100" font-family="sans-serif" font-size="9" fill="#484F58">•</text>
      <text x="112" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#8B949E">TELEGRAM BOT API</text>
    </g>
  </g>

  <!-- Right Graphic: Oscilloscope Waveform & Diagnostics Node -->
  <g transform="translate(350, 55)">
    <rect x="-36" y="-28" width="72" height="56" rx="6" fill="#0A1017" stroke="#21262D" stroke-width="1"/>
    <!-- Grid lines -->
    <line x1="-36" y1="0" x2="36" y2="0" stroke="#161B22" stroke-width="1"/>
    <line x1="0" y1="-28" x2="0" y2="28" stroke="#161B22" stroke-width="1"/>

    <!-- Waveform Track -->
    <path d="M -32 0 L -18 0 L -12 -14 L -6 18 L 0 -10 L 6 10 L 12 0 L 32 0" stroke="#1F2A38" stroke-width="1.5" fill="none"/>
    <path d="M -32 0 L -18 0 L -12 -14 L -6 18 L 0 -10 L 6 10 L 12 0 L 32 0" stroke="#00D2FF" stroke-width="1.8" fill="none" class="pulse-line"/>
    <circle cx="0" cy="-10" r="3" fill="#38EF7D" class="heart-node"/>
  </g>
</svg>"""

with open('assets/cards/card-monitor.svg', 'w', encoding='utf-8') as f:
    f.write(card_monitor)

# -------------------------------------------------------------
# 4. card-steganography.svg (Steganography Image Carrier)
# -------------------------------------------------------------
card_steg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 110" width="100%" height="110" fill="none">
  <defs>
    <linearGradient id="stegBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B10"/>
      <stop offset="50%" stop-color="#100F1A"/>
      <stop offset="100%" stop-color="#141124"/>
    </linearGradient>
    <linearGradient id="stegAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#BD5FFF"/>
      <stop offset="100%" stop-color="#00D2FF"/>
    </linearGradient>
  </defs>

  <style>
    @keyframes bitPulse {
      0%, 100% { opacity: 0.2; }
      50% { opacity: 0.9; }
    }
    @keyframes keyRotate {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    .bit-cell-1 { animation: bitPulse 1.8s ease-in-out infinite; }
    .bit-cell-2 { animation: bitPulse 2.4s ease-in-out infinite 0.6s; }
    .bit-cell-3 { animation: bitPulse 1.5s ease-in-out infinite 1.1s; }
  </style>

  <rect x="1" y="1" width="418" height="108" rx="10" fill="url(#stegBg)" stroke="#21262D" stroke-width="1.2"/>
  <line x1="1" y1="1" x2="419" y2="1" stroke="url(#stegAccent)" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Left Content -->
  <g transform="translate(22, 0)">
    <text x="0" y="32" font-family="'SF Mono', 'Segoe UI Mono', Consolas, monospace" font-size="11" font-weight="700" fill="#BD5FFF" letter-spacing="1.5px">04 // CRYPTOGRAPHY &amp; SECURITY</text>
    <text x="0" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" fill="#F0F6FC" letter-spacing="1.5px">Steganography-</text>
    <text x="0" y="78" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500" fill="#8B949E" letter-spacing="0.2px">Cryptographic Least Significant Bit (LSB) Carrier Tool</text>
    <g transform="translate(0, 92)">
      <text font-family="'SF Mono', Consolas, monospace" font-size="9" font-weight="600" fill="#BD5FFF">TYPESCRIPT</text>
      <text x="68" font-family="sans-serif" font-size="9" fill="#484F58">•</text>
      <text x="80" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#8B949E">CANVAS PIXELS</text>
      <text x="170" font-family="sans-serif" font-size="9" fill="#484F58">•</text>
      <text x="182" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#8B949E">LSB ENCRYPTION</text>
    </g>
  </g>

  <!-- Right Graphic: Cryptographic Pixel Matrix -->
  <g transform="translate(350, 55)">
    <rect x="-30" y="-30" width="60" height="60" rx="8" fill="#0C0E17" stroke="#251F38" stroke-width="1.2"/>
    <!-- 3x3 Pixel Bit Grid -->
    <rect x="-22" y="-22" width="12" height="12" rx="2" fill="#BD5FFF" class="bit-cell-1"/>
    <rect x="-6" y="-22" width="12" height="12" rx="2" fill="#2E234A"/>
    <rect x="10" y="-22" width="12" height="12" rx="2" fill="#00D2FF" class="bit-cell-2"/>
    <rect x="-22" y="-6" width="12" height="12" rx="2" fill="#2E234A"/>
    <rect x="-6" y="-6" width="12" height="12" rx="2" fill="#BD5FFF" class="bit-cell-3"/>
    <rect x="10" y="-6" width="12" height="12" rx="2" fill="#2E234A"/>
    <rect x="-22" y="10" width="12" height="12" rx="2" fill="#00D2FF" class="bit-cell-2"/>
    <rect x="-6" y="10" width="12" height="12" rx="2" fill="#2E234A"/>
    <rect x="10" y="10" width="12" height="12" rx="2" fill="#BD5FFF" class="bit-cell-1"/>
  </g>
</svg>"""

with open('assets/cards/card-steganography.svg', 'w', encoding='utf-8') as f:
    f.write(card_steg)

# -------------------------------------------------------------
# 5. card-virtualmemory.svg (Virtual Memory Paging Simulator)
# -------------------------------------------------------------
card_vm = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 110" width="100%" height="110" fill="none">
  <defs>
    <linearGradient id="vmBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B10"/>
      <stop offset="50%" stop-color="#0A121A"/>
      <stop offset="100%" stop-color="#0C1724"/>
    </linearGradient>
    <linearGradient id="vmAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#79C0FF"/>
      <stop offset="100%" stop-color="#58A6FF"/>
    </linearGradient>
  </defs>

  <style>
    @keyframes frameSlide {
      0%, 100% { opacity: 0.3; transform: scale(0.96); }
      50% { opacity: 1; transform: scale(1); filter: drop-shadow(0 0 3px #79C0FF); }
    }
    .page-frame-active {
      animation: frameSlide 2.5s ease-in-out infinite;
    }
  </style>

  <rect x="1" y="1" width="418" height="108" rx="10" fill="url(#vmBg)" stroke="#21262D" stroke-width="1.2"/>
  <line x1="1" y1="1" x2="419" y2="1" stroke="url(#vmAccent)" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Left Content -->
  <g transform="translate(22, 0)">
    <text x="0" y="32" font-family="'SF Mono', 'Segoe UI Mono', Consolas, monospace" font-size="11" font-weight="700" fill="#79C0FF" letter-spacing="1.5px">05 // OPERATING SYSTEMS</text>
    <text x="0" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="19" font-weight="800" fill="#F0F6FC" letter-spacing="1.2px">Virtual-Memory-Simulator</text>
    <text x="0" y="78" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500" fill="#8B949E" letter-spacing="0.2px">FIFO, LRU, &amp; Optimal OS Paging Replacement Engine</text>
    <g transform="translate(0, 92)">
      <text font-family="'SF Mono', Consolas, monospace" font-size="9" font-weight="600" fill="#79C0FF">JAVASCRIPT</text>
      <text x="68" font-family="sans-serif" font-size="9" fill="#484F58">•</text>
      <text x="80" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#8B949E">PAGING ALGORITHMS</text>
      <text x="200" font-family="sans-serif" font-size="9" fill="#484F58">•</text>
      <text x="212" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#8B949E">SIMULATION</text>
    </g>
  </g>

  <!-- Right Graphic: Memory Page Frames Stack -->
  <g transform="translate(350, 55)">
    <rect x="-32" y="-30" width="64" height="60" rx="6" fill="#0A1017" stroke="#1D2A3B" stroke-width="1.2"/>
    <!-- Stack of 3 Paging Frames -->
    <rect x="-24" y="-22" width="48" height="12" rx="3" fill="#142132" stroke="#253A52" stroke-width="1"/>
    <text x="0" y="-13" text-anchor="middle" font-family="'SF Mono', Consolas, monospace" font-size="8" fill="#8B949E">FRAME 0 [P1]</text>
    
    <rect x="-24" y="-6" width="48" height="12" rx="3" fill="#142132" stroke="#58A6FF" stroke-width="1.2" class="page-frame-active"/>
    <text x="0" y="3" text-anchor="middle" font-family="'SF Mono', Consolas, monospace" font-size="8" fill="#79C0FF" font-weight="700">FRAME 1 [P4]*</text>
    
    <rect x="-24" y="10" width="48" height="12" rx="3" fill="#142132" stroke="#253A52" stroke-width="1"/>
    <text x="0" y="19" text-anchor="middle" font-family="'SF Mono', Consolas, monospace" font-size="8" fill="#8B949E">FRAME 2 [P2]</text>
  </g>
</svg>"""

with open('assets/cards/card-virtualmemory.svg', 'w', encoding='utf-8') as f:
    f.write(card_vm)

# -------------------------------------------------------------
# 6. card-prometheus.svg (Prometheus EBM SDK)
# -------------------------------------------------------------
card_prom = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 110" width="100%" height="110" fill="none">
  <defs>
    <linearGradient id="prBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B10"/>
      <stop offset="50%" stop-color="#120F16"/>
      <stop offset="100%" stop-color="#18131E"/>
    </linearGradient>
    <linearGradient id="prAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFA657"/>
      <stop offset="100%" stop-color="#FF7B72"/>
    </linearGradient>
  </defs>

  <style>
    @keyframes dialSweep {
      0% { transform: rotate(-30deg); }
      50% { transform: rotate(30deg); }
      100% { transform: rotate(-30deg); }
    }
    .gauge-needle {
      transform-origin: 350px 65px;
      animation: dialSweep 4s ease-in-out infinite;
    }
  </style>

  <rect x="1" y="1" width="418" height="108" rx="10" fill="url(#prBg)" stroke="#21262D" stroke-width="1.2"/>
  <line x1="1" y1="1" x2="419" y2="1" stroke="url(#prAccent)" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Left Content -->
  <g transform="translate(22, 0)">
    <text x="0" y="32" font-family="'SF Mono', 'Segoe UI Mono', Consolas, monospace" font-size="11" font-weight="700" fill="#FFA657" letter-spacing="1.5px">06 // AI EVALUATION &amp; BENCHMARKING</text>
    <text x="0" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="19" font-weight="800" fill="#F0F6FC" letter-spacing="1.2px">prometheus-ebm-sdk</text>
    <text x="0" y="78" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500" fill="#8B949E" letter-spacing="0.2px">Epistemic Metacognition Calibration Benchmark Toolkit</text>
    <g transform="translate(0, 92)">
      <text font-family="'SF Mono', Consolas, monospace" font-size="9" font-weight="600" fill="#FFA657">PYTHON</text>
      <text x="44" font-family="sans-serif" font-size="9" fill="#484F58">•</text>
      <text x="56" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#8B949E">BENCHMARKING</text>
      <text x="150" font-family="sans-serif" font-size="9" fill="#484F58">•</text>
      <text x="162" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#8B949E">METRIC SUITE</text>
    </g>
  </g>

  <!-- Right Graphic: Epistemic Calibration Gauge -->
  <g>
    <circle cx="350" cy="55" r="38" fill="#FFA657" fill-opacity="0.03"/>
    <path d="M 322 65 A 32 32 0 1 1 378 65" stroke="#251F2A" stroke-width="3" fill="none"/>
    <path d="M 322 65 A 32 32 0 0 1 350 33" stroke="#FFA657" stroke-width="3" fill="none" stroke-linecap="round"/>
    
    <!-- Calibration Needle -->
    <g class="gauge-needle">
      <line x1="350" y1="65" x2="350" y2="40" stroke="#FF7B72" stroke-width="2" stroke-linecap="round"/>
      <circle cx="350" cy="65" r="4" fill="#FFA657"/>
    </g>
    <text x="350" y="78" text-anchor="middle" font-family="'SF Mono', Consolas, monospace" font-size="8" fill="#FFA657">ECE: 0.042</text>
  </g>
</svg>"""

with open('assets/cards/card-prometheus.svg', 'w', encoding='utf-8') as f:
    f.write(card_prom)

# -------------------------------------------------------------
# 7. assets/workflow-pipeline.svg (Idea to Impact)
# -------------------------------------------------------------
pipeline_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 110" width="100%" height="110" fill="none">
  <defs>
    <linearGradient id="pipeBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#080C11"/>
      <stop offset="100%" stop-color="#0D1219"/>
    </linearGradient>
    <linearGradient id="pipeAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#30363D"/>
      <stop offset="50%" stop-color="#00D2FF"/>
      <stop offset="100%" stop-color="#38EF7D"/>
    </linearGradient>
    <filter id="nodeGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    @keyframes flowPacket {
      0% { stroke-dashoffset: 400; opacity: 0.1; }
      50% { opacity: 0.9; }
      100% { stroke-dashoffset: 0; opacity: 0.1; }
    }
    .flow-line {
      stroke-dasharray: 40 120;
      animation: flowPacket 6s linear infinite;
    }
    .stage-title {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-weight: 700;
      font-size: 11px;
      letter-spacing: 1.5px;
      fill: #F0F6FC;
    }
    .stage-num {
      font-family: "SF Mono", "Segoe UI Mono", Menlo, Consolas, monospace;
      font-weight: 600;
      font-size: 9px;
      letter-spacing: 1px;
      fill: #00D2FF;
    }
  </style>

  <rect x="1" y="1" width="878" height="108" rx="10" fill="url(#pipeBg)" stroke="#21262D" stroke-width="1.2"/>
  <line x1="70" y1="55" x2="810" y2="55" stroke="#21262D" stroke-width="2"/>
  <line x1="70" y1="55" x2="810" y2="55" stroke="url(#pipeAccent)" stroke-width="2.5" stroke-linecap="round" class="flow-line"/>

  <!-- Node 1: EXPLORE -->
  <g transform="translate(70, 55)">
    <circle cx="0" cy="0" r="18" fill="#121820" stroke="#30363D" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="6" fill="#00D2FF" filter="url(#nodeGlow)"/>
    <text x="0" y="-28" text-anchor="middle" class="stage-num">01</text>
    <text x="0" y="36" text-anchor="middle" class="stage-title">EXPLORE</text>
  </g>

  <!-- Node 2: ARCHITECTURE -->
  <g transform="translate(218, 55)">
    <circle cx="0" cy="0" r="18" fill="#121820" stroke="#30363D" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="6" fill="#4FACFE"/>
    <text x="0" y="-28" text-anchor="middle" class="stage-num">02</text>
    <text x="0" y="36" text-anchor="middle" class="stage-title">ARCHITECT</text>
  </g>

  <!-- Node 3: BUILD -->
  <g transform="translate(366, 55)">
    <circle cx="0" cy="0" r="18" fill="#121820" stroke="#00D2FF" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="6" fill="#00D2FF" filter="url(#nodeGlow)"/>
    <text x="0" y="-28" text-anchor="middle" class="stage-num">03</text>
    <text x="0" y="36" text-anchor="middle" class="stage-title">BUILD</text>
  </g>

  <!-- Node 4: BENCHMARK -->
  <g transform="translate(514, 55)">
    <circle cx="0" cy="0" r="18" fill="#121820" stroke="#30363D" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="6" fill="#4FACFE"/>
    <text x="0" y="-28" text-anchor="middle" class="stage-num">04</text>
    <text x="0" y="36" text-anchor="middle" class="stage-title">BENCHMARK</text>
  </g>

  <!-- Node 5: DEPLOY -->
  <g transform="translate(662, 55)">
    <circle cx="0" cy="0" r="18" fill="#121820" stroke="#30363D" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="6" fill="#00D2FF"/>
    <text x="0" y="-28" text-anchor="middle" class="stage-num">05</text>
    <text x="0" y="36" text-anchor="middle" class="stage-title">DEPLOY</text>
  </g>

  <!-- Node 6: ITERATE -->
  <g transform="translate(810, 55)">
    <circle cx="0" cy="0" r="18" fill="#121820" stroke="#38EF7D" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="6" fill="#38EF7D" filter="url(#nodeGlow)"/>
    <text x="0" y="-28" text-anchor="middle" class="stage-num" fill="#38EF7D">06</text>
    <text x="0" y="36" text-anchor="middle" class="stage-title" fill="#38EF7D">ITERATE</text>
  </g>
</svg>"""

with open('assets/workflow-pipeline.svg', 'w', encoding='utf-8') as f:
    f.write(pipeline_svg)

# -------------------------------------------------------------
# 8. assets/build-cycle.svg (Engineering Cycle)
# -------------------------------------------------------------
cycle_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 110" width="100%" height="110" fill="none">
  <defs>
    <linearGradient id="cycleBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080C11"/>
      <stop offset="100%" stop-color="#0D131C"/>
    </linearGradient>
  </defs>

  <style>
    @keyframes marchLine {
      from { stroke-dashoffset: 200; }
      to { stroke-dashoffset: 0; }
    }
    .connector-dash {
      stroke-dasharray: 6 6;
      animation: marchLine 5s linear infinite;
    }
    .stage-box {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-weight: 700;
      font-size: 11px;
      letter-spacing: 2px;
      fill: #F0F6FC;
    }
    .cycle-label {
      font-family: "SF Mono", "Segoe UI Mono", Menlo, Consolas, monospace;
      font-size: 9px;
      letter-spacing: 1px;
      fill: #8B949E;
    }
  </style>

  <rect x="1" y="1" width="878" height="108" rx="10" fill="url(#cycleBg)" stroke="#21262D" stroke-width="1.2"/>

  <!-- Connectors -->
  <line x1="165" y1="55" x2="225" y2="55" stroke="#00D2FF" stroke-width="1.5" class="connector-dash"/>
  <polygon points="228,55 221,51 221,59" fill="#00D2FF"/>

  <line x1="335" y1="55" x2="395" y2="55" stroke="#4FACFE" stroke-width="1.5" class="connector-dash"/>
  <polygon points="398,55 391,51 391,59" fill="#4FACFE"/>

  <line x1="505" y1="55" x2="565" y2="55" stroke="#4FACFE" stroke-width="1.5" class="connector-dash"/>
  <polygon points="568,55 561,51 561,59" fill="#4FACFE"/>

  <line x1="685" y1="55" x2="745" y2="55" stroke="#38EF7D" stroke-width="1.5" class="connector-dash"/>
  <polygon points="748,55 741,51 741,59" fill="#38EF7D"/>

  <!-- Stage 1: BUILD -->
  <g transform="translate(60, 30)">
    <rect x="0" y="0" width="105" height="50" rx="8" fill="#12171E" stroke="#30363D" stroke-width="1.2"/>
    <text x="52" y="24" text-anchor="middle" class="stage-box">BUILD</text>
    <text x="52" y="38" text-anchor="middle" class="cycle-label">01 // INIT</text>
  </g>

  <!-- Stage 2: TEST -->
  <g transform="translate(230, 30)">
    <rect x="0" y="0" width="105" height="50" rx="8" fill="#12171E" stroke="#30363D" stroke-width="1.2"/>
    <text x="52" y="24" text-anchor="middle" class="stage-box">TEST</text>
    <text x="52" y="38" text-anchor="middle" class="cycle-label">02 // VERIFY</text>
  </g>

  <!-- Stage 3: BREAK -->
  <g transform="translate(400, 30)">
    <rect x="0" y="0" width="105" height="50" rx="8" fill="#12171E" stroke="#F85149" stroke-width="1.2" stroke-opacity="0.7"/>
    <text x="52" y="24" text-anchor="middle" class="stage-box" fill="#FF7B72">BREAK</text>
    <text x="52" y="38" text-anchor="middle" class="cycle-label" fill="#FF7B72">03 // STRESS</text>
  </g>

  <!-- Stage 4: UNDERSTAND -->
  <g transform="translate(570, 30)">
    <rect x="0" y="0" width="115" height="50" rx="8" fill="#12171E" stroke="#30363D" stroke-width="1.2"/>
    <text x="57" y="24" text-anchor="middle" class="stage-box" font-size="10">UNDERSTAND</text>
    <text x="57" y="38" text-anchor="middle" class="cycle-label">04 // PROFILE</text>
  </g>

  <!-- Stage 5: REBUILD -->
  <g transform="translate(750, 30)">
    <rect x="0" y="0" width="105" height="50" rx="8" fill="#12171E" stroke="#38EF7D" stroke-width="1.4"/>
    <circle cx="12" cy="12" r="3" fill="#38EF7D"/>
    <text x="52" y="24" text-anchor="middle" class="stage-box" fill="#38EF7D">REBUILD</text>
    <text x="52" y="38" text-anchor="middle" class="cycle-label" fill="#38EF7D">05 // RESILIENT</text>
  </g>
</svg>"""

with open('assets/build-cycle.svg', 'w', encoding='utf-8') as f:
    f.write(cycle_svg)

print("Generated all cards and cycle SVGs successfully!")
