"""
Écrire une fonction transcription_arn(brin_codant)
qui reçoit une chaîne de caractères en paramètre, correspondant à un brin codant d'ADN,
et qui retourne la chaîne de caractère représentant le brin d' ARN correspondant.".
"""
def transcription_arn(chaine_adn):
    chaine_adn = chaine_adn.replace("T", "U")
    return chaine_adn
  
transcription_arn('AGTCTTACCGATCCAT') #'AGUCUUACCGAUCCAU'
