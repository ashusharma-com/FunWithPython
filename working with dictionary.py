app = None
app = {

    'x':'xxxxxxxxxx',
    'summary':'This is simple app',
    'author':'Xyz DEV',

}
print(app)
app['name'] = 'My First Application'
print(app)
app.update({'website':"http://xyz.com"})
print(app)
del app['x']
print(app)

print("\n\n\n")
for key,val in app.items():
    print(key,val)
