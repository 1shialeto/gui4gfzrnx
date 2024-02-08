import tkinter as tk
import subprocess
from tkinter import scrolledtext


def run_console_app():
    process = subprocess.Popen('gfzrnx_2.1.7_win64.exe -h', stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               shell=True)
    output, _ = process.communicate()
    output_text.insert(tk.END, output.decode('utf-8'))


app = tk.Tk()
app.title("Console App Runner")

run_button = tk.Button(app, text="Run Console App", command=run_console_app)
run_button.pack()

output_text = scrolledtext.ScrolledText(app, width=40, height=10)
output_text.pack()

app.mainloop()
