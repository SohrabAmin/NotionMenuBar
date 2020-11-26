import rumps


class NotionMenuBar(rumps.App):
    def __init__(self):
        super(NotionMenuBar, self).__init__("Notion Menu Bar",  icon="notion-logo.png")
        self.menu = [
        {
            'Add To': {
            }
        },
        None,
        'Add Database',
        None
    ]
        # self.add_to = rumps.MenuItem(title="Add To")
        # self.add_database = rumps.MenuItem(title="Add Database")
        self.databases = {}
        # self.menu = [self.add_to, self.add_database]

    @rumps.clicked("Add Database")
    def get_database(self, _):
        window = rumps.Window(title="Add The Database Block Link",
                              cancel="Cancel", ok="Save Database",
                              dimensions=(250, 100))
        window.icon = 'notion-logo.png'
        window = window.run()
        if window.clicked:
            new_database = rumps.MenuItem(title=window.text)
            self.databases[window.text] = new_database
            self.menu['Add To'].add(new_database)

    @rumps.clicked("Add To", "")
    def onoff(self, sender):
        sender.state = not sender.state



if __name__ == "__main__":
    app = NotionMenuBar()
    app.run()
