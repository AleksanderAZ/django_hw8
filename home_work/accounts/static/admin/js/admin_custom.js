(function($) {
    $(document).ready(function() {
            $('input[name="is_active"]').change(
                function() {
                    if (!confirm('Змінити статус активності')) {
                        $(this).prop('checked', !$(this).prop.('checked'));
                    }
                }
            );
    });
});
