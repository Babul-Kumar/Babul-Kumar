/**
 * OctoBanner — GitHub Profile README Generator
 * Two-Layer Architecture:
 * 1. Generator Application (Dark Technical Design Tool)
 * 2. GitHub Profile Preview (Authentic GitHub Document Surface)
 */

document.addEventListener('DOMContentLoaded', async () => {
  // DOM Elements
  const svgHost = document.getElementById('svgHost');
  const stageMat = document.getElementById('stageMat');
  const resolutionTag = document.getElementById('resolutionTag');
  const toast = document.getElementById('toast');
  const exportCanvas = document.getElementById('exportCanvas');

  // Simulated GitHub Context Elements
  const previewFullName = document.getElementById('previewFullName');
  const previewUsername = document.getElementById('previewUsername');
  const previewBio = document.getElementById('previewBio');
  const previewAboutParagraph = document.getElementById('previewAboutParagraph');

  // Drawer & Code
  const btnToggleDrawer = document.getElementById('btnToggleDrawer');
  const drawerContent = document.getElementById('drawerContent');
  const drawerTabBtns = document.querySelectorAll('.drawer-tab-btn');
  const drawerPanes = document.querySelectorAll('.drawer-pane');
  const codeBlock = document.getElementById('codeBlock');

  // Input Fields
  const inputName = document.getElementById('inputName');
  const inputTitle = document.getElementById('inputTitle');
  const inputEthos = document.getElementById('inputEthos');
  const inputHost = document.getElementById('inputHost');
  const inputSpecialization = document.getElementById('inputSpecialization');
  const inputStack = document.getElementById('inputStack');
  const inputGit = document.getElementById('inputGit');

  // Buttons
  const colorChips = document.querySelectorAll('.color-chip');
  const btnResetDefaults = document.getElementById('btnResetDefaults');
  const btnReplay = document.getElementById('btnReplay');
  const btnCopySvg = document.getElementById('btnCopySvg');
  const btnCopyReadme = document.getElementById('btnCopyReadme');
  const btnCopyReadmeQuick = document.getElementById('btnCopyReadmeQuick');
  const btnCopyReadmePane = document.getElementById('btnCopyReadmePane');
  const btnCopySourcePane = document.getElementById('btnCopySourcePane');
  const btnDownloadSvg = document.getElementById('btnDownloadSvg');
  const btnDownloadSvgDock = document.getElementById('btnDownloadSvgDock');
  const btnExportPngDock = document.getElementById('btnExportPngDock');

  // Tabs & Chips
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabPanels = document.querySelectorAll('.tab-panel');
  const viewportChips = document.querySelectorAll('.viewport-chip');
  const viewChips = document.querySelectorAll('.view-chip');
  const themeChips = document.querySelectorAll('.theme-chip');

  // State
  let portraitBase64 = '';
  let activeAccentColor = '#00E5FF';
  let activeTheme = 'dark';
  let isCustomized = false;
  let preloadedDarkSvg = '';
  let preloadedLightSvg = '';
  let currentSvgMarkup = '';

  // 1. Load assets
  try {
    const [pRes, darkRes, lightRes] = await Promise.all([
      fetch('assets/portrait_base64.txt').catch(() => null),
      fetch('dark.svg').catch(() => fetch('assets/dark.svg')).catch(() => null),
      fetch('light.svg').catch(() => fetch('assets/light.svg')).catch(() => null)
    ]);
    if (pRes && pRes.ok) portraitBase64 = (await pRes.text()).trim();
    if (darkRes && darkRes.ok) preloadedDarkSvg = await darkRes.text();
    if (lightRes && lightRes.ok) preloadedLightSvg = await lightRes.text();
  } catch (err) {
    console.warn('Asset loading notice:', err);
  }

  // XML sanitization
  function escapeXml(unsafe) {
    if (typeof unsafe !== 'string') return '';
    return unsafe
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&apos;');
  }

  function clampText(text, maxLen) {
    if (!text) return '';
    const clean = text.trim();
    return clean.length > maxLen ? clean.substring(0, maxLen - 1) + '…' : clean;
  }

  // 2. SVG Template — GitHub-native document style, 1200×380 aspect ratio
  function generateSvgMarkup(params) {
    const name = escapeXml(clampText(params.name || 'BABUL KUMAR', 32).toUpperCase());
    const title = escapeXml(clampText(params.title || 'Computer Science & Engineering • AI/ML • Full-Stack', 60));
    const ethos = escapeXml(clampText(params.ethos || 'Building software, experimenting with AI, and turning ideas into working systems.', 110));

    const host = escapeXml(clampText(params.host || 'babul@dev', 24));
    const userHandle = escapeXml(clampText(params.handle || 'babul-kumar', 32));
    const stack = escapeXml(clampText(params.stack || 'AI / ML • Full-Stack Development • Systems', 80));
    const git = escapeXml(clampText(params.git || 'building software • 26 active repositories', 70));
    const accent = params.accent || '#00E5FF';
    const portrait = params.portrait || portraitBase64;
    const isLight = (params.theme === 'light');

    if (isLight) {
      return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 380" width="100%" height="100%" role="img" aria-label="GitHub Profile Banner for ${name}" style="background:#FFFFFF; font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <radialGradient id="lightRadialCyan" cx="22%" cy="36%" r="42%">
      <stop offset="0%" stop-color="${accent}" stop-opacity="0.08" />
      <stop offset="60%" stop-color="${accent}" stop-opacity="0.01" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0" />
    </radialGradient>
    <radialGradient id="lightRadialIndigo" cx="84%" cy="65%" r="38%">
      <stop offset="0%" stop-color="#4F46E5" stop-opacity="0.04" />
      <stop offset="70%" stop-color="#4F46E5" stop-opacity="0.01" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0" />
    </radialGradient>
    <linearGradient id="portraitGlowLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="${accent}" stop-opacity="0.12" />
      <stop offset="40%" stop-color="${accent}" stop-opacity="0.02" />
      <stop offset="85%" stop-color="#F8FAFC" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.9" />
    </linearGradient>
    <linearGradient id="termBgLight" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC" stop-opacity="0.98" />
      <stop offset="100%" stop-color="#F1F5F9" stop-opacity="0.99" />
    </linearGradient>
    <clipPath id="portraitClipLight">
      <path d="M 64 56 L 312 56 L 312 286 L 298 300 L 64 300 Z" />
    </clipPath>
    <style><![CDATA[
      .anim-frame { opacity: 0; animation: bootFadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.0s forwards; }
      .anim-portrait { opacity: 0; animation: bootScaleIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.25s forwards; }
      .anim-identity { opacity: 0; animation: bootFadeSlide 0.55s cubic-bezier(0.16, 1, 0.3, 1) 0.45s forwards; }
      .anim-terminal { opacity: 0; animation: bootFadeSlide 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.65s forwards; }
      .line-1 { opacity: 0; animation: lineReveal 0.35s ease 0.85s forwards; }
      .line-2 { opacity: 0; animation: lineReveal 0.35s ease 1.02s forwards; }
      .line-3 { opacity: 0; animation: lineReveal 0.35s ease 1.18s forwards; }
      .line-4 { opacity: 0; animation: lineReveal 0.35s ease 1.35s forwards; }
      .idle-cursor { opacity: 0; animation: lineReveal 0.2s ease 1.45s forwards, cursorBlink 0.95s step-end 1.6s infinite; }
      .idle-pulse { animation: pulseDot 2.8s ease-in-out infinite; }
      @keyframes bootFadeIn { from { opacity: 0; } to { opacity: 1; } }
      @keyframes bootFadeSlide { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
      @keyframes bootScaleIn { from { opacity: 0; transform: scale(0.98); } to { opacity: 1; transform: scale(1); } }
      @keyframes lineReveal { from { opacity: 0; } to { opacity: 1; } }
      @keyframes cursorBlink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
      @keyframes pulseDot { 0%, 100% { opacity: 0.95; transform: scale(1); } 50% { opacity: 0.35; transform: scale(0.85); } }
    ]]></style>
  </defs>
  <rect width="1200" height="380" fill="#FFFFFF" />
  <circle cx="260" cy="190" r="280" fill="url(#lightRadialCyan)" />
  <circle cx="960" cy="260" r="300" fill="url(#lightRadialIndigo)" />
  <g stroke="${accent}" stroke-opacity="0.08" stroke-width="1">
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
  <g class="anim-frame">
    <rect x="36" y="24" width="1128" height="332" fill="none" stroke="#E2E8F0" stroke-width="1" />
    <path d="M 32 24 h 10 M 36 20 v 10" stroke="${accent}" stroke-width="1.2" />
    <path d="M 1158 24 h 10 M 1164 20 v 10" stroke="#94A3B8" stroke-width="1" />
    <path d="M 32 356 h 10 M 36 352 v 10" stroke="#94A3B8" stroke-width="1" />
    <path d="M 1158 356 h 10 M 1164 352 v 10" stroke="${accent}" stroke-width="1.2" />
  </g>
  <g class="anim-portrait">
    <line x1="54" y1="52" x2="54" y2="328" stroke="${accent}" stroke-opacity="0.25" stroke-width="1" stroke-dasharray="110 5 20 4" />
    <rect x="60" y="52" width="256" height="252" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1" />
    <path d="M 56 68 v -18 h 18" fill="none" stroke="${accent}" stroke-width="1.5" />
    <path d="M 320 290 v 18 h -18" fill="none" stroke="${accent}" stroke-opacity="0.7" stroke-width="1.5" />
    <g clip-path="url(#portraitClipLight)">
      <image href="data:image/jpeg;base64,${portrait}" x="64" y="56" width="248" height="244" preserveAspectRatio="xMidYMid slice" opacity="0.92" />
      <rect x="64" y="56" width="248" height="244" fill="url(#portraitGlowLight)" />
    </g>
    <rect x="60" y="278" width="256" height="28" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1" />
    <circle class="idle-pulse" cx="74" cy="292" r="3" fill="#059669" />
    <text x="84" y="295" fill="#1E293B" font-size="9" font-weight="500" letter-spacing="0.8" font-family="'JetBrains Mono', monospace">babul@workspace</text>
    <text x="250" y="295" fill="#64748B" font-size="8.5" font-family="'JetBrains Mono', monospace">builder</text>
  </g>
  <g transform="translate(360, 0)">
    <g class="anim-identity">
      <text x="0" y="80" fill="#0F172A" font-size="38" font-weight="800" letter-spacing="-0.02em">${name}</text>
      <text x="2" y="104" fill="${accent}" font-size="10.5" font-weight="600" letter-spacing="1.4" font-family="'JetBrains Mono', monospace">${title}</text>
      <text x="2" y="128" fill="#475569" font-size="12.5" font-weight="400" letter-spacing="0.01em">${ethos}</text>
    </g>
    <g class="anim-terminal" transform="translate(0, 146)">
      <rect width="780" height="182" rx="6" fill="url(#termBgLight)" stroke="#D0D7DE" stroke-width="1" />
      <rect width="780" height="28" rx="6" fill="#E2E8F0" />
      <line x1="0" y1="28" x2="780" y2="28" stroke="#CBD5E1" stroke-width="1" />
      <circle cx="16" cy="14" r="3" fill="#EF4444" fill-opacity="0.8" />
      <circle cx="28" cy="14" r="3" fill="#F59E0B" fill-opacity="0.8" />
      <circle cx="40" cy="14" r="3" fill="#10B981" fill-opacity="0.8" />
      <text x="56" y="18" fill="#64748B" font-size="9" font-family="'JetBrains Mono', monospace">~/babul-kumar &#8226; main</text>
      <g transform="translate(18, 46)" font-family="'JetBrains Mono', monospace" font-size="11">
        <g class="line-1">
          <text x="0" y="0" fill="${accent}">${host}</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#4F46E5">~</text>
          <text x="96" y="0" fill="#0F172A">$ whoami</text>
          <text x="0" y="16" fill="#1E293B" font-weight="500">${userHandle}</text>
        </g>
        <g class="line-2" transform="translate(0, 36)">
          <text x="0" y="0" fill="${accent}">${host}</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#4F46E5">~</text>
          <text x="96" y="0" fill="#0F172A">$ focus</text>
          <text x="0" y="16" fill="#475569">${stack}</text>
        </g>
        <g class="line-3" transform="translate(0, 72)">
          <text x="0" y="0" fill="${accent}">${host}</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#4F46E5">~</text>
          <text x="96" y="0" fill="#0F172A">$ status</text>
          <text x="0" y="16" fill="#059669">${git}</text>
        </g>
        <g class="line-4" transform="translate(0, 108)">
          <text x="0" y="0" fill="${accent}">${host}</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#4F46E5">~</text>
          <text x="96" y="0" fill="#0F172A">$</text>
          <rect class="idle-cursor" x="110" y="-10" width="7" height="13" fill="${accent}" />
        </g>
      </g>
    </g>
  </g>
</svg>`;
    }

    // Default Dark Banner
    return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 380" width="100%" height="100%" role="img" aria-label="GitHub Profile Banner for ${name}" style="background:#090C11; font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <radialGradient id="radialCyan" cx="22%" cy="36%" r="42%">
      <stop offset="0%" stop-color="${accent}" stop-opacity="0.08" />
      <stop offset="60%" stop-color="${accent}" stop-opacity="0.01" />
      <stop offset="100%" stop-color="#090C11" stop-opacity="0" />
    </radialGradient>
    <radialGradient id="radialViolet" cx="84%" cy="65%" r="38%">
      <stop offset="0%" stop-color="#6366F1" stop-opacity="0.06" />
      <stop offset="70%" stop-color="#6366F1" stop-opacity="0.01" />
      <stop offset="100%" stop-color="#090C11" stop-opacity="0" />
    </radialGradient>
    <linearGradient id="portraitGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="${accent}" stop-opacity="0.18" />
      <stop offset="40%" stop-color="${accent}" stop-opacity="0.03" />
      <stop offset="85%" stop-color="#090C11" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#090C11" stop-opacity="0.95" />
    </linearGradient>
    <linearGradient id="termBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0F141F" stop-opacity="0.94" />
      <stop offset="100%" stop-color="#0A0E17" stop-opacity="0.98" />
    </linearGradient>
    <linearGradient id="nameGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="75%" stop-color="#F1F5F9" />
      <stop offset="100%" stop-color="${accent}" />
    </linearGradient>
    <linearGradient id="scanlineGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="${accent}" stop-opacity="0" />
      <stop offset="50%" stop-color="${accent}" stop-opacity="0.03" />
      <stop offset="100%" stop-color="${accent}" stop-opacity="0" />
    </linearGradient>
    <linearGradient id="gridFade" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#FFF" stop-opacity="0.2" />
      <stop offset="90%" stop-color="#000" stop-opacity="0" />
    </linearGradient>
    <mask id="gridMask">
      <rect width="1200" height="380" fill="url(#gridFade)" />
    </mask>
    <clipPath id="portraitClip">
      <path d="M 64 56 L 312 56 L 312 286 L 298 300 L 64 300 Z" />
    </clipPath>
    <clipPath id="termClip">
      <rect x="360" y="154" width="780" height="174" />
    </clipPath>
    <style><![CDATA[
      .anim-frame { opacity: 0; animation: bootFadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.0s forwards; }
      .anim-portrait { opacity: 0; animation: bootScaleIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.25s forwards; }
      .anim-identity { opacity: 0; animation: bootFadeSlide 0.55s cubic-bezier(0.16, 1, 0.3, 1) 0.45s forwards; }
      .anim-terminal { opacity: 0; animation: bootFadeSlide 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.65s forwards; }
      .line-1 { opacity: 0; animation: lineReveal 0.35s ease 0.85s forwards; }
      .line-2 { opacity: 0; animation: lineReveal 0.35s ease 1.02s forwards; }
      .line-3 { opacity: 0; animation: lineReveal 0.35s ease 1.18s forwards; }
      .line-4 { opacity: 0; animation: lineReveal 0.35s ease 1.35s forwards; }
      .idle-cursor { opacity: 0; animation: lineReveal 0.2s ease 1.45s forwards, cursorBlink 0.95s step-end 1.6s infinite; }
      .idle-pulse { animation: pulseDot 2.8s ease-in-out infinite; }
      .idle-glow { animation: glowDrift 5.2s ease-in-out infinite alternate; }
      .idle-scanline { animation: scanlineDrift 5s linear infinite; }
      @keyframes bootFadeIn { from { opacity: 0; } to { opacity: 1; } }
      @keyframes bootFadeSlide { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
      @keyframes bootScaleIn { from { opacity: 0; transform: scale(0.98); } to { opacity: 1; transform: scale(1); } }
      @keyframes lineReveal { from { opacity: 0; } to { opacity: 1; } }
      @keyframes cursorBlink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
      @keyframes pulseDot { 0%, 100% { opacity: 0.95; transform: scale(1); } 50% { opacity: 0.35; transform: scale(0.85); } }
      @keyframes glowDrift { 0% { opacity: 0.7; transform: translate(0, 0); } 100% { opacity: 1.0; transform: translate(10px, -5px); } }
      @keyframes scanlineDrift { 0% { transform: translateY(0px); opacity: 0.02; } 50% { opacity: 0.04; } 100% { transform: translateY(140px); opacity: 0.02; } }
    ]]></style>
  </defs>
  <rect width="1200" height="380" fill="#090C11" />
  <circle class="idle-glow" cx="260" cy="190" r="280" fill="url(#radialCyan)" />
  <circle class="idle-glow" cx="960" cy="260" r="300" fill="url(#radialViolet)" />
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
  <g class="anim-frame">
    <rect x="36" y="24" width="1128" height="332" fill="none" stroke="#1E293B" stroke-opacity="0.5" stroke-width="1" />
    <path d="M 32 24 h 10 M 36 20 v 10" stroke="${accent}" stroke-opacity="0.4" stroke-width="1.2" />
    <path d="M 1158 24 h 10 M 1164 20 v 10" stroke="#64748B" stroke-opacity="0.3" stroke-width="1" />
    <path d="M 32 356 h 10 M 36 352 v 10" stroke="#64748B" stroke-opacity="0.3" stroke-width="1" />
    <path d="M 1158 356 h 10 M 1164 352 v 10" stroke="${accent}" stroke-opacity="0.4" stroke-width="1.2" />
  </g>
  <g class="anim-portrait">
    <line x1="54" y1="52" x2="54" y2="328" stroke="${accent}" stroke-opacity="0.18" stroke-width="1" stroke-dasharray="110 5 20 4" />
    <rect x="60" y="52" width="256" height="252" fill="#0C1017" stroke="#1E293B" stroke-opacity="0.8" stroke-width="1" />
    <path d="M 56 68 v -18 h 18" fill="none" stroke="${accent}" stroke-width="1.5" />
    <path d="M 320 290 v 18 h -18" fill="none" stroke="${accent}" stroke-opacity="0.6" stroke-width="1.5" />
    <g clip-path="url(#portraitClip)">
      <image href="data:image/jpeg;base64,${portrait}" x="64" y="56" width="248" height="244" preserveAspectRatio="xMidYMid slice" opacity="0.9" />
      <rect x="64" y="56" width="248" height="244" fill="url(#portraitGlow)" />
    </g>
    <rect x="60" y="278" width="256" height="28" fill="#090D14" fill-opacity="0.94" stroke="#1E293B" stroke-width="1" />
    <circle class="idle-pulse" cx="74" cy="292" r="3" fill="#10B981" />
    <text x="84" y="295" fill="#E2E8F0" font-size="9" font-weight="500" letter-spacing="0.8" font-family="'JetBrains Mono', monospace">babul@workspace</text>
    <text x="250" y="295" fill="#64748B" font-size="8.5" font-family="'JetBrains Mono', monospace">builder</text>
  </g>
  <g transform="translate(360, 0)">
    <g class="anim-identity">
      <text x="0" y="80" fill="url(#nameGradient)" font-size="38" font-weight="800" letter-spacing="-0.02em">${name}</text>
      <text x="2" y="104" fill="${accent}" font-size="10.5" font-weight="600" letter-spacing="1.4" font-family="'JetBrains Mono', monospace">${title}</text>
      <text x="2" y="128" fill="#94A3B8" font-size="12.5" font-weight="400" letter-spacing="0.01em">${ethos}</text>
    </g>
    <g class="anim-terminal" transform="translate(0, 146)">
      <rect width="780" height="182" rx="6" fill="url(#termBg)" stroke="#1E293B" stroke-width="1" />
      <rect width="780" height="28" rx="6" fill="#0C1017" />
      <line x1="0" y1="28" x2="780" y2="28" stroke="#1E293B" stroke-width="1" />
      <circle cx="16" cy="14" r="3" fill="#EF4444" fill-opacity="0.6" />
      <circle cx="28" cy="14" r="3" fill="#F59E0B" fill-opacity="0.6" />
      <circle cx="40" cy="14" r="3" fill="#10B981" fill-opacity="0.6" />
      <text x="56" y="18" fill="#475569" font-size="9" font-family="'JetBrains Mono', monospace">~/babul-kumar &#8226; main</text>
      <g clip-path="url(#termClip)">
        <rect class="idle-scanline" x="1" y="29" width="778" height="20" fill="url(#scanlineGrad)" pointer-events="none" />
      </g>
      <g transform="translate(18, 46)" font-family="'JetBrains Mono', monospace" font-size="11">
        <g class="line-1">
          <text x="0" y="0" fill="${accent}">${host}</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#A5B4FC">~</text>
          <text x="96" y="0" fill="#F1F5F9">$ whoami</text>
          <text x="0" y="16" fill="#E2E8F0" font-weight="500">${userHandle}</text>
        </g>
        <g class="line-2" transform="translate(0, 36)">
          <text x="0" y="0" fill="${accent}">${host}</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#A5B4FC">~</text>
          <text x="96" y="0" fill="#F1F5F9">$ focus</text>
          <text x="0" y="16" fill="#94A3B8">${stack}</text>
        </g>
        <g class="line-3" transform="translate(0, 72)">
          <text x="0" y="0" fill="${accent}">${host}</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#A5B4FC">~</text>
          <text x="96" y="0" fill="#F1F5F9">$ status</text>
          <text x="0" y="16" fill="#10B981">${git}</text>
        </g>
        <g class="line-4" transform="translate(0, 108)">
          <text x="0" y="0" fill="${accent}">${host}</text>
          <text x="76" y="0" fill="#64748B">:</text>
          <text x="84" y="0" fill="#A5B4FC">~</text>
          <text x="96" y="0" fill="#F1F5F9">$</text>
          <rect class="idle-cursor" x="110" y="-10" width="7" height="13" fill="${accent}" />
        </g>
      </g>
    </g>
  </g>
</svg>`;
  }

  // 3. Parameters from inputs
  function getParams() {
    return {
      name: inputName ? inputName.value : 'BABUL KUMAR',
      title: inputTitle ? inputTitle.value : 'Computer Science & Engineering • AI/ML • Full-Stack',
      ethos: inputEthos ? inputEthos.value : 'Building software, experimenting with AI, and turning ideas into working systems.',
      host: inputHost ? inputHost.value : 'babul@dev',
      handle: inputSpecialization ? inputSpecialization.value : 'babul-kumar',
      stack: inputStack ? inputStack.value : 'AI / ML • Full-Stack Development • Systems',
      git: inputGit ? inputGit.value : 'building software • 26 active repositories',
      accent: activeAccentColor,
      portrait: portraitBase64,
      theme: activeTheme
    };
  }

  // 4. Update preview
  function updatePreview() {
    const params = getParams();

    // Sync simulated GitHub sidebar & about text
    if (previewFullName && inputName) {
      previewFullName.textContent = inputName.value.trim() || 'Babul Kumar';
    }
    if (previewBio && inputEthos) {
      previewBio.textContent = inputEthos.value.trim() || 'Computer Science & Engineering student • Builder';
    }
    if (previewAboutParagraph && inputEthos) {
      previewAboutParagraph.textContent = `I'm a Computer Science & Engineering student and software builder focused on artificial intelligence, machine learning, and full-stack software development. ${inputEthos.value.trim()}`;
    }

    if (!isCustomized) {
      if (activeTheme === 'dark' && preloadedDarkSvg) {
        currentSvgMarkup = preloadedDarkSvg;
      } else if (activeTheme === 'light' && preloadedLightSvg) {
        currentSvgMarkup = preloadedLightSvg;
      } else {
        currentSvgMarkup = generateSvgMarkup(params);
      }
    } else {
      currentSvgMarkup = generateSvgMarkup(params);
    }

    svgHost.innerHTML = currentSvgMarkup;

    if (codeBlock) {
      codeBlock.textContent = currentSvgMarkup;
    }

    // Update download links
    const blob = new Blob([currentSvgMarkup], { type: 'image/svg+xml;charset=utf-8' });
    const blobUrl = URL.createObjectURL(blob);
    const downloadHref = (!isCustomized && activeAccentColor === '#00E5FF')
      ? (activeTheme === 'light' ? 'light.svg' : 'dark.svg')
      : blobUrl;
    const downloadName = (activeTheme === 'light' ? 'light.svg' : 'dark.svg');

    if (btnDownloadSvg) {
      btnDownloadSvg.href = downloadHref;
      btnDownloadSvg.download = downloadName;
    }
    if (btnDownloadSvgDock) {
      btnDownloadSvgDock.href = downloadHref;
      btnDownloadSvgDock.download = downloadName;
    }
  }

  // 5. Live input listeners
  const allInputs = [
    inputName, inputTitle, inputEthos,
    inputHost, inputSpecialization, inputStack, inputGit
  ];

  allInputs.forEach(input => {
    if (input) {
      input.addEventListener('input', () => {
        isCustomized = true;
        updatePreview();
      });
    }
  });

  // 6. Color picker
  colorChips.forEach(chip => {
    chip.addEventListener('click', () => {
      colorChips.forEach(c => {
        c.classList.remove('active');
        c.setAttribute('aria-checked', 'false');
      });
      chip.classList.add('active');
      chip.setAttribute('aria-checked', 'true');
      activeAccentColor = chip.dataset.color || '#00E5FF';
      isCustomized = true;
      updatePreview();
      showToast(`Accent: ${chip.title}`);
    });
  });

  // 7. Tab navigation (Profile, Content, Appearance)
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      tabPanels.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');
      const targetPanel = document.getElementById(`panel-${btn.dataset.tab}`);
      if (targetPanel) targetPanel.classList.add('active');
    });
  });

  // 8. Viewport selectors (Desktop is DEFAULT)
  viewportChips.forEach(chip => {
    chip.addEventListener('click', () => {
      viewportChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      const frame = chip.dataset.frame;

      stageMat.classList.remove('frame-desktop', 'frame-mobile');
      stageMat.classList.add(`frame-${frame}`);

      if (frame === 'desktop') {
        resolutionTag.textContent = 'Desktop • 1040px (Default)';
      } else if (frame === 'mobile') {
        resolutionTag.textContent = 'Mobile • 420px (Responsive)';
      }
    });
  });

  // 9. View mode selector (Full Profile vs README Only)
  viewChips.forEach(chip => {
    chip.addEventListener('click', () => {
      viewChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      const view = chip.dataset.view;

      stageMat.classList.remove('view-profile', 'view-readme');
      stageMat.classList.add(`view-${view}`);
    });
  });

  // 10. Theme selectors (Dark / Light)
  themeChips.forEach(chip => {
    chip.addEventListener('click', () => {
      themeChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      activeTheme = chip.dataset.theme;

      stageMat.classList.remove('theme-dark', 'theme-light');
      stageMat.classList.add(`theme-${activeTheme}`);
      updatePreview();
      showToast(`Theme: ${activeTheme === 'dark' ? 'GitHub Dark' : 'GitHub Light'}`);
    });
  });

  // 11. Replay Animation
  function replaySequence() {
    svgHost.innerHTML = '';
    void svgHost.offsetWidth;
    svgHost.innerHTML = currentSvgMarkup;
    showToast('Replaying banner animation');
  }

  if (btnReplay) btnReplay.addEventListener('click', replaySequence);

  // 12. Reset to defaults
  if (btnResetDefaults) {
    btnResetDefaults.addEventListener('click', () => {
      isCustomized = false;
      activeTheme = 'dark';
      
      stageMat.classList.remove('theme-light', 'frame-mobile', 'view-readme');
      stageMat.classList.add('theme-dark', 'frame-desktop', 'view-profile');
      
      viewportChips.forEach((c, idx) => c.classList.toggle('active', idx === 0));
      viewChips.forEach((c, idx) => c.classList.toggle('active', idx === 0));
      themeChips.forEach((c, idx) => c.classList.toggle('active', idx === 0));

      resolutionTag.textContent = 'Desktop • 1040px (Default)';

      if (inputName) inputName.value = 'BABUL KUMAR';
      if (inputTitle) inputTitle.value = 'Computer Science & Engineering • AI/ML • Full-Stack';
      if (inputEthos) inputEthos.value = 'Building software, experimenting with AI, and turning ideas into working systems.';

      if (inputHost) inputHost.value = 'babul@dev';
      if (inputSpecialization) inputSpecialization.value = 'babul-kumar';
      if (inputStack) inputStack.value = 'AI / ML • Full-Stack Development • Systems';
      if (inputGit) inputGit.value = 'building software • 26 active repositories';

      activeAccentColor = '#00E5FF';
      colorChips.forEach((c, idx) => {
        c.classList.toggle('active', idx === 0);
        c.setAttribute('aria-checked', idx === 0 ? 'true' : 'false');
      });

      updatePreview();
      replaySequence();
      showToast('Reset to defaults');
    });
  }

  // 13. Collapsible Developer drawer
  if (btnToggleDrawer) {
    btnToggleDrawer.addEventListener('click', () => {
      const isExpanded = btnToggleDrawer.getAttribute('aria-expanded') === 'true';
      btnToggleDrawer.setAttribute('aria-expanded', (!isExpanded).toString());
      drawerContent.classList.toggle('collapsed', isExpanded);
      drawerContent.setAttribute('aria-hidden', isExpanded.toString());
    });
  }

  drawerTabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      drawerTabBtns.forEach(b => b.classList.remove('active'));
      drawerPanes.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const pane = document.getElementById(`pane-${btn.dataset.pane}`);
      if (pane) pane.classList.add('active');
    });
  });

  // 14. Clipboard helpers
  async function copyText(text, successMsg) {
    try {
      await navigator.clipboard.writeText(text);
      showToast(successMsg);
    } catch (err) {
      const ta = document.createElement('textarea');
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
      showToast(successMsg);
    }
  }

  const readmeMarkdown = `<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./light.svg">
  <img src="./dark.svg" alt="Babul Kumar — developer profile" width="100%">
</picture>`;

  if (btnCopySvg) {
    btnCopySvg.addEventListener('click', () => copyText(currentSvgMarkup, 'SVG copied to clipboard!'));
  }
  if (btnCopySourcePane) {
    btnCopySourcePane.addEventListener('click', () => copyText(currentSvgMarkup, 'SVG source copied!'));
  }
  if (btnCopyReadme) {
    btnCopyReadme.addEventListener('click', () => copyText(readmeMarkdown, 'README snippet copied!'));
  }
  if (btnCopyReadmeQuick) {
    btnCopyReadmeQuick.addEventListener('click', () => copyText(readmeMarkdown, 'README snippet copied!'));
  }
  if (btnCopyReadmePane) {
    btnCopyReadmePane.addEventListener('click', () => copyText(readmeMarkdown, 'README snippet copied!'));
  }

  // 15. PNG Export
  function exportHighResPng() {
    const svgEl = svgHost.querySelector('svg');
    if (!svgEl) return;

    showToast('Rendering PNG...');

    const svgData = new XMLSerializer().serializeToString(svgEl);
    const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
    const url = URL.createObjectURL(svgBlob);

    const img = new Image();
    img.onload = () => {
      exportCanvas.width = 2400;
      exportCanvas.height = 760;
      const ctx = exportCanvas.getContext('2d');
      ctx.imageSmoothingEnabled = true;
      ctx.imageSmoothingQuality = 'high';

      ctx.drawImage(img, 0, 0, 2400, 760);
      URL.revokeObjectURL(url);

      const pngUrl = exportCanvas.toDataURL('image/png');
      const dlLink = document.createElement('a');
      dlLink.download = `babul-kumar-hero-${activeTheme}-2x.png`;
      dlLink.href = pngUrl;
      document.body.appendChild(dlLink);
      dlLink.click();
      document.body.removeChild(dlLink);
      showToast('PNG downloaded!');
    };
    img.onerror = () => {
      showToast('PNG export failed. Use SVG download instead.');
    };
    img.src = url;
  }

  if (btnExportPngDock) btnExportPngDock.addEventListener('click', exportHighResPng);

  // 16. Toast notification
  function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => {
      toast.classList.remove('show');
    }, 2400);
  }

  // Initial render
  updatePreview();
});
