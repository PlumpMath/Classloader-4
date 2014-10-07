import sublime, sublime_plugin
import os
import os.path
import sys
import subprocess

class MarkedCommand(sublime_plugin.ApplicationCommand):
  
  WINDOWS = "windows"
  MAC     = "darwin"

  def run(self):

    # get current file
    filename = self.getFile()

    if filename:
      if (sys.platform == self.MAC):
        subprocess.call(["/usr/bin/open -a Marked " + filename], shell=True)
      else:
        sublime.status_message("MarkedCommand could not run because Marked is not known on this OS.")


  def is_enabled(self):
    return True

  def getFile(self):

    view = sublime.active_window().active_view()

    filename = view.file_name()

    if os.path.splitext(filename)[1] == ".md":
      return filename
    else:
      return False

  def description(self):
    return "Marked: open a MarkDown file with Marked"

