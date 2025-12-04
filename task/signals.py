from django.db.models.signals import post_save, m2m_changed, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from task.models import Task, TaskDetail


@receiver(m2m_changed, sender=Task.assigned_to.through)
def notify_employees_on_assignment(sender, instance, action, **kwargs):

    if action == 'post_add':
        assigned_emails = [emp.email for emp in instance.assigned_to.all()]

        if assigned_emails:
            send_mail(
                subject='New Task Assigned',
                message=f'You have been assigned a new task: {instance.title}',
                from_email='arafatsojib2020@gmail.com',
                recipient_list=assigned_emails,
                fail_silently=False,
            )

@receiver(post_delete, sender=Task)
def delete_associate_details(sender, instance, **kwargs):
    try:
        details = instance.details     
        if details.id:                
            details.delete()
    except TaskDetail.DoesNotExist:
        pass   