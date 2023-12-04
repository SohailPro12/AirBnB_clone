<h1>  AirBnB clone - The console </h1>

<hr />
<img src="/images/console.png" border="0">

<h2> Description </h2>
This is the first step towards building your first full web application: the **AirBnB clone**.
The aim of the project is to deploy a replica of the [Airbnb Website](https://www.airbnb.com/) using my server. The final version of this project will have:
- ```A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)```
- ```A website (front-end) with static and dynamic functionalities```
- ```A comprehensive database to manage the backend functionalities```
- ```An API that provides a communication interface between the front and backend of the system.```

## Table of Contents
---
* Objetives
* Requeriments
* Installation and execution
* Console commands and Usage
* Tests
* Development environment
* Authors

## Objectives
---
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Requeriments
---
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* Your code should use the pycodestyle (version 2.8.*)

## Installation and execution 🔧
---
* Clone the repository
> $ git clone https://github.com/SohailPro12/AirBnB_clone.git
* Move in to the directory
> $ cd AirBnB_clone
* Execute the console file
> /AirBnB_clone$ ./console.py

## Console commands and Usage
---
The commands available for this command interpreter are:

| Name       | Description   | Usage |
| ---------- | ------------- | ----- |
| **create** | Creates a new instance of the class passed by argument. | `create <class_name>` |
| **show**   | Prints the string representation of an instance. | `show <class_name> <object_id>; <class_name>.show(<object_id>)()` |
| **destroy**| Deletes an instance that was already created. | `destroy <class_name> <object_id>; <class_name>.destroy(<object_id>)()` |
| **all**    | Prints string representation of all instances or of all instances of a specified class. | `all <class_name>; <class_name>.all()` |
| **update** | Updates an instance attribute if exists otherwise create it. | `update <class_name> <object_id> <attribute name> "<attribute value>"; <class_name>.update(<object_id>, <attribute name>, <attribute value>); <class_name>.update(<object_id>, <dictionary representation>)` |
| **help**   | Show all commands or display information about a specific command. | `help; help <command_name>` |
| **quit**   | Exit the console. | `quit` |
| **EOF**    | Exit the console. | `EOF; (ctrl + d)` |

**create, destroy and update commands save changes into a JSON file.**

## Tests ⚙️
---
Coming soon.

## Development environment 🛠️
This project has been tested on Ubuntu 22.04 LTS

* Programming language : Python 3
* Development environment manager vagrant
* Style guidelines: Google Style Python Docstrings
* Python style guide checker  : PycodeStyle

## AUTHORS✒️
---

* [SOHAIL CHAREF](https://github.com/SohailPro12/)  - LinkedIn profile (https://www.linkedin.com/in/sohail-charef/)
* [Mohamed Chatr](https://github.com/Mochatr/) -  LinkedIn profile (https://www.linkedin.com/in/mochatr/)
