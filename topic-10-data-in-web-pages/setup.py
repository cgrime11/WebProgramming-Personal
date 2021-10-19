import dataset

items = [
    {"user":"bob", "note":"this is a nice day"},
    {"user":"santa", "note":"Christmas is coming!"},
    {"user":"bob", "note":"My real name is Robert"},
    {"user":"roger", "note":"I was named after a rabbit"},
    {"user":"roger", "note":"No, honest, I really was..."},
    {"user":"santa", "note":"Rudolph needs a lot of attention"}
]

# connecting to a SQLite database
db = dataset.connect('sqlite:///database.db')

# create a notes table
db['notes'].drop()
table = db['notes']

# put some data in table
for item in items:
    table.insert(item)

print("done.")





