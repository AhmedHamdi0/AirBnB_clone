#!/usr/bin/python3

import cmd

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

CLASSES = {
    "BaseModel": BaseModel,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = '(hbnb) '
    storage = FileStorage()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)."""
        print("")
        return True

    def do_create(self, args):
        """Create a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return

        new_instance = CLASSES[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        if not args:
            print("** class name missing **")
            return
        class_name, _, instance_id = args.partition(' ')
        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return
        if not instance_id:
            print("** instance id missing **")
            return

        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        class_name, _, instance_id = args.partition(' ')
        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return
        if not instance_id:
            print("** instance id missing **")
            return

        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """Prints all string representations of instances"""
        if args:
            class_name, _, _ = args.partition(' ')
            if class_name not in CLASSES:
                print("** class doesn't exist **")
                return

            instances = [str(instance) for key, instance
                         in storage.all().items()
                         if key.split('.')[0] == class_name]
        else:
            instances = [str(instance) for instance in storage.all().values()]

        print(instances)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]
        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        key = f"{class_name}.{instance_id}"

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args_list) < 3:
            print("** attribute name missing **")
            return

        attr_name = args_list[2]
        if len(args_list) < 4:
            print("** value missing **")
            return

        attr_value_str = args_list[3]
        try:
            attr_value = eval(attr_value_str)
        except NameError:
            attr_value = attr_value_str

        setattr(storage.all()[key], attr_name, attr_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
