document.addEventListener('DOMContentLoaded', function() {
    if (typeof django !== 'undefined' && django.jQuery) {
        (function($) {
            $(document).ready(function() {
                $('input[name="is_active"]').change(function() {
                    if (!confirm('Ви дійсно бажаєте змінити статус активності?')) {
                        $(this).prop('checked', !$(this).prop('checked'));
                    }
                });
            });
        })(django.jQuery);
    } else {
        console.error('django.jQuery is not available.');
    }
});