import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab06"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_anno = None
        self.txt_brand = None
        self.txt_retailer = None
        self.btn_top_vendita = None
        self.btn_analizza_vendite = None
        self.txt_result = None
        #self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_anno=ft.Dropdown(options=[ft.dropdown.Option(key= "None", text="Nessun filtro")],width=250,label="Anno",hint_text="inserire anno")
        self._controller.popola_anno()

        self.txt_brand=ft.Dropdown(options=[ft.dropdown.Option(key= "None", text="Nessun filtro")],width=250,label="brand",hint_text="Inserire brand")
        self._controller.popola_brand()

        self.txt_retailer=ft.Dropdown(options=[ft.dropdown.Option(key= "None", text="Nessun filtro")],width=250,label="Retailer",hint_text="Inserire retailer")
        self._controller.popola_retailer()

        row1=ft.Row([self.txt_anno,self.txt_brand,self.txt_retailer],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #row 2
        # button for the "hello" reply
        self.btn_top_vendita = ft.ElevatedButton(text="Top-vendita", on_click=self._controller.top_vendita)
        self.btn_analizza_vendite = ft.ElevatedButton(text="Analizza-vendite", on_click=self._controller.analizza_vendita)
        row2 = ft.Row([self.btn_top_vendita, self.btn_analizza_vendite],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
