from pathlib import Path
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from database import get_db
from models import Project
from schemas import ProjectCreate, ProjectOut, ProjectUpdate, Status, Topic


app = FastAPI(title="Country Digital Project Tracker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
BASE_DIR = Path(__file__).parent
@app.post("/projects", response_model=ProjectOut, status_code=201)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    new_project = Project(**project.model_dump())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project
@app.get("/projects", response_model=list[ProjectOut])
def list_projects(
    country: Optional[str] = None,
    status: Optional[Status] = None,
    topic: Optional[Topic] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Project)

    if country:
        query = query.filter(Project.country == country)
    if status:
        query = query.filter(Project.status == status)
    if topic:
        query = query.filter(Project.topic == topic)

    return query.all()
@app.get("/projects/{project_id}", response_model=ProjectOut)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.get(Project, project_id)

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
@app.put("/projects/{project_id}", response_model=ProjectOut)
def update_project(
    project_id: int, project: ProjectUpdate, db: Session = Depends(get_db)
):
    saved_project = db.get(Project, project_id)

    if saved_project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    update_data = project.model_dump(exclude_unset=True)

    for field_name, new_value in update_data.items():
        setattr(saved_project, field_name, new_value)

    db.commit()
    db.refresh(saved_project)
    return saved_project
@app.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.get(Project, project_id)

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()
    return {"message": "Project deleted successfully"}
@app.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    total_projects = db.query(Project).count()

    by_status = {}
    for status_name in ["Not Started", "Ongoing", "Completed", "Delayed"]:
        by_status[status_name] = (
            db.query(Project).filter(Project.status == status_name).count()
        )

    return {"total_projects": total_projects, "by_status": by_status}
@app.get("/", include_in_schema=False)
def serve_dashboard_page():
    index_file = BASE_DIR / "index.html"

    if index_file.exists():
        return FileResponse(index_file)

    return {"message": "API is running. The dashboard page index.html is not added yet."}
@app.get("/style.css", include_in_schema=False)
def serve_style_file():
    style_file = BASE_DIR / "style.css"

    if style_file.exists():
        return FileResponse(style_file, media_type="text/css")

    raise HTTPException(status_code=404, detail="style.css is not added yet")
@app.get("/app.js", include_in_schema=False)
def serve_javascript_file():
    javascript_file = BASE_DIR / "app.js"

    if javascript_file.exists():
        return FileResponse(javascript_file, media_type="application/javascript")

    raise HTTPException(status_code=404, detail="app.js is not added yet")
