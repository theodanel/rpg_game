import time
import os
import subprocess
import psutil  # pip install psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

EXE_PATH = os.path.join("dist", "rpg_game.exe")
SCRIPT_PATH = "rpg_game.py"

class RebuildHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(SCRIPT_PATH):
            print(f"📁 Modification détectée : {event.src_path}")
            self.rebuild_exe()

    def rebuild_exe(self):
        # Fermer l'exécutable s'il tourne déjà
        for proc in psutil.process_iter(attrs=["pid", "name"]):
            if proc.info["name"] == "rpg_game.exe":
                print("⛔ Fermeture de l'ancienne version...")
                proc.kill()

        # Compiler le script en .exe
        print("🔧 Fichier rpg_game.py modifié, lancement de la recompilation...")
        result = subprocess.run(
            [os.path.join("..", "Thonny", "python.exe"), "-m", "PyInstaller", "--onefile", SCRIPT_PATH],
            capture_output=True, text=True
        )

        if result.returncode == 0 and os.path.exists(EXE_PATH):
            print("✅ .exe généré avec succès. Lancement...")
            subprocess.Popen(EXE_PATH)
        else:
            print("❌ Échec de la compilation :")
            print(result.stderr)

if __name__ == "__main__":
    path = "."  # Dossier à surveiller
    print("👀 Surveillance démarrée sur rpg_game.py...")
    event_handler = RebuildHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
