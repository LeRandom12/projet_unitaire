class UserInterface:
    def error_choice(self, error_message: str) -> int:
        """
        Retourne :
        0 -> ignorer l'erreur
        1 -> toujours ignorer
        2 -> stopper l'opération
        """
        return 2  # valeur par défaut