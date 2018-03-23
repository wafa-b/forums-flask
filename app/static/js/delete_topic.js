<script>
    $(function ()
    {
        $(".delete").submit(function (event)
        {
            var id = event.target.id;
            alert("id = "+id);
                };
            $.ajax({
                type: "DELETE",
                url: "/api/topic/delete" + id,
                dataType: "json",
                success: function (response)
                    {
                        alert("Delete topic successfully !");
                        window.location.href = '/';
                    }
                });


        });
    });


</script>
