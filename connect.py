import socket
import threading

class TicTacToe:
    
    def __init__(self):
        self.board = [ [" "," "," "], [" "," "," "], [" "," "," "] ]  
        self.turn = "X"
        self.you = "X"
        self.opponent = "O"
        self.winner = None
        self.game_over = False
        self.counter = 0

    # Function host_game() hosts the game using a TCP connection at the specified host and port
    
    def host_game(self,host,port):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((host,port))
        server.listen(1)
        client,addr = server.accept()
        self.you = "X"
        self.opponent = "O"
        threading.Thread(target = self.handle_connection,args =(client,)).start()
        server.close()
        
    # Connects to the game
    
    def connect_to_game(self,host,port):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((host,port))
        self.you = "O"    
        self.opponent = "X"
        threading.Thread(target = self.handle_connection,args =(client,)).start()
        
    # Game logic. Takes in move and switches between two players untill game_over is true
    
    def handle_connection(self,client):
        while not self.game_over:
            if self.turn == self.you:
                move = input("Enter a move in the format (row,column): ")
                if(self.check_valid_move(move.split(','))):
                    self.apply_move(move.split(','),self.you)
                    self.turn  = self.opponent
                    client.send(move.encode('utf-8'))     
                else:
                    print("Invalid move!")
            else:
                data = client.recv(1024)
                if not data:
                    break
                else:
                    self.apply_move(data.decode('utf-8').split(','),self.opponent)
                    self.turn = self.you
        client.close()
        
    # Game logic. Counter variable is used to check for a tie
    # Checks for winner or tie and prints it
    
    def apply_move(self,move,player):
        if self.game_over:
            return
        self.counter += 1
        self.board[int(move[0])][int(move[1])] = player
        self.print_board()
        if self.check_if_won():
            if self.winner == self.you:
                print("You win")
                exit()
            elif self.winner == self.opponent:
                print("You lose")
                exit()
        else:
            if self.counter == 9:
                print("Tie")                                            
                exit()
                
    # Checks if the move is valid. The first condition checks for out-of-bounds error and second checks
    # if we are attempting to make a move on already played cell.
    
    def check_valid_move(self,move):
        if (int(move[0]) > 2 or int(move[1]) > 2) or self.board[int(move[0])][int(move[1])] != " ":
            return False
        return True    

    #Checking for winner
    
    def check_if_won(self):
        # Checking for all row matches
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                self.winner = self.board[row][0]
                self.game_over = True
                return True
        # Checking column matches        
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                self.winner = self.board[0][col]
                self.game_over = True
                return True
        # Two if conditions check both diagonals        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.winner =  self.board[0][0]
            self.game_over = True
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self.winner =  self.board[0][2]
            self.game_over = True
            return True
        return False

    # Dislplay the board    
    def print_board(self):
        for row in range(3):
            print(" | ".join(self.board[row]))
            if row != 2:
                print("---------")   
# Run the game!                    
game = TicTacToe()
game.connect_to_game('localhost',3000)
