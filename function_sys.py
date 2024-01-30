# ------AtlantaVR bot------ #
#   By : helias5605
# ------------------------- #

from main import *
from db_handler import *

store = False


def enregistrer_evenement(auteur, id, date, roles, name):
    try:
        cur, conn = initialiser_db()
        enregistrer_evenement(cur, conn, auteur, id, date, roles, name)
        return "L'événement a été créé avec succées !"

    except FileExistsError as e:
        return "Erreur lors de la création du fichier\nMerci de me signaler l'erreur → **helias5605**"


async def button_confirmation(interaction):
    await interaction.response.send_message("Merci, j'ai bien enregistré les rôles !")
    store = True
    passed = True


async def button_annulation(interaction):
    await interaction.response.send_message("D'accord, les réponses n'ont pas été prise en compte")
    store = False
    passed = True
