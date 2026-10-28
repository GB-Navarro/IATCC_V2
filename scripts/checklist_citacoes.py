"""Gera o checklist de validação de um lote: um item por citação, com a página do PDF.

Uso: python scripts/checklist_citacoes.py <lote> <COD> [<COD> ...]
Saída: validacao/humana/lote-<lote>.md (não sobrescreve um checklist existente).
"""

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
NOTAS = RAIZ / "Brain" / "structures"
FONTES = RAIZ / "fontes" / "README.md"
SAIDA = RAIZ / "validacao" / "humana"

CITACAO = re.compile(r"\[(ovml|inferência:[^\]]+|[a-z0-9-]+, pp?\. [^\]]+)\]")
REF = re.compile(r"([a-z0-9-]+-\d{4}), pp?\. ([\d–, ]+)")


def deslocamentos() -> dict[str, list[tuple[int, int]]]:
    """Por fonte, lista de (página impressa inicial, deslocamento). Aceita "10" ou "10 · 9 a partir de p. 263"."""
    desl = {}
    for linha in FONTES.read_text(encoding="utf-8").splitlines():
        cols = [c.strip() for c in linha.split("|")]
        if len(cols) > 5 and cols[1].startswith("`") and re.match(r"\d+", cols[4]):
            faixas = [(0, int(re.match(r"\d+", cols[4]).group()))]
            faixas += [(int(p), int(d)) for d, p in re.findall(r"(\d+) a partir de p\. (\d+)", cols[4])]
            desl[cols[1].strip("`")] = sorted(faixas)
    return desl


def deslocamento(faixas: list[tuple[int, int]], pagina: int) -> int:
    return [d for inicio, d in faixas if pagina >= inicio][-1]


def paginas_pdf(texto: str, desl: dict[str, list[tuple[int, int]]]) -> str:
    saida = []
    for chave, pags in REF.findall(texto):
        if chave not in desl:
            saida.append(f"{chave}: sem deslocamento")
            continue
        f = desl[chave]
        convertidas = re.sub(r"\d+", lambda m: str(int(m.group()) + deslocamento(f, int(m.group()))), pags.strip().rstrip(","))
        saida.append(f"{chave}: PDF {convertidas}")
    return "; ".join(saida)


def itens(cod: str, desl: dict[str, int]) -> list[str]:
    texto = (NOTAS / f"{cod}.md").read_text(encoding="utf-8")
    corpo = texto.split("\n---\n", 1)[1]
    secao, resultado = "", []
    for linha in corpo.splitlines():
        if linha.startswith("## "):
            secao = linha[3:]
            continue
        cits = CITACAO.findall(linha)
        if not cits:
            continue
        if linha.startswith("|"):
            info, valor, fonte = [c.strip() for c in linha.strip("|").split("|")]
            rotulo, resumo, cits = "Origem", f"**{info}:** {valor}", CITACAO.findall(fonte)
        else:
            rotulo, resumo = secao, CITACAO.sub("", linha).strip("- ;.").strip()
        resumo = re.sub(r"\s+([.,;:])", r"\1", re.sub(r"\s+", " ", resumo))
        resumo = resumo if len(resumo) <= 240 else resumo[:240] + "…"
        resultado.append(f"- {rotulo} · {resumo}")
        for c in cits:
            alerta = " ⚠ inferência" if c.startswith("inferência") else ""
            pdf = paginas_pdf(c, desl)
            local = f" — {pdf}" if pdf else " — texto Bloomberg na nota" if c == "ovml" else ""
            resultado.append(f"  - [ ] `[{c}]`{local}{alerta}")
    return resultado


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    lote, codigos = sys.argv[1], sys.argv[2:]
    destino = SAIDA / f"lote-{lote}.md"
    if destino.exists():
        print(f"já existe: {destino}")
        return 1
    desl = deslocamentos()
    linhas = [f"# Validação — lote {lote}", "",
              "Marque cada item depois de conferir a afirmação na página indicada. Itens com ⚠ são inferências: confira as premissas.", ""]
    total = 0
    for cod in codigos:
        its = itens(cod, desl)
        total += sum("[ ]" in i for i in its)
        linhas += [f"## {cod}", "", *its, ""]
    SAIDA.mkdir(exist_ok=True)
    destino.write_text("\n".join(linhas), encoding="utf-8", newline="\n")
    print(f"{destino.relative_to(RAIZ)}: {total} itens")
    return 0


if __name__ == "__main__":
    sys.exit(main())
