import flet as ft

from gui.logic import run_analysis_async


def build_ui(page: ft.Page):
    # ---------------- STATE ----------------
    selected_file = ft.Text()
    output_file = ft.Text()
    log_box = ft.Text(value="", selectable=True)
    progress = ft.ProgressBar(value=0)

    burn_in = ft.TextField(label="Burn-in", value="0.1")
    date_sep = ft.TextField(label="Date separator", value="+")
    date_format = ft.TextField(label="Date format", value="%Y-%m-%d")
    scale = ft.TextField(label="Scale", value="365.24219")

    file_picker = ft.FilePicker()

    # ---------------- CALLBACK HELPERS ----------------
    def add_log(msg):
        log_box.value += msg + "\n"
        page.update()

    def set_progress(i, total):
        if total:
            progress.value = i / total
        page.update()

    def done(result):
        df, csv_path, leaf_path = result
        add_log("DONE")
        if csv_path:
            add_log(f"Saved: {csv_path}")
        progress.value = 1
        page.update()

    def error(msg):
        add_log(f"ERROR: {msg}")

    # ---------------- ACTIONS ----------------
    async def pick_input(_):
        files = await file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["trees", "tre", "tree"],
        )

        if not files:
            selected_file.value = "No file selected"
            page.update()
            return

        selected_file_path = files[0].path
        selected_file.value = selected_file_path
        page.update()

    async def pick_output_file(_):
        path = await file_picker.save_file(
            file_name="results.csv",
            allowed_extensions=["csv", "log", "xsv"],
        )

        if path:
            output_file.value = path
        else:
            output_file.value = ""

        page.update()

    def run_clicked(_):
        log_box.value = ""
        progress.value = 0

        if not selected_file.value or selected_file.value in ("", "Cancelled", "No file selected"):
            add_log("Select input file first")
            return

        if not output_file.value:
            add_log("Select output file first")
            return

        params = {
            "trees_file": selected_file.value,
            "output": output_file.value if output_file.value != "Cancelled" else None,
            "burn_in": float(burn_in.value),
            "date_sep": date_sep.value,
            "date_format": date_format.value,
            "scale": float(scale.value),
        }

        add_log("Starting analysis...")

        run_analysis_async(
            params,
            on_log=add_log,
            on_progress=set_progress,
            on_done=done,
            on_error=error,
        )

    # ---------------- UI ----------------
    page.add(
        ft.Column([
            ft.Row(
                [
                    ft.Text("Brokilon Transmission App", size=22),

                    ft.Container(expand=True),

                    ft.Image(
                        src="brokilon.png",
                        width=48,
                        height=48,
                        fit=ft.BoxFit.CONTAIN,
                    )
                ],
            ),

            ft.Row([
                ft.ElevatedButton(
                    "Select Trees File",
                    on_click=pick_input
                ),
                selected_file,
            ]),

            ft.Row([
                ft.ElevatedButton(
                    "Select Output File",
                    on_click=pick_output_file
                ),
                output_file,
            ]),

            burn_in,
            date_sep,
            date_format,
            scale,

            ft.ElevatedButton("Run Analysis", on_click=run_clicked),

            progress,

            ft.Container(
                content=log_box,
                height=250,
                border_radius=10,
                padding=10,
            ),
        ])
    )
