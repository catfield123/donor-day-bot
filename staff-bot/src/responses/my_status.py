class MyStatusResponses:
    @staticmethod
    def generate_my_status_response(is_admin: bool = False, is_volunteer: bool = False) -> str:
        response = "**Ваш статус**\: \n"
        if is_admin:
            response += "Администратор\n"
        else:
            response += "Не администратор\n"
        if is_volunteer:
            response += "Волонтёр\n\n"
        else:
            response += "Не волонтёр\n\n"

        if is_admin or is_volunteer:
            response += "Список доступных вам команд вы можете посмотреть с помощью /help\n"
        else:
            response += "Чтобы поменять статус, пожалуйста, свяжитесь с администратором\.\n"

        return response