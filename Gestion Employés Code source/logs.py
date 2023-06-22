import logging

# Configuration du niveau de journalisation
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Création d'un gestionnaire de journalisation de fichier
file_handler = logging.FileHandler('./logs/log.txt')

# Configuration du format du gestionnaire de fichier
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Ajout du gestionnaire de fichier au journal
logging.getLogger().addHandler(file_handler)

# Exemples de messages de journalisation
#logging.debug('Ceci est un message de débogage')
#logging.info('Ceci est un message informatif')
#logging.warning('Ceci est un avertissement')
#logging.error('Ceci est une erreur')
#logging.critical('Ceci est une erreur critique')
