import webapp

class urlsrandom(webapp.webApp):
    def process(self, parsedRequest):
        #Process the relevant elements of the request.
        import random
        randomURL = random.randint(1,99999999)

        return ("200 OK", "<html><body><h1><A HREF=" + str(randomURL) +
                              ">Dame Otra</h1></A></body></html>")
if __name__ == "__main__":
    try:
        testWebApp = urlsrandom("localhost", 1234)
    except KeyboardInterrupt:
        print ("\nClosing binded socket")
