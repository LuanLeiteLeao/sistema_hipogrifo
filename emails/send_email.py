from django.core.mail import send_mail
from django.conf import settings
# variavel global para mandar e-mail
is_send_email=True
is_email_send_yourself=True


def enviar(subject,message,email):
    # caso seja para enviar para si mesmo
    if is_email_send_yourself:
        email = settings.EMAIL_HOST_USER 
    #caso seja para enviar 
    if is_send_email:
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
    # caso n seja, ele vai printar na tela oque iria se enviado
    else:
        print(subject + '\n' + message)


def confirmacao_novo_cadastro_pessoa(nome,nova_senha,email):
    subject = 'Nova Senha Sistema Hipogrifo'
    message = 'olá senhor(a) {} a sua nova senha é {}\n'.format(nome,nova_senha)
    enviar(subject, message, email)

    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['test.email.desenvolvimento@gmail.com',]
    # send_mail( subject, message, email_from, recipient_list )
