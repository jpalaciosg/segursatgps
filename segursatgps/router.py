class DBRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'locations':
            return 'history_db'
        if model._meta.app_label == 'alerts':
            return 'history_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'locations':
            return 'history_db'
        if model._meta.app_label == 'alerts':
            return 'history_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'locations' or obj2._meta.app_label == 'locations':
            return True
        elif 'locations' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        if obj1._meta.app_label == 'alerts' or obj2._meta.app_label == 'alerts':
            return True
        elif 'alerts' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'locations':
            return db == 'history_db'
        if app_label == 'alerts':
            return db == 'history_db'
        return None