
    var product_json = '{{ product_json }}'
    console.log(product_json)
    if (product_json == "" || product_json == "{}") {
        product_json = {}
    } else {
        product_json = product_json.replaceAll('&quot;', '"')
        console.log(product_json)
        product_json = jQuery.parseJSON(product_json)
        console.log(product_json)
    }
    var prod_arr = {}
    if (Object.keys(product_json).length > 0) {
        Object.keys(product_json).map(k => {
            prod_arr[product_json[k].id] = product_json[k]
        })
    }

    function calc() {
        var sub_total = 0;
        var grand_total = 0;
        $('#POS-field table tbody tr').each(function() {
            price = $(this).find('[name="price[]"]').val()
            qty = $(this).find('[name="qty[]"]').val()
            qty = qty > 0 ? qty : 0
            total = parseFloat(price) * parseFloat(qty)
            $(this).find('.product_total').text(parseFloat(total).toLocaleString('en-US'))
            sub_total += parseFloat(total)
        })
        tax = $('[name="tax"]').val()
        tax = tax / 100;
        var tax_amount = parseFloat(sub_total) * parseFloat(tax);
        $('#tax_amount').text(parseFloat(tax_amount).toLocaleString('en-US'))
        $('[name="tax_amount"]').val(parseFloat(tax_amount))
        $('#grand_total').text(parseFloat(sub_total).toLocaleString('en-US'))
        $('[name="grand_total"]').val(parseFloat(sub_total))
        $('#sub_total').text(parseFloat(sub_total).toLocaleString('en-US'))
        $('[name="sub_total"]').val(parseFloat(sub_total))

    }
    $(function() {
        $('#product-id').select2({
            placeholder: "Please Select Product here",
            width: '100%'
        })
        $('#add_item').click(function() {
            var id = $('#product-id').val()
            var qty = $('#product-qty').val()
            console.log(id, qty)
            if (id == '' || qty == '' || id == null || qty == null) {
                alert("Product and Quantity Field is required!")
                return false
            }
            if (!!prod_arr[id]) {
                if ($('#POS-field table tbody input[name="product_id[]"][value="' + id + '"]').length > 0) {
                    alert('Item Already in the List.')
                    return false;
                }
                data = prod_arr[id]
                var tr = $($('noscript#item-clone').html()).clone()
                tr.find('[name="qty[]"]').val(qty)
                tr.find('[name="product_id[]"]').val(id)
                tr.find('[name="price[]"]').val(data.price)
                tr.find('.product_name').text(data.name)
                tr.find('.product_price').text(parseFloat(data.price).toLocaleString('en-US'))
                tr.find('.product_total').text(parseFloat(data.price * qty).toLocaleString('en-US'))
                $('#POS-field table tbody').append(tr)
                $('#product-id').val('').trigger('change')
                $('#product-qty').val(1)
                calc()
                tr.find('[name="qty[]"]').on('input keypress keyup keydown', function() {
                    calc()
                })
                tr.find('.rem-item').click(function() {
                    if (confirm("Are you sure to remove " + data.name + " product form list?") == true) {
                        tr.remove()
                        calc()
                    }
                })
            } else {
                alert("Undefined Product");
            }
        })
        $('[name="tax"]').on('input keypress keydown keyup', function() {
            calc()
        })
        $('#check_out').click(function() {
            if ($('#POS-field table tbody tr').length <= 0) {
                alert("Add atleast 1 product first!")
                return false;
            }
            uni_modal("Checkout", "{% url 'checkout-modal' %}?grand_total=" + $('[name="grand_total"]').val())
        })
        $('#pos-form').submit(function(e) {
            e.preventDefault();
            var _this = $(this)
            $('.err-msg').remove();
            var el = $('<div>')
            el.addClass("alert alert-danger err-msg")
            el.hide()
            if (_this[0].checkValidity() == false) {
                _this[0].reportValidity();
                return false;
            }
            start_loader();
            $.ajax({
                headers: {
                    "X-CSRFToken": '{{csrf_token}}'
                },
                url: "{% url 'save-pos' %}",
                data: new FormData($(this)[0]),
                cache: false,
                contentType: false,
                processData: false,
                method: 'POST',
                type: 'POST',
                dataType: 'json',
                error: err => {
                    console.log(err)
                    end_loader();
                },
                success: function(resp) {
                    if (typeof resp == 'object' && resp.status == 'success') {
                        el.removeClass("alert alert-danger err-msg")
                            // location.reload()
                        uni_modal("Receipt", "{% url 'receipt-modal' %}?id=" + resp.sale_id)
                        $('#uni_modal').on('hide.bs.modal', function() {
                            location.reload()
                        })
                    } else if (resp.status == 'failed' && !!resp.msg) {
                        el.text(resp.msg)
                    } else {
                        el.text("An error occured", 'error');
                        end_loader();
                        console.err(resp)
                    }
                    _this.prepend(el)
                    el.show('slow')
                    $("html, body, .modal").scrollTop(0);
                    end_loader()
                }
            })
        })
    })
