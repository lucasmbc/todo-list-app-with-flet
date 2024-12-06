import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    tasks = ft.ListView(expand=True, spacing=10, padding=20)

    def add_task(e):
        if task_input.value.strip() != "":
            def remove_current_task(event):
                tasks.controls.remove(task_item)
                page.update()

            task_item = ft.Row(
                controls=[
                    ft.Text(task_input.value, expand=True),
                    ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINE, 
                        on_click=remove_current_task
                    )
                ]
            )
            
            tasks.controls.append(task_item)
            
            task_input.value = ""
            
            page.update()

    task_input = ft.TextField(
        label="Digite uma tarefa", 
        expand=True
    )

    add_button = ft.IconButton(
        icon=ft.icons.ADD_CIRCLE_OUTLINED,
        on_click=add_task
    )

    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        task_input,
                        add_button
                    ]
                ),
                tasks
            ],
            width=600,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)