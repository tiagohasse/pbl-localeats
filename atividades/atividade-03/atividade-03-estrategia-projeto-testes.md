# Atividade 3: Estratégia e Projeto de Testes do LocalEats

## 1. Identificação

**Turma:** Qualidade de Software (ADS5N26-2C)  
**Equipe:** Trabalho Individual  
**Data:** 22/09/2026

### Integrantes

| Nome                    | Usuário no GitHub                            |
| ----------------------- | -------------------------------------------- |
| Tiago Hasse Niemczewski | [@tiagohasse](https://github.com/tiagohasse) |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

Garantir que o usuário consiga adicionar itens no seu carrinho e finalizar o pedido sem inconsistências de valores ou perda de dados.

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante              | Funcionalidade incluída | O que será verificado                                                                                |
| ----------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------- |
| Tiago Hasse Niemczewski | Fazer pedido            | Adição e remoção de itens do cardápio, recálculo de valores, persistência de estado e checkout final. |

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa                                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------------------------- |
| Criar conta                 | O foco principal do ciclo de testes é o fluxo financeiro e operacional da conclusão de compras no app. |

### 2.3 Abordagem

| Item                                    | Decisão da equipe                                    | Justificativa                                                                                                |
| --------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Níveis de teste                         | Teste de Sistema (*System Testing*)                  | Avaliação do fluxo completo de compra através da interface web, do cardápio ao modal de confirmação.        |
| Tipos de teste                          | Funcional e Não funcional (Confiabilidade)           | Validar o cumprimento das regras de cálculo/pedido e a capacidade de retenção de dados diante de interrupção. |
| Perspectiva caixa-preta ou caixa-branca | Caixa-preta (*Black-box*)                            | O foco está nas entradas (ações de clique e seleção) e resultados observáveis em tela, sem acesso ao código. |
| Técnicas de teste                       | Transição de Estados e Particionamento/Valor Limite  | Transição para o ciclo do carrinho/F5 e equivalência para limites de quantidade e regras de cálculo do total. |

### 2.4 Ambiente e responsabilidades

| Item                                      | Definição                                                                                                   |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Ambiente necessário                       | Navegador Google Chrome/Firefox atualizado, conexão de rede e usuário previamente cadastrado e autenticado. |
| Responsáveis pelo planejamento            | Tiago Hasse Niemczewski                                                                                     |
| Responsáveis pela especificação dos casos | Tiago Hasse Niemczewski                                                                                     |
| Responsáveis pela futura execução         | Tiago Hasse Niemczewski                                                                                     |

### 2.5 Critérios

| Critério  | Definição da equipe                                                                                             |
| --------- | --------------------------------------------------------------------------------------------------------------- |
| Entrada   | Aplicação LocalEats acessível, cardápios carregados com itens disponíveis e usuário de teste autenticado.       |
| Saída     | 100% dos casos de teste planejados executados com registros de resultados e defeitos impeditivos documentados.   |
| Suspensão | Indisponibilidade total do servidor/sistema (erro 500/offline) ou falha crítica que impeça abrir restaurantes.  |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

| ID  | Integrante              | Funcionalidade | Risco                                                                                                | Consequência                                                                                                    | Probabilidade | Impacto | Prioridade | Justificativa                                                                                             |
| --- | ----------------------- | -------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | :-----------: | :-----: | :--------: | --------------------------------------------------------------------------------------------------------- |
| R01 | Tiago Hasse Niemczewski | Fazer pedido   | Perda do estado e itens do carrinho ao recarregar a página (F5) ou em oscilações de rede.            | Frustração do cliente por perder o tempo de seleção dos pratos, abandono do carrinho e perda direta de vendas. |     Alta      |  Alto   |    Alta    | Falha comprovada em exploração: o carrinho reside em memória volátil e é zerado sem aviso prévio no F5.   |
| R02 | Tiago Hasse Niemczewski | Fazer pedido   | Inconsistência no recálculo de valores ou permanência indevida do botão de finalizar ao zerar itens. | Cobrança com divergência em relação aos pratos selecionados ou tentativa de submeter pedidos sem itens.         |     Média     |  Alto   |    Alta    | A manipulação dinâmica de pratos exige atualização matemática exata e bloqueio de estados vazios (0 itens). |

### 3.2 Aplicação das técnicas

#### Análise do integrante 1 - R01

**Integrante:** Tiago Hasse Niemczewski  
**Funcionalidade:** Fazer pedido  
**Risco relacionado:** R01  
**Técnica escolhida:** Transição de estados  

**Por que a técnica foi escolhida:**  
A técnica é ideal para validar o comportamento de sistemas que reagem a eventos externos e mudam de estado sequencialmente, permitindo verificar como a aplicação se comporta perante interrupções e recarregamentos de página.

**Aplicação da técnica:**  
* **Estado 1 (E1):** Carrinho Vazio (nenhum item selecionado, botão "Finalizar Pedido" ausente).
* **Evento 1:** Adicionar Prato Especial 0 $\rightarrow$ Transição para **Estado 2 (E2)**.
* **Estado 2 (E2):** Carrinho Ativo (1 item presente, total R$ 59,17, botão habilitado).
* **Evento 2 (Interrupção):** Recarregar a página (F5).
  * *Comportamento Esperado:* Permanece no **Estado 2 (E2)** (estado recuperado com itens preservados).
  * *Comportamento Observado no app:* Retorna indevidamente ao **Estado 1 (E1)** (carrinho zerado).
* **Evento 3:** Clicar em "Finalizar Pedido" $\rightarrow$ Transição para **Estado 3 (E3)**.
* **Estado 3 (E3):** Pedido Concluído (modal de confirmação em tela e carrinho liberado).

**Casos derivados:** CT01 e CT02

---

#### Análise do integrante 1 - R02

**Integrante:** Tiago Hasse Niemczewski  
**Funcionalidade:** Fazer pedido  
**Risco relacionado:** R02  
**Técnica escolhida:** Particionamento de equivalência e análise de valor limite  

**Por que a técnica foi escolhida:**  
A técnica permite particionar as entradas numéricas em classes válidas e inválidas, identificando com precisão os valores de fronteira (limites) em que o sistema deve ativar ou desativar o botão de checkout e recalcular os totais.

**Aplicação da técnica:**  
* **Classe Inválida (C1):** Quantidade de itens no carrinho = 0 (carrinho vazio).
  * *Resultado esperado:* O botão "Finalizar Pedido" deve estar indisponível/oculto e o total zerado.
* **Classe Válida - Limite Mínimo (C2):** Quantidade de itens no carrinho = 1 (fronteira mínima aceitável para um pedido).
  * *Resultado esperado:* Botão "Finalizar Pedido" ativo, quantidade "1 itens" exibida e valor unitário exato.
* **Classe Válida (C3):** Quantidade de itens no carrinho > 1 (múltiplos itens).
  * *Resultado esperado:* Soma aritmética exata de todos os pratos somados.

**Casos derivados:** CT03

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

### CT01: Persistência do carrinho após recarregamento da página (F5)

**Integrante responsável:** Tiago Hasse Niemczewski  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R01  
**Técnica utilizada:** Transição de estados  

**Pré-condição:**  
Usuário autenticado no sistema e página de cardápio de um restaurante aberta.

**Dados de entrada:**  
Prato: "Prato Especial 0" (Valor: R$ 59,17).

**Passos:**

1. Na página do restaurante, clicar no botão "+ Adicionar" do Prato Especial 0.
2. Observar a abertura do componente flutuante "Seu Pedido" com 1 item e valor de R$ 59,17.
3. Pressionar a tecla F5 no teclado ou o botão de recarregar do navegador.

**Resultado esperado:**  
A página é recarregada e o componente flutuante "Seu Pedido" reaparece automaticamente preservado, contendo 1x Prato Especial 0 e o valor total de R$ 59,17.

---

### CT02: Finalização de pedido com sucesso no fluxo padrão

**Integrante responsável:** Tiago Hasse Niemczewski  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R01  
**Técnica utilizada:** Transição de estados  

**Pré-condição:**  
Usuário autenticado, cardápio carregado e prato adicionado ao carrinho flutuante.

**Dados de entrada:**  
Prato: "Prato Especial 0" (Valor: R$ 59,17).

**Passos:**

1. Adicionar o "Prato Especial 0" ao pedido.
2. No componente flutuante "Seu Pedido", clicar no botão "Finalizar Pedido".
3. Aguardar a transição da requisição em tela.

**Resultado esperado:**  
O sistema transiciona para o estado concluído exibindo o modal com o título "Pedido Realizado!", ícone de confirmação e botão "Ver Detalhes", com o carrinho sendo esvaziado.

---

### CT03: Validação de limite mínimo e recálculo ao zerar itens do carrinho

**Integrante responsável:** Tiago Hasse Niemczewski  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R02  
**Técnica utilizada:** Particionamento de equivalência e análise de valor limite  

**Pré-condição:**  
Usuário autenticado na página de cardápio de um restaurante com carrinho vazio.

**Dados de entrada:**  
Prato: "Prato Especial 0" (R$ 59,17). Ação de subtração de quantidade.

**Passos:**

1. Clicar em "+ Adicionar" no Prato Especial 0 (atingindo o limite mínimo válido de 1 item).
2. Constatar que o carrinho exibe "1 itens" e o botão "Finalizar Pedido" está visível e ativo.
3. No componente flutuante do carrinho, clicar no ícone de subtração (-) ao lado do item adicionado para decrementar a quantidade para a classe inválida (0 itens).

**Resultado esperado:**  
A quantidade do item é zerada, o item é removido da listagem, o total financeiro zera e o componente flutuante "Seu Pedido" é ocultado da tela, impedindo a finalização de compras vazias.

---

### 4.2 Matriz de rastreabilidade

| Integrante              | Funcionalidade | Risco ou requisito                                          | Técnica utilizada                                         | Casos de teste |
| ----------------------- | -------------- | ----------------------------------------------------------- | --------------------------------------------------------- | -------------- |
| Tiago Hasse Niemczewski | Fazer pedido   | R01: Perda de dados do carrinho por recarregamento          | Transição de estados                                      | CT01 e CT02    |
| Tiago Hasse Niemczewski | Fazer pedido   | R02: Inconsistência na manipulação de quantidades e cálculo | Particionamento de equivalência e análise de valor limite | CT03           |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Antigravity / Gemini

**Como foi utilizada:**  
Utilizada como ferramenta de diálogo socrático e tutoria para estruturar o plano de testes, mapear riscos operacionais e conectar formalmente as técnicas de projeto de testes às regras do LocalEats.

**Uma sugestão que precisou ser alterada ou rejeitada:**  
A IA sugeriu inicialmente avaliar um risco de tentativa de pedido por usuário não autenticado e aplicar Tabela de Decisão para múltiplos cliques rápidos. Ambas as sugestões foram rejeitadas criticamente pelo estudante: a primeira por ser incompatível com a aplicação (que não permite navegação sem login), e a segunda por ser artificial para o cenário, optando-se de forma mais pertinente por Particionamento de Equivalência e Análise de Valor Limite para o controle de quantidades e cálculo do carrinho.

**Como as respostas foram verificadas:**  
Todos os comportamentos do fluxo de pedidos foram observados e validados diretamente pelo estudante na aplicação LocalEats, assegurando total rastreabilidade, clareza técnica e capacidade de defesa oral das decisões tomadas.

