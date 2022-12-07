# -*- coding: utf-8 -*-
"""Jogador de Xadrez X Aleatório com jogadas possíveis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q795-j7g8_t9_xxGavRvxQn11Q7cjCgQ

# Importando bibliotecas necessárias
"""

!pip install chess
import chess
import random
import chess.polyglot
from google.colab import drive
import chess.svg

board = chess.Board()

drive.mount("/content/drive")

#criando tabuleiro
board = chess.Board()
board

def obterMelhorJogada(board=board):
  melhorJogada = ""
  with chess.polyglot.open_reader("drive/MyDrive/xadrez/bookfish.bin") as reader:
    for entry in reader.find_all(board):
      melhorJogada = entry.move
      break
  if not melhorJogada:
    print("Não achou jogada")
    melhorJogada = random.sample(list(board.legal_moves), 1)[0]
  return melhorJogada


print("Melhor jogada agora: ", obterMelhorJogada())

valores = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}

def random_move(board):
  legal_moves = []
  for i in board.legal_moves:
    legal_moves.append(i)
  board.push(random.choice(legal_moves))

def funcao_melhorMovimento(board):
  best_moves = []
  max = -999
  for i in board.legal_moves:
    board.push(i)
    move_value = min(board,2) + valor_board(board)
    if (move_value == max):
      best_moves.append(i)
    elif (move_value > max):
      best_moves.clear()
      best_moves.append(i)
      max = move_value
    board.pop()
  board.push(random.choice(best_moves))

def min(board, profundidade):
  pior = 999
  for i in board.legal_moves:
    board.push(i)
    if (profundidade != 0):
      move_value = valor_board(board) + max(board, profundidade - 1)
    else:
      board.pop()		
      return 0		
    if (move_value < pior):
      pior = move_value		
    board.pop()
  return pior


def max(board, profundidade):
  max = -999
  for i in board.legal_moves:
    board.push(i)
    if (profundidade != 0):
      move_value = valor_board(board) + min(board, profundidade - 1)
    else:
      board.pop()		
      return 0		
    if (move_value > max):
      max = move_value		
    board.pop()
  return max


def valor_board(board):
  count = 0;
  pm = board.piece_map()
  for i in pm:
    val = valores[pm[i].piece_type]
    if pm[i].color == chess.WHITE:
      count-=val
    if pm[i].color == chess.BLACK:
      count+=val
  return count;

#decidindo se o jogador X é jogador das brancas ou pretas
branco = random.randint(0, 10)%2==0
if branco:
  print("Você é jogador das brancas")
else:
  print("Você é jogador das pretas")
  move = obterMelhorJogada()
  board.push(move)
board

def obterJogadasPossiveis(board=board):
  jogadas = []
  jogadas += board.legal_moves
  print("total de jogadas possíveis", len(jogadas))
  jogada = random.sample(jogadas, 1)[0]
  return jogada

#oponente jogando
jogada = obterJogadasPossiveis()
board.push(jogada)
board

#oponente jogando
move = input("Jogada: ")
board.push_san(move)
display(board)

print("")

#minha IA jogando:
jogada = obterJogadasPossiveis()
board.push(jogada)
board

#oponente jogando
move = input("Jogada: ")
board.push_san(move)
display(board)

print("")

#minha IA jogando:
jogada = obterJogadasPossiveis()
board.push(jogada)
board

#oponente jogando
move = input("Jogada: ")
board.push_san(move)
display(board)

print("")

#minha IA jogando:
jogada = obterJogadasPossiveis()
board.push(jogada)
board

#oponente jogando
move = input("Jogada: ")
board.push_san(move)
display(board)

print("")

#minha IA jogando:
jogada = obterJogadasPossiveis()
board.push(jogada)
board

#oponente jogando
move = input("Jogada: ")
board.push_san(move)
display(board)

print(""