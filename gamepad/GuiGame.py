
import tkinter

#Import the games
import GuiRockPaperScissors
import GuiHangMan
import GuiPokerDice
import GuiMineSweeper

#create the top level tkinter widget, i.e. the main window
root = tkinter.Tk()

#customize title & size
root.title ("Game Pad")
mainframe = tkinter.Frame(root, height = 200, width = 500)

#pack and grid a geometry managers. here we use pack to embed the object into the root
mainframe.pack_propagate(0)
mainframe.pack(padx = 5, pady = 5)

#pack a label to the top of the main frame
intro = tkinter.Label(mainframe, text = "Select a game")
#intro.pack(side = "top")
intro.pack(pady = 20)

#pack a button for rockpaperscissors
rps_button = tkinter.Button(mainframe, text = "Rock, Paper,Scissors", command = GuiRockPaperScissors.gui)
rps_button.pack(fill = tkinter.constants.X)

#pack a button for hangman
hm_button = tkinter.Button(mainframe, text = "Hang Man", command = GuiHangMan.gui)
hm_button.pack(fill = tkinter.constants.X)

#pack a button for pokerdice
pd_button = tkinter.Button(mainframe, text = "Poker Dice", command = GuiPokerDice.gui)
pd_button.pack(fill = tkinter.constants.X)

#pack a button for mine sweeper
pd_button = tkinter.Button(mainframe, text = "Mine Sweeper", command = GuiMineSweeper.gui)
pd_button.pack(fill = tkinter.constants.X)

#pack the exit button
exit_button = tkinter.Button(mainframe, text = "Exit", command = root.destroy)
exit_button.pack(side = "bottom")

root.mainloop()

