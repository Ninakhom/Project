from ConnectDB import create_connection, close_connection, get_cursor
import ast
import requests 
conn = create_connection()
cursor = get_cursor(conn)
cursor.execute("""Create table if not exists food_table(food_name TEXT,nutrients TEXT,serving_size REAL)""")
conn.commit()
def get_food_info(food_name):
    cursor.execute("select * from food_table where food_name=?",(food_name,))
    food_info = cursor.fetchone()
    if food_info:
        return ast.literal_eval(food_info[1]),food_info[2]
    else:
        url="https://api.nal.usda.gov/fdc/v1/foods/search?"
        api_key="IAvvXOlWXCb3tNQjhvTawW6jtmD8Xl3eejJJI9EE"
        query = url+"query="+food_name+"&api_key=" + api_key
        res=requests.get(query).json()
        food_item=res["foods"][0]
        nutrients = food_item["foodNutrients"]
        serving_size=food_item["servingSize"]

        cursor.execute("""insert into food_table (food_name,nutrients, serving_size) values
                (?,?,?,?)""", (food_name,str(nutrients), serving_size)
        )
        conn.commit()
        return nutrients, serving_size
    
cal=0
po=0
fat=0
car=0

while True:
    food_name= input("enter")
    if food_name=="done":
        break
    food_intake=float(input("Enter amont of:" ))
    nutrients,serving_size=get_food_info(food_name)