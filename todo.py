import sqlite3
from bottle import route, run, debug, template, request

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    #mod 1#result = c.fetchall()
    #mod 1return str(result)
    #mod 1
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output
	#mod 1

#mod 2

@route('/new', method='GET')
def new_item():

    new = request.GET.get('task', '').strip()

    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
    new_id = c.lastrowid

    conn.commit()
    c.close()
    return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
#mod 2


# reloader and deb for development only
run(host='localhost', port=8210, debug=True, reloader=True)






