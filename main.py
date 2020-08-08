if __name__ == '__main__':
    from Game import Game
    get_input = input("Please enter the number each player must get to play the game:")
    game = Game(get_input)
    game.play_game()
