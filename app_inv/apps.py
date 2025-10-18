from django.apps import AppConfig


class AppInvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_inv'
    

    def ready(self):
        import app_inv.signals.free_plan_signal