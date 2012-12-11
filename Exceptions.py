class MultipleInstanceException(Exception):
    def __str__(self):
        return "An instance of this object has already been saved to the \
         database, run picklmonger.update() to modify the class"

if __name__ == "__main__":
    raise MultipleInstanceException()


class MultipleModelException(Exception):
    def __str__(self):
        return "A model with the same name is already in \
        the database, rename the model you are trying to save"


class NoInstanceException(Exception):
    def __str__(self):
        return "There is no model instance with this instanceName \
        in the database"

if __name__ == "__main__":
    raise MultipleInstanceException()
