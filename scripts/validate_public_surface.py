#!/usr/bin/env python3
"""Validate the public-safe static website surface."""

from __future__ import annotations

import fnmatch
import html
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
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
    "404.html",
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
    "docs/PUBLIC_SURFACE_PHASE_3_1_DISCOVERY_AND_CLAIMS_MAP.md",
    "docs/PUBLIC_SURFACE_PHASE_3_1_HANDOFF.md",
    "docs/PUBLIC_SURFACE_PHASE_3_1R3R1_HANDOFF.md",
    "docs/codex_runs/20260608_phase_2_1_hub_public_language_qa_handoff.md",
    "docs/codex_runs/20260608_phase_2_2_homepage_public_language_correction_handoff.md",
    "docs/codex_runs/20260714_phase_3_2_cloudflare_404_hardening_handoff.md",
    "scripts/validate_public_surface.py",
]

CLOUDFLARE_BUILD_COMMAND = (
    "set -eu; rm -rf dist; mkdir -p dist; cp index.html 404.html styles.css dist/; "
    "cp -R assets procurement ai-control pt dist/; test -f dist/index.html; "
    "test -f dist/404.html; test -f dist/styles.css; test -f dist/assets/favicon.svg; "
    "test -f dist/procurement/index.html; test -f dist/ai-control/index.html; "
    "test -f dist/pt/index.html; test -f dist/pt/procurement/index.html; "
    "test -f dist/pt/ai-control/index.html"
)

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
    "assets/trustgate-sovereign-execution-firewall-pt.svg",
    "assets/trustgate-sovereign-working-example.svg",
    "assets/trustgate-sovereign-working-example-pt.svg",
    "assets/tg360-evidence-cockpit.svg",
    "assets/tg360-evidence-cockpit-pt.svg",
    "assets/trustgate-action-clearance-chain-en-v2.svg",
    "assets/trustgate-action-clearance-chain-pt-v2.svg",
    "assets/trustgate-enterprise-verification-chain-en-v2.svg",
    "assets/trustgate-enterprise-verification-chain-pt-v2.svg",
    "assets/tg360-evidence-cockpit-en-v2.svg",
    "assets/tg360-evidence-cockpit-pt-v2.svg",
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
    "production enforcement",
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
    "The action-clearance and proof layer for consequential agentic AI.",
    "A governed deployment and a governed platform do not automatically authorize a specific action",
    "A decision alone is not execution authority",
    "Demonstrated through a bounded local reference path. No production enforcement, customer deployment, cross-process security guarantee or enterprise-wide non-bypassability is claimed.",
    "The decision is verified where the change would occur",
    "Invalid, altered, reused or stale clearance is rejected before the target changes",
    "A cleared flight still needs its clearance verified before entering the protected runway",
    "Principal",
    "Purpose",
    "Action",
    "Target",
    "Route",
    "Evidence",
    "Impact",
    "Policy",
    "Clearance",
    "Receipt",
    "Target Verification",
    "Outcome Proof",
    "TG360",
    "evidence cockpit",
    "TG360 displays the accepted local evidence chain",
    "it does not become a second decision engine",
    "TG360 also shows whether the bounded reference target changed or remained unchanged after the accepted or rejected action.",
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
    "Illustrative enterprise-stack example only",
    "not limited to that stack",
    "LangGraph",
    "Microsoft Copilot Studio",
    "Amazon Bedrock AgentCore",
    "not a single vendor stack",
    "Illustrated with an IBM enterprise stack",
    "No live, certified, supported, endorsed, production or partner integration is claimed",
    "DORA-relevant operational-resilience evidence",
    "TrustGate supports DORA-oriented control evidence. It does not independently determine regulatory compliance.",
    "Data-protection accountability lens",
    "It does not replace a DPIA, lawful-basis assessment, records of processing, DPO judgement or legal determination",
    "Review-ready evidence posture",
    "Protected-target assurance",
    "Operational-resilience evidence",
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
    "A camada de autorização da ação e prova para IA agêntica empresarial.",
    "Uma implementação governada e uma plataforma governada não autorizam automaticamente uma ação específica",
    "Uma decisão, por si só, não constitui autoridade de execução",
    "Demonstrado através de um percurso de referência local e delimitado. Não é reivindicada aplicação em produção, implementação num cliente, garantia de segurança entre processos ou não contornabilidade a nível empresarial.",
    "A decisão é validada onde a alteração ocorreria",
    "Uma autorização inválida, alterada, reutilizada ou desatualizada é rejeitada antes de o sistema-alvo mudar",
    "Um voo autorizado continua a necessitar de validação da sua autorização antes de entrar na pista protegida",
    "Principal",
    "Propósito",
    "Ação",
    "Sistema-alvo",
    "Rota",
    "Evidência",
    "Impacto",
    "Política",
    "Autorização",
    "Recibo",
    "Validação do sistema-alvo",
    "Prova do resultado",
    "TG360",
    "cockpit de evidência",
    "O TG360 apresenta a cadeia de evidência local aceite",
    "não se torna um segundo motor de decisão",
    "O TG360 também mostra se o sistema-alvo de referência delimitado foi alterado ou permaneceu inalterado após a ação aceite ou rejeitada.",
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
    "não se limita a esta stack",
    "LangGraph",
    "Microsoft Copilot Studio",
    "Amazon Bedrock AgentCore",
    "não de uma única stack de fornecedor",
    "Ilustrado com uma stack empresarial IBM",
    "Não é reivindicada qualquer integração ativa, certificada, suportada, recomendada, de produção ou de parceria",
    "Evidência de resiliência operacional relevante para DORA",
    "A TrustGate apoia evidência de controlo orientada para DORA. Não determina, por si só, a conformidade regulamentar.",
    "Perspetiva de responsabilização em proteção de dados",
    "Não substitui uma AIPD/DPIA, a avaliação da base de licitude, os registos de atividades de tratamento, o julgamento do EPD/DPO ou uma determinação jurídica",
    "Postura de evidência preparada para análise",
    "Garantia do sistema-alvo protegido",
    "Evidência de resiliência operacional",
    "sem reivindicação de implantação em produção",
    "sem certificação de conformidade",
    "sem reivindicação de tração com clientes",
    "não substitui revisão humana",
    "TrustGate",
    "Certify",
    "Evidra",
    "FieldDelta",
]

AI_CONTROL_PROHIBITED_VISIBLE = [
    "the execution firewall for agentic ai",
    "execution firewall",
    "unique",
    "first of its kind",
    "only solution",
    "market-leading",
    "production ready",
    "customer deployed",
    "dora compliant",
    "dora certified",
    "gdpr compliant",
    "certified compliant",
    "guaranteed control",
    "enterprise-wide non-bypassability",
    "unbypassable",
    "audit-ready",
    "roi guaranteed",
    "realised savings",
    "avoided liability",
    "live connector",
    "live telemetry",
    "live db2 integration",
    "live manta integration",
    "live watsonx integration",
    "firewall de execução",
    "pronta para auditoria",
]

AI_CONTROL_ALLOWED_BOUNDARY_PHRASES = [
    "No production enforcement, customer deployment, cross-process security guarantee or enterprise-wide non-bypassability is claimed.",
    "no live telemetry claim",
    "no guaranteed compliance",
]

PT_AI_CONTROL_ALLOWED_BOUNDARY_PHRASES = [
    "Não é reivindicada aplicação em produção, implementação num cliente, garantia de segurança entre processos ou não contornabilidade a nível empresarial.",
]

AI_CONTROL_INTERNAL_TERMS = [
    "TGCB",
    "TGOS",
    "TGPE",
    "TGAPI",
    "CACSAC",
    "acceptance tag",
    "internal evidence ID",
    "private API schema",
    "receipt consumption register",
    "certifier registry",
    "reason-code catalogue",
    "canonical digest preimage",
    "src/trustgate_core",
    "artifacts/tg",
    "/Users/",
    "Codex",
]

PAGE_METADATA_CONTRACTS = {
    "index.html": (
        "Pedro Barbas | Evidence-first systems",
        "Evidence-first systems for procurement intelligence, AI control, and reviewable proof.",
    ),
    "procurement/index.html": (
        "Deal Hunter | Procurement Intelligence for Ireland and Portugal",
        "Deal Hunter helps infrastructure and procurement teams review earlier source-backed opportunity context before the formal tender becomes the only visible signal.",
    ),
    "ai-control/index.html": (
        "TrustGate Sovereign | Action clearance and proof for agentic AI",
        "TrustGate evaluates whether one exact consequential agentic action may proceed, binds the decision into evidence, and supports protected-target verification before state change.",
    ),
    "pt/index.html": (
        "Pedro Barbas | Sistemas orientados por evidência",
        "Sistemas orientados por evidência para inteligência de procurement, controlo de IA e prova passível de revisão.",
    ),
    "pt/procurement/index.html": (
        "Deal Hunter | Inteligência de procurement para a Irlanda e Portugal",
        "Deal Hunter ajuda equipas de infraestrutura e procurement a rever contexto de oportunidade mais cedo, suportado por fontes, antes de o tender formal se tornar o único sinal visível.",
    ),
    "pt/ai-control/index.html": (
        "TrustGate Sovereign | Autorização da ação e prova para IA agêntica",
        "A TrustGate avalia se uma ação agêntica específica pode prosseguir, vincula a decisão a evidência e apoia a validação pelo sistema-alvo protegido antes da alteração de estado.",
    ),
}

EN_PROTECTED_TARGET_BOUNDARY = (
    "Demonstrated through a bounded local reference path. No production enforcement, customer deployment, "
    "cross-process security guarantee or enterprise-wide non-bypassability is claimed."
)

PT_PROTECTED_TARGET_BOUNDARY = (
    "Demonstrado através de um percurso de referência local e delimitado. Não é reivindicada aplicação em produção, "
    "implementação num cliente, garantia de segurança entre processos ou não contornabilidade a nível empresarial."
)

EN_TG360_TARGET_CHANGE = (
    "TG360 also shows whether the bounded reference target changed or remained unchanged after the accepted or rejected action."
)

PT_TG360_TARGET_CHANGE = (
    "O TG360 também mostra se o sistema-alvo de referência delimitado foi alterado ou permaneceu inalterado após a ação aceite ou rejeitada."
)

ACCESSIBILITY_PROHIBITED_CLAIMS = [
    "execution firewall",
    "DORA compliant",
    "DORA certified",
    "GDPR compliant",
    "production ready",
    "customer deployed",
    "enterprise-wide non-bypassability",
    "unbypassable",
    "unique",
    "first of its kind",
    "only solution",
    "market-leading",
    "audit-ready",
    "guaranteed compliance",
    "guaranteed control",
    "ROI guaranteed",
    "realised savings",
]

RUNTIME_STORAGE_PATTERNS = [
    "fetch(",
    "XMLHttpRequest",
    "WebSocket",
    "EventSource",
    "sendBeacon",
    "navigator.sendBeacon",
    "localStorage",
    "sessionStorage",
    "indexedDB",
    "document.cookie",
    "javascript:",
]

APPROVED_STATIC_HTTPS_LINKS = ALLOWED_EXTERNAL_HREFS

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


def not_found_contract_failures(text: str) -> list[str]:
    failures: list[str] = []
    parser = parse_public_html(text)
    required_patterns = {
        "English document language": r'<html\s+lang="en"',
        "noindex robots directive": r'<meta\b[^>]*name="robots"[^>]*content="noindex"',
        "root-relative stylesheet": r'<link\b[^>]*rel="stylesheet"[^>]*href="/styles\.css"',
        "root-relative favicon": r'<link\b[^>]*rel="icon"[^>]*href="/assets/favicon\.svg"',
        "homepage link": r'<a\b[^>]*href="/"',
    }
    for label, pattern in required_patterns.items():
        if not re.search(pattern, text, re.IGNORECASE):
            failures.append(f"404 page missing {label}")
    if "Page not found" not in parser.title or "This page could not be found." not in visible_text(text):
        failures.append("404 page missing clear page-not-found title or heading")
    if parser.scripts:
        failures.append("404 page must not contain JavaScript")

    prohibited = ["docs/", "scripts/", "codex_runs", "private repository", "support request", "source code", "deployment internals"]
    lower = html.unescape(text).casefold()
    for term in prohibited:
        if term.casefold() in lower:
            failures.append(f"404 page exposes prohibited internal language: {term}")

    for attribute, value in re.findall(r'\b(href|src)="([^"]+)"', text, re.IGNORECASE):
        lowered = value.casefold()
        if lowered.startswith(("http://", "https://", "//", "javascript:")):
            failures.append(f"404 page contains external or executable {attribute}: {value}")
        elif not value.startswith(("/", "#")):
            failures.append(f"404 page contains directory-dependent {attribute}: {value}")
    return failures


def check_not_found_page(errors: list[str]) -> None:
    path = ROOT / "404.html"
    if not path.exists():
        return
    for failure in not_found_contract_failures(read_text(path)):
        add_error(errors, failure)


def check_cloudflare_package(errors: list[str]) -> None:
    runbook = ROOT / "docs/deployment_runbook.md"
    if runbook.exists() and CLOUDFLARE_BUILD_COMMAND not in read_text(runbook):
        add_error(errors, "Deployment runbook missing exact Cloudflare build command")
    dist = ROOT / "dist"
    if not dist.exists():
        return
    allowed = {"index.html", "404.html", "styles.css", "assets", "procurement", "ai-control", "pt"}
    found = {path.name for path in dist.iterdir()}
    if found != allowed:
        add_error(errors, f"dist/ top-level package must contain only approved public entries; found {sorted(found)}")
    required = [
        "index.html", "404.html", "styles.css", "assets/favicon.svg",
        "procurement/index.html", "ai-control/index.html", "pt/index.html",
        "pt/procurement/index.html", "pt/ai-control/index.html",
    ]
    for relative in required:
        if not (dist / relative).is_file():
            add_error(errors, f"Cloudflare package missing: dist/{relative}")
    for private_name in ("docs", "scripts", "README.md", ".git"):
        if (dist / private_name).exists():
            add_error(errors, f"Private repository entry copied into dist/: {private_name}")


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


def visible_text(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"<(script|style)\b.*?</\1>", "", text, flags=re.IGNORECASE | re.DOTALL)
    return normalize_label(text)


class PublicHTMLInspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.in_title = False
        self.meta: dict[str, str] = {}
        self.headings: list[dict[str, object]] = []
        self.current_heading: dict[str, object] | None = None
        self.images: list[dict[str, str]] = []
        self.links: list[str] = []
        self.anchors: list[dict[str, str]] = []
        self.scripts = 0
        self.event_attributes: list[str] = []
        self.javascript_urls: list[str] = []
        self.claim_surfaces: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        lowered = tag.lower()
        values = {name.lower(): value or "" for name, value in attrs}
        if lowered == "title":
            self.in_title = True
        if lowered == "meta":
            key = values.get("name") or values.get("property")
            if key:
                self.meta[key.lower()] = values.get("content", "")
                self.claim_surfaces.append((f"meta:{key.lower()}", values.get("content", "")))
        if re.fullmatch(r"h[1-6]", lowered):
            self.current_heading = {"level": int(lowered[1]), "text": ""}
            self.headings.append(self.current_heading)
        if lowered == "img":
            self.images.append(values)
        if lowered == "a":
            self.links.append(values.get("href", ""))
            self.anchors.append(values)
        if lowered == "script":
            self.scripts += 1
        for name, value in values.items():
            if name.startswith("on"):
                self.event_attributes.append(name)
            if value.lower().startswith("javascript:"):
                self.javascript_urls.append(value)
            if name in {"alt", "aria-label", "title"} or name.startswith("data-"):
                self.claim_surfaces.append((f"{lowered}[{name}]", value))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        lowered = tag.lower()
        if lowered == "title":
            self.in_title = False
        if re.fullmatch(r"h[1-6]", lowered):
            self.current_heading = None

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.claim_surfaces.append(("text-node", data))
        if self.in_title:
            self.title_parts.append(data)
        if self.current_heading is not None:
            self.current_heading["text"] = str(self.current_heading["text"]) + data

    def handle_comment(self, data: str) -> None:
        self.claim_surfaces.append(("html-comment", data))

    @property
    def title(self) -> str:
        return normalize_label("".join(self.title_parts))


def parse_public_html(text: str) -> PublicHTMLInspector:
    parser = PublicHTMLInspector()
    parser.feed(text)
    parser.close()
    return parser


INTERNAL_PATH_PATTERNS = {"src/trustgate_core", "artifacts/tg", "/Users/"}


def bounded_html_unescape(value: str, rounds: int = 3) -> str:
    decoded = value
    for _ in range(rounds):
        next_value = html.unescape(decoded)
        if next_value == decoded:
            break
        decoded = next_value
    return decoded


def internal_disclosure_matches(value: str) -> list[str]:
    decoded = unicodedata.normalize("NFKC", bounded_html_unescape(value))
    folded = decoded.casefold()
    matches: list[str] = []
    for term in AI_CONTROL_INTERNAL_TERMS:
        if term in INTERNAL_PATH_PATTERNS:
            found = term in decoded
        else:
            found = unicodedata.normalize("NFKC", term).casefold() in folded
        if found:
            matches.append(term)
    return matches


def raw_disclosure_failures(relative: str, text: str) -> list[str]:
    failures: list[str] = []
    for term in internal_disclosure_matches(text):
        failures.append(f"Literal or entity-decoded public source discloses '{term}' in {relative}")
    return failures


def parsed_surface_disclosure_failures(relative: str, parser: PublicHTMLInspector) -> list[str]:
    failures: list[str] = []
    for surface, value in parser.claim_surfaces:
        for term in internal_disclosure_matches(value):
            failures.append(f"Parser-decoded surface {surface} discloses '{term}' in {relative}")
    return failures


def parsed_svg_disclosure_failures(relative: str, text: str) -> list[str]:
    failures: list[str] = []
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        return [f"SVG parse failure in {relative}: {exc}"]
    for element in root.iter():
        tag = element.tag.rsplit("}", 1)[-1]
        surfaces = [(f"svg:{tag}:text", element.text or ""), (f"svg:{tag}:tail", element.tail or "")]
        surfaces.extend((f"svg:{tag}[{name}]", value) for name, value in element.attrib.items())
        for surface, value in surfaces:
            for term in internal_disclosure_matches(value):
                failures.append(f"Parser-decoded surface {surface} discloses '{term}' in {relative}")
    return failures


def parsed_svg_root(text: str) -> ET.Element | None:
    try:
        return ET.fromstring(text)
    except ET.ParseError:
        return None


def svg_public_surface(root: ET.Element) -> str:
    values: list[str] = []
    for element in root.iter():
        values.extend([element.text or "", element.tail or ""])
        for name, value in element.attrib.items():
            if name not in {"id", "data-role", "data-node-id", "data-label-for", "d", "x", "y", "x1", "x2", "y1", "y2", "width", "height", "viewBox"}:
                values.append(value)
    return normalize_label(unicodedata.normalize("NFKC", bounded_html_unescape(" ".join(values))))


SVG_VISUAL_CONTRACTS = {
    "en-hero": ["Proposed action", "TrustGate Sovereign", "action clearance", "Bound receipt", "Protected-target verification", "Accept", "reject", "proof"],
    "pt-hero": ["Ação proposta", "TrustGate Sovereign", "autorização da ação", "Recibo vinculado", "sistema-alvo protegido", "Aceitar", "rejeitar", "Prova do resultado"],
    "pt-enterprise": ["watsonx Orchestrate", "ação proposta", "Manta", "linhagem e contexto", "identidade e autoridade", "autorização", "recibo vinculado", "sistema-alvo protegido", "lado do Db2", "aceite ou rejeitado", "Evidência do resultado"],
    "pt-tg360": ["Cockpit de evidência TG360", "Contexto conhecido", "Âmbito delimitado", "Demonstração sintética", "Não ativado", "Visibilidade da prova", "Sessão privada"],
}

PT_SVG_FORBIDDEN_LABELS = [
    "Agentic request", "Authority", "Scope", "clear", "hold", "execution firewall",
    "known context", "bounded scope", "synthetic demo", "not activated", "proof visibility",
    "walkthrough", "private evidence", "Db2 target", "Illustrative stack example only",
    "lineage/context", "proposed action", "protected-target verification boundary",
]


def svg_visual_contract_failures(kind: str, text: str) -> list[str]:
    failures: list[str] = []
    root = parsed_svg_root(text)
    if root is None:
        return [f"Malformed SVG for visual contract: {kind}"]
    surface = svg_public_surface(root)
    surface_lower = surface.casefold()
    if "execution firewall" in surface_lower:
        failures.append(f"Retired execution-firewall claim in SVG surface: {kind}")

    title = next((normalize_label(element.text or "") for element in root.iter() if element.tag.rsplit("}", 1)[-1] == "title"), "")
    desc = next((normalize_label(element.text or "") for element in root.iter() if element.tag.rsplit("}", 1)[-1] == "desc"), "")
    if not title:
        failures.append(f"Localized SVG title missing: {kind}")
    if not desc:
        failures.append(f"Localized SVG description missing: {kind}")

    for concept in SVG_VISUAL_CONTRACTS.get(kind, []):
        if concept.casefold() not in surface_lower:
            failures.append(f"SVG concept missing in {kind}: {concept}")
    if kind.startswith("pt-"):
        for label in PT_SVG_FORBIDDEN_LABELS:
            if label.casefold() in surface_lower:
                failures.append(f"English operational label in {kind}: {label}")

    if "enterprise" in kind:
        ids = {element.attrib.get("id", "") for element in root.iter()}
        roles = {element.attrib.get("data-role", "") for element in root.iter()}
        node_ids = {element.attrib.get("data-node-id", "") for element in root.iter()}
        for marker in ["trustgate-clearance", "protected-target-verification", "target-outcome"]:
            if f"{marker}-rect" not in ids or marker not in node_ids:
                failures.append(f"Enterprise SVG structural marker missing in {kind}: {marker}")
        for connector in ["clearance-to-verification", "verification-to-outcome", "outcome-to-evidence"]:
            if connector not in roles:
                failures.append(f"Enterprise SVG connector role missing in {kind}: {connector}")
        if any("clearance-to-target" in role or "direct-bypass" in role for role in roles):
            failures.append(f"Direct clearance-to-target bypass connector found in {kind}")

    for element in root.iter():
        tag = element.tag.rsplit("}", 1)[-1]
        if tag == "script":
            failures.append(f"Script element found in SVG contract: {kind}")
        if tag == "image":
            href = element.attrib.get("href", "") or element.attrib.get("{http://www.w3.org/1999/xlink}href", "")
            if href.startswith("http://") or href.startswith("https://"):
                failures.append(f"External image reference found in SVG contract: {kind}")
        for name in element.attrib:
            if name.lower().startswith("on"):
                failures.append(f"Event-handler attribute found in SVG contract: {kind}")
    return failures


AI_VISUAL_ASSET_ROUTES = {
    "ai-control/index.html": [
        "../assets/trustgate-action-clearance-chain-en-v2.svg",
        "../assets/trustgate-enterprise-verification-chain-en-v2.svg",
        "../assets/tg360-evidence-cockpit-en-v2.svg",
    ],
    "pt/ai-control/index.html": [
        "../../assets/trustgate-action-clearance-chain-pt-v2.svg",
        "../../assets/trustgate-enterprise-verification-chain-pt-v2.svg",
        "../../assets/tg360-evidence-cockpit-pt-v2.svg",
    ],
}

RETIRED_AI_VISUAL_ASSETS = [
    "trustgate-sovereign-execution-firewall.svg",
    "trustgate-sovereign-execution-firewall-pt.svg",
    "trustgate-sovereign-working-example.svg",
    "trustgate-sovereign-working-example-pt.svg",
    "tg360-evidence-cockpit.svg",
    "tg360-evidence-cockpit-pt.svg",
]

SVG_VISUAL_PAIRS = [
    ("assets/trustgate-action-clearance-chain-en-v2.svg", "assets/trustgate-action-clearance-chain-pt-v2.svg"),
    ("assets/trustgate-enterprise-verification-chain-en-v2.svg", "assets/trustgate-enterprise-verification-chain-pt-v2.svg"),
    ("assets/tg360-evidence-cockpit-en-v2.svg", "assets/tg360-evidence-cockpit-pt-v2.svg"),
]


def route_visual_contract_failures(relative: str, text: str) -> list[str]:
    failures: list[str] = []
    for expected in AI_VISUAL_ASSET_ROUTES[relative]:
        if f'src="{expected}"' not in text:
            failures.append(f"Required localized visual route missing in {relative}: {expected}")
    for retired in RETIRED_AI_VISUAL_ASSETS:
        if retired in text:
            failures.append(f"Retired AI Control visual reference in {relative}: {retired}")
    parser = parse_public_html(text)
    for anchor in parser.anchors:
        classes = anchor.get("class", "").split()
        if "button" in classes and "primary" in classes:
            if not anchor.get("href", "").strip():
                failures.append(f"Primary CTA has empty destination in {relative}")
            if "disabled" in anchor or anchor.get("aria-disabled", "").lower() == "true":
                failures.append(f"Primary CTA is disabled in {relative}")
            if anchor.get("style", "") and re.search(r"opacity\s*:\s*(?:0(?:\.\d+)?|\.\d+)", anchor["style"], re.IGNORECASE):
                failures.append(f"Primary CTA opacity below 1 in {relative}")
    return failures


def svg_pair_contract_failures(en_text: str, pt_text: str) -> list[str]:
    failures: list[str] = []
    en_root, pt_root = parsed_svg_root(en_text), parsed_svg_root(pt_text)
    if en_root is None or pt_root is None:
        return ["Malformed SVG in bilingual parity pair"]
    if en_root.attrib.get("viewBox") != pt_root.attrib.get("viewBox"):
        failures.append("Bilingual SVG pair has different viewBox")

    def structure(root: ET.Element) -> tuple[dict[str, tuple[str, ...]], list[tuple[str, str]], list[str], list[str], list[str]]:
        nodes: dict[str, tuple[str, ...]] = {}
        connectors: list[tuple[str, str]] = []
        ids: list[str] = []
        roles: list[str] = []
        owners: list[str] = []
        for element in root.iter():
            element_id = element.attrib.get("id", "")
            role = element.attrib.get("data-role", "")
            if element_id:
                ids.append(element_id)
            if role:
                roles.append(role)
            if element.attrib.get("data-label-for"):
                owners.append(element.attrib["data-label-for"])
            if element.tag.rsplit("}", 1)[-1] == "rect" and element.attrib.get("data-node-id"):
                nodes[element.attrib["data-node-id"]] = tuple(element.attrib.get(key, "") for key in ("x", "y", "width", "height", "rx"))
            if element.tag.rsplit("}", 1)[-1] == "path" and element_id:
                connectors.append((element_id, element.attrib.get("d", "")))
        return nodes, connectors, ids, roles, owners

    en_structure, pt_structure = structure(en_root), structure(pt_root)
    labels = ["node geometry", "connector order and routing", "structural IDs", "semantic data-role sequence", "text ownership sequence"]
    for label, en_value, pt_value in zip(labels, en_structure, pt_structure):
        if en_value != pt_value:
            failures.append(f"Bilingual SVG pair differs in {label}")

    for language, root in (("EN", en_root), ("PT", pt_root)):
        node_ids = {element.attrib.get("data-node-id", "") for element in root.iter() if element.attrib.get("data-node-id")}
        for element in root.iter():
            if element.tag.rsplit("}", 1)[-1] == "g" and element.attrib.get("data-role") in {"primary-label", "secondary-label"}:
                owner = element.attrib.get("data-label-for", "")
                if not owner:
                    failures.append(f"{language} SVG text group missing owner marker")
                elif owner not in node_ids:
                    failures.append(f"{language} SVG text group assigned to unknown node: {owner}")
    return failures


def cta_style_contract_failures(css: str) -> list[str]:
    failures: list[str] = []
    primary = re.search(r"\.button\.primary\s*\{([^}]*)\}", css, re.DOTALL)
    if not primary or "opacity: 1" not in primary.group(1) or "color: #ffffff" not in primary.group(1):
        failures.append("Primary CTA must declare active color and opacity")
    visited = re.search(r"\.button\.primary:visited\s*\{([^}]*)\}", css, re.DOTALL)
    if not visited or "color: #ffffff" not in visited.group(1):
        failures.append("Primary CTA visited state must preserve active contrast")
    print_match = re.search(r"@media\s+print\s*\{([\s\S]*)\}\s*$", css)
    if not print_match or not re.search(r"\.button\.primary[^\{]*\{[^}]*opacity\s*:\s*1", print_match.group(1), re.DOTALL):
        failures.append("Print primary CTA must remain fully opaque")
    return failures


def dark_panel_contrast_contract_failures(css: str) -> list[str]:
    failures: list[str] = []
    selector = ".hero-visual > figcaption,\n.hero-visual > .boundary-note"
    screen_match = re.search(r"\.hero-visual\s*>\s*figcaption\s*,\s*\.hero-visual\s*>\s*\.boundary-note\s*\{([^}]*)\}", css, re.DOTALL)
    if not screen_match:
        failures.append("Shared EN/PT dark-panel contrast selector missing")
    else:
        declarations = screen_match.group(1)
        if "color: #edf4f7" not in declarations:
            failures.append("Dark-panel screen text must use the approved light neutral")
        if "opacity: 1" not in declarations:
            failures.append("Dark-panel screen text must remain fully opaque")
        if re.search(r"color\s*:\s*(?:var\(--(?:text|muted)\)|#13202b|#445766)", declarations, re.IGNORECASE):
            failures.append("Dark foreground assigned to dark-panel screen text")

    print_match = re.search(r"@media\s+print\s*\{([\s\S]*)\}\s*$", css)
    print_css = print_match.group(1) if print_match else ""
    print_rule = re.search(r"\.hero-visual\s*>\s*figcaption\s*,\s*\.hero-visual\s*>\s*\.boundary-note\s*\{([^}]*)\}", print_css, re.DOTALL)
    if not print_rule:
        failures.append("Shared EN/PT print contrast selector missing")
    else:
        declarations = print_rule.group(1)
        for marker in ("color: #edf4f7 !important", "opacity: 1", "-webkit-print-color-adjust: exact", "print-color-adjust: exact"):
            if marker not in declarations:
                failures.append(f"Dark-panel print contrast marker missing: {marker}")
        if re.search(r"color\s*:\s*(?:var\(--(?:text|muted)\)|#13202b|#445766)", declarations, re.IGNORECASE):
            failures.append("Dark foreground assigned to dark-panel print text")
    if selector not in css:
        failures.append("Equivalent EN/PT dark-panel treatment is not explicit")
    for rule in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
        selectors, declarations = rule.group(1), rule.group(2)
        if ("hero-visual" in selectors and ("figcaption" in selectors or "boundary-note" in selectors)
                and re.search(r"color\s*:\s*(?:var\(--(?:text|muted)\)|#13202b|#445766)", declarations, re.IGNORECASE)):
            failures.append("Affected dark-panel selector reverts to a dark foreground")
    return failures


def render_evidence_manifest_failures(text: str) -> list[str]:
    failures: list[str] = []
    for language in ("EN", "PT"):
        block_match = re.search(rf"## {language} PDF Evidence\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
        if not block_match:
            failures.append(f"Missing {language} PDF evidence record")
            continue
        block = block_match.group(1)
        for label in ("Path", "SHA-256", "Generated", "Engine", "Page size", "Orientation", "Margins", "Background graphics", "Headers/footers", "Page count"):
            if not re.search(rf"^- {re.escape(label)}: `?[^`\n]+`?$", block, re.MULTILINE):
                failures.append(f"Missing {language} PDF evidence field: {label}")
        hash_match = re.search(r"^- SHA-256: `([0-9a-f]{64})`$", block, re.MULTILINE)
        if not hash_match:
            failures.append(f"Invalid or missing {language} PDF evidence hash")
        count_match = re.search(r"^- Page count: `([1-9][0-9]*)`$", block, re.MULTILINE)
        if not count_match:
            failures.append(f"Reported {language} page count lacks a complete evidence record")
    return failures


def print_contract_failures(css: str) -> list[str]:
    failures: list[str] = []
    required = ["@media print", "break-inside: avoid-page", "page-break-inside: avoid", "break-after: avoid-page", "page-break-after: avoid", ".hero-visual", ".scenario-note", ".sovereign-card"]
    for marker in required:
        if marker not in css:
            failures.append(f"Print contract marker missing: {marker}")
    print_match = re.search(r"@media\s+print\s*\{([\s\S]*)\}\s*$", css)
    if not print_match:
        return failures
    print_css = print_match.group(1)
    for selector in ["main", ".section-band", ".scenario-note", ".accountability-panel", ".boundary-grid"]:
        if re.search(rf"{re.escape(selector)}[^{{]*\{{[^}}]*display\s*:\s*none", print_css, re.IGNORECASE | re.DOTALL):
            failures.append(f"Print contract hides substantive content: {selector}")
    if re.search(r"\.section-band[^\{]*\{[^\}]*break-before\s*:\s*page", print_css, re.IGNORECASE | re.DOTALL):
        failures.append("Print contract forces every section onto a new page")
    return failures


def validate_adversarial_html_for_internal_disclosure(sample: str) -> list[str]:
    parser = parse_public_html(sample)
    return raw_disclosure_failures("adversarial HTML", sample) + parsed_surface_disclosure_failures("adversarial HTML", parser)


def runtime_failures(relative: str, text: str) -> list[str]:
    failures: list[str] = []
    lower = text.lower()
    for pattern in RUNTIME_STORAGE_PATTERNS:
        if pattern.lower() in lower:
            failures.append(f"Runtime/storage mechanism '{pattern}' found in {relative}")
    for url in re.findall(r"https?://[^\s\"'<>]+", text, re.IGNORECASE):
        if url == "http://www.w3.org/2000/svg":
            continue
        if url in APPROVED_STATIC_HTTPS_LINKS:
            continue
        failures.append(f"Unapproved external URL in {relative}: {url}")
    for marker in ["fonts.googleapis", "fonts.gstatic", "unpkg", "jsdelivr"]:
        if marker in lower:
            failures.append(f"Unapproved runtime host '{marker}' found in {relative}")
    if re.search(r"(?:^|[^a-z])cdn(?:[^a-z]|$)", lower):
        failures.append(f"Unapproved CDN marker found in {relative}")
    return failures


def html_integrity_failures(relative: str, text: str) -> list[str]:
    failures: list[str] = []
    parser = parse_public_html(text)
    if parser.scripts:
        failures.append(f"Script element found in {relative}")
    for attribute in parser.event_attributes:
        failures.append(f"Event-handler attribute '{attribute}' found in {relative}")
    if parser.javascript_urls:
        failures.append(f"javascript: URL found in {relative}")

    h1_count = sum(1 for heading in parser.headings if heading["level"] == 1)
    if h1_count != 1:
        failures.append(f"Exactly one H1 required in {relative}; found {h1_count}")
    for heading in parser.headings:
        if not normalize_label(str(heading["text"])):
            failures.append(f"Empty H{heading['level']} found in {relative}")
    for previous, current in zip(parser.headings, parser.headings[1:]):
        if int(current["level"]) > int(previous["level"]) + 1:
            failures.append(f"Heading hierarchy skips a level in {relative}")

    for image_attrs in parser.images:
        src = image_attrs.get("src", "")
        if "alt" not in image_attrs:
            failures.append(f"Image missing alt attribute in {relative}: {src}")
        elif not image_attrs["alt"].strip() and not src.endswith("assets/mark.svg"):
            failures.append(f"Non-decorative image has empty alt in {relative}: {src}")

    for href in parser.links:
        if not href.strip():
            failures.append(f"Empty href found in {relative}")
        if "localhost" in href.lower() or "127.0.0.1" in href:
            failures.append(f"Local preview link found in {relative}: {href}")
        if href.startswith("file:") or "/Users/" in href:
            failures.append(f"Local filesystem link found in {relative}: {href}")

    expected_title, expected_description = PAGE_METADATA_CONTRACTS[relative]
    if parser.title != expected_title:
        failures.append(f"Exact title mismatch in {relative}")
    for key, expected in {
        "description": expected_description,
        "og:title": expected_title,
        "og:description": expected_description,
    }.items():
        if parser.meta.get(key) != expected:
            failures.append(f"Exact metadata mismatch in {relative}: {key}")

    for surface, value in parser.claim_surfaces:
        if surface != "text-node":
            for phrase in ACCESSIBILITY_PROHIBITED_CLAIMS:
                if phrase.lower() in value.lower():
                    failures.append(f"Prohibited claim '{phrase}' in {surface} of {relative}")
    failures.extend(raw_disclosure_failures(relative, text))
    failures.extend(parsed_surface_disclosure_failures(relative, parser))
    failures.extend(runtime_failures(relative, text))
    return failures


def phase31_contract_failures(relative: str, text: str) -> list[str]:
    failures: list[str] = []
    public_text = visible_text(text)
    if relative == "ai-control/index.html":
        allowed = AI_CONTROL_ALLOWED_BOUNDARY_PHRASES
        if public_text.count(EN_PROTECTED_TARGET_BOUNDARY) < 2:
            failures.append("English protected-target boundary must appear beside both principles")
        if EN_TG360_TARGET_CHANGE not in public_text:
            failures.append("English TG360 bounded-target-change signal missing")
    elif relative == "pt/ai-control/index.html":
        allowed = PT_AI_CONTROL_ALLOWED_BOUNDARY_PHRASES
        if public_text.count(PT_PROTECTED_TARGET_BOUNDARY) < 2:
            failures.append("Portuguese protected-target boundary must appear beside both principles")
        if PT_TG360_TARGET_CHANGE not in public_text:
            failures.append("Portuguese TG360 bounded-target-change signal missing")
        if "walkthrough" in public_text.lower():
            failures.append("Visible Portuguese walkthrough terminology must use sessão privada")
    else:
        return failures

    scan_text = public_text
    for phrase in allowed:
        scan_text = re.sub(re.escape(phrase), "", scan_text, flags=re.IGNORECASE)
    for phrase in AI_CONTROL_PROHIBITED_VISIBLE:
        if phrase.lower() in scan_text.lower():
            failures.append(f"Prohibited visible AI Control phrase in {relative}: {phrase}")
    return failures


def check_ai_control_contract(errors: list[str]) -> None:
    for relative in ["ai-control/index.html", "pt/ai-control/index.html"]:
        for failure in phase31_contract_failures(relative, read_text(ROOT / relative)):
            add_error(errors, failure)

    root = visible_text(read_text(ROOT / "index.html"))
    pt_root = visible_text(read_text(ROOT / "pt/index.html"))
    if "Action clearance and proof for consequential agentic AI." not in root:
        add_error(errors, "English root AI Control card is not aligned to Phase 3.1")
    if "Autorização da ação e prova para IA agêntica empresarial." not in pt_root:
        add_error(errors, "Portuguese root AI Control card is not aligned to Phase 3.1")

    hero_svg = read_text(ROOT / "assets/trustgate-sovereign-execution-firewall.svg")
    working_svg = read_text(ROOT / "assets/trustgate-sovereign-working-example.svg")
    for relative, text in {
        "assets/trustgate-sovereign-execution-firewall.svg": hero_svg,
        "assets/trustgate-sovereign-working-example.svg": working_svg,
    }.items():
        for failure in raw_disclosure_failures(relative, text) + parsed_svg_disclosure_failures(relative, text) + runtime_failures(relative, text):
            add_error(errors, failure)
        for phrase in ACCESSIBILITY_PROHIBITED_CLAIMS:
            if phrase.lower() in text.lower():
                add_error(errors, f"Prohibited claim '{phrase}' in public SVG source: {relative}")
    for required in ["action clearance", "Bound", "receipt", "Protected-target", "Outcome"]:
        if required.lower() not in hero_svg.lower():
            add_error(errors, f"Protected-clearance SVG missing label: {required}")
    for required in ["watsonx", "Manta", "TrustGate", "protected-target", "Db2-side"]:
        if required.lower() not in working_svg.lower():
            add_error(errors, f"Illustrative-stack SVG missing role: {required}")


def check_all_route_integrity(errors: list[str]) -> None:
    for relative in HTML_PAGES:
        for failure in html_integrity_failures(relative, read_text(ROOT / relative)):
            add_error(errors, failure)


def check_runtime_network_storage(errors: list[str]) -> None:
    paths = [ROOT / relative for relative in HTML_PAGES] + [ROOT / "styles.css"] + sorted((ROOT / "assets").glob("*.svg"))
    for path in paths:
        relative = rel(path)
        if relative in HTML_PAGES:
            continue
        for failure in raw_disclosure_failures(relative, read_text(path)) + runtime_failures(relative, read_text(path)):
            add_error(errors, failure)


def check_visual_semantics(errors: list[str]) -> None:
    assets = {
        "en-hero": "assets/trustgate-action-clearance-chain-en-v2.svg",
        "pt-hero": "assets/trustgate-action-clearance-chain-pt-v2.svg",
        "en-enterprise": "assets/trustgate-enterprise-verification-chain-en-v2.svg",
        "pt-enterprise": "assets/trustgate-enterprise-verification-chain-pt-v2.svg",
        "pt-tg360": "assets/tg360-evidence-cockpit-pt-v2.svg",
    }
    for kind, relative in assets.items():
        for failure in svg_visual_contract_failures(kind, read_text(ROOT / relative)):
            add_error(errors, failure)
    for relative in AI_VISUAL_ASSET_ROUTES:
        for failure in route_visual_contract_failures(relative, read_text(ROOT / relative)):
            add_error(errors, failure)
    for en_relative, pt_relative in SVG_VISUAL_PAIRS:
        for failure in svg_pair_contract_failures(read_text(ROOT / en_relative), read_text(ROOT / pt_relative)):
            add_error(errors, f"{failure}: {en_relative} / {pt_relative}")
    for failure in print_contract_failures(read_text(ROOT / "styles.css")):
        add_error(errors, failure)
    for failure in cta_style_contract_failures(read_text(ROOT / "styles.css")):
        add_error(errors, failure)
    for failure in dark_panel_contrast_contract_failures(read_text(ROOT / "styles.css")):
        add_error(errors, failure)
    handoff = ROOT / "docs/PUBLIC_SURFACE_PHASE_3_1R3R1_HANDOFF.md"
    if handoff.exists():
        for failure in render_evidence_manifest_failures(read_text(handoff)):
            add_error(errors, failure)


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
        source = read_text(path)
        if relative in HTML_PAGES:
            source = re.sub(r"<(script|style)\b.*?</\1>", "", source, flags=re.IGNORECASE | re.DOTALL)
            source = html.unescape(re.sub(r"<[^>]+>", "\n", source, flags=re.DOTALL))
        lines = source.splitlines()
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
        for failure in raw_disclosure_failures(rel(path), text) + parsed_svg_disclosure_failures(rel(path), text):
            add_error(errors, failure)
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


def check_validator_regressions(errors: list[str]) -> None:
    def require_condition(condition: bool, case: str) -> None:
        if not condition:
            add_error(errors, f"Validator self-check failed: {case}")

    require_condition(bool(raw_disclosure_failures("fixture.html", '<img alt="TGCB">')), "reject internal term in img alt")
    require_condition(bool(raw_disclosure_failures("fixture.html", '<div aria-label="TGOS"></div>')), "reject internal term in aria-label")

    encoded_html_cases = {
        "entity-encoded internal term in alt": '<img src="assets/example.svg" alt="TG&#67;B">',
        "entity-encoded internal term in aria-label": '<div aria-label="TG&#79;S"></div>',
        "entity-encoded internal term in title": '<span title="TG&#80;E">Safe text</span>',
        "entity-encoded internal term in metadata": '<meta name="description" content="Internal TG&#65;PI contract">',
        "entity-encoded internal term in Open Graph metadata": '<meta property="og:description" content="TG&#67;B evidence">',
        "entity-encoded internal term in data attribute": '<div data-owner="TG&#67;B"></div>',
        "entity-encoded internal term in hidden text": '<div hidden>TG&#67;B</div>',
        "entity-encoded internal term in comment": '<!-- TG&#67;B -->',
        "double-encoded internal term": 'TG&amp;#67;B',
        "entity-encoded local filesystem path": '&#47;Users&#47;pbarbas&#47;private',
        "mixed-case encoded internal term": 'tg&#67;b',
        "hexadecimal entity-encoded internal term": '<span title="TG&#x43;B">Safe text</span>',
    }
    for case, sample in encoded_html_cases.items():
        require_condition(bool(validate_adversarial_html_for_internal_disclosure(sample)), f"reject {case}")

    encoded_svg_cases = {
        "entity-encoded internal term in SVG title": '<svg xmlns="http://www.w3.org/2000/svg"><title>TG&#67;B</title><desc>Safe</desc></svg>',
        "entity-encoded internal term in SVG description": '<svg xmlns="http://www.w3.org/2000/svg"><title>Safe</title><desc>Internal TG&#79;S detail</desc></svg>',
    }
    for case, sample in encoded_svg_cases.items():
        require_condition(bool(raw_disclosure_failures("fixture.svg", sample) + parsed_svg_disclosure_failures("fixture.svg", sample)), f"reject {case}")

    require_condition(not validate_adversarial_html_for_internal_disclosure("<p>TrustGate clearance receipt</p>"), "accept safe public receipt text")
    require_condition(not validate_adversarial_html_for_internal_disclosure("<p>No production enforcement is claimed.</p>"), "accept safe negative claim")

    en_hero_svg = read_text(ROOT / "assets/trustgate-action-clearance-chain-en-v2.svg")
    pt_hero_svg = read_text(ROOT / "assets/trustgate-action-clearance-chain-pt-v2.svg")
    en_enterprise_svg = read_text(ROOT / "assets/trustgate-enterprise-verification-chain-en-v2.svg")
    pt_enterprise_svg = read_text(ROOT / "assets/trustgate-enterprise-verification-chain-pt-v2.svg")
    en_tg360_svg = read_text(ROOT / "assets/tg360-evidence-cockpit-en-v2.svg")
    pt_tg360_svg = read_text(ROOT / "assets/tg360-evidence-cockpit-pt-v2.svg")
    pt_ai_html = read_text(ROOT / "pt/ai-control/index.html")
    en_ai_html = read_text(ROOT / "ai-control/index.html")

    require_condition(bool(svg_visual_contract_failures("en-hero", en_hero_svg.replace("</svg>", "<text>execution firewall</text></svg>"))), "reject retired claim in SVG visible text")
    require_condition(bool(svg_visual_contract_failures("en-hero", en_hero_svg.replace("action-clearance and proof chain", "execution firewall"))), "reject retired claim in SVG title")
    require_condition(bool(route_visual_contract_failures("pt/ai-control/index.html", pt_ai_html.replace("trustgate-action-clearance-chain-pt-v2.svg", "trustgate-action-clearance-chain-en-v2.svg"))), "reject English hero asset on PT route")
    require_condition(bool(svg_visual_contract_failures("pt-tg360", pt_tg360_svg.replace("</svg>", "<text>walkthrough</text></svg>"))), "reject walkthrough in PT TG360 SVG")
    require_condition(bool(svg_visual_contract_failures("pt-hero", re.sub(r"<title\b[^>]*>.*?</title>", "", pt_hero_svg, flags=re.DOTALL))), "reject missing PT SVG title")
    require_condition(bool(svg_visual_contract_failures("pt-hero", re.sub(r"<desc\b[^>]*>.*?</desc>", "", pt_hero_svg, flags=re.DOTALL))), "reject missing PT SVG description")
    require_condition(bool(svg_visual_contract_failures("en-enterprise", en_enterprise_svg.replace("protected-target-verification", "missing-verification"))), "reject missing protected-target verification group")
    require_condition(bool(svg_visual_contract_failures("en-enterprise", en_enterprise_svg.replace("</svg>", '<path data-role="clearance-to-target-bypass" d="M0 0h1"/></svg>'))), "reject direct clearance-to-target bypass connector")
    missing_receipt_svg = en_hero_svg.replace("bound receipt", "artifact").replace(">Bound<", ">Missing<").replace(">receipt<", ">artifact<")
    require_condition(bool(svg_visual_contract_failures("en-hero", missing_receipt_svg)), "reject missing bound-receipt concept")
    require_condition(bool(svg_visual_contract_failures("en-hero", en_hero_svg.replace("</svg>", '<image href="https://example.com/a.png"/></svg>'))), "reject external SVG image reference")
    require_condition(bool(svg_visual_contract_failures("en-hero", en_hero_svg.replace("</svg>", "<script>bad()</script></svg>"))), "reject SVG script element")
    require_condition(bool(svg_visual_contract_failures("en-hero", en_hero_svg.replace("<rect id=", '<rect onclick="bad()" id=', 1))), "reject SVG event-handler attribute")
    require_condition(bool(route_visual_contract_failures("pt/ai-control/index.html", pt_ai_html.replace("tg360-evidence-cockpit-pt-v2.svg", "missing-pt.svg"))), "reject broken localized asset route")
    require_condition(bool(route_visual_contract_failures("ai-control/index.html", en_ai_html.replace('class="button primary"', 'class="button primary" aria-disabled="true"', 1))), "reject disabled primary CTA")
    require_condition(bool(route_visual_contract_failures("ai-control/index.html", re.sub(r'(<a class="button primary" )href="[^"]+"', r'\1href=""', en_ai_html, count=1))), "reject empty primary CTA destination")
    require_condition(bool(svg_pair_contract_failures(en_hero_svg, pt_hero_svg.replace('viewBox="0 0 900 440"', 'viewBox="0 0 901 440"'))), "reject EN/PT different viewBox")
    require_condition(bool(svg_pair_contract_failures(en_hero_svg, pt_hero_svg.replace('x="24" y="190" width="110"', 'x="25" y="190" width="110"', 1))), "reject EN/PT different node coordinates")
    require_condition(bool(svg_pair_contract_failures(en_enterprise_svg, pt_enterprise_svg.replace('data-node-id="orchestration-input"', 'data-node-id="missing-input"', 1))), "reject missing PT node")
    require_condition(bool(svg_pair_contract_failures(en_tg360_svg.replace('</svg>', '<path id="extra-connector" data-role="extra-connector" d="M0 0h1"/></svg>'), pt_tg360_svg)), "reject extra EN connector")
    require_condition(bool(svg_visual_contract_failures("en-enterprise", en_enterprise_svg.replace('</svg>', '<path id="clearance-to-target" data-role="clearance-to-target-bypass" d="M0 0h1"/></svg>'))), "reject direct clearance-to-outcome connector")
    require_condition(bool(svg_pair_contract_failures(en_hero_svg.replace('data-label-for="proposed-action"', '', 1), pt_hero_svg)), "reject missing text-owner marker")
    require_condition(bool(route_visual_contract_failures("ai-control/index.html", en_ai_html.replace("trustgate-action-clearance-chain-en-v2.svg", "trustgate-sovereign-execution-firewall.svg"))), "reject legacy English asset reference")
    require_condition(bool(svg_visual_contract_failures("pt-hero", pt_hero_svg.replace(">Ação<", ">Agentic request<", 1))), "reject English operational label in PT SVG")
    require_condition(bool(svg_pair_contract_failures(en_hero_svg, pt_hero_svg.replace('data-label-for="proposed-action"', 'data-label-for="bound-receipt"', 1))), "reject text assigned to wrong node")
    require_condition(bool(route_visual_contract_failures("ai-control/index.html", en_ai_html.replace('class="button primary"', 'class="button primary" style="opacity: 0.5"', 1))), "reject primary CTA opacity below 1")
    evidence_fixture = "## EN PDF Evidence\n" + "\n".join(["- Path: `/tmp/en.pdf`", "- SHA-256: `" + "a" * 64 + "`", "- Generated: `2026-07-11T00:00:00+01:00`", "- Engine: `Chromium`", "- Page size: `A4`", "- Orientation: `portrait`", "- Margins: `12 mm`", "- Background graphics: `enabled`", "- Headers/footers: `disabled`", "- Page count: `14`"]) + "\n## PT PDF Evidence\n" + "\n".join(["- Path: `/tmp/pt.pdf`", "- SHA-256: `" + "b" * 64 + "`", "- Generated: `2026-07-11T00:00:00+01:00`", "- Engine: `Chromium`", "- Page size: `A4`", "- Orientation: `portrait`", "- Margins: `12 mm`", "- Background graphics: `enabled`", "- Headers/footers: `disabled`", "- Page count: `14`"])
    require_condition(bool(render_evidence_manifest_failures(evidence_fixture.replace("- SHA-256: `" + "a" * 64 + "`\n", "", 1))), "reject missing PDF evidence hash in handoff")
    require_condition(bool(render_evidence_manifest_failures(evidence_fixture.replace("- Path: `/tmp/en.pdf`\n", "", 1))), "reject reported page count without complete evidence record")
    contrast_css = read_text(ROOT / "styles.css")
    require_condition(bool(dark_panel_contrast_contract_failures(contrast_css.replace("color: #edf4f7;", "color: #13202b;", 1))), "reject dark foreground on dark action panel")
    require_condition(bool(dark_panel_contrast_contract_failures(contrast_css.replace("color: #edf4f7;\n  opacity: 1;", "color: #edf4f7;\n  opacity: 0.6;", 1))), "reject dark-panel opacity below 1")
    require_condition(bool(dark_panel_contrast_contract_failures(contrast_css.replace(".hero-visual > .boundary-note", ".hero-visual > .missing-pt-note", 1))), "reject missing equivalent PT contrast treatment")
    require_condition(bool(dark_panel_contrast_contract_failures(contrast_css + "\n.hero-visual > figcaption { color: #445766; }\n")), "reject enterprise caption reverting to dark foreground")
    require_condition(not svg_visual_contract_failures("en-enterprise", en_enterprise_svg), "accept EN vendor and product names")
    require_condition(not svg_visual_contract_failures("pt-enterprise", pt_enterprise_svg), "accept localized PT enterprise labels")
    require_condition(not svg_visual_contract_failures("pt-hero", pt_hero_svg), "accept localized PT hero labels")

    root_title, root_description = PAGE_METADATA_CONTRACTS["index.html"]
    root_fixture = (
        f'<html><head><title>{root_title}</title><meta name="description" content="{root_description}">'
        f'<meta property="og:title" content="{root_title}"><meta property="og:description" content="{root_description}">'
        '</head><body><h1>Root</h1><img src="assets/example.svg" alt="Example"></body></html>'
    )
    old_og = root_fixture.replace(root_title, "The execution firewall for agentic AI", 1).replace(
        f'content="{root_title}"', 'content="The execution firewall for agentic AI"'
    )
    require_condition(
        any("og:title" in failure or "execution firewall" in failure for failure in html_integrity_failures("index.html", old_og)),
        "old execution-firewall wording in og:title",
    )
    require_condition(any("Script element" in failure for failure in html_integrity_failures("index.html", root_fixture + "<script></script>")), "reject inline script")
    require_condition(any("Event-handler" in failure for failure in html_integrity_failures("index.html", root_fixture.replace("<h1", '<main onclick="x()"><h1'))), "reject event-handler attribute")
    require_condition(bool(runtime_failures("fixture.html", "fetch('/x')")), "reject fetch call")
    require_condition(bool(runtime_failures("fixture.html", "new WebSocket('/x')")), "reject WebSocket call")
    require_condition(bool(runtime_failures("fixture.html", "localStorage.setItem('x', 'y')")), "reject localStorage use")
    require_condition(
        any("missing alt" in failure.lower() for failure in html_integrity_failures("index.html", root_fixture.replace(' alt="Example"', ""))),
        "missing image alt",
    )
    require_condition(
        any("Exactly one H1" in failure for failure in html_integrity_failures("index.html", root_fixture.replace("</body>", "<h1>Second</h1></body>"))),
        "duplicate H1 on non-AI route",
    )

    pt_source = read_text(ROOT / "pt/ai-control/index.html")
    en_source = read_text(ROOT / "ai-control/index.html")
    require_condition(
        any("walkthrough" in failure.lower() for failure in phase31_contract_failures("pt/ai-control/index.html", pt_source + "<p>walkthrough</p>")),
        "visible Portuguese walkthrough",
    )
    require_condition(
        any("target-change" in failure for failure in phase31_contract_failures("ai-control/index.html", en_source.replace(EN_TG360_TARGET_CHANGE, ""))),
        "missing TG360 target-changed signal",
    )
    require_condition(
        any("boundary" in failure for failure in phase31_contract_failures("ai-control/index.html", en_source.replace(EN_PROTECTED_TARGET_BOUNDARY, "", 1))),
        "incomplete protected-target boundary",
    )
    require_condition(
        any("dora compliant" in failure.lower() for failure in phase31_contract_failures("ai-control/index.html", en_source + "<p>DORA compliant</p>")),
        "positive DORA-compliance claim",
    )


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_not_found_page(errors)
    check_cloudflare_package(errors)
    check_page_content(errors)
    check_ai_control_contract(errors)
    check_all_route_integrity(errors)
    check_route_links(errors)
    check_disallowed_files(errors)
    check_external_js_css_fonts(errors)
    check_analytics_keywords(errors)
    check_forms_and_cookies(errors)
    check_blocked_claims(errors)
    check_svg_files(errors)
    check_html_links_and_assets(errors)
    check_runtime_network_storage(errors)
    check_visual_semantics(errors)
    check_validator_regressions(errors)

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
