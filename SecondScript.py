from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
        def on_created(self, event):
            file_name : str = event.src_path[15:].replace(".txt","").lower()
            for char in file_name:
                if char in "ауоыэеёиюяayeiou":
                    print(char.lower())
                else:
                    print(char.upper())
            print()
    

observer = Observer()
observer.schedule(Handler(), path="C:\\Users\\kirik")
observer.start()
try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()



