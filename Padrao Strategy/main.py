from personagem import personagem
from  mago import mago
from lutador import lutador
from atirador import atirador

mago = personagem(mago(10))
lutador = personagem(lutador(20))
atirador = personagem(atirador(15))

mago.tipo_habilidade()
lutador.tipo_habilidade()
atirador.tipo_habilidade()
