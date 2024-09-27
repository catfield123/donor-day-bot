

class HelpResponses:

    BASE_HELP_RESPONSE = (
        "Этот бот предназначен для изменения статуса донора волонтёром после звонка потенциальному донору, а также для рассылки сообщений донорам\.\n\n"
    )

    @staticmethod
    def generate_full_help_response(is_admin: bool = False, is_volunteer: bool = False) -> str:
        response = HelpResponses.BASE_HELP_RESPONSE
        if is_admin:
            response += (
                "**Доступные вам как администратору команды**\: \n"
                "/new\_volunteer — назначить волонтёра\n"
                "/send\_message — отправить рассылку донорам\n\n"
            )
        if is_volunteer:
            response += (
                "**Доступные вам как волонтёру команды**\: \n"
                "/change\_donor\_status — изменить статус донора \n"
            )

        if not is_admin and not is_volunteer:
            response += (
                "Этим ботом могут пользоваться только администраторы и волонтёры\.\n\n"
                "Чтобы поменять статус, пожалуйста, свяжитесь с администратором\.\n\n"
            )

        return response