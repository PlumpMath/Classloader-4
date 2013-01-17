import sublime, sublime_plugin
import os

class PromptCommand(sublime_plugin.ApplicationCommand):
  
  WINDOWS = "windows"
  MAC     = "mac?"

  def run(self):

    # get location of current file
    location = self.getLocation()

    # go to location
    os.chdir(location)

    # print(os.environ["OS"])

    if (os.environ["OS"].lower().find(self.WINDOWS) != -1):
      os.system("C:\Windows\System32\cmd.exe")
    elif (False):
      os.system("gnome-terminal")
    else:
      sublime.status_message("PromptCommand could not run since it does not know what terminal to use on this os.")


  def is_enabled(self):
    return True

  def getLocation(self):

    view = sublime.active_window().active_view()

    filename = view.file_name()

    # on Windows paths contains backward slashes
    filename = filename.replace("\\", "/")

    # end index
    lastslashindex = filename.rfind("/")

    # get folder structure  
    location = filename[0:lastslashindex]

    # replace slashes with dots
    return location


  def description(self):
    return "Prompt: open a shell prompt for the current file location"

