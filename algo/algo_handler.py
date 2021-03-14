import algo.caesar as caesar
import algo.frequency_analysis as frequency
import algo.vigenere as vigenere


def handle(parameters):
    algo = parameters.get("algo")
    shift = parameters.get("decalage")
    clear_text = parameters.get("texte")
    key = parameters.get("cle")
    cryted_text = parameters.get("crypte")
    action = parameters.get("action")
    frequency_list = []
    if (action == None or action.strip() == ""):
        return ("Une action doit être définie ou des champs sont manquants.", "", frequency_list, False, action)
    if(algo == "frequence" and action != "analyse"):
        return ("Afin de procéder à l'analyse fréquentielle, veuillez sélectionner l'algorithme 'Analyse fréquentielle' en haut de la page et sélectionner 'Analyse fréquentielle' en bas de la page.", "", frequency_list, False, action)
    if action == "chiffrer" and (clear_text == None or clear_text.strip() == ""):
        return ("Le champ texte en clair ne doit pas être vide. Si vous souhaitez faire une simple analyse sélectionner le radio bouton 'Analyse'", "", frequency_list, False, action)
    if action == "dechiffer" and (cryted_text == None or cryted_text.strip() == ""):
        return ("Le champ texte crypté/chiffré ne doit pas être vide. Si vous souhaitez faire une simple analyse sélectionner le radio bouton 'Analyse'", "", frequency_list, False, action)
    if action == "analyse" and (clear_text == None or clear_text.strip() == ""):
        return ("Pour l'analyse, le champ de texte en clair ne doit pas être vide.", "", frequency_list, False, action)

    # Fin des cas d'erreurs
    if algo == "cesar":
        if shift == None or not isinstance(shift, int):
            return ("Dans le cadre du chiffrement de César, le décalage doit être un nombre entier !", "", frequency_list, False, action)
        else:
            is_action_to_encrypt = (action == "chiffrer")
            if is_action_to_encrypt:
                cryted_text = caesar.encrypt_or_decrypt(
                    clear_text, int(shift), True)
            else:
                clear_text = caesar.encrypt_or_decrypt(
                    cryted_text, int(shift), False)
    elif algo == "frequence":
        frequency_list = frequency.frequency(clear_text)
    elif algo == "vigenere":
        if (key == None or key.strip() == ""):
            return ("Dans le cadre de l'algorithme de Vigenère, la clé doit être renseignée !", "", frequency_list, False, action) 
        is_action_to_encrypt = (action == "chiffrer")
        if is_action_to_encrypt:
            cryted_text = vigenere.encrypt_or_decrypt_mathematically(clear_text, key, True)
        else:
            clear_text = vigenere.encrypt_or_decrypt_mathematically(cryted_text, key, False)

    return (clear_text, cryted_text, frequency_list, True, action)
