from instapy import InstaPy

session = InstaPy(username="no_one_can_help_u", password="9128873233!!")
session.login()

session.set_do_comment(enabled=True, percentage=100)

session.set_comment("Kaise hain aap? Sab bdhiya hai!")

session.join_group_chat("SHANSKARI_BALAK👻💯")

while True:
    session.watch_group_chat()
    if session.new_message():
        session.reply_to_message()
