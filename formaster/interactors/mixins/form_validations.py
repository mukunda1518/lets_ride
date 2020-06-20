from formaster.exceptions.exceptions import FormClosed


class FormValidationMixin:

    def validate_for_live_form(self, form_id: int):
        is_form_live = self.storage.get_form_status(form_id)
        is_form_closed = not is_form_live

        if is_form_closed:
            raise FormClosed(form_id)