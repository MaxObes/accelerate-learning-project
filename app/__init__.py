# app/__init__.py
from .database import Base, engine, SessionLocal
from .models import Teacher, Student, Assignment, Score

__all__ = ["Base", "engine", "SessionLocal", "Teacher", "Student", "Assignment", "Score"]