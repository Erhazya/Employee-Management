import mysql.connector
import logs

config = {}
conn = mysql.connector.connect(**config)

try:
    config = {
        'user': 'admin',
        'password': 'Azertyuiop$1',
        'host': '109.89.241.235',
        'port': '3306',
        'database': 'User_Informations',
        'raise_on_warnings': True
    }

    conn = mysql.connector.connect(**config)

    cursor = conn.cursor()
except mysql.connector.Error as err:
    logs.logging.error('Erreur de connexion à la base de données : ' + format(err) + str(config))


def check_username(username):
    """
    Vérifie si le nom d'utilisateur existe dans la base de données.

    Args:
        username (str): Le nom d'utilisateur à vérifier.

    Returns:
        tuple: Un tuple contenant un booléen indiquant si le nom d'utilisateur est valide et l'ID associé.
    """
    print("Vérification de l'utilisateur")
    query = "SELECT * FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        if row[1] == username:
            print("Valide")
            return True, row[0]
    print("Nom d'utilisateur invalide")
    return False, None


def check_password(password):
    """
    Vérifie si le mot de passe existe dans la base de données.

    Args:
        password (str): Le mot de passe à vérifier.

    Returns:
        tuple: Un tuple contenant un booléen indiquant si le mot de passe est valide et l'ID associé.
    """
    print("Vérification du mot de passe")
    query = "SELECT * FROM passwords"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        if row[1] == password:
            print("Valide")
            return True, row[2]
    print("Mot de passe invalide")
    return False, None


def connect(username_entry=None, password_entry=None):
    """
    Fonction de connexion à la base de données.

    Args:
        username_entry (str): Le nom d'utilisateur saisi.
        password_entry (str): Le mot de passe saisi.

    Returns:
        bool: True si la connexion est réussie, False sinon.
    """
    username = username_entry
    password = password_entry

    username_result = check_username(username)
    password_result = check_password(password)

    if username_result[0] and password_result[0] and username_result[1] == password_result[1]:
        print("Connexion validée")
        return True
    else:
        print("Connexion impossible")
        return False
