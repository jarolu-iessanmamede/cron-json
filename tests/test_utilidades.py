import utilidades.utilidades as util


def test_frecuencia_dias_valida():
    assert util.calcular_frecuencia("0y:0M:0w:3d:0h:0m:0s") == 259200

def test_frecuencia_semana_valida():
    assert util.calcular_frecuencia("0y:0M:2w:0d:0h:0m:0s") == 1209600


