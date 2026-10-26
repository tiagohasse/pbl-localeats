# Registro do ciclo de TDD

## Comportamento escolhido

Cobrar taxa fixa de R$ 5 para entregas em distâncias de até 3 km (cenário: 2 km e pedido de R$ 50).

## Red

**Teste criado:** `test_taxa_entrega_distancia_ate_3km`

**Motivo da falha:** A função `calcular_taxa_entrega` ainda não havia sido definida em `src/pedido.py`, resultando em erro de importação (`ImportError: cannot import name 'calcular_taxa_entrega'`).

## Green

**Implementacao realizada:** Declaração da função `calcular_taxa_entrega(distancia_km, total_pedido)` retornando o valor fixo `5` (`return 5`), aplicando a estratégia do menor código possível (*Fake It*) para fazer o teste passar.

## Refactor

**Melhoria realizada:** Nenhuma refatoração estrutural foi necessária neste primeiro ciclo, mantendo o código conciso e direto.

**Resultado final:** Toda a suíte passou com sucesso: 5 testes aprovados (`5 passed`), sem regressão nas funções anteriores.

---

# Ciclo 2

## Comportamento escolhido

Cobrar taxa adicional de R$ 2 por quilômetro que exceder 3 km (cenário: 4 km e pedido de R$ 50 -> taxa R$ 7).

## Red

**Teste criado:** `test_taxa_entrega_distancia_acima_de_3km`

**Motivo da falha:** A função retornava o valor fixo `5`, gerando falha de asserção (`AssertionError: assert 5 == 7`).

## Green

**Implementacao realizada:** Adicionada condição `if distancia_km > 3:` calculando `5 + (distancia_km - 3) * 2`.

## Refactor

**Melhoria realizada:** Nenhuma refatoração necessária no momento; lógica simples e legível.

**Resultado final:** Toda a suíte passou com sucesso: 6 testes aprovados (`6 passed`).

---

# Ciclo 3

## Comportamento escolhido

Garantir entrega gratuita para pedidos com valor total igual ou superior a R$ 100 (cenário: 5 km e pedido de R$ 100 -> taxa R$ 0).

## Red

**Teste criado:** `test_taxa_entrega_gratis_a_partir_de_100_reais`

**Motivo da falha:** O cálculo aplicava a regra de quilometragem sem verificar o valor do pedido, retornando 9 em vez de 0 (`AssertionError: assert 9 == 0`).

## Green

**Implementacao realizada:** Adicionada verificação no início da função `if total_pedido >= 100: return 0`.

## Refactor

**Melhoria realizada:** Extração de valores literais para constantes com nomes semânticos (`TAXA_BASE = 5` e `LIMITE_FRETE_GRATIS = 100`). Isso aumenta a legibilidade, facilita manutenções futuras e centraliza as regras de negócio sem alterar o comportamento ou quebrar os testes existentes.

**Resultado final:** Toda a suíte passou com sucesso: 7 testes aprovados (`7 passed`).