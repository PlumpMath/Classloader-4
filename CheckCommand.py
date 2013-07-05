import sublime, sublime_plugin

class CheckCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    
    print "hello"
    for region in self.view.sel():
      if region.empty():
        line = self.view.line(region)

      self.view.insert(edit, region.begin(), unichr(10003)) 

  def is_enabled(self):
    return self.view != None


  def description(self):#
    return "Check: Insert a check mark to check something..."
