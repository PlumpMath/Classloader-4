import sublime, sublime_plugin
import os
import fnmatch

class ClassloaderClassCompletion(sublime_plugin.EventListener):
  """Looks through folders starting from a 'com' folder to find namespaces and classes for Classloader code"""
  
  def __init__(self): 
    self.view = sublime.active_window().active_view()

    self.getNamespaces()
    self.getClasses()

  def writingPackage(self):
    for region in self.view.sel():
      line = self.view.line(region)
      line_contents = self.view.substr(line)

      return (line_contents.find("Package") != -1)

  def getNamespaces(self):
    root = self.getComFolder();

    namespaces = []
    for path in self.getList(root, False):
      path = self.convertPath(path)
      namespaces.append((path, path))

    return namespaces

  def getClasses(self):
    root = self.getComFolder();

    classes = []
    for path in self.getList(root, True):
      path = self.convertPath(path)
      classes.append((path, path))

    return classes

  def getList(self, root, includeFiles):
    matches = []
    if (root):
      for root, dirnames, filenames in os.walk(root):        
        if (includeFiles):
          for filename in fnmatch.filter(filenames, '*.js'):
            matches.append(os.path.join(root, filename).replace("\\", "/"))
        else:
          for dirname in dirnames:
            matches.append(os.path.join(root, dirname).replace("\\", "/"))

    return matches  

  def convertPath(self, path):
    returnvalue = "";
    if (path.find(".js") != -1):
      returnvalue = path[path.find("/com/")+1:path.find(".js")]
    else:
      returnvalue = path[path.find("/com/")+1:]

    return returnvalue.replace("/", ".")


  def getComFolder(self):
    filename = self.view.file_name()

    # on Windows paths contains backward slashes
    filename = filename.replace("\\", "/")

    # start and end index
    comindex = filename.find('/com/')

    if (comindex == -1):
      return False

    # get folder structure  
    package = filename[0:comindex + 5]

    return package

  def on_query_completions(self, view, prefix, locations):
    self.view = view
    #self.getNamespaces()

    if(self.writingPackage()):
      sugs = self.getNamespaces()
    else:
      sugs = self.getClasses()
    
    return sugs
