#!/Users/christopher.ogbunuzor/.pyenv/shims/python
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="my-secret-pw",
  database="Todo"
)

mycursor = mydb.cursor()

# mycursor.execute("show tables;")
# for x in mycursor:
#   print(x)

# mycursor.execute("select * from Movies;")
# movielist = []
# for x in mycursor:
#    movielist.append(x)

#create method to add new items to Todo list
def add_to_list(item):
    sql = "INSERT INTO items VALUES (%s, %s)"
    # Keep the initial status as NotStarted
    val = (item, "NotStarted")
        
    mycursor.execute(sql, val)

    # We commit to save the change
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    return {"item": item, "status": "NotStarted"}

def get_all_items():
    try:
        mycursor.execute('select * from items;')
        
        rows = mycursor.fetchall()
        return { "count": len(rows), "items": rows }
    except Exception as e:
        print('Error: ', e)
        return None

def get_item_status(item):
    try:
        mycursor.execute("select status from items where item='%s'" % item)
        status = mycursor.fetchone()[0]
        return status
    except Exception as e:
        print('Error: ', e)
        return None

def update_status(item, status):
    # Check if the passed status is a valid value
    if (status.lower().strip() == 'not started'):
        status = "NOTSTARTED"
    elif (status.lower().strip() == 'in progress'):
        status = "INPROGRESS"
    elif (status.lower().strip() == 'completed'):
        status = "COMPLETED"
    else:
        print("Invalid Status: " + status)
        return None

    try:
        sql = "UPDATE items SET status = %s WHERE item = %s "
        # Keep the initial status as NotStarted
        val = (status, item)
        
        mycursor.execute(sql, val)
        #mycursor.execute('update items set status=? where item=?', (status, item))
        mydb.commit()
        return {item: status}
    except Exception as e:
        print('Error: ', e)
        return None

def delete_item(item):
    try:
        
        mycursor.execute('delete from items where item=%s', (item,))
        mydb.commit()
        return {'item': item}
    except Exception as e:
        print('Error: ', e)
        return None




