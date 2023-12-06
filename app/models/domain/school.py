from typing import Optional

from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.rwmodel import RWModel


class GradeInDB(RWModel, IDModelMixin, DateTimeModelMixin):
    grade_name: str

class ClassInDB(RWModel, IDModelMixin, DateTimeModelMixin):
    class_name: str
    grade_id : int