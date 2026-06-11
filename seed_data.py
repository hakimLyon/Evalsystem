import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluation_system.settings')
django.setup()

from evaluations.models import Group, WeightConfig

if not WeightConfig.objects.exists():
    WeightConfig.objects.create(
        name="Default Config",
        student_weight=20,
        tutor_weight=40,
        invited_weight=40,
        tutor_password="tutor2024",
        invited_password="invited2024",
    )

if not Group.objects.exists():
    for i in range(1, 7):
        Group.objects.create(name=f"Group {i}", description=f"Presentation group {i}")

print("Seed done: config + 6 groups")
