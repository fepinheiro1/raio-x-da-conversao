#!/usr/bin/env python3
"""Verifica os requisitos locais do Raio-X de Conversão sem instalar nada."""

import argparse
import importlib
import json
import os
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request


MIN_PYTHON = (3, 8)
STDLIB_MODULES = ("argparse", "html", "json", "re", "ssl", "urllib.request")


def check_python():
    current = sys.version_info[:3]
    ok = current >= MIN_PYTHON
    return {
        "status": "ok" if ok else "missing",
        "version": ".".join(map(str, current)),
        "minimum": ".".join(map(str, MIN_PYTHON)),
        "message": "Python compatível." if ok else "Python 3.8 ou superior é obrigatório.",
    }


def check_stdlib():
    missing = []
    for module in STDLIB_MODULES:
        try:
            importlib.import_module(module)
        except ImportError:
            missing.append(module)
    return {
        "status": "ok" if not missing else "missing",
        "missing": missing,
        "message": (
            "Biblioteca padrão disponível; nenhum pacote pip é necessário."
            if not missing
            else "Módulos ausentes: " + ", ".join(missing)
        ),
    }


def check_output_dir(path):
    absolute = os.path.abspath(path)
    if not os.path.isdir(absolute):
        return {
            "status": "missing",
            "path": absolute,
            "message": "A pasta de saída não existe.",
        }
    try:
        with tempfile.NamedTemporaryFile(dir=absolute, prefix="raio-x-preflight-", delete=True):
            pass
    except OSError as exc:
        return {
            "status": "missing",
            "path": absolute,
            "message": "Sem permissão de escrita: " + str(exc),
        }
    return {
        "status": "ok",
        "path": absolute,
        "message": "Pasta de saída gravável.",
    }


def normalize_url(url):
    if not url:
        return None
    parsed = urllib.parse.urlparse(url)
    if not parsed.scheme:
        url = "https://" + url
        parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError("URL inválida; use http:// ou https://")
    return url


def check_store_access(url, timeout):
    if not url:
        return {
            "status": "pending",
            "message": "Informe --url para testar o acesso HTTPS à loja.",
        }
    try:
        normalized = normalize_url(url)
    except ValueError as exc:
        return {"status": "missing", "url": url, "message": str(exc)}

    request = urllib.request.Request(
        normalized,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; RaioXConversao/1.0)",
            "Range": "bytes=0-0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            response.read(1)
            return {
                "status": "ok",
                "url": response.geturl(),
                "http_status": response.status,
                "message": "Acesso HTTPS à loja confirmado.",
            }
    except urllib.error.HTTPError as exc:
        return {
            "status": "warning",
            "url": normalized,
            "http_status": exc.code,
            "message": (
                "A rede alcançou a loja, mas ela recusou a coleta estática. "
                "Tente o navegador controlável ou declare a limitação."
            ),
        }
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {
            "status": "missing",
            "url": normalized,
            "message": "Não foi possível acessar a loja: " + str(exc),
        }


def build_report(args):
    report = {
        "python": check_python(),
        "stdlib": check_stdlib(),
        "output": check_output_dir(args.output_dir),
        "store_access": check_store_access(args.url, args.timeout),
        "browser_control": {
            "status": "external-check",
            "message": (
                "O agente deve verificar se possui navegador controlável e viewport mobile. "
                "Sem isso, use o Modo Estático."
            ),
        },
        "pagespeed": {
            "status": "optional",
            "message": "PageSpeed Insights é opcional e exige autorização antes da chamada externa.",
        },
    }
    local_keys = ("python", "stdlib", "output")
    report["local_requirements_ok"] = all(report[key]["status"] == "ok" for key in local_keys)
    report["static_mode_ready"] = (
        report["local_requirements_ok"]
        and report["store_access"]["status"] in ("ok", "warning")
    )
    return report


def print_human(report):
    labels = (
        ("python", "Python"),
        ("stdlib", "Biblioteca padrão"),
        ("output", "Pasta de saída"),
        ("store_access", "Acesso à loja"),
        ("browser_control", "Navegador controlável"),
        ("pagespeed", "PageSpeed"),
    )
    print("Pré-check do Raio-X de Conversão")
    for key, label in labels:
        item = report[key]
        print("- {0}: {1} — {2}".format(label, item["status"].upper(), item["message"]))


def main():
    parser = argparse.ArgumentParser(
        description="Verifica os requisitos do Raio-X sem instalar ou alterar o sistema."
    )
    parser.add_argument("--url", help="URL da loja para testar acesso HTTPS")
    parser.add_argument("--output-dir", default=".", help="pasta onde os relatórios serão gerados")
    parser.add_argument("--timeout", type=float, default=8.0, help="timeout do teste de rede")
    parser.add_argument("--json", action="store_true", help="imprime resultado em JSON")
    args = parser.parse_args()

    report = build_report(args)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_human(report)
    return 0 if report["local_requirements_ok"] else 2


if __name__ == "__main__":
    sys.exit(main())
