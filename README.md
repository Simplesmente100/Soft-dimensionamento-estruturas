# Software de Dimensionamento de Estruturas

Projeto de software em Python para apoiar a **modelagem, análise, dimensionamento e detalhamento de estruturas de madeira para coberturas**, com quantitativos de materiais e documentação técnica.

> **Aviso de segurança:** este repositório está em fase inicial. O código ainda não constitui ferramenta de cálculo estrutural validada e não deve ser usado, isoladamente, para projetar, liberar ou executar estruturas reais. Qualquer resultado futuro deverá ser verificado por engenheiro habilitado, com responsabilidade técnica, hipóteses explícitas, testes independentes e conferência das normas brasileiras vigentes.

## Objetivos

- Modelar geometria de coberturas e elementos estruturais.
- Organizar ações, combinações e verificações de cálculo em módulos testáveis.
- Apoiar o dimensionamento de peças de madeira e ligações, após validação técnica.
- Gerar desenhos, relatórios de cálculo e quantitativos de materiais.
- Manter rastreabilidade de hipóteses, unidades, referências normativas e versões.
- Facilitar contribuições de desenvolvedores e agentes de IA por meio de instruções explícitas e testes automatizados.

## Estado atual

O projeto contém uma estrutura inicial de pacote Python e uma função geométrica simples para propriedades de uma seção retangular. **Não há ainda um motor de dimensionamento estrutural completo.**

## Começar

Requer Python 3.11 ou superior.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux/macOS:
# source .venv/bin/activate

python -m pip install -e ".[dev]"
pytest
```

## Organização

```text
src/soft_estruturas/   # código da aplicação
tests/                 # testes automatizados
docs/                  # escopo, metodologia e validação
AGENTS.md              # instruções para agentes de IA
CONTRIBUTING.md        # fluxo de contribuição
```

## Princípios de desenvolvimento

1. Usar unidades explícitas e documentadas; evitar misturar unidades no mesmo cálculo.
2. Separar geometria, ações, análise, verificações normativas, interface e relatórios.
3. Testar casos de referência e limites; nunca confiar apenas em exemplos gerados por IA.
4. Registrar as hipóteses e a fonte técnica de cada verificação estrutural.
5. Não inventar parâmetros normativos. Confirmar a edição vigente das normas antes de implementar verificações.
6. Não incluir senhas, tokens ou chaves de API no repositório.
7. Submeter cálculos estruturais a revisão independente antes de qualquer uso profissional.

## Contribuição

Leia [CONTRIBUTING.md](CONTRIBUTING.md) e [AGENTS.md](AGENTS.md) antes de modificar o projeto. Consulte também o [plano de desenvolvimento](docs/ROADMAP.md).

## Licença

Ainda não foi definida. Até a inclusão de uma licença, todos os direitos permanecem reservados; a publicação do código não concede automaticamente permissão de reutilização.
