import rumps


class NotionMenuBar(rumps.App):
    def __init__(self):
        super(NotionMenuBar, self).__init__("Notion Menu Bar",  icon="notion-logo.png")
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
            self.databases[window.text] = rumps.MenuItem(title=window.text)
            self.menu['Add To'].update(self.databases)



if __name__ == "__main__":
    app = NotionMenuBar()
    app.menu = [
        {
            'Add To': {

            }
        },
        None,
        'Add Database',
        None
    ]
    app.run()
