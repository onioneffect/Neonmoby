import requests as r

my_heads = {
    "Foo": "Bar"
    # This part is for plugging in the headers from your own browser
    # Still a WIP
}

class NeonmobSession:
    def __init__(self, user_name : str = None, pass_word : str = None):
        if user_name and pass_word:
            self.rsession = r.Session()
            self.un = user_name
            self.pw = pass_word

        return

    def login(self, user_name : str = None, pass_word : str = None):
        if not user_name and not pass_word:
            user_name = self.un
            pass_word = self.pw

        return self.rsession.post(
            "https://neonmob.com/signin",
            headers = my_heads,
            data = {"password": self.pw, "username": self.un}
        )
