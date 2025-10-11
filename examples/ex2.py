from pyrite.monolith import element, section, cluster, feature
from pyrite.monolith.layers import tk


@element(intents="main_window", type=tk.tktypes.Tk)
def window():

    @element(window, intents="header", type=tk.tktypes.Label,
             init=tk.tkinit(text="Tasks (0)"),
             layout=tk.tklayout.pack(pady=5))
    def header():
        pass

    @section(window, intents="entry", type=tk.tktypes.Entry,
             layout=tk.tklayout.pack(pady=5))
    def entry():
        pass

    @element(window, intents="task_area", type=tk.tktypes.Frame,
             layout=tk.tklayout.pack(fill="both", expand=True))
    def task_area():

        @cluster(task_area, intents="task_item", type=tk.tktypes.Frame)
        def task_item(text):
            label = tk.tktypes.Label(text=text)
            label.pack(anchor="w")

    @element(window,
             intents="add_button",
             type=tk.tktypes.Button,
             init=tk.tkinit(text="Add Task"),
             layout=tk.tklayout.pack(pady=5),
             bind='command')
    def add_button():
        text = entry.get()
        if text.strip():
            task_area.task_item(text)
            count = len(task_area.children)
            header.config(text=f"Tasks ({count})")
            entry.delete(0, "end")


@element(intents="feature_section")
def feature_section():

    @feature(feature_section, host=window.task_area, intents="logger_feature")
    def logger_feature():
        print("Logger active for task_area")


tk.run()