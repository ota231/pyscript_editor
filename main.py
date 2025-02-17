import sys
import io
import time
from pyscript import document, when

@when("click", "#run-code")
def execute_code(event):
    user_code = document.querySelector("#editor").innerText

    #redirect stdout
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
        exec(user_code)
    except Exception as e:
        new_stdout.write(str(e))
    finally:
        sys.stdout = old_stdout

    output_content = new_stdout.getvalue()

    document.querySelector("#output-container").innerText = output_content

@when("click", "#mode-selector")
def switch_modes(event):
    mode = document.querySelector('#mode-selector').value
    scripting_mode = document.querySelector("#scripting-mode")
    interactive_mode = document.querySelector("#interactive-mode")

    if mode == "scripting":
        scripting_mode.style.display = 'flex'
        interactive_mode.style.display = "none"
    else:
        interactive_mode.style.display = "block"
        scripting_mode.style.display = 'none'

        