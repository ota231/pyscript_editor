import sys
import io
from pyscript import document

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

    document.querySelector("#output").innerText = output_content