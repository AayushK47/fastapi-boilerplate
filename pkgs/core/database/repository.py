from tortoise import Tortoise
from tortoise.models import Model

class DBRepository:
    def __init__(self, db: Tortoise, model: Model) -> None:
        self._db = db
        self._model = model
    

    async def all(self):
        return await self._model.all(using_db=self._db).values()


    async def create(self, data):
        return await self._model.create(using_db=self._db, **data)

    async def create_or_update(self, data):
        return await self._model.update_or_create(
            data, 
            using_db=self._db
        )

    async def get_where(self, filter):
        return await self._model.filter(**filter).values()

    async def first_where(self, filter):
        return await self._model.filter(**filter).first()

    async def exists(self, filter):
        return await self._model.filter(**filter).count()

    async def bulk_insert(self, data):
        return await self._model.bulk_create(data, using_db=self._db)
    
    async def update_where(self, filter, data):
        return await self._model.filter(**filter).update(**data)

    async def delete_where(self, filter):
        return await self._model.filter(filter).delete()