import sublime, sublime_plugin
import os

class ClassloaderRefactorCommand(sublime_plugin.TextCommand):

  def run(self, edit):

    # get a list of folders

    # suggest the list and prompt to move

    # prompt to rename

    # move/rename the file

    # rewrite package line

    # rewrite classname (could be tricky)

    # find other files referencing the old class

    # open these files and rewrite the references

    pass

  def getClassInfo(self):
    self.className = ""
    self.packageName = ""