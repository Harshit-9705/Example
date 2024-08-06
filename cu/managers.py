from django.contrib.auth.base_user import BaseUserManager

class CustomManagers(BaseUserManager):
    def create_user(self,phone_num,password=None,**extra_fields):

        if not phone_num:
            raise ValueError("Phone Number is required")

        use = self.model(phone_num=phone_num,**extra_fields)
        use.set_password(password)
        use.save(using = self.db)
        return use
    
    def create_superuser(self,phone_num,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)

        return self.create_user(phone_num,password,**extra_fields)



# from django.contrib.auth.base_user import BaseUserManager

# class CustomUserManager(BaseUserManager):
#     def create_user(self, phone_num, password=None, **extra_fields):
#         if not phone_num:
#             raise ValueError("Phone number is required")
        
#         user = self.model(phone_num=phone_num, **extra_fields)
#         user.set_password(password)  # Use set_password to handle password hashing
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, phone_num, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
        
#         return self.create_user(phone_num, password, **extra_fields)




      
