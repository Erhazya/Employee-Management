import mysql.connector 
import logs

try:
    config = {
        'user': 'admin',
        'password': 'Azertyuiop$1',
        'host': '109.89.241.235',
        'port': '3306',
        'database': 'Employes_Informations',
        'raise_on_warnings': True
    }

    conn = mysql.connector.connect(**config)

    cursor = conn.cursor()
except mysql.connector.Error as err:
    logs.logging.error('Employes Informations : Erreur de connexion à la base de données : ' + format(err) + str(config))



def add_employes(id=100000, name="test", firstname="test", phone="2323233", address="add", diplome=0, salary=122):

    query = "INSERT INTO employes (id, name, firstname, phone, address, diplome, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (id, name, firstname, phone, address, diplome, salary)
    
    cursor.execute(query, values)
    result = cursor.fetchone()
    conn.commit()
    
    

def del_employes(id):
    query = "DELETE FROM employes WHERE id = %s"
    values = (id)
    
    cursor.execute(query, values)
    conn.commit()
    




def list_employes():
    """
    Vérifie si le nom d'utilisateur existe dans la base de données.

    Args:
        username (str): Le nom d'utilisateur à vérifier.

    Returns:
        tuple: Un tuple contenant un booléen indiquant si le nom d'utilisateur est valide et l'ID associé.
    """

    query = "SELECT * FROM employes ORDER BY name"
    cursor.execute(query)
    result = cursor.fetchall()
    return result
    





def update_employes(name, firstname, phone, address, diplome, salary, id):
    query = "UPDATE employes SET name = %s, firstname = %s, phone = %s, address = %s, diplome = %s, salary = %s WHERE id = %s "
    cursor.execute(query, (name,firstname,phone,address,diplome,salary,id))
    conn.commit()












