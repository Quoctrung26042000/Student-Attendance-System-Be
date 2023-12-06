from typing import Optional

from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.school import GradeInDB, ClassInDB


class GradeRepository(BaseRepository):
    async def create_grade(
        self,
        *,
        grade_name: str,
    ) -> GradeInDB:
        grade = GradeInDB(grade_name=grade_name)
        async with self.connection.transaction():
            grade_row = await queries.create_new_grade(
                self.connection,
                grade_name=grade.grade_name,
            )
        return grade.copy(update=dict(grade_row))
    


    