from django.db import models
from ipray.models import IPrayUser

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(IPrayUser, on_delete=models.CASCADE, related_name='created_communities')

    def __str__(self):
        return self.name

    def get_members(self):
        members = []
        for membership in self.members.all():
            members.append({
                'user_id': membership.user.id,
                'email': membership.user.email,
                'device_token': membership.device_token,
                'role': membership.role,
                })
        return members


class Membership(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
    ]

    user = models.ForeignKey(IPrayUser, on_delete=models.CASCADE, related_name='memberships')
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='members')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    device_token = models.CharField(max_length=255, blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'community')

    def __str__(self):
        return f"{self.user.email} - {self.community.name} ({self.role})"

    def promote_to_admin(self):
        self.role = 'admin'
        self.save()

    def demote_to_member(self):
        self.role = 'member'
        self.save()


    @classmethod
    def create_membership(cls, user, community, role='member'):
        # Try to fetch the user's device token
        device = user.devices.last()  # Assuming you want to use the most recent device
        device_token = device.token if device else None

        membership, created = cls.objects.get_or_create(
            user=user,
            community=community,
            defaults={'role': role, 'device_token': device_token}
        )

        if not created and membership.device_token != device_token:
            membership.device_token = device_token
            membership.save()

        return membership