from tortoise import Model, fields

class FamilyMember(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    parent_id = fields.IntField(null=True)

    class Meta:
        table = "family_member"