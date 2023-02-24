# AirBnB Clone

This project is an implementation of a command-line interface for an Airbnb clone application. The application allows users to create, update and delete objects in a simulated Airbnb database.

## Command Interpreter (Console Function)

The command interpreter is a CLI that allows users to interact with the Airbnb clone application. It provides a command-line interface for users to enter commands, which are then processed and executed by the interpreter. The interpreter reads user input, processes it, and displays the appropriate output.

## How to Start the Command Interpreter

To start the command interpreter, clone the repository and navigate to the project directory. Then, run the command:
```
$ ./console.py
```
This will start the command interpreter and display a prompt indicating that it is ready to receive user input.

## How to Use the Command Interpreter

To use the command interpreter, enter commands at the prompt and press enter. The interpreter will then process the command and display the appropriate output.

The available commands include:

- `create` - create a new object
- `show` - display information about an object
- `destroy` - delete an object
- `all` - display information about all objects
- `update` - update an object's information

For a full list of commands and their usage, enter the command `help` at the prompt.

## Examples

Here are some examples of how to use the command interpreter:
```
$ ./console.py
(hbnb) create User
7d257547-0516-47f6-820f-95b44d05b9ea
(hbnb) show User 7d257547-0516-47f6-820f-95b44d05b9ea
[User] (7d257547-0516-47f6-820f-95b44d05b9ea) {'id': '7d257547-0516-47f6-820f-95b44d05b9ea', 'created_at': datetime.datetime(2023, 2, 24, 10, 0, 0, 0), 'updated_at': datetime.datetime(2023, 2, 24, 10, 0, 0, 0)}
(hbnb) update User 7d257547-0516-47f6-820f-95b44d05b9ea name "John Doe"
(hbnb) show User 7d257547-0516-47f6-820f-95b44d05b9ea
[User] (7d257547-0516-47f6-820f-95b44d05b9ea) {'id': '7d257547-0516-47f6-820f-95b44d05b9ea', 'created_at': datetime.datetime(2023, 2, 24, 10, 0, 0, 0), 'updated_at': datetime.datetime(2023, 2, 24, 10, 0, 0, 0), 'name': 'John Doe'}
(hbnb) all User
[[User] (7d257547-0516-47f6-820f-95b44d05b9ea) {'id': '7d257547-0516-47f6-820f-95b44d05b9ea', 'created_at': datetime.datetime(2023, 2, 24, 10, 0, 0, 0), 'updated_at': datetime.datetime(2023, 2, 24, 10,
```
