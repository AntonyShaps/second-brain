from app.domain.model import Category, Project, Task, Note 

def test_category_can_have_project_task_note():
    home_category = Category("Home")
    renovation_project = Project("Renovation", category_id = home_category.id)
    cleaning_task = Task("Cleaning", category_id = home_category.id)
    misc_note = Note("Thoughts", "Thoughts on moving out", category_id = home_category.id)
    
    assert renovation_project.category_id == home_category.id
    assert cleaning_task.category_id == home_category.id
    assert misc_note.category_id == home_category.id
