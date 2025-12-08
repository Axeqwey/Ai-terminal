import subprocess

def run_cmd(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=False  # получаем байты
        )

        # Windows пишет в cp866
        stdout = result.stdout.decode("cp866", errors="replace")
        stderr = result.stderr.decode("cp866", errors="replace")

        if stdout.strip():
            return stdout
        if stderr.strip():
            return stderr

        return "Команда выполнена."

    except Exception as e:
        return f"Ошибка выполнения команды: {e}"
