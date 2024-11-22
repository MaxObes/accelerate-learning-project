import strawberry
from typing import List
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.resolvers import (
    resolve_all_teachers,
    resolve_all_students,
    resolve_all_assignments,
    resolve_get_assignment_by_id,
    resolve_create_assignment,
    resolve_add_score,
    resolve_remove_assignment,
    resolve_remove_score,
)
from app.models import Teacher, Student, Assignment, Score

# Strawberry Type Definitions
@strawberry.type
class Teacher:
    id: int
    name: str
    email: str


@strawberry.type
class Student:
    id: int
    name: str
    email: str


@strawberry.type
class Assignment:
    id: int
    title: str
    description: str
    teacher: Teacher


@strawberry.type
class Score:
    id: int
    student: Student
    assignment: Assignment
    score: int
    created_at: str
    updated_at: str


# Strawberry Query Type
@strawberry.type
class Query:
    all_teachers: List[Teacher] = strawberry.field(resolver=resolve_all_teachers)
    all_students: List[Student] = strawberry.field(resolver=resolve_all_students)
    all_assignments: List[Assignment] = strawberry.field(resolver=resolve_all_assignments)
    get_assignment_by_id: Assignment = strawberry.field(resolver=resolve_get_assignment_by_id)


# Strawberry Mutation Type
@strawberry.type
class Mutation:
    create_assignment: Assignment = strawberry.mutation(resolver=resolve_create_assignment)
    add_score: Score = strawberry.mutation(resolver=resolve_add_score)
    remove_assignment: bool = strawberry.mutation(resolver=resolve_remove_assignment)
    remove_score: bool = strawberry.mutation(resolver=resolve_remove_score)


# Build Strawberry Schema
schema = strawberry.Schema(query=Query, mutation=Mutation)

# FastAPI Application
app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)