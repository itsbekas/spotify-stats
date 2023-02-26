class BaseRepository:
    def __init__(self, model_cls):
        self.model_cls = model_cls

    def create(self, **kwargs):
        obj = self.model_cls(**kwargs)
        obj.save()
        return obj

    def get_by_id(self, obj_id):
        return self.model_cls.objects(id=obj_id).first()

    def get_all(self):
        return self.model_cls.objects()

    def update(self, obj_id, **kwargs):
        obj = self.get_by_id(obj_id)
        if not obj:
            return None
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    def delete(self, obj_id):
        obj = self.get_by_id(obj_id)
        if not obj:
            return False
        obj.delete()
        return True
