
class FormClosed(Exception):

    def __init__(self, form_id: int):
        self.form_id = form_id


class FormDoesNotExist(Exception):

    def __init__(self, form_id: int):
        self.form_id = form_id


class QuestionDoesNotBelongToForm(Exception):

    def __init__(self, form_id: int, question_id: int):
        self.form_id = form_id
        self.question_id = question_id


class InvalidUserResponseSubmit(Exception):

    def __init__(self, question_id: int, option_id: int):
        self.option_id = option_id
        self.question_id = question_id

