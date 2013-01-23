Classloader
===========

Sublime Text 2 snippets and plugins for writing Classloader code and a few other commands that I find useful.

##Snippets:
- Class
- Extends
- Import
- Package
- Static function

##Commands:

###ClassloaderPackageCommand
Fills out the package namespace when on the "Package" line of a (saved) file.

###ClassLoaderRefactorCommand 
Takes selected text to create a new snippet and asks your for a package to save the file to.

###CreateSnippetCommand 
Takes selected text to create a new snippet and asks your for a package to save the file to.

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
