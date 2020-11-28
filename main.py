import io

import requests
from markdownify import markdownify as md
import rumps
from notion.client import NotionClient
import notion.block as block
from md2notion.upload import upload, convert





with open('/Users/sohrab/Desktop/token_v2.txt') as f:
    token_v2 = f.readline()

client = NotionClient(token_v2=token_v2)

class NotionMenuBar(rumps.App):
    def __init__(self):
        super(NotionMenuBar, self).__init__("Notion Menu Bar",  icon="notion-logo.png")
        self.menu = [
        {
            'Add To': {
                "Databases",
                None
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
            new_database = rumps.MenuItem(title=self.get_page_name(window.text))
            self.databases[self.get_page_name(window.text)] = window.text
            self.menu['Add To'].add(new_database)
            new_database.set_callback(self.onoff)


    def onoff(self, sender):
        sender.state = not sender.state
        window = rumps.Window(title="Paste the link",
                              cancel="Cancel", ok="Save Link",
                              dimensions=(250, 100))
        window.icon = 'notion-logo.png'
        window = window.run()
        if window.clicked:
            cv = client.get_collection_view(self.databases[sender.title])
            row = cv.collection.add_row()


    def get_page_name(self, link):
        return client.get_block(link).title


if __name__ == "__main__":
    url = 'http://www.cs.toronto.edu/~bonner/courses/2020f/csc311/'

    page = client.get_block("https://www.notion.so/The-Page-0a2a66080879419aa0fa7efeae521a73")

    new_page = page.children.add_new(block.PageBlock, title="New Markdown Page")



    path = url
    r = requests.get(path)
    if not r.status_code < 300:  # TODO: Make this better..., should only accept success
        raise RuntimeError(f'Could not get file {path}, HTTP {r.status_code}')
    fileName = path.split('?')[0]
    fileName = fileName.split('/')[-1]
    fileLike = io.StringIO(r.text)
    fileLike.name = path

    upload(fileLike, new_page)

    app = NotionMenuBar()
    app.run()
