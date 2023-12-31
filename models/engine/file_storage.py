import json

class FileStorage:
    __file_path = "file.json"  # Asegúrate de que el nombre del archivo sea el correcto
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        objects_dict = {}
        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(objects_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                objects_dict = json.load(file)

            for key, obj_dict in objects_dict.items():
                class_name, obj_id = key.split('.')
                obj = eval(class_name)(**obj_dict)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass  # No hagas nada si el archivo no existe

