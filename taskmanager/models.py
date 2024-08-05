from taskmanager import db

class Category(db.Model):
    # schema for the category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
                    # max string length of 25, must be unique string, cannot be empty field
    
    # establish replationship for using ondelete for category_id in "Tasks"
    # identifies relationship with "tasks" table, backreferences the categorys, cascades delete to all tasks
    # lazy=True means anythime query a category it simultaneously identifies any task linked to that category
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)
    

    def __repr__(self):
        # __repr__ is used to represent itself in the form of a string, similar to 'this' in JS
        return self.category_name



class Task(db.Model):
    # schema for the task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
                    # max string length of 50, must be unique string, cannot be empty field
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
                    # ondelete="CASCADE" means if category is deleted the deletion is cascaded to all tasks within the category
                    # if this was not present, all tasks with this categroy would give an error when category deleted


    def __repr__(self):
        # __repr__ is used to represent itself in the form of a string, similar to 'this' in JS
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        ) # alternatively, could use f"#{self.id} - Task:{self.task_name}|Urgent:{self.is_urgent}"