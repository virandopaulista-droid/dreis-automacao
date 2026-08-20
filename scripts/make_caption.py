#!/usr/bin/env python3
"""Legenda generica gerada automaticamente pelo assistente de onboarding do
painel BEEF MTK pro cliente "Dreis". Sem geracao por IA -- so
templates simples com os dados que Rob informou no formulario de
cadastro. Edite este arquivo a vontade se o tom/informacoes mudarem.

Usage: make_caption.py <feed|reel> [--weekday <dia>]
Prints: caminho pro arquivo temporario com a legenda.
"""
import random
import sys
import tempfile

LABEL = "Dreis"
ADDRESS = "Estr. do Jararau, 140 Chácara Nani, São Paulo - SP"
HOURS = "🕠todos os dias Horário: 18:00 á 23:50"
HASHTAGS = ""

WEEKDAY_DISHES = {

}

GENERIC_TEMPLATES = [
    "\u2728 {label} te espera hoje! Vem conferir tudo que a gente preparou com cuidado especialmente pra voce.\n\n{footer}",
    "\U0001F37D\uFE0F Bora fazer aquele pedido/visita na {label}? Sempre com capricho, sempre pensando em te dar a melhor experiencia.\n\n{footer}",
]

SPECIAL_TEMPLATES = [
    "\U0001F37D\uFE0F Hoje o destaque e {prato}, preparado com todo o cuidado pela {label}. Vem provar!\n\n{footer}",
]


def build_footer():
    lines = [l for l in [ADDRESS, HOURS, HASHTAGS] if l]
    return "\n".join(lines)


def build_caption(kind, weekday=None):
    prato = WEEKDAY_DISHES.get(weekday) if weekday else None
    footer = build_footer()
    if prato:
        template = random.choice(SPECIAL_TEMPLATES)
        return template.format(prato=prato, label=LABEL, footer=footer)
    template = random.choice(GENERIC_TEMPLATES)
    return template.format(label=LABEL, footer=footer)


def main():
    args = sys.argv[1:]
    if not args or args[0] not in ("feed", "reel"):
        print("Uso: make_caption.py <feed|reel> [--weekday <dia>]", file=sys.stderr)
        raise SystemExit(1)
    kind = args[0]
    weekday = None
    if "--weekday" in args:
        idx = args.index("--weekday")
        if idx + 1 < len(args):
            weekday = args[idx + 1]
    caption = build_caption(kind, weekday)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write(caption)
        path = f.name
    print(path)


if __name__ == "__main__":
    main()
