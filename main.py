import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="Yeni ileti",
        message=" Hoşgeldiniz",

        # displaying time
        timeout=2
    )
    # waiting time
    time.sleep(5)
