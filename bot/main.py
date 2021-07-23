import bot
import db

from time import sleep

final_respose = "Спасибо, вопросов больше нет."
attempts_allowed = 2  # attempts


def create_massage(telegram_id):
    """Creating text for message."""
    question_id = db.check_for_questionid_db(telegram_id)
    if question_id <= db.get_amout_of_questions_db():
        question = db.look_for_question_db(question_id)
        if db.get_attempt(telegram_id) > attempts_allowed:
            return question.upper()
        return question
    return final_respose


def main():
    try:
        data = bot.get_updates_json(bot.url)
        if db.check_last_updateid_db() is None:
            update_id = bot.last_update(data)['update_id'] - 1
        else:
            update_id = db.check_last_updateid_db()
        while True:
            if int(update_id) != bot.last_update(data)['update_id']:
                print(f'We have a new massage!\n'
                      f'from: {bot.get_username(bot.last_update(data))} \n'
                      f'id: {bot.get_telegramid(bot.last_update(data))}')
                for message in data['result']:
                    message_id = str(message['update_id'])
                    if db.check_on_update_db(message_id) is None:
                        username = bot.get_username(message)
                        telegram_id = bot.get_telegramid(message)
                        # adding message id into db
                        db.add_update_id_db(message_id)
                        # checking for user in db
                        if db.check_for_user_db(telegram_id, username) is None:
                            db.save_user_db(telegram_id, username)
                        # compering answer with variants
                        question_id = db.check_for_questionid_db(telegram_id)
                        answers = db.get_variants_of_answers_db(question_id)
                        answer = bot.get_message(message)
                        if answer in answers:
                            print('saving answer!')
                            answer_id = db.get_answer_id_db(answer)
                            # adding user answer into db
                            db.save_answer_db(telegram_id, question_id, answer_id)
                            # updating question id in user instance
                            db.update_questionid_userinstance_db(telegram_id, question_id)
                            question_id = db.check_for_questionid_db(telegram_id)
                            answers = db.get_variants_of_answers_db(question_id)
                        else:
                            attempt = db.get_attempt(telegram_id)
                            db.add_attempt(telegram_id, attempt)
                        # sending massage
                        chat_id = bot.get_chat_id(message)
                        question = create_massage(telegram_id)
                        # creating a message body
                        question_and_variants = question + "\n" + "\n".join(
                            i.capitalize() for i in answers
                        )
                        bot.send_message(chat_id, question_and_variants)
                        update_id = db.check_last_updateid_db()
            else:

                data = bot.get_updates_json(bot.url)
            sleep(3)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
