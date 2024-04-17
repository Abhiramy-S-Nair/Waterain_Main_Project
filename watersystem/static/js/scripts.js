document.addEventListener('DOMContentLoaded', function () {
    const updateAddressButton = document.getElementById('update-address-button');
    const updateAddressForm = document.getElementById('update-address-form');

    updateAddressButton.addEventListener('click', function () {
        toggleUpdateAddressForm();
    });

    function toggleUpdateAddressForm() {
        if (updateAddressForm.style.display === "none") {
            updateAddressForm.style.display = "block";
        } else {
            updateAddressForm.style.display = "none";
        }
    }

    function updateAddress() {
        var formData = new FormData(document.getElementById("update-address-form"));
        fetch("/update-address/", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
        })
        .then(response => response.json())
        .then(data => {
            // Handle response data (e.g., display success message)
        })
        .catch(error => {
            console.error("Error updating address:", error);
        });
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            var cookies = document.cookie.split(";");
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
