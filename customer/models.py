from django.db import models
from frame.models import BaseModel


class Customer(BaseModel):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phone = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    @classmethod
    def get_config(cls):
        return {
            "model_name": "Customer",
            "list_title": "Customers",
            "create_title": "Create Customer",
            "enable_search": True,
            "default_sort_by": "created_at",
            "list_url": "customer-list",
            "navigation": True,
            "fields": [
                {
                    "name": "customer_id",
                    "display_name": "Customer Id",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "name",
                    "display_name": "Name",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "email",
                    "display_name": "Email",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "phone",
                    "display_name": "Phone",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "created_at",
                    "display_name": "Created At",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
                {
                    "name": "updated_at",
                    "display_name": "Updated At",
                    "enable_in_list": True,
                    "enable_in_detail": True,
                    "enable_in_form": True,
                },
            ],
            "actions": {
                "button": [
                    {
                        "name": "Create",
                        "url": "customer-create",
                        "disabled": [
                            "detail",
                        ],
                    },
                ],
                "dropdown": [
                    {
                        "name": "Details",
                        "url": "customer-detail",
                        "disabled": [
                            "detail",
                        ],
                    },
                    {
                        "name": "Edit",
                        "url": "customer-update",
                    },
                    {
                        "name": "Delete",
                        "url": "customer-delete",
                    },
                ],
            },
        }
