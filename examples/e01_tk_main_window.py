from pyrite.monolith import element, section, routine
from pyrite.monolith.layers import tk
from PIL import Image, ImageTk  # I


'''
Examples of Monolith with Tkinter layer
Examples are inspired by https://realpython.com/python-gui-tkinter/#creating-a-simple-application-with-tkinter
More Tkinter widgets: https://docs.python.org/3/library/tkinter.ttk.html#widget-classes
More Tkinter layouts: https://docs.python.org/3/library/tkinter
All examples are orgnaized in sections, so you can run them one at a time by uncommenting the call at the bottom of this file.
This shows how concise and clear the code is using Monolith framework.
'''

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
        Note: real widgt instantiation, layout and configuration is done by the Monolith tk Layer. 
        We must use the tkinit, tklayout and tkconfigure helpers to pass parameters to the widgets constructors and methods.
        main_window function is called when the main window is created by the Monolith tk layer, after construction, configuration and layout.
        Note that if one call main_window Scope as a function, it not createa new window, but configure and layout are applied again before original decorated funcion is called. Thanks to the Monolith tk Layer.  
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

    @section(scope=examples)
    def ex6(ex6):
        '''
        This example demonstrates how to create a main window with nested frames using the Monolith framework with Tkinter as the GUI layer.
        Note that Monolith tk layer defaults to ttk widgets, so Frame is a ttk.Frame. To use tk.Frame, we must specify it explicitly using the type parameter.
        As known, ttk.Frame does not support the background parameter, so we must use a style to set the background color.
        The example shows how simply styles can be applied to widgets using the Monolith tk layer.
        The original example quoted in the comment uses only tk.Frame, so the background parameter is used directly.
        '''
        '''
        import tkinter as tk

        root = tk.Tk()
        root.title("Nested Frames")
        root.config(bg="skyblue")

        frame = tk.Frame(root, width=200, height=200)
        frame.pack(padx=10, pady=10)

        nested_frame = tk.Frame(frame, width=190, height=190, bg="red")
        nested_frame.pack(padx=10, pady=10)

        root.mainloop()        
        '''
        @element(scope=ex6, intents="main_window", type=tk.tktypes.AppWindow, init=tk.tkinit(title='ex6'), configure=tk.tkconfigure(bg="skyblue"), layer = tk.TkGuiLayer() )
        def main_window(main_window):
            main_window.minsize(300, 300)
            main_window.geometry("300x300+50+50")

            @element(scope=main_window, type=tk.tktypes.Frame, init=tk.tkinit(width=200, height=200), layout=tk.tklayout.pack(padx=10, pady=10))
            def outer_frame(outer_frame):
                @element(scope=outer_frame, type=tk.tktypes.Frame, init=tk.tkinit(width=190, height=190), style=tk.tkstyle(background="red"))
                def inner_frame(inner_frame):
                    pass

        tk.run()

    @section(scope=examples)
    def ex7(ex7):
        '''
        import tkinter as tk
        from tkinter import ttk

        root = tk.Tk()
        root.title("Image Editor")

        image = tk.PhotoImage(file="forest.png")

        # Tools frame
        tools_frame = tk.Frame(root, width=200, height=400, bg="skyblue")
        tools_frame.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.Y)
        tk.Label(
            tools_frame,
            text="Original Image",
            bg="skyblue",
        ).pack(padx=5, pady=5)
        thumbnail_image = image.subsample(5, 5)
        tk.Label(tools_frame, image=thumbnail_image).pack(padx=5, pady=5)

        # Tools and Filters tabs
        notebook = ttk.Notebook(tools_frame)
        notebook.pack(expand=True, fill="both")

        tools_tab = tk.Frame(notebook, bg="lightblue")
        tools_var = tk.StringVar(value="None")
        for tool in ["Resizing", "Rotating"]:
            tk.Radiobutton(
                tools_tab,
                text=tool,
                variable=tools_var,
                value=tool,
                bg="lightblue",
            ).pack(anchor="w", padx=20, pady=5)

        filters_tab = tk.Frame(notebook, bg="lightgreen")
        filters_var = tk.StringVar(value="None")
        for filter in ["Blurring", "Sharpening"]:
            tk.Radiobutton(
                filters_tab,
                text=filter,
                variable=filters_var,
                value=filter,
                bg="lightgreen",
            ).pack(anchor="w", padx=20, pady=5)

        notebook.add(tools_tab, text="Tools")
        notebook.add(filters_tab, text="Filters")

        # Image frame
        image_frame = tk.Frame(root, width=400, height=400, bg="grey")
        image_frame.pack(padx=5, pady=5, side=tk.RIGHT)
        display_image = image.subsample(2, 2)
        tk.Label(
            image_frame,
            text="Edited Image",
            bg="grey",
            fg="white",
        ).pack(padx=5, pady=5)
        tk.Label(image_frame, image=display_image).pack(padx=5, pady=5)

        root.mainloop()            
        '''

        @element(scope=ex7, intents="main_window", type=tk.tktypes.AppWindow, init=tk.tkinit(title='ex7'), layer = tk.TkGuiLayer() )
        def main_window(main_window):
            main_window.minsize(600, 400)
            main_window.geometry("600x400+50+50")

            #@element(scope=main_window, type=tk.tktypes.PhotoImage, init=tk.tkinit(file="./examples/assets/pngimg.com - forest_PNG47.png"))
            #def an_image(an_image):
            #    pass
            try:                
                an_image = tk.tktypes.PhotoImage(Image.open("./examples/assets/pngimg.com - forest_PNG47.png"))
                main_window.an_image = an_image  # Keep a reference to avoid garbage collection
            except Exception as e:
                print("Error loading image:", e)
                an_image = tk.tktypes.PhotoImage()  # Create an empty PhotoImage if loading fails

            @element(scope=main_window, type=tk.tktypes.Frame, init=tk.tkinit(width=200, height=400), style=tk.tkstyle(background="skyblue"), layout=tk.tklayout.pack(padx=5, pady=5, side="left", fill="y"))
            def tools_frame(tools_frame):

                @element(scope=tools_frame, type=tk.tktypes.Label, init=tk.tkinit(text="Original Image"), style=tk.tkstyle(background="skyblue"), layout=tk.tklayout.pack(padx=5, pady=5))
                def label1(label1):
                    pass

                @element(scope=tools_frame, type=tk.tktypes.Label, init=tk.tkinit(image=an_image.subsample(5, 5)))
                def thumbnail_label(thumbnail_label):
                    pass

                @element(scope=tools_frame, type=tk.tktypes.Notebook, layout=tk.tklayout.pack(expand=True, fill="both"))
                def notebook__(notebook__):
                    if True:
                        @element(scope=notebook__, type=tk.tktypes.Frame, style=tk.tkstyle(background="lightblue"))
                        def tools_tab(tools_tab):
                            if True:
                                #@element(scope=notebook, type=tk.tktypes.StringVar, init=tk.tkinit(value="None"))
                                #def tools_var(tools_var):
                                #    pass
                                tools_var = tk.tktypes.StringVar(value="None")
                                for tool in ["Resizing", "Rotating"]:
                                    @element(scope=tools_tab, type=tk.tktypes.Radiobutton, init=tk.tkinit(text=tool, variable=tools_var, value=tool), style=tk.tkstyle(background="lightblue"), layout=tk.tklayout.pack(anchor="w", padx=20, pady=5))
                                    def radiobutton(radiobutton):
                                        pass

                        @element(scope=notebook__, type=tk.tktypes.Frame, style=tk.tkstyle(background="lightgreen"))
                        def filters_tab(filters_tab):
                            if True:
                                #@element(scope=notebook, type=tk.tktypes.StringVar, init=tk.tkinit(value="None"))
                                #def filters_var(filters_var):
                                #    pass
                                filters_var = tk.tktypes.StringVar(value="None")
                                    
                                for i, filter in enumerate(["Blurring", "Sharpening"]):
                                    @element(scope=filters_tab, clustering=i, type=tk.tktypes.Radiobutton, init=tk.tkinit(text=filter, variable=filters_var, value=filter), style=tk.tkstyle(background="lightgreen"), layout=tk.tklayout.pack(anchor="w", padx=20, pady=5))
                                    def radiobutton(radiobutton):
                                        pass

                        #notebook__.__joint__.tool.add(tools_tab.__joint__.tool, text="Tools")
                        #notebook__.__joint__.tool.add(filters_tab.__joint__.tool, text="Filters")

            @element(scope=main_window, type=tk.tktypes.Frame, init=tk.tkinit(width=400, height=400), style=tk.tkstyle(background="grey"), layout=tk.tklayout.pack(padx=5, pady=5, side="right"))
            def image_frame(image_frame):
                @element(scope=image_frame, type=tk.tktypes.Label, init=tk.tkinit(text="Edited Image"), style=tk.tkstyle(background="grey", foreground="white"), layout=tk.tklayout.pack(padx=5, pady=5))
                def label2(label2):
                    pass
                @element(scope=image_frame, type=tk.tktypes.Label, init=tk.tkinit(image=an_image.subsample(2, 2)), layout=tk.tklayout.pack(padx=5, pady=5))
                def display_label(display_label):
                    pass


        main_window.tools_frame.notebook__.__joint__.tool.add(main_window.tools_frame.notebook__.tools_tab.__joint__.tool, text="Tools")
        main_window.tools_frame.notebook__.__joint__.tool.add(main_window.tools_frame.notebook__.filters_tab.__joint__.tool, text="Filters")

        tk.run()


                                        

    

#examples.ex1()
#examples.ex2()
#examples.ex3()
#examples.ex4()
#examples.ex5()
#examples.ex6()
examples.ex7()