from plyer import notification
import time
if __name__== "__main__":
    title = "Happy Learning :) "
    with open("words.txt") as vc:
        lines = vc.readlines()
        for vocab in lines:
            notification.notify(title=title, message=vocab.strip(), timeout=10)
        with open("words.txt") as vc:
            lines = vc.readlines()
            for vocab in lines:
                notification.notify(title=title, message=vocab.strip(), timeout=10)
                time.sleep(300)
if __name__ == "__main__":
    while True:
        title = "Happy Learning :) "
    with open("words.txt") as vc:
        lines = vc.readlines()
        for vocab in lines:
            notification.notify(title=title, message=vocab.strip(), timeout=10)
            time.sleep(300)