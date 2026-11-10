# Atividade 4: Testes Automatizados do LocalEats

---

## 1. Identificação

- **Turma:** Qualidade de Software (ADS5N26-2C)
- **Modalidade:** Individual
- **Repositório:** https://github.com/tiagohasse/pbl-localeats
- **Diretório da atividade:** https://github.com/tiagohasse/pbl-localeats/tree/main/atividades/atividade-04
- **Data da última execução:** 10/11/2026

### Integrantes

1. Tiago Hasse Niemczewski

---

## 2. Integrantes e responsabilidades

| ID | Integrante responsável | Tipo | Comportamento verificado | Arquivo e função de teste |
|---|---|---|---|---|
| TU01 | Tiago Hasse Niemczewski | Unitário | Avaliação válida dentro do intervalo | `tests/test_regras_localeats.py::test_avaliacao_valida_com_nota_valida` |
| TU02 | Tiago Hasse Niemczewski | Unitário | Avaliação inválida acima do limite | `tests/test_regras_localeats.py::test_avaliacao_invalida_acima_do_limite` |
| TU03 | Tiago Hasse Niemczewski | Unitário | Lançamento de exceção com tipo de dado inválido | `tests/test_regras_localeats.py::test_avaliacao_com_tipo_invalido_lanca_excecao` |
| TF01 | Tiago Hasse Niemczewski | Funcional | Validação de erro ao tentar login com credenciais inválidas | `tests/test_localeats.py::test_login_com_credenciais_invalidas_exibe_mensagem_de_erro` |

---

## 3. Testes unitários

### Regras disponíveis

#### Regra 4: avaliação do restaurante

```python
avaliacao_valida(nota)
```

- Retorna `True` para notas entre 1 e 5.
- Retorna `False` para notas abaixo de 1 ou acima de 5.

### Registro das regras implementadas

#### Regra de Tiago Hasse Niemczewski

- **Regra escolhida:** Regra 4: validar avaliação do restaurante
- **Função implementada:** `avaliacao_valida(nota)`
- **Arquivo da implementação:** `src/regras_localeats.py`
- **Testes criados:** `test_avaliacao_valida_com_nota_valida`; `test_avaliacao_invalida_acima_do_limite`; `test_avaliacao_com_tipo_invalido_lanca_excecao`
- **Comportamentos verificados:** Validação de notas válidas (entre 1 e 5 retornam `True`), rejeição de notas fora do limite permitido (retornam `False`) e verificação de robustez com disparo de exceção (`TypeError`) ao receber tipos não numéricos.

---

## 4. Aplicação do TDD

### TDD de Tiago Hasse Niemczewski

- **Regra escolhida:** Regra 4: validar avaliação do restaurante
- **Primeiro teste escrito:** `test_avaliacao_valida_com_nota_valida`
- **Por que o teste falhou inicialmente:** O teste falhou durante a fase de coleta com `ImportError: cannot import name 'avaliacao_valida' from 'src.regras_localeats'`, pois o arquivo `src/regras_localeats.py` estava inicialmente vazio e a função ainda não existia.
- **Implementação mínima realizada:** Foi criada a declaração da função `avaliacao_valida(nota)` retornando o valor estático `True`, o que foi o mínimo suficiente para fazer o primeiro teste passar (fase Green).
- **Segundo teste escrito:** `test_avaliacao_invalida_acima_do_limite`
- **Melhoria ou refatoração realizada:** Ao introduzir o segundo teste com uma nota acima de 5 (esperando `False`), o teste falhou com `AssertionError: assert True is False`. Refatoramos a implementação para a expressão idiomática `return 1 <= nota <= 5`, fazendo com que ambos os testes passassem. Em seguida, adicionamos o terceiro teste (`test_avaliacao_com_tipo_invalido_lanca_excecao`) com `pytest.raises(TypeError)` para validar resiliência contra tipos não comparáveis, como strings.

---

## 5. Testes funcionais com Playwright

**Sistema:** https://local-eats-unisenac.vercel.app/

### Requisitos de cada teste funcional

- acessar o LocalEats;
- realizar pelo menos uma interação pela interface;
- utilizar locators do Playwright;
- possuir pelo menos duas assertions;
- verificar resultados observáveis;
- não utilizar `time.sleep`;
- executar com pytest;
- identificar o integrante responsável no código.

### Teste funcional de Tiago Hasse Niemczewski

- **ID:** `TF01`
- **Fluxo automatizado:** Tentativa de login no sistema com credenciais inválidas.
- **Interação realizada:** Acesso à página inicial do LocalEats (que redireciona para a tela de autenticação `login.html`), preenchimento dos campos de e-mail (`#loginEmail`) e senha (`#loginPassword`) com dados inexistentes e clique no botão de submissão (`#loginForm button.primary-btn`).
- **Primeira assertion:** A caixa de mensagem de erro (`#errorMsg`) torna-se visível na tela (`expect(mensagem_erro).to_be_visible()`).
- **Segunda assertion:** O conteúdo textual da notificação informa que as credenciais são inválidas (`expect(mensagem_erro).to_contain_text("Invalid credentials")`).
- **Arquivo e função:** `tests/test_localeats.py::test_login_com_credenciais_invalidas_exibe_mensagem_de_erro`
- **Resultado final:** aprovado

---

## 6. Resultado da execução

- **Quantidade total de testes:** 4
- **Testes aprovados:** 4
- **Testes reprovados:** 0
- **Link para o relatório:** [relatorio-pytest.txt](relatorio-pytest.txt)
- **Observações:** Todos os testes foram executados e aprovados com sucesso.

---

## 7. Explicações individuais

### Explicação do teste de Tiago Hasse Niemczewski

- **Teste escolhido:** `tests/test_localeats.py::test_login_com_credenciais_invalidas_exibe_mensagem_de_erro`
- **Comportamento verificado:** Verifica se o sistema impede o acesso indevido e notifica visualmente o usuário caso credenciais inválidas sejam informadas na tela de autenticação.
- **Dados ou estado inicial:** Navegador aberto na página de login do LocalEats (`https://local-eats-unisenac.vercel.app/`), com os campos vazios e a mensagem de erro inicialmente oculta.
- **Resultado esperado:** Ao submeter o formulário com dados incorretos, o sistema deve acionar o elemento de erro `#errorMsg` exibindo o texto `"Invalid credentials"`, garantindo que o usuário permaneça na tela de login.
- **O que faria o teste falhar:** O teste falharia caso a aplicação permitisse o login indevidamente, se não exibisse a mensagem de alerta, se o texto da notificação fosse alterado, ou se os seletores dos elementos (`#loginEmail`, `#loginPassword`, `#errorMsg`) fossem modificados na interface.

---

## 8. Uso de inteligência artificial

- **Ferramenta utilizada:** Google Antigravity / Gemini
- **Como a ferramenta foi utilizada:** Como apoio e tutoria em pair programming, orientando o roteiro do ciclo TDD (Red, Green, Refactor), auxiliando na inspeção técnica dos elementos da interface real do LocalEats e na formatação das asserções e documentação.
- **Uma sugestão que precisou ser alterada ou rejeitada:** A IA sugeriu inicialmente como terceiro teste unitário (`TU03`) testar a nota `0`, rotulando-o como "caso de borda".
- **Motivo da alteração ou rejeição:** Notei criticamente que testar a nota `0` era conceitualmente redundante em relação ao teste de nota `6` (ambos cobriam apenas as partições de equivalência inválidas fora do intervalo 1 a 5). Por isso, recusei a sugestão e propus testar um caso anômalo de tipo de dado inválido (string `"excelente"`) com `pytest.raises(TypeError)`, tornando a suíte muito mais rigorosa e cobrindo dois diferenciais técnicos da disciplina.
- **Como o código sugerido foi verificado:** Todos os testes foram executados manualmente no PowerShell com `pytest` e `pytest-playwright` (inclusive com `--headed --slowmo 1000` para conferência visual de cada interação), validando tanto os momentos de falha esperada quanto a aprovação final.

---

## 9. Diferenciais opcionais

- [x] Terceiro teste unitário para caso de borda.
- [x] Uso de `pytest.raises` para verificar exceção.
- [ ] Parametrização com `pytest.mark.parametrize`.
- [ ] Cenário BDD em Gherkin.
- [ ] Automação com `pytest-bdd`.
- [ ] Organização com Page Object Model.
- [ ] Segundo teste funcional pelo mesmo integrante.
- [ ] Execução em mais de um navegador.
- [ ] Screenshot, vídeo ou trace do Playwright.
- [ ] Registro de uma falha encontrada e corrigida.

### Descrição dos diferenciais

- **Terceiro teste unitário para caso de borda / entrada anômala:** Foi implementado o teste `test_avaliacao_com_tipo_invalido_lanca_excecao` em `tests/test_regras_localeats.py`, que valida a resiliência da função contra entradas de tipos inválidos (passagem de string em vez de valor numérico).
- **Uso de `pytest.raises` para verificar exceção:** O teste `test_avaliacao_com_tipo_invalido_lanca_excecao` utiliza o gerenciador de contexto `with pytest.raises(TypeError):` para interceptar e validar formalmente a exceção de tipo disparada pela linguagem, comprovando que entradas inadequadas são rejeitadas com erro explícito.

---