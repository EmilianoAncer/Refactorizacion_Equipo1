# Building project locally

Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment. Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements

    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src

# How to run

1. Navigate to src forder
2. Run main.py file

   > python main.py

3. To regenerate the report delete existing one.

# SOLID Principle

1. Dependency Inversion Principle: System functionality is partitioned into components. For example: csv_utils is only used to parse the csv file and each of the report generators is its own component.

2. Open Closed Principle: System task are distributed in diferent functions, as can be seen in each of the report generators, all tasks have been split into their own function block.

3. Interface Segregation Principle: Because the system has been segregated, fucntions do not depend on each other, if we have an error we would know where the problem is and thanks to that we can fix it right away.

# Design Patterns

1. Facade: As we can see on main.py we are able to generate both the reports by only calling 2 functions from each, this makes it extremly simple to build the report at any point in the code without having to paste in a big block of code when needing to.

2. Builder: In both of the reports generators builders are used to run the code step by step, this makes it easy to track what the code us doing and in case of errors we can debug it easily.
