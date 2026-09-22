# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

## 1. Identificação

**Turma:** Qualidade de Software (ADS5N26-2C)  
**Equipe:** Trabalho Individual  
**Data:** 22/09/2026

### Integrantes

| Nome                    | Usuário no GitHub                            |
| ----------------------- | -------------------------------------------- |
| Tiago Hasse Niemczewski | [@tiagohasse](https://github.com/tiagohasse) |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo      | Necessidade                                                                            | Interessado                                            | Consequência se não for atendida                                                                                                                       |
| --------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Explícita | Permitir a realização de pedidos para os restaurantes locais.                          | Cliente e Restaurante                                  | O cliente não consegue efetuar compras e os restaurantes não realizam vendas, inviabilizando a finalidade principal do negócio.                        |
| Explícita | Permitir a consulta aos pedidos realizados e seus detalhes.                            | Cliente                                                | O cliente não consegue acompanhar a situação ou histórico de suas compras, gerando insegurança e sobrecarga nos canais de suporte.                     |
| Implícita | Armazenamento e proteção segura de credenciais e senhas (uso de hashing/criptografia). | Usuários (Clientes/Restaurantes) e a Empresa LocalEats | Risco de vazamento de credenciais em caso de invasão, comprometimento de contas pessoais, perda de credibilidade da marca e penalidades legais (LGPD). |
| Implícita | Interface responsiva e confortável para navegação e pedidos em dispositivos móveis.    | Cliente (consumidor final)                             | Dificuldade ou impossibilidade de navegação em smartphones, cliques acidentais em botões pequenos, frustração do usuário e abandono do aplicativo.     |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

Sim. Ter todas as funcionalidades implementadas não garante a satisfação do usuário se as necessidades implícitas forem ignoradas. Por exemplo, se o usuário tentar acessar o LocalEats em seu smartphone e não conseguir navegar confortavelmente por conta de botões diminutos ou formatação desajustada de layout, a experiência será frustrante e o sistema será julgado como de baixa qualidade, mesmo que o pedido pudesse ser concluído.

---

## 3. Tarefa 2: Exploração da aplicação

| Integrante              | Funcionalidade | O que foi realizado                                                                                                                                                                                                  | O que foi observado                                                                                                                                                                                           | Evidência                                                                                                                                   |
| ----------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Tiago Hasse Niemczewski | Fazer pedido   | **Uso esperado:** Adição de item ao pedido (Prato Especial 0) e clique em "Finalizar Pedido" logado.<br>**Uso alternativo:** Adição de item ao pedido seguida de recarregamento da página (F5) antes da finalização. | No uso esperado, o componente flutuante exibe o total e permite finalizar gerando confirmação. No uso alternativo (F5), todo o carrinho é esvaziado imediatamente sem persistência de estado ou aviso prévio. | [ver antes do F5](evidencias/fazer-pedido-carrinho-antes-f5.png) \| [ver depois do F5](evidencias/fazer-pedido-carrinho-zerado-apos-f5.png) |

---

## 4. Tarefa 3: Requisitos e características de qualidade

| Integrante              | Requisito de Qualidade                                                                                                                                                                                                                            | Característica ou subcaracterística                 | Justificativa                                                                                                                                                                                                                                                                                                                                                   | Como avaliar                                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tiago Hasse Niemczewski | O sistema deve preservar o estado e os itens do carrinho de compras localmente durante a sessão do usuário, permitindo recuperar o pedido em caso de recarregamento acidental da página (F5), queda de conexão ou encerramento inesperado da aba. | Confiabilidade / Recuperabilidade (*ISO/IEC 25010*) | Em um aplicativo de delivery, o cliente despende tempo escolhendo pratos. Se faltar luz, houver oscilação de rede ou recarregamento involuntário da página, a perda abrupta dos dados causa frustração e abandono da compra. A capacidade de restabelecer o estado (recuperabilidade) preserva o esforço do cliente e garante a continuidade do fluxo de venda. | Adicionar um ou mais itens ao carrinho, recarregar a página (F5) no mesmo navegador e comparar se a lista de itens, quantidades e valor total permanecem idênticos ao estado prévio à interrupção. |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Antigravity / Gemini

**Como foi utilizada:**  
Utilizada de forma interativa como tutoria pedagógica para estruturar o documento no padrão sugerido, debater a formulação de necessidades explícitas e implícitas e mapear a subcaracterística formal da norma ISO/IEC 25010 (Confiabilidade / Recuperabilidade) correspondente ao cenário testado.

**Como as respostas foram verificadas:**  
A aplicação LocalEats foi explorada manualmente pelo próprio estudante no navegador, reproduzindo os cenários esperados e alternativos e gerando as capturas de tela das evidências. As justificativas e respostas conceituais foram formuladas com base nos conceitos da disciplina e compreendidas para sustentação na defesa técnica oral.

