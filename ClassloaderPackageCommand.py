import sublime, sublime_plugin

class ClassloaderPackageCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    
    namespace = self.getNamespace()

    if (not namespace):
      return

    for region in self.view.sel():
      if region.empty():
        line = self.view.line(region)

        line_contents = self.view.substr(line)

        if (line_contents.find("Package") != -1):
          self.view.replace(edit, region, namespace)

  def is_enabled(self):
    return self.view != None

  def getNamespace(self):
    filename = self.view.file_name()

    # if not filename:
    #   self.view.window().show_input_panel("Please provide a fully qualified namespace", "", self.is_enabled, self.is_enabled, self.is_enabled)


    # on Windows paths contains backward slashes
    filename = filename.replace("\\", "/")

    # start and end index
    comindex = filename.find('/com/')
    lastslashindex = filename.rfind("/")

    if (comindex == -1):
      return False

    # get folder structure  
    package = filename[comindex + 1:lastslashindex]

    # replace slashes with dots
    return package.replace("/",".")


  def description(self):
    return "Classloader: Insert package namespace "
