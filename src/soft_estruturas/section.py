"""Propriedades geométricas básicas de seções transversais.

Estas funções calculam apenas propriedades geométricas ideais; não realizam
dimensionamento estrutural nem verificações normativas.
"""

from math import isfinite


def rectangular_area(width_m: float, height_m: float) -> float:
    """Retorna a área de um retângulo em m² a partir de dimensões em metros.

    Raises:
        ValueError: se uma dimensão não for finita ou não for positiva.
    """
    if not isfinite(width_m) or not isfinite(height_m):
        raise ValueError("As dimensões devem ser números finitos.")
    if width_m <= 0 or height_m <= 0:
        raise ValueError("As dimensões devem ser positivas.")
    return width_m * height_m


def rectangular_second_moment(width_m: float, height_m: float) -> float:
    """Momento de inércia geométrico em m⁴ em torno do eixo centroidal paralelo à largura.

    A expressão é I = b*h³/12. As dimensões devem ser fornecidas em metros.
    Não representa, por si só, uma verificação de resistência ou estabilidade.
    """
    if not isfinite(width_m) or not isfinite(height_m):
        raise ValueError("As dimensões devem ser números finitos.")
    if width_m <= 0 or height_m <= 0:
        raise ValueError("As dimensões devem ser positivas.")
    return width_m * height_m**3 / 12.0
