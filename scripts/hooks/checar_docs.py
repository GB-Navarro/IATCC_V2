"""Hook (Stop e SessionStart): avisa quando Brain/, scripts/, CLAUDE.md ou os hooks mudaram
depois da última atualização de docs/.

Cobra uma vez por leva de mudanças: a hora da última cobrança fica em
docs/.ultima_verificacao.
"""

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
MARCADOR = DOCS / ".ultima_verificacao"
OBSERVADOS = [ROOT / "Brain", ROOT / "scripts", ROOT / "CLAUDE.md", ROOT / ".claude" / "settings.json"]
MAX_LISTADOS = 15


def arquivos(caminho: Path):
    if caminho.is_file():
        yield caminho
        return
    for f in caminho.rglob("*"):
        partes = f.relative_to(ROOT).parts
        if f.is_file() and not any(p.startswith(".") or p == "__pycache__" for p in partes):
            yield f


def referencia() -> float:
    tempos = [f.stat().st_mtime for f in DOCS.glob("*.md")]
    if MARCADOR.exists():
        tempos.append(float(MARCADOR.read_text(encoding="utf-8").strip() or 0))
    return max(tempos, default=0.0)


def alterados() -> list[str]:
    ref = referencia()
    return sorted(
        f.relative_to(ROOT).as_posix()
        for c in OBSERVADOS if c.exists()
        for f in arquivos(c)
        if f.stat().st_mtime > ref
    )


def mensagem(lista: list[str]) -> str:
    itens = "\n".join(f"- {a}" for a in lista[:MAX_LISTADOS])
    resto = f"\n- … e mais {len(lista) - MAX_LISTADOS}" if len(lista) > MAX_LISTADOS else ""
    return (
        "Arquivos alterados desde a última atualização de docs/:\n"
        f"{itens}{resto}\n\n"
        "Se a mudança for relevante (critérios no CLAUDE.md), atualize docs/evolucao.md "
        "e, se couber, docs/decisoes.md e docs/README.md. Se não for, diga em uma linha por quê. "
        "Se a mudança veio do usuário e implica decisão, pergunte o motivo."
    )


def main() -> int:
    try:
        entrada = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        entrada = {}
    evento = entrada.get("hook_event_name", "Stop")

    if evento == "Stop" and entrada.get("stop_hook_active"):
        return 0

    lista = alterados()
    if not lista:
        return 0

    MARCADOR.write_text(str(time.time()), encoding="utf-8")
    if evento == "SessionStart":
        saida = {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": mensagem(lista)}}
    else:
        saida = {"decision": "block", "reason": mensagem(lista)}
    print(json.dumps(saida))
    return 0


if __name__ == "__main__":
    sys.exit(main())
