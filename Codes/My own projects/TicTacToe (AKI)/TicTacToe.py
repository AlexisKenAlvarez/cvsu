import tkinter as tk

# LIGHT VER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def lightver():
    root = tk. Tk()
    root.title("Tic Tac Toe")
    root.resizable(width=True, height=True)
    root.geometry("800x750")
    root.configure(bg="#FFFFFF")

    def restart():
        root.destroy()
        lightver()

    def exitgame():
        root.destroy()

    def mainmenu():
        root.destroy()
        menu()

    tturns = tk.BooleanVar()
    tturns.set(True)

    # ANSWERS VAR
    box_123 = tk.IntVar()
    box_123.set(0)

    box_456 = tk.IntVar()
    box_456.set(0)

    box_789 = tk.IntVar()
    box_789.set(0)

    box_147 = tk.IntVar()
    box_147.set(0)

    box_258 = tk.IntVar()
    box_258.set(0)

    box_369 = tk.IntVar()
    box_369.set(0)

    box_159 = tk.IntVar()
    box_159.set(0)

    box_357 = tk.IntVar()
    box_357.set(0)

    box_TIE = tk.IntVar()
    box_TIE.set(0)

    # BOX WIN
    def box_123_win():
        box_1.configure(bg="#33CC00", fg="white")
        box_2.configure(bg="#33CC00", fg="white")
        box_3.configure(bg="#33CC00", fg="white")

    def box_456_win():
        box_4.configure(bg="#33CC00", fg="white")
        box_5.configure(bg="#33CC00", fg="white")
        box_6.configure(bg="#33CC00", fg="white")

    def box_789_win():
        box_7.configure(bg="#33CC00", fg="white")
        box_8.configure(bg="#33CC00", fg="white")
        box_9.configure(bg="#33CC00", fg="white")

    def box_147_win():
        box_1.configure(bg="#33CC00", fg="white")
        box_4.configure(bg="#33CC00", fg="white")
        box_7.configure(bg="#33CC00", fg="white")

    def box_258_win():
        box_2.configure(bg="#33CC00", fg="white")
        box_5.configure(bg="#33CC00", fg="white")
        box_8.configure(bg="#33CC00", fg="white")

    def box_369_win():
        box_3.configure(bg="#33CC00", fg="white")
        box_6.configure(bg="#33CC00", fg="white")
        box_9.configure(bg="#33CC00", fg="white")

    def box_159_win():
        box_1.configure(bg="#33CC00", fg="white")
        box_5.configure(bg="#33CC00", fg="white")
        box_9.configure(bg="#33CC00", fg="white")

    def box_357_win():
        box_3.configure(bg="#33CC00", fg="white")
        box_5.configure(bg="#33CC00", fg="white")
        box_7.configure(bg="#33CC00", fg="white")

    def box_tie():
        box_1.configure(bg="red", fg="white")
        box_2.configure(bg="red", fg="white")
        box_3.configure(bg="red", fg="white")
        box_4.configure(bg="red", fg="white")
        box_5.configure(bg="red", fg="white")
        box_6.configure(bg="red", fg="white")
        box_7.configure(bg="red", fg="white")
        box_8.configure(bg="red", fg="white")
        box_9.configure(bg="red", fg="white")

    def null():
        pass

    # X OR O OUTPUT WINNER
    def newX():
        tk.Label(root, text="Congratulations, Player X wins!🎉", font=("Arial", 15, "bold")).place(relx=1, x=-565, y=230)
        tk.Button(root, text="AGAIN?", font=("Arial", 15, "bold"), command=restart).place(relx=1, x=-445, y=550)
        box_1.configure(command=null)
        box_2.configure(command=null)
        box_3.configure(command=null)
        box_4.configure(command=null)
        box_5.configure(command=null)
        box_6.configure(command=null)
        box_7.configure(command=null)
        box_8.configure(command=null)
        box_9.configure(command=null)

    def newO():
        tk.Label(root, text="Congratulations, Player O wins!🎉", font=("Arial", 15, "bold")).place(relx=1, x=-565, y=230)
        tk.Button(root, text="AGAIN?", font=("Arial", 15, "bold"), command=restart).place(relx=1, x=-445, y=550)
        box_1.configure(command=null)
        box_2.configure(command=null)
        box_3.configure(command=null)
        box_4.configure(command=null)
        box_5.configure(command=null)
        box_6.configure(command=null)
        box_7.configure(command=null)
        box_8.configure(command=null)
        box_9.configure(command=null)

    def TIED():
        tk.Label(root, text="TIE!", font=("Arial", 15, "bold"), width=50).place(relx=1, x=-702, y=240)
        tk.Button(root, text="AGAIN?", font=("Arial", 15, "bold"), command=restart).place(relx=1, x=-445, y=550)
        box_1.configure(command=null)
        box_2.configure(command=null)
        box_3.configure(command=null)
        box_4.configure(command=null)
        box_5.configure(command=null)
        box_6.configure(command=null)
        box_7.configure(command=null)
        box_8.configure(command=null)
        box_9.configure(command=null)

    # TIC X
    def TICX1():
        if tturns.get() == True:
            box_1.configure(text="X", font=("Arial", 30, "bold"), fg="black", padx=14, pady=2, command=null)
            tturns.set(False)
            box_123.set(box_123.get() + 1)
            box_147.set(box_147.get() + 1)
            box_159.set(box_159.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_123.get() >= 3:
                newX()
                box_123_win()
            elif box_147.get() >= 3:
                newX()
                box_147_win()
            elif box_159.get() >= 3:
                newX()
                box_159_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_1.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_123.set(box_123.get() - 1)
            box_147.set(box_147.get() - 1)
            box_159.set(box_159.get() - 1)
            if box_123.get() <= -3:
                newO()
                box_123_win()
            elif box_147.get() <= -3:
                newO()
                box_147_win()
            elif box_159.get() <= -3:
                newO()
                box_159_win()

    def TICX2():
        if tturns.get() == True:
            box_2.configure(text="X", font=("Arial", 30, "bold"), fg="black", padx=14, pady=2, command=null)
            tturns.set(False)
            box_123.set(box_123.get() + 1)
            box_258.set(box_258.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_123.get() >= 3:
                newX()
                box_123_win()
            elif box_258.get() >= 3:
                newX()
                box_258_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_2.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_123.set(box_123.get() - 1)
            box_258.set(box_258.get() - 1)
            if box_123.get() <= -3:
                newO()
                box_123_win()
            elif box_258.get() <= -3:
                newO()
                box_258_win()

    def TICX3():
        if tturns.get() == True:
            box_3.configure(text="X", font=("Arial", 30, "bold"), fg="black", padx=14, pady=2, command=null)
            tturns.set(False)
            box_123.set(box_123.get() + 1)
            box_369.set(box_369.get() + 1)
            box_357.set(box_357.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_123.get() >= 3:
                newX()
                box_123_win()
            elif box_369.get() >= 3:
                newX()
                box_369_win()
            elif box_357.get() >= 3:
                newX()
                box_357_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_3.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_123.set(box_123.get() - 1)
            box_369.set(box_369.get() - 1)
            box_357.set(box_357.get() - 1)
            if box_123.get() <= -3:
                newO()
                box_123_win()
            elif box_369.get() <= -3:
                newO()
                box_369_win()
            elif box_357.get() <= -3:
                newO()
                box_357_win()

    def TICX4():
        if tturns.get() == True:
            box_4.configure(text="X", font=("Arial", 30, "bold"), fg="black", padx=14, pady=2, command=null)
            tturns.set(False)
            box_456.set(box_456.get() + 1)
            box_147.set(box_147.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_456.get() >= 3:
                newX()
                box_456_win()
            elif box_147.get() >= 3:
                newX()
                box_147_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_4.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_456.set(box_456.get() - 1)
            box_147.set(box_147.get() - 1)
            if box_456.get() <= -3:
                newO()
                box_456_win()
            elif box_147.get() <= -3:
                newO()
                box_147_win()

    def TICX5():
        if tturns.get() == True:
            box_5.configure(text="X", font=("Arial", 30, "bold"), fg="black", padx=14, pady=2, command=null)
            tturns.set(False)
            box_456.set(box_456.get() + 1)
            box_258.set(box_258.get() + 1)
            box_159.set(box_159.get() + 1)
            box_357.set(box_357.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_456.get() >= 3:
                newX()
                box_456_win()
            elif box_258.get() >= 3:
                newX()
                box_258_win()
            elif box_159.get() >= 3:
                newX()
                box_159_win()
            elif box_357.get() >= 3:
                newX()
                box_357_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_5.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_456.set(box_456.get() - 1)
            box_258.set(box_258.get() - 1)
            box_159.set(box_159.get() - 1)
            box_357.set(box_357.get() - 1)
            if box_456.get() <= -3:
                newO()
                box_456_win()
            elif box_258.get() <= -3:
                newO()
                box_258_win()
            elif box_159.get() <= -3:
                newO()
                box_159_win()
            elif box_357.get() <= -3:
                newO()
                box_357_win()

    def TICX6():
        if tturns.get() == True:
            box_6.configure(text="X", font=("Arial", 30, "bold"), fg="black", padx=14, pady=2, command=null)
            tturns.set(False)
            box_456.set(box_456.get() + 1)
            box_369.set(box_369.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_456.get() >= 3:
                newX()
                box_456_win()
            elif box_369.get() >= 3:
                newX()
                box_369_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_6.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_456.set(box_456.get() - 1)
            box_369.set(box_369.get() - 1)
            if box_456.get() <= -3:
                newO()
                box_456_win()
            elif box_369.get() <= -3:
                newO()
                box_369_win()
            

    def TICX7():
        if tturns.get() == True:
            box_7.configure(text="X", font=("Arial", 30, "bold"), fg="black", padx=14, pady=2, command=null)
            tturns.set(False)
            box_789.set(box_789.get() + 1)
            box_147.set(box_147.get() + 1)
            box_357.set(box_357.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_789.get() >= 3:
                newX()
                box_789_win()
            elif box_147.get() >= 3:
                newX()
                box_147_win()
            elif box_357.get() >= 3:
                newX()
                box_357_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_7.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_789.set(box_789.get() - 1)
            box_147.set(box_147.get() - 1)
            box_357.set(box_357.get() - 1)
            if box_789.get() <= -3:
                newO()
                box_789_win()
            elif box_147.get() <= -3:
                newO()
                box_147_win()
            elif box_357.get() <= -3:
                newO()
                box_357_win()
                

    def TICX8():
        if tturns.get() == True:
            box_8.configure(text="X", font=("Arial", 30, "bold"), fg="black", padx=14, pady=2, command=null)
            tturns.set(False)
            box_789.set(box_789.get() + 1)
            box_258.set(box_258.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_789.get() >= 3:
                newX()
                box_789_win()
            elif box_258.get() >= 3:
                newX()
                box_258_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_8.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_789.set(box_789.get() - 1)
            box_258.set(box_258.get() - 1)
            if box_789.get() <= -3:
                newO()
                box_789_win()
            elif box_258.get() <= -3:
                newO()
                box_258_win()

    def TICX9():
        if tturns.get() == True:
            box_9.configure(text="X", font=("Arial", 30, "bold"), fg="black", padx=14, pady=2, command=null)
            tturns.set(False)
            box_789.set(box_789.get() + 1)
            box_369.set(box_369.get() + 1)
            box_159.set(box_159.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_789.get() >= 3:
                newX()
                box_789_win()
            elif box_369.get() >= 3:
                newX()
                box_369_win()
            elif box_159.get() >= 3:
                newX()
                box_159_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_9.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_789.set(box_789.get() - 1)
            box_369.set(box_369.get() - 1)
            box_159.set(box_159.get() - 1)
            if box_789.get() <= -3:
                newO()
                box_789_win()
            elif box_369.get() <= -3:
                newO()
                box_369_win()
            elif box_159.get() <= -3:
                newO()
                box_159_win()

    LabelIntro = tk.LabelFrame(root, padx=200, pady=1)
    LabelIntro.place(relx=1, rely=0, x=-400, y=80, anchor=tk.CENTER)

    frame = tk.LabelFrame(root, text="2 Player",padx=160, pady=100, bd=5, bg="#CCCCCC")
    frame.place(relx=1, rely=0, x=-400, y=400, anchor=tk.CENTER)

    myIntro = tk.Label(LabelIntro, text="TIC TAC TOE", font=("Arial Black", 23, "bold"))
    myIntro.grid(row=0, column=0, columnspan=3, rowspan=1, pady=5)

    myIntro2 = tk.Label(LabelIntro, text="by Alexis Ken Alvarez", font=("Arial Black", 8, "bold", "italic"))
    myIntro2.grid(row=1, column=0, columnspan=3, rowspan=1, pady=5)

    exitButton = tk.Button(root, text="EXIT", font=("Arial", 15, "bold"), command=exitgame)
    exitButton.place(relx=1, x=-430, y=695)

    returnButton = tk.Button(root, text="RETURN", font=("Arial", 15, "bold"), command=mainmenu, padx=10)
    returnButton.place(relx=1, x=-458, y=645)

    box_1 = tk.Button(frame, padx=40, pady=30, command=TICX1)
    box_2 = tk.Button(frame, padx=40, pady=30, command=TICX2)
    box_3 = tk.Button(frame, padx=40, pady=30, command=TICX3)

    box_4 = tk.Button(frame, padx=40, pady=30, command=TICX4)
    box_5 = tk.Button(frame, padx=40, pady=30, command=TICX5)
    box_6 = tk.Button(frame, padx=40, pady=30, command=TICX6)

    box_7 = tk.Button(frame, padx=40, pady=30, command=TICX7)
    box_8 = tk.Button(frame, padx=40, pady=30, command=TICX8)
    box_9 = tk.Button(frame, padx=40, pady=30, command=TICX9)

    box_1.grid(row=1, column=0)
    box_2.grid(row=1, column=1)
    box_3.grid(row=1, column=2)

    box_4.grid(row=2, column=0)
    box_5.grid(row=2, column=1)
    box_6.grid(row=2, column=2)

    box_7.grid(row=3, column=0)
    box_8.grid(row=3, column=1)
    box_9.grid(row=3, column=2)

    root.mainloop()

# DARK VERSION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def darkver():
    root = tk. Tk()
    root.title("Tic Tac Toe")
    root.resizable(width=True, height=True)
    root.geometry("800x750")
    root.configure(bg="#666666")

    def restart():
        root.destroy()
        darkver()

    def exitgame():
        root.destroy()

    def mainmenu():
        root.destroy()
        menu()

    tturns = tk.BooleanVar()
    tturns.set(True)

    # PROBABLE WINNING BOX VAR
    box_123 = tk.IntVar()
    box_123.set(0)

    box_456 = tk.IntVar()
    box_456.set(0)

    box_789 = tk.IntVar()
    box_789.set(0)

    box_147 = tk.IntVar()
    box_147.set(0)

    box_258 = tk.IntVar()
    box_258.set(0)

    box_369 = tk.IntVar()
    box_369.set(0)

    box_159 = tk.IntVar()
    box_159.set(0)

    box_357 = tk.IntVar()
    box_357.set(0)

    box_TIE = tk.IntVar()
    box_TIE.set(0)

    # BOX WIN
    def box_123_win():
        box_1.configure(bg="#33CC00", fg="#003300")
        box_2.configure(bg="#33CC00", fg="#003300")
        box_3.configure(bg="#33CC00", fg="#003300")

    def box_456_win():
        box_4.configure(bg="#33CC00", fg="#003300")
        box_5.configure(bg="#33CC00", fg="#003300")
        box_6.configure(bg="#33CC00", fg="#003300")

    def box_789_win():
        box_7.configure(bg="#33CC00", fg="#003300")
        box_8.configure(bg="#33CC00", fg="#003300")
        box_9.configure(bg="#33CC00", fg="#003300")

    def box_147_win():
        box_1.configure(bg="#33CC00", fg="#003300")
        box_4.configure(bg="#33CC00", fg="#003300")
        box_7.configure(bg="#33CC00", fg="#003300")

    def box_258_win():
        box_2.configure(bg="#33CC00", fg="#003300")
        box_5.configure(bg="#33CC00", fg="#003300")
        box_8.configure(bg="#33CC00", fg="#003300")

    def box_369_win():
        box_3.configure(bg="#33CC00", fg="#003300")
        box_6.configure(bg="#33CC00", fg="#003300")
        box_9.configure(bg="#33CC00", fg="#003300")

    def box_159_win():
        box_1.configure(bg="#33CC00", fg="#003300")
        box_5.configure(bg="#33CC00", fg="#003300")
        box_9.configure(bg="#33CC00", fg="#003300")

    def box_357_win():
        box_3.configure(bg="#33CC00", fg="#003300")
        box_5.configure(bg="#33CC00", fg="#003300")
        box_7.configure(bg="#33CC00", fg="#003300")

    def box_tie():
        box_1.configure(bg="red", fg="white")
        box_2.configure(bg="red", fg="white")
        box_3.configure(bg="red", fg="white")
        box_4.configure(bg="red", fg="white")
        box_5.configure(bg="red", fg="white")
        box_6.configure(bg="red", fg="white")
        box_7.configure(bg="red", fg="white")
        box_8.configure(bg="red", fg="white")
        box_9.configure(bg="red", fg="white")

    def null():
        pass

    # X OR O OUTPUT WINNER
    def newX():
        tk.Label(root, text="Congratulations, Player X wins!🎉", font=("Arial", 15, "bold")).place(relx=1, x=-565, y=230)
        tk.Button(root, text="AGAIN?", font=("Arial", 15, "bold"), command=restart, bg="#333333", fg="white").place(relx=1, x=-445, y=550)
        box_1.configure(command=null)
        box_2.configure(command=null)
        box_3.configure(command=null)
        box_4.configure(command=null)
        box_5.configure(command=null)
        box_6.configure(command=null)
        box_7.configure(command=null)
        box_8.configure(command=null)
        box_9.configure(command=null)
        
    def newO():
        tk.Label(root, text="Congratulations, Player O wins!🎉", font=("Arial", 15, "bold")).place(relx=1, x=-565, y=230)
        tk.Button(root, text="AGAIN?", font=("Arial", 15, "bold"), command=restart, bg="#333333", fg="white").place(relx=1, x=-445, y=550)
        box_1.configure(command=null)
        box_2.configure(command=null)
        box_3.configure(command=null)
        box_4.configure(command=null)
        box_5.configure(command=null)
        box_6.configure(command=null)
        box_7.configure(command=null)
        box_8.configure(command=null)
        box_9.configure(command=null)

    def TIED():
        tk.Label(root, text="TIE!", font=("Arial", 15, "bold"), width=50).place(relx=1, x=-702, y=240)
        tk.Button(root, text="AGAIN?", font=("Arial", 15, "bold"), command=restart, bg="#333333", fg="white").place(relx=1, x=-445, y=550)
        box_1.configure(command=null)
        box_2.configure(command=null)
        box_3.configure(command=null)
        box_4.configure(command=null)
        box_5.configure(command=null)
        box_6.configure(command=null)
        box_7.configure(command=null)
        box_8.configure(command=null)
        box_9.configure(command=null)

    # TIC X
    def TICX1():
        if tturns.get() == True:
            box_1.configure(text="X", font=("Arial", 30, "bold"), fg="white", padx=14, pady=2, command=null)
            tturns.set(False)
            box_123.set(box_123.get() + 1)
            box_147.set(box_147.get() + 1)
            box_159.set(box_159.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_123.get() >= 3:
                newX()
                box_123_win()
            elif box_147.get() >= 3:
                newX()
                box_147_win()
            elif box_159.get() >= 3:
                newX()
                box_159_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_1.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_123.set(box_123.get() - 1)
            box_147.set(box_147.get() - 1)
            box_159.set(box_159.get() - 1)
            if box_123.get() <= -3:
                newO()
                box_123_win()
            elif box_147.get() <= -3:
                newO()
                box_147_win()
            elif box_159.get() <= -3:
                newO()
                box_159_win()

    def TICX2():
        if tturns.get() == True:
            box_2.configure(text="X", font=("Arial", 30, "bold"), fg="white", padx=14, pady=2, command=null)
            tturns.set(False)
            box_123.set(box_123.get() + 1)
            box_258.set(box_258.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_123.get() >= 3:
                newX()
                box_123_win()
            elif box_258.get() >= 3:
                newX()
                box_258_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_2.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_123.set(box_123.get() - 1)
            box_258.set(box_258.get() - 1)
            if box_123.get() <= -3:
                newO()
                box_123_win()
            elif box_258.get() <= -3:
                newO()
                box_258_win()

    def TICX3():
        if tturns.get() == True:
            box_3.configure(text="X", font=("Arial", 30, "bold"), fg="white", padx=14, pady=2, command=null)
            tturns.set(False)
            box_123.set(box_123.get() + 1)
            box_369.set(box_369.get() + 1)
            box_357.set(box_357.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_123.get() >= 3:
                newX()
                box_123_win()
            elif box_369.get() >= 3:
                newX()
                box_369_win()
            elif box_357.get() >= 3:
                newX()
                box_357_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_3.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_123.set(box_123.get() - 1)
            box_369.set(box_369.get() - 1)
            box_357.set(box_357.get() - 1)
            if box_123.get() <= -3:
                newO()
                box_123_win()
            elif box_369.get() <= -3:
                newO()
                box_369_win()
            elif box_357.get() <= -3:
                newO()
                box_357_win()

    def TICX4():
        if tturns.get() == True:
            box_4.configure(text="X", font=("Arial", 30, "bold"), fg="white", padx=14, pady=2, command=null)
            tturns.set(False)
            box_456.set(box_456.get() + 1)
            box_147.set(box_147.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_456.get() >= 3:
                newX()
                box_456_win()
            elif box_147.get() >= 3:
                newX()
                box_147_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_4.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_456.set(box_456.get() - 1)
            box_147.set(box_147.get() - 1)
            if box_456.get() <= -3:
                newO()
                box_456_win()
            elif box_147.get() <= -3:
                newO()
                box_147_win()

    def TICX5():
        if tturns.get() == True:
            box_5.configure(text="X", font=("Arial", 30, "bold"), fg="white", padx=14, pady=2, command=null)
            tturns.set(False)
            box_456.set(box_456.get() + 1)
            box_258.set(box_258.get() + 1)
            box_159.set(box_159.get() + 1)
            box_357.set(box_357.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_456.get() >= 3:
                newX()
                box_456_win()
            elif box_258.get() >= 3:
                newX()
                box_258_win()
            elif box_159.get() >= 3:
                newX()
                box_159_win()
            elif box_357.get() >= 3:
                newX()
                box_357_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_5.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_456.set(box_456.get() - 1)
            box_258.set(box_258.get() - 1)
            box_159.set(box_159.get() - 1)
            box_357.set(box_357.get() - 1)
            if box_456.get() <= -3:
                newO()
                box_456_win()
            elif box_258.get() <= -3:
                newO()
                box_258_win()
            elif box_159.get() <= -3:
                newO()
                box_159_win()
            elif box_357.get() <= -3:
                newO()
                box_357_win()

    def TICX6():
        if tturns.get() == True:
            box_6.configure(text="X", font=("Arial", 30, "bold"), fg="white", padx=14, pady=2, command=null)
            tturns.set(False)
            box_456.set(box_456.get() + 1)
            box_369.set(box_369.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_456.get() >= 3:
                newX()
                box_456_win()
            elif box_369.get() >= 3:
                newX()
                box_369_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_6.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_456.set(box_456.get() - 1)
            box_369.set(box_369.get() - 1)
            if box_456.get() <= -3:
                newO()
                box_456_win()
            elif box_369.get() <= -3:
                newO()
                box_369_win()
            

    def TICX7():
        if tturns.get() == True:
            box_7.configure(text="X", font=("Arial", 30, "bold"), fg="white", padx=14, pady=2, command=null)
            tturns.set(False)
            box_789.set(box_789.get() + 1)
            box_147.set(box_147.get() + 1)
            box_357.set(box_357.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_789.get() >= 3:
                newX()
                box_789_win()
            elif box_147.get() >= 3:
                newX()
                box_147_win()
            elif box_357.get() >= 3:
                newX()
                box_357_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_7.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_789.set(box_789.get() - 1)
            box_147.set(box_147.get() - 1)
            box_357.set(box_357.get() - 1)
            if box_789.get() <= -3:
                newO()
                box_789_win()
            elif box_147.get() <= -3:
                newO()
                box_147_win()
            elif box_357.get() <= -3:
                newO()
                box_357_win()
                

    def TICX8():
        if tturns.get() == True:
            box_8.configure(text="X", font=("Arial", 30, "bold"), fg="white", padx=14, pady=2, command=null)
            tturns.set(False)
            box_789.set(box_789.get() + 1)
            box_258.set(box_258.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_789.get() >= 3:
                newX()
                box_789_win()
            elif box_258.get() >= 3:
                newX()
                box_258_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_8.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_789.set(box_789.get() - 1)
            box_258.set(box_258.get() - 1)
            if box_789.get() <= -3:
                newO()
                box_789_win()
            elif box_258.get() <= -3:
                newO()
                box_258_win()

    def TICX9():
        if tturns.get() == True:
            box_9.configure(text="X", font=("Arial", 30, "bold"), fg="white", padx=14, pady=2, command=null)
            tturns.set(False)
            box_789.set(box_789.get() + 1)
            box_369.set(box_369.get() + 1)
            box_159.set(box_159.get() + 1)
            box_TIE.set(box_TIE.get() + 1)
            if box_789.get() >= 3:
                newX()
                box_789_win()
            elif box_369.get() >= 3:
                newX()
                box_369_win()
            elif box_159.get() >= 3:
                newX()
                box_159_win()
            elif box_TIE.get() >= 5:
                TIED()
                box_tie()
        else:
            box_9.configure(text="O", font=("Arial", 30, "bold"), fg="#FF9900", padx=12, pady=2, command=null)
            tturns.set(True)
            box_789.set(box_789.get() - 1)
            box_369.set(box_369.get() - 1)
            box_159.set(box_159.get() - 1)
            if box_789.get() <= -3:
                newO()
                box_789_win()
            elif box_369.get() <= -3:
                newO()
                box_369_win()
            elif box_159.get() <= -3:
                newO()
                box_159_win()

    LabelIntro = tk.LabelFrame(root, padx=200, pady=1, bg="#333333")
    LabelIntro.place(relx=1, rely=0, x=-400, y=80, anchor=tk.CENTER)

    frame = tk.LabelFrame(root, text="2 Player",padx=160, pady=100, bd=5, bg="#333333", fg="white")
    frame.place(relx=1, rely=0, x=-400, y=400, anchor=tk.CENTER)

    myIntro = tk.Label(LabelIntro, text="TIC TAC TOE", font=("Arial Black", 23, "bold"), bg="#333333", fg="white")
    myIntro.grid(row=0, column=0, columnspan=3, rowspan=1, pady=5)

    myIntro2 = tk.Label(LabelIntro, text="by Alexis Ken Alvarez", font=("Arial Black", 8, "bold", "italic"), bg="#333333", fg="white")
    myIntro2.grid(row=1, column=0, columnspan=3, rowspan=1, pady=5)

    exitButton = tk.Button(root, text="EXIT", font=("Arial", 15, "bold"), command=exitgame, bg="#333333", fg="white")
    exitButton.place(relx=1, x=-430, y=695)

    returnButton = tk.Button(root, text="RETURN", font=("Arial", 15, "bold"), command=mainmenu, padx=10, bg="#333333", fg="white")
    returnButton.place(relx=1, x=-458, y=645)

    box_1 = tk.Button(frame, padx=40, pady=30, command=TICX1, bg="#666666")
    box_2 = tk.Button(frame, padx=40, pady=30, command=TICX2, bg="#666666")
    box_3 = tk.Button(frame, padx=40, pady=30, command=TICX3, bg="#666666")

    box_4 = tk.Button(frame, padx=40, pady=30, command=TICX4, bg="#666666")
    box_5 = tk.Button(frame, padx=40, pady=30, command=TICX5, bg="#666666")
    box_6 = tk.Button(frame, padx=40, pady=30, command=TICX6, bg="#666666")

    box_7 = tk.Button(frame, padx=40, pady=30, command=TICX7, bg="#666666")
    box_8 = tk.Button(frame, padx=40, pady=30, command=TICX8, bg="#666666")
    box_9 = tk.Button(frame, padx=40, pady=30, command=TICX9, bg="#666666")

    box_1.grid(row=1, column=0)
    box_2.grid(row=1, column=1)
    box_3.grid(row=1, column=2)

    box_4.grid(row=2, column=0)
    box_5.grid(row=2, column=1)
    box_6.grid(row=2, column=2)

    box_7.grid(row=3, column=0)
    box_8.grid(row=3, column=1)
    box_9.grid(row=3, column=2)

    root.mainloop()

# MAIN MENU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def menu():
    master = tk.Tk()
    master.title("Welcome!")
    master.geometry("550x400")
    master.resizable(width=False, height=False)
    master.configure(bg="#666666")

    def light_ver_cmd():
        master.destroy()
        lightver()

    def dark_ver_cmd():
        master.destroy()
        darkver()


    # Light theme
    def light():
        introTXT1.config(bg="#FFFFFF")
        introTXT1.tag_config("TICTAC", font=("Lemon", 28, "bold", "underline"), justify="center", foreground="#000000")
        introTXT1.tag_config("Welcometo", font=("Lemon", 28, "bold"), justify="center", foreground="#000000")
        introFrame2.configure(foreground="#000000", bg="#FFFFFF")
        startbutton.configure(bg="#FFFFFF", foreground="#000000")
        master.configure(bg="#333333")
        startbutton["command"] = light_ver_cmd
        themelight.configure(bg="#FFFFFF", foreground="#000000")
        themedark.configure(bg="#FFFFFF", foreground="#000000")

    # Dark theme
    def dark():
        introTXT1.config(bg="#333333")
        introTXT1.tag_config("Welcometo", font=("Lemon", 28, "bold"), justify="center", foreground="#FFFFFF")
        introTXT1.tag_config("TICTAC", font=("Lemon", 28, "bold", "underline"), justify="center", foreground="#FFFFFF")
        introTXT1.tag_config("TOE", font=("Lemon", 28, "bold", "underline"), justify="center", foreground="#FF9900")
        introFrame2.configure(foreground="#FFFFFF", bg="#333333")
        startbutton.configure(bg="#333333", foreground="#FFFFFF")
        master.configure(bg="#666666")
        startbutton["command"] = dark_ver_cmd
        themelight.configure(bg="#333333", foreground="#FFFFFF")
        themedark.configure(bg="#333333", foreground="#FFFFFF")

    introTXT1 = tk.Text(master, padx=30, pady=10, height=19, width=50, borderwidth=5, bg="#333333")

    introTXT1.insert(tk.INSERT, "Welcome to \nTICTACTOE")
    introTXT1.place(relx=1, x=-43, y=30, anchor=tk.NE)

    introTXT1.tag_add("Welcometo", 1.0, 1.11)
    introTXT1.tag_config("Welcometo", font=("Lemon", 28, "bold"), justify="center", foreground="#FFFFFF")

    introTXT1.tag_add("TICTAC", 2.0, 2.6)
    introTXT1.tag_config("TICTAC", font=("Lemon", 28, "bold", "underline"), justify="center", foreground="#FFFFFF")

    introTXT1.tag_add("TOE", 2.6, 2.9)
    introTXT1.tag_config("TOE", font=("Lemon", 28, "bold", "underline"), justify="center", foreground="#FF9900")

    introFrame2 = tk.Label(master, text="Press LAUNCH to start", font=("Agency FB", 22, "bold"), padx=10, pady=5, foreground="#FFFFFF", bd=2, bg="#333333")
    introFrame2.place(relx=1, x=-390, y=210)

    startbutton = tk.Button(master, text="LAUNCH", font=("Forte", 15, "bold"), padx=40, pady=5, command=dark_ver_cmd, borderwidth=5, bg="#333333", foreground="#FFFFFF")
    startbutton.place(relx=1, x=-368, y=280)

    themelight = tk.Button(master, text="LIGHT", font=("Forte", 15, "bold"), padx=10, pady=1, command=light, borderwidth=5, bg="#333333", foreground="#FFFFFF")
    themelight.place(relx=1, x=-168, y=282)

    themedark = tk.Button(master, text="DARK", font=("Forte", 15, "bold"), padx=10, pady=1, command=dark, borderwidth=5, bg="#333333", foreground="#FFFFFF")
    themedark.place(relx=1, x=-482, y=282)

    master.mainloop()

menu()