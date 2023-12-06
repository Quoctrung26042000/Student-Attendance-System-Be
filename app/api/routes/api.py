from fastapi import APIRouter

from app.api.routes import authentication, comments, profiles, tags, users, teacher, school
from app.api.routes.articles import api as articles

router = APIRouter()
router.include_router(authentication.router, tags=["authentication"], prefix="/account")
router.include_router(teacher.router, tags=["School Manager"], prefix="/school")
router.include_router(school.router, tags=["School Manager"], prefix="/school")
# router.include_router(users.router, tags=["users"], prefix="/user")
# router.include_router(profiles.router, tags=["profiles"], prefix="/profiles")
# router.include_router(articles.router, tags=["articles"])
# router.include_router(
#     comments.router,
#     tags=["comments"],
#     prefix="/articles/{slug}/comments",
# )
# router.include_router(tags.router, tags=["tags"], prefix="/tags")
