Classloader
===========

Sublime Text 2 commands, snippets and plugins for writing Classloader JavaScript code and a few other commands that I find convenient.

##Commands:
I've added some commands to Sublime, some with shortcuts.

###ClassloaderPackageCommand
Fills out the package namespace when on the "Package" line of a (saved) file.

###ClassloaderMoveClassCommand 
Move and/or a class and fix all references that other classes have to it.

###CreateSnippetCommand 
Takes selected text to create a new snippet and asks your for a package to save the file to.

###PromptCommand
Opens up shell command prompt. Easy if you want to do something with a file on the command line.

###MarkedCommand
Opens up the file in Marked, as long as the file is a MarkDown file and as long as Marked is available. Currently only works on OS-X, since Marked is only available there. It could possibly be updated with a configuration to work with different applications on different operating systems.



##Code Completion:

###ClassloaderClassCompletion 
Suggests namespaces and classes for "Package" lines, "Import" and "Extends". The code understand when Import and Extends statements run over multiple lines.

##Snippets

###Package, Extends and Import
Very simple single line statements. It's just a little quicker.

###Class
Take the filename as the Class name, and writes out the constructor.

###Component, Command, Query
Take the filename as the Class name, and writes out extends statement, resource statements and the constructor, and sometimes the main method of the class.

###Static and Static Anonymous
Writes out 'static' methods for a class

##Theme
The package included my prefered theme, modified with my preferences.
