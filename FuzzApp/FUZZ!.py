from fuzzywuzzy import process
import Levenshtein
import Tkinter as tk
import tkFont
import os



def fuzz_match(s):
    w_list = []
    with open("words.txt") as w:
        for word in w:
            w_list.append(word.strip())
    fuzz_result = process.extractOne(s.lower(), w_list)
    return fuzz_result


# Gradient Frame Code from link below
# https://stackoverflow.com/questions/11892521/tkinter-custom-window
class GradientFrame(tk.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, borderwidth=1, relief="sunken"):
        tk.Canvas.__init__(self, parent, borderwidth=borderwidth,
                           relief=relief)
        self._color1 = "maroon"
        self._color2 = "gold"
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.create_line(i, 0, i, height, tags=("gradient"), fill=color)
        self.lower("gradient")


class FuzzApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('MSBA Spelling Bee (sponsored by FuzzyWuzzy)')
        helv48 = tkFont.Font(family='Helvetica', size=48, weight='bold')
        helv24 = tkFont.Font(family='Helvetica', size=24, weight='bold')
        gradient_frame = GradientFrame(self)
        gradient_frame.pack(side="top", fill="both", expand=True)
        inner_frame = tk.Frame(gradient_frame)
        inner_frame.pack(side="top", fill="both", expand=True,
                         padx=50, pady=50)
        bottom_frame = tk.Frame(inner_frame)
        bottom_frame.pack(side="bottom")

        button1 = tk.Button(bottom_frame, text="Close", font=helv24, width=10,
                            command=self.destroy)
        button1.pack(side="right")
        user_input = tk.Entry(inner_frame, font=helv48, width=60,
                              justify='center')
        user_input.pack(side="top")
        user_input.focus_set()
        fuzz_result = tk.Text(inner_frame, font=helv48)
        fuzz_result.configure(state="disable")
        fuzz_result.pack(side="bottom")

        def fuzzy():
            fuzz_result.configure(state="normal")
            s = user_input.get()
            fuzz_result.insert(tk.END, "The correct spelling is: " +
                               fuzz_match(s)[0] + "\n" + "Your score is: " +
                               str(fuzz_match(s)[1]) + "\n")
            fuzz_result.configure(state="disable")

        def clear():
            user_input.delete(0, tk.END)

        button3 = tk.Button(bottom_frame, text="Clear", font=helv24, width=10,
                            command=clear)
        button3.pack(side="left")
        button2 = tk.Button(bottom_frame, text="Fuzz!", font=helv24, width=10,
                            bg="green", fg="black", command=fuzzy)
        button2.pack(side="left")

if __name__ == "__main__":
    app = FuzzApp()
    app.mainloop()
