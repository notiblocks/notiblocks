import time
import random

from notiblocks.notiblocks import NBConfig
from notiblocks.notiblocks import NBHandler

from notiblocks.notiblocks import ILConfig
from notiblocks.notiblocks import ILFormatter

def main():
    print("== Notiblocks Examples ==")
    
    nb_conf = NBConfig(
        success_sign_color="blue",
        time_sign_color="gREen",
        success_sign="SUCCESS",
        success_bracket_color="cyan",
        time_sign_stamp="DATE",
        bracket_style="round     ",
        warn_bracket_sign="square"
    )

    nb_handler = NBHandler(nb_conf)

    # You could even format things inline
    print(nb_handler.success(ILFormatter.format(message="This is a $TEST$ successful message", args=["red"])))

    print(nb_handler.fail("And this is a failed message"))
    print(nb_handler.warn("But this is a warning message"))
    print(nb_handler.log("This is a logged message."))

    id = 0

    print("== LOGS ==")
    while True:
        delay = random.uniform(1, 3)
        print(nb_handler.log(f"New registration -- USER-id: {id}"))
        id += 1
        time.sleep(delay)


# MAIN
if __name__ == '__main__':
    main()