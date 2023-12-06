from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from app.api.dependencies.database import get_repository
from app.core.config import get_app_settings
from app.core.settings.app import AppSettings
from app.db.errors import EntityDoesNotExist
from app.db.repositories.school import GradeRepository
from app.models.schemas.school import (
    GradeInCreate,
    GradeInRepository,
    ClassInCreate
)
from app.resources import strings
from app.services import jwt
from app.services.authentication import check_email_is_taken, check_username_is_taken

router = APIRouter()


@router.post(
    "/create_grade",
    status_code=HTTP_201_CREATED,
    response_model=GradeInRepository,
    name="register:grade",
)
async def register_teacher(
    grade_create: GradeInCreate = Body(..., embed=True, alias="grade"),
    grade_repo: GradeRepository = Depends(get_repository(GradeRepository)),
) -> GradeInRepository:
    grade_created = await grade_repo.create_grade(**grade_create.dict())
    return GradeInRepository(
        grade_name = grade_created.grade_name
    )

