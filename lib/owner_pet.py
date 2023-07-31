class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.owner = owner

        if pet_type not in Pet.PET_TYPES:
            raise TypeError("Pet type must be valid")
        Pet.all.append(self)
        self.pet_type = pet_type


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if  not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet Class")
        pet.owner = self

    def get_sorted_pets(self):
        pets_by_name = {pet.name: pet for pet in Pet.all if pet.owner == self}
        sorted_names = sorted(pets_by_name.keys())

        sorted_pets = [pets_by_name[name] for name in sorted_names]
        return sorted_pets