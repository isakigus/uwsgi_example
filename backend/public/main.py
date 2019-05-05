from pyfiglet import Figlet
figlet = Figlet(font="slant")


def application(environ, start_response):
    # import rpdb;rpdb.set_trace()
    start_response("200 OK", [("Content-Type", "text/plain"),
                              ("Content-Encoding", "utf-8")])
    yield figlet.renderText("Hello wooooooorld!").encode("utf-8")
    for k, v in environ.items():
        yield f"{k:>20} => {v}\n".encode("utf-8")


