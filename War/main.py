from classes import Deck
from classes import Player

def wonWar( cardsUser, cardsCPU ):
    print('Bora tirar as cartas e começar uma guerra')
    number_turns = 3

    for turn in range(number_turns):
        if cardsUser[turn].getValue() > cardsCPU[turn].getValue():
            return 'User'
        elif cardsUser[turn].getValue() < cardsCPU[turn].getValue():
            return 'Cpu'

    return 'nobody'


def main():

    try:
        wannaPlay = input('Deseja jogar? (Yes/No) ')

        if wannaPlay.lower() != 'yes':
            return

        deck = Deck()
        user = Player()
        cpu = Player()
        user.setHand( deck.distribuiteCardsPlayer1() )
        cpu.setHand( deck.distribuiteCardsPlayer2() )

        while len(user)>0 and len(cpu)>0:

            print('\n \n')
            print('User tem ', len(user), ' cartas')
            print('Cpu tem ', len(cpu), ' cartas')

            wannaGetCard = input('Deseja virar uma carta? (Yes/No) ')

            if wannaGetCard.lower() != 'yes':
                break

            cardUser = user.play()
            cardCPU = cpu.play()
            winnerCards = [cardUser, cardCPU]

            print('\n usuário', cardUser.getRank() )
            print('computador', cardCPU.getRank() )

            if cardUser.getValue() > cardCPU.getValue():
                print('Usuário ganhou a rodada \n\n')
                user.winTurn( winnerCards )
                continue

            elif cardUser.getValue() < cardCPU.getValue():
                print('Cpu ganhou a rodada \n\n')
                cpu.winTurn( winnerCards )
                continue

            else:
                print('Guerraaaaaaaaa war war war')

                while len(user) >= 3 and len(cpu) >= 3:

                    cardsUser = user.war()
                    cardsCPU = cpu.war()
                    winnerCards = winnerCards + cardsCPU
                    winnerCards = winnerCards + cardsUser

                    winner = wonWar( cardsUser, cardsCPU )

                    if winner == 'User':
                        print('User venceu a rodada  \n\n')
                        user.winTurn( winnerCards )
                        break

                    elif winner == 'Cpu':
                        print('Cpu venceu a rodada  \n\n')
                        cpu.winTurn( winnerCards )
                        break

                else:
                    break

                continue


        if len(user) > len(cpu):
            print(' \n\n Vitória do proletariado')
        else:
            print('  \n\n Vitória da máquina')

    except:
        print('Erro!')


    finally:
        print('Fim de jogo')


main()
