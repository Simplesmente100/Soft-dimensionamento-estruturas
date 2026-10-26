# Instruções para agentes de IA

## Missão
Desenvolver com segurança um software Python para modelagem e dimensionamento de estruturas de madeira para coberturas no contexto brasileiro.

## Regras obrigatórias
- Antes de alterar código, leia o README e os documentos relevantes em `docs/`.
- Não alegue conformidade normativa sem indicar norma, edição, seção aplicável e validação independente.
- Não invente fórmulas, coeficientes, limites, classes de resistência ou combinações de ações.
- Nunca trate resultados deste projeto como projeto estrutural validado.
- Mantenha unidades explícitas em nomes, documentação ou tipos. Documente conversões.
- Separe funções puras de cálculo da interface, arquivos, rede e relatórios.
- Adicione testes para cada mudança: caso nominal, limites e entradas inválidas.
- Não apague testes nem reduza sua cobertura para fazer a suíte passar.
- Não introduza dependências sem explicar a necessidade.
- Não armazene segredos, credenciais ou dados pessoais no código.
- Prefira alterações pequenas, revisáveis e com mensagens de commit claras.
- Se faltar uma referência técnica essencial, interrompa a implementação normativa e registre a dúvida em vez de adivinhar.

## Fluxo de trabalho
1. Inspecione a estrutura e os testes existentes.
2. Resuma a mudança proposta.
3. Implemente a menor alteração coerente.
4. Execute `pytest` e os verificadores disponíveis.
5. Relate arquivos alterados, testes executados e limitações conhecidas.

## Segurança estrutural
O software é experimental. Qualquer cálculo estrutural futuro exige verificação por profissional habilitado, comparação com exemplos independentes e revisão técnica antes de uso real.
