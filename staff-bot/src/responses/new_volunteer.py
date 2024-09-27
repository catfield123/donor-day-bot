class NewVolunteerResponses:
    ASK_FOR_FORWARDED_MESSAGE = "Перешлите сообщение пользователя, которого хотите назначить волонтёром\."
    
    OPERATION_CANCELED = (
        "Добавление волонтёра отменено\. \n" 
        "Если вы захотите добавить волонтёра, введите команду /new\_volunteer или отправьте текст `Назначить волонтёра`"
    )

    CANT_DETECT_FORWARDED_MESSAGE = (
        f"Не удаётся обнаружить переслоннаое сообщение от пользователя\. Повторите попытку\. \n\n"
        "Возможно, проблема в том, что у пользвателя в настройках приватности запрещено пересылать его сообщения\. "
        "Если это так, пожалуйста, попросите его выключить данную настройку или добавить вас в исключения\."
    )

    PLEASE_FORWARD_NOT_FROM_BOT = "Пожалуйста, перешлите сообщение от пользователя, которого хотите назначить волонтёром\. Сообщение, которое вы переслали было отправлено ботом, а не пользователем\. \."

    @staticmethod
    def get_confirm_text(message) -> str:
        full_name = message.forward_from.full_name.replace('.', '\\.')
        if message.forward_from.username:
            username_text = f"[{full_name}](https://t.me/{message.forward_from.username})"
        else:
            username_text = full_name
        return (
            f"Назначить {username_text} волонтёром? \n"
            "Пожалуйста, подтвердите ваше действие, нажав на одну из кнопок\. \n"
            "Если вы не уверены, вы можете отменить действие\."
        )
        
    VOLUNTEER_ASSIGNED = "Волонтёр назначен\. \n"
    


    