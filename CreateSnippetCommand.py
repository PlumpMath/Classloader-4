import sublime, sublime_plugin
import os

class CreateSnippetCommand(sublime_plugin.TextCommand):

  saveOnCreate = False

  def run(self, edit):
    # get the selection
    self.content = self.getSelectionContent(edit);

    if not self.content:
      return;

    # get as much information to prefill some snippet information
    self.getInfo()

    # create content for the snippet
    snippet = self.getSnippet();

    # open a new file
    self.newSnippet()

    # insert the string
    self.view.insert(edit, 0, snippet)

    # position the cursor to edit the content of the 

    pos = sublime.Region(30, 30 + len(self.content))
    self.view.sel().clear()
    self.view.sel().add(pos)

    # either before or after this, or between, trigger a dialog to choose a package and tell to save
    self.showPackageList()

  def getSelectionContent(self, edit):
    for region in self.view.sel():
      content = self.view.substr(region)
      if len(content) != 0:
        return content
    return False;

  def getInfo(self):
    file = self.view.file_name()
    if file:
      self.ext = file[file.rfind(".") + 1:]
    else:
      self.ext = ''
    self.firstword = self.content[0:self.content.find(" ")]
    if self.content.find(" ") == -1:
      self.firstword = self.content


  def getSnippet(self):
    return "<snippet>\n\t<content><![CDATA[" + self.content.lower() + "]]></content>\n\t<tabTrigger>" + self.firstword.lower() + "</tabTrigger>\n\t<scope>source." + self.ext+ "</scope>\n\t<description>" + self.firstword[0:1].upper() + self.firstword[1:].lower() + "</description>\n</snippet>"

  def newSnippet(self):
    self.view = sublime.active_window().new_file();
    # set the syntax to XML
    self.view.set_syntax_file("Packages/XML/XML.tmLanguage")

  def saveSnippet(self):
    self.view.run_command("save")

  def getPackageList(self):
    # get a list of packages from sublime's package folder
    self.path = sublime.packages_path()

    self.packageList = []
    for dir in os.listdir(self.path):
      if os.path.isdir(os.path.join(self.path, dir)):
        self.packageList.append(dir)

  def showPackageList(self):
    self.getPackageList();
    sublime.status_message("Choose a package for the new snippet.")
    sublime.active_window().show_quick_panel(self.packageList, self.choosePackage)

  def choosePackage(self, index):

    if index != -1:
      self.snippet_filename = os.path.join(self.path, self.packageList[index], self.firstword + ".sublime-snippet")
      self.view.retarget(self.snippet_filename)
      if self.saveOnCreate:
         self.saveSnippet()
    else:
      sublime.status_message("No package selected for the new snippet.")
    
  def is_enabled(self):
    return self.view != None

  def description(self):
    return "Snippet: Create Snippet from selection"
