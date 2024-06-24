from repositories.DataRepository import DataRepository
from flask import Flask, jsonify, request
from flask_cors import CORS

# Start app
app = Flask(__name__)
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})
CORS(app)

# Custom endpoint
# endpoint = '/api'



# ROUTES

# -------------------- User Endpoints --------------------

@app.route("/api/users/", methods=["GET", "POST"])
def user_crud():
  # GET: Get all users
  if request.method == "GET":
    return jsonify(users = DataRepository.read_users()),200
  
  # POST: Create a new user
  elif request.method == "POST":
    data = DataRepository.json_or_formdata(request)
    new_id = DataRepository.create_user(data['name'], data['last_name'], data['password'], data['email'])
    return jsonify(message = "User created successfully!", id = new_id), 201

@app.route("/api/users/<int:user_id>", methods=["GET", "PUT", "DELETE"])
def user_by_id(user_id):
  # GET: Get a user by ID
  if request.method == "GET":
    return jsonify(user = DataRepository.read_user(user_id))
  # PUT: Update a user
  elif request.method == "PUT":
    data = DataRepository.json_or_formdata(request)
    values = DataRepository.update_user(data['name'], data['last_name'], data['password'], data['email'], user_id)
    # print(values)
    return jsonify(user_id = user_id), 200
  # DELETE: Delete a user
  elif request.method == "DELETE":
    data = DataRepository.delete_user(user_id)
    if data > 1:
      return jsonify(message = "User deleted successfully!"), 200
    else:
      return jsonify(message = "User not found!"), 404
  
  
  # -------------------- pets Endpoints --------------------
  
@app.route("/api/pets/", methods=["GET", "POST"])
def pet_crud():
  # GET: Get all pets
  if request.method == "GET":
    return jsonify(pets = DataRepository.read_pets()),200
  
  # POST: Create a new pet
  elif request.method == "POST":
    data = DataRepository.json_or_formdata(request)
    # print(data)
    new_id = DataRepository.create_pet(data['breed'], data['species'], data['name'], data['sterilized'], data['microchip'], data['gender'], data['year_of_birth'])
    return jsonify(message = "Pet created successfully!", id = new_id), 201

  # elif request.method == "POST":
  #   data = DataRepository.json_or_formdata(request)
  #   new_id = DataRepository.create_pet(data['breed'], data['species'], data['name'], data['sterilized'], data['microchip'], data['gender'], data['year_of_birth'])
  #   return jsonify(message = "Pet created successfully!", id = new_id), 201

@app.route("/api/pets/<int:pet_id>", methods=["GET", "PUT", "DELETE"])
def pet_by_id(pet_id):
  # GET: Get a pet by ID
  if request.method == "GET":
    return jsonify(pet = DataRepository.read_pet(pet_id))
  # PUT: Update a pet
  elif request.method == "PUT":
    data = DataRepository.json_or_formdata(request)
    values = DataRepository.update_pet(data['breed'], data['species'], data['name'], data['sterilized'], data['microchip'], data['gender'], data['year_of_birth'], pet_id)
    # print(values)
    return jsonify(pet_id = pet_id), 200
  # DELETE: Delete a pet
  elif request.method == "DELETE":
    data = DataRepository.delete_pet(pet_id)
    if data > 1:
      return jsonify(message = "Pet deleted successfully!"), 200
    else:
      return jsonify(message = "Pet not found!"), 404
  

  # -------------------- vets Endpoints --------------------
@app.route('/api/vets/search/', methods=['GET'])
def vet_searchd(data):
    # print("-+-+-+-+-+-+-")
    # print(request.args)
    try:
        # data = DataRepository.json_or_formdata(request)
        result = DataRepository.search_vets_available(data['name'], data['location'], data['type'])
        return jsonify(result), 200

    except KeyError as e:
        # Handle missing keys if necessary
        return jsonify({"error": f"Missing parameter: {str(e)}"}), 400

    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500
  
@app.route("/api/vets/", methods=["GET", "POST"])
def vet_crud():
  # GET: Get all vets
  if request.method == "GET":
    return jsonify(vets = DataRepository.read_vets()),200
  
  # POST: Create a new vet
  elif request.method == "POST":
    data = DataRepository.json_or_formdata(request)
    new_id = DataRepository.create_vet(data['name'], data['description'], data['location'], data['email'], data['type_id'])
    return jsonify(message = "Vet created successfully!", id = new_id), 201

@app.route("/api/vets/<int:vet_id>", methods=["GET", "PUT", "DELETE"])  
def vet_by_id(vet_id):
  # GET: Get a vet by ID
  if request.method == "GET":
    return jsonify(vet = DataRepository.read_vet(vet_id))
  # PUT: Update a vet
  elif request.method == "PUT":
    data = DataRepository.json_or_formdata(request)
    values = DataRepository.update_vet(data['name'], data['description'], data['location'], data['email'], data['type_id'], vet_id)
    # print(values)
    return jsonify(vet_id = vet_id), 200
  # DELETE: Delete a vet
  elif request.method == "DELETE":
    data = DataRepository.delete_vet(vet_id)
    if data > 1:
      return jsonify(message = "Vet deleted successfully!"), 200
    else:
      return jsonify(message = "Vet not found!"), 404
  
   # -------------------- types Endpoints --------------------
   
# @app.route("/api/types", methods=["GET"])
# def type_crud():
# # GET: Get all types
#   if request.method == "GET":
#     return jsonify(types = DataRepository.read_types()),200
    
# @app.route("/api/types/<int:vet_id>", methods=["GET"])  
# def vet_by_id(vet_id):
#   # GET: Get a vet by ID
#   if request.method == "GET":
#     return jsonify(vet = DataRepository.read_vet(vet_id))

@app.route("/api/types/", methods=["GET"])
def get_types():
    # GET: Get all types
    # print(DataRepository.read_types())
    if request.method == "GET":
        response = jsonify(types=DataRepository.read_types()), 200
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return response
      
@app.route("/api/types/<int:type_id>", methods=["GET"])
def get_type_by_id(type_id):
    # GET: Get a vet by ID
    if request.method == "GET":
        response = jsonify(type=DataRepository.read_type(type_id)), 200
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return response

if __name__ == '__main__':
  app.run(port=5000)
  # app.run(host='0.0.0.0', port=5000)
