from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.ninjas_model import Ninja

class Dojo:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.list_of_ninjas = []

    # grab all the dojos and its info
    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM dojos"

        result = connectToMySQL(DATABASE).query_db( query )

        list_of_dojos = []
        for row in result:
            list_of_dojos.append( cls(row) )
        return list_of_dojos
    
    # add a dojo into the database
    @classmethod
    def add_dojo(cls, data):
        query = """
            INSERT INTO dojos( name )
            VALUES (%(name)s)
        """

        result = connectToMySQL(DATABASE).query_db( query, data)
        return result

    # gets 1 dojo with its current ninjas, also creates a list of ninjas
    @classmethod
    def get_one_with_ninjas( cls, data ):
        query = """
            SELECT *
            FROM dojos d LEFT JOIN ninjas n
            ON d.id = n.dojo_id
            WHERE d.id = %(dojo_id)s
        """

        result = connectToMySQL( DATABASE ).query_db( query, data )
        current_dojo = cls( result[0] )
        # iterates through the object and creates a list of ninjas to be stored
        for row in result:
            if row['n.id'] != None:
                current_ninja = {
                    'id' : row['n.id'],
                    'dojo_id' : row['dojo_id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'age' : row['age'],
                    'created_at' : row['n.created_at'],
                    'updated_at' : row['n.updated_at']
                }
                current_dojo.list_of_ninjas.append( (Ninja(current_ninja) ) )
        return current_dojo