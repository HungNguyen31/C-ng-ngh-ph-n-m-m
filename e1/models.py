from django.db import models

class Student(models.Model):  # Tên lớp nên viết hoa chữ cái đầu
    name = models.CharField(max_length=255)  # Tên sinh viên
    gender = models.BooleanField()  # Giới tính (True/False)
    birth_day = models.DateField()  # Ngày sinh (chỉnh sửa từ DataField thành DateField)

    def __str__(self):
        return self.name  # Hiển thị tên trong admin

class Course(models.Model):
    name = models.CharField(max_length=50)  # Tên khóa học
    year = models.IntegerField(default=2025)
    start_date = models.DateField()  # Ngày bắt đầu
    end_date = models.DateField()  # Ngày kết thúc
    active = models.BooleanField(default=True)  # Trường active

    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date})"  # Hiển thị tên khóa học kèm ngày bắt đầu và kết thúc
