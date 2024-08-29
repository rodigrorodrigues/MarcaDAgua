from tkinter import ttk
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color
import io
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as tb
from PIL import Image, ImageTk
import webbrowser

def add_watermark(input_pdf, output_pdf, watermark_text):
    try:
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=A4)
        can.setFillColor(Color(0, 0, 0, alpha=0.3))  # Black color with 30% opacity
        can.setFont("Helvetica", 50)
        can.saveState()
        can.translate(A4[0] / 2, A4[1] / 2)
        can.rotate(45)
        can.drawCentredString(0, 0, watermark_text)
        can.restoreState()
        can.save()

        packet.seek(0)
        watermark = PdfReader(packet)
        pdf_reader = PdfReader(open(input_pdf, "rb"))
        pdf_writer = PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page.merge_page(watermark.pages[0])
            pdf_writer.add_page(page)
        with open(output_pdf, "wb") as output_file:
            pdf_writer.write(output_file)
        return True
    except Exception as e:
        print(f"Erro ao adicionar marca d'água: {e}")
        return False

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path)
    
    if file_path:
        base_name = os.path.basename(file_path)
        output_name = f"MarcaDAgua_{base_name}" #Autocomplete output file name
        entry_output.delete(0, tk.END)
        entry_output.insert(0, output_name)

def start_watermark():
    input_pdf = entry_file.get()
    watermark_text = entry_watermark.get()
    output_pdf = entry_output.get()
    if add_watermark(input_pdf, output_pdf, watermark_text):
        messagebox.showinfo("Sucesso", "Marca d'água adicionada com sucesso!")
        output_dir = os.path.dirname(os.path.abspath(output_pdf))
        subprocess.Popen(f'explorer "{output_dir}"')
    else:
        messagebox.showerror("Erro", "Falha ao adicionar marca d'água.")

def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(foreground='grey')
    entry.bind("<FocusIn>", lambda event: on_focus_in(event, placeholder))
    entry.bind("<FocusOut>", lambda event: on_focus_out(event, placeholder))

def on_focus_in(event, placeholder):
    if event.widget.get() == placeholder:
        event.widget.delete(0, tk.END)
        event.widget.config(foreground='black')

def on_focus_out(event, placeholder):
    if event.widget.get() == "":
        event.widget.insert(0, placeholder)
        event.widget.config(foreground='grey')


root = tb.Window(themename="flatly")
root.title("Adicionar Marca d'Água em PDF")
root.geometry("770x420") 
root.configure(bg='white')
root.resizable(True, True)

frame = ttk.Frame(root, padding="10 10 10 10", style="White.TFrame")
frame.place(relwidth=1, relheight=1)
style = ttk.Style(root)
style.configure("White.TFrame", background="white")

# Header
header = ttk.Label(frame, text="Adicionar Marca d'Água em PDF", font=("Helvetica", 16, "bold"), background="white")
header.grid(row=1, column=0, columnspan=3, pady=10)

ttk.Label(frame, text="Arquivo PDF:", font=("Helvetica", 10), background="white", anchor="e").grid(row=2, column=0, padx=(5, 2), pady=10, sticky=tk.E)
entry_file = ttk.Entry(frame, width=50)
entry_file.grid(row=2, column=1, padx=(2, 5), pady=10)
add_placeholder(entry_file, "Caminho para o arquivo PDF")
ttk.Button(frame, text="Selecionar", command=select_file).grid(row=2, column=2, padx=2, pady=2)

ttk.Label(frame, text="Texto da Marca d'Água:", font=("Helvetica", 10), background="white", anchor="e").grid(row=3, column=0, padx=(5, 2), pady=10, sticky=tk.E)
entry_watermark = ttk.Entry(frame, width=50)
entry_watermark.grid(row=3, column=1, padx=(2, 5), pady=10)
add_placeholder(entry_watermark, "Insira seu texto")

ttk.Label(frame, text="Nome do Arquivo de Saída:", font=("Helvetica", 10), background="white", anchor="e").grid(row=4, column=0, padx=(5, 2), pady=10, sticky=tk.E)
entry_output = ttk.Entry(frame, width=50)
entry_output.grid(row=4, column=1, padx=(2, 5), pady=10)
add_placeholder(entry_output, "Nome do arquivo de saída")


ttk.Button(frame, text="Adicionar Marca d'Água", command=start_watermark).grid(row=5, column=0, columnspan=3, pady=20)

def open_link(event):
    webbrowser.open_new("https://github.com/rodigrorodrigues/MarcaDAguaPDF")

# Footer
ttk.Label(frame, text="Rodrigo Rodrigues", font=("Helvetica", 10), background="white").grid(row=6, column=0, columnspan=3, pady=(10, 2))

link_label = ttk.Label(frame, text="https://github.com/rodigrorodrigues/MarcaDAguaPDF", font=("Helvetica", 10), background="white", foreground="blue", cursor="hand2")
link_label.grid(row=7, column=0, columnspan=3, pady=(2, 10))
link_label.bind("<Button-1>", open_link)

root.mainloop()