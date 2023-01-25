class DisabledFormMixin:
    disabled_fields = ()
    fields = {}

    def _disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
