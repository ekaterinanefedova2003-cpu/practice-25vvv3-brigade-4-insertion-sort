import tkinter as tk
from tkinter import filedialog, messagebox
import time

# ------------------ СОРТИРОВКА ------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# ------------------ ГЛОБАЛЬНЫЕ ДАННЫЕ ------------------
numbers = []
input_mode = None  # "manual" или "file"

# ------------------ ВЫБОР РЕЖИМА ------------------
def choose_manual():
    global input_mode
    input_mode = "manual"

    text_box.config(state="normal")
    text_box.delete("1.0", tk.END)

    status_label.config(text="Режим: ввод вручную")

def choose_file():
    global input_mode, numbers

    input_mode = "file"

    filename = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=[("Текстовые файлы", "*.txt")]
    )

    if filename:
        try:
            with open(filename, "r") as f:
                numbers = list(map(int, f.read().split()))

            text_box.config(state="normal")
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, " ".join(map(str, numbers)))
            text_box.config(state="disabled")

            status_label.config(text=f"Режим: файл ({filename.split('/')[-1]})")

        except:
            messagebox.showerror("Ошибка", "Не удалось открыть файл.")

# ------------------ СОРТИРОВКА + ЗАМЕР ВРЕМЕНИ ------------------
def sort_numbers():
    global numbers

    try:
        if input_mode == "manual":
            text = text_box.get("1.0", tk.END).strip()
            numbers = list(map(int, text.split()))

        if not numbers:
            messagebox.showwarning("Внимание", "Нет данных для сортировки.")
            return

        start = time.perf_counter()
        insertion_sort(numbers)
        end = time.perf_counter()

        # вывод результата
        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, " ".join(map(str, numbers)))
        result_box.config(state="disabled")

        timer_label.config(
            text=f"Время выполнения: {end - start:.8f} сек."
        )

    except ValueError:
        messagebox.showerror("Ошибка", "Введите только целые числа.")

# ------------------ СОХРАНЕНИЕ ------------------
def save_result():
    if not numbers:
        messagebox.showwarning("Внимание", "Нет результата для сохранения.")
        return

    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Текстовые файлы", "*.txt")]
    )

    if filename:
        with open(filename, "w") as f:
            f.write(" ".join(map(str, numbers)))

        messagebox.showinfo("Готово", "Файл сохранён.")

# ------------------ GUI ------------------
window = tk.Tk()
window.title("Сортировка вставками")
window.geometry("700x600")
window.resizable(False, False)

# Заголовок
tk.Label(window, text="СОРТИРОВКА ВСТАВКАМИ",
         font=("Arial", 14, "bold")).pack(pady=10)

# Выбор режима
frame_mode = tk.Frame(window)
frame_mode.pack(pady=5)

tk.Button(frame_mode, text="Ввести вручную",
          width=20, command=choose_manual).pack(side="left", padx=10)

tk.Button(frame_mode, text="Загрузить из файла",
          width=20, command=choose_file).pack(side="left", padx=10)

status_label = tk.Label(window, text="Режим: не выбран")
status_label.pack(pady=5)

# Ввод
tk.Label(window, text="Введите числа через пробел:").pack()

text_box = tk.Text(window, height=5, width=70)
text_box.pack()

# Кнопка сортировки
tk.Button(window, text="Сортировать",
          width=25, command=sort_numbers).pack(pady=10)

# Результат
tk.Label(window, text="Отсортированный массив:").pack()

result_box = tk.Text(window, height=5, width=70)
result_box.pack()
result_box.config(state="disabled")

# Время
timer_label = tk.Label(window, text="")
timer_label.pack(pady=10)

#


Сохранение
tk.Button(window, text="Сохранить результат",
          width=25, command=save_result).pack(pady=5)

# Выход
tk.Button(window, text="Выход",

width=25, command=window.destroy).pack(pady=10)

window.mainloop()
