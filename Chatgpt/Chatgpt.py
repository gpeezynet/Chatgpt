import tkinter as tk
import sqlite3

# Connect to the database
conn = sqlite3.connect('inventory.db')
c = conn.cursor()

# Create the database tables if they don't already exist
c.execute('''
CREATE TABLE IF NOT EXISTS items (
    item_id INTEGER PRIMARY KEY,
    item_description TEXT,
    lot_number TEXT,
    receiving_date TEXT,
    inventory_value INTEGER
)
''')
conn.commit()

# Main window class
class InventoryWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Set the title and size of the window
        self.title("Inventory")
        self.geometry("600x400")
        
        # Create the main frame to hold the other widgets
        main_frame = tk.Frame(self, bg="light blue")
        main_frame.pack(fill="both", expand=True)
        
        # Create the listbox to display the items
        self.listbox = tk.Listbox(main_frame, bg="white")
        self.listbox.pack(side="left", fill="both", expand=True)
        
        # Create the scrollbar for the listbox
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # Create the text boxes for data entry
        description_label = tk.Label(self, text="Description", bg="light blue")
        description_label.pack(side="top", fill="x")
        self.description_entry = tk.Entry(self)
        self.description_entry.pack(side="top", fill="x")
        
        lot_number_label = tk.Label(self, text="Lot Number", bg="light blue")
        lot_number_label.pack(side="top", fill="x")
        self.lot_number_entry = tk.Entry(self)
        self.lot_number_entry.pack(side="top", fill="x")
        
        receiving_date_label = tk.Label(self, text="Receiving Date", bg="light blue")
        receiving_date_label.pack(side="top", fill="x")
        self.receiving_date_entry = tk.Entry(self)
        self.receiving_date_entry.pack(side="top", fill="x")
        
        inventory_value_label = tk.Label(self, text="Inventory Value", bg="light blue")
        inventory_value_label.pack(side="top", fill="x")
        self.inventory_value_entry = tk.Entry(self)
        self.inventory_value_entry.pack(side="top", fill="x")
        
        # Create the buttons to
