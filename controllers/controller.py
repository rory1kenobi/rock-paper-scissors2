from app import app
from models.player import *
from models.game import *
from flask import render_template, request

@app.route('/<player_1_choice>/<player_2_choice>')
def result(player_1_choice, player_2_choice):
    player_1 = Player("player 1", player_1_choice)
    player_2 = Player("player 2", player_2_choice)
    game = Game()
    winner = game.play(player_1, player_2)
    return render_template("game.html", player_1 = player_1, player_2 = player_2, winner = winner)

@app.route('/')
def home():
    game = Game()
    return render_template("home.html", title = "home")

@app.route('/play', methods=["POST"])
def play_():
    return render_template('play.html', title='Player 1', name1=request.form['name1'])

@app.route('/rock')
def rock():
    return render_template('player2.html', title='Player 2', choice='rock')

@app.route('/paper')
def paper():
    return render_template('player2.html', title='Player 2', choice='paper')

@app.route('/scissors')
def scissors():
    return render_template('player2.html', title='Player 2', choice='scissors')

# @app.route('/computer')
# def play_computer_():
#     player_1_name_input = request.form['player_1_name']
#     player_1_choice_input = request.form['player_1_choice']
#     player_1 = Player(player_1_name_input, player_1_choice_input)
#     game = Game(player_1)
#     player_2 = game.play_computer()
#     choices_list_keys = list(game.the_winner.keys())
#     result = game.play(player_1, player_2)
#     return render_template('game.html', player_1=player_1, player_2=player_2, game=game, result=result, choices=choices_list_keys, title="Results are in!")

