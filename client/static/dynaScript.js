$(document).ready(() => {
    function dynaFilters() {
        return new Promise((reject, resolve) => {
            let project = document.getElementById('project');
            let filter_by = $('#filter_by');

            if (project.value !== 'CUST') {
                filter_by.empty().append(`<option value="fix_version">Fix Version</option>`);
            } else {
                filter_by.empty().append(`<option value="latest_version">Latest Version</option>`);
            }
            resolve();
        })
    }

    $('#project').on('change', () => {
        dynaFilters();
    });

    dynaFilters();
});
