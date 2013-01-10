import sublime, sublime_plugin

class ClassloaderClassCompletionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    filename = self.view.file_name()
    comindex = filename.find('/com/') + 1
    lastslashindex = filename.rfind("/")

    packagename = filename[comindex:lastslashindex].replace("/",".")

    if(packagename[0:3] != "com"):
      return

    package = False;
    sels = self.view.sel()  
    for region in self.view.sel():
      if region.empty():
        line = self.view.line(region)

        line_contents = self.view.substr(line)

        if(line_contents.find("Package") != -1):
          print(region, "insert ", packagename, "in selection")
          self.view.insert(edit, 9, packagename)

  def description(self):
    return "A description"
