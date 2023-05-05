import json;
import os;
import tkinter as tk;
from tkinter import filedialog;

def operation():
	folder_path = entry_folder.get();
	selected_option = opt.get();

	txt_result.configure(state="normal");
	txt_result.delete("1.0", tk.END);

	for root, dirs, files in os.walk(folder_path):
		for filename in files:
			if filename.endswith('.json'):
				file_path = os.path.join(root, filename);

				try:
					with open(file_path, 'r', encoding='utf-8') as json_file:
						data = json.load(json_file);
				except (FileNotFoundError, json.JSONDecodeError) as e:
					txt_result.insert(tk.END, f"{filename} - Error: {str(e)}\n");
					continue;

				if selected_option in data:
					if data[selected_option]:
						data[selected_option] = [];
						with open(file_path, 'w', encoding='utf-8') as json_file:
							json.dump(data, json_file, ensure_ascii=False, separators=(',', ':'));
						txt_result.insert(tk.END, f"{filename} - successfully completed\n", "success");
					else:
						txt_result.insert(tk.END, f"{filename} - the selected array is already empty\n");
				else:
					txt_result.insert(tk.END, f"{filename} - array not found\n");

				txt_result.update();

	txt_result.configure(state="disabled");


def browse_folder():
	folder_selected = filedialog.askdirectory();
	entry_folder.delete(0, tk.END);
	entry_folder.insert(0, folder_selected);


win = tk.Tk();
win.title("Clash of Clans Villages Object Array Removal");

lbl_folder = tk.Label(win, text="Folder:");
lbl_folder.grid(row=0, column=0, padx=5, pady=5);

entry_folder = tk.Entry(win);
entry_folder.grid(row=0, column=1, padx=5, pady=5);

btn_browse = tk.Button(win, text="Select", command=browse_folder);
btn_browse.grid(row=0, column=2, padx=5, pady=5);

lbl_option = tk.Label(win, text="select object to remove:");
lbl_option.grid(row=1, column=0, padx=5, pady=5);

opt = tk.StringVar();
opt.set("obstacles");

menu_opt = tk.OptionMenu(win, opt, "obstacles", "obstacles2", "cooldowns", "decos");
menu_opt.grid(row=1, column=1, padx=5, pady=5);

btn_process = tk.Button(win, text="Start Process", command=operation);
btn_process.grid(row=2, column=0, columnspan=3, padx=10, pady=10);

lbl_result = tk.Label(win, text="Results:");
lbl_result.grid(row=3, column=0, padx=5, pady=5);

txt_result = tk.Text(win, height=40, width=80)
txt_result.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

win.mainloop()
