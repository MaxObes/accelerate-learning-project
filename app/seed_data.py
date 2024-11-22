from app.models import Base, Teacher, Student, Assignment, Score
from app.database import engine, SessionLocal

def populate_data():
    # Initialize the database
    Base.metadata.create_all(bind=engine)

    # Start a session
    db = SessionLocal()

    # Add teachers
    teacher1 = Teacher(name="John Doe", email="john.doe@school.com")
    teacher2 = Teacher(name="Jane Smith", email="jane.smith@school.com")
    db.add_all([teacher1, teacher2])
    db.commit()

    # Add students
    student1 = Student(name="Alice", email="alice@student.com")
    student2 = Student(name="Bob", email="bob@student.com")
    db.add_all([student1, student2])
    db.commit()

    # Add assignments
    assignment1 = Assignment(title="Math Test", description="Algebra Problems", teacher_id=teacher1.id)
    assignment2 = Assignment(title="Science Quiz", description="Physics Questions", teacher_id=teacher2.id)
    db.add_all([assignment1, assignment2])
    db.commit()

    # Add scores
    score1 = Score(student_id=student1.id, assignment_id=assignment1.id, score=85)
    score2 = Score(student_id=student2.id, assignment_id=assignment1.id, score=90)
    db.add_all([score1, score2])
    db.commit()

    print("Database has been populated with sample data!")

if __name__ == "__main__":
    populate_data()