#!/usr/bin/env python3
"""
Coletor técnico do Raio-X de Conversão.
Busca páginas de uma loja virtual e extrai sinais objetivos: plataforma,
stack de terceiros, JSON-LD, peso, imagens, analytics. 100% biblioteca padrão.

Uso:
  python3 coletar.py https://loja.com.br [https://loja.com.br/produto-x ...] --out coleta.json
  python3 coletar.py https://loja.com.br --psi --out coleta.json   # inclui PageSpeed mobile (lento)
"""
import argparse
import json
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36 RaioXConversao/1.0")

PLATAFORMAS = [
    ("Shopify", ["cdn.shopify.com", "myshopify.com", "Shopify.theme", "shopify-features"]),
    ("Nuvemshop", ["tiendanube", "nuvemshop", "cdn.tiendanube.com", "lojavirtualnuvem"]),
    ("VTEX", ["vteximg.com.br", "vtexassets.com", "vtex.com.br", "__RUNTIME__", "vtexcommercestable"]),
    ("Tray", ["tcdn.com.br", "tray.com.br", "traycheckout"]),
    ("Loja Integrada", ["lojaintegrada", "awsli.com.br"]),
    ("Yampi", ["yampi.com.br", "cdn.yampi"]),
    ("Bagy", ["bagy.com.br", "cdn.bagy"]),
    ("Wake/Fbits", ["fbits.net", "wake.commerce", "wakecommerce"]),
    ("Linx", ["linximpulse", "linx.com.br", "linx-impulse"]),
    ("Shoppub", ["shoppub"]),
    ("WooCommerce", ["woocommerce", "wp-content/plugins/woocommerce"]),
    ("Magento", ["Magento", "/static/version", "mage/cookies"]),
    ("Wix", ["wixstatic.com", "wix.com"]),
    ("Squarespace", ["squarespace.com"]),
]

TERCEIROS = {
    "analytics": [
        ("GA4/gtag", ["googletagmanager.com/gtag", "gtag('config'", 'gtag("config"']),
        ("Google Tag Manager", ["googletagmanager.com/gtm.js", "GTM-"]),
        ("Meta Pixel", ["connect.facebook.net", "fbq("]),
        ("TikTok Pixel", ["analytics.tiktok.com"]),
        ("Microsoft Clarity", ["clarity.ms"]),
        ("Hotjar", ["hotjar.com"]),
        ("Pinterest Tag", ["pintrk"]),
    ],
    "busca_recomendacao": [
        ("Algolia", ["algolia"]),
        ("Doofinder", ["doofinder"]),
        ("Linx Impulse", ["linximpulse"]),
        ("SmartHint", ["smarthint"]),
        ("Searchanise", ["searchanise"]),
        ("Klevu", ["klevu"]),
    ],
    "suite_performa": [
        ("PowerSearch", ["powersearch"]),
        ("PowerDisplay", ["powerdisplay"]),
        ("PowerCart", ["powercart"]),
        ("PowerClip", ["powerclip"]),
        ("PowerSlider", ["powerslider"]),
        ("PowerChat", ["powerchat"]),
        ("PowerPush", ["performa-powerpush", "powerpush"]),
        ("PowerInfinity", ["powerinfinity"]),
        ("PowerLook", ["powerlook"]),
        ("PowerHits/Conectiva", ["cdn.performa.ai", "performa.ai"]),
    ],
    "reviews_prova_social": [
        ("Trustvox", ["trustvox"]),
        ("Yotpo", ["yotpo"]),
        ("Loox", ["loox.io"]),
        ("Judge.me", ["judge.me"]),
        ("Opiniões Verificadas", ["opinioes-verificadas", "netreviews", "avis-verifies"]),
        ("Konfidency", ["konfidency"]),
        ("Reclame Aqui (selo)", ["reclameaqui"]),
    ],
    "chat_atendimento": [
        ("WhatsApp (link)", ["wa.me/", "api.whatsapp.com"]),
        ("JivoChat", ["jivosite", "jivochat"]),
        ("Zendesk", ["zendesk"]),
        ("Tawk.to", ["tawk.to"]),
        ("Octadesk", ["octadesk"]),
        ("Intercom", ["intercom"]),
    ],
    "push_recuperacao": [
        ("OneSignal", ["onesignal"]),
        ("PushNews", ["pushnews"]),
        ("Insider", ["useinsider"]),
        ("CartStack", ["cartstack"]),
        ("Enviou", ["enviou.com.br"]),
        ("Edrone", ["edrone"]),
        ("Mailbiz", ["mailbiz"]),
        ("Klaviyo", ["klaviyo"]),
        ("ActiveCampaign", ["activehosted", "activecampaign"]),
        ("RD Station", ["rdstation", "d335luupugsy2"]),
        ("Dito", ["dito.com.br", "ditocdn"]),
        ("SocialMiner/Charles", ["socialminer"]),
        ("OptinMonster (overlay)", ["optinmonster"]),
        ("Poptin (overlay)", ["poptin"]),
        ("Wisepops (overlay)", ["wisepops"]),
        ("Privy (overlay)", ["privy.com", "privymktg"]),
    ],
    "video_commerce": [
        ("Vídeo nativo (<video>)", ["<video"]),
        ("YouTube embed", ["youtube.com/embed", "youtube-nocookie.com/embed"]),
        ("Vimeo player", ["player.vimeo.com"]),
        ("Videowise", ["videowise"]),
        ("Tolstoy", ["gotolstoy"]),
        ("Bambuser", ["bambuser"]),
        ("Firework", ["fireworktv", "fwpub", "firework.com"]),
        ("Vurdere", ["vurdere"]),
        ("WeShow/Stories shoppable", ["weshow", "shoppablevideo"]),
    ],
}


def fetch(url, timeout=25):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "pt-BR,pt;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            raw = r.read()
            charset = r.headers.get_content_charset() or "utf-8"
            return {
                "status": r.status,
                "final_url": r.geturl(),
                "bytes": len(raw),
                "html": raw.decode(charset, errors="replace"),
                "headers": dict(r.headers),
            }
    except urllib.error.HTTPError as e:
        return {"status": e.code, "final_url": url, "bytes": 0, "html": "", "erro": str(e)}
    except Exception as e:  # DNS, SSL, timeout...
        return {"status": None, "final_url": url, "bytes": 0, "html": "", "erro": f"{type(e).__name__}: {e}"}


def detectar_plataforma(html):
    for nome, pistas in PLATAFORMAS:
        for pista in pistas:
            if pista.lower() in html.lower():
                return nome
    return "não identificada"


def detectar_terceiros(html):
    low = html.lower()
    achados = {}
    for grupo, itens in TERCEIROS.items():
        achados[grupo] = [nome for nome, pistas in itens
                          if any(p.lower() in low for p in pistas)]
    return achados


def extrair_jsonld(html):
    blocos = re.findall(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        html, re.DOTALL | re.IGNORECASE)
    out = []
    for b in blocos:
        try:
            data = json.loads(b.strip())
        except json.JSONDecodeError:
            out.append({"erro": "JSON-LD inválido (não parseia)"})
            continue
        for item in (data if isinstance(data, list) else [data]):
            if not isinstance(item, dict):
                continue
            tipo = item.get("@type", "?")
            resumo = {"tipo": tipo}
            if (tipo == "Product" or (isinstance(tipo, list) and "Product" in tipo)):
                offers = item.get("offers") or {}
                if isinstance(offers, list):
                    offers = offers[0] if offers else {}
                resumo["campos"] = {
                    "name": bool(item.get("name")),
                    "image": bool(item.get("image")),
                    "description": bool(item.get("description")),
                    "brand": bool(item.get("brand")),
                    "sku": bool(item.get("sku")),
                    "gtin": any(item.get(k) for k in ("gtin", "gtin13", "gtin8", "gtin14", "mpn")),
                    "offers_price": bool(offers.get("price")),
                    "offers_availability": bool(offers.get("availability")),
                    "aggregateRating": bool(item.get("aggregateRating")),
                }
            out.append(resumo)
    return out


def analisar_html(html):
    low = html.lower()
    imgs = re.findall(r"<img\b[^>]*>", html, re.IGNORECASE)
    sem_alt = [i for i in imgs if not re.search(r'alt=["\'][^"\']+["\']', i, re.IGNORECASE)]
    title = re.search(r"<title[^>]*>(.*?)</title>", html, re.DOTALL | re.IGNORECASE)
    meta_desc = re.search(
        r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', html, re.IGNORECASE)
    return {
        "title": (title.group(1).strip()[:200] if title else None),
        "meta_description": (meta_desc.group(1).strip()[:300] if meta_desc else None),
        "tem_viewport_meta": 'name="viewport"' in low or "name='viewport'" in low,
        "num_scripts": len(re.findall(r"<script\b", low)),
        "num_scripts_externos": len(re.findall(r'<script[^>]+src=', low)),
        "num_imgs": len(imgs),
        "imgs_sem_alt": len(sem_alt),
        "imgs_lazy": len(re.findall(r'loading=["\']lazy["\']', low)),
        "tem_input_busca": bool(re.search(r'<input[^>]+(type=["\']search["\']|name=["\']q["\']|placeholder=["\'][^"\']*busc)', low)),
        "tem_favicon": "rel=\"icon\"" in low or "rel='icon'" in low or "shortcut icon" in low,
        "menciona_cnpj": bool(re.search(r"cnpj", low)),
        "menciona_pix": bool(re.search(r"\bpix\b", low)),
        "menciona_troca_devolucao": bool(re.search(r"troca|devolu", low)),
        "menciona_frete_gratis": bool(re.search(r"frete\s*gr[aá]tis", low)),
        "links_whatsapp": len(re.findall(r"wa\.me/|api\.whatsapp\.com", low)),
    }


def pagespeed(url):
    """Consulta a API pública do PageSpeed Insights (mobile). Lento: 30-60s."""
    api = ("https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="
           + urllib.parse.quote(url, safe="") + "&strategy=mobile&locale=pt_BR")
    try:
        req = urllib.request.Request(api, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.loads(r.read().decode("utf-8"))
    except Exception as e:
        return {"erro": f"{type(e).__name__}: {e}"}
    out = {}
    lh = data.get("lighthouseResult", {})
    perf = lh.get("categories", {}).get("performance", {}).get("score")
    out["lab_performance_score"] = round(perf * 100) if perf is not None else None
    audits = lh.get("audits", {})
    for chave, audit in (("lcp_s", "largest-contentful-paint"),
                         ("cls", "cumulative-layout-shift"),
                         ("tbt_ms", "total-blocking-time"),
                         ("speed_index_s", "speed-index")):
        a = audits.get(audit, {})
        out[f"lab_{chave}"] = a.get("displayValue")
    campo = data.get("loadingExperience", {}).get("metrics", {})
    if campo:
        mapa = {"LARGEST_CONTENTFUL_PAINT_MS": "campo_lcp_ms",
                "INTERACTION_TO_NEXT_PAINT": "campo_inp_ms",
                "CUMULATIVE_LAYOUT_SHIFT_SCORE": "campo_cls_x100"}
        for k, nome in mapa.items():
            if k in campo:
                out[nome] = {"p75": campo[k].get("percentile"),
                             "categoria": campo[k].get("category")}
    return out


def coletar(url, com_psi=False):
    r = fetch(url)
    resultado = {
        "url": url,
        "status": r.get("status"),
        "url_final": r.get("final_url"),
        "https_ok": (r.get("final_url") or "").startswith("https://"),
        "peso_html_kb": round(r.get("bytes", 0) / 1024, 1),
    }
    if r.get("erro"):
        resultado["erro"] = r["erro"]
        return resultado
    html = r["html"]
    resultado["plataforma"] = detectar_plataforma(html)
    resultado["terceiros"] = detectar_terceiros(html)
    resultado["jsonld"] = extrair_jsonld(html)
    resultado["analise"] = analisar_html(html)
    if com_psi:
        print(f"  consultando PageSpeed Insights (mobile) para {url} — pode levar 1 min...",
              file=sys.stderr)
        resultado["pagespeed_mobile"] = pagespeed(url)
    return resultado


def main():
    ap = argparse.ArgumentParser(description="Coletor técnico do Raio-X de Conversão")
    ap.add_argument("urls", nargs="+", help="URLs a coletar (home, categoria, PDP...)")
    ap.add_argument("--out", help="arquivo JSON de saída (padrão: stdout)")
    ap.add_argument("--psi", action="store_true",
                    help="consulta PageSpeed Insights mobile para cada URL (lento)")
    args = ap.parse_args()

    paginas = []
    for u in args.urls:
        if not u.startswith("http"):
            u = "https://" + u
        print(f"coletando {u} ...", file=sys.stderr)
        paginas.append(coletar(u, com_psi=args.psi))

    saida = json.dumps({"paginas": paginas}, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(saida)
        print(f"ok: {args.out}", file=sys.stderr)
    else:
        print(saida)


if __name__ == "__main__":
    main()
