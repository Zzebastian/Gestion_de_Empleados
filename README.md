# Gestion_de_Empleados
The practical work consists of 6 files (including this one):

database.py: a database backup, which consists of a script capable of re-generating the original database.

gestion_empleados.db: the database on which the program operates.

PantallasTkinter.py: the program where the graphical interface is created, on which the user works. It has two keys: {"admin": "123456"} and {"": "") that allow automatic login. The passwords are stored as hashes, as the file was shared through Replit and that application makes it public to everyone. This can be bypassed by modifying line 703 of the code, replacing _Inicial() with _Seleccion().

funcionesBdD.py: a set of functions that operate on the database. It was done this way because they were created and tested individually and in parallel to the construction of the Tkinter screens.

Resumen.csv: a sample of the exportable file generated by the program, where you can see in detail how the capability to extract data from the program to an external file works.

NOTE: Although the loading of overtime hours is enabled, the system does not display them on the Month Detail screen. This is mainly due to aesthetic and time-related issues.
