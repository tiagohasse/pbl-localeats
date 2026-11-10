import re
from playwright.sync_api import Page, expect

def test_login_com_credenciais_invalidas_exibe_mensagem_de_erro(page: Page):
    page.goto("https://local-eats-unisenac.vercel.app/")

    page.locator("#loginEmail").fill("usuario_inexistente@teste.com")
    page.locator("#loginPassword").fill("senha_incorreta_123")
    page.locator("#loginForm button.primary-btn").click()

    mensagem_erro = page.locator("#errorMsg")

    expect(mensagem_erro).to_be_visible()

    expect(mensagem_erro).to_contain_text("Invalid credentials")

    expect(page).to_have_url(re.compile(r"login\.html"))