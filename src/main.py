"""Simple placeholder GUI for mapmakers demo."""

import os
import tkinter as tk
from tkinter import messagebox


TILESET_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tilesets", "sample_tileset.ppm")


def load_tileset(path=TILESET_PATH):
    """Load a tileset image."""
    if not os.path.exists(path):
        messagebox.showerror("Tileset", f"Tileset not found: {path}")
        return None
    try:
        image = tk.PhotoImage(file=path)
        return image
    except tk.TclError as exc:
        messagebox.showerror("Tileset", f"Failed to load tileset: {exc}")
        return None


def render_grid(canvas, grid_type="square", size=10, cell=32):
    """Render a simple square grid onto the canvas."""
    if grid_type not in {"square", "hex"}:
        raise ValueError("grid_type must be 'square' or 'hex'")

    for y in range(size):
        for x in range(size):
            x1 = x * cell
            y1 = y * cell
            x2 = x1 + cell
            y2 = y1 + cell
            canvas.create_rectangle(x1, y1, x2, y2, outline="gray")


def edit_tiles():
    """Launch a minimal GUI for editing tiles."""
    root = tk.Tk()
    root.title("Mapmakers Demo")
    canvas = tk.Canvas(root, width=320, height=320)
    canvas.pack()

    tileset = load_tileset()
    render_grid(canvas)

    root.mainloop()


if __name__ == "__main__":
    edit_tiles()
