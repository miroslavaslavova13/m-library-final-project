class DisabledFormMixin:
    disabled_fields = ()
    fields = {}

    def _disable_fields(self):
        if self.disabled_fields == "__all__":
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
