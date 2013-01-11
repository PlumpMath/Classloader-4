import sublime, sublime_plugin

class ClassloaderClassCompletionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    
    namespace = self.getNamespace()
    if (!namespace):
      return

    sels = self.view.sel()  
    for region in self.view.sel():
      if region.empty():
        line = self.view.line(region)

        line_contents = self.view.substr(line)

        if (line_contents.find("Package") != -1):
          print(region, "insert ", packagename, "in selection")
          self.view.insert(edit, 9, packagename)

  def getNamespace(self):
    filename = self.view.file_name()

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
    return "A description"
