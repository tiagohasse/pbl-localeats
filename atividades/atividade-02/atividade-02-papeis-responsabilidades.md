# Atividade 2: Organização da Qualidade no LocalEats

## 1. Identificação

**Turma:** Qualidade de Software (ADS5N26-2C)  
**Equipe:** Trabalho Individual  
**Data:** 22/09/2026

### Integrantes

| Nome                    | Usuário no GitHub                            |
| ----------------------- | -------------------------------------------- |
| Tiago Hasse Niemczewski | [@tiagohasse](https://github.com/tiagohasse) |

**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado                                           | Possível consequência para o produto ou para a equipe                                                                                       |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Funcionalidades chegam aos usuários com defeitos.               | Perda de credibilidade e evasão de usuários (churn), que ficam impossibilitados de concluir pedidos e migram para plataformas concorrentes. |
| Alguns integrantes acreditam que somente o QA deve testar.      | Sobrecarga e gargalo no profissional de QA com falhas simples, atrasando entregas e gerando retrabalho evitável desde a escrita do código.  |
| Defeitos são identificados, mas nem sempre registrados/seguidos. | Retrabalho de reteste desnecessário (bugs reportados várias vezes), perda de visibilidade de riscos críticos e lentidão para correção.     |

### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

Não. A qualidade é uma responsabilidade compartilhada por toda a equipe (Whole Team Approach). Enquanto o QA orienta as práticas de teste, prevenção e acompanhamento de falhas, ele não programa nem corrige o código sozinho. A qualidade precisa ser construída desde o início: o PO definindo regras claras, os desenvolvedores implementando com testes unitários e boas práticas, e o time todo garantindo que o produto chegue estável ao usuário.

---

## 3. Tarefa 2: Papéis e competências

| Integrante              | Papel analisado                     | Responsabilidades relacionadas à qualidade                                                                                                                                              | Competências técnicas                                                                                                                   | Competências comportamentais                                                                                                          |
| ----------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Tiago Hasse Niemczewski | Analista de Qualidade (QA)          | Encontrar e documentar defeitos e desvios de regras no app; planejar e projetar casos de teste; apoiar na validação dos critérios de aceite; mitigar riscos antes de versões subirem.   | Entendimento das regras de negócio e expectativas do usuário; técnicas de teste funcional (caixa-preta); noções de funcionamento web/APIs. | Comunicação assertiva (clareza nos relatos de bugs); empatia (evitar atritos com devs); pensamento crítico (priorização baseada em risco). |
| (Equipe LocalEats)      | Responsável pelo Produto (PO)       | Definir critérios de aceitação claros nas histórias de usuário; validar regras de negócio com stakeholders; priorizar a resolução de defeitos conforme o valor gerado para o cliente. | Gestão de requisitos e backlog; mapeamento de regras de negócio; métricas de produto e experiência do usuário.                           | Tomada de decisão, negociação transparente e escuta ativa.                                                                            |
| (Equipe LocalEats)      | Desenvolvedor (Dev)                 | Implementar funcionalidades aderentes aos requisitos; escrever testes unitários; revisar código de pares (peer review); corrigir defeitos com agilidade e qualidade.                  | Linguagens de programação, arquitetura de sistemas, frameworks de testes unitários e versionamento com Git.                              | Atenção a detalhes, capacidade de resolução analítica de problemas e espírito de colaboração.                                         |
| (Equipe LocalEats)      | Liderança Técnica (Tech Lead)       | Definir diretrizes de arquitetura e padrões de código; aprovar revisões críticas de código; assegurar padrões não funcionais (segurança e performance); orientar boas práticas do time.  | Engenharia de software avançada, arquitetura de microsserviços/APIs, automação de integração contínua (CI/CD) e segurança.               | Liderança técnica, mentoria de equipe e visão sistêmica holística.                                                                    |

---

## 4. Tarefa 3: Matriz de responsabilidades

Utilizem:

- **R:** responsável por executar a atividade;
- **A:** aprovador ou responsável final;
- **C:** consultado antes da execução ou decisão;
- **I:** informado sobre o resultado.

| Atividade de qualidade                 |   PO    |   Dev   |   QA    | Tech Lead |
| -------------------------------------- | :-----: | :-----: | :-----: | :-------: |
| Definir critérios de aceitação         |  **A**  |    C    |  **R**  |     C     |
| Revisar requisitos                     |  **A**  |  **R**  |  **R**  |     C     |
| Implementar a funcionalidade           |    I    |  **R**  |    I    |   **A**   |
| Revisar o código                       |    I    |  **R**  |    I    |   **A**   |
| Criar testes unitários                 |    I    |  **R**  |    C    |   **A**   |
| Planejar e executar testes do sistema  |    I    |    C    | **R/A** |     I     |
| Registrar e acompanhar defeitos        |    I    |  **R**  | **R/A** |     I     |
| Priorizar a correção dos defeitos      |  **A**  |    I    |    C    |     C     |
| Aprovar a disponibilização da versão   |  **A**  |    I    |    C    |     C     |

### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**  
Definição dos critérios de aceitação.

**Consequência:**  
Esta atividade carrega o maior risco de falha por exigir comunicação constante e alinhamento próximo entre PO, QA e Desenvolvedores. Se o PO redigir critérios de forma isolada ou superficial, regras importantes e cenários de exceção serão omitidos. Como consequência, o desenvolvedor implementará com base em suposições e o QA não terá parâmetros objetivos para distinguir entre um defeito e um comportamento esperado, gerando retrabalho e atritos desnecessários.

### 4.2 Práticas de QA recomendadas

| Prática recomendada                               | Problema que ajuda a resolver                                                                                                                  | Papéis envolvidos               |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **Reuniões Diárias (*Daily Meetings*)**           | Falta de comunicação e desalinhamento contínuo entre os membros; demora para expor impedimentos e falhas bloqueantes no dia a dia.            | PO, Dev, QA e Tech Lead         |
| **Alinhamento Pré-Teste (*Test Kick-Off*)**       | Entrega de código "por cima do muro" para o QA sem alinhamento prévio; minimiza bugs triviais e reduz o tempo de testes antes da homologação. | Desenvolvedor (Dev) e QA        |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Antigravity / Gemini

**Como foi utilizada:**  
Utilizada de forma interativa como tutoria para estruturar o diagnóstico organizacional da equipe, debater a diferenciação conceitual entre responsabilidades, hard skills e soft skills do papel de QA, e formatar a distribuição da matriz RACI e práticas ágeis.

**Como as respostas foram verificadas:**  
Todas as respostas foram formuladas a partir de reflexões críticas do próprio estudante, contextualizadas para a realidade do LocalEats e validadas para garantir domínio e capacidade de sustentação na defesa técnica oral.

