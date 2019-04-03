#!/bin/bash

. ~/.virtualenvs/django-unit-test-sample/bin/activate

pip_install_confirm() {
    read -r -p "${1:-Install pip libraries from requirements.txt will begin. Are you sure? [y/N]} " response
    case "$response" in
        [yY][eE][sS]|[yY])
            true
            pip install -r requirements.txt
            echo "Installing Django requirements process success."
            ;;
        *)
            false
            echo "Bootstrap process canceled."
            ;;
    esac
}

migration_confirm() {
    read -r -p "${1:-Django migration process will begin. Are you sure? [y/N]} " response
    case "$response" in
        [yY][eE][sS]|[yY])
            true
            python manage.py makemigrations
            python manage.py migrate
            echo "Django Migration Model process success."
            ;;
        *)
            false
            echo "Bootstrap process canceled."
            ;;
    esac
}

add_admin_confirm() {
    read -r -p "${1:-It will add Django admin user. Are you sure? [y/N]} " response
    case "$response" in
        [yY][eE][sS]|[yY])
            true
            read -p 'Username: ' username_var
            read -p 'Email Address: ' email_var
            while true; do
                read -s -p "Password: " password_1
                echo
                read -s -p "Password (again): " password_2
                echo
                [ "$password_1" = "$password_2" ] && break
                echo "Please try again"
            done
            echo "from django.contrib.auth.models import User; User.objects.create_superuser('"$username_var"', '"$email_var"', '"$password_1"')" | python manage.py shell
            echo "Django Registering admin user process success."
            ;;
        *)
            false
            echo "Bootstrap process canceled."
            ;;
    esac
}

collect_static_confirm() {
    read -r -p "${1:-It will run collectstatic command. Are you sure? [y/N]} " response
    case "$response" in
        [yY][eE][sS]|[yY])
            true
            python manage.py collectstatic --noinput
            echo "Django collect static process success."
            ;;
        *)
            false
            echo "Bootstrap process canceled."
            ;;
    esac
}

pip_install_confirm
migration_confirm
add_admin_confirm
collect_static_confirm