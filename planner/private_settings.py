import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'hqm16_3@bmmi1bx@+a(+1lupqy(!y^4yv=e(d^p!m-ny&)$mqf')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'plannerapp',
        'USER': 'Catfish',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# 이메일 전송 관련 설정
EMAIL = {
    'EMAIL_BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
    'EMAIL_PORT': 587,        # 구글 SMTP 포트번호
    'EMAIL_USE_TLS': True,
    'EMAIL_HOST': "smtp.gmail.com",               # 이메일 전송 호스트 설정
    'EMAIL_HOST_USER': 'tom9744@dgu.ac.kr',   # 이메일 발송 이메일 계정
    'EMAIL_HOST_PASSWORD': 'yang4972@',          # 이메일 발송 이메일 계정의 비밀번호
    'SERVER_EMAIL': 'Gmail ID',
}

# AWS 서비스 KEY
AWS_ACCESS_KEY_ID = 'AKIA55OYZP3MZFKC7HSY'
AWS_SECRET_ACCESS_KEY = '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'
