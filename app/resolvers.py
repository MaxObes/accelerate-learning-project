from typing import List
from app.models import Teacher, Student, Assignment, Score
from app.database import SessionLocal

db = SessionLocal()

# Query Resolvers
def resolve_all_teachers(_: str, info) -> List[Teacher]:
    return db.query(Teacher).all()

def resolve_all_students(_: str, info) -> List[Student]:
    return db.query(Student).all()

def resolve_all_assignments(_: str, info) -> List[Assignment]:
    return db.query(Assignment).all()

def resolve_get_assignment_by_id(_: str, id: int) -> Assignment:
    return db.query(Assignment).filter_by(id=id).first()

# Mutation Resolvers
def resolve_create_assignment(_: str, info, teacherId: int, title: str, description: str = None) -> Assignment:
    assignment = Assignment(title=title, description=description, teacher_id=teacherId)
    db.add(assignment)
    db.commit()
    return assignment

def resolve_add_score(_: str, info, studentId: int, assignmentId: int, score: int) -> Score:
    score_record = Score(student_id=studentId, assignment_id=assignmentId, score=score)
    db.add(score_record)
    db.commit()
    return score_record

def resolve_remove_assignment(_: str, info, id: int) -> bool:
    assignment = db.query(Assignment).filter_by(id=id).first()
    if assignment:
        db.delete(assignment)
        db.commit()
        return True
    return False

def resolve_remove_score(_: str, info, id: int) -> bool:
    score = db.query(Score).filter_by(id=id).first()
    if score:
        db.delete(score)
        db.commit()
        return True
    return False