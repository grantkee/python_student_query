class Student:
  def __init__(self, name, major, major_id, gpa):
    self.name = name
    self.major = major
    self.major_id = major_id
    self.gpa = gpa

  # ids: ["STEM", "Art", "Business", "English"]

  def on_honor_roll(self):
    if self.gpa >= 3.5:
      return True
    else:
      return False

  # def field_of_study(self, ids):
  #   if self.major_id in ids
  #     return self.name
    