
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error 
import traceback

app = Flask(__name__)


def update_data(id,name):
	try:
		connection =mysql.connector.connect(
			host = 'localhost',
			database= 'northwind',
			user='Sathish',
			password='Sathish@2354'

			)
		if connection.is_connected():
			cursor=connection.cursor()

			insert_query="""UPDATE customers SET CompanyName=%s WHERE CustomerID = %s ;"""

			data= (name,id)

			cursor.execute(insert_query,data)
			connection.commit()
			print("Data  Successfully Updated")

	except Error as e:
		print("MYSQL Error:", e)
		traceback.print_exc()
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MYSQL Conection is closed")
	
def insert_data(id,name):
	try:
		connection =mysql.connector.connect(
			host = 'localhost',
			database= 'northwind',
			user='Sathish',
			password='Sathish@2354'

			)
		if connection.is_connected():
			cursor=connection.cursor()

			insert_query="""INSERT INTO customers (CustomerID, CompanyName) VALUES(%s, %s);"""

			data= (id,name)

			cursor.execute(insert_query,data)
			connection.commit()
			print("Data  Successfully Updated")

	except Error as e:
		print("MYSQL Error:", e)
		traceback.print_exc()
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MYSQL Conection is closed")
			
@app.route('/customer',methods=['GET'])
def get_users_all():
	try:
		connection =mysql.connector.connect(
			host = 'localhost',
			database= 'northwind',
			user='Sathish',
			password='Sathish@2354'

			)
		if connection.is_connected():
			cursor=connection.cursor()
			insert_query="""SELECT * FROM customers"""
			cursor.execute(insert_query)
			result=cursor.fetchall()
			cursor.close()
			
			return jsonify(result)
	except Error as e:
		print("MYSQL Error:", e)
		traceback.print_exc()
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MYSQL Conection is closed")

@app.route('/customer/<string:id>',methods=['GET'])
def get_users(id):
	try:
		connection =mysql.connector.connect(
			host = 'localhost',
			database= 'northwind',
			user='Sathish',
			password='Sathish@2354'

			)
		if connection.is_connected():
			cursor=connection.cursor()
			insert_query="""SELECT * FROM customers where CustomerID=%s"""

			data=([id])
			cursor.execute(insert_query,data)
			result=cursor.fetchall()
			cursor.close()
			
			return jsonify(result)
	except Error as e:
		print("MYSQL Error:", e)
		traceback.print_exc()
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MYSQL Conection is closed")
			

@app.route('/customers_insert',methods=['POST'])
def recived_data_insert():
	try:
		data = request.get_json()
		if data:
			print("Recived data:", data)

			id = data.get('id')
			name = data.get('name')
			print(id,name)

			if id is not None and name is not None:
				insert_data(id,name)
				return jsonify({"message": "Data Recived", "data": data}), 200
			else:
				return jsonify({"error":"Invalid data format"}), 400
		else:
			return jsonify({"error": "No Data Recived"}),400
			
	except Exception as e:
		print("Error:", e)
		traceback.print_exc()
		return jsonify({"error":"Internal server"}), 500
	
@app.route('/customers_update',methods=['POST'])
def recived_data_update():
	try:
		data = request.get_json()
		if data:
			print("Recived data:", data)

			id = data.get('id')
			name = data.get('name')
			print(id,name)

			if id is not None and name is not None:
				update_data(id,name)
				return jsonify({"message": "Data Recived", "data": data}), 200
			else:
				return jsonify({"error":"Invalid data format"}), 400
		else:
			return jsonify({"error": "No Data Recived"}),400
	except Exception as e:
		print("Error:", e)
		traceback.print_exc()
		return jsonify({"error":"Internal server"}), 500






#########################################################ORDER###################################################################
		

def update_order(id,eid,cid):
	connection = None
	cursor = None
	try:
		connection =mysql.connector.connect(
			host = 'localhost',
			database= 'northwind',
			user='Sathish',
			password='Sathish@2354'

			)
		if connection.is_connected():
			cursor=connection.cursor()
			insert_query="""UPDATE orders SET CustomerID=%s, EmployeeID=%s WHERE OrderID = %s ;"""

			data= (cid,eid,id)

			cursor.execute(insert_query,data)
			connection.commit()
			print("Data  Successfully Updated")

	except Error as e:
		print("MYSQL Error:", e)
		traceback.print_exc()
	finally:
		if cursor:
			cursor.close()
		if connection and connection.is_connected():
			connection.close()
			print("MYSQL Conection is closed")
	
def insert_order(id,eid,cid):
	try:
		connection =mysql.connector.connect(
			host = 'localhost',
			database= 'northwind',
			user='Sathish',
			password='Sathish@2354'

			)
		if connection.is_connected():
			cursor=connection.cursor()

			insert_query="""INSERT INTO orders (OrderID, CustomerID,EmployeeID) VALUES(%s, %s,%s);"""

			data= (id,cid,eid)

			cursor.execute(insert_query,data)
			connection.commit()
			print("Data  Successfully ADDED")

	except Error as e:
		print("MYSQL Error:", e)
		traceback.print_exc()
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MYSQL Conection is closed")
			



@app.route('/orders',methods=['GET'])
def get_order_all():
	try:
		connection =mysql.connector.connect(
			host = 'localhost',
			database= 'northwind',
			user='Sathish',
			password='Sathish@2354'

			)
		if connection.is_connected():
			cursor=connection.cursor()
			insert_query="""SELECT * FROM orders"""
			cursor.execute(insert_query)
			result=cursor.fetchall()
			cursor.close()
			
			return jsonify(result)
	except Error as e:
		print("MYSQL Error:", e)
		traceback.print_exc()
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MYSQL Conection is closed")

@app.route('/order/<int:id>',methods=['GET'])
def get_order(id):
	try:
		connection =mysql.connector.connect(
			host = 'localhost',
			database= 'northwind',
			user='Sathish',
			password='Sathish@2354'

			)
		if connection.is_connected():
			cursor=connection.cursor()
			insert_query="""SELECT * FROM orders where OrderID=%s"""

			data=(id)
			cursor.execute(insert_query,data)
			result=cursor.fetchall()
			cursor.close()
			
			return jsonify(result)
	except Error as e:
		print("MYSQL Error:", e)
		traceback.print_exc()
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MYSQL Conection is closed")
			

@app.route('/order_insert',methods=['POST'])
def recived_order_insert():
	try:
		data = request.get_json()
		if data:
			print("Recived data:", data)

			id = data.get('id')
			eid = data.get('eid')
			cid = data.get('cid')
			print(id,eid,cid)

			if id is not None and eid is not None:
				insert_order(id,eid,cid)
				return jsonify({"message": "Data Recived", "data": data}), 200
			else:
				return jsonify({"error":"Invalid data format"}), 400
		else:
			return jsonify({"error": "No Data Recived"}),400
			
	except Exception as e:
		print("Error:", e)
		traceback.print_exc()
		return jsonify({"error":"Internal server"}), 500
	
@app.route('/order_update',methods=['POST'])
def recived_order_update():
	try:
		data = request.get_json()
		if data:
			print("Recived data:", data)

			id = data.get('id')
			eid = data.get('eid')
			cid = data.get('cid')

			if id is not None and eid is not None:
				update_order(id,eid,cid)
				return jsonify({"message": "Data Recived", "data": data}), 200
			else:
				return jsonify({"error":"Invalid data format"}), 400
		else:
			return jsonify({"error": "No Data Recived"}),400
	except Exception as e:
		print("Error:", e)
		traceback.print_exc()
		return jsonify({"error":"Internal server"}), 500

######################################################products##############################################################

def update_products(id,name):
	try:
		connection =mysql.connector.connect(
			host = 'localhost',
			database= 'northwind',
			user='Sathish',
			password='Sathish@2354'

			)
		if connection.is_connected():
			cursor=connection.cursor()

			insert_query="""UPDATE products SET ProductName=%s WHERE ProductID = %s ;"""

			data= (name,id)

			cursor.execute(insert_query,data)
			connection.commit()
			print("Data  Successfully Updated")

	except Error as e:
		print("MYSQL Error:", e)
		traceback.print_exc()
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MYSQL Conection is closed")
	
def insert_products(id,name):
	try:
		connection =mysql.connector.connect(
			host = 'localhost',
			database= 'northwind',
			user='Sathish',
			password='Sathish@2354'

			)
		if connection.is_connected():
			cursor=connection.cursor()

			insert_query="""INSERT INTO products (ProductID, ProductName) VALUES(%s, %s);"""

			data= (id,name)

			cursor.execute(insert_query,data)
			connection.commit()
			print("Data  Successfully Updated")

	except Error as e:
		print("MYSQL Error:", e)
		traceback.print_exc()
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MYSQL Conection is closed")
			
@app.route('/products',methods=['GET'])
def get_products_all():
	try:
		connection =mysql.connector.connect(
			host = 'localhost',
			database= 'northwind',
			user='Sathish',
			password='Sathish@2354'

			)
		if connection.is_connected():
			cursor=connection.cursor()
			insert_query="""SELECT * FROM products"""
			cursor.execute(insert_query)
			result=cursor.fetchall()
			cursor.close()
			
			return jsonify(result)
	except Error as e:
		print("MYSQL Error:", e)
		traceback.print_exc()
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MYSQL Conection is closed")

@app.route('/products/<string:id>',methods=['GET'])
def get_products(id):
	try:
		connection =mysql.connector.connect(
			host = 'localhost',
			database= 'northwind',
			user='Sathish',
			password='Sathish@2354'

			)
		if connection.is_connected():
			cursor=connection.cursor()
			insert_query="""SELECT * FROM products where ProductID=%s"""

			data=([id])
			cursor.execute(insert_query,data)
			result=cursor.fetchall()
			cursor.close()
			
			return jsonify(result)
	except Error as e:
		print("MYSQL Error:", e)
		traceback.print_exc()
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MYSQL Conection is closed")
			

@app.route('/products_insert',methods=['POST'])
def recived_products_insert():
	try:
		data = request.get_json()
		if data:
			print("Recived data:", data)

			id = data.get('id')
			name = data.get('name')
			print(id,name)

			if id is not None and name is not None:
				insert_products(id,name)
				return jsonify({"message": "Data Recived", "data": data}), 200
			else:
				return jsonify({"error":"Invalid data format"}), 400
		else:
			return jsonify({"error": "No Data Recived"}),400
			
	except Exception as e:
		print("Error:", e)
		traceback.print_exc()
		return jsonify({"error":"Internal server"}), 500
	
@app.route('/products_update',methods=['POST'])
def recived_products_update():
	try:
		data = request.get_json()
		if data:
			print("Recived data:", data)

			id = data.get('id')
			name = data.get('name')
			print(id,name)

			if id is not None and name is not None:
				update_products(id,name)
				return jsonify({"message": "Data Recived", "data": data}), 200
			else:
				return jsonify({"error":"Invalid data format"}), 400
		else:
			return jsonify({"error": "No Data Recived"}),400
	except Exception as e:
		print("Error:", e)
		traceback.print_exc()
		return jsonify({"error":"Internal server"}), 500





			

if __name__=='__main__':
	app.run(debug=True)

			
