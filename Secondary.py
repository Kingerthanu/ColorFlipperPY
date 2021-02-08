import pygame
import tkinter as tk
import time
InputWindow = tk.Tk()
InputWindow.geometry("250x250")
InputWindow.title("Input Value")
InputWindow.iconbitmap(False, "SecondaryIco.ico")
pygame.init()
SCREEN = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Color Flipper")
pygame.display.set_icon(pygame.image.load("Stock.jpg"))
SquareChart = [pygame.Rect(0, 0, 300, 300), pygame.Rect(300, 0, 300, 300), pygame.Rect(600, 0, 300, 300),
               pygame.Rect(0, 300, 300, 300), pygame.Rect(
                   300, 300, 300, 300), pygame.Rect(600, 300, 300, 300),
               pygame.Rect(0, 600, 300, 300), pygame.Rect(
                   300, 600, 300, 300), pygame.Rect(600, 600, 300, 300)

               ]


def DrawChart(r, g, b):
    for each in SquareChart:
        cR, cG, cB = 0, 0, 0
        while True:
            if cR != r or cG != g or cB != b:
                pygame.draw.rect(SCREEN, pygame.Color(
                    cR, cG, cB), each)
            else:
                break
            if cR != r:
                cR += 1
            elif cG != g:
                cG += 1
            elif cB != b:
                cB += 1
            pygame.display.flip()


while True:
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            pygame.quit()
        if Event.type == pygame.KEYDOWN and Event.key == pygame.K_UP:
            R = tk.Entry(InputWindow)
            Rl = tk.Label(InputWindow, text="Red: ")
            G = tk.Entry(InputWindow)
            Gl = tk.Label(InputWindow, text="Green: ")
            B = tk.Entry(InputWindow)
            Bl = tk.Label(InputWindow, text="Blue: ")
            ConfirmBut = tk.Button(
                InputWindow, text="Confirm", command=lambda: [DrawChart(int(R.get()), int(G.get()), int(B.get())), InputWindow.destroy()]).pack()
            R.pack()
            R.focus()
            G.pack()
            B.pack()
            Rl.place(x=5, y=23)
            Gl.place(x=5, y=46)
            Bl.place(x=5, y=69)
            InputWindow.mainloop()
            print("Reached")
            InputWindow = tk.Tk()
            InputWindow.geometry("250x250")
            InputWindow.title("Input Value")
    pygame.display.flip()
