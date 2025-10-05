from pyrite.monolith import element, section, routine
from pyrite.monolith.layers import tk


@element()
def examples(examples):
    @section(scope=examples)
    def ex1(ex1):
        @element(scope=ex1,intents="main_window", type=tk.tktypes.AppWindow, init=tk.tkinit(title='ex1'), layer = tk.TkGuiLayer() )
        def main_window(main_window):
            pass
        tk.run()
    @section(scope=examples)
    def ex2(ex2):
        @element(scope=ex2,intents="main_window", type=tk.tktypes.AppWindow, init=tk.tkinit(title='ex2'), configure=tk.tkconfigure(background='yellow'), layer = tk.TkGuiLayer() )
        def main_window(main_window):
            #main_window.configure(background="yellow")
            main_window.minsize(200, 200)
            main_window.maxsize(500, 500)
            main_window.geometry("300x300+50+50")
        tk.run()
    @section(scope=examples)
    def ex3(ex3):
        '''
        this example demonstrates how to create a main window using the Monolith framework with Tkinter as the GUI layer.
        The main window is configured with a title, minimum size, and geometry. Additionally, two labels are added to the window with specific text.
        1. Main Window Creation: The main window is created using the AppWindow type from the tk.tktypes module. It is initialized with a title 'ex3' and configured to have a minimum size of 200x200 pixels and a geometry of 300x300 pixels positioned at (50, 50) on the screen.
        2. Label Creation: Two labels are created as elements within the main window scope:
            - The first label displays the text "Nothing will work unless you do." and is packed into the window using the pack layout manager.
            - The second label displays the text "- Maya Angelou" and is added to the window without any specific layout manager, so it will follow the default behavior.
        3. Running the Application: Finally, the tk.run() function is called to start the Tkinter event loop, which makes the window responsive and interactive.
        4. Note: The commented-out section at the beginning shows a traditional Tkinter approach to creating a similar window with labels, which is more verbose compared to the Monolith framework approach.
        5. Overall, this example illustrates how to use the Monolith framework to create a simple GUI application with a main window and labels in a concise manner.
        6. The use of decorators and the element function allows for a clear and structured definition of the GUI components and their properties.
        7. The layout management is handled using the pack layout manager for the first label, while the layout of the second label is propagated from the first.
        8. The example showcases the ease of creating GUI applications with Monolith and Tkinter, reducing boilerplate code and enhancing readability.
        9. The use of intents, types, and initialization parameters in the element function provides flexibility and customization options for the GUI components.
        10. The overall structure of the code promotes modularity and separation of concerns, making it easier to maintain and extend the application in the future.
        '''
        @element(scope=ex3, intents="main_window", type=tk.tktypes.AppWindow, init=tk.tkinit(title='ex3'), layer = tk.TkGuiLayer() )
        def main_window(main_window):
            main_window.minsize(200, 200)
            main_window.geometry("300x300+50+50")

            @element(scope=main_window, type=tk.tktypes.Label, init=tk.tkinit(text="Nothing will work unless you do."), layout=tk.tklayout.pack())
            def label1(label1):
                pass

            @element(scope=main_window, type=tk.tktypes.Label, init=tk.tkinit(text="- Maya Angelou"))
            def label2(label2):
                pass
        tk.run()
    @section(scope=examples)
    def ex4(ex4):
        '''
        import tkinter as tk
        from tkinter import ttk

        root = tk.Tk()
        root.title("Widgets Demo")

        widgets = [
            tk.Label,
            tk.Checkbutton,
            ttk.Combobox,
            tk.Entry,
            tk.Button,
            tk.Radiobutton,
            tk.Scale,
            tk.Spinbox,
        ]

        for widget in widgets:
            try:
                widget = widget(root, text=widget.__name__)
            except tk.TclError:
                widget = widget(root)
            widget.pack(padx=5, pady=5, fill="x")

        root.mainloop()
        '''

        '''
        this example shows how to create a main window with various Tkinter widgets using Monolith framework.
        The widgets included are Label, Checkbutton, Combobox, Entry, Button, and Radiobutton.
        1. Main Window Creation: The main window is created using the AppWindow type from the tk.tktypes module. It is initialized with a title 'ex4' and configured to have a minimum size of 200x200 pixels and a geometry of 300x300 pixels positioned at (50, 50) on the screen.
        2. Widget Creation: Each widget is created as a separate element within the main window scope. The widgets are initialized with appropriate properties:
            - Label: Displays the text "Label". It is packed with padding and set to fill the horizontal space.
            - Checkbutton: Displays the text "Checkbutton". No additional properties are set. But layout is propagated from previous element.
            - Combobox: Initialized with three options: "Option 1", "Option 2", and "Option 3". No additional properties are set. But layout is propagated from previous element.
            - Entry: A text entry field. No additional properties are set. But layout is propagated from previous element.
            - Button: Displays the text "Button". No additional properties are set. But layout is propagated from previous element.
            - Radiobutton: Displays the text "Radiobutton". No additional properties are set. But layout is propagated from previous element.
        3. Layout Management: The Label widget uses the pack layout manager with padding and horizontal fill. The other widgets inherit the layout from the Label widget, ensuring consistent spacing and alignment.
        4. Running the Application: Finally, the tk.run() function is called to start the Tkinter event loop, which makes the window responsive and interactive.
        5. Note: The commented-out section at the beginning shows a traditional Tkinter approach to creating a similar window with widgets, which is more verbose compared to the Monolith framework approach.
        '''
        @element(scope=ex4, intents="main_window", type=tk.tktypes.AppWindow, init=tk.tkinit(title='ex4'), layer = tk.TkGuiLayer() )
        def main_window(main_window):
            main_window.minsize(200, 200)
            main_window.geometry("300x300+50+50")
            
            @element(scope=main_window, type=tk.tktypes.Label, init=tk.tkinit(text=tk.tktypes.Label.__name__), layout=tk.tklayout.pack(padx=5, pady=5, fill="x"))
            def label(label):
                pass
            @element(scope=main_window, type=tk.tktypes.Checkbutton, init=tk.tkinit(text=tk.tktypes.Checkbutton.__name__))
            def checkbutton(checkbutton):
                pass
            @element(scope=main_window, type=tk.tktypes.Combobox, init=tk.tkinit(values=["Option 1", "Option 2", "Option 3"]))
            def combobox(combobox):
                pass
            @element(scope=main_window, type=tk.tktypes.Entry, init=tk.tkinit())
            def entry(entry):
                pass
            @element(scope=main_window, type=tk.tktypes.Button, init=tk.tkinit(text=tk.tktypes.Button.__name__))
            def button(button):
                pass
            @element(scope=main_window, type=tk.tktypes.Radiobutton, init=tk.tkinit(text=tk.tktypes.Radiobutton.__name__))
            def radiobutton(radiobutton):
                pass


        tk.run()


    @section(scope=examples)
    def ex5(ex5):
        '''
        '''
        '''
        import tkinter as tk
        from tkinter import ttk

        root = tk.Tk()
        root.title("Tkinter Combobox")
        root.geometry("200x80")

        def selection_changed(event):
            label.config(text=f"{event.widget.get()} selected!")

        combobox = ttk.Combobox(root, values=["One", "Two", "Three"])
        combobox.set("One")
        combobox.bind("<<ComboboxSelected>>", selection_changed)
        combobox.pack(padx=5, pady=5, fill="x")

        # A helper label to show the selected value
        label = tk.Label(root, text="One selected!")
        label.pack(padx=5, pady=5, fill="x")

        root.mainloop()
        '''
        @element(scope=ex5, intents="main_window", type=tk.tktypes.AppWindow, init=tk.tkinit(title='ex5'), layer = tk.TkGuiLayer() )
        def main_window(main_window):
            main_window.minsize(200, 80)
            main_window.geometry("200x80+50+50")


            @element(scope=main_window, type=tk.tktypes.Combobox, init=tk.tkinit(values=["One", "Two", "Three"], text="One"), layout=tk.tklayout.pack(padx=5, pady=5, fill="x"))
            def combobox(combobox):
                @routine(scope=combobox, bind='<<ComboboxSelected>>')
                def selection_changed(combobox,event):
                    label.config(text=f"{event.widget.get()} selected!")

            #layout is propagated from previous element (label will be packed as well). This behavior is provided by the Monolith tk Layer
            @element(scope=main_window, type=tk.tktypes.Label, init=tk.tkinit(text="One selected!"))
            def label(label):
                pass
        tk.run()


    

#examples.ex1()
#examples.ex2()
#examples.ex3()
#examples.ex4()
examples.ex5()