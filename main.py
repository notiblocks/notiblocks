from notiblocks import NBConfig, NBHandler

# METHODS
def main():
    print("== Notiblocks Examples ==")
    
    nb_conf = NBConfig(
        success_sign_color="blue",
        time_sign_color="red",
        success_sign="SUCCESS",
        success_bracket_color="can"
    )

    nb_handler = NBHandler(nb_conf)

    print(nb_handler.sucess("This is a successful message"))
    print(nb_handler.fail("And this is a failed message"))
    print(nb_handler.warn("But this is a warning message"))
    print(nb_handler.log("This is a logged message."))


# MAIN
if __name__ == '__main__':
    main()