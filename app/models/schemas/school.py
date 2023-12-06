from typing import Optional, List

from pydantic import BaseModel, EmailStr, HttpUrl

from app.models.domain.school import GradeInDB, ClassInDB
from app.models.schemas.rwschema import RWSchema



class GradeInCreate(RWSchema):
    grade_name:str

class GradeInRepository(GradeInCreate):
    pass


class ClassInCreate(ClassInDB):
    pass