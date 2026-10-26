"""Regras de negocio relacionadas ao calculo de pedidos."""


def validar_item(item: dict) -> None:
    """Valida preco e quantidade de um item.

    Raises:
        ValueError: se o preco ou a quantidade nao forem positivos.
    """
    if item["preco"] <= 0:
        raise ValueError("O preco deve ser positivo.")

    if item["quantidade"] <= 0:
        raise ValueError("A quantidade deve ser positiva.")


def calcular_total(itens: list[dict]) -> float:
    """Calcula o total do pedido.

    Uma lista vazia resulta em total igual a zero.
    """
    total = 0

    for item in itens:
        validar_item(item)
        total += item["preco"] * item["quantidade"]

    return total


# EXERCICIO:
# Implemente com TDD a funcao descrita abaixo.
#
TAXA_BASE = 5
LIMITE_FRETE_GRATIS = 100
def calcular_taxa_entrega(distancia_km, total_pedido):
    if distancia_km < 0:
        raise ValueError("A distancia nao pode ser negativa.")

    if total_pedido >= LIMITE_FRETE_GRATIS:
        return 0

    if distancia_km > 3:
        return TAXA_BASE + (distancia_km - 3) * 2
    return TAXA_BASE