import threading

import brokilon.ccd.cli.breath_helper


def run_analysis_async(params, on_log, on_progress, on_done, on_error):
    """
    Runs your pipeline in a background thread so UI doesn't freeze.
    """

    def worker():
        try:
            def log(msg):
                on_log(msg)

            def progress(i, total):
                on_progress(i, total)

            result = brokilon.ccd.cli.breath_helper.process_trees_file(
                trees_file=params["trees_file"],
                output=params["output"],
                burn_in=params["burn_in"],
                date_sep=params["date_sep"],
                date_format=params["date_format"],
                scale=params["scale"],
                log_callback=log,
                progress_callback=progress,
            )

            on_done(result)

        except Exception as e:
            on_error(str(e))

    threading.Thread(target=worker, daemon=True).start()
