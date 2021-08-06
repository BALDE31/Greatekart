from django.contrib import admin
from .models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}

    ordering = ['id']
    list_display = ('category_name', 'slug',)
    
    """
    readonly_fields = ('last_login', 'date_joined')
    filter_horizontal = ()
    list_filter = ['last_name', 'username']
    search_fields = ['last_name', 'first_name', 'email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('last_name', 'first_name', 'username')}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superadmin', 'is_admin')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    """
    


#admin.site.register(Category)

