#!/usr/bin/env python3
"""Validate the public-safe static website surface."""

from __future__ import annotations

import fnmatch
import html
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

HTML_PAGES = [
    "index.html",
    "procurement/index.html",
    "ai-control/index.html",
    "pt/index.html",
    "pt/procurement/index.html",
    "pt/ai-control/index.html",
]

REQUIRED_FILES = [
    "index.html",
    "styles.css",
    "procurement/index.html",
    "ai-control/index.html",
    "pt/index.html",
    "pt/procurement/index.html",
    "pt/ai-control/index.html",
    "README.md",
    "docs/public_claims_ledger.md",
    "docs/restrictions.md",
    "docs/publication_checklist.md",
    "docs/deployment_runbook.md",
    "docs/review_notes.md",
    "docs/site_content_model.md",
    "docs/translation_glossary.md",
    "docs/codex_runs/20260608_phase_2_1_hub_public_language_qa_handoff.md",
    "docs/codex_runs/20260608_phase_2_2_homepage_public_language_correction_handoff.md",
    "scripts/validate_public_surface.py",
]

REQUIRED_SVGS = [
    "assets/mark.svg",
    "assets/favicon.svg",
    "assets/og-image.svg",
    "assets/evidence-control-pattern.svg",
    "assets/procurement-evidence-chain.svg",
    "assets/ai-action-control-gate.svg",
    "assets/evidence-pack.svg",
    "assets/simulation-review-pack.svg",
    "assets/trustgate-sovereign-execution-firewall.svg",
    "assets/trustgate-sovereign-working-example.svg",
    "assets/tg360-evidence-cockpit.svg",
]

SECRET_NAMES = {
    "credentials.json",
    "id_rsa",
    "token.json",
}

SECRET_PATTERNS = [
    ".env",
    ".env.*",
    "*.pem",
    "*.key",
]

BINARY_IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif"}
TEXT_SUFFIXES = {".html", ".css", ".md", ".svg", ".py"}

ANALYTICS_KEYWORDS = [
    "google-analytics",
    "gtag",
    "plausible",
    "hotjar",
    "segment",
    "mixpanel",
    "facebook pixel",
]

COOKIE_CODE_PATTERNS = [
    "document.cookie",
    "set-cookie",
    "cookieconsent",
    "cookiescript",
]

BLOCKED_PUBLIC_CLAIMS = [
    "production-ready",
    "production ready",
    "production execution service",
    "production security gateway",
    "production deployment",
    "customer-proven",
    "trusted by",
    "guaranteed compliance",
    "compliance-certified",
    "DORA compliant",
    "AI Act compliant",
    "GDPR compliant",
    "regulator-approved",
    "legal determination",
    "guarantees examiner readiness",
    "guarantees prediction",
    "guaranteed prediction",
    "win probability",
    "likely winner",
    "replaces human review",
    "replacement for human review",
    "replaces legal review",
    "replaces compliance",
    "makes AI safe",
    "makes AI agents safe",
    "validates physics",
    "solver correctness",
    "automatic design approval",
    "live national coverage",
    "autonomous decisioning",
    "customer traction",
]

BLOCKED_PORTUGUESE_CLAIMS = [
    "pronto para produção",
    "comprovado por clientes",
    "usado por clientes",
    "garantimos conformidade",
    "conformidade garantida",
    "certificado de conformidade",
    "conforme DORA",
    "cumpre DORA",
    "conforme RGPD",
    "cumpre RGPD",
    "conforme AI Act",
    "aprovado pelo regulador",
    "aprovação regulatória",
    "determinação legal",
    "decisão legal",
    "garante previsão",
    "previsão garantida",
    "probabilidade de vitória",
    "vencedor provável",
    "substitui revisão humana",
    "substitui revisão legal",
    "substitui compliance",
    "torna a IA segura",
    "segurança garantida",
    "valida a física",
    "validação de solver",
    "aprovação automática de design",
]

BLOCKED_PUBLIC_HTML_CLAIMS = [
    "production ready",
    "production-ready",
    "production deployment achieved",
    "customer pilot executed",
    "customer findings",
    "customer data used",
    "production data used",
    "live telemetry enabled",
    "connector execution enabled",
    "CP-7 authorized",
    "legally compliant",
    "regulatory certified",
    "security certified",
    "guaranteed compliance",
    "guaranteed ROI",
    "guaranteed savings",
    "realized savings",
    "avoided liability",
    "IBM endorsement",
    "IBM partnership",
    "IBM Engineering AI Hub integration",
    "live watsonx Orchestrate integration",
    "live Manta integration",
    "live Db2 integration",
    "only TrustGate",
    "Codex",
    "TGVIDEO",
    "TG360-EVID",
    "dados de clientes usados",
    "dados de produção usados",
    "telemetria em direto ativada",
    "execução de conectores ativada",
    "CP-7 autorizado",
    "legalmente conforme",
    "certificado regulatoriamente",
    "certificado de segurança",
    "ROI garantido",
    "poupanças garantidas",
    "responsabilidade evitada",
    "endosso IBM",
    "parceria IBM",
    "integração IBM Engineering AI Hub",
    "integração em direto com watsonx Orchestrate",
    "integração em direto com Manta",
    "integração em direto com Db2",
]

GUARDRAIL_WORDS = [
    "blocked",
    "forbidden",
    "not claimed",
    "what is not claimed",
    "not a ",
    "not an ",
    "not live",
    "not automated",
    "not automatic",
    "not to ",
    "no ",
    "do not",
    "does not",
    "without",
    "avoid",
    "avoids",
    "boundary",
    "boundaries",
    "risk if overclaimed",
    "unsupported",
    "stays private",
    "stay private",
    "must not",
    "bloqueado",
    "proibido",
    "não ",
    "nao ",
    "não é",
    "sem ",
    "o que não é afirmado",
    "não afirma",
    "não substitui",
    "não automatiza",
]

ALLOWED_EXTERNAL_HREFS = {
    "https://www.linkedin.com/in/pedrobarbas/",
}

PAGE_NAV_LABELS = {
    "index.html": ["Home", "Procurement", "AI Control", "Boundaries", "Contact"],
    "procurement/index.html": ["Procurement", "Boundaries", "Contact"],
    "ai-control/index.html": ["AI Control", "Boundaries", "Contact"],
    "pt/index.html": ["Início", "Procurement", "Controlo IA", "Limites", "Contacto"],
    "pt/procurement/index.html": ["Procurement", "Limites", "Contacto"],
    "pt/ai-control/index.html": ["Controlo IA", "Limites", "Contacto"],
}

FORBIDDEN_NAV_FOOTER_LABELS = {
    "procurement/index.html": ["Home", "AI Control", "AI Control track", "Procurement track", "Deal Hunter track"],
    "ai-control/index.html": ["Home", "Procurement", "Procurement track", "Deal Hunter track"],
    "pt/procurement/index.html": ["Início", "Home", "AI Control", "Controlo IA", "Controlo de IA", "AI Control track", "Procurement track", "Deal Hunter track"],
    "pt/ai-control/index.html": ["Início", "Home", "Procurement", "Procurement track", "Deal Hunter track"],
}

FORBIDDEN_TRACK_HREFS = {
    "procurement/index.html": {"../", "/", "../ai-control/", "/ai-control/", "ai-control/"},
    "ai-control/index.html": {"../", "/", "../procurement/", "/procurement/", "procurement/"},
    "pt/procurement/index.html": {"/pt/", "/pt/ai-control/", "/ai-control/", "../ai-control/", "ai-control/"},
    "pt/ai-control/index.html": {"/pt/", "/pt/procurement/", "/procurement/", "../procurement/", "procurement/"},
}

HTML_LANG = {
    "index.html": '<html lang="en">',
    "procurement/index.html": '<html lang="en">',
    "ai-control/index.html": '<html lang="en">',
    "pt/index.html": '<html lang="pt-PT">',
    "pt/procurement/index.html": '<html lang="pt-PT">',
    "pt/ai-control/index.html": '<html lang="pt-PT">',
}

LANGUAGE_SWITCH_LINKS = {
    "index.html": "/pt/",
    "procurement/index.html": "/pt/procurement/",
    "ai-control/index.html": "/pt/ai-control/",
    "pt/index.html": "/",
    "pt/procurement/index.html": "/procurement/",
    "pt/ai-control/index.html": "/ai-control/",
}

EXPECTED_HREFLANG = {
    "index.html": [("en", "/"), ("pt-PT", "/pt/"), ("x-default", "/")],
    "procurement/index.html": [("en", "/procurement/"), ("pt-PT", "/pt/procurement/")],
    "ai-control/index.html": [("en", "/ai-control/"), ("pt-PT", "/pt/ai-control/")],
    "pt/index.html": [("en", "/"), ("pt-PT", "/pt/"), ("x-default", "/")],
    "pt/procurement/index.html": [("en", "/procurement/"), ("pt-PT", "/pt/procurement/")],
    "pt/ai-control/index.html": [("en", "/ai-control/"), ("pt-PT", "/pt/ai-control/")],
}

ROOT_REQUIRED_TEXT = [
    "EVIDENCE-FIRST SYSTEMS",
    "Choose the right track",
    "Two tracks, one evidence-first operating model",
    "Deal Hunter",
    "PROCUREMENT INTELLIGENCE",
    "AI Control Systems",
    "TrustGate · Certify · Evidra · FieldDelta",
]

PT_ROOT_REQUIRED_TEXT = [
    "Escolha o percurso certo",
    "Dois percursos, um modelo operativo orientado por evidência",
    "Deal Hunter",
    "Sistemas de Controlo de IA",
    "TrustGate · Certify · Evidra · FieldDelta",
]

ROOT_COUNTRY_TEXT_OPTIONS = [
    "Ireland & Portugal",
    "Ireland and Portugal",
]

ROOT_BLOCKED_TEXT = [
    "PUBLIC HUB",
    "Claims & boundaries",
    "Claims and boundaries",
    "Two doors, one primary GTM wedge",
    "PRIMARY COMMERCIAL FOCUS NOW",
    "ASYMMETRIC ROUTER",
    "ACTIVE GTM - IRELAND FIRST - PORTUGAL NEXT",
    "GTM wedge",
    "Ireland first, Portugal next",
    "Ireland first - Portugal next",
]

BLOCKED_PUBLIC_HTML_LANGUAGE = [
    "GTM wedge",
    "primary commercial focus",
    "asymmetric router",
    "active GTM",
    "internal strategy",
    "track is not primary commercial GTM page",
    "two doors, one primary GTM wedge",
    "primary commercial GTM page",
    "active procurement wedge",
]

PROCUREMENT_REQUIRED_TEXT = [
    "The tender is not the beginning of the opportunity. It is often the moment everyone else sees it too.",
    "What is not claimed",
    "Ireland is the first buyer-conversation path",
    "opportunity tracking",
    "pre-tender",
]

PROCUREMENT_REQUIRED_TEXT_OPTIONS = [
    [
        "source-backed opportunity trail",
        "source-backed review model",
    ],
]

PROCUREMENT_BLOCKED_LANGUAGE = [
    "Project identity",
    "project identity",
    "Evidence chain",
    "evidence chain",
    "governed intelligence control plane",
    "control plane",
    "Country-pack architecture",
    "country-pack architecture",
    "synthetic evidence packs",
    "upstream evidence",
    "upstream opportunity",
    "canonical identity",
    "principal continuity",
    "deterministic",
]

AI_CONTROL_REQUIRED_TEXT = [
    "TrustGate Sovereign",
    "execution firewall for agentic AI",
    "A governed deployment and a governed platform do not automatically authorize a specific action",
    "A governed airport does not mean every flight may take off",
    "Principal",
    "Action",
    "Context",
    "Route",
    "Admission",
    "Telemetry",
    "Proof",
    "Held Gate",
    "TG360",
    "evidence cockpit",
    "TGSG",
    "tool and capability trust",
    "knowledge and retrieval authority",
    "content and document integrity",
    "workflow and autonomy boundaries",
    "budget and latency envelopes",
    "multi-agent provenance",
    "watsonx Orchestrate",
    "Manta",
    "Db2",
    "Illustrative example only",
    "no live watsonx Orchestrate, Manta, or Db2 integration",
    "no production deployment claim",
    "no compliance certification",
    "no customer traction claim",
    "no replacement for human review",
    "TrustGate",
    "Certify",
    "Evidra",
    "FieldDelta",
]

PT_PROCUREMENT_REQUIRED_TEXT = [
    "O tender não é o início da oportunidade. Muitas vezes, é o momento em que todos os outros também a veem.",
    "O que não é afirmado",
    "Irlanda primeiro. Portugal a seguir.",
    "pré-concurso",
    "trilho de oportunidade suportado por fontes",
]

PT_AI_CONTROL_REQUIRED_TEXT = [
    "TrustGate Sovereign",
    "firewall de execução para IA agêntica",
    "Uma implantação governada e uma plataforma governada não autorizam automaticamente uma ação específica",
    "Um aeroporto governado não significa que todos os voos possam descolar",
    "Principal",
    "Ação",
    "Contexto",
    "Rota",
    "Admissão",
    "Telemetria",
    "Prova",
    "Porta mantida",
    "TG360",
    "cockpit de evidência",
    "TGSG",
    "confiança de ferramentas e capacidades",
    "autoridade de conhecimento e recuperação",
    "integridade de conteúdos e documentos",
    "limites de workflow e autonomia",
    "envelopes de orçamento e latência",
    "proveniência multiagente",
    "watsonx Orchestrate",
    "Manta",
    "Db2",
    "Exemplo ilustrativo",
    "não reivindica integração em direto com watsonx Orchestrate, Manta ou Db2",
    "sem reivindicação de implantação em produção",
    "sem certificação de conformidade",
    "sem reivindicação de tração com clientes",
    "não substitui revisão humana",
    "TrustGate",
    "Certify",
    "Evidra",
    "FieldDelta",
    "Sistemas de Controlo",
]

SEO_REQUIREMENTS = [
    "<title>",
    'name="description"',
    'property="og:title"',
    'property="og:description"',
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_repo_files() -> list[Path]:
    ignored_dirs = {".git", "__pycache__"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in ignored_dirs for part in path.parts):
            continue
        if path.is_file():
            files.append(path)
    return files


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def add_error(errors: list[str], message: str) -> None:
    errors.append(f"FAIL: {message}")


def normalize_label(value: str) -> str:
    text = re.sub(r"<[^>]+>", "", value)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def extract_anchor_links(fragment: str) -> list[tuple[str, str]]:
    anchor_pattern = re.compile(r"""<a\b([^>]*)>(.*?)</a>""", re.IGNORECASE | re.DOTALL)
    href_pattern = re.compile(r"""href=["']([^"']+)["']""", re.IGNORECASE)
    links: list[tuple[str, str]] = []
    for match in anchor_pattern.finditer(fragment):
        attrs = match.group(1)
        href_match = href_pattern.search(attrs)
        href = href_match.group(1) if href_match else ""
        links.append((href, normalize_label(match.group(2))))
    return links


def extract_nav_fragments(text: str) -> dict[str, list[str]]:
    header_navs = re.findall(
        r"""<div\b[^>]*class=["'][^"']*\bnav-links\b[^"']*["'][^>]*>(.*?)</div>""",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    footer_navs = re.findall(
        r"""<footer\b.*?<nav\b[^>]*>(.*?)</nav>.*?</footer>""",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    return {"header": header_navs, "footer": footer_navs}


def check_page_navigation(errors: list[str], relative: str, text: str) -> None:
    expected_labels = PAGE_NAV_LABELS[relative]
    fragments_by_area = extract_nav_fragments(text)
    all_nav_footer_links: list[tuple[str, str]] = []

    for area, fragments in fragments_by_area.items():
        if not fragments:
            add_error(errors, f"{area.title()} navigation missing in {relative}")
            continue

        links = extract_anchor_links(fragments[0])
        labels = [label for _, label in links]
        all_nav_footer_links.extend(links)
        if labels != expected_labels:
            add_error(errors, f"{area.title()} navigation labels in {relative} must be {expected_labels}; found {labels}")

    forbidden_labels = {label.lower() for label in FORBIDDEN_NAV_FOOTER_LABELS.get(relative, [])}
    for _, label in all_nav_footer_links:
        if label.lower() in forbidden_labels:
            add_error(errors, f"Forbidden nav/footer label in {relative}: {label}")


def check_language_metadata(errors: list[str], relative: str, text: str) -> None:
    if HTML_LANG[relative] not in text:
        add_error(errors, f"HTML lang attribute incorrect in {relative}: expected {HTML_LANG[relative]}")

    for hreflang, href in EXPECTED_HREFLANG[relative]:
        pattern = rf"""<link\b[^>]*rel=["']alternate["'][^>]*hreflang=["']{re.escape(hreflang)}["'][^>]*href=["']{re.escape(href)}["']"""
        if not re.search(pattern, text, re.IGNORECASE):
            add_error(errors, f"Missing hreflang alternate in {relative}: {hreflang} -> {href}")


def check_language_switcher(errors: list[str], relative: str, text: str) -> None:
    if "language-switcher" not in text:
        add_error(errors, f"Language switcher missing in {relative}")
    if "EN" not in text or "PT" not in text:
        add_error(errors, f"Language switcher labels missing in {relative}")
    if "aria-label" not in text:
        add_error(errors, f"Accessible language switcher label missing in {relative}")
    if 'aria-current="true"' not in text:
        add_error(errors, f"Current language indicator missing in {relative}")

    expected_href = LANGUAGE_SWITCH_LINKS[relative]
    if f'href="{expected_href}"' not in text:
        add_error(errors, f"Language switcher target missing in {relative}: {expected_href}")


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def check_required_files(errors: list[str]) -> None:
    for required in REQUIRED_FILES + REQUIRED_SVGS:
        path = ROOT / required
        if not path.exists():
            add_error(errors, f"Required file missing: {required}")
        elif path.is_file() and not read_text(path).strip():
            add_error(errors, f"Required file is empty: {required}")


def check_page_content(errors: list[str]) -> None:
    page_requirements = {
        "index.html": ROOT_REQUIRED_TEXT,
        "procurement/index.html": PROCUREMENT_REQUIRED_TEXT,
        "ai-control/index.html": AI_CONTROL_REQUIRED_TEXT,
        "pt/index.html": PT_ROOT_REQUIRED_TEXT,
        "pt/procurement/index.html": PT_PROCUREMENT_REQUIRED_TEXT,
        "pt/ai-control/index.html": PT_AI_CONTROL_REQUIRED_TEXT,
    }

    for relative in HTML_PAGES:
        path = ROOT / relative
        if not path.exists():
            continue
        text = read_text(path)
        lower = text.lower()
        visible_text = html.unescape(text)
        visible_lower = visible_text.lower()

        check_language_metadata(errors, relative, text)
        check_language_switcher(errors, relative, text)

        for marker in SEO_REQUIREMENTS:
            if marker.lower() not in lower:
                add_error(errors, f"SEO marker missing in {relative}: {marker}")

        for required in page_requirements[relative]:
            haystack = visible_lower if relative == "index.html" else visible_text
            needle = required.lower() if relative == "index.html" else required
            if needle not in haystack:
                add_error(errors, f"Required page content missing in {relative}: {required}")

        if relative == "procurement/index.html":
            for blocked in PROCUREMENT_BLOCKED_LANGUAGE:
                if blocked in visible_text:
                    add_error(errors, f"Procurement page contains architecture-native language: {blocked}")
            for options in PROCUREMENT_REQUIRED_TEXT_OPTIONS:
                if not any(option in visible_text for option in options):
                    add_error(errors, f"Procurement page missing buyer-native wording option: {' or '.join(options)}")

        if relative == "index.html":
            if not any(option.lower() in visible_lower for option in ROOT_COUNTRY_TEXT_OPTIONS):
                add_error(errors, "Root page missing homepage country wording: Ireland & Portugal or Ireland and Portugal")
            for blocked in ROOT_BLOCKED_TEXT:
                if blocked.lower() in visible_lower:
                    add_error(errors, f"Blocked root page language present: {blocked}")

        for blocked in BLOCKED_PUBLIC_HTML_LANGUAGE:
            if blocked.lower() in visible_lower:
                add_error(errors, f"Blocked public-facing language in {relative}: {blocked}")

        for blocked_label in ["claims & boundaries", "claims and boundaries"]:
            if blocked_label in visible_lower:
                add_error(errors, f"Public HTML page must use Boundaries label only in {relative}")

        if 'id="boundaries"' not in text:
            add_error(errors, f"Boundaries section missing id in {relative}")
        if 'id="contact"' not in text:
            add_error(errors, f"Contact section missing id in {relative}")

        check_page_navigation(errors, relative, text)

        if 'href="#boundaries"' not in text:
            add_error(errors, f"Boundaries nav link missing in {relative}")
        if 'href="#contact"' not in text:
            add_error(errors, f"Contact nav link missing in {relative}")


def check_route_links(errors: list[str]) -> None:
    root = read_text(ROOT / "index.html") if (ROOT / "index.html").exists() else ""
    if 'href="procurement/"' not in root:
        add_error(errors, "Root page missing internal link to procurement/")
    if 'href="ai-control/"' not in root:
        add_error(errors, "Root page missing internal link to ai-control/")

    pt_root = read_text(ROOT / "pt/index.html") if (ROOT / "pt/index.html").exists() else ""
    if 'href="/pt/procurement/"' not in pt_root:
        add_error(errors, "Portuguese root page missing internal link to /pt/procurement/")
    if 'href="/pt/ai-control/"' not in pt_root:
        add_error(errors, "Portuguese root page missing internal link to /pt/ai-control/")

    for relative in ["procurement/index.html", "ai-control/index.html", "pt/procurement/index.html", "pt/ai-control/index.html"]:
        path = ROOT / relative
        if not path.exists():
            continue
        text = read_text(path)
        forbidden_hrefs = FORBIDDEN_TRACK_HREFS[relative]
        for href, label in extract_anchor_links(text):
            local_href = normalize_local_reference(href)
            if local_href in forbidden_hrefs:
                add_error(errors, f"Forbidden isolated-track link in {relative}: {label or href} -> {href}")


def check_disallowed_files(errors: list[str]) -> None:
    for path in iter_repo_files():
        name = path.name
        suffix = path.suffix.lower()
        if name in SECRET_NAMES:
            add_error(errors, f"Obvious secret file is present: {rel(path)}")
        if any(fnmatch.fnmatch(name, pattern) for pattern in SECRET_PATTERNS):
            add_error(errors, f"Potential secret file is present: {rel(path)}")
        if suffix == ".pdf":
            add_error(errors, f"PDF committed: {rel(path)}")
        if suffix in BINARY_IMAGE_SUFFIXES:
            add_error(errors, f"Raster image committed for this static surface: {rel(path)}")


def check_external_js_css_fonts(errors: list[str]) -> None:
    external_script = re.compile(r"""<script\b[^>]*\bsrc=["']https?://""", re.IGNORECASE)
    external_link = re.compile(r"""<link\b[^>]*\bhref=["']https?://""", re.IGNORECASE)
    css_external = re.compile(r"""@import\s+|url\(["']?https?://|@font-face""", re.IGNORECASE)
    font_domains = ["fonts.googleapis", "fonts.gstatic", "typekit", "use.typekit"]

    for path in iter_repo_files():
        if path.suffix.lower() in {".html", ".md"}:
            text = read_text(path)
            for match in external_script.finditer(text):
                add_error(errors, f"External JavaScript reference in {rel(path)}:{line_number(text, match.start())}")
            for match in external_link.finditer(text):
                add_error(errors, f"External CSS/font link in {rel(path)}:{line_number(text, match.start())}")
            lower = text.lower()
            for domain in font_domains:
                if domain in lower:
                    add_error(errors, f"External font reference '{domain}' found in {rel(path)}")

        if path.suffix.lower() == ".css":
            text = read_text(path)
            for match in css_external.finditer(text):
                add_error(errors, f"External CSS/font construct in {rel(path)}:{line_number(text, match.start())}")


def check_analytics_keywords(errors: list[str]) -> None:
    for path in iter_repo_files():
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if rel(path).startswith("scripts/"):
            continue
        lower = read_text(path).lower()
        for keyword in ANALYTICS_KEYWORDS:
            if keyword in lower:
                add_error(errors, f"Analytics keyword '{keyword}' found in {rel(path)}")


def check_forms_and_cookies(errors: list[str]) -> None:
    for path in iter_repo_files():
        if path.suffix.lower() not in {".html", ".css", ".svg"}:
            continue
        text = read_text(path)
        if path.suffix.lower() == ".html" and re.search(r"<form\b", text, re.IGNORECASE):
            add_error(errors, f"Form element found in {rel(path)}")
        lower = text.lower()
        for pattern in COOKIE_CODE_PATTERNS:
            if pattern in lower:
                add_error(errors, f"Cookie-related code '{pattern}' found in {rel(path)}")


def context_allows_claim(context: str) -> bool:
    lower = context.lower()
    return any(word in lower for word in GUARDRAIL_WORDS)


def check_blocked_claims(errors: list[str]) -> None:
    scan_files = [path for path in iter_repo_files() if path.suffix.lower() in {".html", ".md"}]
    for path in scan_files:
        relative = rel(path)
        blocked_claims = BLOCKED_PUBLIC_CLAIMS + BLOCKED_PORTUGUESE_CLAIMS
        if relative in HTML_PAGES:
            blocked_claims = blocked_claims + BLOCKED_PUBLIC_HTML_CLAIMS
        lines = read_text(path).splitlines()
        for index, line in enumerate(lines):
            lower_line = line.lower()
            for phrase in blocked_claims:
                if phrase.lower() not in lower_line:
                    continue
                start = max(0, index - 10)
                end = min(len(lines), index + 6)
                context = "\n".join(lines[start:end])
                if context_allows_claim(context):
                    continue
                add_error(errors, f"Blocked claim '{phrase}' lacks guardrail context in {relative}:{index + 1}")


def check_svg_files(errors: list[str]) -> None:
    assets_dir = ROOT / "assets"
    if not assets_dir.exists():
        add_error(errors, "Assets directory missing")
        return

    for path in sorted(assets_dir.glob("*.svg")):
        text = read_text(path)
        lower = text.lower()
        if re.search(r"""(?:href|xlink:href)=["']https?://""", text, re.IGNORECASE):
            add_error(errors, f"External href found in SVG: {rel(path)}")
        if "url(http://" in lower or "url(https://" in lower:
            add_error(errors, f"External URL reference found in SVG: {rel(path)}")
        if re.search(r"<script\b", text, re.IGNORECASE):
            add_error(errors, f"Script tag found in SVG: {rel(path)}")
        if re.search(r"<foreignobject\b", text, re.IGNORECASE):
            add_error(errors, f"foreignObject found in SVG: {rel(path)}")
        if not re.search(r"<title\b[^>]*>.*?</title>", text, re.IGNORECASE | re.DOTALL):
            add_error(errors, f"SVG missing <title>: {rel(path)}")
        if not re.search(r"<desc\b[^>]*>.*?</desc>", text, re.IGNORECASE | re.DOTALL):
            add_error(errors, f"SVG missing <desc>: {rel(path)}")


def normalize_local_reference(value: str) -> str:
    return value.split("#", 1)[0].split("?", 1)[0]


def check_html_links_and_assets(errors: list[str]) -> None:
    attr_pattern = re.compile(r"""(?:src|href)=["']([^"']+)["']""", re.IGNORECASE)

    for relative in HTML_PAGES:
        path = ROOT / relative
        if not path.exists():
            continue
        text = read_text(path)
        ids = set(re.findall(r"""\bid=["']([^"']+)["']""", text))

        for match in attr_pattern.finditer(text):
            value = match.group(1)
            if value.startswith("#"):
                anchor = value[1:]
                if anchor and anchor not in ids:
                    add_error(errors, f"Broken internal anchor in {relative}: #{anchor}")
                continue
            if value.startswith("mailto:"):
                continue
            if value.startswith("http://") or value.startswith("https://"):
                if value not in ALLOWED_EXTERNAL_HREFS:
                    add_error(errors, f"Unexpected external link or asset in {relative}:{line_number(text, match.start())}: {value}")
                continue
            if value.startswith("javascript:") or value.startswith("data:"):
                add_error(errors, f"Disallowed URL scheme in {relative}:{line_number(text, match.start())}: {value}")
                continue

            local_value = normalize_local_reference(value)
            if not local_value:
                continue
            if local_value.startswith("/"):
                target = (ROOT / local_value.lstrip("/")).resolve()
            else:
                target = (path.parent / local_value).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                add_error(errors, f"Reference escapes repo root in {relative}: {value}")
                continue
            if not target.exists():
                add_error(errors, f"Missing local reference in {relative}: {value}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_page_content(errors)
    check_route_links(errors)
    check_disallowed_files(errors)
    check_external_js_css_fonts(errors)
    check_analytics_keywords(errors)
    check_forms_and_cookies(errors)
    check_blocked_claims(errors)
    check_svg_files(errors)
    check_html_links_and_assets(errors)

    if errors:
        print("Public surface validation: FAIL")
        for error in errors:
            print(error)
        print(f"Summary: {len(errors)} failure(s)")
        return 1

    print("Public surface validation: PASS")
    print(f"Required files checked: {len(REQUIRED_FILES)}")
    print(f"HTML pages checked: {len(HTML_PAGES)}")
    print("Bilingual route, SEO, language switcher, persona-specific nav, TrustGate Sovereign content, procurement language, Boundaries, Contact, safety, claim, SVG, and local link checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
