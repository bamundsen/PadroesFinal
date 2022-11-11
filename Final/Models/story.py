from Characters.character import Character
from StoryLine.character_factory import Character_Factory
from StoryLine.character_factory import Character_Type

class Story:
    def __init__(self) :
        self.character = Character
        self.list_answers = int
    
    
if __name__ == '__main__':
    story_1 = Story
    
    answer = -1
    jobs = [None, Character_Type.GUERREIRO, Character_Type.MAGO, Character_Type.LADINO, Character_Type.CLERIGO]
    while(answer <1 or answer >4):
        print('Sua aventura comeca agora, escolha o tipo de heroi que voce e: '
            '\n1 - Guerreiro\n2 - Mago\n3 - Ladino\n4 - Clerigo')
        answer = int(input())
        

   
    story_1.list_answers = answer
    story_1.character = Character_Factory.create(jobs[answer])
    print(f'Sua classe e: {story_1.character.name}\nSeus pontos de vida sao: {story_1.character.hp}\nSeus ataques sao: {story_1.character.attack_1} e {story_1.character.attack_2}\nSua quintessencia e: {story_1.character.quintessence}')
    