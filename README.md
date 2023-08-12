# 0x00. AirBnB Clone - The Console

Welcome to the AirBnB Clone project! In this repository, you will find the codebase for building a simplified version of the AirBnB web application. The primary objective of this project is to develop a command-line interface (CLI) that allows you to manage various AirBnB objects.

## Background Context

The AirBnB Clone project serves as the foundation for creating a web application that emulates some of the features provided by Airbnb. This initial phase of the project focuses on developing a command interpreter, which is a CLI tool that facilitates the management of AirBnB objects. These objects include Users, States, Cities, Places, and more. This command interpreter will be instrumental in the subsequent phases of the project, such as database storage, API integration, and front-end development.

## Project Overview

The project can be broken down into several key components:

1. **BaseModel Class**: You will implement a parent class called `BaseModel`, which handles the initialization, serialization, and deserialization of instances. This class forms the basis for all other classes in the project.

2. **Serialization Flow**: You will establish a serialization flow that involves converting instances to dictionaries, JSON strings, and files. This flow ensures that objects can be stored and retrieved effectively.

3. **AirBnB Object Classes**: You will create classes for various AirBnB objects, such as Users, States, Cities, Places, etc. All of these classes will inherit from the `BaseModel` class and will share common functionalities.

4. **File Storage Engine**: The project will include an abstracted storage engine known as "File storage." This engine will handle the storage and retrieval of data related to AirBnB objects.

5. **Unit Testing**: To ensure the correctness of your code, you will write unit tests using the `unittest` module. These tests will validate the functionality of classes and the storage engine.

## Learning Objectives

By completing this project, the following learning objectives are achieved:

- Creating Python packages to organize and structure your code.
- Building a command interpreter using the `cmd` module, allowing to manage AirBnB objects through the terminal.
- Implementing unit tests to validate the code's functionality.
- Demonstrating serialization and deserialization of classes to facilitate data storage and retrieval.
- Utilizing JSON files for data storage and exchange.
- Managing datetime objects for accurate timestamping.
- Understanding and using UUIDs (Universally Unique Identifiers).
- Handling arguments in functions using `*args` and `**kwargs`.

## Getting Started

1. Review the provided resources to understand the concepts involved.
2. Explore the existing codebase and directory structure.
3. Start by implementing the `BaseModel` class and the command interpreter.
4. As working on the project, make use of the knowledge gained about serialization, file storage, and unit testing.
## Project Structure

- The project directory contains the various modules and files necessary for the AirBnB Clone project.
- The `models` directory will host the classes representing AirBnB objects.
- The `engine` directory will include the file storage and related functionality.
- The `tests` directory contains unit tests for different parts of the project.

## Running the Command Interpreter

To run the command interpreter:
- navigate to the project directory 
- and execute the main script:

```bash
./console.py
```

Once the interpreter is running, you can use various commands:
to create, retrieve, update, and delete AirBnB objects.

## Acknowledgments

This project provides an excellent opportunity to :
solidify Python skills,
gain practical experience in developing a command interpreter,
managing complex object hierarchies.
