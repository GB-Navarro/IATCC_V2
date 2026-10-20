"""Cria uma nota canônica por estrutura em Brain/structures/ a partir de _template.md.

Preenche só o que sai do nome do arquivo da Bloomberg (código, nome, embed).
Nunca sobrescreve notas existentes e nunca escreve em bloomberg_description/.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

BRAIN = Path(__file__).resolve().parent.parent / "Brain"
STRUCTURES = BRAIN / "structures"
BLOOMBERG = STRUCTURES / "bloomberg_description"
TEMPLATE = BRAIN / "_template.md"
HASHES = STRUCTURES / ".bloomberg_hashes.json"

NOME_COD = re.compile(r"^(?P<nome>.+) \((?P<cod>[^()]+)\)$")
GENERICA = re.compile(r"^\d+L$")

# Sinônimos que não aparecem no nome do arquivo.
ALIASES_EXTRA = {"FE": ["Variance Forward"]}

CAMPOS_1_PERNA = ("barreira:", "barreiras:", "payoff:")


def nota(template: str, stem: str, nome: str, cod: str) -> str:
    aliases = [nome, *ALIASES_EXTRA.get(cod, [])]
    texto = template.replace(
        "aliases: [<Nome>]",
        "aliases: [" + ", ".join(json.dumps(a, ensure_ascii=False) for a in aliases) + "]",
    )
    texto = texto.replace("<Nome> (<COD>)", stem)

    if GENERICA.match(cod):
        linhas = [l for l in texto.splitlines() if not l.startswith(CAMPOS_1_PERNA)]
        linhas.insert(linhas.index("composta_de: []"), "familia: generica")
        texto = "\n".join(linhas) + "\n"
        texto = re.sub(r"## Pernas\n\n\|.*\|\n\|.*\|\n\n", "", texto)

    return texto


def registrar_hashes(arquivos: list[Path]) -> None:
    atuais = {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in arquivos}
    if not HASHES.exists():
        HASHES.write_text(json.dumps(atuais, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"hashes registrados: {len(atuais)}")
        return
    registrados = json.loads(HASHES.read_text(encoding="utf-8"))
    for nome in sorted(registrados.keys() | atuais.keys()):
        if registrados.get(nome) != atuais.get(nome):
            print(f"ALERTA hash diferente do registrado: {nome}")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    template = TEMPLATE.read_text(encoding="utf-8")
    arquivos = sorted(BLOOMBERG.glob("*.md"))
    criadas, existentes = [], []

    for f in arquivos:
        m = NOME_COD.match(f.stem)
        if not m:
            print(f"ERRO nome fora do padrão '<Nome> (<COD>).md': {f.name}")
            return 1
        destino = STRUCTURES / f"{m['cod']}.md"
        if destino.exists():
            existentes.append(destino.name)
            continue
        destino.write_text(nota(template, f.stem, m["nome"], m["cod"]), encoding="utf-8", newline="\n")
        criadas.append(destino.name)

    registrar_hashes(arquivos)
    print(f"criadas: {len(criadas)} | já existiam: {len(existentes)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
