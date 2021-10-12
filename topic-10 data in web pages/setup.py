import dataset

items=[
{"user":"bob", "note":"this is a nice day"},
{"user":"santa", "note":"this is a not nice day"},
{"user":"phil", "note":"this isn't a nice day"},
{"user":"todd", "note":"this will be a nice day"},
{"user":"will", "note":"this won't be a nice day"},
{"user":"robert", "note":"this has been a nice day"},

]

#connect to the database
db= dataset.connect('sqlite:///mydatabase.db')

#create the table
db['notes'].drop()
table=db['notes']

#put data in the table
for item in items:
    table.insert(item)

print("done")