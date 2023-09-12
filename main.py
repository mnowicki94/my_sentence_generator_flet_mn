import flet as ft


def main(page: ft.Page):
    page.title = "Sentence generator"
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("Sentence Generator"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False
                    ),
                ]
            ),
        ],
    )
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    txt = ft.TextField(value="", text_align="center", width=300, multiline=True, max_lines=3)

    def generate_sentence(e):
        from random import randint

        part1 = [
            "dualizm",
            "problem",
            "egzegeza",
            "problematyka",
            "kwestia",
            "dychotomia",
            "retoryka",
            "dysonans",
            "istota",
            "źródło",
            "polityka",
            "filozofia",
            "doktryna",
            "implikacje",
            "prawdziwy sens",
            "ideologia w duchu",
            "kontestowanie",
            "aberracja",
            "renesans",
            "dewaluacja",
            "tragizm",
            "reperkusje",
            "konsekwencje",
            "główne zadania",
            "teoria",
            "postulat",
            "pozytywne skutki",
            "negatywne skutki"
        ]

        part2 = [
            "wolności w post-nowoczesności",
            "emancypacji zwierząt domowych",
            "segregacji rasowej",
            "duszy polskiej",
            "percepcji indywidualnej",
            "obarczania winą innych",
            "ksenofobii pierwotnej",
            "tolerancji odmienności",
            "picia taniego alkoholu pod sklepem"]

        connectors = ["a"]


        #### 2) losowanko

        part1a_selected = part1[randint(0, len(part1) - 1)]
        part2a_selected = part2[randint(0, len(part2) - 1)]

        connectors_selected = connectors[randint(0, len(connectors) - 1)]

        part1.remove(part1a_selected)
        part2.remove(part2a_selected)

        part1b_selected = part1[randint(0, len(part1) - 1)]
        part2b_selected = part2[randint(0, len(part2) - 1)]

        #### 3) print
        temat = ' '.join([part1a_selected.capitalize(), part2a_selected, connectors_selected, part1b_selected,
                          part2b_selected + "."])
        txt.value = temat
        page.update()

    page.add(
        ft.Row(
            [
                txt
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.ElevatedButton("Generate!", on_click=generate_sentence)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

#app
# ft.app(target=main)

#webapp
ft.app(target=main, view=ft.AppView.WEB_BROWSER)