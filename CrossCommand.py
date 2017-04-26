import sublime, sublime_plugin

class CrossCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    
    for region in self.view.sel():
      if region.empty():
        line = self.view.line(region)

      self.view.insert(edit, region.begin(), chr(215))

  def is_enabled(self):
    return self.view != None


  def description(self):
    return "Cross: Insert a cross mark to cross something out..."
