from flask import Flask, request, jsonify
import mysql.connector

# Database connection details
db_config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "your_database_name"
}

app = Flask(__name__)

# Helper function to connect to database
def get_connection():
  connection = mysql.connector.connect(**db_config)
  return connection

# Function to close connection
def close_connection(connection):
  if connection:
    connection.close()

# -------------------- User Endpoints --------------------

@app.route("/api/users", methods=["GET", "POST"])
def user_crud():
  connection = get_connection()
  cursor = connection.cursor()

  # GET: Get all users
  if request.method == "GET":
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    response = {"data": users}
  
  # POST: Create a new user
  elif request.method == "POST":
    data = request.get_json()
    sql = "INSERT INTO users (name, last_name, password, email) VALUES (%s, %s, %s, %s)"
    values = (data["name"], data["last_name"], data["password"], data["email"])
    cursor.execute(sql, values)
    connection.commit()
    response = {"message": "User created successfully!"}

  cursor.close()
  close_connection(connection)
  return jsonify(response)

@app.route("/api/users/<int:user_id>", methods=["GET", "PUT", "DELETE"])
def user_by_id(user_id):
  connection = get_connection()
  cursor = connection.cursor()

  # GET: Get a user by ID
  if request.method == "GET":
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    if user:
      response = {"data": user}
    else:
      response = {"message": "User not found!"}

  # PUT: Update a user
  elif request.method == "PUT":
    data = request.get_json()
    sql = """
      UPDATE users
      SET name = %s, last_name = %s, password = %s, email = %s
      WHERE id = %s
    """
    values = (data["name"], data["last_name"], data["password"], data["email"], user_id)
    cursor.execute(sql, values)
    connection.commit()
    response = {"message": "User updated successfully!"}

  # DELETE: Delete a user
  elif request.method == "DELETE":
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    connection.commit()
    response = {"message": "User deleted successfully!"}

  cursor.close()
  close_connection(connection)
  return jsonify(response)

# -------------------- Pet Endpoints --------------------

@app.route("/api/pets", methods=["GET", "POST"])
def pet_crud():
  connection = get_connection()
  cursor = connection.cursor()

  # GET: Get all pets
  if request.method == "GET":
    cursor.execute("SELECT * FROM pets")
    pets = cursor.fetchall()
    response = {"data": pets}
  
  # POST: Create a new pet
  elif request.method == "POST":
    data = request.get_json()
    sql = """
      INSERT INTO pets (breed, species, name, sterilized, microchip, gender, year_of_birth)
      VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (data["breed"], data["species"], data["name"], data["sterilized"], data["microchip"], data["gender"], data["year_of_birth"])
    cursor.execute(sql, values)
    connection.commit()
    response = {"message": "Pet created successfully!"}

  cursor.close()
  close_connection(connection)
  return jsonify(response)

# ... previous code ...

@app.route("/api/pets/<int:pet_id>", methods=["GET", "PUT", "DELETE"])
def pet_by_id(pet_id):
  connection = get_connection()
  cursor = connection.cursor()

  # GET: Get a pet by ID
  if request.method == "GET":
    cursor.execute("SELECT * FROM pets WHERE id = %s", (pet_id,))
    pet = cursor.fetchone()
    if pet:
      response = {"data": pet}
    else:
      response = {"message": "Pet not found!"}

  # PUT: Update a pet
  elif request.method == "PUT":
    data = request.get_json()
    sql = """
      UPDATE pets
      SET breed = %s, species = %s, name = %s, sterilized = %s, microchip = %s, gender = %s, year_of_birth = %s
      WHERE id = %s
    """
    values = (data["breed"], data["species"], data["name"], data["sterilized"], data["microchip"], data["gender"], data["year_of_birth"], pet_id)
    cursor.execute(sql, values)
    connection.commit()
    response = {"message": "Pet updated successfully!"}

  # DELETE: Delete a pet
  elif request.method == "DELETE":
    cursor.execute("DELETE FROM pets WHERE id = %s", (pet_id,))
    connection.commit()
    response = {"message": "Pet deleted successfully!"}

  cursor.close()
  close_connection(connection)
  return jsonify(response)

# -------------------- Vet Endpoints --------------------

@app.route("/api/vets", methods=["GET", "POST"])
def vet_crud():
  connection = get_connection()
  cursor = connection.cursor()

  # GET: Get all vets
  if request.method == "GET":
    cursor.execute("SELECT * FROM vets")
    vets = cursor.fetchall()
    response = {"data": vets}
  
  # POST: Create a new vet
  elif request.method == "POST":
    data = request.get_json()
    sql = """
      INSERT INTO vets (name, description, location, email, type_id)
      VALUES (%s, %s, %s, %s, %s)
    """
    values = (data["name"], data["description"], data["location"], data["email"], data["type_id"])
    cursor.execute(sql, values)
    connection.commit()
    response = {"message": "Vet created successfully!"}

  cursor.close()
  close_connection(connection)
  return jsonify(response)

@app.route("/api/vets/<int:vet_id>", methods=["GET", "PUT", "DELETE"])
def vet_by_id(vet_id):
  connection = get_connection()
  cursor = connection.cursor()

  # GET: Get a vet by ID
  if request.method == "GET":
    cursor.execute("SELECT * FROM vets WHERE id = %s", (vet_id,))
    vet = cursor.fetchone()
    if vet:
      response = {"data": vet}
    else:
      response = {"message": "Vet not found!"}

  # PUT: Update a vet
  elif request.method == "PUT":
    data = request.get_json()
    sql = """
      UPDATE vets
      SET name = %s, description = %s, location = %s, email = %s, type_id = %s
      WHERE id = %s
    """
    values = (data["name"], data["description"], data["location"], data["email"], data["type_id"], vet_id)
    cursor.execute(sql, values)
    connection.commit()
    response = {"message": "Vet updated successfully!"}

  # DELETE: Delete a vet
  elif request.method == "DELETE":
    cursor.execute("DELETE FROM vets WHERE id = %s", (vet_id,))
    connection.commit()
    response = {"message": "Vet deleted successfully!"}

  cursor.close()
  close_connection(connection)
  return jsonify(response)

if __name__ == "__main__":
  app.run(debug=True)

