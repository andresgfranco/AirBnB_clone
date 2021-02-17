# 0x00. AirBnB clone - The console
---
![first](https://camo.githubusercontent.com/59589bd21e8ec09ef94f2d9bb80d36d144bc487fe4737f8b213d005f3273921b/68747470733a2f2f696d6775722e636f6d2f4f696c457358562e706e67)

## Description
This project was created for learning purposes at Holberton School.
Hoblerton AirBnB clone is a full web application; this repo only includes the back-end *console of the app
#### *The Console:
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”.
![second](https://scontent.fctg1-2.fna.fbcdn.net/v/t1.0-9/151880839_2920562224888119_911837572075069119_o.jpg?_nc_cat=106&ccb=3&_nc_sid=730e14&_nc_ohc=13gKv4FhRqIAX94webt&_nc_ht=scontent.fctg1-2.fna&oh=2e3b461d379ae148d2888bc274d1b4e7&oe=605219EF)

---
### Resources
###### Read or watch:
- [HBNB_Project_overview]
- [Unittest]
- [cmd_module]
- [JSON]
- [AirBnB_Website]
---

### Files and Directories
- ```models``` directory will contain all classes used for the entire project.
- ```tests``` directory will contain all unit tests.
- ```console.py``` file is the entry point of our command interpreter.
- ```models/base_model.py``` file is the base class of all our models.
- ```models/engine``` directory will contain all storage classes (using the same prototype).
---
### Tasks

##### 0. README, AUTHORS mandatory
Write a ```README.md```
You should have an ```AUTHORS``` file at the root of your repository, - listing all individuals having contributed content to the repository.

##### 1. Be PEP8 compliant!
Write beautiful code that passes the PEP8 checks.

##### 2. Unittests
All your files, classes, functions must be tested with unit tests

##### 3. BaseModel
Write a class ```BaseModel``` that defines all common attributes/methods for other classes:
- ```models/base_model.py```
- Public instance attributes:
    - ```id```: string - assign with an ```uuid``` when an instance is created:
        - the goal is to have unique ```id``` for each ```BaseModel```
    - ```created_at```: datetime - assign with the current datetime when an instance is created
    - ```updated_at```: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
- ```__str__```: should print: ```[<class name>] (<self.id>) <self.__dict__>```
- Public instance methods:
    - ```save(self)```: updates the public instance attribute ```updated_at``` with the current datetime
    - ```to_dict(self)```: returns a dictionary containing all keys/values of ```__dict__``` of the instance:

##### 4. Create BaseModel from dictionary 
Update ```models/base_model.py```:
- ```__init__(self, *args, **kwargs)```:
    - if ```kwargs``` is not empty:
        - each key of this dictionary is an attribute name (Note ```__class__``` from ```kwargs``` is the only one that should not be added as an attribute.)
        - each value of this dictionary is the value of this attribute name
    - otherwise:
        - create ```id``` and ```created_at``` as you did previously (new instance)

##### 5. Store first object
Write a class ```FileStorage``` that serializes instances to a JSON file and deserializes JSON file to instances:
- ```models/engine/file_storage.py```
- Private class attributes:
    - ```__file_path```: string - path to the JSON file (ex: ```file.json```)
    - ```__objects```: dictionary - empty but will store all objects by ```<class name>.id``` (ex: ```BaseModel.12121212```)
- Public instance methods:
    - ```all(self)```: returns the dictionary ```__objects```
    - ```new(self, obj)```: sets in ```__objects``` the ```obj``` with key ```<obj class name>.id```
    - ```save(self)```: serializes ```__objects``` to the JSON file.
    - ```reload(self)```: deserializes the JSON file to ```__objects```

Update ```models/__init__.py```: to create a unique ```FileStorage``` instance for your application
- import ```file_storage.py```
- create the variable ```storage```, an instance of ```FileStorage```
- call ```reload()``` method on this variable

Update ```models/base_model.py```: to link your ```BaseModel``` to ```FileStorage``` by using the variable ```storage```
- import the variable ```storage```
- in the method ```save(self)```:
    - call ```save(self)``` method of ```storage```
- ```__init__(self, *args, **kwargs):```
    - if it’s a new instance, add a call to the method ```new(self)``` on ```storage```

##### 6. Console 0.0.1
Write a program called ```console.py``` that contains the entry point of the command interpreter:
- You must use the module ```cmd```
- Your class definition must be: ```class HBNBCommand(cmd.Cmd):```
- Your command interpreter should implement:
    - ```quit``` and ```EOF``` to exit the program
    - ```help``` (this action is provided by default by cmd)
    - a custom prompt: ```(hbnb)```
    - an empty line + ```ENTER``` shouldn’t execute anything
- Your code should not be executed when imported

##### 7. Console 0.1 
Update your command interpreter (```console.py```) to have these commands:
- ```create```: Creates a new instance of ```BaseModel```, saves it (to the JSON file) and prints the ```id```. Ex: ```$ create BaseModel```
- ```show```: Prints the string representation of an instance based on the class name and ```id```. Ex: ```$ show BaseModel 1234-1234-1234```.
- ```destroy```: Deletes an instance based on the class name and ```id``` (save the change into the JSON file). Ex: ```$ destroy BaseModel 1234-1234-1234```.
- ```all```: Prints all string representation of all instances based or not on the class name. ```Ex: $ all BaseModel``` or ```$ all```.
- ```update```: Updates an instance based on the class name and ```id``` by adding or updating attribute (save the change into the JSON file). ```Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"```.
    - Usage: ```update <class name> <id> <attribute name> "<attribute value>"```
    - Only one attribute can be updated at the time

##### 8. First User
Write a class ```User``` that inherits from ```BaseModel```:
- ```models/user.py```
- Public class attributes:
    - ```email```: string - empty string
    - ```password```: string - empty string
    - ```first_name```: string - empty string
    - ```last_name```: string - empty string

Update ```FileStorage``` to manage correctly serialization and deserialization of ```User```.
Update your command interpreter (```console.py```) to allow ```show```, ```create```, ```destroy```, ```update``` and ```all``` used with ```User```.

##### 9. More classes!
Write all those classes that inherit from ```BaseModel```:
| Class | Public class attributes |
|-------|-------------------------|
| ```State``` (```models/state.py```) | ```name``` |
| ```City``` (```models/city.py```) | ```state_id```, ```name``` |
| ```Amenity``` (```models/amenity.py```) | ```name``` |
| ```Place``` (```models/place.py```) | ```city_id```, ```user_id```, ```name```, ```description```, ```number_rooms```, ```number_bathrooms```, ```max_guest```, ```price_by_night```, ```latitude```, ```longitude```, ```amenity_ids``` |
| ```Review``` (```models/review.py```) | ```place_id```, ```user_id```, ```text``` |

##### 10. Console 1.0 
Update ```FileStorage``` to manage correctly serialization and deserialization of all our new classes: ```Place```, ```State```, ```City```, ```Amenity``` and ```Review```
Update your command interpreter (```console.py```) to allow those actions: ```show```, ```create```, ```destroy```, ```update``` and ```all``` with all
classes created previously.

_*Enjoy your first console!*_

---

## Authors
- [Adrian Vides] | [Twitter] | [GitHub]
- [Andrés Gonzalez] | [Twitter.] | [GitHub.]



[HBNB_Project_overview]: <https://youtu.be/E12Xc3H2xqo>
[Unittest]: <https://docs.python.org/3.4/library/unittest.html#module-unittest>
[cmd_module]: <https://docs.python.org/3.4/library/cmd.html>
[AirBnB_Website]: <https://intranet.hbtn.io/rltoken/FrRTcvuF5L9wWDzFE9k01A>
[JSON]: <https://docs.python.org/3.4/library/json.html>

---

[GitHub]: <https://github.com/AdrianVides56>
[Twitter]: <https://twitter.com/termi56661>
[Adrian Vides]: <https://www.linkedin.com/in/adrian-felipe-vides-jimenez-a201401b7> 
[GitHub.]: <https://www.linkedin.com/in/andresgfranco>
[Twitter.]: <https://twitter.com/andresgfranco>
[Andrés Gonzalez]: <https://github.com/andresgfranco>

