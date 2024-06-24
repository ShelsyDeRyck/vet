from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

  #########  pets  #########

    @staticmethod
    def read_pets():
        sql = "SELECT * FROM pets"
        data = Database.get_rows(sql)
        return data

    @staticmethod
    def read_pet(pet_id):
        sql = "SELECT * FROM pets WHERE id = %s"
        params = [pet_id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def create_pet(breed, species, name, sterilized, microchip, gender, year_of_birth):
        sql = 'INSERT INTO pets (breed, species, name, sterilized, microchip, gender, year_of_birth) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        params = [breed, species, name, sterilized, microchip, gender, year_of_birth]
        # print(params)
        return Database.execute_sql(sql, params)
    
    @staticmethod
    def update_pet(breed, species, name, sterilized, microchip, gender, year_of_birth, pet_id):
        sql = 'UPDATE pets SET breed = %s, species = %s, name = %s, voornaam = %s, sterilized = %s, microchip = %s, gender = %s, year_of_birth = %s WHERE id = %s'
        params = [breed, species, name, sterilized, microchip, gender, year_of_birth, pet_id]
        return Database.execute_sql(sql, params)

    
    @staticmethod
    def delete_pet(pet_id):
        sql = 'DELETE FROM pets WHERE pet_id = %s'
        params = [pet_id]
        return Database.execute_sql(sql, params)

    #########  users  #########
 
    @staticmethod
    def read_users():
        sql = "SELECT * FROM users"
        data = Database.get_rows(sql)
        return data

    @staticmethod
    def read_user(user_id):
        sql = "SELECT * FROM users WHERE id = %s"
        params = [user_id]
        return Database.get_one_row(sql, params)
    
    @staticmethod
    def create_user(name, last_name, password, email):
        sql = 'INSERT INTO users (name, last_name, password, email) VALUES (%s,%s,%s,%s)'
        params = [name, last_name, password, email]
        return Database.execute_sql(sql, params)
    
    @staticmethod
    def update_user(name, last_name, password, email, user_id):
        sql = 'UPDATE users SET name = %s, last_name = %s, password = %s, email = %s WHERE id = %s'
        params = [name, last_name, password, email, user_id]
        return Database.execute_sql(sql, params)

    @staticmethod
    def delete_user(user_id):
        sql = 'DELETE FROM users WHERE user_id = %s'
        params = [user_id]
        return Database.execute_sql(sql, params)
    
    #########  vets  #########
    
    @staticmethod
    def read_vets():
        sql = "SELECT * FROM vets"
        data = Database.get_rows(sql)
        return data
    
    
    @staticmethod
    def search_vets_available(name, location, type):
        # get all vets with a corresponding name, city or type
        sql = " SELECT DISTINCT v.*, t.* FROM vets v JOIN types t ON v.type_id = t.id WHERE v.name LIKE %s OR v.location LIKE %s OR t.type LIKE %s;"
        params = [f"%{name}%", f"%{location}%", f"{type}"]
        # print("01010101010101010101010")
        # print(Database.get_rows(sql, params))
        return Database.get_rows(sql, params)
    
    @staticmethod
    def read_vet(vet_id):
        sql = "SELECT * FROM vets WHERE id = %s"
        params = [vet_id]
        return Database.get_one_row(sql, params)
    
    @staticmethod
    def create_vet(name, location, description, email, type_id):
        sql = 'INSERT INTO vets (name, location, description, email, type_id) VALUES (%s,%s,%s,%s,%s)'
        params = [name, location, description, email, type_id]
        return Database.execute_sql(sql, params)
    
    @staticmethod
    def update_vet(name, last_name, password, email, vet_id):
        sql = 'UPDATE vets SET name = %s, last_name = %s, password = %s, email = %s WHERE id = %s'
        params = [name, last_name, password, email, vet_id]
        return Database.execute_sql(sql, params)
    
    @staticmethod
    def delete_vet(vet_id):
        sql = 'DELETE FROM vets WHERE vet_id = %s'
        params = [vet_id]
        return Database.execute_sql(sql, params)
    
    #########  types  #########
    @staticmethod
    def read_types():
        # print("read types")
        sql = "SELECT * FROM types"
        data = Database.get_rows(sql)
        return data
    
    @staticmethod
    def read_type(type_id):
        sql = "SELECT * FROM types WHERE id = %s"
        params = [type_id]
        return Database.get_one_row(sql, params)