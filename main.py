import rumps

class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("Awesome App", icon="notion-logo.png")
        self.menu = ["Preferences", "Silly button", "Say hi", "Send to Notion"]

    @rumps.clicked("Preferences")
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")

    @rumps.clicked("Silly button")
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

    @rumps.clicked("Send to Notion")
    def send(self, _):
        window = rumps.Window(title="Send Link to Notion", default_text="https://...", ok="Send to Notion", dimensions=(100, 100))
        window.icon = 'notion-logo.png'
        window = window.run()
        if window.clicked:
            print(window.text)


if __name__ == "__main__":
    AwesomeStatusBarApp().run()