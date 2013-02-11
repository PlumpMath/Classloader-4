Classloader
===========

Sublime Text 2 snippets and plugins for writing Classloader code and a few other commands that I find useful.

##Commands:

###ClassloaderPackageCommand
Fills out the package namespace when on the "Package" line of a (saved) file.

###ClassloaderMoveClassCommand 
Move and/or a class and fix all references that other classes have to it.

###CreateSnippetCommand 
Takes selected text to create a new snippet and asks your for a package to save the file to.

###PromptCommand
Opens up shell command prompt. Easy if you want to do something with a file on the command line.

##Code Completion:

###ClassloaderClassCompletion 
Suggests namespaces and classes for "Package" lines, "Import" and "Extends". The code understand when Import and Extends statements run over multiple lines.

##Snippets

###Package, Extends and Import
Very simple single line statements. It's just a little quicker.

###Class
Take the filename as the Class name, and writes out the constructor.

###Static and Static Anonymous
Writes out 'static' methods for a class
