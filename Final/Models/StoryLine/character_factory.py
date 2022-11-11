from Characters.character import Character
from Characters.warrior import Warrior
from Characters.wizard import Wizard
from Characters.rogue import Rogue
from Characters.cleric import Cleric
from enum import Enum

class Character_Type(Enum):
    GUERREIRO = 1
    MAGO = 2
    LADINO = 3
    CLERIGO = 4
    
class Character_Factory:
    
    @staticmethod
    def create(character_type) -> Character:
        if character_type == Character_Type.GUERREIRO:
            return Warrior('Guerreiro', 200, 40, 'Lanca de duas maos', 'Espada media e escudo', 'Vigor', 'Investida', 'Potencia')
        if character_type == Character_Type.MAGO:
            return Wizard('Mago', 100, 0, 'Magia: Misseis Magicos', 'Magia: Bola de Fogo', 'Magia: Telecinesia', 'Magia: Sono', 'Inteligencia')
        if character_type == Character_Type.LADINO:
            return Rogue('Ladino', 120, 10, 'Adaga', 'Arco longo', 'Furtividade', 'Corda', 'Destreza')
        if character_type == Character_Type.CLERIGO:
            return Cleric('Clerigo', 150, 20, 'Maca e escudo', 'Magia: Chama Divina', 'Domínio: Passo etereo', 'Magia: Luz cegante', 'Fe')
        else:
            return None