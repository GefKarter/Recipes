from rest_framework import routers
from .api import *


router = routers.DefaultRouter()
router.register('api/recipe', RecipeViewset, 'dish_recipes')


urlpatterns = router.urls
